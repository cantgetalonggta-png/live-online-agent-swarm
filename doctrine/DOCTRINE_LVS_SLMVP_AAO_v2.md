# PERMANENT DOCTRINE v2.0
# LVS → SLMVP → AAO
## Latent Vector Space → System-Level Modifier Validation Pipeline → Atomized Artifact Output

**Status:** PERMANENT — default operating system for every Meridian Swarm investigation and every educator deep-dive  
**Version:** 2.0  
**Updated:** 2026-09-22T04:57:02.267391+00:00  
**Lineage:** doctrine_v1 → doctrine_v2_exhaustive  
**Enforcement:** AGENTS.project.md · HQ `/doctrine` · skill atoms sk_lvs_* · sk_slmvp_* · sk_aao_* · sk_educator_*

---

# Chapter 1 — Latent Vector Space (LVS)

## Foundational Theory

A **latent vector space (LVS)** is a high-dimensional continuous field in which discrete objects (documents, claims, entities, hypotheses, agents, modifiers, artifacts) are mapped to points or sparse multi-vectors such that **geometric relations encode semantic relations**. In representation learning, an embedding is a map \(f: \mathcal{X} \to \mathbb{R}^n\). Distance approximates disagreement; direction approximates a *modifier* (an edit vector). Superposition — many concepts sharing one direction — is the primary failure mode when the object grammar is too coarse.

**Why LVS first:** Without a declared space, every later judgment collapses into rhetoric. You cannot measure "anti-narrative" honesty, tag discipline, or process-vs-origin separation if claims float as free text.

**Real-world case:** The SSCP 557-page report. Pooling the entire PDF into one dense vector erases grant number `R01AI110964`, the March 25 Directive, DEFUSE FCS-insertion language, and Morens FOIA-evasion phrases. Multi-vector / claim-grain storage (ColBERT-style late interaction analog) preserves those rare identifiers.

**Opposite approach:** Single "truthiness" score. That is narrative control wearing a number.

---

## Phase 1 — Preparation (Define the Space)

### Step p1s1 — Declare objects that may occupy the space

**The Why:**  
If the unit of analysis is wrong, every similarity is a lie. "The pandemic," "liberals," "the lab leak" are slogans, not objects. Investigation succeeds when the unit is *this claim, this email, this sequence feature, this grant clause, this IC assessment sentence*.

**Foundational theory:**  
Ontology precedes embedding. Object grammar = {Document, Chunk, Entity, Claim, Hypothesis, Agent, Modifier, Artifact}. Superposition research (sparse autoencoders / TSAE knowledge atomization) shows raw activations mix concepts; operational analog is a blended claim that mixes EcoHealth late reporting with "therefore bioweapon."

**Granular Execution Plan:**
1. Enumerate allowed object types (closed set until intentionally extended).
   a. Document — primary source PDF, FOIA dump, IC summary, court docket, peer-reviewed paper.
   b. Chunk — section/page-anchored text unit from extraction.
   c. Entity — person, org, grant ID, lab, sequence feature, policy rule.
   d. Claim — one testable proposition with tag + why + sources.
   e. Hypothesis — H1 lab accident, H2 zoonosis, H3 deliberate weapon (or domain equivalents).
   f. Agent — swarm role report container (not an atom; findings inside are atoms).
   g. Modifier — named steering rule M1…Mn with pass/fail test.
   h. Artifact — shipped MD/JSON/HTML/GitHub/Drive object with version + hash.
2. Assign stable ID schemes:
   a. Claims: `C01`…`Cnn`
   b. Hypotheses: `H1`…`Hk`
   c. Skills: `sk_<slug>`
   d. Agents: lowercase role id (`origins`, `truthverifier`, …)
   e. Modifiers: `M1`…`Mn`
3. Forbid pooling: minimum grain = one claim or one footnote-backed proposition. Never one vector per chapter for decision work.
4. Provenance required on every object: source URL or PDF page, ISO timestamp, SHA-256 of source file when applicable.
5. Write the object registry to JSON before any tagging begins.

**Required Tools/Resources:**
- Public-record ceiling (HITL=YES)
- SHA-256 of source PDF
- Claim schema `{id, text, tag, why, sources[], modifiers[]}`
- Mindset: geometry over rhetoric

