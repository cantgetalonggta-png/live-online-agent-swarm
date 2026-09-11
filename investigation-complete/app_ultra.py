"""Meridian Ultra Atlas interactive — full people/entities/methods/locations."""
from __future__ import annotations
import json
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
ULTRA = ROOT / "MERIDIAN_ULTRA_ATLAS.json"
ATLAS = ROOT / "COMPLETION_ATLAS.json"
PLATES = ROOT / "plates"

st.set_page_config(page_title="Meridian Ultra Atlas", layout="wide")
st.title("Meridian Ultra Atlas")
st.caption("PUBLIC RECORD CEILING · 41 people · 20 entities · 30 locations · DM-1..10 full · 8 pipelines · schematic plates only")

data = json.loads(ULTRA.read_text(encoding="utf-8")) if ULTRA.exists() else {}
st.sidebar.code(data.get("ceiling", "public only")[:200])
st.sidebar.metric("People", data.get("stats", {}).get("n_people", 0))
st.sidebar.metric("Locations", data.get("stats", {}).get("n_locations", 0))
st.sidebar.metric("Methods", data.get("stats", {}).get("n_methods", 0))

tabs = st.tabs([
    "Overview", "People", "Entities", "Locations", "Methods DM", "Pipelines",
    "Timeline", "Logic chain", "Plates", "Photo policy", "Export",
])

with tabs[0]:
    st.json(data.get("stats"))
    st.markdown("### DOJ inner-circle diagram names (public press)")
    st.write(data.get("doj_inner_circle_public_diagram"))
    st.markdown("### Public evidence")
    st.json(data.get("public_evidence_index"))
    st.markdown("### Sources ingested")
    st.write(data.get("sources_ingested"))

with tabs[1]:
    people = data.get("people") or []
    filt = st.multiselect("Filter pipelines", sorted({p for x in people for p in x.get("pipelines", [])}))
    tagf = st.multiselect("Filter photo policy", ["public_wiki", "public_press_only", "none", "never"])
    rows = []
    for p in people:
        if filt and not any(x in p.get("pipelines", []) for x in filt):
            continue
        if tagf and p.get("photo_policy") not in tagf:
            continue
        rows.append({
            "id": p["id"], "name": p["name"], "roles": "; ".join(p.get("roles", [])[:2]),
            "pipelines": ",".join(p.get("pipelines", [])), "tag": p.get("tag"),
            "photo": p.get("photo_policy"), "window": p.get("window"),
        })
    st.dataframe(rows, use_container_width=True, height=420)
    choice = st.selectbox("Detail", [f"{p['id']} — {p['name']}" for p in people])
    if choice:
        p = people[[f"{x['id']} — {x['name']}" for x in people].index(choice)]
        st.markdown(f"#### {p['name']}")
        st.write(p)
        if p.get("photo_refs"):
            st.markdown("**Public photo refs (open yourself — not embedded deepfakes):**")
            for u in p["photo_refs"]:
                st.markdown(f"- {u}")
        if p.get("photo_policy") == "never":
            st.error("Photo policy NEVER — victims / private / CONTRADICTED identity: no images.")

with tabs[2]:
    st.dataframe(data.get("entities") or [], use_container_width=True)

with tabs[3]:
    st.dataframe(data.get("locations") or [], use_container_width=True)

with tabs[4]:
    for m in data.get("discovery_methods") or []:
        with st.expander(f"{m['id']} — {m['name']} [{m.get('default_tag')}]"):
            st.write(m.get("detail"))
            st.write("**Inputs:**", m.get("inputs"))
            st.write("**Procedure:**", m.get("procedure"))

with tabs[5]:
    pipes = data.get("pipelines") or []
    for p in pipes:
        with st.expander(f"{p['id']} — {p['name']} [{p.get('status')}] ~{p.get('completeness_hint')}%"):
            st.write(p.get("summary"))
            st.write("**Chain:**", p.get("chain"))
            st.write("**Roles:**", p.get("roles_chain"))
            st.write("**Exhibits:**", p.get("exhibits"))
            st.write("**People IDs:**", p.get("people_ids"))
            if p.get("verdict"):
                st.error(p["verdict"])
            st.write("**Next:**", p.get("next"))

with tabs[6]:
    st.dataframe(data.get("master_timeline") or [], use_container_width=True)

with tabs[7]:
    lc = data.get("logic_chain") or {}
    st.write(lc.get("name"))
    st.dataframe(lc.get("steps") or [], use_container_width=True)
    st.info(lc.get("note"))
    st.markdown("### BC-PIPE")
    st.dataframe(data.get("bc_pipe") or [], use_container_width=True)
    st.markdown("### Redaction initials")
    st.json(data.get("redaction_initials_part2"))

with tabs[8]:
    st.markdown("### Schematic plates (no photoreal faces)")
    for name in ["pl01_global_waypoints.png", "pl02_eastern_feeder_chain.png", "pl03_network_roles.png", "pl04_timeline.png"]:
        path = PLATES / name
        if path.exists():
            st.image(str(path), caption=name, use_container_width=True)
        else:
            st.warning(f"Missing {name}")

with tabs[9]:
    st.json(data.get("photo_policy"))
    st.markdown("### Never list")
    st.write(data.get("never_list"))
    st.warning("AI image generation of real-person likenesses is not used here without a reference workflow. Wikipedia links are provided for public figures only. Victims: names only.")

with tabs[10]:
    if ULTRA.exists():
        st.download_button("Download MERIDIAN_ULTRA_ATLAS.json", ULTRA.read_text(encoding="utf-8"),
                           file_name="MERIDIAN_ULTRA_ATLAS.json", mime="application/json")
    md = ROOT / "MERIDIAN_ULTRA_ATLAS.md"
    if md.exists():
        st.download_button("Download MERIDIAN_ULTRA_ATLAS.md", md.read_text(encoding="utf-8"),
                           file_name="MERIDIAN_ULTRA_ATLAS.md", mime="text/markdown")
