"""Overseer — ceiling + self-control replan authority."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from utils.directives import public_ceiling_check
from tools.registry import REGISTRY


class OverseerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        phase = task.get("phase", "pre")
        goal = task.get("goal", "")
        self.log(f"Overseer {phase}: ceiling + self-control")
        ceil = REGISTRY.call("ceiling_check", goal=goal)
        if not ceil.get("allowed", True):
            self.monitor.raise_flag("ceiling", ceil.get("reason", "blocked"), "crit")
            return {"status": "blocked", "phase": phase, "ceiling": ceil}

        replan = None
        if phase == "post":
            # Self-control: if health flags or weak claims, propose replan
            health = self.monitor.health()
            flags = health.get("open_flags") or []
            snap = self.vault.snapshot()
            solid = (snap.get("by_status") or {}).get("SOLID", 0)
            total = snap.get("n_claims", 0) or 1
            if flags or (solid / total) < 0.2:
                replan = {
                    "action": "self_control_replan",
                    "reason": "weak solid ratio or open flags",
                    "suggested_next_goal": f"Public-source deep dive on: {goal[:80]}",
                    "hitl_required": False,  # internal replan ok; dissemination still HITL
                }
                REGISTRY.call(
                    "skill_propose",
                    skill="permanent-agent-swarm",
                    change="Increase live evidence weight for next run",
                    rationale=str(replan),
                    agent=self.name,
                )

        REGISTRY.call("policy_assert", permanent_swarm=True)
        REGISTRY.call("audit_write", event=f"overseer_{phase}", payload={"goal": goal[:120]})
        return {
            "status": "ok",
            "phase": phase,
            "ceiling": ceil,
            "self_control": True,
            "replan": replan,
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
