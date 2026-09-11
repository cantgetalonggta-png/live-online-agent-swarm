"""Teacher — explain + self-learning proposals (HITL apply)."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from utils.self_learning import SkillProposalQueue

class TeacherAgent(BaseAgent):
    plane = "work"

    def __init__(self, name, monitor, vault):
        super().__init__(name, monitor, vault)
        self.queue = SkillProposalQueue(self.config.audit_path.replace("audit.jsonl", "skill_proposals.jsonl"))

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        collected = task.get("collected", {})
        self.log("Teacher lessons + self-learning proposals")
        lessons = [
            f"Goal framed as public research: {goal[:120]}",
            f"Work agents reporting: {list(collected.keys())}",
            "Skill proposals require HITL before apply.",
        ]
        prop = self.queue.propose(
            skill="permanent-agent-swarm",
            change="Tune parallel_work roster per domain from this run",
            rationale=f"Run collected keys={list(collected.keys())}",
            agent=self.name,
        )
        return {
            "status": "ok",
            "lessons": lessons,
            "skill_proposals": [prop],
            "pending_queue_n": len(self.queue.list_pending()),
            "self_learning": True,
            "hitl_required_to_apply": True,
        }
