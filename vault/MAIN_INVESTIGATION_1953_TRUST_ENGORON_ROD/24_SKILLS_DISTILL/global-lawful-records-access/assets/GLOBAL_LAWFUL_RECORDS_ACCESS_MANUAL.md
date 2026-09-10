---
title: "Global Lawful Records Access Manual"
subtitle: "Operational checklist · Decision tree · All tools & steps · Business / Deeds / Legal specialty"
author: "live-online-agent-swarm / global-lawful-records-access skill"
date: "2026-09-09"
---

# Global Lawful Records Access Manual

**Lawful channels only. No illegal bypassing. No exploits. No circumvention.**

This manual is the PDF-ready consolidation of the `global-lawful-records-access` skill: complete operational checklist, flowchart decision tree, full tools+steps inventory, and a specialized runbook for **business records, deeds, and legal filings** worldwide (USA-inclusive).

---

# 1. Core doctrines

1. **Authorization** — Access only what you are authorized to access (public portal, statutory fee, FOIA grant, library credential you hold, employment, court order, client engagement).
2. **Ownership / public status** — Prefer public records and open data. Paywalls may have lawful alternatives; they must not be cracked.
3. **Barrier validity** — Login walls, paywalls, role gates, CAPTCHAs, and robots.txt are valid barriers. Route around them only via authorized channels.

**If the only path is illegal, stop and document lawful alternatives.**

---

# 2. Complete operational checklist

## A. Job intake
- [ ] Purpose stated
- [ ] Type: business · property · court · academic · government · corporate · news
- [ ] Country / state / county identified
- [ ] Names / IDs / addresses listed (with spelling variants)
- [ ] Barrier expected
- [ ] Authorization doctrine satisfied
- [ ] HITL if bulk / irreversible
- [ ] Compliance gates passed
- [ ] Data minimization plan

## B. Path selection
- [ ] Free portal → use
- [ ] Statutory fee → pay
- [ ] FOIA path → file
- [ ] Library / ILL → use held credential
- [ ] Role-based → document auth before login
- [ ] Sealed → counsel / motion only
- [ ] No lawful path → STOP

## C. Pre-flight
- [ ] Official portal URL
- [ ] ToS / robots skim for bulk
- [ ] Rate plan
- [ ] Capture plan (PDF, URL, time, SHA-256)
- [ ] Vault path set

## D. Execute by type (tick relevant)
- **Business:** SOS / EDGAR / Companies House / ASIC / MCA / ACRA / OpenCorporates / 990
- **Property:** Recorder / assessor / ACRIS / land registry / fee images
- **Court:** CourtListener → PACER / state portal; public only
- **Government:** Data.gov / reading room → FOIA
- **Academic:** Unpaywall / arXiv / PMC / CORE; no pirate
- **News/archives:** wire, press, Wayback, national archives

## E. Post-collection
- [ ] Provenance logged
- [ ] Hash if evidence
- [ ] SOLID/MAYBE/CONTESTED
- [ ] PII minimized
- [ ] Dual-persist
- [ ] Negatives + FUs logged

## F. Never
Crack · CAPTCHA farm · credential fraud · sealed bypass · pirate academic · private bulk beyond public record

---

# 3. Flowchart decision tree

```
START → TYPE → JURISDICTION → BARRIER → AUTHORIZED?
  NO  → STOP (list FOIA / fee / counsel / library / order)
  YES → branch:

BUSINESS: SOS / EDGAR / Companies House / ASIC / MCA / ACRA / OpenCorporates
PROPERTY: County recorder · ACRIS · HM Land Registry · cadastre (fee OK)
COURT:    CourtListener → PACER · state portals · national courts
          Sealed → motion only
ACADEMIC: DOI → Unpaywall → OA repos → library ILL
GOV:      Open data → FOIA
NEWS:     Free / press / library / Wayback
LOGIN:    Lawful credential only

AFTER: URL+time+portal → hash → confidence tag → minimize → persist → END
```

### Barrier matrix

