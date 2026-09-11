"""SelfMetrics — pulse + solid ratio always online."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class SelfMetricsAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        phase = task.get("phase", "tick")
        self.log(f"SelfMetrics {phase}")
        pulse = REGISTRY.call("pulse", phase=phase)
        health = REGISTRY.call("health", monitor=self.monitor)
        claims = self.vault.all_claims()
        ratio = REGISTRY.call("solid_ratio", claims=claims)
        # write pulse line
        from pathlib import Path
        import json, time
        p = Path(self.config.metrics_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": time.time(), "phase": phase, "pulse": pulse, "ratio": ratio, "health_uptime": health.get("uptime_sec")}) + "\n")
        return {"status": "ok", "phase": phase, "pulse": pulse, "solid_ratio": ratio, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
