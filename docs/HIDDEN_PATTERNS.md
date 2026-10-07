# HIDDEN PATTERNS — Non-obvious structure for a future PhD paper

These are *observations about the release and its verification surface*,
each phrased as a falsifiable thesis with a concrete next experiment.
Nothing here claims a new theorem.

## P1. The "verification cliff": 63% → 44% → ?

235/372 families (63%) link a Lean *scope doc*, but only ~162/372 papers
(44%) have a *formalized main result* in `formalization.yaml` (185 comparator
declarations — some papers check >1 sentence). Thesis: **scope-doc ≠ proof**;
the drop-off measures formalization debt. Next: track the ratio weekly via
exp 04; plot debt burn-down as OpenAI "adds more Lean proofs" per its promise.

## P2. Exceptions cluster at the top

The two most famous items (zeta-7/8, Hodge-CM) are *both* declared exceptions
to the fixed 3h procedure, and the 11/12 alternate was human-edited. Thesis:
**breakthrough-scale outputs did not come from the benchmarked pipeline** —
implications for "372/4000 success-rate" readings (README: grouped+filtered by
significance; failures undisclosed). Next: demand per-result compute/prompt
disclosure (cf. AGMAI request) before any scaling-law claim.

## P3. Scope exclusions hide in the most quotable corollaries

π: series convergence excluded. Zeta: applications + explicit Siegel constant
excluded. Matmul: bit-complexity/practicality excluded. Fourier: Lean proves a
*weaker subsequential* bound. Thesis: **press-friendly corollaries systematically
sit outside the checked statement**. Next: build a scope-exclusion table for all
162 formalized papers (parse every scope note) — a publishable survey chapter.

## P4. Subject skew predicts referee latency

Lean coverage by area is wildly uneven (logic 6/6, combinatorics ~33/37 vs.
alg-geom ~7/36, topology ~3/18 at release). Thesis: **L3-heavy fields
(alg-geom, topology, PDEs) will dominate the error surface**, matching the
README warning. Next: correlate coverage vs. time-to-first-independent-confirm;
Kakeya/Hilbert-Smith/L=BPL as canaries.

## P5. Reasoning summaries show "prove-too-much" self-correction

The 42-page/45-stage π summary repeatedly hits "Barrier/lost gains/
obstruction" and at one stage the model notices its lemma would *prove too
much*, backtracks, and repairs. Thesis: **overgeneralization-detection is the
visible signature of the model's internal verifier** — worth mining across all
10 summaries for a taxonomy of self-corrections (a genuine AI-for-math
contribution even if some theorems fall). Next: NLP-stage mining of the 10
summaries; code stages as "barrier → repair" graphs.

## P6. The ℂ-vs-ℝ² micro-check is the whole ballgame in miniature

The video's closing question ("plane written as ℂ — really the same plane?")
has answer yes (ℂ≅ℝ², usual metric) — trivial, yet it *is* the human-half job:
every L1 verdict reduces to a pile of such micro-checks. Thesis: **a
crowdsourced 'question-file reading log' (one signed-off micro-check per
Challenge file) is the fastest path to community confidence**. Next: open a
405-file reading tracker; this repo's exp 05 is its seed.

## From these to a PhD paper

Pick P3 (scope-exclusion survey) + P5 (self-correction taxonomy) as two
empirical chapters, P1 as longitudinal measurement, P2+P4 as methods critique.
`papers/PAPER_DRAFT.md` scaffolds exactly that arc with falsifiable claims only.
