# Paper draft scaffold — from verification log to publishable paper

Target: a *methods + measurement* paper (not a claim of new theorems):
"Independent Verification of AI-Claimed Mathematics at Scale: A Reproducible
Protocol Applied to the October-2026 722-Manuscript Release".

## Proposed structure

1. **Introduction.** 722/372 release; why scale breaks normal refereeing;
   L1/L2/L3 trust model; our contribution: from-scratch Docker reproduction
   of all classical footprints + live catalog audit + scope-reading protocol.
2. **Background.** RH & zero-free regions (1896 → Vinogradov–Korobov →
   fixed-strip 7/8 gap); Hadwiger–Nelson 4–7 → de Grey 1581-pt → ≠5 claim;
   π irrationality (Mahler 42 → Salikhov 7.6 → 2) & Flint–Hills;
   UGC (2002), ω≤9/4, Hodge-CM; Lean + Comparator (3 axioms).
3. **Methods.** Zero-to-hero protocol (docs/METHODS.md); search triangulation
   (Exa→DDG→OpenResearch→arXiv→agent-reach→wiki, sequential, 429-backoff);
   reproducibility contract (no edit without run).
4. **Results.** FINDINGS table with receipts; live-audit counts with date;
   scope-exclusion table (extend P3 to all 162).
5. **Hidden patterns.** P1–P6 as falsifiable theses + next experiments.
6. **Threats to validity.** We did not rebuild Lean (kernel trust assumed);
   statement-match needs experts; counts drift; offline degradation.
7. **Related work.** ten-proofs / NavierStokesAndEuler / PrimeGaps186
   conditional formalizations; IAS AGMAI guidelines; third-party 003 rebuild.
8. **Conclusion.** Checking is the new hard part: machine half fast,
   human half slow — with a concrete crowdsourced path (question-file log).

## What remains for submission

- [ ] Rebuild ≥1 L1 Lean proof independently (`lake build` + Comparator +
      nanoda) and paste receipt.
- [ ] Extend scope-exclusion table to all formalized papers.
- [ ] Weekly reruns of exp 04 (longitudinal P1).
- [ ] Expert read of ≥1 short Challenge file (signed note).
- [ ] Citation pass + journal template.
