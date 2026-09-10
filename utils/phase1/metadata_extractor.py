"""
M1.1 Metadata extraction pipeline.
Ingest public MD/CSV/text → schema-normalized entities.
Target ≥95% parse success on clean public metadata.
"""
from __future__ import annotations
import csv
import hashlib
import io
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse


ENTITY_TYPES = ("person", "org", "location", "document", "date", "identifier", "url", "claim")


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


# Lightweight regex extractors (no external NLP deps required for baseline)
_URL_RE = re.compile(r"https?://[^\s)>\"]+", re.I)
_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
_DATE_RE = re.compile(
    r"\b(?:\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4}|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})\b",
    re.I,
)
_ORG_HINT = re.compile(
    r"\b([A-Z][A-Za-z0-9&.\- ]{2,40}(?:Inc|LLC|Corp|Ltd|Company|Agency|Department|Bureau|Commission|Authority|Office))\b"
)
_PERSON_HINT = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b")
_ID_HINT = re.compile(r"\b(?:Case|Docket|File|Doc|Record|Parcel|EIN|CIK)[\s#:.-]*([A-Z0-9\-/]{4,})\b", re.I)


def extract_from_text(text: str, source: Optional[str] = None, doc_id: Optional[str] = None) -> Dict[str, Any]:
    """Extract schema-normalized entities from free text / markdown."""
    entities: List[Dict[str, Any]] = []
    seen = set()

    def add(etype: str, value: str, conf: float = 0.7, extra: Optional[dict] = None):
        key = (etype, value.lower().strip())
        if not value or key in seen:
            return
        seen.add(key)
        ent = {
            "type": etype,
            "value": value.strip(),
            "confidence": conf,
            "source": source,
            "hash": _hash(f"{etype}:{value}"),
        }
        if extra:
            ent.update(extra)
        entities.append(ent)

    for m in _URL_RE.finditer(text):
        url = m.group(0).rstrip(".,;")
        add("url", url, 0.95, {"host": urlparse(url).netloc})
    for m in _DATE_RE.finditer(text):
        add("date", m.group(0), 0.8)
    for m in _ID_HINT.finditer(text):
        add("identifier", m.group(0), 0.75)
    for m in _ORG_HINT.finditer(text):
        add("org", m.group(1), 0.65)
    # Persons: lower confidence, filter common false positives
    stop = {"The", "This", "That", "With", "From", "Into", "About", "After", "Before", "Under"}
    for m in _PERSON_HINT.finditer(text):
        name = m.group(1)
        if name.split()[0] not in stop and len(name) > 4:
            add("person", name, 0.55)

    # Simple claim lines (sentences with verbs of assertion)
    for line in text.splitlines():
        line = line.strip()
        if 40 < len(line) < 400 and re.search(r"\b(is|are|was|were|must|shall|states|reports)\b", line, re.I):
            add("claim", line[:300], 0.5)

    doc = {
        "doc_id": doc_id or _hash(text[:200]),
        "source": source,
        "extracted_at": _utc(),
        "char_count": len(text),
        "entity_count": len(entities),
        "entities": entities,
        "parse_success": True,
    }
    return doc


def extract_from_csv(content: str, source: Optional[str] = None) -> Dict[str, Any]:
    """Normalize CSV rows into entity-like records (header-aware)."""
    reader = csv.DictReader(io.StringIO(content))
    rows = []
    entities: List[Dict[str, Any]] = []
    try:
        for i, row in enumerate(reader):
            if i > 5000:  # safety cap
                break
            clean = {k: (v or "").strip() for k, v in row.items() if k}
            rows.append(clean)
            # Promote obvious columns
            for k, v in clean.items():
                kl = k.lower()
                if not v:
                    continue
                if "url" in kl or "link" in kl:
                    entities.append({"type": "url", "value": v, "confidence": 0.9, "row": i})
                elif "date" in kl or "time" in kl:
                    entities.append({"type": "date", "value": v, "confidence": 0.85, "row": i})
                elif "name" in kl or "party" in kl:
                    entities.append({"type": "person", "value": v, "confidence": 0.7, "row": i})
                elif "org" in kl or "company" in kl or "agency" in kl:
                    entities.append({"type": "org", "value": v, "confidence": 0.75, "row": i})
        success = True
    except Exception as e:
        success = False
        rows = []
        entities = [{"type": "error", "value": str(e), "confidence": 1.0}]

    return {
        "doc_id": _hash(content[:200]),
        "source": source,
        "extracted_at": _utc(),
        "format": "csv",
        "row_count": len(rows),
        "entity_count": len(entities),
        "entities": entities[:2000],
        "sample_rows": rows[:5],
        "parse_success": success,
    }


def extract(content: str, mime_hint: str = "text", source: Optional[str] = None, doc_id: Optional[str] = None) -> Dict[str, Any]:
    """Unified entry: choose text vs csv pipeline."""
    mime = (mime_hint or "text").lower()
    if "csv" in mime or (content.count(",") > 5 and content.count("\n") > 2 and "\t" not in content[:200]):
        # Heuristic CSV detect
        first = content.splitlines()[0] if content else ""
        if "," in first and not first.startswith("#"):
            return extract_from_csv(content, source=source)
    return extract_from_text(content, source=source, doc_id=doc_id)


def batch_success_rate(results: List[Dict[str, Any]]) -> float:
    if not results:
        return 0.0
    ok = sum(1 for r in results if r.get("parse_success"))
    return ok / len(results)
