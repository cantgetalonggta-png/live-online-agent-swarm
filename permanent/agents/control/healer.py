"""Healer — retry/degrade/circuit always online."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class HealerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        results = task.get("results") or {}
        failed = [k for k, v in results.items() if isinstance(v, dict) and v.get("status") in ("failed", "error")]
        self.log(f"Healer failed={failed}")
        actions = []
        for name in failed[: self.config.heal_retries]:
            actions.append(REGISTRY.call("retry", agent=name))
        if len(failed) > 3:
            actions.append(REGISTRY.call("degrade", mode="read_only"))
            actions.append(REGISTRY.call("circuit_break", open=True))
        return {"status": "ok", "failed": failed, "actions": actions, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
