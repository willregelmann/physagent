# Objectives — co-emergence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits to this file happen only via `governance`-labeled PRs. The scout opens
issues only for milestones listed here; merged work is measured against these
milestones by the topic-drift metric.

Ordering reflects priority: prefer the checkable frontier (proofs, numerics)
over interpretive framework work.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| CE-10 | Signature → complex weight: derive the θ↔signature identification or document the obstruction | Either (a) a merged Sketch-level derivation that the complex self-consistency weight follows from hyperbolic (Lorentzian) temporal mode structure, with every remaining gap named and any residual support of the path-integral analogy stated explicitly; or (b) a merged documented obstruction stating precisely why temporal mode structure cannot induce a weight on the configuration space the fixed-point map acts on. In either case, a follow-up PR updates §3 framing and the abstract to state the derived-vs-stipulated status of the identification | Open — derivation landed; framing follow-up pending. PR #89 merged 2026-06-12 (exploration `explorations/2026-06-10-derived-weight-from-signature.md`; issue #81 closed): **outcome (a)**, a Sketch-level derivation that the complex weight ⟺ hyperbolic temporal mode structure, with a precisely localized polarization obstruction (gap (c)). The done-condition's second clause — the follow-up PR updating §3 framing and the abstract to the derived-up-to-polarization status — is **not yet done and not yet issued**; it is the remaining CE-10 work (the "CE-10 follow-ons" in the cross-program ordering), scout-specifiable now | #81 (closed) |
| CE-1 | Interference metric separating quantum from classical contributions | Metric defined; identically zero for Riemannian fixed points, nonzero for Lorentzian (θ≠0); validated in the N=4–16 toy model; merged into Section 3 | Done (PR #74, merged 2026-06-11) | #32 |
| CE-2 | Explain imaginary-fraction rank dependence (0.26 → 0.34) | Analytical expression or fitted functional form (e.g. a − b/rank^c) with mechanism; comparison against Haar-random baseline | Open | #33 |
| CE-3 | Distinct Einstein–Hilbert actions across smooth structures | Proof sketch that distinct exotic structures yield distinct S_EH, OR explicit counterexample, OR identification of the additional geometric data the framework needs | Open | #29 |
| CE-4 | Two-loop β_ξ: does the conformal fixed point shift? | Literature verdict (verified citations) plus structural argument; consequence for Conjecture 2 stated either way | Open | #30 |
| CE-5 | Machine-check the entropy-excess lemma chain (Lean4) | Green `lake build` proving purity decrease (all ranks) and rank-2 entropy excess; unproven dependencies explicit; paper annotated | Open | #45 |
| CE-6 | General-rank entropy excess | Proof under stated moderate-entry hypotheses, or sharp characterization of the failure region (counterexample exists at extreme entry ratios) | Open | — |
| CE-7 | Level 3 dynamics: Page–Wootters without fundamental Hilbert space | Convergence to unitary time evolution in the semiclassical limit at Sketch level; promotes co-emergence thesis Conjecture → Sketch | Open | — |
| CE-8 | Level 0 manifold class | A 4-manifold class admitting both Lorentzian metrics and rich exotic-structure theory, or a Rigorous negative classification | Open | — |
| CE-9 | Level 1 measure on Sm(M) | Proposed natural measure without metric input, with invariance properties stated; Conjecture level acceptable | Open | — |

## Notes

CE-10 was added on the experimenter's explicit nomination (issue #81, "Note
for the governor"); per the trailing-log rule adopted in the 2026-06-11
governance synthesis, milestones covering in-flight work require such a
nomination.

**CE-10 status (governor, 2026-06-14 weekly pass):** the derivation half of
CE-10 is complete — PR #89 merged the exploration and closed issue #81 with a
positive outcome (a). What remains for the milestone is the *designated
follow-up*: a paper-text PR updating §3 framing and the abstract to state the
identification as derived-up-to-polarization (exploration §7 item 1). That
follow-up is not yet filed as an issue; the scout should spec it against this
milestone (it sits in the cross-program ordering as "CE-10 follow-ons"). The
exploration's *other* follow-ups are deliberately **not** folded into CE-10:
the polarization-selection question (gap (c), §7 item 2) and k-sum robustness
(gap (b), §7 item 3) are new research directions, not part of CE-10's
done-condition, and would need the thread-proposal/debate channel before
becoming milestones. Exploration §7 item 5 (the cosmetic `m^{1+iθ}` →
`m^{1-iθ}` sign-label slip) already landed via #91 → PR #90.

**Cross-program priority (governor, 2026-06-11; information for the worker's
ranking criterion (a) and the scout's milestone selection):** this cycle's
order across programs is GGD-2 > FPE-4 > SCB-2/3 > SCB-4 > GGD-1 > FPE-5 >
CE-10 follow-ons > SCB-6 > FPE-1 > FPE-7 > FPE-6 > FPE-2 > CE-4..CE-9.
`experimenter-priority` issues outrank all of it, per the worker routine.
CE-4 (#30) and CE-5 (#45) already have issues (worker-claimable); CE-6 through
CE-9 are unissued (scout-fillable). SCB-5 (port to index.tex) requires a
`.github/` edit (protected path) and is excluded from the autonomous ordering;
it needs experimenter approval. Rationale:
`explorations/governance/2026-06-11-cycle-1-direction-debate.md`.

## Out of scope for autonomous work

- arXiv submission decisions (experimenter only).
- Merging this program with `signature-change-boundary` (explicitly forbidden
  by that program's README scope note).
