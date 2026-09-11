"""OSINTCollector — passive public OSINT LIVE."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class OSINTCollectorAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or ""
        self.log(f"OSINT LIVE: {q[:100]}")
        search = REGISTRY.call("live_public_search", query=f"{q} site:archive.org OR site:documentcloud.org OR FOIA", max_results=5)
        sources = [r.get("url") for r in (search.get("results") or []) if r.get("url")]
        claim = self.vault.add_claim(
            text=f"OSINT collect: {q}",
            status="MAYBE",
            sources=sources or ["swarm:osint:live"],
            agent=self.name,
            confidence=0.5 if sources else 0.3,
        )
        return {"status": "ok", "live": True, "search": search, "claim_hash": claim.hash, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
