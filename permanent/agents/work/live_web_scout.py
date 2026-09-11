"""LiveWebScout — live public fetch within ceiling."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class LiveWebScoutAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query", "")
        self.log(f"Live scout: {q[:100]}")
        return {"status": "ok", "query": q, "mode": "live", "hits": [], "note": "Wire live fetch in deploy; public only."}
