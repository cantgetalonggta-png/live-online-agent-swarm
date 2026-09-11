"""Live tool registry — every agent wired; readiness always-online."""
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Optional
import time

try:
    import yaml
except ImportError:
    yaml = None

from tools.live_web import live_public_search, fetch_public_url
from tools.logical_tools import LOGICAL_IMPL


class ToolRegistry:
    def __init__(self, config_path: Optional[str] = None):
        base = Path(__file__).resolve().parents[1]
        self.config_path = Path(config_path) if config_path else base / "config" / "agent_tools.yaml"
        self.bindings: Dict[str, List[str]] = {}
        self.impl: Dict[str, Any] = {
            "live_public_search": live_public_search,
            "fetch_public_url": fetch_public_url,
            **LOGICAL_IMPL,
        }
        self._load()
        self._ensure_all_agents()

    def _load(self):
        if self.config_path.exists() and yaml:
            data = yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {}
            agents = data.get("agents", {})
            for name, meta in agents.items():
                self.bindings[name] = list(meta.get("tools", []))
        else:
            self.bindings = {}

    def _ensure_all_agents(self):
        """Always-online: every agent has at least one tool binding."""
        defaults = {
            "Overseer": ["ceiling_check", "flag_read", "audit_write", "policy_assert"],
            "Supervisor": ["orchestrate", "fanout", "fanin", "hitl_notice"],
            "Planner": ["decompose", "cost_bounds"],
            "FlagMonitor": ["flag_arm", "flag_scan", "flag_raise"],
            "Healer": ["retry", "degrade", "circuit_break"],
            "SelfMetrics": ["pulse", "latency", "solid_ratio", "health"],
            "Researcher": ["live_public_search", "fetch_public_url", "claim_write"],
            "Investigator": ["live_public_search", "claim_write", "lead_open", "vault_query"],
            "OSINTCollector": ["live_public_search", "claim_write"],
            "LiveWebScout": ["live_public_search", "fetch_public_url"],
            "Pattern": ["vault_query", "claim_write"],
            "Anticipation": ["vault_query", "risk_list", "autopilot_suggest"],
            "Teacher": ["lesson_write", "skill_propose"],
            "Synthesizer": ["report_write", "claim_write"],
            "Compliance": ["ceiling_check", "hitl_gate"],
            "TruthVerifier": ["bayesian_ach", "claim_write", "vault_query"],
            "Auditor": ["audit_write"],
            "MemoryVault": ["vault_snapshot", "vault_query", "claim_write"],
            "ExploreSub": ["vault_query", "live_public_search"],
            "ScoutSub": ["live_public_search", "fetch_public_url"],
            "GeneralSub": ["orchestrate", "live_public_search"],
            "ReviewerSub": ["report_write", "audit_write"],
            "CompletenessAuditor": ["vault_query", "report_write", "audit_write"],
            "AutopilotDirector": ["autopilot_suggest", "orchestrate", "skill_propose"],
        }
        for name, tools in defaults.items():
            if name not in self.bindings or not self.bindings[name]:
                self.bindings[name] = tools
            else:
                # merge unique
                merged = list(dict.fromkeys(self.bindings[name] + tools))
                self.bindings[name] = merged

    def tools_for(self, agent: str) -> List[str]:
        return self.bindings.get(agent, [])

    def call(self, tool: str, **kwargs) -> Any:
        if tool not in self.impl:
            return {"status": "stub", "tool": tool, "note": "logical tool (no external call)"}
        return self.impl[tool](**kwargs)

    def readiness(self) -> Dict[str, Any]:
        probe = live_public_search("FOIA 20 working days site:justice.gov", max_results=2)
        online = probe.get("status") == "ok"
        return {
            "ts": time.time(),
            "live_web": online,
            "probe_status": probe.get("status"),
            "n_results": probe.get("n", 0),
            "agents_bound": len(self.bindings),
            "tools_impl": len(self.impl),
            "always_online_policy": True,
            "every_agent_wired": all(bool(v) for v in self.bindings.values()),
        }

    def agent_tool_matrix(self) -> Dict[str, Any]:
        return {
            "always_online": True,
            "agents": {
                name: {
                    "tools": tools,
                    "live_capable": any(t in ("live_public_search", "fetch_public_url") for t in tools),
                    "n_tools": len(tools),
                }
                for name, tools in sorted(self.bindings.items())
            },
        }


REGISTRY = ToolRegistry()
