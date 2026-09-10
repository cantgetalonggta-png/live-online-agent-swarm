# Specialized Manual — Business Records, Deeds & Legal Filings (Worldwide, Lawful Only)

## Purpose
Operator runbook for the three document classes used most in corporate/property investigations.  
Integrates with ACRIS / SOS / PACER workflows already used in the 1953 Trust / 301 E 66 vault.

---

## Part I — Business records

### What you can lawfully get
- Formation / articles / certificates
- Annual reports / confirmation statements
- Officers, directors, registered agents
- Registered office addresses
- Charges / UCC liens (jurisdiction-dependent)
- SEC periodic filings (public companies)
- Nonprofit 990s

### What you usually cannot get without extra authority
- Full beneficial ownership in secrecy jurisdictions without register access
- Bank account details
- Non-public tax returns
- Internal board minutes (unless filed or produced in discovery)

### USA playbook
1. OpenCorporates → candidate jurisdictions.
2. State SOS → entity page → PDF filings.
3. If Delaware: status + agent; order certified docs if needed (fee).
4. If officers point to FL/NY/CA → run those SOS too.
5. EDGAR if “Inc” is public issuer.
6. IRS EO if nonprofit.
7. UCC debtor search in formation + HQ states.

### UK playbook
1. Companies House search → filing history.
2. Download confirmation statement, accounts (if filed), charges.
3. PSC (persons with significant control) register when published.

### Other
- AU ASIC, IN MCA, SG ACRA: same pattern — search → pay small fee if required → download.
- Always prefer official register over secondary scrapers for court use.

### Output schema (CSV/JSON)
`entity_name, jurisdiction, reg_number, status, officers, agent, address, filing_date, source_url, retrieved_at, hash`

---

## Part II — Deeds & property

### What you can lawfully get
- Recorded deeds, mortgages, assignments, liens, easements
- Tax assessor owner + values
- Parcel maps / GIS
- Condo unit schedules (when recorded)
- ACRIS parties/legals bulk (NYC Open Data)

### What needs fee or visit
- Certified copies
- Some historical image reels
- Some non-digitized counties

### USA county playbook
1. Address → county (or NYC borough/block/lot).
2. Assessor → owner of record + mailing.
3. Recorder grantor/grantee or doc type filter.
4. Build chain of title table.
5. For condos: unit lot numbers (e.g. 301 E 66 lots 1001–1202).
6. If unit occupied but no deed → sponsor/owners-corp hypothesis (document as pattern, not crime).

### NYC ACRIS playbook (proven in vault)
1. Open Data legals `borough=1, block=…`
2. Filter street number + name.
3. Collect document_ids → parties table.
4. Classify person vs bank vs sponsor entity.
5. Fee portal for deed PDF images when needed.

### UK / other
- HM Land Registry title register + title plan (fee).
- National cadastre equivalents — always statutory fee routes.

### Output schema
`address, parcel_or_bbl, owner_of_record, doc_id, doc_type, record_date, grantor, grantee, source_url, retrieved_at, hash`

---

## Part III — Legal filings (court)

### What you can lawfully get
- Public complaints, answers, motions, orders, judgments
- Dockets / RECAP uploads
- Oral argument audio where published
- Opinions

### What you cannot
- Sealed exhibits, grand jury, some juvenile, some settlement conf.
- Without court order or party status

### Federal USA playbook
1. CourtListener party/case search.
2. Download RECAP docs free.
3. If missing critical doc → PACER account → download → (optionally) upload to RECAP.
4. Cite: `Case Name, No. __ (Court), Dkt. No. __, Doc. __ (date)`.

### State USA playbook
1. Identify e-filing portal (NYSCEF, etc.).
2. Public access search.
3. Pay portal fees if required (lawful).

### Civil investigation tips
- Search all name variants + entity names + “as executor” / “trustee”.
- Pull caption page for counsel list → new SOS targets.
- Timeline docket events → TL- CSV.

### Output schema
`case_name, case_no, court, doc_no, doc_type, filed_date, parties, counsel, source_url, retrieved_at, hash`

---

## Part IV — Combined investigation recipe (entity → property → court)

```
1. Name / entity from lead
2. SOS + OpenCorporates → officers + addresses
3. Addresses → county recorder / ACRIS → deeds + unit map
4. Officers + entity → CourtListener / state portal → dockets
5. Graph edges: entity—OWNS→parcel; person—OFFICER→entity; person—PARTY→case
6. Tag confidence; dual-persist; open FUs for fee-only images
```

## Part V — Compliance hard stops
- No sealed access without order
- No paywall cracks
- No bulk personal-data beyond public record without H14-style HITL
- GDPR minimization for EU persons even when names appear in US dockets
