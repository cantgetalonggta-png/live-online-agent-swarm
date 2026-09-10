"""
Central configuration for the Live Online Investigation Swarm.
All agents share this config. Public-record ceiling + HITL enforced.
"""
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()


def _bool_env(name: str, default: bool = True) -> bool:
    v = (os.getenv(name) or "").strip().lower()
    if not v:
        return default
    return v in ("1", "true", "yes", "on")


class SwarmConfig(BaseModel):
    name: str = "Live Online Investigation Swarm"
    version: str = "1.1.0"
    hitl_required: bool = Field(default_factory=lambda: _bool_env("HITL_REQUIRED", True))
    public_record_ceiling: bool = Field(default_factory=lambda: _bool_env("PUBLIC_RECORD_CEILING", True))
    max_parallel_agents: int = 8
    timeout_seconds: int = 120
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    swarm_env: str = os.getenv("SWARM_ENV", "dev")
    auth_enabled: bool = Field(default_factory=lambda: bool((os.getenv("SWARM_API_KEY") or "").strip()))
    redis_configured: bool = Field(default_factory=lambda: bool((os.getenv("REDIS_URL") or "").strip()))
    tavily_configured: bool = Field(default_factory=lambda: bool((os.getenv("TAVILY_API_KEY") or "").strip()))
    llm_primary: str = os.getenv("LLM_PRIMARY", "anthropic")
    llm_fallback: str = os.getenv("LLM_FALLBACK", "groq")

    roles: List[str] = [
        "Supervisor",
        "MemoryVault",
        "PatternDetector",
        "Anticipation",
        "Compliance",
        "OSINTCollector",
        "TruthVerifier",
        "ResearchPlanner",
        "Synthesizer",
        "LiveWebScout",
    ]

    absolute_rules: List[str] = [
        "Only public records and operator-supplied public material",
        "HITL = YES for bulk ingest, external actions, irreversible decisions",
        "SOLID / MAYBE tagging on every claim",
        "No private data, no credential packs, no unauthorized access",
        "Respect robots.txt, ToS, rate limits, jurisdiction",
        "Every claim must have provenance (URL + timestamp + hash)",
    ]


config = SwarmConfig()
