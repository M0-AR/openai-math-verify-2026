"""Experiment 03 — Pi irrationality score + Flint–Hills partial sums (real data).

Score definition (video): |pi - p/q| = 1/q^mu  ->  mu = -log|pi-p/q|/log q.
- mu(22/7) ~ 3.4, mu(355/113) ~ 3.2 (lucky early convergents).
- Later convergents must fall back toward 2 if mu(pi)=2 (family 017 claim).
- Best proved classical bound ~7.1 (Salikhov 7.6063 / later refinements);
  we recompute the *observed* scores from real convergents of pi.
- Flint–Hills sum S_N = sum_{n<=N} 1/(n^3 sin^2 n): spike at n=355 adds ~24.6;
  we compute partial sums live to show convergence behavior is delicate and
  that family 017's scope EXCLUDES the series (scope note) — flagged honestly.

Uses mpmath with 50 digits; fully deterministic, no network.
"""
from fractions import Fraction
import math

import mpmath


def convergents_of_pi(n_terms=12):
    mpmath.mp.dps = 60
    # continued fraction of pi: [3;7,15,1,292,1,1,1,2,1,3,1,...]
    cf = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1]
    convs = []
    for k in range(2, min(n_terms + 1, len(cf) + 1)):  # skip 3/1 (log 1 = 0)
        num, den = cf_frac(cf[:k])
        convs.append((int(num), int(den)))
    return convs, float(mpmath.pi)


def cf_frac(cf):
    # convergent numerator/denominator of [a0;a1,a2,...]
    h1, h2 = 1, 0
    k1, k2 = 0, 1
    for a in cf:
        h1, h2 = a * h1 + h2, h1
        k1, k2 = a * k1 + k2, k1
    return h1, k1


def score(p, q, pi):
    if q <= 1:
        return float("nan")
    err = abs(pi - p / q)
    if err <= 0:
        return float("inf")
    return -math.log(err) / math.log(q)


def flint_hills(N):
    mpmath.mp.dps = 50
    s = mpmath.mpf(0)
    terms = {}
    for n in range(1, N + 1):
        t = 1 / (mpmath.mpf(n) ** 3 * (mpmath.sin(n) ** 2))
        s += t
        if n in (113, 355, 104348, 312689):
            terms[n] = float(t)
    return float(s), terms


def main():
    mpmath.mp.dps = 50
    pi = float(mpmath.pi)
    convs, _ = convergents_of_pi(12)
    print(" p/q        err            mu-score")
    rows = []
    for p, q in convs:
        mu = score(p, q, pi)
        rows.append((p, q, mu))
        print(f" {p:>7}/{q:<7} {abs(pi-p/q):.3e}   {mu:.3f}")
    # checks on the two famous ones
    d = {q: mu for p, q, mu in rows}
    assert abs(d[7] - 3.4) < 0.15, d[7]
    assert abs(d[113] - 3.2) < 0.15, d[113]
    # later convergents should be near 2 (necessary footprint of mu=2)
    late = [mu for p, q, mu in rows if q > 1000]
    print(f"late-convergent scores (q>1000): {[round(v,3) for v in late]} (cluster near 2 => consistent with mu=2)")
    S, terms = flint_hills(5000)
    print(f"Flint-Hills S_5000 ~= {S:.6f}; spike terms: {terms}")
    print("NOTE: family 017 Lean scope covers mu(pi)=2 ONLY; series convergence is OUTSIDE the checked statement.")
    return {"convergents": [(p, q, mu) for p, q, mu in rows], "S_5000": S, "spikes": terms}


if __name__ == "__main__":
    main()
