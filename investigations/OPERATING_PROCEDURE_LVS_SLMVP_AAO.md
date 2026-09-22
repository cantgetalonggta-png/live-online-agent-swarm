# PERMANENT OPERATING PROCEDURE
## LVS → SLMVP → AAO
**Status**: PERMANENT — swarm default for every investigation and educator deep-dive  
**Version**: 1.0 · 2026-09-22  
**Pipeline**: Latent Vector Space → System-Level Modifier Validation Pipeline → Atomized Artifact Output

This document is the reloadable artifact form of HQ → Doctrine. Chat is the index; this file + HQ + GitHub + Drive are the product.

---

## Registered Modifiers (must fire every cycle)

| ID | Name | Pass/fail test |
|----|------|----------------|
| M1 | Public-record ceiling | No private data, no creds, no unauthorized access |
| M2 | HITL=YES | Bulk ingest / GitHub / Drive require operator authorization |
| M3 | Dual-anti-narrative | Both 2020-media slogans and Telegram overclaims can be OVERSTATED |
| M4 | Tag discipline | SOLID only with primary documents |
| M5 | Process ≠ origin | Debarment/FOIA/6-ft do not close H1 |
| M6 | Category-error watch | Methods overlap ≠ identity of ideologies |

---

## Chapter 1 — Latent Vector Space (LVS)

**Thesis**: Meaning is geometry. Claims, documents, agents, and hypotheses occupy positions. Distance is disagreement; direction is a modifier. Do not pool rare facts into one mushy embedding.

### Comparative table

| Approach | Opposite | Why it matters |
|----------|----------|----------------|
| Single dense vector (lossy pool) | Multi-vector / atom (claim-level) | Pooling kills rare IDs (grant numbers, FCS, March 25) |
| Reconstruction latents | Semantic latents | Pretty ≠ decision-useful |
| Superposed activations | Disentangled atoms | Superposition hides facts |

### Phase 1 — Preparation (define the space)

#### Step p1s1 — Declare objects that may occupy the space
**The Why**: Wrong unit of analysis makes every similarity a lie. "The pandemic" is not a unit; "this claim / email / sequence / grant clause" is.

**Foundational theory**: Embedding is a map f: object → ℝⁿ. Object grammar is the ontology. Superposition is the failure mode of coarse grammar.

**Granular execution**:
1. Enumerate object types: Document, Chunk, Entity, Claim, Hypothesis, Agent, Modifier, Artifact.
2. Stable IDs: C01…Cnn, H1…Hk, sk_*, agent ids.
3. Forbid pooling a 557-page report into one vector. Minimum grain = one claim or footnote-backed proposition.
4. Provenance on every object: URL/PDF page, timestamp, hash.

**Tools**: Public-record ceiling (HITL=YES); SHA-256 of source; Claim schema {id,text,tag,why,source}; mindset geometry-over-rhetoric.

**Pitfalls & fixes**:
- Mistake: Embedding headlines ("lab leak proven"). Fix: Testable sentence + SOLID/CONTESTED/OVERSTATED/IRREGULARITY.
- Mistake: One vector per agent report. Fix: One vector per finding; report is a container.

**KPI**: Every object type listed with example ID; no unlabeled blobs.

#### Step p1s2 — Choose axes that correspond to decisions, not vibes
**The Why**: Must separate process failure vs origin, confidence vs probability, mechanism vs mortality. Mixing axes turns death tolls into "proof of manufacture."

**Foundational theory**: Semantic spaces beat reconstruction spaces for planning; axes must be decision-relevant.

**Granular execution**:
1. Axis A: epistemic tag (SOLID / CONTESTED / OVERSTATED / IRREGULARITY).
2. Axis B: hypothesis support (H1/H2/H3 signed weights).
3. Axis C: source quality (primary .gov / FOIA / peer-review / IC / secondary).
4. Axis D: incentive/conflict.
5. Refuse a single "truthiness" axis.

**Tools**: ACH matrix; source-quality weights; COI flag.

**Pitfalls & fixes**:
- Mistake: Media consensus as axis. Fix: Primary document, not chyrons.
- Mistake: Collapsing confidence and probability. Fix: Store both (CIA low-conf lean ≠ low probability).

**KPI**: Four named axes; new claim plotable in <2 minutes.

### Phase 2 — Execution (place objects)

#### Step p2s1 — Ingest and chunk at claim grain
**The Why**: ColBERT-style late interaction keeps token vectors because pooling destroys rare identifiers. Same rule for claims.

**Foundational theory**: Dense single-vector retrieval is lossy for R01AI110964 / DEFUSE / March 25. Knowledge atomization exists because superposition hides facts.

**Granular execution**:
1. Hash source; re-ingest on hash change.
2. Extract by section (pdfplumber); keep page anchors.
3. Split to claims: one proposition, one tag, one why, one source list.
4. Link Claim—SUPPORTED_BY→Source; Claim—ABOUT→Entity.

**Tools**: pdfplumber; graph schema; SHA-256.

**Pitfalls & fixes**:
- Mistake: Skipping image pages then claiming full read. Fix: Log extraction density; second-pass footnotes.

**KPI**: Every claim has page/document pointer; coverage % known.

