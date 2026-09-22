# RESEARCH PACK v1.0 — Permanent Swarm Learning Corpus
**Updated:** 2026-09-22T05:10:30.615215+00:00  
**Lineage:** doctrine_v2 × research_cycle4  
**Pipeline fit:** LVS (vectors) → SLMVP (gates) → AAO (atoms) + educator template  

Sources: 2026 industry comparisons (vector DB rankings), BenchLM Sep 2026 leaderboards, GraphRAG/ColBERT literature, Heuer ACH / Bayesian ACH papers. Treat leaderboard names as **time-stamped snapshots** (Sep 2026), not eternal truth.

---

# Part A — Vector Database Tools (LVS substrate)

## Foundational theory
A vector database stores high-dimensional embeddings and answers nearest-neighbor queries (ANN) under metrics such as cosine, L2, or inner product. For Meridian Swarm, vectors implement **LVS claim-grain placement**: each ClaimAtom (not whole report) is a point; metadata carries tag, hypothesis weights, source quality, COI.

## 2026 landscape split
| Class | Examples | Role |
|-------|----------|------|
| Vector-first | Pinecone, Qdrant, Weaviate, Milvus, Chroma, LanceDB | Built for ANN; filters bolted on |
| Vector-enabled general | Postgres+pgvector, sqlite-vec, DuckDB-vss, Redis/ES | ACID/SQL + vectors |

## Comparative matrix (production RAG, mid-2026 practitioner consensus)

| DB | Deploy | Hybrid | Comfortable scale | Cost shape | Pick when |
|----|--------|--------|-------------------|------------|-----------|
| **pgvector** | Postgres ext | FTS+HNSW compose | tens of M; 100M+ w/ pgvectorscale | Free if you have PG | Default: ACID + claims already relational |
| **Qdrant** | OSS + Cloud | dense+sparse, payload filters | 100M+ | Strong $/latency | Filtered high-throughput self-host |
| **Weaviate** | OSS + Cloud | BM25+HNSW deep hybrid | 100M+ | Managed steeper | GraphQL, multi-modal, hybrid depth |
| **Pinecone** | Managed only | sparse+dense | 100M–billions | Cheap start, steep scale | Zero-ops, data can leave |
| **Milvus/Zilliz** | OSS + Cloud | yes | hundreds of M–billions | Software cheap, ops heavy | True billion-scale |
| **Chroma** | Embedded/local | basic | small–medium | Free local | Prototypes, LangChain default |
| **LanceDB** | Local/edge | multi-vector support | medium | $0 local | Desktop/edge, frequent updates |
| **Vespa** | Self-host/cloud | best-in-class ranking | large | higher | Search+rank+recommend unified |

### Benchmarks (indicative, 1M×1536 curated community)
Qdrant / LanceDB often lead p50 latency; Pinecone leads ops simplicity; pgvector wins operational unity under ~10–50M vectors.

### Meridian Swarm recommendation (doctrine-aligned)
1. **Prototype:** Chroma or in-memory + claim JSON  
2. **Production investigation corpus:** **pgvector** (claims + tags + ACH columns in one SQL transaction) **or Qdrant** if filter latency dominates  
3. **Rare-ID preservation:** enable **multi-vector / MaxSim** backends (Qdrant ≥1.10, Weaviate ≥1.29, LanceDB ≥0.15, VectorChord for Postgres) — aligns with LVS claim that single dense pool kills grant numbers  
4. **Never:** one vector per 557-page PDF for decision work  

### KPI
- Claim retrieval Recall@k measured on labeled SSCP-style probes  
- Rare identifier retrieval (grant IDs, dates, DEFUSE) > dense-only baseline  

---

# Part B — Advanced Learning Language Models (Sep 2026 snapshot)

**Caveat (M3 dual-anti-narrative):** Leaderboards shift monthly; scores ≠ production fit. Use models as *agents* under SLMVP gates, not as oracles.

