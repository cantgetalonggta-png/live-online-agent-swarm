"""Teacher — explain findings; propose skill refinements (HITL apply)."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class TeacherAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        collected = task.get("collected", {})
        self.log("Teacher synthesizing lessons")
        lessons = [
            f"Goal framed as public research: {goal[:120]}",
            f"Work agents reporting: {list(collected.keys())}",
            "Skill proposals require HITL before apply.",
        ]
        proposals = [
            {
                "skill": "permanent-agent-swarm",
                "change": "Tune parallel_work roster per domain",
                "hitl_required": True,
            }
        ]
        return {"status": "ok", "lessons": lessons, "skill_proposals": proposals}
