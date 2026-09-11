"""LiveWebScout — fetch public URLs LIVE."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class LiveWebScoutAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or ""
        self.log(f"Scout LIVE: {q[:100]}")
        search = REGISTRY.call("live_public_search", query=q, max_results=3)
        fetches = []
        for r in (search.get("results") or [])[:2]:
            url = r.get("url")
            if url:
                fetches.append(REGISTRY.call("fetch_public_url", url=url, max_chars=1500))
        return {
            "status": "ok",
            "live": True,
            "search": search,
            "fetches": [{"url": f.get("url"), "n_chars": f.get("n_chars"), "status": f.get("status")} for f in fetches],
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