**Common Pitfalls & Fixes:**
1. Mistake: Embedding headlines ("lab leak proven") instead of propositions.  
   Fix: Rewrite as a testable sentence; assign SOLID / CONTESTED / OVERSTATED / IRREGULARITY.
2. Mistake: One vector per agent report.  
   Fix: One vector (or record) per *finding* inside the report; agent report is a container.
3. Mistake: Free-text entities without IDs.  
   Fix: Normalize to Entity registry before claim authoring.

**KPI / Success Metric:**  
You can list every object type with at least one example ID. No unlabeled blobs remain. Object registry file exists and is hashed.

---

### Step p1s2 — Choose axes that correspond to decisions, not vibes

**The Why:**  
A latent space used for investigation must separate (1) process failure vs origin inference, (2) confidence vs probability, (3) mechanism vs mortality. Mixing those axes is how outcome magnitude (e.g., millions of deaths) is misused as likelihood of a specific mechanism.

**Foundational theory:**  
Semantic latents outperform reconstruction latents for planning because they preserve *action-relevant* structure. Investigation analog: axes must support decisions (tag, ACH weight, source quality), not "how spicy is this take."

**Granular Execution Plan:**
1. Axis A — Epistemic tag: SOLID | CONTESTED | OVERSTATED | IRREGULARITY.
2. Axis B — Hypothesis support: signed weights toward H1 / H2 / H3 (or domain set).
3. Axis C — Source quality: primary .gov / FOIA / peer-review / IC product / secondary commentary.
4. Axis D — Incentive/conflict: author is party to grant, paper, policy, or funding chain (boolean + note).
5. Explicitly refuse a single "truthiness" axis.
6. Store confidence and probability as *separate* fields (CIA "low confidence" ≠ "low probability").

**Required Tools/Resources:**
- ACH matrix template
- Source-quality weight table
- Conflict-of-interest flag field
- Dual-anti-narrative mindset (M3)

**Common Pitfalls & Fixes:**
1. Mistake: Using media consensus as an axis.  
   Fix: Primary document on the axis, not chyrons.
2. Mistake: Collapsing confidence and probability.  
   Fix: Two fields always.
3. Mistake: Mortality on the mechanism axis.  
   Fix: Outcome metrics stay off origin likelihood until a causal model links them.

**KPI / Success Metric:**  
Four named axes exist on paper/JSON. A new claim can be plotted on all four in under two minutes by a second operator.

---

## Phase 2 — Execution (Place Objects)

### Step p2s1 — Ingest and chunk at claim grain

**The Why:**  
Late-interaction multi-vector models keep one vector per token because pooling destroys rare identifiers. Operational analog: one record per claim, never one record per chapter.

**Foundational theory:**  
Dense single-vector retrieval is lossy for rare entities (grant numbers, DEFUSE language, specific dates). Knowledge-atomization research exists because superposition hides facts.

**Granular Execution Plan:**
1. Hash the source file (SHA-256). If hash changes, re-ingest; never silently mutate.
2. Extract text by section (e.g., pdfplumber); keep page anchors.
3. Log extraction density per page; flag sparse/image pages for second-pass footnote harvest.
4. Split to claims: one proposition, one tag, one why, one source list.
5. Link graph edges: Claim—SUPPORTED_BY→Source; Claim—ABOUT→Entity; Claim—SUPPORTS/REFUTES→Hypothesis.
6. Do not claim "word-for-word full read" without density coverage %.

**Required Tools/Resources:**
- pdfplumber (or equivalent)
- Graph schema Document-HAS_CHUNK-Chunk-MENTIONS-Entity
- SHA-256 tooling
- HITL gate before bulk external push

**Common Pitfalls & Fixes:**
1. Mistake: OCR-skipping image pages then claiming full ingest.  
   Fix: Coverage % known; second-pass harvest.
2. Mistake: One claim mixing process + origin.  
   Fix: Split (M5 Process ≠ origin).
3. Mistake: Secondary blogs as primary.  
   Fix: Source quality axis demotes them.

**KPI / Success Metric:**  
Every claim has a page or document pointer. Extraction coverage % is recorded. Hash of source is stored.

---

### Step p2s2 — Link and re-project after new evidence

