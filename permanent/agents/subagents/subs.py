"""Built-in subagents: Explore, Scout, General, Reviewer."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class ExploreSubAgent(BaseAgent):
    plane = "subagents"
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("ExploreSub read-only")
        return {"status": "ok", "mode": "read_only", "query": task.get("query", ""), "hits": []}

class ScoutSubAgent(BaseAgent):
    plane = "subagents"
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("ScoutSub external docs")
        return {"status": "ok", "mode": "external_docs", "query": task.get("query", "")}

class GeneralSubAgent(BaseAgent):
    plane = "subagents"
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("GeneralSub multi-step")
        return {"status": "ok", "mode": "general", "task": task}

class ReviewerSubAgent(BaseAgent):
    plane = "subagents"
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.log("ReviewerSub quality")
        return {"status": "ok", "mode": "review", "findings": [], "edit": "deny"}
