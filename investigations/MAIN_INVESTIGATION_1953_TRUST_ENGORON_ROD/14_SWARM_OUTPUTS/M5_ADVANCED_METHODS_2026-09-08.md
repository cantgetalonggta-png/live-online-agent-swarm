# 3) FIVE ADVANCED LEARNING / INVESTIGATION METHODS
**HITL=YES · distill as deep as public-record ceiling allows**

---

### M1 — Temporal burst + instrument clustering
**What:** Align every dated instrument (will, trust amend, wire, email, filing) on a single timeline; flag same-day and ±48h clusters.  
**Why:** Caught Feb 4 2019 amend+wire; 48h will/1953 restatement; next-day Reinhart hire.  
**How deep:** Build machine-readable event table (date, actor, instrument type, amount, bates/source); run burst detection (e.g. DBSCAN on timestamps or simple 24–48h windows); require primary PDF for each burst member.  
**Output:** CLUE files + graph edges with `dated_with` relations.

---

### M2 — Beneficiary / control dual-graph (legal form vs economic substance)
**What:** Two parallel graphs — (A) formal roles (trustee, executor, beneficiary) (B) who can move money (wire authority, authorized contact, signatory).  
**Why:** Kahn is both residual beneficiary *and* Butterfly wire instructor *and* Southern Trust contact; Indyke both executor and PLLC payee.  
**How deep:** For each entity, extract from primary: signers, authorized users, beneficiaries, “trading authority” clauses (Butterfly irrevocable + Epstein trading authority language in DB internal email reporting). Score divergence: high formal power + high operational power = control concentration.  
**Output:** MAP dual layers; APR control-concentration score.

---

### M3 — Entity-family + circular-flow forensics
**What:** Group entities by name stem (Southern_*, Butterfly, 1953, HBRK, Financial Trust) and reconstruct multi-hop wires (A→B→A, estate↔bank↔trust).  
**Why:** Southern Country loops and Butterfly $13M path are where residual vs insulation fights live.  
**How deep:** From SARs/exhibits/probate accountings: edge list (from, to, amount, date, bank); compute strongly connected components; flag post-death cycles and missing supporting docs (loan agreements).  
**Output:** GRAPH_EDGES money layer; AAD circular-flow anomalies.

---

### M4 — Role-boundary expansion detection (occupation drift)
**What:** Track when a professional acts outside stated occupation (CPA writes immigration marital endorsement; lawyer advises immigration messaging; accountant logs lingerie/tuition).  
**Why:** Maps enabler function without requiring “knew trafficking” proof.  
**How deep:** Code each act: {tax, corporate, litigation, immigration, lifestyle-pay, trust-ops}; alert when actor’s modal role ≠ act class. Prioritize acts with notarization or bank effect.  
**Output:** PT role-expansion; BC like Kahn immigration letter.

---

### M5 — Competing-hypotheses ledger with document gates (ACH-lite, no theater)
**What:** For each contested money edge (e.g. Butterfly decant), hold **exactly two** working hypotheses; list **minimum primary documents** that would raise/lower each; refuse elevation without gates.  
**Example (BC-NEW-01):**  
- H_substance: decant insulated executor wealth from victims  
- H_form: routine irrevocable-trust restructuring with independent adviser  
**Gates:** full decant instrument, adviser letter, successor trust agreements, probate disclosure, bank statements.  
**Why:** Stops slogan wars; forces document acquisition list (operator PDFs / FOIA / docket).  
**Output:** per-breadcrumb H-pair + gate checklist in `04_NEEDS_FOLLOW_UPS`.

---

## Distill stack order (recommended)
1. M1 timeline table from existing sources  
2. M2 dual graph for Indyke/Kahn/Shuliak/Butterfly/1953  
3. M3 Southern + Butterfly wire SCC  
4. M4 role codes on Kahn/Indyke acts  
5. M5 gates → operator HITL which PDFs to ingest next  
