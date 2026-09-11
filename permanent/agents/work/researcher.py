"""Researcher — LIVE public research via ToolRegistry."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY

class ResearcherAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query", "")
        self.log(f"Research LIVE: {q[:100]}")
        search = REGISTRY.call("live_public_search", query=q, max_results=5)
        notes = []
        sources = []
        if search.get("status") == "ok":
            for r in search.get("results", []):
                notes.append(f"{r.get('title','')}: {r.get('url','')}")
                sources.append(r.get("url", ""))
        elif search.get("status") == "blocked":
            return {"status": "blocked", "query": q, "reason": search.get("error")}
        else:
            notes.append(f"search_status={search.get('status')} err={search.get('error')}")
        claim = self.vault.add_claim(
            text=f"Public research on: {q} | hits={len(sources)}",
            status="MAYBE",
            sources=sources or ["swarm:researcher:live"],
            agent=self.name,
            confidence=0.55 if sources else 0.35,
        )
        return {
            "status": "ok",
            "query": q,
            "live": True,
            "search": search,
            "notes": notes,
            "claim_hash": claim.hash,
            "tag": "MAYBE",
            "tools_wired": REGISTRY.tools_for(self.name),
        }
