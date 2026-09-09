"""
Streamlit live dashboard for the Investigation Swarm.
Run: streamlit run dashboard/app.py --server.port 8501
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import asyncio
import json
import pandas as pd
from datetime import datetime

from swarm_runtime import get_runtime
from utils.bayesian import run_ach, matrix_to_dict, best_hypothesis
from swarm_config import config

st.set_page_config(
    page_title="Live Investigation Swarm",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Styles ──────────────────────────────────────────────────────
st.markdown(
    """
<style>
    .status-SOLID { color: #0a7; font-weight: 700; }
    .status-MAYBE { color: #c80; font-weight: 700; }
    .status-CONTESTED { color: #c40; font-weight: 700; }
    .status-CONTRADICTED { color: #a00; font-weight: 700; }
    .hitl-box { background: #332200; border-left: 4px solid #fa0; padding: 0.75rem; margin: 0.5rem 0; }
    .metric-card { background: #1a1a2e; padding: 1rem; border-radius: 8px; }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🕵️ Live Online Investigation Swarm")
st.caption(
    f"{config.name} v{config.version} · Bayesian ACH · RedisGraph RAG · HITL · Public-record ceiling"
)

# ── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.header("Controls")
    page = st.radio(
        "View",
        ["Run Swarm", "Bayesian Verify", "Graph RAG", "Claims & Memory", "Health"],
        index=0,
    )
    st.divider()
    st.markdown("**Absolute rules**")
    for r in config.absolute_rules:
        st.caption(f"• {r}")
    st.divider()
    if st.button("Refresh runtime"):
        st.rerun()

supervisor, monitor, vault = get_runtime()


def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Streamlit often has a running loop; use nest if needed
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                return pool.submit(asyncio.run, coro).result()
        return loop.run_until_complete(coro)
    except RuntimeError:
        return asyncio.run(coro)


# ── Pages ───────────────────────────────────────────────────────
if page == "Run Swarm":
    st.subheader("Orchestrate multi-agent run")
    goal = st.text_area(
        "Investigation goal",
        value="Map public records on open government transparency initiatives",
        height=100,
    )
    col1, col2 = st.columns([1, 3])
    with col1:
        run_btn = st.button("▶ Run Swarm", type="primary", use_container_width=True)

    if run_btn and goal.strip():
        with st.spinner("Supervisor orchestrating agents (Compliance → parallel collect → Bayesian verify → synthesize)…"):
            result = run_async(supervisor.run({"goal": goal.strip()}))
        st.session_state["last_result"] = result
        st.success(f"Status: {result.get('status')}")

        if result.get("results", {}).get("hitl_notice"):
            st.markdown(
                f'<div class="hitl-box">{result["results"]["hitl_notice"]}</div>',
                unsafe_allow_html=True,
            )

        # Metrics
        m1, m2, m3, m4 = st.columns(4)
        snap = result.get("memory_snapshot", {})
        m1.metric("Claims", snap.get("claim_count", 0))
        m2.metric("Graph nodes", snap.get("graph", {}).get("nodes", 0))
        m3.metric("Verifications", snap.get("verifications", 0))
        m4.metric("Events", result.get("health", {}).get("total_events", 0))

        # TruthVerifier ACH
        tv = result.get("results", {}).get("TruthVerifier", {})
        if tv.get("ach"):
            st.subheader("Bayesian ACH result")
            ach = tv["ach"]
            st.write(f"**Best hypothesis:** {ach.get('best', {}).get('text')}  ")
            st.write(
                f"Posterior **{ach.get('best', {}).get('posterior')}** → "
                f"<span class='status-{ach.get('claim_status')}'>{ach.get('claim_status')}</span>",
                unsafe_allow_html=True,
            )
            hyp_df = pd.DataFrame(ach.get("hypotheses", []))
            if not hyp_df.empty:
                st.bar_chart(hyp_df.set_index("id")["posterior"])
                with st.expander("Full ACH matrix"):
                    st.dataframe(hyp_df, use_container_width=True)
                    st.json(ach.get("evidence", []))

        # Agent results
        st.subheader("Agent outputs")
        for name, res in result.get("results", {}).items():
            if name in ("hitl_notice",):
                continue
            with st.expander(f"{name}"):
                st.json(res if isinstance(res, dict) else {"value": res})

        with st.expander("Full JSON"):
            st.json(result)

    elif "last_result" in st.session_state:
        st.info("Showing last run. Click Run Swarm for a new one.")
        st.json(st.session_state["last_result"].get("memory_snapshot", {}))

elif page == "Bayesian Verify":
    st.subheader("Bayesian Belief Network + ACH")
    claim = st.text_area("Claim to verify", height=80, placeholder="Enter a precise claim…")
    with st.expander("Optional evidence (JSON list)"):
        evidence_raw = st.text_area(
            "evidence",
            value="[]",
            help='[{"description":"…","source":"…","likelihood_if_h":0.8,"likelihood_if_not_h":0.3,"quality":0.7}]',
        )
    if st.button("Verify", type="primary") and claim.strip():
        try:
            evidence = json.loads(evidence_raw) if evidence_raw.strip() else None
        except json.JSONDecodeError:
            st.error("Invalid evidence JSON")
            evidence = None
        # RAG enrich
        rag = vault.rag_query(claim, top_k=3)
        extra = []
        for r in rag.get("results", []):
            extra.append(
                {
                    "description": r.get("text", "")[:200],
                    "source": r.get("source", "graph_rag"),
                    "likelihood_if_h": min(0.85, 0.5 + float(r.get("score", 0.3)) * 0.4),
                    "likelihood_if_not_h": max(0.15, 0.5 - float(r.get("score", 0.3)) * 0.3),
                    "quality": min(0.9, 0.5 + float(r.get("score", 0.3)) * 0.4),
                }
            )
        all_ev = (evidence or []) + extra
        matrix = run_ach(claim.strip(), evidence_items=all_ev or None)
        result = matrix_to_dict(matrix)
        vault.store_verification(result)
        from utils.directives import Claim, ClaimStatus
        from utils.bayesian import confidence_to_claim_status

        best = best_hypothesis(matrix)
        status_str = confidence_to_claim_status(best.posterior)
        try:
            st_enum = ClaimStatus(status_str)
        except ValueError:
            st_enum = ClaimStatus.MAYBE
        c = Claim(
            text=claim.strip(),
            status=st_enum,
            sources=["dashboard:/verify"],
            confidence=round(best.posterior, 4),
            agent="Dashboard-TruthVerifier",
            notes=f"Best: {best.text}",
        )
        vault.store_claim(c)

        st.markdown(
            f"**Status:** <span class='status-{status_str}'>{status_str}</span> · "
            f"Posterior: **{best.posterior:.3f}**",
            unsafe_allow_html=True,
        )
        st.write(f"Best hypothesis: {best.text}")
        hyp_df = pd.DataFrame(result["hypotheses"])
        st.bar_chart(hyp_df.set_index("id")[["prior", "posterior"]])
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Hypotheses")
            st.dataframe(hyp_df, use_container_width=True)
        with c2:
            st.subheader("Evidence")
            st.dataframe(pd.DataFrame(result["evidence"]), use_container_width=True)
        if rag.get("results"):
            st.subheader("RAG context used")
            st.json(rag["results"])

elif page == "Graph RAG":
    st.subheader("Hybrid Graph + Vector RAG (RedisGraph-compatible)")
    stats = vault.graph.stats()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nodes", stats.get("nodes", 0))
    c2.metric("Edges", stats.get("edges", 0))
    c3.metric("Chunks", stats.get("chunks", 0))
    c4.metric("Redis", "yes" if stats.get("redis_connected") else "in-memory")
    st.caption(f"Labels: {stats.get('labels', {})} · RedisGraph module: {stats.get('redis_graph')}")

    tab1, tab2, tab3 = st.tabs(["Query", "Ingest document", "Cypher-like"])
    with tab1:
        q = st.text_input("Query", value="public records transparency")
        k = st.slider("top_k", 1, 15, 5)
        if st.button("Hybrid search") and q:
            out = vault.rag_query(q, top_k=k)
            st.write(f"Backend: `{out.get('backend')}`")
            for i, r in enumerate(out.get("results", []), 1):
                st.markdown(f"**{i}. score={r.get('score', 0):.3f}** via `{r.get('via')}` · {r.get('title')}")
                st.write(r.get("text", "")[:400])
                st.caption(r.get("source"))
                st.divider()
    with tab2:
        doc_id = st.text_input("doc_id", value=f"doc-{datetime.utcnow().strftime('%H%M%S')}")
        title = st.text_input("title", value="Public note")
        source = st.text_input("source URL", value="https://example-public.org/page")
        body = st.text_area("text (will be split into ~500-char chunks)", height=150)
        if st.button("Ingest") and body.strip():
            chunks = [body[i : i + 500] for i in range(0, len(body), 500)]
            vault.add_document(doc_id, title, source, chunks)
            st.success(f"Ingested {len(chunks)} chunks into Graph RAG")
            st.json(vault.graph.stats())
    with tab3:
        pattern = st.selectbox(
            "Pattern",
            [
                "MATCH (c:Claim) RETURN c LIMIT 20",
                "MATCH (e:Entity) RETURN e LIMIT 20",
                "MATCH (d:Document) RETURN d LIMIT 20",
            ],
        )
        if st.button("Run"):
            st.json(vault.graph.cypher_like(pattern))

elif page == "Claims & Memory":
    st.subheader("MemoryVault claims")
    claims = vault.all_claims()
    if claims:
        df = pd.DataFrame(claims)
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df["status"].value_counts())
    else:
        st.info("No claims yet. Run the swarm or verify a claim.")
    st.subheader("Recent verifications")
    for v in vault.verification_history[-5:][::-1]:
        with st.expander(v.get("claim", "?")[:80]):
            st.json(v)
    st.subheader("Snapshot")
    st.json(vault.snapshot())

elif page == "Health":
    st.subheader("Swarm health")
    st.json(monitor.health())
    st.subheader("Config")
    st.json(
        {
            "name": config.name,
            "version": config.version,
            "hitl_required": config.hitl_required,
            "public_record_ceiling": config.public_record_ceiling,
            "roles": config.roles,
            "absolute_rules": config.absolute_rules,
        }
    )
    st.subheader("Graph")
    st.json(vault.graph.stats())

st.divider()
st.caption("Public-record only · HITL enforced · SOLID/MAYBE discipline · FastAPI at :8000 · Streamlit :8501")
