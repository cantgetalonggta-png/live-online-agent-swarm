"""SelfMetrics — latency, success, claim ratios, pulse."""
from __future__ import annotations
import time
from typing import Any, Dict
from agents.base import BaseAgent

class SelfMetricsAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        phase = task.get("phase", "pulse")
        self.log(f"SelfMetrics phase={phase}")
        health = self.monitor.health()
        snap = self.vault.snapshot()
        n = snap.get("n_claims", 0) or 1
        by = snap.get("by_status", {})
        solid_ratio = by.get("SOLID", 0) / n if n else 0.0
        maybe_ratio = by.get("MAYBE", 0) / n if n else 0.0
        metrics = {
            "phase": phase,
            "ts": time.time(),
            "health": health,
            "vault": snap,
            "solid_ratio": round(solid_ratio, 3),
            "maybe_ratio": round(maybe_ratio, 3),
            "permanent_swarm": True,
        }
        if solid_ratio < 0.2 and snap.get("n_claims", 0) >= 5:
            self.monitor.raise_flag("quality", "SOLID ratio low", "warn")
        return {"status": "ok", "metrics": metrics}
