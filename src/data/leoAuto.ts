export type LeoTag = "SOLID" | "CONTESTED" | "OVERSTATED" | "IRREGULARITY";
export type LeoRow = { tag: LeoTag; verdict: string; omission: number; warrant: string; why?: string };

/** Bounded honest claim wording */
export const LEO_AUTO_BOUNDED: Record<string, LeoRow> = {
  C01: { tag: "CONTESTED", verdict: "CONTESTED", omission: 0.6, warrant: "WATCHLIST_PRIMARY_HUNT", why: "Missing serology/host/notebook primaries" },
  C02: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "Process FOIA chain present" },
  C03: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "HHS debarment operative acts" },
  C04: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "Morens/Fauci TI process primary" },
  C05: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "TI anchors for six-foot empiric basis" },
  C06: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "Bounded: mixed evidence not absolute" },
  C07: { tag: "CONTESTED", verdict: "CONTESTED", omission: 0.333, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Missing universal net counterfactual" },
  C08: { tag: "CONTESTED", verdict: "CONTESTED", omission: 0.333, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Missing criminal_judgment" },
  C09: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "IHR/WHO public record bounded" },
  C10: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "GAO/OIG ranges primary" },
  C11: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "Production delay process primary" },
};

/** Absolute slogan narratives vs public secondary (pack v2.1 / cycle 19–20) */
export const LEO_AUTO_SLOGAN: Record<string, LeoRow> = {
  C01: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.6, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('proven/debunked', 'unsubmitted'), ('proven', 'unsubmitted'), ('settled science', 'unsubmitted')]" },
  C02: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.5, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('no nih influence', 'investigation'), ('purely objective', 'investigation')]" },
  C03: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.0, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('fully complied', 'incident'), ('all applicable requirements', 'incident'), ('in full compliance', 'incident')]" },
  C04: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.0, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('fully transparent', 'investigation'), ('complete transparency', 'investigation')]" },
  C05: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.0, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('rigorously science-based', 'sort of just appeared')]" },
  C06: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.0, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('absolutely ineffective', 'mixed'), (\"masks don't work\", 'mixed'), ('ineffective in all contexts', 'mixed')]" },
  C07: { tag: "CONTESTED", verdict: "CONTESTED", omission: 0.333, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Partial primary: missing ['universal_net']" },
  C08: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.333, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('adjudicated criminal', 'missing')]" },
  C09: { tag: "IRREGULARITY", verdict: "IRREGULARITY", omission: 0.0, warrant: "ESCALATE_TO_TARGETED_FOIA", why: "Overclaim clash: [('proven', 'hypotheses remain'), ('there is no lab leak', 'hypotheses remain'), ('conspiracy theory', 'hypotheses remain')]" },
  C10: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "All documented parameters verified cleanly within public record bounds." },
  C11: { tag: "SOLID", verdict: "SOLID", omission: 0.0, warrant: "NONE", why: "All documented parameters verified cleanly within public record bounds." },
};

export const LEO_AUTO = LEO_AUTO_BOUNDED;

