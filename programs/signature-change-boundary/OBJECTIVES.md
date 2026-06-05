# Objectives — signature-change-boundary

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

Scope guard (from README, binding on all routines): this is a fixed-background,
test-field program. Do **not** merge it into `co-emergence` or attach
self-consistency machinery to it. The four open points below come from the
seed note's own review section.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| SCB-1 | Odd-type profile restatement | Note restates the profile as λ ≃ −c·sgn(x⁰)·\|x⁰\|ⁿ and carries the two-sided (genuine signature-change) analysis through §§3–6 | Open | — |
| SCB-2 | No-log strengthening | Explicit statement in §5 that ν = 1/2 excludes logarithmic solutions for every n | Open | — |
| SCB-3 | Rigor labels | §§3–6 labeled Rigorous (given fixed background), §7 labeled Sketch, per project convention | Open | — |
| SCB-4 | Citation verification | The exploratory references (Ellis et al.; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) verified per METHODOLOGY citation discipline, or replaced | Open | — |
| SCB-5 | Port to index.tex | `index.tex` compiles with verified bibliography; note: adding it to the CI build matrix touches `.github/` (protected path) and therefore needs experimenter approval — flag in the PR | Open | — |

SCB-1 through SCB-4 should land before SCB-5 (port a corrected note, not a
draft).
