# Objectives — signature-change-boundary

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

Scope guard (from README, binding on all routines): this is a fixed-background,
test-field program. Do **not** merge it into `co-emergence` or attach
self-consistency machinery to it.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| SCB-1 | Odd-type profile restatement | Note restates the profile as λ ≃ −c·sgn(x⁰)·\|x⁰\|ⁿ and carries the two-sided (genuine signature-change) analysis through §§3–6 | Complete (PR #78, 2026-06-10) | #65 |
| SCB-2 | No-log strengthening | Explicit statement in §5 that ν = 1/2 excludes logarithmic solutions for every n | **Done** (PR #128, merged 2026-06-23; #120) | — |
| SCB-3 | Rigor labels | §§3–6 labeled Rigorous (given fixed background), §7 labeled Sketch, per project convention | **Done** (PR #128, merged 2026-06-23; #120) — but see SCB-4: §4/§8 subsequently reset Rigorous→Sketch by correction PR #147 (T2) | — |
| SCB-4 | Citation verification | The exploratory references (Ellis et al.; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) verified per METHODOLOGY citation discipline, or replaced; the note's "Relation to existing work" section flags any still-unverified reference inline | **Open — certification VOID and thread HALTED (T2, 2026-07-02).** PR #138's paper-grade content certification is void: red-team found reference [3] **Hayward 1992** cited as *supporting* the continuity-of-momentum (no-surface-layer) condition, when Hayward requires *vanishing* junction momentum and explicitly **rebutted** the Dray–Manogue–Tucker condition the note adopts. `needs-human` on #75 (experimenter-only to clear); correction PR **#147** (`agent-pr`+`demotion`) open and armed, also resetting §4 geodesic-continuation and §8 unification Rigorous→Sketch. **No SCB re-work proceeds until the experimenter clears #75; only #147 advances.** The SCB README "paper-grade verified" line is likewise falsified for [3] — its correction rides #147/responder, not this governance PR (the thread is halted; the governor edits only this row) | #75, #147 |
| SCB-5 | Port to index.tex | `index.tex` compiles with verified bibliography; note: adding it to the CI build matrix touches `.github/` (protected path) and therefore needs experimenter approval — flag in the PR | Open | — |
| SCB-6 | Expanding Lorentzian region | §§3–6 re-derived on ds² = λ(x⁰)(dx⁰)² + a²(x⁰)dx⃗² with prescribed smooth a(x⁰) > 0; each result labeled Rigorous-given-background or explicitly demoted with the obstruction stated; a→const limit recovers the existing note exactly | **Done** (PR #113, merged 2026-06-17; note `2026-06-17-expanding-region-note.md`; #63) — test-field crossing structure unconditionally robust; bulk geometry benign only if the proper expansion rate stays bounded at Σ, else Σ is a curvature singularity | #63 |

## Notes

SCB-2 through SCB-4 should land before SCB-5 (port a corrected note, not a
draft). SCB-2 and SCB-3 are below single-issue granularity individually and
may be combined into one issue. SCB-6 is ordered after SCB-2/3/4 and is
independent of SCB-5 (it produces a new note and touches no protected path).
Issue #63 already meets the agent-ready quality bar; it awaits only the label
(see the routine-gap note flagged to the experimenter in the 2026-06-11
governance synthesis).

**Cross-program priority (governor, 2026-07-05 monthly pass; supersedes the
2026-06-11 ordering, of which 5 of its top 9 slots — GGD-2, FPE-4, SCB-2/3,
SCB-6, FPE-1 — are now Done/void):** open milestones in priority order —
GGD-1 (in-flight, #136) > CE-13 (co-emergence anchor-language audit; contains
the confirmed L980 demotion) > FPE-5 (Schauder M6/M7) > FPE-7 (well-definedness
M8/M9) > GGD-3 (noise-kernel cross-check, needs #107) > CE-10 follow-ons >
CE-11, CE-12 (promoted 2026-06-21; scout to spec) > FPE-6 (Planck-boundary
retirement) > FPE-2 (assumption A3) > CE-5 (#45, in-flight) > CE-6..CE-9.
Halted/blocked, unranked: **this program's thread (`needs-human` #75 — only
correction PR #147 proceeds; SCB-4 certification void, T2)**; FPE-3 (blocked by
FPE-4); SCB-5 (experimenter-gated `.github/` edit).
`experimenter-priority` issues outrank all of it, per the worker routine.
Rationale: `explorations/governance/2026-07-05-monthly-record-integrity.md`.
