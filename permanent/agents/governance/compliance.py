"""Compliance — public-record + HITL pre-check."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import public_ceiling_check

class ComplianceAgent(BaseAgent):
    plane = "governance"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        self.log("Compliance pre_check")
        ceiling = public_ceiling_check(goal)
        allowed = ceiling.get("allowed", False) and self.config.public_record_ceiling
        return {
            "allowed": allowed,
            "reason": ceiling.get("reason", ""),
            "hitl_required": self.config.hitl_required,
            "public_record_ceiling": self.config.public_record_ceiling,
        }
