"""Permanent always-on swarm factory — never single-agent default. Always-online."""
from __future__ import annotations
from typing import Dict
from utils.monitor import SwarmMonitor
from utils.memory import MemoryVault
from utils.always_online import assert_always_online
from agents.base import BaseAgent
from agents.control.overseer import OverseerAgent
from agents.control.planner import PlannerAgent
from agents.control.flag_monitor import FlagMonitorAgent
from agents.control.healer import HealerAgent
from agents.control.self_metrics import SelfMetricsAgent
from agents.control.supervisor import SupervisorAgent
from agents.work.researcher import ResearcherAgent
from agents.work.investigator import InvestigatorAgent
from agents.work.osint_collector import OSINTCollectorAgent
from agents.work.live_web_scout import LiveWebScoutAgent
from agents.work.pattern import PatternAgent
from agents.work.anticipation import AnticipationAgent
from agents.work.teacher import TeacherAgent
from agents.work.synthesizer import SynthesizerAgent
from agents.work.autopilot_director import AutopilotDirectorAgent
from agents.governance.compliance import ComplianceAgent
from agents.governance.truth_verifier import TruthVerifierAgent
from agents.governance.auditor import AuditorAgent
from agents.governance.completeness_auditor import CompletenessAuditorAgent
from agents.memory.memory_vault_agent import MemoryVaultAgent
from agents.subagents.subs import ExploreSubAgent, ScoutSubAgent, GeneralSubAgent, ReviewerSubAgent


class PermanentSwarm:
    """Always routes through Supervisor + full planes. Always-online policy."""

    def __init__(self):
        self.monitor = SwarmMonitor()
        self.vault = MemoryVault()
        self.agents: Dict[str, BaseAgent] = {}
        self._build()
        self.online_report = assert_always_online(list(self.agents.keys()))

    def _build(self):
        m, v = self.monitor, self.vault
        registry = {
            "Overseer": OverseerAgent("Overseer", m, v),
            "Planner": PlannerAgent("Planner", m, v),
            "FlagMonitor": FlagMonitorAgent("FlagMonitor", m, v),
            "Healer": HealerAgent("Healer", m, v),
            "SelfMetrics": SelfMetricsAgent("SelfMetrics", m, v),
            "Researcher": ResearcherAgent("Researcher", m, v),
            "Investigator": InvestigatorAgent("Investigator", m, v),
            "OSINTCollector": OSINTCollectorAgent("OSINTCollector", m, v),
            "LiveWebScout": LiveWebScoutAgent("LiveWebScout", m, v),
            "Pattern": PatternAgent("Pattern", m, v),
            "Anticipation": AnticipationAgent("Anticipation", m, v),
            "Teacher": TeacherAgent("Teacher", m, v),
            "Synthesizer": SynthesizerAgent("Synthesizer", m, v),
            "AutopilotDirector": AutopilotDirectorAgent("AutopilotDirector", m, v),
            "Compliance": ComplianceAgent("Compliance", m, v),
            "TruthVerifier": TruthVerifierAgent("TruthVerifier", m, v),
            "Auditor": AuditorAgent(m, v),
            "CompletenessAuditor": CompletenessAuditorAgent("CompletenessAuditor", m, v),
            "MemoryVault": MemoryVaultAgent("MemoryVault", m, v),
            "ExploreSub": ExploreSubAgent("ExploreSub", m, v),
            "ScoutSub": ScoutSubAgent("ScoutSub", m, v),
            "GeneralSub": GeneralSubAgent("GeneralSub", m, v),
            "ReviewerSub": ReviewerSubAgent("ReviewerSub", m, v),
        }
        self.agents = registry
        self.agents["Supervisor"] = SupervisorAgent(m, v, registry)
        for name in self.agents:
            self.monitor.set_status(name, "idle")

    async def run(self, goal: str) -> dict:
        """ONLY entry point — permanent swarm, never bypass Supervisor."""
        # Always-online gate (non-blocking WARN)
        self.online_report = assert_always_online(list(self.agents.keys()))
        supervisor = self.agents["Supervisor"]
        result = await supervisor.run({"goal": goal})
        result["always_online"] = self.online_report
        result["n_agents"] = len(self.agents)
        return result

    def roster(self) -> dict:
        return {
            "permanent_swarm": True,
            "always_online": True,
            "n_agents": len(self.agents),
            "agents": sorted(self.agents.keys()),
            "health": self.monitor.health(),
            "online_gate": self.online_report.get("status") if isinstance(self.online_report, dict) else None,
        }


def build_permanent_swarm() -> PermanentSwarm:
    return PermanentSwarm()
