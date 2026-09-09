"""Shared swarm factory used by CLI, FastAPI, and Streamlit."""
from utils.monitor import SwarmMonitor
from utils.memory import MemoryVault
from agents import (
    SupervisorAgent,
    OSINTCollectorAgent,
    TruthVerifierAgent,
    LiveWebScoutAgent,
    MemoryVaultAgent,
    ComplianceAgent,
    PatternAgent,
    AnticipationAgent,
    SynthesizerAgent,
)

# Process-level singletons so API + dashboard share state
_monitor = None
_vault = None
_supervisor = None


def get_runtime():
    global _monitor, _vault, _supervisor
    if _supervisor is None:
        _monitor = SwarmMonitor()
        _vault = MemoryVault()
        specialists = {
            "Compliance": ComplianceAgent(_monitor, _vault),
            "OSINTCollector": OSINTCollectorAgent(_monitor, _vault),
            "LiveWebScout": LiveWebScoutAgent(_monitor, _vault),
            "Pattern": PatternAgent(_monitor, _vault),
            "TruthVerifier": TruthVerifierAgent(_monitor, _vault),
            "MemoryVault": MemoryVaultAgent(_monitor, _vault),
            "Anticipation": AnticipationAgent(_monitor, _vault),
            "Synthesizer": SynthesizerAgent(_monitor, _vault),
        }
        _supervisor = SupervisorAgent(_monitor, _vault, specialists)
    return _supervisor, _monitor, _vault
