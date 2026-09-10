# Complete Operational Checklist — Global Lawful Records Access

**Print / tick every job. Lawful channels only. No bypass. No exploits.**

---

## A. Job intake (before any search)

- [ ] **Purpose stated** (investigation / journalism / due diligence / academic / personal public-record)
- [ ] **Information type** selected: business · property · court · academic · government · corporate · news
- [ ] **Country / state / county / province** identified
- [ ] **Entity or person name** (exact spelling variants listed)
- [ ] **Address / parcel / case number / DOI / EIN** if known
- [ ] **Barrier expected**: free · fee · login · subscription · FOIA · sealed · role-based
- [ ] **Authorization doctrine** satisfied (public / fee / FOIA / library / employment / court order / client)
- [ ] **HITL** obtained if bulk, multi-jurisdiction, or irreversible external action
- [ ] **legal-osint-compliance-layer** gates passed
- [ ] **Data minimization** plan (fields needed only)

**STOP if:** only path is illegal circumvention.

---

## B. Path selection (decision)

- [ ] Open public portal exists → use it
- [ ] Statutory fee registry → budget fee + account
- [ ] FOIA / equivalent → prepare request text + agency
- [ ] Library / ILL / university access held → use credential
- [ ] Role-based → document authorization basis before login
- [ ] Sealed court → counsel + motion path only
- [ ] No lawful path → document gap; do not invent access

---

## C. Pre-flight technical

- [ ] Portal URL verified (official `.gov` / registry domain preferred)
- [ ] robots.txt / ToS skimmed for bulk rules
- [ ] Rate-limit plan if multiple queries
- [ ] Capture plan: screenshot · PDF download · hash (SHA-256) · URL + timestamp
- [ ] Storage location set (vault folder / evidence tag)
- [ ] No third-party keys harvested or reused

---

## D. Execution by type

### D1 Business filings
- [ ] State of incorporation known
- [ ] SOS / Companies House / ASIC / MCA / ACRA / OpenCorporates searched
- [ ] Articles / annual report / officers / agent captured
- [ ] Public company → EDGAR 10-K/10-Q/8-K pulled
- [ ] Nonprofit → IRS 990 pulled
- [ ] Cross-check OpenCorporates for multi-jurisdiction entities

### D2 Property / deeds
- [ ] County (or NYC BBL) known
- [ ] Recorder / ACRIS / land registry searched by address · APN · owner
- [ ] Deed / mortgage / lien / transfer list captured
- [ ] Assessor tax owner + mailing noted
- [ ] Statutory copy fee paid if image needed
- [ ] GIS map screenshot if useful

### D3 Court filings
- [ ] Federal vs state vs foreign decided
- [ ] CourtListener / RECAP tried first (US federal free path)
- [ ] PACER used with paid account if needed (or fee waiver)
- [ ] State judiciary portal used for state cases
- [ ] Docket + public PDFs only
- [ ] Sealed items logged as unavailable without order

### D4 Government / FOIA
- [ ] Reading room / Data.gov searched first
- [ ] FOIA filed with clear description + date range + format
- [ ] Request ID tracked
- [ ] Appeal path noted if denied

### D5 Academic
- [ ] DOI → Unpaywall / OA
- [ ] arXiv / PMC / CORE / BASE / DOAJ tried
- [ ] Library / ILL if still closed
- [ ] No shadow-library / pirate path

### D6 News / archives
- [ ] Press release / wire / free reprint searched
- [ ] Library database if subscribed
- [ ] Wayback / national archive for historical public pages
- [ ] Copyright respected (summarize; no bulk republication of protected text)

---

## E. Post-collection quality

- [ ] Source URL + portal name + retrieval datetime logged
- [ ] SHA-256 of primary files computed (if evidence)
- [ ] SOLID / MAYBE / CONTESTED tags applied to claims
- [ ] Personal data minimized; GDPR/CCPA-aware handling if EU/CA persons
- [ ] Dual-persist (GitHub / Drive / vault) if investigation SOP
- [ ] Dead ends logged in false-leads folder
- [ ] Next FU listed if incomplete

---

## F. Absolute never-do (hard fail)

- [ ] ~~Crack paywall / login~~
- [ ] ~~CAPTCHA farm / bot evasion~~
- [ ] ~~Credential stuffing / shared PACER fraud~~
- [ ] ~~Hack FOIA / sealed systems~~
- [ ] ~~Sci-Hub / pirate academic~~
- [ ] ~~Doxx / private directory bulk beyond public record~~

**Sign-off:** Operator ________ Date ________ Job ID ________
