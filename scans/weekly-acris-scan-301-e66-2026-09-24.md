# Weekly LAWFUL public-record scan
**Property:** 301 East 66th Street, Manhattan, NY 10065  
**Also known as:** 1260 Second Avenue  
**Condo billing BBL (public):** 1-01441-7501  
**Scan date:** 2026-09-24  
**Legal basis:** NYC official open-data extracts + JustFix Who Owns What public pages  
**Fees paid:** none (no HITL fee pull authorized)  
**Personal-data policy:** only names/entities already published on official ACRIS party rows or JustFix HPD-derived public pages; no bulk GDPR harvest.

## Source freshness (SOLID)
| Source | Dataset ID | Last updated (portal) | Used |
|---|---|---|---|
| ACRIS Real Property Legals | 8h5j-fqxa | 2026-09-08 | yes |
| ACRIS Real Property Master | bnx9-e6tj | 2026-09-08 | yes |
| ACRIS Real Property Parties | 636b-3b5g | 2026-09-15 | yes |
| JustFix Who Owns What | whoownswhat.justfix.org | live public page | yes (summary only) |
| Live ACRIS web UI (a836-acris.nyc.gov) | n/a | near-real-time | **not used** (rate/bandwidth limits; no automated scrape) |

**Coverage caveat (SOLID):** Open Data ACRIS extracts are monthly. Intra-month recordings after the extract good-through date will not appear until the next publish. Absence of a 2025/2026 row is **not** proof that nothing was recorded after the extract.

## Pipeline units requested
5P, 11P, 14G, 10N, 10B, 10F, 11J

### Unit-level ACRIS Legals hits (exact unit field)
| Unit | Hits in extract | Latest document_id | Condo tax lot in extract | Tag |
|---|---|---|---|---|
| 5P | 0 | — | not in extract under that unit string | MAYBE |
| 11P | 0 | — | not in extract | MAYBE |
| 14G | 0 | — | not in extract | MAYBE |
| 10N | 4 | 2020111100345001 / 002 / 003 / 005 | lot 1125 | SOLID (2020 cluster only) |
| 10B | 0 | — | not in extract | MAYBE |
| 10F | 0 | — | not in extract | MAYBE |
| 11J | 0 | — | not in extract | MAYBE |

No new 2025 or 2026 document_ids for this street number/name in the current Open Data extract.

### 10N party strings
- 301/66 OWNERS CORP.
- NEW YORK COMMUNITY BANK
- 301 EAST 66TH STREET ASSOCIATES LIMITED PARTNERSHI

## Building-level recent recordings (not pipeline units)
- 2024080800247001 DEED 9G $950000 — STEINBERG, EYDE I / EAST 66 9G LLC (SOLID)
- 2024080800247002 PAT 9G — EAST 66 9G LLC / BOARD OF MANAGERS (SOLID)
- 2024012600702001 ASST 6K — JPMorgan/FDIC/First Republic assignment cluster (SOLID)

## Compliance
Official Open Data only. No fees. Dual-persist GitHub + Drive.
