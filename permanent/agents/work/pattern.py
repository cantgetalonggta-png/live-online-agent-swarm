"""Pattern — vault cluster detection."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class PatternAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        q = task.get("query") or task.get("goal") or ""
        self.log(f"Pattern: {q[:80]}")
        hits = REGISTRY.call("vault_query", vault=self.vault, q=q)
        snap = self.vault.snapshot()
        return {"status": "ok", "hits": hits, "snapshot": snap, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
