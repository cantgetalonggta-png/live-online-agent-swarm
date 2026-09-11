"""Synthesizer — final coherent report."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class SynthesizerAgent(BaseAgent):
    plane = "work"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task.get("goal", "")
        collected = task.get("collected", {})
        vault_snapshot = task.get("vault_snapshot") or self.vault.snapshot()
        self.log("Synthesizing permanent swarm report")
        agents_ok = [k for k, v in collected.items() if isinstance(v, dict) and v.get("status") in ("ok", "planned", "armed", "completed", "healed", "clear")]
        agents_fail = [k for k, v in collected.items() if isinstance(v, dict) and v.get("status") == "failed"]
        report = {
            "goal": goal,
            "permanent_swarm": True,
            "agents_ok": agents_ok,
            "agents_fail": agents_fail,
            "vault": vault_snapshot,
            "summary": (
                f"Permanent swarm completed for goal. "
                f"OK={len(agents_ok)} FAIL={len(agents_fail)} claims={vault_snapshot.get('n_claims', 0)}."
            ),
            "claim_policy": "All claims tagged SOLID/MAYBE/CONTESTED/CONTRADICTED with provenance.",
        }
        self.vault.add_claim(
            text=report["summary"],
            status="MAYBE",
            sources=["swarm:synthesizer"],
            agent=self.name,
            confidence=0.55,
        )
        return {"status": "ok", "report": report}
