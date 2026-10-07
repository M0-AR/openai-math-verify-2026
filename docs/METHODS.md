# METHODS — Zero-to-Hero Verification Protocol (best practice, 2026–2027)

## 0. What we verify (and what we do NOT claim)

Upstream: `openai/math` (Apache-2.0), released 2026-10-06: **722 manuscripts /
372 families** from ~4,000 posed problems, ~3h ChatGPT-Pro thinking each,
**235/372 link Lean**, **162 papers w/ formalized main result** (Oct-7 count),
10 abridged reasoning summaries. Exceptions to the fixed procedure: zeta-7/8
and Hodge-CM; 11/12 writeup human-edited. **Nothing peer-reviewed at release.**

This repo is **independent, from-scratch**: no upstream PDF/Lean vendored.
We verify *footprints and checkability*, we do NOT re-prove headline theorems.

## 1. Three trust levels (L1/L2/L3)

- **L1 — Lean-checked + short statement** (human can read the Challenge file:
  zeta Re>7/8, plane≠5, π μ=2). Verdict ≈ as solid as math gets *once an
  independent party rebuilds the proof and confirms statement-match*.
- **L2 — Lean-checked + long statement** (60–17,000 lines; reading the question
  is itself research). Needs expert sign-off on definitions.
- **L3 — paper-only** (Hodge-CM, Hilbert10/ℚ, L=BPL, fast int-mult, Kakeya…).
  README warns "could have issues". Full referee timeline (months).

## 2. Comparator best practice (leanprover/comparator)

1. Challenge (`sorry`) and Solution files kept separate; Challenge trusted.
2. `comparator_config.json`: `theorem_names`, `permitted_axioms =
   [propext, Quot.sound, Classical.choice]` ONLY.
3. Build both in `landrun` sandbox; export via `lean4export`.
4. Check: same statement, axioms ⊆ permitted, Lean kernel (+ optional
   external kernel e.g. nanoda) accepts.
5. Definition-holes need an extra human verifier (reflexivity trap).

Red flags: extra axioms, `sorry` in Solution, statement drift
(quietly changed definition / extra assumption), scope exclusions
(e.g. Flint–Hills series outside π scope; Landau–Siegel constant inexplicit).

## 3. Search-triangulation used here (Oct 2026–2027 window)

One-query-at-a-time across: websearch (Exa), DuckDuckGo, OpenResearch
(web/OpenAlex/HN/news), paper-search (arXiv 22-source unified), agent-reach
(web), wiki, Kaggle, gitmcp, GSD websearch — with 5–10s backoff on 429 and
DuckDuckGo-lite fallback. Every number in README re-checked against ≥2
independent secondary sources + live GitHub API (exp 04).

## 4. Reproducibility contract

- `docker compose up` reproduces everything; `make run` runs exps 01–05.
- No file edited without an executed run (`benchmark_runner.py` receipt).
- Live-data anchor: exp 04 queries `raw.githubusercontent.com/openai/math`
  at runtime; offline → explicit `live:false`, never faked pass.
- Real computed data: sieve to 10⁶, 3^7 coloring exhaustion, mpmath-50-digit
  π convergents, Flint–Hills S_5000 — all deterministic seeds.
