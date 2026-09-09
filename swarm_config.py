"""
Central configuration for the Live Online Agent Swarm.
All agents share this config. Public-record ceiling + HITL enforced.
"""
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class SwarmConfig(BaseModel):
    name: str = "Live Online Investigation Swarm"
    version: str = "1.0.0"
    hitl_required: bool = Field(default=True)
    public_record_ceiling: bool = Field(default=True)
    max_parallel_agents: int = 8
    timeout_seconds: int = 120
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Roles loaded from skills
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
    
    # Legal directives (from legal-osint-compliance-layer + ethical-data-harvesting)
    absolute_rules: List[str] = [
        "Only public records and operator-supplied public material",
        "HITL = YES for bulk ingest, external actions, irreversible decisions",
        "SOLID / MAYBE tagging on every claim",
        "No private data, no credential packs, no unauthorized access",
        "Respect robots.txt, ToS, rate limits, jurisdiction",
        "Every claim must have provenance (URL + timestamp + hash)",
    ]

config = SwarmConfig()