/** Cycle 21: OpenAlex live + Unpaywall OA (M38) */
export const OPEN_ACCESS_LIVE = {
  updated: "2026-09-22T07:51:22.660972+00:00",
  C01: { openalex: [{"id": "W3012565918", "title": "Zoonotic origins of human coronaviruses", "year": 2020, "cited_by": 983, "doi": "https://doi.org/10.7150/ijbs.45472", "oa_url": "https://doi.org/10.7150/ijbs.45472", "is_oa": true}, {"id": "W2931144334", "title": "Infectious Disease Threats in the Twenty-First Century: Strengthening the Global Response", "year": 2019, "cited_by": 820, "doi": "https://doi.org/10.3389/fimmu.2019.00549", "oa_url": "https://www.frontiersin.org/articles/10.3389/fimmu.2019.00549/pdf", "is_oa": true}, {"id": "W3191809422", "title": "The origins of SARS-CoV-2: A critical review", "year": 2021, "cited_by": 518, "doi": "https://doi.org/10.1016/j.cell.2021.08.017", "oa_url": "http://www.cell.com/article/S0092867421009910/pdf", "is_oa": true}, {"id": "W4200429845", "title": "The emergence, genomic diversity and global spread of SARS-CoV-2", "year": 2021, "cited_by": 441, "doi": "https://doi.org/10.1038/s41586-021-04188-6", "oa_url": "https://www.nature.com/articles/s41586-021-04188-6.pdf", "is_oa": true}, {"id": "W2111322194", "title": "Wet markets\u2014a continuing source of severe acute respiratory syndrome and influenza?", "year": 2004, "cited_by": 441, "doi": "https://doi.org/10.1016/s0140-6736(03)15329-9", "oa_url": "http://www.thelancet.com/article/S0140673603153299/pdf", "is_oa": true}], unpaywall: null },
  C02: { openalex: [{"id": "W3011127849", "title": "The proximal origin of SARS-CoV-2", "year": 2020, "cited_by": 5515, "doi": "https://doi.org/10.1038/s41591-020-0820-9", "oa_url": "https://www.nature.com/articles/s41591-020-0820-9.pdf", "is_oa": true}, {"id": "W3092136311", "title": "Characteristics of SARS-CoV-2 and COVID-19", "year": 2020, "cited_by": 5506, "doi": "https://doi.org/10.1038/s41579-020-00459-7", "oa_url": "https://www.nature.com/articles/s41579-020-00459-7.pdf", "is_oa": true}, {"id": "W3018517500", "title": "The trinity of COVID-19: immunity, inflammation and intervention", "year": 2020, "cited_by": 4653, "doi": "https://doi.org/10.1038/s41577-020-0311-8", "oa_url": "https://www.nature.com/articles/s41577-020-0311-8.pdf", "is_oa": true}, {"id": "W3203433659", "title": "Mechanisms of SARS-CoV-2 entry into cells", "year": 2021, "cited_by": 3267, "doi": "https://doi.org/10.1038/s41580-021-00418-x", "oa_url": "https://www.nature.com/articles/s41580-021-00418-x.pdf", "is_oa": true}, {"id": "W3008295344", "title": "High expression of ACE2 receptor of 2019-nCoV on the epithelial cells of oral mucosa", "year": 2020, "cited_by": 2953, "doi": "https://doi.org/10.1038/s41368-020-0074-x", "oa_url": "https://www.nature.com/articles/s41368-020-0074-x.pdf", "is_oa": true}], unpaywall: {"status": "OK", "doi": "10.1038/s41591-020-0820-9", "title": "The proximal origin of SARS-CoV-2", "is_oa": true, "oa_status": "bronze", "best_oa_url": "https://www.nature.com/articles/s41591-020-0820-9.pdf", "host_type": "publisher", "version": "publishedVersion", "oa_source": "unpaywall", "journal": "Nature Medicine", "year": 2020} },
} as const;

export const FOIA_WARRANTS = [
  {
    "claim_id": "C01",
    "tag": "IRREGULARITY",
    "warrant": "C01-FOIA-LATEST.md",
    "date_start": "2019-09-01",
    "date_end": "2025-06-30",
    "vaughn": true
  },
  {
    "claim_id": "C02",
    "tag": "IRREGULARITY",
    "warrant": "C02-FOIA-LATEST.md",
    "date_start": "2020-01-31",
    "date_end": "2020-04-30",
    "vaughn": true
  },
  {
    "claim_id": "C03",
    "tag": "IRREGULARITY",
    "warrant": "C03-FOIA-LATEST.md",
    "date_start": "2014-06-01",
    "date_end": "2025-01-31",
    "vaughn": true
  },
  {
    "claim_id": "C04",
    "tag": "IRREGULARITY",
    "warrant": "C04-FOIA-LATEST.md",
    "date_start": "2020-01-01",
    "date_end": "2024-12-31",
    "vaughn": true
  },
  {
    "claim_id": "C05",
    "tag": "IRREGULARITY",
    "warrant": "C05-FOIA-LATEST.md",
    "date_start": "2020-02-01",
    "date_end": "2020-06-30",
    "vaughn": true
  },
  {
    "claim_id": "C06",
    "tag": "IRREGULARITY",
    "warrant": "C06-FOIA-LATEST.md",
    "date_start": "2020-02-01",
    "date_end": "2023-12-31",
    "vaughn": true
  },
  {
    "claim_id": "C07",
    "tag": "CONTESTED",
    "warrant": "C07-FOIA-LATEST.md",
    "date_start": "2020-03-01",
    "date_end": "2024-12-31",
    "vaughn": true
  },
  {
    "claim_id": "C08",
    "tag": "IRREGULARITY",
    "warrant": "C08-FOIA-LATEST.md",
    "date_start": "2020-03-01",
    "date_end": "2021-12-31",
    "vaughn": true
  },
  {
    "claim_id": "C09",
    "tag": "IRREGULARITY",
    "warrant": "C09-FOIA-LATEST.md",
    "date_start": "2019-12-01",
    "date_end": "2025-06-30",
    "vaughn": true
  }
] as const;

export const VAUGHN_TRACKER_SUMMARY = {"claims_in_tracker": 9, "waves_per_claim": 3, "filed_count": 0, "template_ready": 9, "productions_received": 0, "vaughn_indexes_received": 0} as const;

export const CYCLE21_META = {
  cycle: 21,
  m38: true,
  features: ["unpaywall_c02", "vaughn_wave_tracker", "openalex_refined", "primary_route_wire"],
  updated: "2026-09-22T07:51:22.660972+00:00",
} as const;

/** Phase 4 open-access HQ run (slogan stress) — superseded by LEO_AUTO_SLOGAN for UI */
export const LEO_PHASE4_SLOGAN = LEO_AUTO_SLOGAN;
