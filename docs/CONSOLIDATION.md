# Consolidation: 10 routines → 5

**Live document.** Updated as steps land. Last updated 2026-07-25.

This tracks the migration from the routine set that grew by accretion to the
one the 2026-07-24 design review actually specified. It exists because the
review diagnosed accretion and then the very next change accreted: `generator`
and `adversary` were added without cutting anything, taking the count from
eight to ten against a design that called for five.

## Current state

| | |
|---|---|
| Routine definitions | **10** |
| With a scheduled caller | 8 → **10** once this PR merges |
| Actually running | **0** — fleet dark on Copilot quota since 2026-07-14 |
| Claims in graph | 29 (24 live, 5 dead) |
| Tier distribution | 17 rigorous, 7 sketch, **0 conjecture, 0 speculation** |
| Lint errors | 9 |

### The structural problem: two disjoint systems

Nothing in the original loop reads the claim graph, and nothing feeding the
original loop reaches the generative tier. They were built alongside each
other, not one replacing the other.

| Routine | reads claim graph | reads OBJECTIVES / issues |
|---|---|---|
| `generator`, `adversary` | **yes** | no |
| `worker`, `scout`, `governor`, `responder`, `explorer`, `librarian`, `red-team` | no | **yes** |
| `reviewer` | no | no (operates on PRs) |

This is the thing the consolidation has to fix. The routine count is a symptom.

## Target: the five

| Designed | Currently | Status |
|---|---|---|
| **generator** | `generator` | definition merged; caller in flight |
| **adversary** | `adversary` | definition merged; caller in flight. Must absorb `reviewer` + `red-team` |
| **prover** | `worker` | exists, but claims issues rather than reading the graph |
| **synthesist** | `explorer` | roughly maps; also issue-native |
| **steward** | — | **does not exist.** Why eleven dark days went unnoticed |

