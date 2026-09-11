"""AutopilotDirector — self-directed goal picking (public ceiling)."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY
from utils.autopilot import AutopilotQueue


class AutopilotDirectorAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("AutopilotDirector self-directed pick")
        q = AutopilotQueue()
        nxt = q.next_goal()
        if not nxt:
            nxt = q.enqueue("Public FOIA response deadlines map", source="AutopilotDirector")
        REGISTRY.call("orchestrate", goal=nxt.get("goal", ""))
        return {
            "status": "ok",
            "next_goal": nxt,
            "queued_n": len(q.list_queued()),
            "self_directed": True,
            "public_ceiling": True,
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
