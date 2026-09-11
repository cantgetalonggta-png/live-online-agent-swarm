"""Shared directives — claims, HITL, ceiling."""
from __future__ import annotations
from enum import Enum
from typing import Any, Dict

class ClaimStatus(str, Enum):
    SOLID = "SOLID"
    MAYBE = "MAYBE"
    CONTESTED = "CONTESTED"
    CONTRADICTED = "CONTRADICTED"

def require_hitl(action: str) -> Dict[str, Any]:
    return {
        "hitl_required": True,
        "action": action,
        "message": f"HITL gate: operator approval required before '{action}'.",
        "codes": ["H1-H15"],
    }

def public_ceiling_check(goal: str) -> Dict[str, Any]:
    blocked_tokens = ["private key", "password dump", "unauthorized access", "doxx"]
    g = goal.lower()
    for t in blocked_tokens:
        if t in g:
            return {"allowed": False, "reason": f"Ceiling block: matches '{t}'"}
    return {"allowed": True, "reason": "Public-record ceiling OK (heuristic)"}
