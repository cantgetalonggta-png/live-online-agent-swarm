# Weekly lawful public-record scan — 301 East 66th Street, Manhattan

- Scan date (operator clock): 2026-09-09
- Scope: public ACRIS Open Data + NYC official portals + JustFix public pages only
- Fees: none paid. No ACRIS image-fee pulls. HITL required before any paid image download.
- Personal-data rule: only party strings already published in ACRIS Open Data / JustFix building pages. No GDPR-style bulk personal harvest.
- Access: Socrata public API + public HTML. No login, no circumvention.

## Building identifiers (SOLID)

| Field | Value | Tag | Source |
|---|---|---|---|
| Address | 301 East 66th Street, Manhattan, NY 10065 | SOLID | NYC DOF / JustFix |
| Alias | 1260–1274 Second Avenue | SOLID | Property Address Directory / commercial listings citing PAD |
| Borough-Block-Lot (condo billing) | 1-01441-7501 | SOLID | JustFix Who Owns What; PropertyShark citing DOF |
| Year built / units | 1956 / ~199–200 residential | SOLID | JustFix / PLUTO-class public summaries |
| Condo conversion | ~1990 | SOLID | public building histories citing conversion |

Official portals used:
- ACRIS Real Property Legals: `https://data.cityofnewyork.us/resource/8h5j-fqxa.json` (dataset 8h5j-fqxa)
- ACRIS Real Property Master: `https://data.cityofnewyork.us/resource/bnx9-e6tj.json` (dataset bnx9-e6tj)
- ACRIS Real Property Parties: `https://data.cityofnewyork.us/resource/636b-3b5g.json` (dataset 636b-3b5g)
- JustFix Who Owns What: `https://whoownswhat.justfix.org/en/address/MANHATTAN/301/EAST%2066%20STREET/summary`
- Official ACRIS app (not scraped this week): `https://a836-acris.nyc.gov` — live images may require per-document fee; **not pulled**.

Open Data “good through / last updated”: datasets last updated **2026-09-08**. Monthly automation. Documents recorded after the extract cutoff will not appear until the next monthly load. Treat “no new unit-level deed this week” as **MAYBE-incomplete** until next extract.

## Pipeline units requested

5P, 11P, 14G, 10N, 10B, 10F, 11J

### Unit-level visibility in ACRIS Legals (street_number = 301, block 1441)

| Unit | Condo lot (when visible) | Unit-specific docs in Open Data | Latest document_id(s) | Tag |
|---|---|---|---|---|
| 10N | 1125 | Yes | **2025120200479001, 2025120200479002, 2025120200479004, 2025120200479005** (recorded 2025-12-04; good_through 2025-12-31). Prior cluster 2020111100345001–0005 (2020). | SOLID |
| 10F | 1118 (historic) | Historic only | 2014011500756001, 2011032400376001–0003 | SOLID historic / no 2024–2026 unit-only hit |
| 11J | 1134 (historic) | Historic only | 2014011500756001, 2011032400376001–0003 | SOLID historic / no 2024–2026 unit-only hit at 301 |
| 5P | not found at 301 | No exact `unit=5P` on street 301 block 1441 | — | MAYBE absent from Open Data unit index (or never separately deeded under that string) |
| 11P | not found | No `unit=11P` | — | MAYBE absent |
| 14G | not found | No `unit=14G` | — | MAYBE absent |
| 10B | not found at 301 | One off-address hit: unit 10B at **333 East 66th Street**, lot 17 (different building, same block) | 2013081200072001 | SOLID as *different building*; do not merge |

**Caveat (SOLID):** ACRIS `unit` strings are inconsistent (`EAST 66 STREET` vs `EAST 66TH STREET`). Exact-match queries can miss variants. A like-search for `5P` only returned **15P** (lot 1180), not 5P.

### December 2025 instrument cluster (most recent material on 10N)

These four document_ids each attach to **137 units** at 301 East 66th Street. They are **building-package financing / assignment instruments**, not standalone unit deeds.

