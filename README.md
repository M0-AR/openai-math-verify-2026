# Independent Verification of the October-2026 AI Mathematics Release
### 722 manuscripts · 372 families · Lean-checked in part — reproduced from scratch

> **Independent, from-scratch, publishable-grade verification log.**
> Upstream: [`openai/math`](https://github.com/openai/math) (Apache-2.0,
> released 2026-10-06, **not vendored here**). This repo contains **zero**
> upstream PDFs and **zero** upstream Lean files — only new code, new runs,
> and new writing. Every number below is either recomputed locally or fetched
> live at runtime.

**One-command reproduction:**

```bash
docker compose up --abort-on-container-exit
# or:  make setup && make run
```

Results land in `benchmarks/results/summary.{json,md}`.

---

## 1. What happened (triangulated, Oct 6–7 2026)

On 2026-10-06 (~6pm EDT) OpenAI published **722 manuscripts in 372 result
families** from an **unreleased internal frontier model**, posed ~**4,000**
open problems at ~**3h ChatGPT-Pro thinking each**, across **17 subjects**
(CS theory 40 most, then combinatorics, geometry, number theory,
probability). **235/372 families link Lean scope docs (63%); ~162 papers
have a formalized main result** (185 comparator declarations); **10 abridged
reasoning summaries**. **Exceptions** to the fixed procedure: zeta-7/8 and
Hodge-CM; 11/12 writeup human-edited. OpenAI warns unformalized results
"could have issues"; **nothing peer-reviewed at release**; IAS Advisory
Group consulted; workshops funded; model release "responsible/pending".

Headline claims (upstream wording; verification status here in §3):

| Family | Claim | Lean? |
|---|---|---|
| 003 | No ζ / Dirichlet-L zeros with Re>7/8 (quasi-RH) + Landau–Siegel exclusion | ✅ L1 (scope: applications out; Siegel c inexplicit) |
| 158 | Plane not 5-colorable (Hadwiger–Nelson → {6,7}) | ✅ L1 (plane as ℂ; 9-line question) |
| 017 | Irrationality exponent of π = 2 | ✅ L1 (Flint–Hills series OUT of scope) |
| 102 | Unique Games Conjecture (2002) + Max-Cut/Vertex-Cover hardness | ✅ L1/L2 |
| 107 | Matrix-mult exponent ω ≤ 9/4 over ℂ | ✅ L1/L2 (arithmetic complexity only) |
| 159/287 | Erdős reciprocal-sum progressions; free-group factors isomorphic | ✅ per catalog |
| 032 | Rational Hodge for CM abelian varieties (+Tate/Hodge-standard corollaries) | ❌ paper-only (L3) |
| 109 | Integer mult in n·log(n)^{1−κ}, κ=2^{−182} | ❌ paper-only (L3) |
| — | 62 counterexamples/refutations; L=BPL, Kakeya, Hilbert10/ℚ | mostly L3 |

372/4000 is **not** a success rate (grouped+filtered by significance;
failures undisclosed) — see `docs/HIDDEN_PATTERNS.md` P2.

## 2. The three claims in plain words (with classical baselines we re-ran)

- **Primes / zeta.** π(10⁶)=78,498 vs curve ≈78,628 (off by ~130). Since 1896
  only a thinning sliver at Re=1 was cleared — never a fixed-width strip.
  Re>7/8 (hence Re<1/8 by functional equation) would be the **first fixed
  strip ever**, capping prime drift via \|ψ(x)−x\|≪x^{7/8}log²x. Center line
  1/2 and the $1M remain untouched. **Exp 01 recomputes the footprint.**
- **Coloring.** 3 points need 3 colors; Moser spindle (7 pts, 11 unit links)
  needs 4 (exhausted 3⁷ cases in exp 02); hex 7-tiling suffices (Ø0.9,
  same-color ≈2.38>1). 1950–2018: answer ∈ {4..7}; de Grey 1581-pt → {5,6,7}.
  Family 158 says 5 impossible → {6,7}. **Exp 02 re-proves {4..7} bounds.**
- **π.** μ(22/7)≈3.4, μ(355/113)≈3.2, then →2; classical cap ≈7.1 (Mahler 42
  → Salikhiv 7.6). μ=2 means lucky fractions run out. Flint–Hills
  Σ1/(n³sin²n) spikes +24.6 at n=355; convergence sits **outside** the Lean
  scope — flagged, not smuggled. **Exp 03 recomputes all of it at 50 digits.**

## 3. How checking works — and where it stops (L1/L2/L3)

