"""Swarm monitor + SelfMetrics sink."""
from __future__ import annotations
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class SwarmMonitor:
    started_at: float = field(default_factory=time.time)
    status: Dict[str, str] = field(default_factory=dict)
    logs: List[Dict[str, Any]] = field(default_factory=list)
    counters: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    latencies_ms: Dict[str, List[float]] = field(default_factory=lambda: defaultdict(list))
    flags: List[Dict[str, Any]] = field(default_factory=list)

    def log(self, agent: str, msg: str):
        self.logs.append({"ts": time.time(), "agent": agent, "msg": msg})
        self.counters[f"log:{agent}"] += 1

    def set_status(self, agent: str, status: str):
        self.status[agent] = status
        self.counters[f"status:{status}"] += 1

    def record_latency(self, agent: str, ms: float):
        self.latencies_ms[agent].append(ms)

    def raise_flag(self, kind: str, detail: str, severity: str = "warn"):
        flag = {"ts": time.time(), "kind": kind, "detail": detail, "severity": severity}
        self.flags.append(flag)
        self.counters[f"flag:{kind}"] += 1
        return flag

    def health(self) -> Dict[str, Any]:
        up = time.time() - self.started_at
        avg_lat = {
            k: (sum(v) / len(v) if v else 0.0) for k, v in self.latencies_ms.items()
        }
        return {
            "uptime_sec": round(up, 2),
            "agents": dict(self.status),
            "counters": dict(self.counters),
            "avg_latency_ms": avg_lat,
            "open_flags": [f for f in self.flags if f.get("severity") in ("warn", "crit")],
            "permanent_swarm": True,
        }
