# Master Skills Encyclopedia

## Agent Swarm Document Distill

- **id:** `sk_agent_swarm_document_distill`
- **version:** 1
- **domain:** infrastructure
- **definition:** End-to-end: download long PDF → section extract → claim tag → Drive + GitHub push → live HTML dashboard under HITL public-record ceiling.
- **purpose:** Operational multi-agent pipeline for 500+ page oversight reports.
- **inputs:** pdf_url, hitl_flag, github_repo, drive_folder
- **outputs:** distilled_md, claims_json, dashboard_html, github_commit_sha
- **dependencies:** sk_public_record_claim_tagging, sk_document_ingestion
- **subskills:** pdfplumber_section, github_push_files, drive_upload
- **tags:** swarm, hitl, dashboard

## Atomized Artifact Output

- **id:** `sk_atomized_artifact_output`
- **version:** 1
- **domain:** infrastructure
- **definition:** Emit versioned ClaimAtoms, SkillAtoms, agent reports, ACH posteriors, HTML dashboards, and GitHub/Drive hashes. Chat is index; artifacts are product.
- **purpose:** Make investigation results citable, reloadable, and session-surviving.
- **inputs:** validated_claims, skill_atoms, agent_reports
- **outputs:** markdown_report, json_state, html_dashboard, github_commit, drive_file
- **dependencies:** sk_system_level_modifier_validation, sk_agent_swarm_document_distill
- **subskills:** claim_atom_schema, skill_atom_schema, multi_channel_backup
- **tags:** aao, atoms, dashboard, doctrine

## Educator Macro Micro Guide

- **id:** `sk_educator_macro_micro_guide`
- **version:** 1
- **domain:** pedagogy
- **definition:** Mandatory pedagogical wrapper: for every step emit Phase Header, Step Title, Why, Granular Execution Plan, Tools/Resources, Common Pitfalls & Fixes (2–3), and KPI before next step. High operational volume without blending points.
- **purpose:** Prevent summarizing away gates; force falsifiable completion criteria on deep-dives.
- **inputs:** topic, goal_or_process, phase_plan
- **outputs:** structured_guide, kpi_checklist
- **dependencies:** sk_atomized_artifact_output
- **subskills:** phase_grouping, pitfall_enumeration, kpi_definition
- **tags:** educator, macro_micro, template, doctrine

## Educator Macro Micro Template

- **id:** `sk_educator_macro_micro_template`
- **version:** 1
- **domain:** education
- **definition:** Mandatory step template: Phase, Step Title, Why, Theory, Nested Execution, Tools, Pitfalls+Fixes, KPI, and contrast table vs opposite approach.
- **purpose:** Block summarization skips and unfalsifiable depth; force measurable completion before next step.
- **inputs:** topic, goal, evidence_corpus
- **outputs:** phase_structured_guide, kpi_checklist
- **dependencies:** sk_atomized_artifact_output
- **subskills:** phase_grouping, kpi_definition, pitfall_enumeration
- **tags:** pedagogy, macro_micro, doctrine

## Grant Oversight Failure Audit

- **id:** `sk_grant_oversight_failure_audit`
- **version:** 1
- **domain:** governance
- **definition:** Audit high-risk research grants (e.g. EcoHealth/WIV) for late progress reports, unreported experiments, sample location misrepresentation, and FOIA evasion culture.
- **purpose:** Document process failures independently of whether the research caused a pandemic.
- **inputs:** nih_grant_files, year5_progress_report, hhs_debarment, morens_emails
- **outputs:** violation_timeline, solid_documented_list
- **dependencies:** sk_public_record_claim_tagging
- **subskills:** foia_evasion_detection, durc_go_f_policy
- **tags:** ecohealth, nih, foia, debarment

## Lab Leak Epistemology

- **id:** `sk_lab_leak_epistemology`
- **version:** 1
- **domain:** research_synthesis
- **definition:** Evaluate origin hypotheses (lab accident vs zoonosis) under public-record ceiling: weight IC low-confidence assessments, market geospatial evidence, genetic features (FCS, RBD), and absence of smoking-gun samples.
- **purpose:** Avoid both premature conspiracy and premature dismissal; keep both hypotheses open until primary evidence closes them.
- **inputs:** odni_summaries, cia_2025_assessment, sago_2025, worobey_pekar_papers, wiv_grant_records
- **outputs:** posterior_odds_table, solid_maybe_contested_flags
- **dependencies:** sk_public_record_claim_tagging, sk_bayesian_ach
- **subskills:** fcs_natural_analogs, market_clustering, go_f_definition_dispute
- **tags:** covid_origins, bayesian, intelligence

