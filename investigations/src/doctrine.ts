export type Pitfall = { mistake: string; fix: string };
export type Step = {
  id: string;
  title: string;
  why: string;
  theory: string;
  execution: string[][];
  tools: string[];
  pitfalls: Pitfall[];
  kpi: string;
};
export type Phase = { id: string; title: string; intent: string; steps: Step[] };
export type Chapter = {
  id: string;
  title: string;
  thesis: string;
  contrast: { a: string; b: string; note: string }[];
  phases: Phase[];
};

export const DOCTRINE_META = {
  name: "LVS → SLMVP → AAO",
  full: "Latent Vector Space → System-Level Modifier Validation Pipeline → Atomized Artifact Output",
  version: "1.1",
  status: "PERMANENT — swarm default operating procedure",
};

export const CHAPTERS: Chapter[] = [
  {
    id: "ch1",
    title: "Chapter 1 — Latent Vector Space (LVS)",
    thesis:
      "A latent vector space is a high-dimensional numeric field where meaning is geometry. Claims, documents, agents, and hypotheses occupy positions. Distance is disagreement; direction is a modifier. You do not argue in slogans here — you place objects, measure angles, and refuse to pool a rare fact into a single mushy embedding.",
    contrast: [
      {
        a: "Single dense vector (lossy pool)",
        b: "Multi-vector / atom (token- or claim-level)",
        note: "Pooling kills rare identifiers (grant numbers, FCS, March 25). Keep atoms.",
      },
      {
        a: "Reconstruction latents (looks like the input)",
        b: "Semantic latents (preserves action-relevant structure)",
        note: "Pretty reconstruction ≠ useful decision space. Policy and ACH need semantics.",
      },
      {
        a: "Superposed activations (many concepts in one neuron)",
        b: "Disentangled atoms (sparse, separable, reconstructable)",
        note: "SAE/TSAE-style atomization is the theoretical target; claim-atoms are the operational analog.",
      },
    ],
    phases: [
      {
        id: "p1",
        title: "Phase 1 — Preparation (define the space)",
        intent: "Name the axes before you embed anything. Unnamed axes produce narrative mush.",
        steps: [
          {
            id: "p1s1",
            title: "Declare objects that may occupy the space",
            why: "If the unit of analysis is wrong, every later similarity is a lie. COVID origin work fails when the unit is 'the pandemic' instead of 'this claim, this email, this sequence, this grant clause.'",
            theory:
              "In representation learning, an embedding is a map f: object → ℝⁿ. The object grammar (document, chunk, claim, entity, hypothesis) is the ontology. Superposition (many concepts sharing one direction) is the failure mode when the grammar is too coarse.",
            execution: [
              ["Enumerate object types: Document, Chunk, Entity, Claim, Hypothesis, Agent, Modifier, Artifact."],
              ["Assign a stable ID scheme: C01…Cnn claims; H1…Hk hypotheses; sk_* skill atoms; agent ids."],
              ["Forbid pooling a whole 557-page report into one vector. Minimum grain = one claim or one footnote-backed proposition."],
              ["Record provenance on every object: URL or PDF page, timestamp, hash."],
            ],
            tools: [
              "Public-record ceiling (HITL=YES)",
              "SHA-256 of source PDF",
              "Claim schema: {id, text, tag, why, source}",
              "Mindset: geometry over rhetoric",
            ],
            pitfalls: [
              {
                mistake: "Embedding headlines ('lab leak proven') instead of propositions.",
                fix: "Rewrite as a testable sentence with a tag: SOLID / CONTESTED / OVERSTATED / IRREGULARITY.",
              },
              {
                mistake: "One vector per agent report (too coarse).",
                fix: "One vector per finding inside the report. Agent report is a container, not an atom.",
              },
            ],
            kpi: "You can list every object type and at least one example ID for each. No unlabeled blobs remain.",
          },
          {
            id: "p1s2",
            title: "Choose axes that correspond to decisions, not vibes",
            why: "A latent space used for investigation must separate (1) process failure vs origin inference, (2) confidence vs probability, (3) mechanism vs mortality. Mixing those axes is how 7.1M deaths get treated as proof of manufacture.",
            theory:
              "Semantic latent spaces outperform reconstruction spaces on planning because they preserve action-relevant structure. Investigation analog: axes must be decision-relevant — tag, likelihood ratio, source quality — not 'how spicy is this take.'",
            execution: [
              ["Axis A: epistemic tag (SOLID / CONTESTED / OVERSTATED / IRREGULARITY)."],
              ["Axis B: hypothesis support (H1 lab accident / H2 zoonosis / H3 weapon) as signed weights."],
              ["Axis C: source quality (primary .gov / FOIA / peer-review / IC / secondary)."],
              ["Axis D: incentive/conflict (author is a party to the grant, the paper, or the policy)."],
              ["Refuse a single 'truthiness' axis. That is narrative control wearing a number."],
            ],
            tools: ["ACH matrix", "Source-quality weights", "Conflict-of-interest flag"],
            pitfalls: [
              {
                mistake: "Using media consensus as an axis.",
                fix: "Consensus is not evidence. Put the primary document on the axis, not the chyrons.",
              },
              {
                mistake: "Collapsing confidence and probability (CIA 'low confidence' ≠ 'low probability').",
                fix: "Store both. Low confidence + lean-H1 is a different object than high confidence H2.",
              },
            ],
            kpi: "Four named axes exist on paper. A new claim can be plotted on all four in under two minutes.",
          },
        ],
      },
      {
        id: "p2",
        title: "Phase 2 — Execution (place objects)",
        intent: "Ingest, chunk, embed, and link. Do not skip chunking.",
        steps: [
          {
            id: "p2s1",
            title: "Ingest and chunk at claim grain",
            why: "Late-interaction (ColBERT-style) keeps one vector per token because pooling destroys rare identifiers. Operational analog: keep one record per claim, never one record per chapter.",
            theory:
              "Dense single-vector retrieval is lossy for rare entities (R01AI110964, DEFUSE, March 25 Directive). Multi-vector / atomized storage preserves those. Knowledge-atomization research (TSAE on entity activations) exists because superposition hides facts.",
            execution: [
              ["Hash the source file. If hash changes, re-ingest; never silently mutate."],
              ["Extract text by section (pdfplumber), keep page anchors."],
              ["Split to claims: one proposition, one tag, one why, one source list."],
              ["Link Claim—SUPPORTED_BY→Source and Claim—ABOUT→Entity."],
            ],
            tools: ["pdfplumber", "Graph schema Document-HAS_CHUNK-Chunk-MENTIONS-Entity", "SHA-256"],
            pitfalls: [
              {
                mistake: "OCR-skipping image pages and then claiming 'we read all 557 pages word for word.'",
                fix: "Log extraction density per page. Flag sparse pages for second-pass footnote harvest.",
              },
            ],
            kpi: "Every claim has a page or document pointer. Extraction coverage % is known, not assumed 100%.",
          },
          {
            id: "p2s2",
            title: "Link and re-project after new evidence",
            why: "Latent geometry is not static. A new FOIA drop or IC statement must move claim positions, not just append a footnote.",
            theory:
              "World models that freeze latents after first ingest drift. Re-embedding under the same axes is the investigation analog of continual learning — same metric, updated points.",
            execution: [
              ["When a new primary source arrives, re-hash and re-tag only affected claims."],
              ["Recompute ACH weights for H1/H2/H3; do not reset unrelated SOLID process claims."],
              ["Log the delta: which tags flipped, which posteriors moved, which modifiers re-fired."],
            ],
            tools: ["Versioned claims JSON", "ACH table", "CHANGELOG in UPDATE_LOG.md"],
            pitfalls: [
              {
                mistake: "Treating every news article as a geometry update.",
                fix: "Only primary sources or IC products move axes. Commentary stays secondary.",
              },
              {
                mistake: "Silent overwrite of old claim tags.",
                fix: "Keep prior tag in lineage; bump version on the claim atom.",
              },
            ],
            kpi: "Any tag flip has a before/after and a source ID in the log.",
          },
        ],
      },
      {
        id: "p2opt",
        title: "Phase 3 — Optimization (space hygiene)",
        intent: "Cull duplicates, orphans, and blended claims that violate sparsity.",
        steps: [
          {
            id: "p2opt1",
            title: "Deduplicate and split blended claims",
            why: "A claim that mixes EcoHealth late reporting with 'therefore lab leak' fails sparsity and steers readers into M5 violations.",
            theory:
              "Atom Theory: separability requires independent tagging. Blended claims are superposed concepts — the operational failure SAE research tries to undo.",
            execution: [
              ["Scan for 'and therefore' glue between process and origin."],
              ["Split into two claims with independent tags."],
              ["Remove duplicate claims that share the same proposition under different IDs."],
            ],
            tools: ["claims_distilled.json", "TagPill rules", "M5 Process ≠ origin"],
            pitfalls: [
              {
                mistake: "Keeping a spicy blended claim because it 'reads well.'",
                fix: "Readable narratives hide OVERSTATED clauses. Split first, synthesize later.",
              },
            ],
            kpi: "Zero claims that both assert a process fact and an origin conclusion in one sentence.",
          },
        ],
      },
    ],
  },
  {
    id: "ch2",
    title: "Chapter 2 — System-Level Modifier Validation Pipeline (SLMVP)",
    thesis:
      "A modifier is any instruction that steers the latent space: 'avoid mainstream narrative,' 'HITL=YES,' 'public-record ceiling,' 'do not overclaim manufacture.' System-level means the modifier is enforced on the whole swarm, not whispered to one agent. Validation means you test whether the modifier changed geometry honestly — or just flipped the partisan sign.",
    contrast: [
      {
        a: "Prompt-level vibe ('be based')",
        b: "System-level gate (tag, source, HITL, ceiling)",
        note: "Vibes are not reproducible. Gates leave an audit trail.",
      },
      {
        a: "Unvalidated anti-mainstream (new dogma)",
        b: "Validated anti-narrative (both 2020 media AND Telegram overclaim get tagged OVERSTATED)",
        note: "If only one tribe's slogans die, the modifier failed.",
      },
    ],
    phases: [
      {
        id: "p3",
        title: "Phase 1 — Register modifiers",
        intent: "Write every steering rule as a named object with a test.",
        steps: [
          {
            id: "p3s1",
            title: "Atomize modifiers",
            why: "Unnamed modifiers cannot be validated. 'Maximum common sense' is not a test. 'No claim gets SOLID without a primary document' is a test.",
            theory:
              "In latent-space arithmetic, an edit is z_q = z_ref + α(Σ add − Σ remove). Unspecified α and unspecified add/remove vectors produce drift. Named modifiers are the add/remove clauses. Validation is checking the resulting geometry still reconstructs the source (faithfulness) and still separates hypotheses (separability).",
            execution: [
              ["M1 Public-record ceiling: only .gov, FOIA, peer-review, IC summaries, court dockets, user-supplied public PDFs."],
              ["M2 HITL=YES on bulk ingest, external push, irreversible writes (GitHub/Drive)."],
              ["M3 Dual-anti-narrative: reject both 'lab leak is racist conspiracy' and '7.1M deaths prove bioweapon.'"],
              ["M4 Tag discipline: SOLID requires primary docs; CONTESTED is allowed; OVERSTATED is a first-class tag."],
              ["M5 Process ≠ origin: EcoHealth debarment does not move H1 posterior to 1.0."],
              ["M6 Category-error watch: 'methods overlap with party-state information control' ≠ 'US liberals are communists.'"],
            ],
            tools: ["Modifier registry (this playbook)", "SOLID/CONTESTED/OVERSTATED/IRREGULARITY enum", "HITL flag"],
            pitfalls: [
              {
                mistake: "Treating 'avoid mainstream' as 'believe the inverse of CNN 2020.'",
                fix: "Inverse-of-a-lie is not automatically true. Run ACH. Tag OVERSTATED on both sides.",
              },
              {
                mistake: "Letting HITL=YES become theater (no actual gate).",
                fix: "No Drive/GitHub push of new conclusions without a written SOLID/CONTESTED split.",
              },
            ],
            kpi: "Six named modifiers, each with a one-line pass/fail test. Swarm reports cite which modifiers fired.",
          },
        ],
      },
      {
        id: "p4",
        title: "Phase 2 — Validate modifiers against both tribes",
        intent: "A modifier that only wounds one narrative is captured.",
        steps: [
          {
            id: "p4s1",
            title: "Adversarial pass on every major claim",
            why: "Confirmation bias is the default human prior. The pipeline must spend equal effort trying to kill H1 and H2.",
            theory:
              "Analysis of Competing Hypotheses (Heuer) was built to stop intel analysts from marrying one story. Bayesian update is the numeric form: likelihood ratios, not vibes. CIA Jan 2025 'low confidence, no new intel, still both plausible' is a modifier test: did you over-read a lean?",
            execution: [
              ["For each claim, write the strongest case FOR and AGAINST in the same card."],
              ["Apply M3: if your 'anti-mainstream' conclusion has no primary doc, it is not SOLID."],
              ["Apply M5: process crimes stay SOLID even if origin stays CONTESTED."],
              ["Log CIA-style confidence separately from probability."],
            ],
            tools: ["ACH matrix", "Likelihood notes", "Source-quality weights"],
            pitfalls: [
              {
                mistake: "Using mortality as a likelihood for origin (7.1M → manufactured).",
                fix: "Mortality is an outcome axis. Origin is a mechanism axis. Do not multiply them.",
              },
              {
                mistake: "Treating debarment as genetic proof.",
                fix: "Debarment proves grant-term failure. Sequences still have to match. They don't, for published EcoHealth chimeras vs SARS-CoV-2.",
              },
            ],
            kpi: "Every C01–C11 card has FOR, AGAINST, tag, and modifier IDs. No card is tag-only.",
          },
        ],
      },
    ],
  },
  {
    id: "ch3",
    title: "Chapter 3 — Atomized Artifact Output (AAO)",
    thesis:
      "Output is not a vibe essay. Output is a set of atoms: SkillAtoms, ClaimAtoms, Agent reports, ACH posteriors, HTML dashboards, Drive/GitHub hashes. If it cannot be cited, tagged, and versioned, it did not ship.",
    contrast: [
      {
        a: "One mega-narrative",
        b: "Many tagged atoms + a synthesizer",
        note: "Mega-narratives hide OVERSTATED clauses. Atoms make them fireable.",
      },
      {
        a: "Chat-only answer",
        b: "App + GitHub + Drive + per-agent HTML",
        note: "Permanent use requires artifacts that survive the session.",
      },
    ],
    phases: [
      {
        id: "p5",
        title: "Phase 1 — Emit atoms",
        intent: "One atom = one teachable or testable unit.",
        steps: [
          {
            id: "p5s1",
            title: "Write ClaimAtoms and SkillAtoms to schema",
            why: "Encyclopedia and dashboards die when fields are free-text only. Schema is how the next cycle reloads state instead of reinventing it.",
            theory:
              "Atom Theory (representability, sparsity, separability) plus skill-tree schema {id, name, definition, purpose, inputs, outputs, dependencies, tags, version, lineage}. A claim atom that cannot reconstruct the source quote fails representability. A claim that mixes three issues fails sparsity. A claim that cannot be tagged independently fails separability.",
            execution: [
              ["ClaimAtom: {id, text, tag, why, sources[], modifiers[]}"],
              ["SkillAtom: {id: sk_*, name Title Case, definition, purpose, inputs, outputs, domain, version, lineage}"],
              ["AgentReport: already in HQ — do not collapse findings into the verdict paragraph only."],
              ["Always emit: markdown report, JSON, HTML dashboard, Drive copy, GitHub path."],
            ],
            tools: ["skill-engine/state.json", "src/data/swarm.ts", "src/data/doctrine.ts", "GitHub push_files", "Drive upload"],
            pitfalls: [
              {
                mistake: "Dumping the encyclopedia into chat and calling it shipped.",
                fix: "Chat is the index. Artifacts are the product. HQ routes + GitHub + Drive must exist.",
              },
              {
                mistake: "Versionless overwrites.",
                fix: "Bump version on edit; keep lineage to the cycle (SSCP_cycle2, doctrine_v1).",
              },
            ],
            kpi: "A third party can open HQ → Doctrine, HQ → Agents, GitHub investigations/, Drive folder, and reconstruct the same tags without the chat.",
          },
        ],
      },
      {
        id: "p6",
        title: "Phase 2 — Educator wrapper (macro-to-micro)",
        intent: "Every future deep-dive uses this wrapper so steps cannot collapse into summary.",
        steps: [
          {
            id: "p6s1",
            title: "Apply the mandatory step template",
            why: "Summarizing is how modifiers get lost. The template forces Why, Execution, Tools, Pitfalls, KPI on every step so 'common sense' cannot skip the measurement.",
            theory:
              "Pedagogy: retrieval + worked examples beat generic advice. Operational volume is not verbosity for its own sake — it is preventing skipped gates. The failure mode of high-volume output is blending points; the H2/H3/nested-list layout exists to stop blending.",
            execution: [
              ["Phase header (chronological)."],
              ["Step title (verb + object)."],
              ["The Why (theory + criticality)."],
              ["Granular execution (nested 1 / a / i)."],
              ["Required tools/resources (including mindset)."],
              ["Common pitfalls & fixes (2–3)."],
              ["KPI before next step."],
              ["Where claims appear, add a contrast table vs the opposite approach."],
            ],
            tools: ["This Doctrine page (canonical)", "TagPill language", "HITL"],
            pitfalls: [
              {
                mistake: "Writing 40 pages with no KPI — unfalsifiable depth.",
                fix: "If you cannot say what 'done' looks like, you wrote literature, not a pipeline.",
              },
              {
                mistake: "Skipping 'obvious' steps (hash the PDF, name the axes).",
                fix: "Obvious steps are where silent errors compound. Keep them.",
              },
            ],
            kpi: "A new investigation can be run by walking Chapter 1→2→3 without inventing a new method.",
          },
        ],
      },
    ],
  },
];

export const MODIFIERS = [
  { id: "M1", name: "Public-record ceiling", test: "No private data, no creds, no unauthorized access." },
  { id: "M2", name: "HITL=YES", test: "Bulk ingest / GitHub / Drive require operator authorization." },
  { id: "M3", name: "Dual-anti-narrative", test: "Both 2020-media slogans and Telegram overclaims can be OVERSTATED." },
  { id: "M4", name: "Tag discipline", test: "SOLID only with primary documents." },
  { id: "M5", name: "Process ≠ origin", test: "Debarment/FOIA/6-ft do not close H1." },
  { id: "M6", name: "Category-error watch", test: "Methods overlap ≠ identity of ideologies." },
];
