"""Investigator — lead-driven LIVE public investigation."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class InvestigatorAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("lead") or task.get("goal") or ""
        self.log(f"Investigate LIVE: {q[:100]}")
        REGISTRY.call("lead_open", lead=q)
        search = REGISTRY.call("live_public_search", query=q, max_results=5)
        sources = [r.get("url") for r in (search.get("results") or []) if r.get("url")]
        claim = self.vault.add_claim(
            text=f"Investigation lead: {q} | live_hits={len(sources)}",
            status="MAYBE",
            sources=sources or ["swarm:investigator:live"],
            agent=self.name,
            confidence=0.5 if sources else 0.3,
        )
        return {
            "status": "ok",
            "live": True,
            "search": search,
            "claim_hash": claim.hash,
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
