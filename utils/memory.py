"""
MemoryVault — durable shared state for the swarm.
In production this would be Redis + PostgreSQL + Neo4j.
Here we keep an in-memory store with provenance.
"""
from typing import Dict, List, Optional
from utils.directives import Claim, ClaimStatus
from datetime import datetime
import json

class MemoryVault:
    def __init__(self):
        self.claims: Dict[str, Claim] = {}
        self.timeline: List[dict] = []
        self.entities: Dict[str, dict] = {}
        self.logs: List[str] = []

    def store_claim(self, claim: Claim) -> str:
        claim.provenance_hash = claim.compute_hash()
        self.claims[claim.provenance_hash] = claim
        self.logs.append(f"[{datetime.utcnow().isoformat()}] Stored {claim.status}: {claim.text[:80]}...")
        return claim.provenance_hash

    def query(self, keyword: str) -> List[Claim]:
        return [c for c in self.claims.values() if keyword.lower() in c.text.lower()]

    def add_timeline_event(self, date: str, event: str, sources: List[str], status: ClaimStatus = ClaimStatus.MAYBE):
        self.timeline.append({
            "date": date,
            "event": event,
            "sources": sources,
            "status": status.value,
            "recorded": datetime.utcnow().isoformat()
        })
        self.timeline.sort(key=lambda x: x["date"])

    def snapshot(self) -> dict:
        return {
            "claim_count": len(self.claims),
            "timeline_events": len(self.timeline),
            "entities": len(self.entities),
            "recent_logs": self.logs[-10:]
        }
