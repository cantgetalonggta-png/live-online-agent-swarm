"""
FastAPI live backend for the Investigation Swarm.
Auth: SWARM_API_KEY (optional dev open mode if unset)
Integrations: Redis (durable graph), Tavily (public search), multi-LLM hooks
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
import os

from swarm_runtime import get_runtime
from utils.bayesian import run_ach, matrix_to_dict
from swarm_config import config
from utils.auth import require_write_key, require_api_key, auth_enabled
from utils.llm_client import get_llm
from utils.tavily_client import get_tavily

# CORS — tighten via SWARM_CORS_ORIGINS (comma-separated) or * for dev
_cors = [o.strip() for o in (os.getenv("SWARM_CORS_ORIGINS") or "*").split(",") if o.strip()]

app = FastAPI(
    title="Live Online Investigation Swarm API",
    description="Bayesian ACH · Graph RAG · Multi-agent Supervisor · HITL · optional Redis/Tavily/LLM",
    version=config.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors if _cors != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GoalRequest(BaseModel):
    goal: str = Field(..., min_length=3, description="Investigation goal / question")


class VerifyRequest(BaseModel):
    claim: str
    evidence: Optional[List[Dict[str, Any]]] = None
    hypotheses: Optional[List[str]] = None
    sources: Optional[List[str]] = None


class RAGRequest(BaseModel):
    query: str
    top_k: int = 5


class DocIngest(BaseModel):
    doc_id: str
    title: str
    source: str
    chunks: List[str]
    meta: Optional[Dict[str, Any]] = None


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2)
    max_results: int = 5


class LLMRequest(BaseModel):
    prompt: str = Field(..., min_length=3)
    system: Optional[str] = None
    max_tokens: int = 800


@app.get("/")
def root():
    return {
        "name": config.name,
        "version": config.version,
        "docs": "/docs",
        "auth_enabled": auth_enabled(),
        "dashboard_hint": "streamlit run dashboard/app.py",
        "absolute_rules": config.absolute_rules,
    }


@app.get("/health")
def health():
    _, monitor, vault = get_runtime()
    llm = get_llm()
    tavily = get_tavily()
    gstats = vault.graph.stats() if hasattr(vault, "graph") else {}
    return {
        "status": "ok",
        "swarm": monitor.health(),
        "memory": vault.snapshot(),
        "config": {
            "hitl_required": config.hitl_required,
            "public_record_ceiling": config.public_record_ceiling,
            "roles": config.roles,
            "auth_enabled": auth_enabled(),
            "swarm_env": config.swarm_env,
        },
        "integrations": {
            "redis": {
                "configured": bool(os.getenv("REDIS_URL")),
                "connected": bool(gstats.get("redis_connected")),
                "redis_graph": bool(gstats.get("redis_graph")),
            },
            "tavily": tavily.status(),
            "llm": llm.status(),
        },
    }


@app.get("/integrations")
def integrations(_role: str = Depends(require_api_key)):
    """Status of optional paid/hooks — never returns secret values."""
    llm = get_llm()
    tavily = get_tavily()
    _, _, vault = get_runtime()
    gstats = vault.graph.stats()
    return {
        "auth_enabled": auth_enabled(),
        "redis": {
            "configured": bool(os.getenv("REDIS_URL")),
            "connected": bool(gstats.get("redis_connected")),
            "redis_graph": bool(gstats.get("redis_graph")),
        },
        "tavily": tavily.status(),
        "llm": llm.status(),
        "cors": os.getenv("SWARM_CORS_ORIGINS", "*"),
    }


@app.post("/swarm/run")
async def swarm_run(req: GoalRequest, _role: str = Depends(require_write_key)):
    supervisor, _, _ = get_runtime()
    try:
        result = await supervisor.run({"goal": req.goal})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/verify")
async def verify_claim(req: VerifyRequest, _role: str = Depends(require_write_key)):
    """Direct Bayesian ACH verification (also stores in vault + graph)."""
    _, _, vault = get_runtime()
    evidence = list(req.evidence or [])
    try:
        rag = vault.rag_query(req.claim, top_k=3)
        for r in rag.get("results", []):
            evidence.append(
                {
                    "id": r.get("chunk_id", "rag"),
                    "description": r.get("text", "")[:200],
                    "source": r.get("source", "graph_rag"),
                    "likelihood_if_h": min(0.85, 0.5 + float(r.get("score", 0.3)) * 0.4),
                    "likelihood_if_not_h": max(0.15, 0.5 - float(r.get("score", 0.3)) * 0.3),
                    "quality": min(0.9, 0.5 + float(r.get("score", 0.3)) * 0.4),
                }
            )
    except Exception:
        pass

    matrix = run_ach(req.claim, hyp_texts=req.hypotheses, evidence_items=evidence or None)
    result = matrix_to_dict(matrix)
    vault.store_verification(result)

    from utils.directives import Claim, ClaimStatus
    from utils.bayesian import confidence_to_claim_status, best_hypothesis

    best = best_hypothesis(matrix)
    status_str = confidence_to_claim_status(best.posterior)
    try:
        st = ClaimStatus(status_str)
    except ValueError:
        st = ClaimStatus.MAYBE
    c = Claim(
        text=req.claim,
        status=st,
        sources=req.sources or ["api:/verify"],
        confidence=round(best.posterior, 4),
        agent="API-TruthVerifier",
        notes=f"Best: {best.text}",
    )
    h = vault.store_claim(c)
    result["claim_hash"] = h
    return result


@app.post("/rag/query")
def rag_query(req: RAGRequest, _role: str = Depends(require_api_key)):
    _, _, vault = get_runtime()
    return vault.rag_query(req.query, top_k=req.top_k)


@app.post("/rag/ingest")
def rag_ingest(doc: DocIngest, _role: str = Depends(require_write_key)):
    _, _, vault = get_runtime()
    vault.add_document(doc.doc_id, doc.title, doc.source, doc.chunks, doc.meta)
    # Persist to Redis if configured
    try:
        if hasattr(vault, "graph") and hasattr(vault.graph, "save"):
            vault.graph.save()
    except Exception:
        pass
    return {"status": "ingested", "doc_id": doc.doc_id, "chunks": len(doc.chunks), "graph": vault.graph.stats()}


@app.post("/search/public")
def search_public(req: SearchRequest, _role: str = Depends(require_write_key)):
    """Tavily public web search hook — empty if no TAVILY_API_KEY."""
    tavily = get_tavily()
    return tavily.search(req.query, max_results=req.max_results)


@app.post("/llm/complete")
def llm_complete(req: LLMRequest, _role: str = Depends(require_write_key)):
    """Optional LLM completion — returns offline stub if no provider keys."""
    llm = get_llm()
    if not llm.is_available():
        return {
            "status": "skipped_no_key",
            "text": None,
            "note": "Set OPENAI_API_KEY / ANTHROPIC_API_KEY / GROK_API_KEY / GROQ_API_KEY",
            "llm": llm.status(),
        }
    text = llm.complete(req.prompt, system=req.system or "You are a lawful public-record investigation assistant. Never invent private data. Prefer SOLID/MAYBE discipline. No bypass advice.", max_tokens=req.max_tokens)
    return {"status": "ok" if text else "error", "text": text, "llm": llm.status()}


@app.get("/claims")
def list_claims(_role: str = Depends(require_api_key)):
    _, _, vault = get_runtime()
    return {"claims": vault.all_claims(), "count": len(vault.claims)}


@app.get("/graph/stats")
def graph_stats(_role: str = Depends(require_api_key)):
    _, _, vault = get_runtime()
    return vault.graph.stats()


@app.get("/graph/cypher")
def graph_cypher(pattern: str = "MATCH (c:Claim) RETURN c LIMIT 20", _role: str = Depends(require_api_key)):
    _, _, vault = get_runtime()
    return {"pattern": pattern, "results": vault.graph.cypher_like(pattern)}


@app.get("/verifications")
def list_verifications(_role: str = Depends(require_api_key)):
    _, _, vault = get_runtime()
    return {"verifications": vault.verification_history[-20:], "count": len(vault.verification_history)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=False)
