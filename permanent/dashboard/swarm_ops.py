"""Streamlit Swarm Ops Board — always-online matrix + live run."""
from __future__ import annotations
import asyncio
import json
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

st.set_page_config(page_title="Permanent Swarm Ops", layout="wide")
st.title("Permanent Agent Swarm — Ops Board")
st.caption("ALWAYS ONLINE · every agent wired · public-record ceiling · HITL")

from agents.permanent_runtime import build_permanent_swarm
from tools.registry import REGISTRY
from utils.always_online import assert_always_online

swarm = build_permanent_swarm()
roster = swarm.roster()
online = assert_always_online(roster["agents"])
matrix = REGISTRY.agent_tool_matrix()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Agents", roster["n_agents"])
c2.metric("Live web", "ON" if online.get("live_web") else "OFF")
c3.metric("Online gate", online.get("status", "?"))
c4.metric("Tools impl", REGISTRY.readiness().get("tools_impl", 0))

tab1, tab2, tab3, tab4 = st.tabs(["Roster", "Tool matrix", "LIVE run", "Readiness JSON"])

with tab1:
    st.json(roster)

with tab2:
    st.json(matrix)
    st.dataframe(
        [
            {"agent": k, "n_tools": v["n_tools"], "live": v["live_capable"], "tools": ", ".join(v["tools"])}
            for k, v in matrix["agents"].items()
        ],
        use_container_width=True,
    )

with tab3:
    goal = st.text_input("Goal", "Public FOIA EpsteinDocs archive.org index")
    if st.button("Run permanent swarm"):
        with st.spinner("Full pipeline..."):
            result = asyncio.run(swarm.run(goal))
        st.success(result.get("status"))
        st.json({
            "status": result.get("status"),
            "n_agents": result.get("n_agents"),
            "n_claims": len(result.get("claims") or []),
            "always_online": result.get("always_online", {}).get("status"),
            "memory": result.get("memory_snapshot"),
        })
        with st.expander("Full"):
            st.json(result)

with tab4:
    st.json(online)

st.sidebar.markdown("### Policy")
st.sidebar.code("PERMANENT_SWARM=true\nALWAYS_ONLINE=true\nPUBLIC_RECORD_CEILING=true")
