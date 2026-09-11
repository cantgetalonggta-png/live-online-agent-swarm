"""Planner — decompose goals into parallel/sequential steps."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class PlannerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        self.log(f"Planning for: {goal[:120]}")
        plan = {
            "goal": goal,
            "parallel_work": [
                {"agent": "Researcher", "task": {"query": goal, "mode": "public"}},
                {"agent": "Investigator", "task": {"query": goal, "mode": "leads"}},
                {"agent": "OSINTCollector", "task": {"query": goal, "mode": "public_search"}},
                {"agent": "LiveWebScout", "task": {"query": goal, "mode": "live"}},
                {"agent": "Pattern", "task": {"query": goal}},
                {"agent": "Anticipation", "task": {"query": goal}},
            ],
            "sequential": [
                "TruthVerifier",
                "MemoryVault",
                "Teacher",
                "Synthesizer",
                "Auditor",
            ],
            "bounds": {
                "max_parallel": self.config.max_parallel_work,
                "max_steps": self.config.max_agent_steps,
            },
        }
        return {"status": "planned", "plan": plan}
