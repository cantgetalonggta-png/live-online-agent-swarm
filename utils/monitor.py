"""
Simple observability for the live swarm.
"""
from datetime import datetime
from typing import List

class SwarmMonitor:
    def __init__(self):
        self.events: List[str] = []
        self.agent_status: dict = {}

    def log(self, agent: str, message: str):
        entry = f"[{datetime.utcnow().isoformat()}] [{agent}] {message}"
        self.events.append(entry)
        print(entry)

    def set_status(self, agent: str, status: str):
        self.agent_status[agent] = {"status": status, "ts": datetime.utcnow().isoformat()}

    def health(self) -> dict:
        return {
            "total_events": len(self.events),
            "agents": self.agent_status,
            "last_5": self.events[-5:]
        }
