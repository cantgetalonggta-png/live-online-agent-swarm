# Phase 4 / Node 4: Open-Access Telemetry Orchestration
Updated: 2026-09-22T06:49:15.406246+00:00

## Topology (lawful mesh)

```
[.gov FOIA seeds] ──┐
[OpenAlex/Crossref] ─┼─► [Hash/stage cache] ─► [LEO + Forensics] ─► [C01–C11 auto-verdict]
[Unpaywall-class OA]─┘                              │
                                          [Decoupled telemetry]
```

## IN scope
- site:*.gov / oversight.house.gov / gao.gov / who.int public PDFs
- FOIA reading-room & Oversight-published releases
- OpenAlex / Crossref / Unpaywall open APIs (open access metadata + OA PDFs)
- User-supplied public documents
- LEO + document forensics on obtained files

## OUT of scope (still refused)
- intitle:index of backup|db|conf|env secret hunting against third parties
- Gobuster/Dirbuster directory fuzzing of non-owned systems
- Credentialed intranet pierce
- Production Tor onion scrape pipelines for C01-C11
- Runtime client mutation / toString camouflage

## Lawful dork templates (public records only)
- `site:oversight.house.gov filetype:pdf debarment`
- `site:oversight.house.gov filetype:pdf "Proximal Origin"`
- `site:gao.gov filetype:pdf "improper payments" COVID OR pandemic`
- `site:who.int SAGO origins SARS-CoV-2`
- `site:gov filetype:pdf "R01AI110964"`

## Auto-verdict (slogan stress test)

| ID | Tag | Omit | Warrant |
|----|-----|------|---------|
| C01 | **OVERSTATED** | 0.6 | ESCALATE_TO_TARGETED_FOIA |
| C02 | **IRREGULARITY** | 0.25 | ESCALATE_TO_TARGETED_FOIA |
| C03 | **IRREGULARITY** | 0.0 | ESCALATE_TO_TARGETED_FOIA |
| C04 | **SOLID** | 0.0 | NONE |
| C05 | **SOLID** | 0.0 | NONE |
| C06 | **SOLID** | 0.0 | NONE |
| C07 | **CONTESTED** | 0.333 | ESCALATE_TO_TARGETED_FOIA |
| C08 | **CONTESTED** | 0.333 | ESCALATE_TO_TARGETED_FOIA |
| C09 | **IRREGULARITY** | 0.333 | ESCALATE_TO_TARGETED_FOIA |
| C10 | **SOLID** | 0.0 | NONE |
| C11 | **SOLID** | 0.0 | NONE |

Tag counts: `{'OVERSTATED': 1, 'IRREGULARITY': 3, 'SOLID': 5, 'CONTESTED': 2}`

Telemetry: `{"elapsed_s": 1.21, "event_counts": {"claim_start": 11, "foia_seed": 11, "openalex": 2, "claim_done": 11}, "n_events": 35}`

## Note
OpenAlex called live for C01/C02 scholarly metadata. No Tor production harvest. No directory fuzzing.
