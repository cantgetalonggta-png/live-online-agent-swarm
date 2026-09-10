# Global Lawful Access — Decision Flowchart

```
START: What do you need?
│
├─[Business filing]──► Country known?
│                      ├─ USA → SOS / EDGAR / OpenCorporates
│                      ├─ UK → Companies House
│                      ├─ Other → national register (see country-portals.md)
│                      └─ Unknown country → OpenCorporates search first
│
├─[Property / deed]──► Country + locality known?
│                      ├─ USA → County recorder / ACRIS / assessor
│                      ├─ UK → HM Land Registry (fee)
│                      └─ Other → national cadastre (fee often required)
│
├─[Court filing]─────► Federal / state / foreign?
│                      ├─ US federal → CourtListener then PACER
│                      ├─ US state → state judiciary portal
│                      └─ Foreign → national court portal
│                      NOTE: Sealed = stop without court order
│
├─[Academic paper]───► Have DOI?
│                      ├─ Yes → Unpaywall / publisher OA / arXiv / PMC
│                      └─ No → title search CORE/BASE/DOAJ/library
│                      NEVER: pirate / sci-hub instructions in this skill
│
├─[Government doc]───► Already published?
│                      ├─ Yes → Data.gov / agency site / Federal Register
│                      └─ No → FOIA or equivalent request
│
├─[News article]─────► Free reprint / press release / library DB / wire
│
└─[Behind login only]─► Do you have lawful credential?
                       ├─ Yes → use it; document auth basis
                       └─ No → list how to obtain auth (employment, counsel,
                                FOIA, court order, library card). STOP if none.
```

## Barrier handling matrix

| Barrier | Lawful response | Unlawful (forbidden) |
|---|---|---|
| Free public portal | Use it | — |
| Statutory fee | Pay fee | Steal document |
| Library paywall | Use library card / ILL | Share login / crack |
| PACER fee | Account + pay or fee waiver | Account sharing fraud |
| FOIA delay | Wait / appeal | Hack agency systems |
| Login / role gate | Get authorization | Credential stuffing, spoofing |
| CAPTCHA / bot wall | Manual / authorized API | CAPTCHA farms, evasion |
| Sealed court file | Motion to unseal via counsel | Any other access |
