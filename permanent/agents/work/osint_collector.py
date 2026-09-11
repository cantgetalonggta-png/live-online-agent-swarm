"""OSINTCollector — passive public OSINT only."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class OSINTCollectorAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query", "")
        self.log(f"OSINT public: {q[:100]}")
        return {
            "status": "ok",
            "query": q,
            "mode": "public_search",
            "ceiling": "osint-public-ceiling",
            "findings": [],
            "note": "Passive public methods only; no unauthorized access.",
        }