**The Why:**  
Latent geometry is not static. A new FOIA drop or IC statement must move claim positions, not merely append a footnote.

**Foundational theory:**  
Continual learning analog: same metric, updated points. Freezing after first ingest produces drift relative to the public record.

**Granular Execution Plan:**
1. On new primary source: re-hash; re-tag only affected claims.
2. Recompute ACH weights for open hypotheses; do not reset unrelated SOLID process claims.
3. Log delta: which tags flipped, which posteriors moved, which modifiers re-fired.
4. Version-bump claim atoms; keep prior tag in lineage.

**Required Tools/Resources:**
- Versioned claims JSON
- ACH table
- UPDATE_LOG.md / CHANGELOG

**Common Pitfalls & Fixes:**
1. Mistake: Treating every news article as geometry update.  
   Fix: Only primary sources or IC products move axes.
2. Mistake: Silent overwrite of old tags.  
   Fix: Lineage + version on every flip.

**KPI / Success Metric:**  
Any tag flip has before/after and a source ID in the log.

---

## Phase 3 — Optimization (Space Hygiene)

### Step p2opt1 — Deduplicate and split blended claims

**The Why:**  
A claim that mixes EcoHealth late reporting with "therefore lab leak" fails sparsity and steers readers into M5 violations.

**Foundational theory:**  
Atom Theory criteria: representability, sparsity, separability. Blended claims are superposed concepts.

**Granular Execution Plan:**
1. Scan for "and therefore" glue between process and origin.
2. Split into two claims with independent tags.
3. Remove duplicates that share the same proposition under different IDs.
4. Re-plot on four axes.

**Required Tools/Resources:**
- claims_distilled.json
- TagPill rules
- M5 Process ≠ origin

**Common Pitfalls & Fixes:**
1. Mistake: Keeping a spicy blended claim because it "reads well."  
   Fix: Split first, synthesize later.
2. Mistake: Deduping away a claim that differs only on source quality.  
   Fix: Keep if source class differs; merge if identical proposition + same sources.

**KPI / Success Metric:**  
Zero claims that both assert a process fact and an origin conclusion in one sentence.

---

# Chapter 2 — System-Level Modifier Validation Pipeline (SLMVP)

## Foundational Theory

A **modifier** is any instruction that steers the latent space: "avoid mainstream narrative," "HITL=YES," "public-record ceiling," "do not overclaim manufacture." **System-level** means the modifier is enforced on the whole swarm, not whispered to one agent. **Validation** means testing whether the modifier changed geometry *honestly* — or merely flipped the partisan sign.

In latent arithmetic:  
\(z_q = z_{ref} + \alpha\left(\sum_{a \in A}(z_a - z_0) - \sum_{r \in R}(z_r - z_0)\right)\)  
Named modifiers are the add/remove clauses. Unspecified \(\alpha\) and unnamed clauses produce drift.

**Opposite approach:** Prompt-level vibe ("be based"). Vibes are not reproducible and leave no audit trail.

---

## Phase 1 — Register Modifiers

### Step p3s1 — Atomize modifiers with pass/fail tests

**The Why:**  
Unnamed modifiers cannot be validated. "Maximum common sense" is not a test. "No claim gets SOLID without a primary document" is a test.

**Foundational theory:**  
Gates leave audit trails. Capture occurs when a modifier only wounds one tribe's slogans.

**Granular Execution Plan:**
1. Register permanent modifiers:
   | ID | Name | Pass/Fail Test |
   |----|------|----------------|
   | M1 | Public-record ceiling | No private data, no creds, no unauthorized access |
   | M2 | HITL=YES | Bulk ingest / GitHub / Drive require operator authorization |
   | M3 | Dual-anti-narrative | Both 2020-media slogans AND Telegram overclaims can be OVERSTATED |
   | M4 | Tag discipline | SOLID only with primary documents |
   | M5 | Process ≠ origin | Debarment/FOIA/6-ft do not close H1 |
   | M6 | Category-error watch | Methods overlap ≠ identity of ideologies |
2. Each swarm report cites which modifiers fired.
3. New domain may add M7+ only with a written test.

**Required Tools/Resources:**
- Modifier registry (this doctrine)
- Tag enum
- HITL flag in META

