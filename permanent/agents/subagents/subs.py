"""Permanent subagents — each always online with tools."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class ExploreSubAgent(BaseAgent):
    plane = "subagents"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or "vault explore"
        hits = REGISTRY.call("vault_query", vault=self.vault, q=q)
        search = REGISTRY.call("live_public_search", query=q, max_results=2)
        return {"status": "ok", "hits": hits, "live": search, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}


class ScoutSubAgent(BaseAgent):
    plane = "subagents"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or ""
        search = REGISTRY.call("live_public_search", query=q, max_results=3)
        return {"status": "ok", "live": True, "search": search, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}


class GeneralSubAgent(BaseAgent):
    plane = "subagents"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal") or task.get("query") or ""
        orch = REGISTRY.call("orchestrate", goal=goal)
        search = REGISTRY.call("live_public_search", query=goal, max_results=2)
        return {"status": "ok", "orch": orch, "live": search, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}


class ReviewerSubAgent(BaseAgent):
    plane = "subagents"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        body = str(task.get("body") or task.get("goal") or "")[:500]
        rep = REGISTRY.call("report_write", title="reviewer", body=body)
        REGISTRY.call("audit_write", event="reviewer_sub", payload={"n": len(body)})
        return {"status": "ok", "report": rep, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
