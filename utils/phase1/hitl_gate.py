"""
M2.2 HITL gate service — grant files + irreversible action checks.
Public-record ceiling immutable. H7 never grantable.
"""
from __future__ import annotations
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

DEFAULT_GRANT_PATHS = [
    Path("vault/hitl/active_grant.json"),
    Path("vault/MAIN_INVESTIGATION_1953_TRUST_ENGORON_ROD/00_HITL_AND_INDEX/active_grant.json"),
]

# Actions always blocked regardless of grant
ALWAYS_BLOCKED: Set[str] = {
    "H7",
    "barrier_bypass",
    "credential_abuse",
    "login_walled",
    "paywall_bypass",
    "captcha_evasion",
    "auth_bypass",
    "private_account",
    "illegal_scrape",
    "restricted_fulltext",
    "csam",
    "social_engineering",
}

# Map action labels → matrix IDs
ACTION_TO_ID = {
    "bulk_harvest": "H1",
    "full_ocr_campaign": "H2",
    "drive_large_upload": "H3",
    "git_force": "H4",
    "new_scope": "H5",
    "tag_upgrade_rock_solid": "H6",
    "non_public": "H7",
    "publish_external": "H8",
    "person_deep_pass": "H9",
    "pacer_paid": "H10",
    "contact_third_party": "H11",
    "amend_method": "H12",
    "promote_theory": "H13",
    "gdpr_bulk": "H14",
    "public_deploy": "H15",
    "swarm_run": "A10",
    "rag_ingest": "A5",
    "dual_persist": "A5",
    "public_search": "A1",
    "phase_build": "PHASE2_BUILD",
}


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _parse_ts(s: str) -> Optional[datetime]:
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return None


class HITLGate:
    def __init__(self, grant_path: Optional[Path] = None):
        self.grant_path = Path(grant_path) if grant_path else None
        self._grant: Optional[Dict[str, Any]] = None
        self.reload()

    def reload(self) -> bool:
        paths: List[Path] = []
        if self.grant_path:
            paths.append(self.grant_path)
        env = os.getenv("HITL_GRANT_PATH")
        if env:
            paths.append(Path(env))
        paths.extend(DEFAULT_GRANT_PATHS)
        for p in paths:
            if p.exists():
                try:
                    self._grant = json.loads(p.read_text(encoding="utf-8"))
                    self.grant_path = p
                    return True
                except Exception:
                    continue
        self._grant = None
        return False

    def active(self) -> bool:
        g = self._grant
        if not g or g.get("status") != "ACTIVE":
            return False
        exp = _parse_ts(str(g.get("expiry_utc") or ""))
        if not exp:
            return False
        return _utc_now() < exp.astimezone(timezone.utc)

    def grant_info(self) -> Dict[str, Any]:
        g = dict(self._grant or {})
        g["is_active"] = self.active()
        g["checked_at"] = _utc_now().isoformat().replace("+00:00", "Z")
        g["grant_path"] = str(self.grant_path) if self.grant_path else None
        return g

    def classes(self) -> Set[str]:
        if not self.active():
            return set()
        raw = (self._grant or {}).get("granted_classes") or []
        return set(str(x) for x in raw)

    def check(self, action: str, *, irreversible: bool = False, meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Returns {allowed, hitl_required, reason, matrix_id, grant_id}.
        """
        action_key = (action or "").strip().lower().replace(" ", "_")
        matrix_id = ACTION_TO_ID.get(action_key, action_key.upper() if action_key.startswith("h") else action_key)

        # Absolute ceiling
        if matrix_id in ALWAYS_BLOCKED or action_key in ALWAYS_BLOCKED:
            return {
                "allowed": False,
                "hitl_required": False,
                "reason": "ALWAYS_BLOCKED_public_record_ceiling",
                "matrix_id": "H7",
                "grant_id": (self._grant or {}).get("grant_id"),
                "active_grant": self.active(),
            }

        # Autonomous classes when grant active
        classes = self.classes()
        if self.active():
            # A-class and phase build always ok under active grant
            if matrix_id.startswith("A") or matrix_id in classes or action_key in {c.lower() for c in classes}:
                return {
                    "allowed": True,
                    "hitl_required": False,
                    "reason": "covered_by_active_grant",
                    "matrix_id": matrix_id,
                    "grant_id": (self._grant or {}).get("grant_id"),
                    "active_grant": True,
                }
            # Prior reaffirmed scopes
            prior = set((self._grant or {}).get("prior_scopes_reaffirmed") or [])
            if any(matrix_id in p or action_key in p.lower() for p in prior):
                return {
                    "allowed": True,
                    "hitl_required": False,
                    "reason": "prior_scope_reaffirmed",
                    "matrix_id": matrix_id,
                    "grant_id": (self._grant or {}).get("grant_id"),
                    "active_grant": True,
                }

        # Explicit H-gates without active covering grant
        if matrix_id.startswith("H") or irreversible:
            return {
                "allowed": False,
                "hitl_required": True,
                "reason": "explicit_hitl_required",
                "matrix_id": matrix_id,
                "grant_id": (self._grant or {}).get("grant_id"),
                "active_grant": self.active(),
                "how_to_authorize": f"HITL=YES {matrix_id} [scope]",
            }

        # Default: require HITL if config says so and no grant
        return {
            "allowed": self.active(),
            "hitl_required": not self.active(),
            "reason": "active_grant" if self.active() else "no_active_grant",
            "matrix_id": matrix_id,
            "grant_id": (self._grant or {}).get("grant_id"),
            "active_grant": self.active(),
        }


_default: Optional[HITLGate] = None


def get_hitl_gate() -> HITLGate:
    global _default
    if _default is None:
        _default = HITLGate()
    return _default


def require_hitl_gate(action: str, **kwargs) -> Dict[str, Any]:
    return get_hitl_gate().check(action, **kwargs)
