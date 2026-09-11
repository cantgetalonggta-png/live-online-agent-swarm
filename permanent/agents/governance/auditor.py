"""Auditor — append-only decision log."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from utils.audit import AuditorLog

class AuditorAgent(BaseAgent):
    plane = "governance"

    def __init__(self, monitor, vault):
        super().__init__("Auditor", monitor, vault)
        self.logbook = AuditorLog(self.config.audit_path)

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        action = task.get("action", "seal")
        goal = task.get("goal", "")
        keys = task.get("results_keys", [])
        self.log(f"Audit {action}")
        event = self.logbook.write(
            actor="Auditor",
            action=action,
            inputs={"goal": goal, "results_keys": keys},
            decision="sealed" if action == "seal" else action,
            hitl_required=self.config.hitl_required,
        )
        return {"status": "ok", "event": event}
