"""Permanent Agent Swarm configuration — always-on, public ceiling."""
from __future__ import annotations
import os
from dataclasses import dataclass, field
from typing import List

@dataclass
class SwarmConfig:
    permanent_swarm: bool = True
    never_bypass_supervisor: bool = True
    public_record_ceiling: bool = True
    hitl_required: bool = True
    max_parallel_work: int = 6
    max_agent_steps: int = 12
    heal_retries: int = 2
    metrics_every_n_sec: int = 30
    audit_path: str = "vault/audit.jsonl"
    claims_path: str = "vault/claims.jsonl"
    metrics_path: str = "vault/metrics.jsonl"
    flag_path: str = "vault/flags.jsonl"
    allowed_claim_tags: List[str] = field(
        default_factory=lambda: ["SOLID", "MAYBE", "CONTESTED", "CONTRADICTED"]
    )
    hitl_actions: List[str] = field(
        default_factory=lambda: [
            "bulk_ingest",
            "external_action",
            "irreversible_decision",
            "dissemination",
            "fee_paid_access",
            "contact_living_people",
        ]
    )

    @classmethod
    def from_env(cls) -> "SwarmConfig":
        c = cls()
        c.permanent_swarm = os.getenv("PERMANENT_SWARM", "true").lower() == "true"
        c.public_record_ceiling = os.getenv("PUBLIC_RECORD_CEILING", "true").lower() == "true"
        c.hitl_required = os.getenv("HITL_REQUIRED", "true").lower() == "true"
        c.never_bypass_supervisor = os.getenv("NEVER_BYPASS_SUPERVISOR", "true").lower() == "true"
        return c

config = SwarmConfig.from_env()
