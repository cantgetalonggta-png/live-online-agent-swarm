"""Base agent for permanent swarm."""
from __future__ import annotations
import time
from abc import ABC, abstractmethod
from typing import Any, Dict
from utils.monitor import SwarmMonitor
from utils.memory import MemoryVault
from swarm_config import config

class BaseAgent(ABC):
    plane: str = "work"
    permanent: bool = True

    def __init__(self, name: str, monitor: SwarmMonitor, vault: MemoryVault):
        self.name = name
        self.monitor = monitor
        self.vault = vault
        self.config = config

    def log(self, msg: str):
        self.monitor.log(self.name, msg)

    def set_status(self, status: str):
        self.monitor.set_status(self.name, status)

    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        self.set_status("running")
        t0 = time.time()
        try:
            out = await self.execute(task)
            self.monitor.record_latency(self.name, (time.time() - t0) * 1000)
            self.set_status("idle")
            return out
        except Exception as e:
            self.monitor.raise_flag("agent_fail", f"{self.name}: {e}", severity="crit")
            self.set_status("failed")
            self.monitor.record_latency(self.name, (time.time() - t0) * 1000)
            return {"status": "failed", "agent": self.name, "error": str(e)}

    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        ...