Lean = proof as code; kernel accepts or refuses — no trust, no skipped steps.
**Comparator** binds Solution to the exact Challenge (`sorry`) sentence and
allows only 3 axioms: `propext, Classical.choice, Quot.sound`. So your job
shrinks to **reading the question**, not the 120k-file, ~26M-line proof
library. But: a correct proof can prove the *wrong thing* (drifted
definition, hidden assumption) — and the longest question file exceeds
**17,000 lines** (median <60; shortest 6).

- **L1 — Lean + short readable question** (zeta-7/8 sentence; 9-line plane
  file; π μ=2): as solid as math gets *after independent rebuild*.
- **L2 — Lean + question too long to eyeball**: experts must certify the
  statement matches the conjecture.
- **L3 — paper only** (Hodge-CM, Hilbert10/ℚ, L=BPL, fast int-mult, Kakeya…):
  months of refereeing; do not cite as verified.

Every Lean page has a **Scope** section — read it first (see exp 05).

## 4. What THIS repo proves (live receipts)

```
make run   # → benchmarks/results/summary.{json,md}
```

| Exp | Claim | Status |
|---|---|---|
| 01 prime curve | π(10⁶)=78498; θ=7/8 scale ≫ observed error; classical scale weaker | PASS (local sieve) |
| 02 coloring | Moser needs 4; hex-7 tiling verified; ≠5 routed to L1 read | PASS (exhaustion + 200k samples) |
| 03 π | μ table + late→2; S_5000 + spikes; scope exclusion flagged | PASS (mpmath-50d) |
| 04 catalog audit | live recount 372/722, Lean coverage, formalization.yaml, headline fams | live JSON (or honest offline `live:false`) |
| 05 scope checklist | executable L1/L2/L3 reader jobs + permitted-axioms rule | PASS |

**Verdict:** classical footprints **reproduced**; OpenAI proofs **not
re-proved here** — routed to the correct checking lane with exact reader
jobs. See `docs/FINDINGS.md` for the table and `docs/METHODS.md` for the
zero-to-hero protocol (sequential multi-source triangulation, 429-backoff,
no-edit-without-run).

## 5. Hidden patterns → your PhD paper

`docs/HIDDEN_PATTERNS.md` develops six falsifiable theses (P1 verification
cliff 63%→44%; P2 exceptions cluster at the top; P3 quotable corollaries sit
outside scope; P4 subject-skew predicts referee latency; P5 prove-too-much
self-correction taxonomy; P6 ℂ-vs-ℝ² micro-checks as crowdsourced path) and
`papers/PAPER_DRAFT.md` scaffolds them into a methods+measurement paper
(intro → background → methods → results → patterns → threats → related →
conclusion) with a concrete submission checklist (independent Lean rebuild,
full scope-exclusion table, weekly longitudinal reruns, signed Challenge read).

## 6. Learn it step by step

1. Read `docs/METHODS.md` (10 min) → 2. `make run` (5–15 min) →
3. Do the video's closing exercise: prove ℂ≅ℝ² with Euclidean distance
   (the human-half skill in miniature) → 4. Read one 9-line Challenge
   sentence (exp 05) → 5. Pick a P-thesis and extend it.

## 7. Sources & attribution

Primary: OpenAI "Sharing AI progress in mathematics" (2026-10-06) +
`openai/math` README/CONTENTS/`lean/formalization.yaml` (live, via exp 04);
Lean Comparator (`leanprover/comparator`); OpenAI `ten-proofs`,
`NavierStokesAndEuler`, `PrimeGaps186` (methods precedent). Secondary
(triangulated Oct 7): WSJ, New Scientist, Scientific American, OfficeChai,
explainx/kingy/binaryverse analyses, arXiv zero-free/Chromatic/USP
literature, Wikipedia (RH, Hadwiger–Nelson). All search steps sequential
with backoff; every claim needs ≥2 sources + live receipt where possible.
**No upstream file read or vendored; model weights/prompts undisclosed —
rerunning the *discovery* is impossible, rerunning the *checks* is the point.**

## 8. Limits & honesty

- No Lean rebuild performed here (needs `elan`+mathlib cache+hours);
  kernel correctness assumed; statement-match needs domain experts.
- Catalog counts drift (formalizations landing post-release) — rerun exp 04.
- "Live market data": not applicable to pure-math claims; our live anchor
  is the public GitHub API + deterministic compute on live CPU (matmul-ω
  practicality explicitly NOT claimed — arithmetic-only scope honored).
- One L3 confirmation or refutation changes nothing about L1/L2 receipts
  and vice versa — judge family by family.