## Proprietary frontier (BenchLM / industry Sep 2026 — illustrative)
| Tier | Models (names as reported Sep 2026) | Typical role |
|------|-------------------------------------|--------------|
| Flagship reasoning | Claude Fable 5.1 / Claude Opus 5 class; GPT-6 Astra / GPT-5.x class; Gemini 3.x Pro | Hard ACH, long reasoning, agent orchestration |
| Fast / cheap | Gemini Flash class; Claude/GPT mid tiers | Bulk claim tagging, extraction |
| Agentic tool-use | Frontier models with tool calling + long context (0.5–1M+) | Swarm supervisor, multi-hop |

## Open-weight frontier (Sep 2026 snapshot)
| Model family | Notes |
|--------------|-------|
| **Qwen3.8 Max** class | Often tops open-weight aggregate scores; long context |
| **GLM-5.x** (Z.ai) | Strong all-round / agents; MIT-ish licenses on some |
| **DeepSeek V3/V4** class | Reasoning + coding efficiency; MIT lineage common |
| **Kimi K2/K3** class | Long-horizon coding agents |
| Edge: **Gemma 4**, small Qwen | Laptop/private |

## Gap (mid-2026 analyses)
Open weights ~months behind closed aggregate on broad intelligence indices; **near-parity** on some coding / long-context tasks. Choice = task + budget + data residency + recall risk.

## Swarm model routing (AAO practice)
| Agent role | Model preference |
|------------|------------------|
| Supervisor / ACH synthesizer | Flagship proprietary or best open with tool-use |
| Claim tagger (bulk) | Fast mid-tier or strong open |
| TruthVerifier adversarial | *Different* model family than author (reduce shared blind spots) |
| Local / air-gapped | Open weights only; log model id + hash in artifacts |

### KPI
Every ClaimAtom stores `model_id`, `prompt_hash`, `gate_ids_fired`. Reconstructability requires knowing *which* LLM tagged the claim.

---

# Part C — SLMVP Modifier Gates (expanded catalog)

## Existing permanent (M1–M6)
| ID | Gate | Pass/fail |
|----|------|-----------|
| M1 | Public-record ceiling | No private data/creds/unauthorized access |
| M2 | HITL=YES | Bulk ingest / GitHub / Drive need operator auth |
| M3 | Dual-anti-narrative | Both media-2020 *and* inverse-dogma can be OVERSTATED |
| M4 | Tag discipline | SOLID only with primary docs |
| M5 | Process ≠ origin | Debarment/FOIA/policy admissions do not close origin H |
| M6 | Category-error watch | Methods overlap ≠ identity of ideologies |

## Expanded gates (M7–M16) — register as optional→permanent after 1 cycle fire log

| ID | Gate | Theory | Pass/fail test | Failure mode if missing |
|----|------|--------|----------------|-------------------------|
| **M7** | Model-diversity | Shared LLM blind spots | Author agent and verifier use different model families *or* independent adversarial prompt | Correlated hallucination |
| **M8** | Confidence≠probability | IC epistemology | Both fields present on every ACH hypothesis | Over-read of "lean" |
| **M9** | Likelihood-ratio required | Bayesian ACH | Every posterior move cites LR note or "unquantified qualitative" flag | Vibes-as-Bayes |
| **M10** | Rare-ID retrieval | LVS multi-vector | Probe set of grant IDs/dates must retrieve | Dense-pool loss |
| **M11** | Reconstructability | AAO | Third party rebuilds tags from HQ+GitHub+Drive without chat | Session-only knowledge |
| **M12** | Capture-ratio | M3 optimization | OVERSTATED fire ratio poles ≤4:1 unless primary-doc asymmetry documented | Captured "anti-mainstream" |
| **M13** | Blend ban | Atom sparsity | No process+origin in one ClaimAtom sentence | Superposed claims |
| **M14** | Source-class floor | Epistemic hygiene | Secondary-only claims cannot be SOLID | Media as evidence |
| **M15** | Temporal re-project | Continual LVS | New primary hash triggers re-tag of affected claims | Frozen 2020 geometry |
| **M16** | Cost/latency budget | Ops | Explicit $ and p95 budget per cycle logged | Silent runaway API spend |

