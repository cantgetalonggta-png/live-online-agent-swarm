---
name: global-lawful-records-access
description: Fully expanded international USA-inclusive step-by-step system for legally accessing business records, deeds, court filings, academic papers, government documents, corporate data, and news worldwide. Only lawful authorized alternative channels — no illegal bypassing, exploits, or circumvention. Triggers on global public records access, SEC EDGAR, Companies House, PACER, FOIA, land registry, OpenCorporates, Unpaywall, lawful paywall alternatives, or how to legally obtain restricted public information.
---

# Global Lawful Records Access

Maximum-detail operational blueprint for **lawful** access to restricted or hard-to-reach information worldwide.  
**Absolute ban:** no illegal bypassing, no exploits, no CAPTCHA circumvention, no credential stuffing, no unauthorized portal access.

## Core Doctrines (apply before every request)

1. **Authorization** — You may only access what you are authorized to access (public portal, paid statutory fee, FOIA grant, employment, court order, client engagement, library credential you hold).
2. **Ownership / Public Status** — Prefer truly public records and open data; paywalls may have lawful alternatives (library, OA, statutory registry fee) but must not be cracked.
3. **Barrier Validity** — Login walls, paywalls, role gates, and robots.txt are valid barriers. Route around them only via **authorized** channels (FOIA, registry fee, academic OA, press credential, legal counsel).

## When to Use This Skill

- User asks how to legally get business filings, deeds, court docs, academic papers, government docs, corporate data, or news.
- Investigation needs PACER, state SOS, county recorder, Companies House, ASIC, land registries, FOIA, Unpaywall, etc.
- Operator asks for “global access manual,” country-by-country portals, or decision tree for restricted info.
- Pair with `legal-osint-compliance-layer` (gates) and `ethical-data-harvesting` (methods) before any bulk collect.

## 10-Phase International Access Workflow

### Phase 1 — Identify Information Type
1. Category: business · property · court · academic · government · corporate · news.
2. Country / sub-jurisdiction (state, county, province).
3. Barrier type: paywall · login · subscription · role-based · fee · sealed.
4. Apply doctrines above; if only illegal path exists → **STOP** and say so.

### Phase 2 — USA Business Records
**Tools:** SEC EDGAR · State Secretary of State business search · IRS EO Search · OpenCorporates  
**Steps:**
1. State of registration.
2. SOS portal → name / officer / entity ID.
3. Pull articles, annual reports, agent, status.
4. Public companies → EDGAR 10-K / 10-Q / 8-K / S-1.
5. Nonprofits → IRS Form 990.

### Phase 3 — USA Property Records
**Tools:** County Recorder / Clerk · Assessor · GIS · DOF/ACRIS (NYC) · JustFix  
**Steps:**
1. Identify county (or borough/block/lot for NYC).
2. Recorder search: address · APN · owner.
3. Retrieve deeds, liens, mortgages, transfers.
4. Assessor for valuation / tax owner.
5. Pay statutory copy fees when required — lawful.

### Phase 4 — USA Court Records
**Tools:** PACER (federal) · CourtListener / RECAP · State judiciary portals  
**Steps:**
1. Federal vs state.
2. PACER account (paid per-page; fee waivers exist for qualifying users).
3. State portal free/paid dockets.
4. Retrieve complaints, orders, judgments, dockets — only public filings.
5. Sealed / confidential = not available without court order.

### Phase 5 — USA Government Documents
**Tools:** FOIA.gov · agency reading rooms · Federal Register · Data.gov · USA.gov  
**Steps:**
1. Search open data / reading rooms first.
2. File FOIA if not published (expect delays; track request ID).
3. Download released packages only.

### Phase 6 — International Business Records
**Tools:** Companies House (UK) · ASIC (AU) · MCA (IN) · ACRA (SG) · EU national registers · OpenCorporates · Sunbiz (FL example)  
**Steps:** country → national registry → company name → filings (often small fee).

### Phase 7 — International Property / Cadastre
**Tools:** HM Land Registry (UK) · LINZ (NZ) · SLA (SG) · India state land records · EU cadastre systems  
**Steps:** country → land registry → address/parcel → statutory fee → title/deed extract.

