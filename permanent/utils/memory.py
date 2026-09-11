"""Minimal MemoryVault — claim store + snapshot (Graph RAG hook-compatible)."""
from __future__ import annotations
import hashlib
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class Claim:
    text: str
    status: str  # SOLID|MAYBE|CONTESTED|CONTRADICTED
    sources: List[str]
    agent: str
    confidence: float = 0.5
    ts: float = field(default_factory=time.time)

    @property
    def hash(self) -> str:
        return hashlib.sha256(self.text.encode()).hexdigest()[:16]

@dataclass
class MemoryVault:
    claims: List[Claim] = field(default_factory=list)
    docs: Dict[str, Any] = field(default_factory=dict)
    entities: Dict[str, Any] = field(default_factory=dict)

    def add_claim(self, text: str, status: str, sources: List[str], agent: str, confidence: float = 0.5) -> Claim:
        c = Claim(text=text, status=status, sources=sources, agent=agent, confidence=confidence)
        self.claims.append(c)
        return c

    def all_claims(self) -> List[Dict[str, Any]]:
        return [
            {
                "hash": c.hash,
                "text": c.text,
                "status": c.status,
                "sources": c.sources,
                "agent": c.agent,
                "confidence": c.confidence,
                "ts": c.ts,
            }
            for c in self.claims
        ]

    def snapshot(self) -> Dict[str, Any]:
        by_status = {}
        for c in self.claims:
            by_status[c.status] = by_status.get(c.status, 0) + 1
        return {
            "n_claims": len(self.claims),
            "by_status": by_status,
            "n_docs": len(self.docs),
            "n_entities": len(self.entities),
        }

    def query(self, q: str, top_k: int = 5) -> List[Claim]:
        ql = q.lower()
        scored = [(c, sum(1 for w in ql.split() if w in c.text.lower())) for c in self.claims]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [c for c, s in scored[:top_k] if s > 0]
