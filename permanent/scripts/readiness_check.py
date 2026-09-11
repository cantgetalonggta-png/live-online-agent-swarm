#!/usr/bin/env python3
"""Per-agent / per-tool always-online readiness check."""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agents.permanent_runtime import build_permanent_swarm
from tools.registry import REGISTRY
from utils.always_online import assert_always_online

def main():
    swarm = build_permanent_swarm()
    roster = swarm.roster()
    report = assert_always_online(roster["agents"])
    matrix = REGISTRY.agent_tool_matrix()
    out = {
        **report,
        "n_agents": roster["n_agents"],
        "agents": roster["agents"],
        "tools_impl": REGISTRY.readiness().get("tools_impl"),
        "every_agent_wired": REGISTRY.readiness().get("every_agent_wired"),
        "matrix_n": len(matrix["agents"]),
    }
    print(json.dumps(out, indent=2, default=str))
    # READY or DEGRADED both exit 0 if live_web; OFFLINE_LIVE -> 1
    return 0 if out.get("live_web") else 1

if __name__ == "__main__":
    raise SystemExit(main())