To retire: `responder` (a substrate artifact of the worker's context dying),
`scout` (a weekly stage starving a daily producer), `governor` (milestone
author for an objective function the redesign replaces), `librarian` (fold into
intake).

## Steps

### Step 1 — wire the generative tier · IN FLIGHT

Add `autonomy-generator.yml` and `autonomy-adversary.yml`. Both daily, paired
an hour apart (07:00 / 08:00 UTC) so nothing accumulates unadjudicated
overnight.

Cadence chosen rather than copied: the review found the old pipeline's defect
was slow upstream stages starving a daily producer — scout supplied ≤2
issues/week against 7 worker attempts/week, and idea-to-claimable ran 3–4
weeks across three weekly-or-slower hops. The generative tier must not become
the bottleneck it was built to remove.

*Unblocks:* nothing else can proceed until the conjecture tier has content.

### Step 2 — retarget `worker` → `prover` · BLOCKED on step 1

Select the highest-ranked live conjecture from the graph instead of claiming an
`agent-ready` issue. Ranking rule versioned in the repo (consequence ×
tractability × novelty).

*Blocked because:* the graph currently holds **zero conjectures**. A prover
picking the highest-ranked live conjecture has nothing to pick.

### Step 3 — fold `reviewer` and `red-team` into `adversary`; retire `responder`

Three routines currently do overlapping adversarial work. `responder` exists
only because the worker's context dies between runs — a substrate artifact,
not a role.

*Blocked because:* removing `reviewer` removes the quorum verdict the merge
gate requires. The gate has to learn about the graph first.

### Step 4 — replace OBJECTIVES-as-closure-conditions; retire `scout` and `governor`

Every milestone is currently a "done =" condition, so 100% of queued work is
gap-closing by construction. Needs a second milestone *type*: generative, with
done-conditions of the form "a falsifiable conjecture is stated, prior-art
checked, first step named."

*Blocked because:* cutting `scout` and `governor` removes the only thing
feeding the `worker` until step 2 lands.

### Step 5 — build `steward` · INDEPENDENT, can start any time

Liveness, quota headroom, failing-run triage, doc drift; dispatches blind
audits without performing them (a routine with full repo context cannot audit
blind). **This is also the T6 fix**, and it is the only step blocked by
nothing.

## What to watch

The consolidation stalls at step 2 if the conjecture tier stays empty. These
are the numbers that say whether it will:

| Metric | Now | Healthy |
|---|---|---|
| Conjectures live | 0 | growing |
| Kill rate (speculations killed / generated) | 5/5 | high, but **not** 100% indefinitely |
| Novel rate (fraction of new claims passing prior-art) | — | high; a low rate means rediscovery |
| Findings per cycle *not* from a surviving speculation | 6 | — |

That last row is the open question. Cycle 1 produced zero surviving
speculations and six real findings, all from the *investigation* each
provoked rather than from any speculation being right. If that holds, the
value model is "speculations are provocations that direct adversarial
attention," not "speculations are candidate truths" — which is close to the
opposite of what `generator.md` currently optimises for. **Not rewriting it on
one data point.**

## Cycle log

### Cycle 1 — 2026-07-24 (driven by hand)

5 speculations, 5 killed on attack, 0 survived steelman. Every death was
earned: two defense passes corrected their own prosecutors before still
convicting.

Findings produced, none from a speculation being right:

- `ce-self-consistency-real-spectrum` — Jacobian has real spectrum everywhere,
  so Neimark–Sacker bifurcation is structurally excluded for this map class
- `fpe-constant-h-rigidity` — the constant-H solution set is isolated and
  transverse; self-consistency is predictive, not merely satisfiable
- `fpe-fixed-point-is-inflationary` — the fixed point is Planck-adjacent, not
  the observed cosmological constant
- `ce-quantumness-not-one-dimensional` — O(N) vs O(N²); the two order
  parameters are genuinely independent
- Dimensional defect found in `fpe-starobinsky-coefficient`, a claim the audit
  had rated CONFIRMED
- `ce-riem-classical-unique` — uniqueness evidence, a Lefschetz index argument,
  and closure of the audit's open β=160 item

### Cycle 2 — 2026-07-25 (driven by hand)

Same mandate as cycle 1, deliberately, so it is a clean second sample. Both
generator and adversary ran on Opus 5.

**5 speculations, 5 killed. Zero survived as stated.** Same headline as cycle 1.
But the speculations were markedly more *computable* — four of five were settled
by calculation rather than argument — and the byproducts are correspondingly
sharper.

New claims produced:

- `ce-second-iterate-real-spectrum` — the second-iterate Jacobian has real
  spectrum everywhere by the same congruence mechanism as the first, and the
  mechanism provably **does not extend to k ≥ 3** (the S-factors would have to
  commute). This *explains* the observed period-2 cap rather than observing it:
  there was never a structural reason to expect Feigenbaum universality, because
  the algebraic protection that keeps the first doubling clean does not recur at
  the second.
- `ce-witness-obstruction` — no single-kernel pairwise witness can track I_S,
  because I_S depends on two independent degrees of freedom per entry while any
  such witness collapses to one. Supersedes the open question left by
  `ce-quantumness-not-one-dimensional` and explains two failed witnesses by one
  mechanism.
- `ce-euclidean-vacuum-at-fixed-point` — **the first live entry in the
  speculation tier.** S1's thesis with the vehicle replaced; gated on an
  independently fatal caveat.

Corrections to existing content, which is the recurring pattern:

- `ce-quantumness-not-one-dimensional`'s restricted result was **retracted as
  evidence** — it is a tautology of how θ\* is defined, and was recorded as a
  positive finding.
- `ce-riem-classical-unique` gained four corrections (β_flip = 0.648020 not
  ~0.698; the flip is supercritical; the β=40 spectrum belongs to the repelling
  fixed point; the period-2 zoo has zero bearing on uniqueness) and one
  failed-route record.
- A possible **direction inversion in the material-dependent-crossover
  conjecture**, surfaced but explicitly *not* certified — recorded on
  `ggd-cpmg-degeneracy` and wanting its own adversarial pass.

What the adversary did that matters more than the verdicts: **three of five
defense passes corrected their own prosecutors** before still convicting, and one
refuted the dispatching brief's central hypothesis. The S2 attack found that a
spectrum the brief cited as decisive belonged to the wrong object entirely.

### What two cycles say about the value model

| | Cycle 1 | Cycle 2 |
|---|---|---|
| Speculations | 5 | 5 |
| Survived as stated | 0 | 0 |
| Findings *not* from a surviving speculation | 6 | ~7 |
| Defects found in existing merged content | 1 | 3 |

**n = 2 on the pattern.** The value comes from the *investigation* each
speculation provokes, not from any being right. That is close to the opposite of
what `generator.md` currently optimises for (survival rate, not provocation), and
two cycles is enough to act on — a rewrite is now justified where it was not
after one.

The conjecture tier is still **empty**, which is what blocks consolidation step 2.
The speculation tier has its first live entry. Whether a generative cycle can
ever populate the conjecture tier — rather than only producing sketch-tier
byproducts and tombstones — remains the open question the redesign was built to
answer.