**Common Pitfalls & Fixes:**
1. Mistake: "Avoid mainstream" = inverse of CNN 2020.  
   Fix: ACH; OVERSTATED available both sides.
2. Mistake: HITL theater (no actual gate).  
   Fix: No Drive/GitHub of new conclusions without written SOLID/CONTESTED split.
3. Mistake: Modifier without a test.  
   Fix: Delete it or write a one-line pass/fail.

**KPI / Success Metric:**  
Six named modifiers with tests. Every major report cites which fired.

---

## Phase 2 — Validate Against Both Tribes

### Step p4s1 — Adversarial pass on every major claim

**The Why:**  
Confirmation bias is the default human prior. The pipeline must spend equal effort trying to kill H1 and H2 (or domain equivalents).

**Foundational theory:**  
Analysis of Competing Hypotheses (Heuer) exists to stop analysts from marrying one story. Bayesian update uses likelihood ratios, not vibes. CIA-style "low confidence, both still plausible" is a modifier test: did you over-read a lean?

**Granular Execution Plan:**
1. For each claim card: strongest FOR and AGAINST in the same card.
2. Apply M3: anti-mainstream conclusion without primary doc → not SOLID.
3. Apply M5: process crimes stay SOLID even if origin stays CONTESTED.
4. Log confidence separately from probability.
5. Mortality / outcome magnitude does not multiply into mechanism likelihood without a causal model.

**Required Tools/Resources:**
- ACH matrix
- Likelihood notes
- Source-quality weights
- Dual-tribe checklist

**Common Pitfalls & Fixes:**
1. Mistake: Deaths count → manufactured.  
   Fix: Outcome ≠ mechanism.
2. Mistake: Debarment = genetic proof.  
   Fix: Sequences must match; published EcoHealth chimeras vs SARS-CoV-2 distance remains relevant.
3. Mistake: Only attacking the "other side."  
   Fix: Equal FOR/AGAINST effort is the KPI, not narrative victory.

**KPI / Success Metric:**  
Every C01–Cnn card has FOR, AGAINST, tag, and modifier IDs. No card is tag-only.

---

## Phase 3 — Optimization (Modifier Hygiene)

### Step p4opt1 — Kill captured modifiers

**The Why:**  
A modifier that only ever fires against one tribe is captured and must be rewritten or retired.

**Granular Execution Plan:**
1. Review last N cycles: which OVERSTATED tags hit tribe A vs B.
2. If ratio > 4:1 without primary-doc asymmetry, flag M3 failure.
3. Rewrite tests to force dual application.

**KPI:** Dual-anti-narrative fire log shows both poles hit within a cycle window when both overclaim.

---

# Chapter 3 — Atomized Artifact Output (AAO)

## Foundational Theory

**Atomized Artifact Output** means the product is a set of versioned, citable, schema-bound units — not a vibe essay. Ideal atoms satisfy representability (reconstruct source), sparsity (one issue), separability (independently taggable).

Skill schema:  
`{id, name, definition, purpose, inputs, outputs, dependencies, subskills, domain, tags, version, lineage}`

Claim schema:  
`{id, text, tag, why, sources[], modifiers[]}`

**Opposite approach:** Chat-only mega-narrative. Session death = knowledge death.

---

## Phase 1 — Emit Atoms

### Step p5s1 — Write ClaimAtoms and SkillAtoms to schema

**The Why:**  
Encyclopedias and dashboards die when fields are free-text only. Schema is how the next cycle reloads state instead of reinventing it.

**Granular Execution Plan:**
1. Write ClaimAtoms for every major proposition.
2. Write SkillAtoms for every teachable/executable procedure (Title Case names, sk_ ids).
3. AgentReport: do not collapse findings into the verdict paragraph only.
4. Always emit multi-channel pack:
   a. Markdown report
   b. JSON state
   c. HTML dashboard (HQ + portable)
   d. GitHub path
   e. Drive copy
5. Bump version on edit; keep lineage to cycle id.

**Required Tools/Resources:**
- artifacts/skill-engine/state.json
- src/data/swarm.ts / doctrine.ts
- GitHub push_files
- Drive upload
- HITL authorization

**Common Pitfalls & Fixes:**
1. Mistake: Dumping encyclopedia into chat and calling it shipped.  
   Fix: Chat is index; artifacts are product.
