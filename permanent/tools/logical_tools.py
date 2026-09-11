"""Logical tool implementations — always wired for control/governance/memory planes."""
from __future__ import annotations
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from utils.directives import public_ceiling_check, require_hitl
from utils.audit import append_audit


def ceiling_check(goal: str = "", **_) -> Dict[str, Any]:
    return public_ceiling_check(goal or "")


def hitl_gate(action: str = "generic", **_) -> Dict[str, Any]:
    return require_hitl(action)


def flag_read(monitor=None, **_) -> Dict[str, Any]:
    if monitor is None:
        return {"status": "ok", "flags": []}
    return {"status": "ok", "flags": list(getattr(monitor, "flags", []))}


def flag_arm(**_) -> Dict[str, Any]:
    return {"status": "armed", "ts": time.time()}


def flag_scan(monitor=None, **_) -> Dict[str, Any]:
    flags = list(getattr(monitor, "flags", [])) if monitor else []
    return {"status": "ok", "n_flags": len(flags), "open": flags[-5:]}


def flag_raise(kind: str = "manual", detail: str = "", severity: str = "warn", monitor=None, **_) -> Dict[str, Any]:
    if monitor:
        return monitor.raise_flag(kind, detail, severity)
    return {"kind": kind, "detail": detail, "severity": severity, "ts": time.time()}


def audit_write(event: str = "event", payload: Optional[Dict] = None, **_) -> Dict[str, Any]:
    try:
        append_audit(event, payload or {})
        return {"status": "ok", "event": event}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def policy_assert(permanent_swarm: bool = True, **_) -> Dict[str, Any]:
    return {"status": "ok", "permanent_swarm": permanent_swarm, "never_bypass_supervisor": True}


def orchestrate(goal: str = "", **_) -> Dict[str, Any]:
    return {"status": "ok", "mode": "permanent_swarm", "goal": goal}


def fanout(agents: Optional[List[str]] = None, **_) -> Dict[str, Any]:
    return {"status": "ok", "agents": agents or []}


def fanin(results: Optional[Dict] = None, **_) -> Dict[str, Any]:
    return {"status": "ok", "n": len(results or {})}


def hitl_notice(action: str = "notice", **_) -> Dict[str, Any]:
    return require_hitl(action)


def decompose(goal: str = "", **_) -> Dict[str, Any]:
    return {
        "status": "ok",
        "goal": goal,
        "parallel_work": [
            {"agent": "Researcher", "task": {"query": goal}},
            {"agent": "Investigator", "task": {"query": goal, "lead": goal}},
            {"agent": "OSINTCollector", "task": {"query": goal}},
            {"agent": "LiveWebScout", "task": {"query": goal}},
            {"agent": "Pattern", "task": {"query": goal}},
            {"agent": "Anticipation", "task": {"query": goal}},
        ],
        "sequential": ["TruthVerifier", "MemoryVault", "Teacher", "Synthesizer", "Auditor"],
    }


def cost_bounds(max_parallel: int = 6, **_) -> Dict[str, Any]:
    return {"max_parallel": max_parallel, "max_steps": 12}


def retry(agent: str = "", **_) -> Dict[str, Any]:
    return {"status": "retry_scheduled", "agent": agent}


def degrade(mode: str = "read_only", **_) -> Dict[str, Any]:
    return {"status": "degraded", "mode": mode}


def circuit_break(open: bool = True, **_) -> Dict[str, Any]:
    return {"circuit": "open" if open else "closed"}


def pulse(phase: str = "tick", **_) -> Dict[str, Any]:
    return {"phase": phase, "ts": time.time(), "alive": True}


def latency(agent: str = "", ms: float = 0.0, **_) -> Dict[str, Any]:
    return {"agent": agent, "ms": ms}


def solid_ratio(claims: Optional[List] = None, **_) -> Dict[str, Any]:
    claims = claims or []
    solid = sum(1 for c in claims if (c.get("status") if isinstance(c, dict) else getattr(c, "status", "")) == "SOLID")
    n = len(claims) or 1
    return {"solid_ratio": solid / n, "n": len(claims)}


