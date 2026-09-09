# RPT-007 — 301 East 66th bulk ACRIS (H1) + full pipeline multi-party roster
**Authority:** `HITL=YES bulk ACRIS 301E66 (H1)`  
**Also requested:** list all people/businesses connecting from pipeline ring; multi-unit list (5P, 11P, 14G, 10N…)  
**Ceiling:** public ACRIS Open Data + DOF/JustFix/HPD-style public + already-public email/unit lists (Curbed/NYPost/BI/process-server exhibits)

---

## 1. Building identity (ROCK_SOLID)

| Field | Value |
|---|---|
| Address | **301 East 66th Street**, New York, NY 10065 (aka 1260–1274 Second Avenue range) |
| BBL (billing / special condo) | **1-01441-7501** (DOF/PropertyShark/JustFix) |
| Tax owner (assessment roll) | **301/66 OWNERS CORP.** — billing 301 E. 66th St. FRNT A |
| Building class | R0 Special Condominium Billing Lot · Tax Class 2 · 16 stories · ~1956 · ~199–200 units |
| Condo unit lots (ACRIS) | Lots **1001–1202** range appear under street #301 / East 66 (178 unit strings in legals) |
| Example unit BBL | **10F → lot 1118** (1-01441-1118) — DOF tax bill shows owner **301/66 OWNERS CORP.** mailing **Apt 10F** |
| Portfolio linkage | JustFix: same portfolio as **1260 Second Avenue**; officers **Mark Epstein, Anthony Barrett, Andrew Losso, Olga Minevich** |

### ACRIS bulk pull (this pass)
| Dataset | Filter | Count |
|---|---|---|
| ACRIS Real Property Legals (Open Data `8h5j-fqxa`) | borough=1, block=1441 | **3,969** rows |
| Filtered to street # **301** + East 66* | | **1,931** legal rows · **227** unique document IDs · **178** unit labels |
| ACRIS Real Property Parties (`636b-3b5g`) | those 227 docs | **613** party rows |
| Files | `21_EAST66_ADDRESS_NETWORK/ACRIS/` | legals JSON, parties JSON, units/lots CSVs |

**Note:** Many pipeline units (5P, 7J, 11P, 14G, 10B, 8A, 11B, 4M, 8H) show **0** ACRIS `unit=` legal rows — consistent with **sponsor/unsold-unit** control (Ossa / 301/66 Owners Corp) where individual condo unit deeds were never recorded under those unit labels, or occupancy was lease/assignment not deed. Units **10F, 10N, 2C, 8C, 11J, 3M, 12B, 2G, 11E** do appear in ACRIS unit field.

---

## 2. Ownership / management entities (ACRIS parties + public)

| Entity | Role | Source |
|---|---|---|
| **301/66 OWNERS CORP.** (variants) | Condo sponsor / unit owner of record on many instruments; tax bill owner | ACRIS parties; DOF |
| **Ossa Properties, Inc.** / Ossa Properties | c/o address on Owners Corp filings; Mark Epstein firm | ACRIS address_1 “C/O OSSA PROPERTIES”; JustFix; Crain’s |
| **301 EAST 66 LLC** | Party on multiple ACRIS docs; c/o Ossa | ACRIS parties |
| **301 East 66th Street Associates L.P.** / **301 EAST 66 ST ASSOCLP** | Historical LP party; address Ossa / Imperial Ppts | ACRIS (incl. FT_ legacy ids) |
| **301 E 66 St Condo Association c/o Ossa** | HPD/openigloo corporate owner label | openigloo / JustFix |
| **Board of Managers / Condominium Board** (many name variants) | Condo board party on liens/agreements | ACRIS parties |
| **30115C Holdings, Inc.** | Unit-level holding (15C) | ACRIS name hit |
| Banks (not pipeline ops) | NY Community Bank, JPMorgan Chase, Citibank, First Republic, MERS, etc. | Mortgages on individual units |

### JustFix / HPD-style public officers (building portfolio)
- **Mark Epstein** — Shareholder  
- **Anthony Barrett** — Head Officer / Agent / Shareholder (Ossa exec who emailed JE on unit 12B)  
- **Andrew Losso** — Officer / Site Manager  
- **Olga Minevich** — common portfolio name  
- **301 E 66 St Condo Association c/o Ossa** — Corporation  

