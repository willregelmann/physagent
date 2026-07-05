# Objectives — fixed-point-existence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

Ordering reflects priority: repair milestones (FPE-4, FPE-5) precede extension
milestones, per the 2026-06-11 governance synthesis.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| FPE-4 | Repair the Banach contraction (demotion #72: M1, M3, M4, M5) | All four gaps closed and Lemma 1 + Theorem 2 re-promoted Sketch → Rigorous via a `promotion-rigorous` PR (verification + independent stress-test markers); OR a documented obstruction at Sketch level identifying which gap is structural, with the README and the co-emergence anchor language updated to permanently-Sketch or retired status. If a repair step founders on well-definedness of F, document and hand off to FPE-7 rather than patching silently | **Done — Outcome B** (PR #109, merged 2026-06-16; issue #103 closed): M3 documented as a **structural** obstruction (Lorentzian hyperbolic Green operator, causal-past support; any repair needs a global foliation beyond A1–A6 and is then foliation-restricted). Banach contraction stays permanently Sketch at the stated generality; README + co-emergence anchor language updated. Note the milestone closed by *documenting* the obstruction, not repairing it — the repair is structurally impossible without added foliation structure (→ FPE-7 shares the M3/M8 root) | #103 (closed) |
| FPE-5 | Repair the Schauder proof (M6, M7) | K_ρ redefined so it is closed and convex in the topology actually used, and a correct ρ-selection argument supplied, restoring Theorem 3 to "Conditional on A3 with no flagged proof gaps"; OR a documented obstruction showing the Schauder strategy fails for a stated structural reason | Open | — |
| FPE-1 | Massless case | Kernel bound (or alternative contraction argument) that does not require m > 0, at Sketch level or better; OR a documented obstruction explaining why the massless case genuinely differs. Note: issue #66's context block predates demotion #72 and cites the demoted kernel bound as Rigorous (under the older "Lemma 3" numbering); it must be read against the M3/M4 gap notes — see the corrective comment on #66 | **Done** (PR #101, merged 2026-06-14; exploration `2026-06-14-FPE1-massless-case.md`): Sketch obstruction — on a compact Σ the massless kernel is Hilbert–Schmidt with the mass scale replaced by the spectral gap λ₁(Σ) or ξR, so Theorem 2's m>0 is not sharp; the binding obstruction is the *shared* M3 hyperbolic→elliptic gap (FPE-1 downstream of FPE-4), not a massless-specific IR failure | #66 |
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

**Cross-program priority (governor, 2026-07-05 monthly pass; supersedes the
2026-06-11 ordering, of which 5 of its top 9 slots — GGD-2, FPE-4, SCB-2/3,
SCB-6, FPE-1 — are now Done/void):** open milestones in priority order —
GGD-1 (in-flight, #136) > CE-13 (co-emergence anchor-language audit; contains
the confirmed L980 demotion) > FPE-5 (Schauder M6/M7) > FPE-7 (well-definedness
M8/M9) > GGD-3 (noise-kernel cross-check, needs #107) > CE-10 follow-ons >
CE-11, CE-12 (promoted 2026-06-21; scout to spec) > FPE-6 (Planck-boundary
retirement) > FPE-2 (assumption A3) > CE-5 (#45, in-flight) > CE-6..CE-9.
Halted/blocked, unranked: the signature-change-boundary thread (`needs-human`
#75 — only correction PR #147 proceeds); FPE-3 (blocked by FPE-4); SCB-5
(experimenter-gated `.github/` edit); SCB-4 (certification void, T2).
`experimenter-priority` issues outrank all of it, per the worker routine.
Rationale: `explorations/governance/2026-07-05-monthly-record-integrity.md`.

Issue text for FPE-4 must carry the stress-test instruction from the
2026-06-11 synthesis (deliverable 3e): the Meda–Pinamonti–Siemssen precedent
lives on FLRW's homogeneous slicing; any M3 repair must state explicitly
whether its kernel control depends on that slicing — a repair valid only on a
preferred foliation must be labeled as such.
