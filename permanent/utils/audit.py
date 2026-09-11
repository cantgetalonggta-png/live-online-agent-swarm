"""Append-only audit log."""
from __future__ import annotations
import hashlib
import json
import time
from pathlib import Path
from typing import Any, Dict, Optional

_DEFAULT = Path("vault/audit.jsonl")


class AuditorLog:
    def __init__(self, path: str = "vault/audit.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, actor: str, action: str, inputs: Dict[str, Any], decision: str, hitl_required: bool = False) -> Dict[str, Any]:
        blob = json.dumps(inputs, sort_keys=True, default=str)
        event = {
            "ts": time.time(),
            "actor": actor,
            "action": action,
            "inputs_hash": hashlib.sha256(blob.encode()).hexdigest()[:16],
            "decision": decision,
            "hitl_required": hitl_required,
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")
        return event


def append_audit(event: str, payload: Optional[Dict[str, Any]] = None, path: str = "vault/audit.jsonl") -> Dict[str, Any]:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    row = {"ts": time.time(), "event": event, "payload": payload or {}}
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, default=str) + "\n")
    return row
