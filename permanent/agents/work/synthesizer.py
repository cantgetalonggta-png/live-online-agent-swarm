"""Synthesizer — final report via wired tools."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class SynthesizerAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        collected = task.get("collected") or {}
        snap = task.get("vault_snapshot") or self.vault.snapshot()
        self.log(f"Synthesize: {goal[:80]}")
        body = f"Goal: {goal}\nAgents: {list(collected.keys())}\nClaims: {snap}"
        rep = REGISTRY.call("report_write", title=f"swarm:{goal[:40]}", body=body)
        return {
            "status": "ok",
            "report": rep,
            "summary": {
                "goal": goal,
                "n_agents_reported": len(collected),
                "vault": snap,
                "permanent_swarm": True,
            },
            "tools_wired": REGISTRY.tools_for(self.name),
            "always_online": True,
        }
