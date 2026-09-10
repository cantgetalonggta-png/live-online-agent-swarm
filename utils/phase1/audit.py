"""
M1.3 Audit trail — append-only JSONL decision log.
Every /verify /rag /swarm decision is recorded with hash provenance.
PUBLIC_RECORD_CEILING + HITL respected.
"""
from __future__ import annotations
import json
import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, List
from threading import Lock

_LOCK = Lock()
DEFAULT_LOG = Path(os.getenv("AUDIT_LOG_PATH", "vault/audit/decisions.jsonl"))


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash_payload(payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


class AuditTrail:
    """Append-only JSONL audit logger."""

    def __init__(self, log_path: Optional[Path] = None):
        self.log_path = Path(log_path) if log_path else DEFAULT_LOG
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            self.log_path.touch()

    def record(
        self,
        actor: str,
        action: str,
        inputs: Any,
        decision: str,
        hitl_required: bool = False,
        meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        event = {
            "ts": _utc_now(),
            "actor": actor,
            "action": action,
            "inputs_hash": _hash_payload(inputs),
            "decision": decision,
            "hitl_required": hitl_required,
            "meta": meta or {},
        }
        line = json.dumps(event, default=str) + "\n"
        with _LOCK:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(line)
        return event

    def tail(self, n: int = 50) -> List[Dict[str, Any]]:
        if not self.log_path.exists():
            return []
        with open(self.log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        out = []
        for line in lines[-n:]:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return out

    def count(self) -> int:
        if not self.log_path.exists():
            return 0
        with open(self.log_path, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)


# Singleton convenience
_default: Optional[AuditTrail] = None


def get_audit() -> AuditTrail:
    global _default
    if _default is None:
        _default = AuditTrail()
    return _default
