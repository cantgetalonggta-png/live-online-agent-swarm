"""Interactive Investigation Completion — full Epstein/Meridian public atlas + always-online swarm."""
from __future__ import annotations
import json
import sys
from pathlib import Path
import asyncio

import streamlit as st

ROOT_SWARM = Path("/workspace/artifacts/permanent-agent-swarm")
sys.path.insert(0, str(ROOT_SWARM))
ATLAS = Path("/workspace/artifacts/investigation-complete/COMPLETION_ATLAS.json")

st.set_page_config(page_title="Investigation Completion Atlas", layout="wide")
st.title("Investigation Completion Atlas")
st.caption("PUBLIC RECORD CEILING · 8 pipelines · associates · DM-1..10 · ALWAYS-ONLINE permanent swarm · U15–U28")

data = json.loads(ATLAS.read_text(encoding="utf-8")) if ATLAS.exists() else {"pipelines": []}

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Pipelines", "Associates", "Discovery Methods", "Completeness",
    "Swarm LIVE", "ACH Verify", "Evidence Links", "Export",
])

def pipeline_score(p: dict) -> float:
    if p.get("completeness_hint") is not None:
        return float(p["completeness_hint"])
    wp = len(p.get("waypoints") or [])
    roles = len(p.get("roles") or []) if isinstance(p.get("roles"), list) else (1 if p.get("roles") else 0)
    tl = len(p.get("timeline") or [])
    exhibits = len(p.get("exhibits") or [])
    nxt = len(p.get("next") or [])
    s = min(100.0, wp * 8 + roles * 5 + tl * 4 + exhibits * 3 + nxt * 2)
    if p.get("status") == "paused_CONTRADICTED":
        s = min(s, 40.0)
    return s

with tab1:
    ids = [p["id"] + " — " + p["name"] for p in data.get("pipelines", [])]
    if not ids:
        st.warning("No atlas loaded")
    else:
        choice = st.selectbox("Pipeline", ids)
        p = data["pipelines"][ids.index(choice)]
        st.subheader(f"{p['id']} — {p['name']}")
        st.write(f"**Status:** `{p.get('status')}` · **Completeness hint:** {pipeline_score(p):.0f}%")
        st.write(p.get("summary", ""))
        if p.get("waypoints"):
            st.markdown("#### Waypoints")
            st.dataframe(p["waypoints"], use_container_width=True)
        if p.get("roles"):
            st.markdown("#### Roles")
            st.dataframe(p["roles"], use_container_width=True)
        if p.get("timeline"):
            st.markdown("#### Timeline")
            st.dataframe(p["timeline"], use_container_width=True)
        if p.get("exhibits"):
            st.markdown("#### Exhibits")
            st.write(p["exhibits"])
        if p.get("next"):
            st.markdown("#### Next leads")
            st.write(p["next"])
        if p.get("verdict"):
            st.error(f"Verdict: {p['verdict']}")
            st.write(p.get("rule", ""))

with tab2:
    st.dataframe(data.get("associates_public", []), use_container_width=True)

with tab3:
    st.dataframe(data.get("discovery_methods", []), use_container_width=True)
    st.info("Method validity ≠ claim truth. Tag every output SOLID/MAYBE/CONTESTED/CONTRADICTED.")

with tab4:
    scores = []
    for p in data.get("pipelines", []):
        scores.append({
            "id": p.get("id"),
            "name": p.get("name"),
            "status": p.get("status"),
            "score": pipeline_score(p),
        })
    if scores:
        overall = sum(s["score"] for s in scores) / len(scores)
        st.metric("Overall completion %", f"{overall:.1f}")
        st.dataframe(scores, use_container_width=True)
        st.progress(min(1.0, overall / 100.0))
        gaps = [s for s in scores if s["score"] < 50]
        if gaps:
            st.warning(f"Gaps (<50%): {[g['id'] for g in gaps]}")
        if st.button("Run CompletenessAuditor agent"):
            try:
                from agents.permanent_runtime import build_permanent_swarm
                swarm = build_permanent_swarm()
                out = asyncio.run(swarm.agents["CompletenessAuditor"].run({}))
                st.json(out)
            except Exception as e:
                st.error(str(e))

with tab5:
    st.markdown("### Permanent Swarm — LIVE always-online run")
    goal = st.text_input("Public research goal", "Public FOIA EpsteinDocs archive.org index")
    if st.button("Run full permanent swarm"):
        try:
            from agents.permanent_runtime import build_permanent_swarm
            swarm = build_permanent_swarm()
            with st.spinner(f"{swarm.roster().get('n_agents', 24)}-agent pipeline..."):
                result = asyncio.run(swarm.run(goal))
            st.success(result.get("status"))
            st.json({
                "status": result.get("status"),
                "permanent_swarm": result.get("permanent_swarm"),
                "n_agents": result.get("n_agents"),
                "always_online": (result.get("always_online") or {}).get("status"),
                "memory_snapshot": result.get("memory_snapshot"),
                "n_claims": len(result.get("claims") or []),
                "health_flags": (result.get("health") or {}).get("open_flags"),
            })
            with st.expander("Full results"):
                st.json(result)
        except Exception as e:
            st.error(str(e))

with tab6:
    st.markdown("### Bayesian ACH claim verify")
    claim = st.text_area("Claim (public)", "Federal FOIA responses are due within 20 working days per statute.")
    sources = st.text_input("Sources (comma URLs)", "https://www.justice.gov/oip/foia-guide")
    if st.button("Verify with TruthVerifier"):
        try:
            from agents.permanent_runtime import build_permanent_swarm
            swarm = build_permanent_swarm()
            tv = swarm.agents["TruthVerifier"]
            src = [s.strip() for s in sources.split(",") if s.strip()]
            out = asyncio.run(tv.run({"claim": claim, "sources": src}))
            st.json(out)
        except Exception as e:
            st.error(str(e))

with tab7:
    pe = data.get("public_evidence_index") or {}
    st.markdown("### Public evidence linker")
    st.write(pe)
    st.markdown("#### Drive delta folders (IDs)")
    st.json(data.get("drive_delta_folders") or {})
    st.markdown("#### Epstein specific children (titles)")
    st.write(data.get("drive_epstein_specific_children") or [])
    st.caption("Large PDFs: title-index only. Never secret-store.")

with tab8:
    st.download_button(
        "Download COMPLETION_ATLAS.json",
        data=ATLAS.read_text(encoding="utf-8") if ATLAS.exists() else "{}",
        file_name="COMPLETION_ATLAS.json",
        mime="application/json",
    )
    st.markdown("""
### Dual-persist checklist
1. Drive skill-tree / investigation-complete / permanent-agent-swarm
2. GitHub live-online-agent-swarm + meridian-drive-vault-atlas
3. Never upload keys.env / secret-store
""")
    if data.get("upgrades_this_run"):
        st.markdown("### U15–U28")
        st.write(data["upgrades_this_run"])

st.sidebar.markdown("### Ceiling")
st.sidebar.code(data.get("ceiling", "public only"))
st.sidebar.markdown("### Claim tags")
st.sidebar.write(data.get("claim_tags", []))
st.sidebar.markdown("### Never")
st.sidebar.write(data.get("never_list", []))
