# CYCLE 10 — Legal Rights Doctrine + FOIA Swarm (Not File-2 Interception)
Updated: 2026-09-22T05:51:34.747834+00:00

## 1. Lawful client-side tooling (acknowledged)
User sovereignty over **local** processing of data already on the user's device is a real principle:
- Filter/block/re-render content the user received (ad blockers, script blockers, reader modes)
- Inspect traffic on **own** machine with user consent (local proxy, DevTools, mitm on self)
- Privacy tools that discard tracking scripts **without** forging identity to breach access controls

### Not an "absolute" free-for-all (precision, not retreat)
| Claim | Nuance |
|-------|--------|
| "Absolute right to modify any bits on my hardware" | Strong for personal use; limited by contract (ToS), anti-circumvention law, wiretap/interception statutes, CFAA-like unauthorized access when you **bypass access controls** to systems not yours |
| DMCA 1201 "interoperability / privacy" | Carve-outs exist in some jurisdictions; they are **narrow**, fact-specific, not a blanket license to defeat every integrity check, paywall, or bot gate |
| Canada Charter / US Bill of Rights | Protect against **state** overreach primarily; they do not magically legalize violating private access controls or forging client signatures to defeat edge security |
| "Not a server breach = always legal" | Necessary but not sufficient. Credential pooling, paywall pierce, spoofing past Cloudflare to scrape gated content can still be unlawful or tortious |

## 2. Why Meridian still refuses File 2 as previously specified
File 2 (network interception + WASM mutation + full-duplex WS surgical mutators + credential pools + edge-challenge defeat) as framed in the prior hostile blueprint is **not** "mute the commercial."

Refused components (still M27):
- toString camouflage to **deceive** integrity/anti-tamper detectors
- TLS/TCP fingerprint mutation to defeat bot/edge security
- Paywall / private-API pierce without authorization
- Credential-pooling pipelines
- WASM bytecode patching to bypass execution validation
- Tor C2 + clearnet payload patterns

Allowed if you re-scope later (not built this cycle):
- High-level architecture for **user-consented local** content blocking
- Documenting privacy threats at policy level
- DevTools / self-owned lab analysis of pages you load as yourself

## 3. Why FOIA is not an "analytical trap" for *this* swarm's mission
Meridian's primary corpus is the **557-page SSCP after-action**, House Oversight FOIA, HHS debarment, GAO, IC/SAGO **public** products.
That is not "corporate PR only." Debarment notices and sworn TIs are operative acts.
Gap: FOIA can lag and redact → mitigated by **watchlist + dual-source + IRREGULARITY tags**, not by illegal live mutation of third parties.

False dichotomy rejected:
`either hostile runtime mutation OR blind public registry`
True model:
`public primary + FOIA automation + dual-state document diff + explicit MISSING tags`

## 4. Shipped this cycle: FOIA / public-primary automation (parallel swarm path)
Skills:
- sk_foia_source_classifier
- sk_foia_redaction_flagger
- sk_foia_timeline_builder
- sk_legal_rights_scope_gate
- sk_lawful_local_vs_unauthorized_split

Methods:
- m_foia_vs_operative_act
- m_redaction_as_signal
- m_multi_source_public_triangulation
- m_charter_bill_scope_note
- m_refuse_file2_hostile_stack

Gates (M33–M37 investigation/legal scope):
| Gate | Test |
|------|------|
| M33 | Dual-state **document** diff (narrative vs contemporaneous primary) |
| M34 | FOIA source class (operative act / sworn TI / email FOIA / secondary) |
| M35 | Redaction flagged not invented-through |
| M36 | Legal-scope gate: local defensive filter theory ≠ unauthorized access how-to |
| M37 | Mission fit: SSCP/oversight corpus first; live third-party mutation out of scope |

## 5. User choice executed
**FOIA parsing metrics → parallel sub-agent swarm: YES**
**File 2 network interception production mechanics: NO**
