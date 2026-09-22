# PRIMARY DOC PROOF ENGINE v1 — Autonomous Cycle
Updated: 2026-09-22T05:27:07.465934+00:00

## Mission
ALWAYS locate primary docs for claims that still need them. If proof exists in public record, fetch and attach. If missing, log MISSING and keep CONTESTED — never invent.

## Separation (doctrine M5)
- **SOLID process failures** stand without origin closure.
- **Origin H1/H2** remain CONTESTED without smoking gun.
- **H3 bioweapon** nearly excluded (IC).

## Claim status board

| ID | Tag | Primary need | Proof attempt result |
|----|-----|--------------|----------------------|
| C01 | CONTESTED | HIGH | CIA 2025 low-conf lean FOUND; serology MISSING; stay CONTESTED |
| C02 | SOLID influence / CONTESTED conspiracy | MED | FOIA emails IN_SSCP; bribery MISSING |
| C03 | SOLID | LOW | HHS debarment PDF FOUND (Jan 2025 Notice+ARM) |
| C04 | SOLID process | LOW-MED | Morens FOIA IN_SSCP |
| C05 | SOLID | LOW | Fauci/Collins TI quotes FOUND |
| C06 | OVERSTATED absolute | MED | Flip-flop FOUND; absolute overstated |
| C07 | SOLID harms / CONTESTED net | MED | Harms FOUND_REF; net CONTESTED |
| C08 | SOLID process / CONTESTED legal | LOW-MED | Directive FOUND_REF |
| C09 | SOLID early / CONTESTED treaty | MED | IHR/WHO FOUND_REF |
| C10 | SOLID scale | LOW | GAO/OIG ranges FOUND |
| C11 | SOLID process | MED | Production logs IN_SSCP |

## Still need (autonomous watchlist)
1. WIV illness serology / notebooks (C01)
2. Intermediate host isolate (C01 H2 side)
3. Payment trail if full Proximal conspiracy escalated (C02)
4. Adjudicated Cuomo false-statement judgment if claimed (C08)
5. Reconciled single PPP $ if forced (prefer GAO ranges) (C10)

## Locked this cycle with live public primary
- **C03**: https://oversight.house.gov/wp-content/uploads/2025/01/Dr.-Peter-Daszak-HHS-Notice_Jan-17-2025_Redacted.pdf — 5-year debarment; Daszak terminated Jan 6 2025
- **C03**: ARM EcoHealth same date — present responsibility failure
- **C01**: CIA Jan 25 2025 — research-related more likely, **low confidence**, both scenarios plausible, no new intel claim
- **C05**: Fauci TI — 6-ft "sort of just appeared" / empiric; Collins TI no supporting evidence
- **C10**: GAO UI fraud $100–135B; SBA OIG ~$200B potentially fraudulent pandemic business loans (method-dependent)

## Engine forever rule
```
foreach claim:
  if needs_primary:
    search(.gov, FOIA, IC, court, peer-review)
    attach(FOUND | IN_SSCP | MISSING)
    if MISSING and tag was SOLID: downgrade or split
    if FOUND and only process: keep M5 (process ≠ origin)
  fire M1,M4,M5,M8,M10
  emit AAO atom
```
