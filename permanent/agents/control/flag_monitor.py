"""FlagMonitor — HITL, ceiling, failures, quality."""
from __future__ import annotations
from typing import Any, Dict
from agents.base import BaseAgent

class FlagMonitorAgent(BaseAgent):
    plane = "control"

    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        action = task.get("action", "arm")
        self.log(f"FlagMonitor action={action}")
        if action == "arm":
            return {"status": "armed", "watching": ["hitl", "ceiling", "agent_fail", "quality", "rate_limit"]}
        if action == "scan":
            health = self.monitor.health()
            crit = [f for f in health.get("open_flags", []) if f.get("severity") == "crit"]
            if crit:
                return {"status": "alert", "flags": crit, "escalate": True}
            return {"status": "clear", "flags": health.get("open_flags", [])}
        if action == "raise":
            kind = task.get("kind", "generic")
            detail = task.get("detail", "")
            sev = task.get("severity", "warn")
            flag = self.monitor.raise_flag(kind, detail, sev)
            return {"status": "raised", "flag": flag}
        return {"status": "noop"}
