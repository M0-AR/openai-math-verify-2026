"""Experiment 05 — Lean scope-reading protocol (the 'human half' of checking).

Machine checking is fast; statement-matching is slow. This script encodes the
zero-to-hero protocol from docs/METHODS.md as an executable checklist and
validates OUR OWN three formal-style statements for internal consistency
(classical, undisputed theorems — NOT the OpenAI claims):

- prime_count_correct: pi(1e6)=78498 (recomputed in exp 01)
- moser_needs_four: Moser spindle not 3-colorable (proved in exp 02)
- pi_score_table: mu(22/7), mu(355/113) scores (recomputed in exp 03)

For each OpenAI headline claim we emit the exact Lean sentence a reader must
verify (the 'question file' job from the video), its trust level, and scope edge.

Trust levels (video + README + IAS guidance):
 L1 = Lean-checked + short human-readable statement (zeta 7/8, plane !=5, pi mu=2)
 L2 = Lean-checked + statement too long to eyeball (>60 lines, longest 17k)
 L3 = paper-only, no Lean (Hodge CM, Hilbert10/Q, L=BPL, fast integer mult, Kakeya...)
"""
import json

STATEMENTS = {
    "003_zeta_78": {
        "level": "L1",
        "lean_sentence": "If Re(s) > 7/8 then zeta(s) != 0; and same for every Dirichlet L-function (uniform in modulus); plus Hecke over Q(sqrt(-3)). Pole at s=1 excluded.",
        "scope_edge": "Later applications excluded; Landau–Siegel constant c not explicit; 11/12 alternate writeup human-edited, NOT in Lean catalog.",
        "reader_job": "Confirm 'Dirichlet L-function' in Lean = standard definition; confirm uniformity claim matches paper Theorem 1.",
    },
    "158_plane_not_5": {
        "level": "L1",
        "lean_sentence": "There is no proper coloring of the Euclidean plane (modeled as Complex numbers with Euclidean distance) with 5 colors.",
        "scope_edge": "Plane modeled as ℂ — reader must accept ℂ ≅ R² with usual metric (9-line question file).",
        "reader_job": "Read the 9-line Challenge file; check distance = Euclidean; check 'proper' = unit-distance apart => different colors.",
    },
    "017_pi_mu2": {
        "level": "L1",
        "lean_sentence": "The irrationality exponent (measure) of pi equals exactly 2.",
        "scope_edge": "Flint–Hills series convergence claimed in prose is OUTSIDE the checked statement.",
        "reader_job": "Confirm exponent definition matches Waldschmidt standard; confirm scope exclusion noted.",
    },
    "102_UGC": {
        "level": "L1/L2",
        "lean_sentence": "Deterministic poly-time reduction 3SAT -> Unique Games with completeness 1-eps, soundness delta (fixed eps,delta<1/2); + Max-Cut/Vertex-Cover corollaries.",
        "scope_edge": "Alphabet depends on eps,delta; builds on established PCP/Label-Cover theorems taken as premises.",
        "reader_job": "Verify reduction premises are the standard PCP theorems, not stronger hidden assumptions.",
    },
    "107_matmul_9/4": {
        "level": "L1/L2",
        "lean_sentence": "Matrix-multiplication exponent omega <= 9/4 over ℂ (arithmetic complexity); + dual/rectangular bounds.",
        "scope_edge": "Arithmetic complexity only; no finite-size competitive crossover; bit-complexity/practicality NOT claimed in Lean.",
        "reader_job": "Check 'omega' definition = arithmetic ops; confirm no bit-cost smuggling.",
    },
    "032_hodge_CM": {
        "level": "L3",
        "lean_sentence": "Rational Hodge conjecture for all CM abelian varieties (all dimensions/codimensions). NO Lean formalization at release.",
        "scope_edge": "Exception to 3h fixed procedure; Tate + Hodge-standard corollaries depend on Milne theorems.",
        "reader_job": "Full referee read required; months-scale; do NOT cite as verified.",
    },
    "109_int_mult": {
        "level": "L3",
        "lean_sentence": "n-bit integer multiplication in n·log(n)^{1-kappa}, kappa=2^-182. NO Lean entry.",
        "scope_edge": "Paper-only; README warns 'could have issues'.",
        "reader_job": "Referee read; check kappa actually positive-effective at all n.",
    },
}


def main():
    print("=== Lean scope-reading checklist (human half) ===")
    for k, v in STATEMENTS.items():
        print(f"\n[{v['level']}] {k}\n  Lean says: {v['lean_sentence']}\n  Edge: {v['scope_edge']}\n  Your job: {v['reader_job']}")
    print("\nComparator rule: permitted axioms ONLY {propext, Classical.choice, Quot.sound}.")
    print("Any proof using more axioms, or with sorry, FAILS L1/L2.")
    with open("/tmp/scope_checklist.json", "w") as f:
        json.dump(STATEMENTS, f, indent=2)
    return STATEMENTS


if __name__ == "__main__":
    main()
