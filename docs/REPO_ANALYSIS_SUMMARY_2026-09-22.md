# Repository Analysis Summary
**Repo:** https://github.com/cantgetalonggta-png/live-online-agent-swarm  
**HEAD:** `19cabba196d5f0036ae42823266fb76428059d57` (2026-09-22 14:06 UTC)  
**Tree:** not truncated · **716** objects · **563** files · **153** directories  
**Drive destination:** NEW_AUTONOMOUS_Project  
**Generated:** 2026-09-22T14:18Z

## What this repo is

Live Online Investigation Swarm: a multi-agent public-record investigation stack. Declared stack is **Bayesian ACH + hybrid Graph RAG + FastAPI + Streamlit + HITL**, with a **public-record ceiling** (no private-data harvest, no unauthorized access).

Runtime entrypoints:
- `python main.py "<goal>"` — CLI swarm
- `python main.py --api` / `uvicorn api.app:app` — FastAPI `:8000`
- `streamlit run dashboard/app.py` — dashboard `:8501`

Optional Redis (`REDIS_URL`) for persistence + RedisGraph; fallback is in-memory NetworkX.

## Architecture (as documented)

```
Supervisor
  ├── Compliance (public-record + HITL gate)
  ├── OSINTCollector  ──┐
  ├── LiveWebScout    ──┼── parallel fan-out
  ├── Pattern         ──┘
  ├── TruthVerifier   ← Bayesian BN + ACH → SOLID / MAYBE / CONTESTED / CONTRADICTED
  ├── MemoryVault     ← Hybrid Graph RAG
  ├── Anticipation
  └── Synthesizer
```

Graph schema: `(:Document)-[:HAS_CHUNK]->(:Chunk)-[:MENTIONS]->(:Entity)` plus `Claim-SUPPORTED_BY-Source`.

Hard rules in README:
1. Public records / operator-supplied public material only
2. HITL for bulk ingest, external actions, irreversible decisions
3. SOLID/MAYBE tagging on every claim
4. No private data, credentials, or unauthorized access
5. Provenance (URL + timestamp + hash) on every claim

## Top-level layout

| Path | Role |
|------|------|
| `main.py`, `swarm_runtime.py`, `swarm_config.py` | Process factory / CLI |
| `api/app.py` | FastAPI: `/swarm/run`, `/verify`, `/rag/*`, `/claims`, `/graph/*`, `/health` |
| `dashboard/app.py` | Streamlit: Run Swarm, Bayesian Verify, Graph RAG, Claims & Memory, Health |
| `agents/` | Supervisor + research + specialized + background |
| `utils/` | Bayesian ACH, Graph RAG, memory, directives, monitor |
| `tools/` | Tool adapters |
| `skills/` | Skill packages (32 files) |
| `skill-engine/` | Distill/export state (14 files) |
| `docs/` | Doctrine, encyclopedia, FOIA/OA, deploy reports (43 files) |
| `doctrine/` | Operating doctrine |
| `investigations/` | Case files — **largest bucket (231 files)** |
| `vault/` | Evidence vault — **91 files**, includes large ACRIS JSON |
| `permanent/` | Frozen artifacts (65 files) |
| `research/` | Research notes (28 files) |
| `investigation-complete/`, `drive-delta/`, `scans/`, `src/` | Completions, deltas, scans |
| `.github/workflows/skill-validate.yml` | CI skill validation |
| `.env.example` | Config template |

## Agent modules (code)

- `agents/supervisor.py` — orchestration (~3.8 KB)
- `agents/base.py` — base agent
- Research: `live_web_scout.py`, `osint_collector.py`, `truth_verifier.py`
- Specialized: `compliance.py`, `memory_vault.py`, `pattern.py`, `synthesizer.py`
- Background: `anticipation.py`

These are small specialist modules, not a huge runtime. Most of the repo mass is **investigative documents and encyclopedias**, not application code.

## Dependencies (`requirements.txt`)

`pydantic>=2`, `python-dotenv`, `fastapi>=0.110`, `uvicorn[standard]`, `streamlit>=1.30`, `networkx>=3`, `redis>=5`, `numpy`, `scikit-learn`, `pandas`, `aiohttp`, `httpx>=0.27`.

No LLM SDK is pinned in requirements. Swarm “intelligence” is expected to be provided by the operator / Grok session, not a bundled model client.

## File-type mix

| Ext | Count | Note |
|-----|------:|------|
| `.md` | 344 | Dominant — docs, encyclopedias, case writeups |
| `.py` | 91 | Runtime + agents + utils |
| `.json` | 43 | Skill trees, matrices, API verify dump |
| `.txt` | 41 | Extracted primary text (EFTA, SSCP sections) |
| `.html` | 21 | Dashboards |
| `.csv` | 12 | Tabular extracts |
| `.pdf` | 3 | Sparse in-repo; most PDFs live on Drive |
| `.yml` / `.yaml` / `.ts` | few | CI + stray TS |