| document_id | doc_type | document_date | recorded | amount | CRFN | Tag |
|---|---|---|---|---|---|---|
| 2025120200479001 | TL&R | 2025-11-18 | 2025-12-04 | 0 | 2025000328421 | SOLID |
| 2025120200479002 | TL&R | 2025-11-18 | 2025-12-04 | 0 | 2025000328422 | SOLID |
| 2025120200479004 | ASST | 2025-11-18 | 2025-12-04 | 0 | 2025000328424 | SOLID |
| 2025120200479005 | AGMT | 2025-11-25 | 2025-12-04 | 6,614,649,329 (field as published; treat magnitude as MAYBE until image review) | 2025000328425 | SOLID id / MAYBE amount semantics |

**Party strings (ACRIS Parties, public):**

- `301/66 OWNERS CORP.` — 301 EAST 66TH STREET, UNIT 1, NEW YORK
- `301 66TH STREET ASSOCIATES LIMITED PARTNERSHIP` — C/O OSSA PROPERTIES, INC., NEW YORK
- `FLAGSTAR BANK, N.A.` — 102 DUFFY AVENUE, HICKSVILLE
- `NEW YORK COMMUNITY BANK` — 102 DUFFY AVENUE, HICKSVILLE

Party-type codes 1/2 as published; role labels not expanded here (see ACRIS Document Control Codes 7isb-wh4c).

**Pipeline coverage inside that 137-unit package:**
- Present: **10N only**
- Absent from the 137-unit legal schedule: **5P, 11P, 14G, 10B, 10F, 11J**

Interpretation (MAYBE): those six units may sit outside the 301/66 Owners Corp. financed pool, may use different unit strings, or may not be separately scheduled. Do not treat absence as proof of different beneficial owner without a deed image (fee / HITL).

### 2020 cluster on 10N (context, not new)

document_ids 2020111100345001 (MTGE, amt 4,990,766.31), 0002 (AGMT 8,000,000), 0003 (AL&R 8,000,000), 0005 (SAT). Parties: 301/66 OWNERS CORP., NEW YORK COMMUNITY BANK, 301 EAST 66TH STREET ASSOCIATES LIMITED PARTNERSHI (truncated string as published).

## JustFix public page (building, not unit)

Who Owns What summary for MANHATTAN / 301 / EAST 66 STREET (public):
- Portfolio associated with 2 buildings; primary BBL 1-01441-7501; ~199 units; year built 1956.
- Published corporate / officer strings on that page (building-level HPD registration style, not ACRIS deeds): 301 E 66 ST CONDO ASSOCIATION C/O OSSA; Ossa Properties Inc; names already published on that page include MARK EPSTEIN (shareholder), ANTHONY BARRETT, ANDREW LOSSO.
- Open violations / eviction counts on the page are building-level, not unit-level for the pipeline set.

JustFix does **not** expose per-unit ACRIS document_ids. Unit scan therefore rests on ACRIS Open Data.

## What is “new” this week

- Open Data extract date 2026-09-08. No document_id newer than the Dec 2025 cluster appeared for the seven pipeline units in the 301 / block 1441 filter.
- No new unit-only DEED for 5P / 11P / 14G / 10B / 10F / 11J visible under exact unit strings.
- New-to-this-scan (relative to a first weekly pass): the Dec 2025 TL&R / ASST / AGMT package IDs and party strings above; the 137-unit schedule that includes 10N and excludes the other six pipeline strings.

## HITL gates still closed

- Do not purchase ACRIS PDF images for CRFNs 2025000328421–42825 without operator HITL.
- Do not scrape a836-acris.nyc.gov result pages beyond what Open Data already publishes.
- Do not bulk-export party mailing lists beyond the four entity strings above.

## Dual persist

- Local artifact: `301_E66_WEEKLY_PUBLIC_SCAN_2026-09-09.md`
- GitHub target: `cantgetalonggta-png/live-online-agent-swarm` path `investigations/301_E66_PUBLIC_SCANS/`
- Drive: upload of same markdown via connected Drive artifact tool when available.