| Barrier | Lawful | Forbidden |
|---|---|---|
| Free portal | Use | — |
| Statutory fee | Pay | Steal |
| Library wall | Your access | Share/crack login |
| PACER fee | Pay/waiver | Fraud |
| FOIA lag | Wait/appeal | Intrusion |
| Login gate | Authorized credential | Stuffing/spoof |
| CAPTCHA | Manual/API | Farms |
| Sealed | Court order path | Any other |

---

# 4. All tools + all steps

## USA Business
- SEC EDGAR — public filings
- State Secretary of State searches — private entity docs
- IRS EO — Form 990
- OpenCorporates — cross-border
- UCC portals — liens

**Steps:** jurisdiction → search name/officer → download filings → officers/agent → EDGAR if public → UCC optional.

## USA Property
- County recorder / clerk
- County assessor / GIS
- NYC ACRIS + Open Data datasets
- JustFix Who Owns What

**Steps:** address→county/BBL → assessor owner → recorder docs → fee images if needed → chain of title.

## USA Courts
- CourtListener / RECAP (free first)
- PACER (paid federal)
- State e-portals (NYSCEF, etc.)

**Steps:** federal vs state → party search → docket → public PDFs → cite case/doc numbers.

## USA Government
- FOIA.gov, Data.gov, Federal Register, agency reading rooms

**Steps:** search published → else FOIA → track ID → appeal if needed.

## International (sample)
| Country | Business | Property | Courts | Open data |
|---|---|---|---|---|
| UK | Companies House | HM Land Registry | HMCTS | data.gov.uk |
| AU | ASIC | state | Federal Court | data.gov.au |
| IN | MCA | state land | eCourts | data.gov.in |
| SG | ACRA | SLA | eLitigation | data.gov.sg |
| NZ | Companies Office | LINZ | courts | — |
| EU | national + OpenCorporates | cadastre | CJEU | data.europa.eu |

## Academic
Unpaywall · arXiv · PMC · CORE · BASE · DOAJ · SSRN · library ILL

## Universal 10 steps
1 Classify · 2 Authorize · 3 Select portal · 4 Search · 5 Retrieve lawfully · 6 Prove provenance · 7 Minimize · 8 Tag confidence · 9 Persist · 10 Escalate lawfully or stop

---

# 5. Specialized: Business, Deeds & Legal filings

## 5.1 Business records
**Get:** articles, annuals, officers, agents, charges, 10-K/Q, 990s.  
**Playbooks:** USA SOS+EDGAR; UK Companies House (+PSC); AU/IN/SG national registers.  
**Schema:** entity, jurisdiction, reg#, status, officers, agent, address, filing_date, url, time, hash.

## 5.2 Deeds & property
**Get:** deeds, mortgages, liens, tax owner, GIS, condo lots.  
**Playbooks:** US county model; NYC ACRIS bulk join; UK title register fee.  
**Pattern:** occupancy without unit deed → sponsor/corporate hold (document as structure).  
**Schema:** address, parcel/BBL, owner, doc_id, type, date, grantor, grantee, url, time, hash.

## 5.3 Legal filings
**Get:** public pleadings, orders, judgments, dockets.  
**Not:** sealed without order.  
**Playbooks:** CourtListener first → PACER; state portals; foreign national courts.  
**Schema:** case, number, court, doc#, type, filed, parties, counsel, url, time, hash.

## 5.4 Combined recipe
Name → SOS/OpenCorporates → addresses → recorder/ACRIS → CourtListener → graph (OWNS / OFFICER / PARTY) → confidence → dual-persist.

---

# 6. Integration with investigation swarm

- Gates: `legal-osint-compliance-layer`
- Harvest ethics: `ethical-data-harvesting`
- Search: `search-techniques-master` / `dorking-mastery`
- Archives: `wayback-machine-mastery`
- NYC example stack: ACRIS Open Data → parties/legals → JustFix officers → fee deeds → PACER captions

---

# 7. Sign-off block

| Field | Value |
|---|---|
| Job ID | |
| Operator | |
| Date | |
| Types collected | |
| Portals used | |
| Fees paid | Y/N |
| FOIA IDs | |
| SHA-256 list | |
| HITL ref | |
| Compliance pass | Y/N |

---

*End of manual. Skill path: global-lawful-records-access. Generated 2026-09-09.*
