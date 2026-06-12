# Objectives — fixed-point-existence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

Ordering reflects priority: repair milestones (FPE-4, FPE-5) precede extension
milestones, per the 2026-06-11 governance synthesis.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| FPE-4 | Repair the Banach contraction (demotion #72: M1, M3, M4, M5) | All four gaps closed and Lemma 1 + Theorem 2 re-promoted Sketch → Rigorous via a `promotion-rigorous` PR (verification + independent stress-test markers); OR a documented obstruction at Sketch level identifying which gap is structural, with the README and the co-emergence anchor language updated to permanently-Sketch or retired status. If a repair step founders on well-definedness of F, document and hand off to FPE-7 rather than patching silently | Open | — |
| FPE-5 | Repair the Schauder proof (M6, M7) | K_ρ redefined so it is closed and convex in the topology actually used, and a correct ρ-selection argument supplied, restoring Theorem 3 to "Conditional on A3 with no flagged proof gaps"; OR a documented obstruction showing the Schauder strategy fails for a stated structural reason | Open | — |
| FPE-1 | Massless case | Kernel bound (or alternative contraction argument) that does not require m > 0, at Sketch level or better; OR a documented obstruction explaining why the massless case genuinely differs. Note: issue #66's context block predates demotion #72 and cites the demoted kernel bound as Rigorous (under the older "Lemma 3" numbering); it must be read against the M3/M4 gap notes — see the corrective comment on #66 | Open | #66 |
| FPE-7 | Well-definedness of F (M8, M9) | The function-space conflation (spacetime fixed point vs. data on a chosen Σ) and the state-selection prescription resolved at Sketch level, or a documented statement of what additional structure well-posedness requires; per demotion #72's suggested follow-up (2) | Open | — |
| FPE-6 | Disposition of the withdrawn Planck-boundary claim (M2) | Either a dimensionally consistent re-derivation of a validity boundary from a repaired κ chain (requires FPE-4's resolution of M1), at Sketch level or better; or a short permanent-retirement note in Section 7 making the withdrawn status final | Open | — |
| FPE-2 | Assumption A3 (uniform stress-energy bound) | A3 established for a nontrivial class of spacetimes, or a counterexample showing A3 can fail in-class. Promotion of Schauder existence from Conditional additionally requires FPE-5 (FPE-5 blocks the promotion clause only; A3 work itself is unblocked) | Open | — |
| FPE-3 | Stability of the Banach fixed point | (Re-scoped per PR #72.) Linearized stability analysis around the contraction fixed point, connecting to the Meda–Pinamonti linear-stability results; Sketch level | Blocked (by FPE-4: presupposes the demoted fixed point) | — |

## Notes

This paper is the Level 2 anchor for `co-emergence` — currently at Sketch
level following demotion #72; FPE-4/FPE-5 are the repair milestones and take
priority over extension milestones within this program. Changes that weaken a
result cited in co-emergence must comment on the affected co-emergence issues
(METHODOLOGY.md issue relations).

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

Issue text for FPE-4 must carry the stress-test instruction from the
2026-06-11 synthesis (deliverable 3e): the Meda–Pinamonti–Siemssen precedent
lives on FLRW's homogeneous slicing; any M3 repair must state explicitly
whether its kernel control depends on that slicing — a repair valid only on a
preferred foliation must be labeled as such.
