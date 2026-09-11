"""MemoryVault agent wrapper."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class MemoryVaultAgent(BaseAgent):
    plane = "memory"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        action = task.get("action", "snapshot")
        self.log(f"MemoryVault {action}")
        if action == "snapshot":
            return {"status": "ok", "snapshot": self.vault.snapshot(), "claims": self.vault.all_claims()}
        if action == "query":
            hits = self.vault.query(task.get("query", ""), top_k=int(task.get("top_k", 5)))
            return {"status": "ok", "hits": [
                {"text": h.text, "status": h.status, "hash": h.hash} for h in hits
            ]}
        return {"status": "ok", "snapshot": self.vault.snapshot()}