def health(monitor=None, **_) -> Dict[str, Any]:
    if monitor:
        return monitor.health()
    return {"status": "unknown"}


def claim_write(vault=None, text: str = "", status: str = "MAYBE", sources: Optional[List] = None, agent: str = "tool", confidence: float = 0.5, **_) -> Dict[str, Any]:
    if vault is None:
        return {"status": "stub", "text": text}
    c = vault.add_claim(text=text, status=status, sources=sources or [], agent=agent, confidence=confidence)
    return {"status": "ok", "hash": c.hash, "tag": status}


def lead_open(lead: str = "", **_) -> Dict[str, Any]:
    return {"status": "open", "lead": lead, "ts": time.time()}


def vault_query(vault=None, q: str = "", **_) -> Dict[str, Any]:
    if vault is None:
        return {"status": "stub", "hits": []}
    hits = vault.query(q)
    return {"status": "ok", "n": len(hits), "hits": [h.text[:120] for h in hits]}


def vault_snapshot(vault=None, **_) -> Dict[str, Any]:
    if vault is None:
        return {"status": "stub"}
    return vault.snapshot()


def bayesian_ach(claim: str = "", sources: Optional[List] = None, **_) -> Dict[str, Any]:
    try:
        from utils.bayesian import run_ach, matrix_to_dict
        m = run_ach(claim)
        return {"status": "ok", **matrix_to_dict(m)}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def lesson_write(lesson: str = "", **_) -> Dict[str, Any]:
    path = Path("vault/lessons.jsonl")
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"ts": time.time(), "lesson": lesson}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return {"status": "ok"}


def skill_propose(skill: str = "permanent-agent-swarm", change: str = "", rationale: str = "", agent: str = "tool", **_) -> Dict[str, Any]:
    from utils.self_learning import SkillProposalQueue
    q = SkillProposalQueue()
    return q.propose(skill=skill, change=change or "unspecified", rationale=rationale or "", agent=agent)


def report_write(title: str = "report", body: str = "", **_) -> Dict[str, Any]:
    path = Path("vault/reports.jsonl")
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"ts": time.time(), "title": title, "body": body[:2000]}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return {"status": "ok", "title": title}


def risk_list(query: str = "", **_) -> Dict[str, Any]:
    return {
        "status": "ok",
        "risks": [
            "Missing public primary source",
            "Claim status may be MAYBE without FOIA confirmation",
            "HITL required for dissemination",
        ],
        "query": query,
    }


def autopilot_suggest(n: int = 3, **_) -> Dict[str, Any]:
    from utils.autopilot import AutopilotQueue
    q = AutopilotQueue()
    return {"status": "ok", "queued": q.list_queued()[:n]}


LOGICAL_IMPL = {
    "ceiling_check": ceiling_check,
    "hitl_gate": hitl_gate,
    "flag_read": flag_read,
    "flag_arm": flag_arm,
    "flag_scan": flag_scan,
    "flag_raise": flag_raise,
    "audit_write": audit_write,
    "policy_assert": policy_assert,
    "orchestrate": orchestrate,
    "fanout": fanout,
    "fanin": fanin,
    "hitl_notice": hitl_notice,
    "decompose": decompose,
    "cost_bounds": cost_bounds,
    "retry": retry,
    "degrade": degrade,
    "circuit_break": circuit_break,
    "pulse": pulse,
    "latency": latency,
    "solid_ratio": solid_ratio,
    "health": health,
    "claim_write": claim_write,
    "lead_open": lead_open,
    "vault_query": vault_query,
    "vault_snapshot": vault_snapshot,
    "bayesian_ach": bayesian_ach,
    "lesson_write": lesson_write,
    "skill_propose": skill_propose,
    "report_write": report_write,
    "risk_list": risk_list,
    "autopilot_suggest": autopilot_suggest,
}
