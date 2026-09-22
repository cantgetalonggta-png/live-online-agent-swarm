# Phase 4 Final Compliance Lock (M38)
Updated: 2026-09-22T07:01:44.395507+00:00

## ForceAllowKernel
**DISCARDED.** Local boolean monkey-patches are not authorization.

## Topology
Public API / FOIA / OpenAlex / Unpaywall → staging cache → telemetry → LEO

## Option 1 — FOIA warrant templates
When `actionable_warrant == ESCALATE_TO_TARGETED_FOIA`, write:
`sscp_ingest/findings/foia_warrants/{CLAIM}-FOIA-{DATE}.md`

Warrants this run: **8**
[
  {
    "warrant_id": "C01-FOIA-20260922",
    "claim_id": "C01",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C02-FOIA-20260922",
    "claim_id": "C02",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C03-FOIA-20260922",
    "claim_id": "C03",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C04-FOIA-20260922",
    "claim_id": "C04",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C05-FOIA-20260922",
    "claim_id": "C05",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C07-FOIA-20260922",
    "claim_id": "C07",
    "tag": "CONTESTED"
  },
  {
    "warrant_id": "C08-FOIA-20260922",
    "claim_id": "C08",
    "tag": "IRREGULARITY"
  },
  {
    "warrant_id": "C09-FOIA-20260922",
    "claim_id": "C09",
    "tag": "IRREGULARITY"
  }
]

## Option 2 — Institutional Linguistic Pack v2
- absolute_overclaims: 30
- risk_indicators: 40
- defensive_phrases: 10

## Auto-verdict tag counts
{'IRREGULARITY': 7, 'SOLID': 3, 'CONTESTED': 1}

## M38 lock (static)
{
  "dump_dorks": false,
  "directory_fuzzing": false,
  "private_api_bypass": false,
  "onion_scrapers": false,
  "force_allow_kernel": false
}
