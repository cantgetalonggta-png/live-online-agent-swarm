# LOG — DocumentCloud 25547032 + IA epsteindocs (HITL=YES)
**Time:** 2026-09-09 (operator turn with full URL list)  
**Authority:** `All tools skills etc HITL=YES: run` + listed URLs  
**Ceiling:** public-record only

## URLs processed
| URL | Result |
|---|---|
| https://s3.documentcloud.org/documents/25547032/doj-jeffrey-epstein-files-released-2025-02-27.pdf | **HELD** local 36,352,499 bytes · 224 pages · Xerox PrimeLink scan 2025-02-27 |
| https://www.documentcloud.org/documents/25547032-…/?mode=text\|document\|grid | SPA shell only (Cloudflare/JS); content from S3 PDF + local extract |
| …#document/p224 | **OCR+pdftotext** — last page of redacted numbered list (entries 241–254) |
| https://ia600705.us.archive.org/21/items/ | items root HTML saved |
| https://ia600705.us.archive.org/21/items/epsteindocs/ | index + metadata API · **561 files · ~4.99 GB · Case 18-2868 label** |

## DOJ 2025-02-27 release — substance
1. **Page 1 (letter):** AG Pamela Bondi → FBI Director Kash Patel, 27 Feb 2025. States prior request returned ~200 pages (flight logs, contact list, victim names/phones). Source said FBI NY FO holds thousands more. Orders full delivery by 08:00 28 Feb 2025 + 14-day OPR-style personnel report.
2. **Pages 2–223:** Scanned production consistent with flight logs / contact sheets / numbered lists. Heavy redaction stamps “Redacted to protect potential victim information.” Text layer weak; middle pages mostly OCR noise.
3. **Page 224 (operator anchor):** Terminal redacted list lines **241–254** + redaction stamp. No readable names, phones, or institutions on this page.

## Control-triangle keyword scan (full extractable text, 105k chars)
**HITS:** Bondi(1), Patel(2), FBI(5), victim(10), redacted(9), flight log(1), contact(1), phone(1).  
**ZERO (not in extractable text):** Indyke, Kahn, Southern Trust, 1953 Trust, Wheatley, Engoron, Reinhart, Wexner, Maxwell, NPA, OPR, Deutsche, JPMorgan, Ghislaine, Acosta, SDNY/SDFL, Mar-a-Lago, Black Book.

**Tag:** This release is **process/oversight correspondence + redacted victim-contact/flight material**, not a 1953-Trust money/control primary. Tag **RS-012_DOJ_2025_BONDI_PATEL_LETTER** = ROCK_SOLID for letter existence; control-triangle names = **NULL in this pack** (not contested — simply absent from extractable layer).

## IA epsteindocs priority inventory (not full bulk — H1 gate)
- 39 original PDFs among 561 derivative files
- Map-relevant already partially staged under `20_ARCHIVE_EPSTEINDOCS/priority/` (plea, bail, Wexner letters/report, flight logs djvu)
- Black book PDF name on IA: `Jeffrey_Epstein39s_Little_Black_Book_unredacted.pdf` (4.6 MB) — already dual-sourced via separate IA black-book item in SQUADS path
- Largest: `Epstein-Docs.pdf` ~388 MB (would need **H1 bulk** if full download)

## Dual-persist targets
- Local vault: `19_DOJ_2025_RELEASE/`, `20_ARCHIVE_EPSTEINDOCS/`
- GitHub investigation tree + Drive when quota OK

## What this pass does NOT do (still gated)
- Full IA mirror of 5 GB (H1)
- Full multi-hour OCR of every middle DOJ page (H2) — middle pages image-noise; low map value
- Promote redacted victim list numbers into entity graph without public unredacted primary (ceiling)
