"""
Lawful operating directives shared by every agent.
Enforces public-record ceiling, HITL, SOLID/MAYBE discipline.
"""
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import hashlib

class ClaimStatus(str, Enum):
    SOLID = "SOLID"      # High confidence, primary sources, consistent
    MAYBE = "MAYBE"      # Tentative, needs more evidence or HITL
    CONTESTED = "CONTESTED"
    UNTESTED = "UNTESTED"
    CONTRADICTED = "CONTRADICTED"

class Claim(BaseModel):
    text: str
    status: ClaimStatus = ClaimStatus.UNTESTED
    sources: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)
    provenance_hash: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    agent: str = "unknown"
    notes: Optional[str] = None

    def compute_hash(self) -> str:
        payload = f"{self.text}|{sorted(self.sources)}|{self.agent}"
        return hashlib.sha256(payload.encode()).hexdigest()[:16]

def enforce_public_record(claim: Claim) -> bool:
    """Reject any claim that cannot demonstrate public provenance."""
    if not claim.sources:
        return False
    # Simple heuristic: must have at least one http/https or archive.org source
    public = any(
        s.startswith("http://") or s.startswith("https://") or "archive.org" in s.lower()
        for s in claim.sources
    )
    return public

def require_hitl(action: str) -> str:
    return f"[HITL REQUIRED] {action} — pause for human confirmation before proceeding."
