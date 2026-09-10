# Flowchart-Style Decision Tree — Global Lawful Records Access

```
┌──────────────────────────────────────────┐
│  START: Need a document / record?        │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│  Q1. What TYPE?                          │
│  business | property | court | academic  │
│  government | corporate | news           │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│  Q2. WHERE (country / state / county)?   │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│  Q3. What BARRIER?                       │
│  free | fee | login | FOIA | sealed      │
└──────────────────┬───────────────────────┘
                   ▼
        ┌──────────┴──────────┐
        │ Authorized path?    │
        └──────────┬──────────┘
           yes │         │ no
               ▼         ▼
         CONTINUE    ┌─────────────────────┐
                     │ STOP. List how to   │
                     │ get authorization:  │
                     │ FOIA, counsel,      │
                     │ library, employer,  │
                     │ court order, fee.   │
                     └─────────────────────┘

══════════════ TYPE BRANCHES ══════════════

[BUSINESS]
  USA private ──► State SOS search ──► articles/annual/agent
  USA public ───► SEC EDGAR ──► 10-K/10-Q/8-K
  USA nonprofit ► IRS EO 990
  UK ───────────► Companies House
  AU ───────────► ASIC
  IN ───────────► MCA
  SG ───────────► ACRA
  Unknown ──────► OpenCorporates ──► then national register

[PROPERTY]
  USA ──► County recorder + assessor
       └─ NYC ──► ACRIS Open Data + a836-acris (images may fee)
  UK ───► HM Land Registry (fee)
  NZ ───► LINZ
  Other ► National cadastre (often fee)

[COURT]
  US federal ──► CourtListener/RECAP ──► if missing, PACER (pay)
  US state ────► State judiciary e-portal
  UK ──────────► HMCTS
  EU ──────────► CJEU + national
  Sealed? ─────► Counsel + motion ONLY ──► else STOP

[ACADEMIC]
  DOI? ──yes──► Unpaywall ──► OA PDF
       ──no───► title @ CORE/BASE/DOAJ/arXiv/PMC
  Still closed ► Library / ILL you hold
  Still closed ► STOP (no pirate path)

[GOVERNMENT]
  Published? ──yes──► Data.gov / agency / Federal Register
             ──no───► FOIA.gov (or national equivalent)
  Denied ───────────► Administrative appeal

[NEWS]
  Free reprint / press release / wire
  Library DB if subscribed
  Wayback if historical public page

[LOGIN / ROLE ONLY]
  Have credential (job / bar / client / court)?
    yes ► Use; log auth basis
    no  ► Obtain auth first; do not spoof

══════════════ AFTER RETRIEVAL ══════════════

  Capture URL + time + portal
       │
       ▼
  Hash file (SHA-256) if evidence
       │
       ▼
  Tag SOLID / MAYBE / CONTESTED
       │
       ▼
  Minimize PII; dual-persist per SOP
       │
       ▼
  END (or open FU if incomplete)
```

## Barrier matrix (quick)

| You face | Do this | Never |
|---|---|---|
| Free portal | Download + cite | — |
| Statutory fee | Pay | Steal |
| Library wall | Your card / ILL | Share login |
| PACER fee | Pay or waiver | Fraudulent account |
| FOIA lag | Wait / appeal | Intrusion |
| Login gate | Lawful credential | Stuffing / spoof |
| CAPTCHA | Manual / official API | Farms / bots |
| Sealed file | Motion via counsel | Any other access |
