"""Anticipation — forward risks / missing evidence."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class AnticipationAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query", "")
        self.log(f"Anticipate: {q[:100]}")
        return {
            "status": "ok",
            "query": q,
            "risks": ["incomplete public sources", "stale secondary reporting"],
            "next_public_sources": ["primary agency pages", "court dockets public", "FOIA reading rooms"],
        }