### Phase 8 — International Court Records
**Tools:** UK Courts & Tribunals · CJEU · Singapore eLitigation · India eCourts · Australia Federal Court  
**Steps:** jurisdiction → judiciary portal → case/party → public filings only.

### Phase 9 — Academic / Scientific
**Tools:** Unpaywall · arXiv · PubMed Central · CORE · BASE · DOAJ · SSRN · institutional repos · library ILL  
**Steps:** DOI → OA resolver → legal full text. Never pirate PDFs from shadow libraries via this skill.

### Phase 10 — News, Archives, Role-Based
**News:** wire (AP/Reuters) · press releases · library databases · government announcements.  
**Archives:** Internet Archive (public captures) · national archives · authorized government mirrors.  
**Role-based:** employment · accreditation · court order · client permission → then portal.  
**Verify authorization before every role-based login.**

## Complete Global Toolset (quick index)

| Domain | Primary portals |
|---|---|
| US business | SEC EDGAR, state SOS, IRS EO, OpenCorporates |
| US property | County recorder/assessor, ACRIS (NYC), JustFix |
| US courts | PACER, CourtListener, state portals |
| US gov | FOIA.gov, Data.gov, Federal Register |
| UK | Companies House, HM Land Registry, Courts & Tribunals, data.gov.uk |
| AU | ASIC, Federal Court portal |
| IN | MCA, eCourts, state land, OGD |
| SG | ACRA, SLA, eLitigation, data.gov.sg |
| EU | National business registers, CJEU, EU Open Data |
| Academic | Unpaywall, arXiv, PMC, CORE, BASE, DOAJ |
| Global corp | OpenCorporates |
| Archives | archive.org, national archives |

Full country list: `references/country-portals.md`  
Decision tree: `assets/decision-flowchart.md`  
USA deep dive: `references/usa-deep-dive.md`

## Decision Tree (short)

```
Need document?
  ├─ Is it already open (gov portal / OA / free docket)? → Download + cite
  ├─ Statutory fee registry (SOS, land, Companies House)? → Pay fee → retrieve
  ├─ FOIA / equivalent request channel? → File request → wait → retrieve release
  ├─ Library / university / ILL subscription you hold? → Use credentialed access
  ├─ Court order / employment / client auth required? → Obtain auth first
  └─ Only illegal bypass remains? → STOP. Report lawful alternatives only.
```

## Integration with Swarm / Investigation Stack

- **Before collect:** `legal-osint-compliance-layer` gates.
- **How to harvest ethically:** `ethical-data-harvesting`.
- **Search operators:** `search-techniques-master` / `dorking-mastery` (public indexes only).
- **Archives:** `wayback-machine-mastery` / `wayback-ghost-index-public`.
- **NYC property (301 E 66 pattern):** ACRIS Open Data + county recorder fees — already in investigation vault.
- **Output:** provenance URL + timestamp + portal name + fee paid Y/N.

## Success Criteria

- Every path is lawful and attributable.
- User is never instructed to crack, spoof, or evade technical controls.
- When access is legitimately impossible without authorization, skill says so and lists how to seek that authorization.
- Outputs cite portal + jurisdiction + retrieval date.

## Self-Evolution

After each successful lawful retrieval, append working portal URL + quirks to `references/country-portals.md`. Prune dead links quarterly.

## Generated operator pack (2026-09-09)

- `assets/COMPLETE_OPERATIONAL_CHECKLIST.md`
- `assets/FLOWCHART_DECISION_TREE_FULL.md`
- `assets/GLOBAL_LAWFUL_RECORDS_ACCESS_MANUAL.md` (PDF-ready master)
- `references/ALL_TOOLS_ALL_STEPS.md`
- `references/SPECIALIZED_BUSINESS_DEEDS_LEGAL.md`
- Artifacts export: `/workspace/artifacts/GLOBAL_LAWFUL_RECORDS_ACCESS_GUIDE/` (md + html + pdf)
