"""FlagMonitor — arm/scan/raise always online."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent
from tools.registry import REGISTRY


class FlagMonitorAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        action = task.get("action", "scan")
        self.log(f"FlagMonitor {action}")
        if action == "arm":
            out = REGISTRY.call("flag_arm")
        elif action == "raise":
            out = REGISTRY.call("flag_raise", kind=task.get("kind", "manual"), detail=task.get("detail", ""), monitor=self.monitor)
        else:
            out = REGISTRY.call("flag_scan", monitor=self.monitor)
        return {"status": "ok", "action": action, "result": out, "tools_wired": REGISTRY.tools_for(self.name), "always_online": True}
