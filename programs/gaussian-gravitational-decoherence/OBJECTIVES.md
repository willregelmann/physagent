# Objectives — gaussian-gravitational-decoherence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| GGD-2 | Experimental discriminability | Updated predictions section quantifying how the Gaussian profile is distinguishable from Diósi–Penrose exponential decay — and from the dissipative-DP variant flagged in #92 — at currently proposed experimental sensitivities, recomputed against the corrected Table 1 platform parameters (errata PR #73), with verified citations to the experimental literature | **Done** (PR #105, merged 2026-06-15; issue #102 closed) — §5 gives the discriminant: max fractional-coherence difference 0.22 (BMV) / ≈0.18 (MAQRO), 3σ-resolvable with ~8000 shots, dDP subsection added, three verified experimental citations. (Row corrected from a stale "Open" in the 2026-07-05 monthly pass — a bookkeeping desync.) | #102 (closed) |
| GGD-1 | Material-dependence crossover | Quantitative threshold (acoustic-mode frequency vs. gravitational coherence frequency) for the Gaussian→exponential transition, with order-of-magnitude evaluation for at least two real materials; an outcome that no realistic platform reaches the crossover, with Conjecture 1 restricted or withdrawn accordingly, satisfies this milestone | Open — in flight (#136, assigned) | #92 (informs), #136 |
| GGD-3 | Independent noise-kernel cross-check | An independent linearized-gravity noise kernel (arXiv:2606.04099, `informs-issue` #107) is first shown *comparable in setup* to `eq:N0000_static`, then either reproduces the time-independent static kernel that yields the Gaussian t² exponent — hardening Result 2 (the Gaussian profile) beyond the framework's built-in Gaussian-noise Assumption 1 — or is shown to disagree under matched assumptions, a demotion signal for Result 2. **Precondition:** establishing kernel comparability is part of the done-condition; agreement/disagreement is signal only under a matched Newtonian/stationary setup. Sketch level acceptable | Open — added 2026-07-05 monthly pass (Position D; consumes librarian pointer #107) | #107 (informs) |

## Notes

This is the program with the most direct falsifiable-prediction content; GGD-2
is the experiment's primary "prediction with error bars" deliverable.

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