2. Mistake: Versionless overwrites.  
   Fix: Bump version + lineage.
3. Mistake: Missing Drive or GitHub "because chat is enough."  
   Fix: AAO incomplete until multi-channel exists.

**KPI / Success Metric:**  
A third party reconstructs the same tags from HQ Doctrine + GitHub + Drive without the chat.

---

## Phase 2 — Educator Wrapper (Macro-to-Micro)

### Step p6s1 — Apply the mandatory step template

**The Why:**  
Summarizing is how modifiers get lost. The template forces Why, Execution, Tools, Pitfalls, KPI on every step so "common sense" cannot skip measurement.

**Foundational theory:**  
Pedagogy: retrieval + worked examples beat generic advice. Operational volume is not vanity verbosity — it prevents skipped gates. Blending points is the failure mode; H2/H3 nested layout stops blending.

**Granular Execution Plan (every step forever):**
1. Phase header (chronological).
2. Step title (verb + object).
3. The Why (theory + criticality).
4. Foundational theory (mechanics, jargon defined in-line).
5. Nested execution (1 / a / i).
6. Required tools/resources (including mindset).
7. Common pitfalls & fixes (2–3).
8. KPI before next step.
9. Contrast table vs opposite approach where claims appear.

**Required Tools/Resources:**
- This Doctrine (canonical)
- Tag language
- HITL

**Common Pitfalls & Fixes:**
1. Mistake: 40 pages with no KPI — unfalsifiable depth.  
   Fix: If you cannot say what "done" looks like, you wrote literature, not a pipeline.
2. Mistake: Skipping "obvious" steps (hash PDF, name axes).  
   Fix: Obvious steps are where silent errors compound.
3. Mistake: Generic advice without domain terms.  
   Fix: Use claim IDs, grant numbers, modifier IDs, ACH labels.

**KPI / Success Metric:**  
A new investigation can be run by walking Chapter 1→2→3 without inventing a new method.

---

## Phase 3 — Optimization (Artifact Hygiene)

### Step p6opt1 — Verify multi-channel reconstructability

**Granular Execution Plan:**
1. Blind reconstruct test: open only Drive + GitHub + HQ Doctrine; rebuild C01–Cnn tags.
2. Fix any missing atom or broken link.
3. Record reconstructability pass/fail in UPDATE_LOG.

**KPI:** Reconstructability test passes for the current cycle.

---

# Comparative Analysis (Global)

| Approach | Opposite | Why it matters |
|----------|----------|----------------|
| Single dense vector | Multi-vector / claim atom | Pooling kills rare IDs |
| Reconstruction latents | Semantic decision axes | Pretty ≠ useful |
| Prompt vibe ("be based") | Named gates M1–M6 | Gates audit |
| Unvalidated anti-mainstream | Dual-anti-narrative | Capture test |
| Mega-narrative | Tagged atoms + synthesizer | OVERSTATED stays fireable |
| Chat-only | App + GitHub + Drive | Session survival |
| Process as origin proof | Process SOLID, origin CONTESTED | M5 integrity |
| Mortality as mechanism likelihood | Separate outcome vs mechanism axes | Category-error watch |

---

# Enforcement Contract

Every future swarm cycle and educator deep-dive **must**:

1. Place objects in LVS at claim grain on four decision axes.
2. Fire M1–M6 and log which passed.
3. Ship AAO pack (MD + JSON + HTML + GitHub + Drive).
4. Use educator template on every step (Why · Execution · Tools · Pitfalls · KPI).
5. Keep dual-anti-narrative: both 2020-media lines and inverse-dogma can be OVERSTATED.
6. Keep process failures SOLID even when origin remains CONTESTED.

**Canonical locations:**
- Live: Meridian Swarm HQ → `/doctrine`
- Artifact: `artifacts/sscp_ingest/findings/DOCTRINE_LVS_SLMVP_AAO.md` (this file)
- OP: `artifacts/sscp_ingest/findings/OPERATING_PROCEDURE_LVS_SLMVP_AAO.md`
- Project: `AGENTS.project.md`
- Skills: `artifacts/skill-engine/state.json`

**Lineage tags:** `doctrine_v2`, `sk_lvs_slmvp_aao_pipeline`, `sk_educator_macro_micro_guide`
