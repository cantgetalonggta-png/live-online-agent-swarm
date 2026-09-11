"""Planner — decompose + cost bounds via wired tools."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class PlannerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        self.log(f"Plan: {goal[:100]}")
        plan = REGISTRY.call("decompose", goal=goal)
        bounds = REGISTRY.call("cost_bounds", max_parallel=self.config.max_parallel_work)
        return {
            "status": "ok",
            "plan": plan,
            "bounds": bounds,
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
