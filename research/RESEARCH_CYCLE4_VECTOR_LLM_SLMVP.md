# DEEP RESEARCH CYCLE 4 — Permanent Learning Pack
Updated: 2026-09-22T05:08:22.073670+00:00

Pipeline still: **LVS → SLMVP → AAO**  
Explore UI: `/explore`  
Doctrine: `/doctrine` · v1.2 modifiers M1–M12

---

## 1. Vector database tools (2026 field)

| Store | Best for | Hard limit / cost shape |
|-------|----------|-------------------------|
| **pgvector** | Already on Postgres; <10–50M vectors; SQL+ACID | Hybrid is glue; latency past tens of M |
| **Qdrant** | Filter-heavy RAG; self-host price/perf | Need ops or cloud |
| **Weaviate** | Native hybrid BM25+vector; schema modules | Feature-rich, more surface |
| **Pinecone** | Zero ops, managed scale | Cost steep; data leaves; residency |
| **Milvus** | Billions; K8s | Ops heavy |
| **Chroma** | Prototype / embedded | Not multi-tenant SLA |
| **LanceDB / Turbopuffer class** | Sparse traffic, object storage | Different latency profile |

**Swarm rule (M12):** pick by constraint (ops, hybrid, scale, residency), not hype.  
**LVS rule:** claim-grain multi-vector > single dense pool of whole reports.  
**Industry consensus:** at small-medium scale, **chunking + embedding + rerank** beat which DB you pick.

### Decision tree for Meridian
1. Sandbox prototype claim search → Chroma or local FAISS  
2. Production claims + SQL metadata → **pgvector**  
3. Filter-heavy tag/source/COI queries at scale → **Qdrant**  
4. Graph-native entity retrieval → Weaviate or GraphRAG layer on top  
5. SaaS-only / no ops → Pinecone if M1 allows cloud  

---

## 2. Advanced LLMs (Sep 2026 snapshot)

Frontier rotates weekly. Use **role fit (M11)**, not brand loyalty.

| Role | Prefer | Why |
|------|--------|-----|
| Hard reasoning / ACH / educator | Frontier closed (Claude Fable/Opus class, GPT-6/5.6 Sol class, Gemini Pro) | Open-ended multi-step still leads closed |
| Bulk tag / NER / extract | Flash/budget or open-weight | Cost + speed |
| Coding agents | Frontier or strong open coders (DeepSeek V4, Qwen, Kimi) | Coding gap nearly closed |
| Self-host / residency | Open-weight (Llama 4, Qwen, DeepSeek, Mistral) | Data control |
| Embeddings | Dense + hybrid; multi-vector/late-interaction for rare IDs | Pooling kills grant numbers |

**Caveat:** leaderboards (BenchLM, Artificial Analysis, Vals) disagree by task. Never treat composite #1 as universal.

---

## 3. SLMVP modifier gates — full set M1–M12

### Core (M1–M6)
- M1 Public-record ceiling  
- M2 HITL=YES  
- M3 Dual-anti-narrative  
- M4 Tag discipline  
- M5 Process ≠ origin  
- M6 Category-error watch  

### Expanded (M7–M12)
- **M7 Reconstructability** — HQ+GitHub+Drive without chat  
- **M8 Confidence ≠ probability** — CIA low-conf ≠ low-P  
- **M9 Capture audit** — OVERSTATED pole ratios honest  
- **M10 Blended-claim ban** — process+origin not one sentence  
- **M11 Model-role fit** — job selects model  
- **M12 Vector-store fit** — constraint selects store  

### Gate composition patterns
| Pattern | Gates | Use |
|---------|-------|-----|
| Ingest | M1 M2 M4 M10 M12 | PDF → claims |
| Origin ACH | M3 M5 M8 M9 M11 | H1/H2/H3 |
| Ship | M2 M7 | GitHub/Drive |
| Pedagogy | M4 M7 + educator template | Deep-dives |

---

## 4. Five advanced methods (autonomous selection)

### 1) Agentic GraphRAG
Graph retrieval + multi-step agent. Agent walks entities/relations, not chunk soup. Fits SSCP entity density (grants, labs, people).

### 2) Sparse Autoencoder / Atom Theory
Sparse, separable, reconstructable features. Operational analog = ClaimAtoms. Do **not** assume SAE "reasoning" directions are causal without intervention tests.

### 3) Bayesian ACH + Belief Layers
Heuer ACH + likelihood ratios. Separate belief P from speech; log confidence vs probability (M8). AutoDS-style Bayesian surprise for open discovery.

### 4) Multi-agent scientific discovery loops
Generate → cluster → reflect → rank (Co-Scientist family). Meridian swarm already this; formalize phases.

### 5) Hybrid + late-interaction retrieval
BM25 + dense + rerank; ColBERT MaxSim for rare tokens. DB choice secondary to retrieval quality.

---

## 5. Emergent synthesis (cycle 4)

1. **LVS needs a store policy (M12)** before scale — start pgvector/JSON, graduate Qdrant when filters hurt.  
2. **SLMVP without M7–M10 was incomplete** — reconstructability, blend ban, capture audit close the loop.  
3. **LLM choice is a modifier (M11)**, not a personality cult.  
4. **GraphRAG + ACH + multi-agent** is the natural upgrade path for SSCP-class work.  
5. **SAE theory informs tagging** but does not replace primary-document discipline (M4).

---

## Enforcement
Every research claim in this pack is **secondary synthesis** (CONTESTED as product truth; SOLID only as "industry comparison consensus as of 2026 sources cited").  
Primary swarm claims still require primary docs (M4).

Lineage: research_cycle4 · doctrine_v1.2 · skill_cycle4
