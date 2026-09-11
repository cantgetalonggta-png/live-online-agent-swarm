"""Append-only audit log."""
from __future__ import annotations
import hashlib
import json
import time
from pathlib import Path
from typing import Any, Dict

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
