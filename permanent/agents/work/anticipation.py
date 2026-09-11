"""Anticipation — risks + autopilot suggest (self-directed)."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY
from utils.autopilot import AutopilotQueue


class AnticipationAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or ""
        self.log(f"Anticipate: {q[:80]}")
        risks = REGISTRY.call("risk_list", query=q)
        ap = REGISTRY.call("autopilot_suggest", n=3)
        # self-directed: enqueue follow-up
        queue = AutopilotQueue()
        prop = queue.enqueue(f"Follow-up public sources for: {q[:100]}", source="Anticipation", priority=4)
        return {
            "status": "ok",
            "risks": risks,
            "autopilot": ap,
            "enqueued": prop,
            "self_directed": True,
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
