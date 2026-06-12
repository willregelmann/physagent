# Objectives — signature-change-boundary

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

Scope guard (from README, binding on all routines): this is a fixed-background,
test-field program. Do **not** merge it into `co-emergence` or attach
self-consistency machinery to it.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| SCB-1 | Odd-type profile restatement | Note restates the profile as λ ≃ −c·sgn(x⁰)·\|x⁰\|ⁿ and carries the two-sided (genuine signature-change) analysis through §§3–6 | Complete (PR #78, 2026-06-10) | #65 |
| SCB-2 | No-log strengthening | Explicit statement in §5 that ν = 1/2 excludes logarithmic solutions for every n | Open | — |
| SCB-3 | Rigor labels | §§3–6 labeled Rigorous (given fixed background), §7 labeled Sketch, per project convention | Open | — |
| SCB-4 | Citation verification | The exploratory references (Ellis et al.; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) verified per METHODOLOGY citation discipline, or replaced; the note's "Relation to existing work" section flags any still-unverified reference inline | Open | — |
| SCB-5 | Port to index.tex | `index.tex` compiles with verified bibliography; note: adding it to the CI build matrix touches `.github/` (protected path) and therefore needs experimenter approval — flag in the PR | Open | — |
| SCB-6 | Expanding Lorentzian region | §§3–6 re-derived on ds² = λ(x⁰)(dx⁰)² + a²(x⁰)dx⃗² with prescribed smooth a(x⁰) > 0; each result labeled Rigorous-given-background or explicitly demoted with the obstruction stated; a→const limit recovers the existing note exactly | Open | #63 |

## Notes

SCB-2 through SCB-4 should land before SCB-5 (port a corrected note, not a
draft). SCB-2 and SCB-3 are below single-issue granularity individually and
may be combined into one issue. SCB-6 is ordered after SCB-2/3/4 and is
independent of SCB-5 (it produces a new note and touches no protected path).
Issue #63 already meets the agent-ready quality bar; it awaits only the label
(see the routine-gap note flagged to the experimenter in the 2026-06-11
governance synthesis).

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
