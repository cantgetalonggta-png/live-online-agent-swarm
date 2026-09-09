"""
Compliance Agent — continuous enforcement of legal-osint-compliance-layer + sensitive-data-defensive-scan.
"""
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import require_hitl

class ComplianceAgent(BaseAgent):
    def __init__(self, monitor, vault):
        super().__init__("Compliance", monitor, vault)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("checking")
        action = task.get("action", "pre_check")
        goal = task.get("goal", "")

        # Hard rules
        forbidden = ["private data", "credential pack", "hack", "unauthorized access", "scrape login"]
        for f in forbidden:
            if f in goal.lower():
                self.log(f"BLOCKED: detected forbidden pattern '{f}'")
                self.set_status("blocked")
                return {
                    "allowed": False,
                    "reason": f"Violates absolute rule: no {f}",
                    "hitl": True
                }

        # Always require HITL for bulk or external
        if "bulk" in goal.lower() or "export" in goal.lower() or "ingest" in goal.lower():
            self.log("HITL required for bulk/ingest action")
            self.set_status("awaiting_hitl")
            return {
                "allowed": True,
                "hitl_required": True,
                "notice": require_hitl(goal),
                "reason": "Bulk or ingest action needs human confirmation"
            }

        self.log("Compliance gate passed (public-record ceiling intact)")
        self.set_status("idle")
        return {"allowed": True, "hitl_required": self.config.hitl_required}
