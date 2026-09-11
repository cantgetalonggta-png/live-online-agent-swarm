"""
Bayesian Belief Network + Analysis of Competing Hypotheses (ACH)
Implements truth-verification skill: priors, likelihoods, posteriors,
dynamic updating, diagnostic evidence.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum
import math
from datetime import datetime


class HypothesisStatus(str, Enum):
    SUPPORTED = "supported"
    CONTESTED = "contested"
    CONTRADICTED = "contradicted"
    UNTESTED = "untested"


@dataclass
class Evidence:
    id: str
    description: str
    source: str
    likelihood_if_h: float  # P(E|H)  0..1
    likelihood_if_not_h: float  # P(E|~H)
    quality: float = 0.7  # source reliability 0..1
    independent: bool = True

    def weight(self) -> float:
        return max(0.05, min(1.0, self.quality))


@dataclass
class Hypothesis:
    id: str
    text: str
    prior: float = 0.5
    posterior: float = 0.5
    status: HypothesisStatus = HypothesisStatus.UNTESTED
    evidence_for: List[str] = field(default_factory=list)
    evidence_against: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class ACHMatrix:
    claim: str
    hypotheses: List[Hypothesis]
    evidence: List[Evidence]
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())


def _clamp(x: float, lo: float = 1e-9, hi: float = 1.0 - 1e-9) -> float:
    return max(lo, min(hi, x))


def bayesian_update(prior: float, likelihood_h: float, likelihood_not_h: float, weight: float = 1.0) -> float:
    """
    Single evidence Bayesian update.
    P(H|E) ∝ P(E|H) * P(H)
    Softened by weight (source quality / independence).
    """
    prior = _clamp(prior)
    lh = _clamp(likelihood_h)
    ln = _clamp(likelihood_not_h)
    # Soft likelihoods toward 0.5 when weight < 1
    lh = 0.5 + weight * (lh - 0.5)
    ln = 0.5 + weight * (ln - 0.5)
    numer = lh * prior
    denom = numer + ln * (1.0 - prior)
    if denom <= 0:
        return prior
    return _clamp(numer / denom)


def sequential_update(prior: float, evidences: List[Evidence], favor: bool = True) -> float:
    """Apply multiple pieces of evidence sequentially."""
    p = prior
    for e in evidences:
        if favor:
            p = bayesian_update(p, e.likelihood_if_h, e.likelihood_if_not_h, e.weight())
        else:
            # Against: flip likelihoods
            p = bayesian_update(p, e.likelihood_if_not_h, e.likelihood_if_h, e.weight())
    return p


def normalize_posteriors(hyps: List[Hypothesis]) -> None:
    total = sum(h.posterior for h in hyps) or 1.0
    for h in hyps:
        h.posterior = h.posterior / total


def status_from_posterior(p: float) -> HypothesisStatus:
    if p >= 0.75:
        return HypothesisStatus.SUPPORTED
    if p <= 0.25:
        return HypothesisStatus.CONTRADICTED
    if 0.4 <= p <= 0.6:
        return HypothesisStatus.UNTESTED
    return HypothesisStatus.CONTESTED


def run_ach(
    claim: str,
    hyp_texts: Optional[List[str]] = None,
    evidence_items: Optional[List[Dict]] = None,
) -> ACHMatrix:
    """
    Full ACH + Bayesian pipeline for a claim.
    Default hypotheses if none supplied.
    """
    if not hyp_texts:
        hyp_texts = [
            "Claim is accurate and well-sourced (primary evidence)",
            "Claim is partially true / incomplete",
            "Claim is contradicted by stronger public evidence",
            "Claim is untestable with current public data",
        ]

    hyps = [
        Hypothesis(id=f"H{i+1}", text=t, prior=1.0 / len(hyp_texts), posterior=1.0 / len(hyp_texts))
        for i, t in enumerate(hyp_texts)
    ]

    evidences: List[Evidence] = []
    if evidence_items:
        for i, item in enumerate(evidence_items):
            evidences.append(
                Evidence(
                    id=item.get("id", f"E{i+1}"),
                    description=item.get("description", str(item)),
                    source=item.get("source", "unknown"),
                    likelihood_if_h=float(item.get("likelihood_if_h", 0.7)),
                    likelihood_if_not_h=float(item.get("likelihood_if_not_h", 0.3)),
                    quality=float(item.get("quality", 0.7)),
                    independent=bool(item.get("independent", True)),
                )
            )
    else:
        # Default synthetic evidence based on claim length / presence of URLs heuristics
        has_public = "http" in claim.lower() or "archive" in claim.lower() or "public" in claim.lower()
        evidences = [
            Evidence(
                id="E1",
                description="Public-source provenance present",
                source="heuristic:source-surface",
                likelihood_if_h=0.8 if has_public else 0.4,
                likelihood_if_not_h=0.3 if has_public else 0.6,
                quality=0.6,
            ),
            Evidence(
                id="E2",
                description="Claim specificity and falsifiability",
                source="heuristic:specificity",
                likelihood_if_h=0.65 if len(claim) > 40 else 0.45,
                likelihood_if_not_h=0.4,
                quality=0.55,
            ),
            Evidence(
                id="E3",
                description="Absence of immediate contradiction in vault context",
                source="heuristic:no-contradiction",
                likelihood_if_h=0.6,
                likelihood_if_not_h=0.45,
                quality=0.5,
            ),
        ]

    # Update each hypothesis against all evidence (simple independent model)
    # H1 (accurate) gets high P(E|H) for supportive evidence; H3 (contradicted) inverse
    for h in hyps:
        p = h.prior
        for e in evidences:
            if "accurate" in h.text.lower() or "well-sourced" in h.text.lower():
                p = bayesian_update(p, e.likelihood_if_h, e.likelihood_if_not_h, e.weight())
                h.evidence_for.append(e.id)
            elif "contradicted" in h.text.lower():
                p = bayesian_update(p, e.likelihood_if_not_h, e.likelihood_if_h, e.weight())
                h.evidence_against.append(e.id)
            elif "partially" in h.text.lower() or "incomplete" in h.text.lower():
                # Mild support
                mid_h = 0.5 + 0.3 * (e.likelihood_if_h - 0.5)
                mid_n = 0.5 + 0.3 * (e.likelihood_if_not_h - 0.5)
                p = bayesian_update(p, mid_h, mid_n, e.weight() * 0.8)
            else:
                # untestable: evidence weakly favors
                p = bayesian_update(p, 0.55, 0.5, e.weight() * 0.5)
        h.posterior = p
        h.status = status_from_posterior(p)

    normalize_posteriors(hyps)
    for h in hyps:
        h.status = status_from_posterior(h.posterior)

    return ACHMatrix(claim=claim, hypotheses=hyps, evidence=evidences)


def best_hypothesis(matrix: ACHMatrix) -> Hypothesis:
    return max(matrix.hypotheses, key=lambda h: h.posterior)


def confidence_to_claim_status(posterior: float) -> str:
    """Map to SOLID / MAYBE / CONTESTED / CONTRADICTED."""
    if posterior >= 0.8:
        return "SOLID"
    if posterior <= 0.2:
        return "CONTRADICTED"
    if 0.35 <= posterior <= 0.65:
        return "MAYBE"
    return "CONTESTED"


def matrix_to_dict(matrix: ACHMatrix) -> dict:
    return {
        "claim": matrix.claim,
        "updated_at": matrix.updated_at,
        "hypotheses": [
            {
                "id": h.id,
                "text": h.text,
                "prior": round(h.prior, 4),
                "posterior": round(h.posterior, 4),
                "status": h.status.value,
                "evidence_for": h.evidence_for,
                "evidence_against": h.evidence_against,
            }
            for h in matrix.hypotheses
        ],
        "evidence": [
            {
                "id": e.id,
                "description": e.description,
                "source": e.source,
                "likelihood_if_h": e.likelihood_if_h,
                "likelihood_if_not_h": e.likelihood_if_not_h,
                "quality": e.quality,
            }
            for e in matrix.evidence
        ],
        "best": {
            "id": best_hypothesis(matrix).id,
            "text": best_hypothesis(matrix).text,
            "posterior": round(best_hypothesis(matrix).posterior, 4),
            "status": best_hypothesis(matrix).status.value,
        },
        "claim_status": confidence_to_claim_status(best_hypothesis(matrix).posterior),
    }
