# Objectives — co-emergence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits to this file happen only via `governance`-labeled PRs. The scout opens
issues only for milestones listed here; merged work is measured against these
milestones by the topic-drift metric.

Ordering reflects priority: prefer the checkable frontier (proofs, numerics)
over interpretive framework work.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| CE-1 | Interference metric separating quantum from classical contributions | Metric defined; identically zero for Riemannian fixed points, nonzero for Lorentzian (θ≠0); validated in the N=4–16 toy model; merged into Section 3 | Open | #32 |
| CE-2 | Explain imaginary-fraction rank dependence (0.26 → 0.34) | Analytical expression or fitted functional form (e.g. a − b/rank^c) with mechanism; comparison against Haar-random baseline | Open | #33 |
| CE-3 | Distinct Einstein–Hilbert actions across smooth structures | Proof sketch that distinct exotic structures yield distinct S_EH, OR explicit counterexample, OR identification of the additional geometric data the framework needs | Open | #29 |
| CE-4 | Two-loop β_ξ: does the conformal fixed point shift? | Literature verdict (verified citations) plus structural argument; consequence for Conjecture 2 stated either way | Open | #30 |
| CE-5 | Machine-check the entropy-excess lemma chain (Lean4) | Green `lake build` proving purity decrease (all ranks) and rank-2 entropy excess; unproven dependencies explicit; paper annotated | Open | #45 |
| CE-6 | General-rank entropy excess | Proof under stated moderate-entry hypotheses, or sharp characterization of the failure region (counterexample exists at extreme entry ratios) | Open | — |
| CE-7 | Level 3 dynamics: Page–Wootters without fundamental Hilbert space | Convergence to unitary time evolution in the semiclassical limit at Sketch level; promotes co-emergence thesis Conjecture → Sketch | Open | — |
| CE-8 | Level 0 manifold class | A 4-manifold class admitting both Lorentzian metrics and rich exotic-structure theory, or a Rigorous negative classification | Open | — |
| CE-9 | Level 1 measure on Sm(M) | Proposed natural measure without metric input, with invariance properties stated; Conjecture level acceptable | Open | — |

## Out of scope for autonomous work

- arXiv submission decisions (experimenter only).
- Merging this program with `signature-change-boundary` (explicitly forbidden
  by that program's README scope note).
