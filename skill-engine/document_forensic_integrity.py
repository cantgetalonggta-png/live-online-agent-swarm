"""
Document Anti-Tamper Defuser + Lawful Evidentiary Orchestrator
Phase 2/3 Meridian — public-record forensic integrity only.
"""
from __future__ import annotations
import hashlib
import datetime
import re
from typing import Dict, Any, List, Optional

class DocumentAntiTamperDefuser:
    @staticmethod
    def calculate_stream_integrity(raw_content: bytes) -> str:
        return hashlib.sha256(raw_content).hexdigest()

    def audit_document_metadata(self, file_metadata: Dict[str, Any], declared_creation_date: str) -> Dict[str, Any]:
        declared_dt = datetime.datetime.strptime(declared_creation_date, "%Y-%m-%d")
        flags = []
        is_authentic = True
        sw = file_metadata.get("authoring_software_release_year")
        if sw and declared_dt.year < int(sw):
            flags.append("ANACHRONISM_DETECTED")
            is_authentic = False
        emb = file_metadata.get("pdf_producer_creation_timestamp")
        if emb:
            embedded_dt = datetime.datetime.strptime(emb, "%Y-%m-%d")
            if embedded_dt > declared_dt + datetime.timedelta(days=30):
                flags.append("RETROACTIVE_FORGERY_WARNING")
                is_authentic = False
        return {
            "is_metadata_authentic": is_authentic,
            "anomaly_logs": flags,
            "action_tag": "STABLE" if is_authentic else "REJECTED_AS_TAMPERED_OR_ANACHRONISTIC",
        }

    def hash_timeline_check(self, doc_id: str, raw_content: bytes, prior_hashes: Dict[str, list], at: str = "") -> Dict[str, Any]:
        h = self.calculate_stream_integrity(raw_content)
        history = prior_hashes.setdefault(doc_id, [])
        status = "FIRST_INGEST" if not history else ("UNCHANGED" if history[-1]["sha256"] == h else "MUTATED_POST_PUBLICATION")
        history.append({"sha256": h, "at": at})
        return {"doc_id": doc_id, "sha256": h, "status": status, "prior_sha256": history[-2]["sha256"] if len(history) > 1 else None}

    def redaction_structure_scan(self, pdf_text_sample: str, visual_redaction_claimed: bool) -> Dict[str, Any]:
        flags = []
        if visual_redaction_claimed and pdf_text_sample:
            markers = len(re.findall(r"\[REDACTED\]|████|blacked", pdf_text_sample, re.I))
            if markers == 0 and len(pdf_text_sample) > 200:
                flags.append("REDACTION_CLAIMED_BUT_NO_MARKERS_IN_TEXT_LAYER")
        return {"flags": flags, "action": "DUAL_STATE_DIFF" if flags else "OK"}

    def rhetorical_hedge_score(self, text: str) -> Dict[str, Any]:
        text = text or ""
        words = re.findall(r"[A-Za-z']+", text.lower())
        n = max(len(words), 1)
        passive = len(re.findall(r"\b(was|were|been|being)\s+\w+ed\b", text.lower()))
        hedge = len(re.findall(r"\b(may|might|could|appears?|seems?|suggests?|certain parameters|systematically observed)\b", text.lower()))
        defensive = (passive + hedge) / n > 0.08
        return {
            "passive_hits": passive,
            "hedge_hits": hedge,
            "defensive_posture_signal": defensive,
            "reliability_adjustment": -0.1 if defensive else 0.0,
            "note": "Soft signal only.",
        }


class LawfulEvidentiaryOrchestrator:
    def __init__(self, adverse_inference_threshold: float = 0.75):
        self.adverse_inference_threshold = adverse_inference_threshold

    def analyze(self, claim_id, public_registry, required_primaries, overclaim_terms=None, underclaim_note=""):
        disclosed = public_registry.get("disclosed_primaries", {})
        missing = [a for a in required_primaries if not disclosed.get(a, False)]
        pub = public_registry.get("core_claim", "").lower()
        overclaims = [t for t in (overclaim_terms or []) if t.lower() in pub]
        omission = len(missing) / max(len(required_primaries), 1)
        gates = []
        if missing: gates.append("M32")
        if omission >= self.adverse_inference_threshold: gates.append("M35")
        if overclaims: gates.extend(["M4", "M33", "M10"])
        if overclaims and omission >= self.adverse_inference_threshold:
            tag, verdict, warrant = "IRREGULARITY", "OVERCLAIM_PLUS_CRITICAL_OMISSION", "ESCALATE_TO_TARGETED_FOIA"
        elif overclaims:
            tag, verdict, warrant = "OVERSTATED", "PUBLIC_NARRATIVE_OVERCLAIMS_EVIDENCE", "REWRITE_CLAIM_TO_MATCH_PRIMARY"
        elif omission >= self.adverse_inference_threshold:
            tag, verdict, warrant = "CONTESTED", "CRITICAL_PRIMARY_OMISSION", "WATCHLIST_PRIMARY_HUNT"
        elif missing:
            tag, verdict, warrant = "CONTESTED", "PARTIAL_PRIMARY", "WATCHLIST_PRIMARY_HUNT"
        else:
            tag, verdict, warrant = "SOLID", "PRIMARIES_PRESENT_CLAIM_BOUNDED", "HOLD"
        return {
            "claim_id": claim_id,
            "tag": tag,
            "verdict": verdict,
            "missing_critical_tracks": missing,
            "overclaim_terms": overclaims,
            "omission_weight": round(omission, 3),
            "gates_fired": sorted(set(gates)),
            "actionable_warrant": warrant,
            "underclaim_note": underclaim_note,
            "legal_note": "Analytical only (M30).",
        }