## Latent Vector Space Ingest

- **id:** `sk_latent_vector_space_ingest`
- **version:** 1
- **domain:** research_synthesis
- **definition:** Map investigation objects (Document, Chunk, Entity, Claim, Hypothesis, Agent, Modifier, Artifact) into a claim-grain latent space with decision axes: epistemic tag, hypothesis support, source quality, conflict-of-interest. Forbid single-vector pooling of long reports.
- **purpose:** Preserve rare identifiers and separate process failure from origin inference using geometry over rhetoric.
- **inputs:** primary_documents, claim_schema, source_hashes
- **outputs:** object_registry, axis_plotted_claims, provenance_graph
- **dependencies:** sk_public_record_claim_tagging
- **subskills:** claim_grain_chunking, multi_vector_preservation, axis_declaration
- **tags:** lvs, embeddings, ontology, doctrine

## Lvs Slmvp Aao Pipeline

- **id:** `sk_lvs_slmvp_aao_pipeline`
- **version:** 1
- **domain:** infrastructure
- **definition:** End-to-end permanent operating pipeline: Latent Vector Space placement → System-Level Modifier Validation → Atomized Artifact Output under dual-anti-narrative and HITL.
- **purpose:** Single default procedure for every swarm investigation and educator deep-dive.
- **inputs:** user_goal, primary_sources, hitl_flag
- **outputs:** doctrine_compliant_artifact_pack
- **dependencies:** sk_latent_vector_space_ingest, sk_system_level_modifier_validation, sk_atomized_artifact_output, sk_educator_macro_micro_template
- **subskills:** pipeline_orchestrate, modifier_gate, artifact_ship
- **tags:** doctrine, permanent, pipeline, swarm

## Policy By Fiat Detection

- **id:** `sk_policy_by_fiat_detection`
- **version:** 1
- **domain:** policy_equity
- **definition:** Identify public-health rules (6-ft distancing, mask mandates, lockdowns) whose quantitative basis was weak or admitted to be ad-hoc ('sort of just appeared').
- **purpose:** Flag when authority claims science but testimony/FOIA show improvisation.
- **inputs:** closed_door_testimony, cdc_guidance_archive, rct_evidence
- **outputs:** arbitrary_rule_list, transparency_failure_score
- **dependencies:** —
- **subskills:** testimony_phrase_match, guidance_flipflop_timeline
- **tags:** fauci, distancing, masks, lockdowns

## Public Record Claim Tagging

- **id:** `sk_public_record_claim_tagging`
- **version:** 1
- **domain:** research_synthesis
- **definition:** Tag every factual claim from a long primary document as SOLID (primary-doc backed), CONTESTED (plausible but split evidence), or OVERSTATED using IC/SAGO/peer-review cross-checks.
- **purpose:** Separate documented institutional failures from advocacy conclusions in partisan or contested reports.
- **inputs:** primary_document_sections, footnote_cites, external_ic_assessments, peer_reviewed_literature
- **outputs:** tagged_claim_list, solid_vs_contested_summary
- **dependencies:** sk_document_ingestion, sk_bayesian_ach
- **subskills:** footnote_harvest, genetic_distance_check, intelligence_assessment_mapping
- **tags:** covid, lab_leak, oversight, hitl, public_record

## System Level Modifier Validation

- **id:** `sk_system_level_modifier_validation`
- **version:** 1
- **domain:** governance
- **definition:** Register named modifiers M1–M6 (public-record ceiling, HITL, dual-anti-narrative, tag discipline, process≠origin, category-error watch) and validate each with a pass/fail test against both narrative tribes.
- **purpose:** Prevent prompt vibes and inverse-dogma from replacing reproducible gates.
- **inputs:** modifier_registry, claim_cards, ach_matrix
- **outputs:** modifier_fire_log, validated_claim_set
- **dependencies:** sk_latent_vector_space_ingest, sk_public_record_claim_tagging
- **subskills:** dual_anti_narrative, confidence_vs_probability, adversarial_for_against
- **tags:** slmvp, hitl, modifiers, doctrine
