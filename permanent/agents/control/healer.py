"""Healer — recover failed agents, circuit-break, degrade."""
from __future__ import annotations
from typing import Any, Dict, List
from agents.base import BaseAgent

class HealerAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        results = task.get("results", {})
        retries = task.get("retries", self.config.heal_retries)
        self.log("Healer scanning failures")
        failed: List[str] = []
        for name, res in results.items():
            if isinstance(res, dict) and res.get("status") == "failed":
                failed.append(name)
            if isinstance(res, dict) and "error" in res and res.get("status") != "ok":
                if name not in failed:
                    failed.append(name)
        healed = []
        degraded = []
        for name in failed:
            # Soft heal: mark for retry / degrade path
            if retries > 0:
                healed.append({"agent": name, "action": "retry_scheduled", "retries_left": retries - 1})
                self.monitor.set_status(name, "healing")
            else:
                degraded.append({"agent": name, "action": "degraded_offline"})
                self.monitor.set_status(name, "degraded")
                self.monitor.raise_flag("degraded", name, "warn")
        return {
            "status": "healed" if healed or not failed else "degraded",
            "failed": failed,
            "healed": healed,
            "degraded": degraded,
        }
