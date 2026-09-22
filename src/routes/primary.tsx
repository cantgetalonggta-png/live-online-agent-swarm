import { createFileRoute, Link } from "@tanstack/react-router";
import {
  PROOF_META,
  PROOF_CLAIMS,
  STILL_NEED,
  LOCKED_PRIMARY,
  TI_ANCHORS,
  CYCLE8,
} from "@/data/primaryProof";
import {
  LEO_AUTO_BOUNDED,
  LEO_AUTO_SLOGAN,
  OPEN_ACCESS_LIVE,
  FOIA_WARRANTS,
  VAUGHN_TRACKER_SUMMARY,
  CYCLE21_META,
} from "@/data/leoAuto";
import { Shell } from "@/components/shell";

export const Route = createFileRoute("/primary")({ component: PrimaryPage });

function PrimaryPage() {
  return (
    <Shell>
      <p className="font-mono text-xs text-primary tracking-widest uppercase">
        Cycle {CYCLE21_META.cycle} · LEO · M38 · {PROOF_META.version}
      </p>
      <h1 className="text-3xl font-semibold mt-1 tracking-tight">{PROOF_META.title}</h1>
      <p className="text-muted text-sm mt-2 max-w-2xl">{PROOF_META.rule}</p>
      <div className="mt-3 flex flex-wrap gap-3 text-sm">
        <Link to="/explore" className="text-primary min-h-11 inline-flex items-center">
          Explore research →
        </Link>
        <Link to="/doctrine" className="text-primary min-h-11 inline-flex items-center">
          Doctrine →
        </Link>
        <Link to="/ach" className="text-primary min-h-11 inline-flex items-center">
          ACH dual-conf →
        </Link>
        <Link to="/skills" className="text-primary min-h-11 inline-flex items-center">
          Skills →
        </Link>
      </div>

      <div className="mt-6 grid sm:grid-cols-3 gap-3">
        <div className="rounded-lg border border-border bg-surface p-3">
          <div className="font-mono text-2xl">{CYCLE8.footnoteHits}</div>
          <div className="text-xs text-muted">footnote/citation hits</div>
        </div>
        <div className="rounded-lg border border-border bg-surface p-3">
          <div className="font-mono text-2xl">{CYCLE8.gates.length}</div>
          <div className="text-xs text-muted">new gates M19–M22</div>
        </div>
        <div className="rounded-lg border border-border bg-surface p-3">
          <div className="font-mono text-2xl">{CYCLE8.packs.length}</div>
          <div className="text-xs text-muted">cycle-8 primary packs</div>
        </div>
      </div>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">Claim primary status</h2>
        <div className="mt-3 space-y-2">
          {PROOF_CLAIMS.map((c) => (
            <article key={c.id} className="rounded-lg border border-border bg-surface p-4">
              <div className="flex flex-wrap justify-between gap-2">
                <span className="font-mono text-xs text-primary">{c.id}</span>
                <span className="font-mono text-[10px] text-muted">need {c.primaryNeed}</span>
              </div>
              <h3 className="font-medium mt-1">{c.claim}</h3>
              <p className="text-sm text-muted mt-1">{c.tag}</p>
              <p className="text-sm mt-2">{c.result}</p>
              {c.watch ? <p className="text-xs text-irreg mt-1 font-mono">watch: {c.watch}</p> : null}
            </article>
          ))}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">TI anchors (process primary)</h2>
        <ul className="mt-3 space-y-2">
          {TI_ANCHORS.map((t) => (
            <li key={t.claim} className="rounded-lg border border-border bg-surface p-3 text-sm">
              <span className="font-mono text-primary mr-2">{t.claim}</span>
              {t.ti}
            </li>
          ))}
        </ul>
      </section>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">Locked primary</h2>
        <div className="mt-3 space-y-2">
          {LOCKED_PRIMARY.map((L) => (
            <div key={L.claim} className="rounded-lg border border-solid/30 bg-solid/5 p-3">
              <div className="font-mono text-xs text-solid">{L.claim}</div>
              <ul className="text-sm mt-1 list-disc pl-5">
                {L.docs.map((d) => (
                  <li key={d}>{d}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      
      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">LEO auto-verdict (document matrix)</h2>
        <p className="text-xs text-muted mt-1">Polarity-aware. Slogan matrix vs bounded true wording. Analytical only (M30).</p>
        <div className="mt-3 overflow-x-auto">
          <table className="w-full text-sm border border-border">
            <thead className="bg-surface-2 text-left">
              <tr>
                <th className="p-2">Claim</th>
                <th className="p-2">Bounded</th>
                <th className="p-2">If slogan overclaim</th>
                <th className="p-2">Omit</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(LEO_AUTO_BOUNDED).map((id) => (
                <tr key={id} className="border-t border-border">
                  <td className="p-2 font-mono text-primary">{id}</td>
                  <td className="p-2">{LEO_AUTO_BOUNDED[id].tag}</td>
                  <td className="p-2 text-muted">{LEO_AUTO_SLOGAN[id]?.tag ?? "—"}</td>
                  <td className="p-2 font-mono text-xs">{LEO_AUTO_BOUNDED[id].omission}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>


      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">
          Cycle 21 · Open Access Live (OpenAlex + Unpaywall)
        </h2>
        <p className="text-xs text-muted mt-1">
          M38 open APIs only · C02 Proximal Origin OA via Unpaywall · updated {CYCLE21_META.updated.slice(0, 10)}
        </p>
        <div className="mt-3 grid md:grid-cols-2 gap-3">
          <div className="rounded-lg border border-border bg-surface p-4">
            <div className="font-mono text-xs text-primary">C01 · OpenAlex</div>
            <ul className="mt-2 space-y-2 text-sm">
              {OPEN_ACCESS_LIVE.C01.openalex.slice(0, 3).map((w) => (
                <li key={w.id}>
                  <span className="font-mono text-[10px] text-muted">{w.id}</span>
                  <div>{w.title}</div>
                </li>
              ))}
            </ul>
          </div>
          <div className="rounded-lg border border-border bg-surface p-4">
            <div className="font-mono text-xs text-primary">C02 · Proximal Origin OA</div>
            {OPEN_ACCESS_LIVE.C02.unpaywall ? (
              <div className="mt-2 text-sm space-y-1">
                <div className="font-medium">{OPEN_ACCESS_LIVE.C02.unpaywall.title}</div>
                <div className="font-mono text-xs text-muted">DOI {OPEN_ACCESS_LIVE.C02.unpaywall.doi}</div>
                <div className="text-xs">
                  is_oa={String(OPEN_ACCESS_LIVE.C02.unpaywall.is_oa)} · {OPEN_ACCESS_LIVE.C02.unpaywall.oa_status}
                </div>
                {OPEN_ACCESS_LIVE.C02.unpaywall.best_oa_url ? (
                  <a
                    className="text-primary text-xs break-all underline"
                    href={OPEN_ACCESS_LIVE.C02.unpaywall.best_oa_url}
                    target="_blank"
                    rel="noreferrer"
                  >
                    OA PDF (Unpaywall)
                  </a>
                ) : null}
              </div>
            ) : (
              <p className="text-sm text-muted mt-2">No Unpaywall row</p>
            )}
            <ul className="mt-3 space-y-1 text-xs text-muted">
              {OPEN_ACCESS_LIVE.C02.openalex.slice(0, 2).map((w) => (
                <li key={w.id}>
                  <span className="font-mono">{w.id}</span> · cites {w.cited_by}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">
          FOIA warrants · Vaughn waves
        </h2>
        <p className="text-xs text-muted mt-1">
          Tracker: {VAUGHN_TRACKER_SUMMARY.claims_in_tracker} claims ·{" "}
          {VAUGHN_TRACKER_SUMMARY.waves_per_claim} waves · filed {VAUGHN_TRACKER_SUMMARY.filed_count} (templates
          only)
        </p>
        <div className="mt-3 overflow-x-auto">
          <table className="w-full text-sm border border-border">
            <thead className="bg-surface-2 text-left">
              <tr>
                <th className="p-2">Claim</th>
                <th className="p-2">Tag</th>
                <th className="p-2">Window</th>
                <th className="p-2">Vaughn</th>
                <th className="p-2">Warrant</th>
              </tr>
            </thead>
            <tbody>
              {FOIA_WARRANTS.map((w) => (
                <tr key={w.claim_id} className="border-t border-border">
                  <td className="p-2 font-mono text-primary">{w.claim_id}</td>
                  <td className="p-2">{w.tag}</td>
                  <td className="p-2 font-mono text-xs">
                    {w.date_start} → {w.date_end}
                  </td>
                  <td className="p-2">{w.vaughn ? "YES" : "—"}</td>
                  <td className="p-2 font-mono text-xs text-muted">{w.warrant}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-irreg">Still need (M20 watchlist)</h2>
        <ul className="mt-3 space-y-1 text-sm">
          {STILL_NEED.map((s) => (
            <li key={s} className="rounded border border-border bg-surface p-3">
              {s}
            </li>
          ))}
        </ul>
      </section>

      <section className="mt-10">
        <h2 className="font-mono text-xs uppercase tracking-widest text-muted">M19–M22</h2>
        <ul className="mt-3 space-y-1 text-sm">
          {CYCLE8.gates.map((g) => (
            <li key={g} className="rounded border border-border bg-surface p-3 font-mono text-xs">
              {g}
            </li>
          ))}
        </ul>
      </section>
    </Shell>
  );
}