### How gates compose
```
ingest → M1,M2,M14
embed/place → M10,M13,M15
judge → M3,M4,M5,M6,M8,M9,M12
ship → M2,M11,M16
verify → M7
```

### KPI
Each swarm report includes `modifier_fire_log: [M1,M3,M4,...]` and at least one **failed** gate attempted (proves gates are not theater).

---

# Part D — Five Advanced Skills / Methods (autonomous selection)

Chosen for maximum leverage on Meridian Swarm + doctrine LVS→SLMVP→AAO:

## 1. Hybrid Dense+Sparse Retrieval + RRF
**Why:** Dense fails on exact IDs; sparse/BM25/SPLADE fails on paraphrase. Fusion (Reciprocal Rank Fusion) is the 2026 default enterprise baseline.  
**Execution:** index dense + sparse; RRF; optional cross-encoder or ColBERT rerank.  
**KPI:** Lift on rare-ID probes vs dense-only.

## 2. Multi-vector Late Interaction (ColBERT / MaxSim)
**Why:** Operationalizes LVS multi-vector theory — one vector per token; MaxSim scoring.  
**Backends:** Qdrant, Weaviate, LanceDB, VectorChord.  
**KPI:** Table/entity-heavy queries beat single-vector dense.

## 3. GraphRAG / Entity-Relation Subgraph Expansion
**Why:** Multi-hop questions ("how do EcoHealth terms relate to WIV GoF policy?") need edges, not top-k chunks. GraphRAG + vector-graph variants show large Recall lifts on multi-hop QA.  
**Execution:** Entity extract → relation triples → vector or Neo4j graph → subgraph expand → LLM rerank.  
**KPI:** Multi-hop claim chains C_i → C_j → H_k traversable.

## 4. Bayesian ACH (Heuer + likelihood ratios)
**Why:** Classical ACH marks consistent/inconsistent; Bayesian ACH forces priors, likelihoods, posteriors, and separates confidence from probability (M8/M9).  
**Execution:** Hypotheses H1…Hk; evidence matrix; diagnosticity; optional BN; report least-inconsistent *and* posterior.  
**KPI:** Every posterior change has an LR note or explicit unquantified flag.

## 5. Multi-Model Adversarial Swarm Orchestration
**Why:** Single-model swarms share blind spots. Route Supervisor / Tagger / TruthVerifier across families (M7).  
**Execution:** Fan-out agents; merge with tag discipline; HITL on external ship.  
**KPI:** Verifier model_id ≠ author model_id on ≥80% of CONTESTED claims.

### Honorable mentions (next cycles)
- SAE / knowledge atomization for claim disentanglement  
- Structured Analytic Techniques suite (Key Assumptions Check, Devil's Advocacy)  
- Evaluation harnesses (MuSiQue / HotpotQA-style multi-hop for investigation corpora)

---

# Part E — Integration map into permanent doctrine

```
[Documents] --extract--> [ClaimAtoms]
                | embed hybrid + multi-vector
                v
            [Vector DB / LVS]
                | Graph edges
                v
            [GraphRAG layer]
                | agents (multi-model)
                v
            [SLMVP M1–M16]
                | ACH Bayesian
                v
            [AAO pack: MD/JSON/HTML/GitHub/Drive]
```

## Enforcement
1. New research cycles append atoms to skill-engine, not only chat.  
2. Vector/LLM choices logged in META each cycle.  
3. Expanded gates M7–M16 start as **CONTESTED-operational** until fire-logged one full investigation, then promote to permanent with M1–M6.

## Sources (primary-style pointers for operators)
- Vector DB 2026 rankings: Suparbase / practitioner blogs (pgvector default; Qdrant perf; Pinecone ops)  
- BenchLM.ai Sep 2026 proprietary + open-weight boards  
- HuggingFace MultiVectorEncoder / ColBERT late interaction  
- GraphRAG / Vector-Graph RAG evaluations (multi-hop Recall lifts)  
- Heuer ACH; Bayesian ACH / HELP frameworks  

**Anti-overclaim:** Model names and scores dated Sep 2026; re-verify before production lock.