**No individual deed party named “Darren Indyke”, “Richard Kahn”, “Jeffrey Epstein”, or “Les Wexner” in the 613-party extract** — control shows as **corporate/sponsor stack** (Ossa / Owners Corp / 301 East 66 LLC) plus **occupancy/office use** from emails and business registrations.

---

## 3. Multi-unit list (pipeline ring) — master

| Unit | Who / what (public) | Ring layer | ACRIS unit hit? |
|---|---|---|---|
| **5P** | Staffers **Lynn and Jojo** (studio) | staff | No |
| **7J** | **Jean-Luc Brunel** (MC2) one-bedroom | recruiter / associate | No |
| **11P** | **Dana** (studio) | housing | No |
| **14G** | **Sarah** (one-bedroom); process server sought **Sarah Kellen-Vickers** at 14G | assistant / housing | No |
| **8A** | **Renata** → **Karina** (Mar 2012) studio | housing | No |
| **2G** | One-bedroom (name blank on list) | housing | Yes (4) |
| **2C** | **JE’s brother** (**Mark Epstein**) | ownership / family | Yes lot **1006** (12) |
| **10N** | **Guest Apartment**; 2015 renovation hold while occupant used 10B | guest | Yes lot **1125** (12) |
| **8C** | **JE brother kids (Joyce)** | family | Yes lot **1087** (12) |
| **11E** | Converted 1BR | housing | Yes (4) |
| **11B** | Guest apt (**Sam Jaradeh** 6 months) | guest | No |
| **10B** | **DKI, PLLC** — **Darren Indyke** office (~decade) | **control / legal** | No (sponsor pattern) |
| **10F** | **HBRK** — **Richard Kahn / Harry Beller** office; **Nine East 71st Corp** address-of-record; tax owner Owners Corp | **control / accounting** | Yes lot **1118** (4) |
| **4M** | Guest Apt | guest | No |
| **8H** | **Eva’s** apt occupied by housekeeper | staff/housing | No |
| **11J** | **Ehud Barak** + **Nili Priel** (took over; Israeli mission alarm install 2016) | VIP guest | Yes lot **1134** (4) |
| **12B** | Estate-sale unit offered to JE by **Anthony Barrett** (Ossa) Mar 2011 | ownership pipeline | Yes (4) |
| **3M** | Guest (“Code is 7002!”) | guest | Yes (4) |
| **2015 options** | 11J, 11B, 11P, 8A, 10B listed as available for “call her own”; 10N under renovation | assignment pipeline | — |

CSV: `21_EAST66_ADDRESS_NETWORK/UNITS/UNIT_ROSTER_PIPELINE_ACRIS.csv`

---

## 4. Full people / businesses connecting to 301 E 66 (pipeline ring)

### A. Ownership / real-estate stack
1. **Mark Epstein** — brother; Ossa; majority unit pattern; units 2C / 8C family labels  
2. **Ossa Properties, Inc.** — management / c/o  
3. **301/66 Owners Corp.** — deed/tax party  
4. **301 East 66 LLC**  
5. **301 East 66th Street Associates L.P.**  
6. **Anthony Barrett** — Ossa exec; unit inventory emails to JE  
7. **Andrew Losso** — officer / site manager (JustFix)  
8. **Olga Minevich** — portfolio officer name (JustFix)  
9. **Les Wexner** — prior-owner narrative (early 1990s tip/sale to Mark) — not ACRIS grantee this pull  
10. **Nine East 71st Street Corporation** — townhouse entity; **address of record unit 10F** (Crain’s)

### B. Control triangle (legal / accounting offices in building)
11. **Darren K. Indyke** / **DKI, PLLC** — office **10B**  
12. **Richard D. Kahn** — HBRK **10F**  
13. **Harry Beller** — HBRK co-founder **10F**; Butterfly successor narrative  
14. **HBRK** (entity) — 10F  
15. **NES LLC** — Groff employer registration history (BI)

