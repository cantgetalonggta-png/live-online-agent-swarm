"""Always-online policy: every agent + tool readiness matrix."""
from __future__ import annotations
import time
from typing import Any, Dict, List

from tools.registry import REGISTRY

# Agents that MUST have live web online
LIVE_REQUIRED = {
    "Researcher", "Investigator", "OSINTCollector", "LiveWebScout", "ScoutSub",
    "ExploreSub", "GeneralSub", "Pattern", "Anticipation", "Synthesizer",
}

# Every roster agent must appear in tool bindings when always_online
FULL_ROSTER = [
    "Overseer", "Supervisor", "Planner", "FlagMonitor", "Healer", "SelfMetrics",
    "Researcher", "Investigator", "OSINTCollector", "LiveWebScout", "Pattern",
    "Anticipation", "Teacher", "Synthesizer", "AutopilotDirector",
    "Compliance", "TruthVerifier", "Auditor", "CompletenessAuditor", "MemoryVault",
    "ExploreSub", "ScoutSub", "GeneralSub", "ReviewerSub",
]


def per_agent_readiness(agents: List[str] | None = None) -> Dict[str, Any]:
    agents = agents or FULL_ROSTER
    probe = REGISTRY.readiness()
    live_ok = bool(probe.get("live_web"))
    matrix = {}
    missing = []
    for name in agents:
        tools = REGISTRY.tools_for(name)
        needs_live = name in LIVE_REQUIRED
        agent_ok = True
        issues = []
        if needs_live and not live_ok:
            agent_ok = False
            issues.append("live_web_offline")
        if not tools:
            # still online if logical tools load later; flag soft
            issues.append("no_tool_binding")
        matrix[name] = {
            "online": agent_ok and (bool(tools) or name == "Supervisor"),
            "tools": tools,
            "needs_live": needs_live,
            "issues": issues,
            "required_online": True,
        }
        if not matrix[name]["online"]:
            missing.append({"agent": name, "issues": issues})
    status = "READY" if not missing and live_ok else ("DEGRADED" if live_ok else "OFFLINE_LIVE")
    return {
        "ts": time.time(),
        "always_online_policy": True,
        "live_web": live_ok,
        "n_agents": len(agents),
        "matrix": matrix,
        "missing": missing,
        "status": status,
        "probe": {k: probe.get(k) for k in ("live_web", "agents_bound", "always_online_policy")},
    }


def assert_always_online(agents: List[str] | None = None) -> Dict[str, Any]:
    rep = per_agent_readiness(agents)
    rep["gate"] = "PASS" if rep["status"] == "READY" else "WARN"
    return rep
