"""
M1.2 Barrier classifier — Input barrier type → lawful route enum.
Routes: FOIA / ATIP / library / public / HITL / blocked
Never bypasses. Metadata-only decisions.
"""
from __future__ import annotations
import re
from enum import Enum
from typing import Any, Dict, List, Optional


class LawfulRoute(str, Enum):
    PUBLIC = "public"           # openly published web / gov portal
    FOIA = "foia"               # US Freedom of Information Act
    ATIP = "atip"               # Canada Access to Information
    LIBRARY = "library"         # public library / archive / PAC
    COURT_PUBLIC = "court_public"
    REGISTRY = "registry"       # property / business / SOS / EDGAR
    HITL = "hitl"               # requires human approval
    BLOCKED = "blocked"         # out of policy / private / illegal


# Keyword heuristics (metadata-only; no payload scraping)
_PUBLIC_HINTS = re.compile(
    r"\b(public\s+record|press\s+release|open\s+data|gov\.|federal\s+register|"
    r"official\s+gazette|whitehouse\.gov|justice\.gov|sec\.gov|edgar|"
    r"foia\.gov|opengov|data\.gov)\b",
    re.I,
)
_FOIA_HINTS = re.compile(
    r"\b(foia|freedom\s+of\s+information|agency\s+record|20\s+working\s+days|"
    r"department\s+of\s+(justice|state|defense)|federal\s+agency)\b",
    re.I,
)
_ATIP_HINTS = re.compile(
    r"\b(atip|access\s+to\s+information|privacy\s+act|canada\.ca|gc\.ca|"
    r"british\s+columbia|ontario|quebec|federal\s+canadian)\b",
    re.I,
)
_LIBRARY_HINTS = re.compile(
    r"\b(library|archive\.org|internet\s+archive|chronicling\s+america|"
    r"newspaper|public\s+library|catalog|worldcat|loc\.gov)\b",
    re.I,
)
_COURT_HINTS = re.compile(
    r"\b(court|docket|pacer|case\s+no|judgment|opinion|scotus|circuit|"
    r"superior\s+court|district\s+court)\b",
    re.I,
)
_REGISTRY_HINTS = re.compile(
    r"\b(property\s+deed|acris|recorder|assessor|sos|secretary\s+of\s+state|"
    r"business\s+entity|corporation\s+search|land\s+title|parcel)\b",
    re.I,
)
_BLOCK_HINTS = re.compile(
    r"\b(password|login|credential|private\s+key|ssn|social\s+security|"
    r"medical\s+record|sealed|classified|paywall\s+bypass|captcha\s+evasion|"
    r"auth\s+bypass|scraping\s+behind)\b",
    re.I,
)
_HITL_HINTS = re.compile(
    r"\b(bulk\s+download|fee-paid|paid\s+access|irreversible|external\s+action|"
    r"send\s+email|file\s+request|submit\s+form|purchase)\b",
    re.I,
)


def classify_barrier(
    text: str,
    meta: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Classify input into a lawful route.
    Returns route enum value + confidence + reasons.
    """
    meta = meta or {}
    blob = f"{text} {json_dumps_safe(meta)}"
    reasons: List[str] = []
    scores: Dict[str, float] = {r.value: 0.0 for r in LawfulRoute}

    if _BLOCK_HINTS.search(blob):
        scores[LawfulRoute.BLOCKED.value] += 10
        reasons.append("blocked_pattern")
    if _HITL_HINTS.search(blob):
        scores[LawfulRoute.HITL.value] += 5
        reasons.append("hitl_pattern")
    if _FOIA_HINTS.search(blob):
        scores[LawfulRoute.FOIA.value] += 4
        reasons.append("foia_pattern")
    if _ATIP_HINTS.search(blob):
        scores[LawfulRoute.ATIP.value] += 4
        reasons.append("atip_pattern")
    if _LIBRARY_HINTS.search(blob):
        scores[LawfulRoute.LIBRARY.value] += 3
        reasons.append("library_pattern")
    if _COURT_HINTS.search(blob):
        scores[LawfulRoute.COURT_PUBLIC.value] += 3
        reasons.append("court_pattern")
    if _REGISTRY_HINTS.search(blob):
        scores[LawfulRoute.REGISTRY.value] += 3
        reasons.append("registry_pattern")
    if _PUBLIC_HINTS.search(blob):
        scores[LawfulRoute.PUBLIC.value] += 2
        reasons.append("public_pattern")

    # Default soft public if nothing strong
    if max(scores.values()) == 0:
        scores[LawfulRoute.PUBLIC.value] = 1.0
        reasons.append("default_public")

    # Hard block overrides
    if scores[LawfulRoute.BLOCKED.value] >= 5:
        route = LawfulRoute.BLOCKED
    else:
        route = LawfulRoute(max(scores, key=scores.get))

    confidence = min(1.0, scores[route.value] / 10.0)

    return {
        "route": route.value,
        "confidence": round(confidence, 3),
        "scores": scores,
        "reasons": reasons,
        "allowed": route != LawfulRoute.BLOCKED,
        "hitl_required": route in (LawfulRoute.HITL, LawfulRoute.FOIA, LawfulRoute.ATIP)
        or confidence < 0.3,
    }


def json_dumps_safe(obj: Any) -> str:
    import json
    try:
        return json.dumps(obj, default=str)
    except Exception:
        return str(obj)
