"""Overseer — constitution, ceiling, escalation. Always online."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import public_ceiling_check

class OverseerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        phase = task.get("phase", "pre")
        goal = task.get("goal", "")
        self.log(f"Overseer phase={phase}")
        ceiling = public_ceiling_check(goal) if goal else {"allowed": True, "reason": "no goal"}
        if not ceiling["allowed"]:
            self.monitor.raise_flag("ceiling_breach", ceiling["reason"], severity="crit")
            return {"status": "blocked", "phase": phase, "ceiling": ceiling, "escalate": True}
        # Affirm permanent swarm policy
        policy = {
            "permanent_swarm": self.config.permanent_swarm,
            "never_bypass_supervisor": self.config.never_bypass_supervisor,
            "public_record_ceiling": self.config.public_record_ceiling,
            "hitl_required": self.config.hitl_required,
        }
        return {
            "status": "ok",
            "phase": phase,
            "ceiling": ceiling,
            "policy": policy,
            "sign_off": phase == "post",
        }
