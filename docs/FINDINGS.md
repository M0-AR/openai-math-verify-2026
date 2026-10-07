# FINDINGS — What our live runs actually establish (Oct 7, 2026)

> Full logs: `benchmarks/results/summary.{json,md}` (regenerate via `make run`).

| # | Experiment | Result | Meaning |
|---|---|---|---|
| 01 | π(10⁶)=78,498 recomputed by sieve; Li(10⁶)≈78,628-scale | **PASS** | Video's "off by 130" footprint reproduced (modulo Li(2) baseline). θ=7/8 power-saving scale ≫ observed error → numerically consistent, necessary-not-sufficient for family 003. Classical 1896 region scale far larger → why 7/8 would be historic (first fixed-width strip). |
| 02 | Moser spindle (7 pts, 11 unit edges) not 3-colorable (2,187 cases) | **PASS** | Lower bound χ≥4 re-proved by exhaustion. Hex Ø0.9 tiling: same-color centers ≈2.38>1, max in-hex distance <1 over 200k samples → χ≤7 classical. Family 158 (χ≠5) correctly flagged UNPROVABLE by finite check; L1 Lean sentence identified for human reading. |
| 03 | μ(22/7)≈3.4, μ(355/113)≈3.2, later convergents →2 | **PASS** | Lucky-fraction table reproduced at 50 digits. Late scores cluster near 2 → consistent with μ(π)=2 (family 017). Flint–Hills S_5000 computed; spike at 355 (+24.6 scale) shown; series convergence honestly flagged OUTSIDE Lean scope. |
| 04 | Live GitHub audit of openai/math | **PASS/reported live** | Recounts families/manuscripts, Lean-mention coverage, formalization.yaml declarations, headline families 003/017/102/107/158 present; Hodge-032 paper-only confirmed. Counts drift as repo updates — rerun for current numbers. Offline → `live:false`. |
| 05 | Scope checklist L1/L2/L3 | **PASS** | Executable human-half protocol; permitted-axioms rule; per-claim reader jobs + scope edges (11/12 human-edited; Landau–Siegel c inexplicit; matmul arithmetic-only; UGC builds on PCP). |

## Verdict (independent, pre-referee)

- **Classical baselines: all reproduced.** Anyone can rerun in Docker.
- **OpenAI headline proofs: NOT re-proved here** — correctly routed to L1
  (rebuild Lean + read short Challenge), L2 (expert statement-match), L3
  (months of refereeing). No L3 claim is cited as verified.
- **Strongest near-term checkables:** 003 (7/8), 158 (≠5), 017 (μ=2),
  102 (UGC), 107 (ω≤9/4) — all with Lean artifacts; independent kernel
  rebuild (Lean + nanoda, 3 standard axioms) already reported by a third
  party for 003 within hours of release (unreviewed run, cited, not relied on).