## Largest objects (size ≠ importance)

1. `vault/.../ACRIS/legals_block_1441.json` — 1.11 MB  
2. Several `investigations/.../15_EFTA_PRIMARY/text/EFTA*.txt` — 120–415 KB  
3. `docs/GOD_TIER_SYSTEM/II_SKILL_TREE/SKILL_TREE_200_NODES.json` — 158 KB  
4. `docs/H15_PUBLIC_DEPLOY/API_VERIFY_REPORT.json` — 85 KB  
5. `investigations/sscp_sections/ecohealth.txt` — 100 KB  

Implication: the repo is also a **case archive** (trust/ACRIS/EFTA + SSCP extracts), not only a framework.

## Recent commit spine (same day, newest first)

| SHA (short) | Message |
|-------------|---------|
| `19cabba` | cycle 28: per-skill encyclopedia verification + architecture ship |
| `7120f11` | docs: architecture domains + frameworks pack (LVS SLMVP AAO FOIA LEO) |
| `e01db33` | docs: complete 128-skill encyclopedia expansion verified cycle 27 |
| `dbb5ced` | docs: general ontology skill/method tree (no single-thesis lock) |
| `2cf11b5` | docs: ingest export pack 2026-09-22 original-task locked verdict |
| `d2c564f` | deploy: ORIGINAL SSCP mission — process≠origin, LEO, FOIA, OA |
| `ee90555` / `4bdd147` | cycle 21 Unpaywall / Vaughn / `/primary` wire |
| `2529c72` | cycle 20 master dashboard + reviewer PASS |
| `173deb6` | cycle 19 C06 linguistic pack + SSCP FOIA dates |
| `154ca6e` / `f9bb505` | Phase 4 final / M38 lock; ForceAllowKernel discarded |
| `fa7fdbe` / `f3d9f47` | Phase 4 OA telemetry + LEO C01–C11 |
| `682e641` | Phase 2/3 document anti-tamper + LEO auto-verdicts |

Pattern: fast same-day documentation/doctrine cycles layered on a smaller Python core.

## What is solid

- Clear stated ceiling: public records + HITL + provenance.
- Runnable surface area is small and named: CLI, FastAPI, Streamlit.
- Hybrid RAG design is explicit (TF-IDF + graph expand, Redis optional).
- Bayesian ACH verdict vocabulary is consistent with later LEO work (SOLID / irregularity / omission).
- CI workflow exists (`skill-validate.yml`).
- Doctrine explicitly discarded ForceAllowKernel / invasive vectors (M38).

## Gaps / risks

1. **Docs heavier than runtime.** 200-node skill tree and 128-skill encyclopedia live in `docs/` and local Drive artifacts; many are markdown expansions, not executed Python skills.
2. **No pinned LLM client.** Swarm calls will no-op or depend on the host agent unless wired separately.
3. **Investigation PII/legal mass.** Trust/ACRIS/EFTA dumps are large. Treat as case work product; do not republish blindly.
4. **README path drift.** README still says `cd agent_swarm_live`; repo root is the project.
5. **Live endpoints in README are bind-all localhost** (`0.0.0.0:8000/8501`) — session-local, not a public deploy unless H15 docs say otherwise.
6. **PDF corpus mostly off-repo** (Drive folder `19WLfIAgWj1hIkYJaCmOb0CknPDX2_MVH` and this new folder). Git is the code+docs spine; Drive is the binary/dashboard spine.

## Operating fence (do not regress)

Authorized: `.gov` / FOIA reading rooms, OpenAlex, Unpaywall, official PDFs, operator-supplied public records.  
Forbidden in this project’s own lock: dump-dorks, directory fuzzing, private API bypass, onion scrapers, runtime mutation, ForceAllowKernel.

Keep **process-failure findings separate from origin conclusions**. Missing primaries → FOIA-warrant draft tag, do not invent pages.

## Recommended next operators

1. Treat `main.py` + `api/app.py` + `dashboard/app.py` as the executable product; keep encyclopedias in `docs/` versioned but not confused with runtime.
2. Add a one-page `ARCHITECTURE.md` at repo root pointing at FastAPI routes and agent graph (README already has most of it).
3. Mirror this summary into Git `docs/REPO_ANALYSIS_SUMMARY_2026-09-22.md` if you want GitHub and Drive in lockstep.
4. Keep automations on hourly 09–18 Vancouver; do not stampede `run_now` (rate-limit already observed).

## Pointers

- GitHub: https://github.com/cantgetalonggta-png/live-online-agent-swarm  
- This Drive folder: https://drive.google.com/drive/folders/1IqbRINg4f2ZoPz-3wai3k0kRjlHu8Lz-  
- Prior working Drive pack: https://drive.google.com/drive/folders/19WLfIAgWj1hIkYJaCmOb0CknPDX2_MVH  