---

## Chapter 2 — System-Level Modifier Validation Pipeline (SLMVP)

**Thesis**: A modifier steers the space. System-level means whole-swarm enforcement. Validation tests honest geometry change, not partisan sign-flip.

### Comparative table

| Approach | Opposite | Why it matters |
|----------|----------|----------------|
| Prompt vibe ("be based") | System gate (tag, source, HITL) | Vibes not reproducible |
| Unvalidated anti-mainstream | Validated dual-anti-narrative | If only one tribe dies, modifier failed |

### Phase 1 — Register modifiers

#### Step p3s1 — Atomize modifiers
**The Why**: Unnamed modifiers cannot be validated. "Common sense" is not a test; "SOLID requires primary docs" is.

**Foundational theory**: Latent edit z_q = z_ref + α(Σadd − Σremove). Named modifiers are the clauses; validation = faithfulness + separability.

**Granular execution**: Register M1–M6 with pass/fail tests (table above).

**Tools**: This playbook; tag enum; HITL flag.

**Pitfalls & fixes**:
- Mistake: "Avoid mainstream" = inverse of CNN 2020. Fix: ACH; OVERSTATED both sides.
- Mistake: HITL theater. Fix: No Drive/GitHub without SOLID/CONTESTED split written.

**KPI**: Six named modifiers with tests; reports cite which fired.

### Phase 2 — Validate against both tribes

#### Step p4s1 — Adversarial pass on every major claim
**The Why**: Confirmation bias is default. Equal effort to kill H1 and H2.

**Foundational theory**: Heuer ACH; Bayesian likelihood ratios; CIA 2025 low-conf both-plausible is a modifier test.

**Granular execution**:
1. FOR and AGAINST on same card.
2. M3: no primary doc → not SOLID.
3. M5: process SOLID even if origin CONTESTED.
4. Confidence separate from probability.

**Tools**: ACH; likelihood notes; source weights.

**Pitfalls & fixes**:
- Mistake: 7.1M deaths → manufactured. Fix: Mortality ≠ mechanism.
- Mistake: Debarment = genetic proof. Fix: Sequences still must match; published EcoHealth chimeras do not.

**KPI**: Every C01–C11 has FOR, AGAINST, tag, modifier IDs.

---

## Chapter 3 — Atomized Artifact Output (AAO)

**Thesis**: Output is atoms: SkillAtoms, ClaimAtoms, agent reports, ACH, HTML, Drive/GitHub. If not citable/tagged/versioned, it did not ship.

### Comparative table

| Approach | Opposite | Why it matters |
|----------|----------|----------------|
| Mega-narrative | Tagged atoms + synthesizer | Hides OVERSTATED clauses |
| Chat-only | App + GitHub + Drive + HTML | Session death otherwise |

### Phase 1 — Emit atoms

#### Step p5s1 — Write ClaimAtoms and SkillAtoms to schema
**The Why**: Free-text-only encyclopedias die. Schema reloads state next cycle.

**Foundational theory**: Atom Theory (representability, sparsity, separability) + skill schema {id,name,definition,purpose,inputs,outputs,dependencies,tags,version,lineage}.

**Granular execution**:
1. ClaimAtom: {id, text, tag, why, sources[], modifiers[]}
2. SkillAtom: sk_* Title Case + full schema
3. AgentReport: do not collapse findings into verdict only
4. Always emit: MD, JSON, HTML, Drive, GitHub

**Tools**: skill-engine/state.json; swarm.ts; doctrine.ts; GitHub; Drive.

**Pitfalls & fixes**:
- Mistake: Chat dump = shipped. Fix: HQ + GitHub + Drive must exist.
- Mistake: Versionless overwrite. Fix: Bump version; lineage.

**KPI**: Third party reconstructs tags from HQ/Doctrine/GitHub/Drive without chat.

### Phase 2 — Educator wrapper (macro-to-micro)

#### Step p6s1 — Apply mandatory step template
**The Why**: Summarizing loses modifiers. Template forces measurement.

**Foundational theory**: Retrieval + worked examples beat generic advice. Volume prevents skipped gates; H2/H3 layout prevents blending.

**Granular execution** (every step forever):
1. Phase header
2. Step title (verb + object)
3. The Why
4. Nested execution (1 / a / i)
5. Tools/resources (incl. mindset)
6. Pitfalls & fixes (2–3)
7. KPI before next
8. Contrast table vs opposite where claims appear

**Tools**: Doctrine page (canonical); TagPill language; HITL.

**Pitfalls & fixes**:
- Mistake: 40 pages, no KPI. Fix: Unfalsifiable = literature not pipeline.
- Mistake: Skip "obvious" (hash PDF, name axes). Fix: Silent errors compound there.

**KPI**: New investigation walks Chapter 1→2→3 without inventing a new method.

---

## Enforcement

Every future swarm cycle and educator deep-dive **must**:
1. Place objects in LVS at claim grain
2. Fire M1–M6 and log which passed
3. Ship AAO pack (MD/JSON/HTML/GitHub/Drive)
4. Use educator template on every step

Lineage tags: `doctrine_v1`, `sk_lvs_slmvp_aao_pipeline`