### C. Assistants / NPA-named / ops staff
16. **Lesley Groff** — unit inventory email author; 10th-floor ops; NPA-named  
17. **Sarah Kellen** (Kellen-Vickers) — business reg (SLK Designs); **14G** service attempts; NPA-named  
18. **Nadia Marcinkova / Marcinko** — Aviloop reg at building; doorman said resided; NPA-named  
19. **Adriana Ross** — BI: NPA-named women shared 66th St address historically  
20. **Lynn** and **Jojo** — staff **5P**  
21. **Larry Visoski** (pilot) — deposition referenced Groff/NES at 10th floor (BI)  
22. **Bruce E. Reinhart** — counsel to Kellen/Marcinkova/pilots (not resident; pipeline legal ring)

### D. Housing / model / guest network (public first names or named)
23. **Jean-Luc Brunel** — **7J**; MC2; deceased 2022  
24. **MC2 Models** (entity) — civil filings re housing pipeline  
25. **Dana** — 11P  
26. **Renata** / **Karina** — 8A turnover  
27. **Sarah** (14G list name; may = Kellen or other)  
28. **Sam Jaradeh** — 11B guest 6 months  
29. **Eva** + housekeeper — 8H  
30. Unnamed “models” / overseas recruits — black-book “Apts. for models”; civil 2015 MC2 allegations  
31. 2015 assignment target (redacted in public excerpts) offered 11J/11B/11P/8A/10B

### E. VIP / political / visitor
32. **Ehud Barak** — **11J** extended use; alarm  
33. **Nili Priel** — Barak spouse; coordinated security email  
34. **Israeli permanent mission to UN / “Rafi from the consulate”** — security install coordination (public DOJ email reporting)  
35. **Steve Bannon** — visit reported (NYPost 2026 summary)

### F. Corporate / townhouse cross-links
36. **Jeffrey Epstein** — unit assignment control; informed of sales; not listed as living in building (doorman)  
37. **Maple Inc.** / **Nine East 71st** transfer chain — deed address parked at 10F  
38. **J. Epstein & Co.** / **Epstein Interests** — historical address cross-links to Ossa era (Crain’s secondary)  
39. **Imperial Properties** — appears on legacy ACRIS party address for Associates LP  

### G. Mortgage / bank parties (ACRIS bulk — non-ops, but building graph)
40+ NY Community Bank, JPMorgan Chase, Citibank, First Republic, Washington Mutual, Bowery Savings, Hudson Valley FCU, MERS, individual unit owners (O’Neill, Flaharty, Grotas, Wong, etc.) — ordinary condo finance; **not** elevated to control-triangle without more.

---

## 5. Pattern (PT-006 upgraded with ACRIS)

```
Wexner --prior--> Ossa/Mark --majority--> 301/66 Owners Corp / 301 E 66 LLC
                         |
         +---------------+----------------+
         |               |                |
      10B Indyke      10F HBRK        2C/8C Mark family
      DKI PLLC        Kahn/Beller     + 150+ sponsor units
         |               |                |
         +------ same building stack -----+
                    |
     guest/staff/model units (5P,7J,11P,14G,10N,11J,…)
                    |
         VIP Barak 11J + Israeli security install
                    |
         Nine E 71 Corp address-of-record @ 10F
```

**Abnormal:** legal + accounting control offices **inside** the same vertical stack used for staff/guest/model housing and VIP stays — not separate Midtown towers.

---

## 6. FU updates
- **FU-012** → **PARTIAL CLOSE**: unit roster + ACRIS bulk + parties dual-persisted; still want primary Groff email PDF exhibit if public PACER/FOIA image available  
- **FU-020 NEW**: Pull individual deed images for lots **1118 (10F), 1125 (10N), 1006 (2C), 1087 (8C), 1134 (11J)** from ACRIS document viewer (manual PDF save)  
- **FU-021 NEW**: Party-name search ACRIS for **OSSA PROPERTIES** grantor/grantee citywide (portfolio expansion) — needs separate H1 if bulk  

## 7. Dual-persist targets
Local `21_EAST66_ADDRESS_NETWORK/` · GitHub vault · Drive RPT-007  

## 8. GDPR / H14
EU/Israel public figures (Barak, Priel) and civil-alleged overseas model pipeline: public sources only. No private phone harvest. First-name-only email occupants left as first names unless already public full identity.
