"""Base agent class for the live swarm."""
from abc import ABC, abstractmethod
from typing import Any, Dict
from utils.monitor import SwarmMonitor
from utils.memory import MemoryVault
from swarm_config import config

class BaseAgent(ABC):
    def __init__(self, name: str, monitor: SwarmMonitor, vault: MemoryVault):
        self.name = name
        self.monitor = monitor
        self.vault = vault
        self.config = config

    def log(self, msg: str):
        self.monitor.log(self.name, msg)

    def set_status(self, status: str):
        self.monitor.set_status(self.name, status)

    @abstractmethod
    async def run(self, task: Dict[str, Any]) -> Dict[str, Any]:
        pass
