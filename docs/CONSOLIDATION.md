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
| Routine definitions | **11** (steward added) |
| With a scheduled caller | **11** |
| Actually running | **0** — fleet dark on Copilot quota since 2026-07-14 |
| Claims in graph | 38 (28 live, 10 dead) |
| Tier distribution | 17 rigorous, 9 sketch, **2 conjecture**, 0 speculation |
| Novelty-unchecked claims | **0** — L5 is unconditional and the backlog is cleared |
| Lint errors | 9 (3×L4, 3×L6, 2×L10, 1×L11) |
| Cycles run | 2, both by hand |

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

*Unblocked 2026-07-25.* The graph now holds two live conjectures, so a prover
has something to pick. Note what they are, because it matters for what step 2
is actually testing:

- `ggd-material-crossover` — a conjecture that was **already in the paper**; the
  node records it rather than creating it.
- `ce-euclidean-vacuum-at-fixed-point` — the first claim to reach the conjecture
  tier **through the promotion gate**, which is the mechanism the redesign was
  built to test.

One of the two is a real answer to the open question; the other is bookkeeping.
Step 2 can proceed, but a sample of one is not yet evidence the generative tier
sustains a prover.

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

### Step 5 — build `steward` · DONE

Liveness, quota headroom, failing-run triage, doc drift; dispatches blind audits
without performing them (a routine with full repo context cannot audit blind).

**Landed:** `automation/routines/steward.md`, `autonomy-steward.yml` (daily
05:00 UTC, before generator and adversary), and `tools/tripwires.py` — which
fixes a deeper gap than T6 alone. The pre-registration calls T1–T5 "the only
in-run safety net", and they had never been mechanically evaluated: `metrics.yml`
delegated them to the governor, a routine that runs weekly and dies in exactly
the failure modes they exist to catch. Flagged as deferred on 2026-06-09 and
still the load-bearing gap when the fleet went dark for eleven days.

T1, T3, T5 and T6 are now computed directly from the GitHub API — deliberately
not from the `metrics/` snapshots, so the evaluator does not inherit the blind
spot it exists to catch. T2 and T4 report as requiring judgment rather than
silently passing.

First run against live state fired **T6** on the real outage, and produced a
number nobody had: **T3 accept rate is 55%** over the trailing 20 verdicts —
direct evidence the quorum was not rubber-stamping, which the day-45 audit could
not compute.

**Closed 2026-07-25.** `.github/workflows/tripwires.yml` runs the same evaluation
every six hours on the default `GITHUB_TOKEN` — no PAT, no Copilot licence, no
quota — so it cannot be taken down by anything that takes the fleet down. It
alerts by email on a fired tripwire and *also* fails the run, so GitHub's own
workflow-failure notification is a second alert path that works even with SMTP
unconfigured.

The steward routine still runs the same check and still goes down with the fleet;
that is now correct division of labour rather than a gap. The workflow is the
liveness signal, the routine is what acts on it.

**Correction, 2026-08-02:** the paragraph above is half right. The workflow
*is* the liveness signal, but "the routine is what acts on it" assumed the
routine could still read that signal by running the same check itself — and
it cannot. Steward's Copilot cloud-agent sandbox 403s on the Actions API
(issues/PRs/contents access only), confirmed on both 2026-08-01 and
2026-08-02 (issues #196, #197): every attempt to run `tools/tripwires.py`
inside the routine reports T1/T3/T5/T6 as `UNKNOWN`, correctly rather than
guessing, but that meant the routine had *no working path* to the mechanical
result at all, not degraded access to it. Compounding this, T6 itself was
fleet-wide (fired only if *zero* `autonomy-*` runs succeeded anywhere), so a
six-of-ten-role outage on 2026-08-02 (bad `MODEL_<ROLE>` variable) sat
undetected by both the routine (couldn't read the signal) and the tripwire
(wasn't scoped to notice a partial outage) for a week. Fixed same day: T6 is
now per-role (`tools/tripwires.py`), and `tripwires.yml` posts its JSON result
to a "Tripwire monitor" issue every six hours specifically so steward can read
it with the issues-scope access its sandbox does have, instead of re-running a
query it cannot make. `automation/routines/steward.md` §1 updated accordingly.
Division of labour is now: the workflow computes *and* publishes; the routine
reads the publication and decides whether to halt.

Step 5 is complete.

## What to watch

The consolidation stalls at step 2 if the conjecture tier stays empty. These
are the numbers that say whether it will:

| Metric | Now | Healthy |
|---|---|---|
| Conjectures live | **2** (1 promoted, 1 extracted) | growing |
| Reached conjecture *via the gate* | **1** | this is the number that matters |
| Kill rate (speculations killed / generated) | 10/10 killed as stated; 1 later revived by reframing | high, but **not** 100% indefinitely |
| Novel rate (fraction of claims passing prior-art) | 12 novel, 9 independent-rederivation, 0 unchecked | high; a low rate means rediscovery |
| Findings *not* from a surviving speculation | 6, then ~7 | — |
| Defects found in existing merged content, per cycle | 1, then 3, plus 4 from the novelty sweep | — |

**The pattern is now at n = 2 and is the main finding of both cycles.** Zero
speculations have survived, and thirteen substantive findings have come out
anyway — every one from the *investigation* a speculation provoked rather than
from any being right. Four of those were defects in already-merged content.

That means the value model is "speculations are provocations that direct
adversarial attention at load-bearing claims," not "speculations are candidate
truths." `generator.md` currently optimises for the second — it scores on
survival rate. **Two cycles is enough to justify rewriting it; one was not.** The
rewrite should target provocativeness: heavily-depended-on nodes, cross-program
edges, and claims already rated CONFIRMED.

The open question the redesign was built to answer now has its first data point.
**Can a generative cycle populate the conjecture tier?** Once, yes — and by a
route neither the design nor the two cycle logs anticipated. See "The first
promotion" below.

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

### Novelty sweep — 2026-07-25

Run after `NOVELTY_ENFORCED_FROM` was deleted and L5 made unconditional, clearing
the last four unchecked nodes. Every check was dispatched blind, in a separate
context, with no access to the claim's own prior conclusion.

| Claim | Verdict |
|---|---|
| `ce-witness-obstruction` | **novel** |
| `ce-euclidean-vacuum-at-fixed-point` | **novel** — cleared for promotion |
| `ce-second-iterate-real-spectrum` | split: algebra prior art, bifurcation consequence novel |
| `ggd-material-crossover` | split: crossover formula prior art (Kubo/Anderson), `m_*` novel |

Four defects in existing content, which is now the reliable yield of any pass:

1. **The crossover formula is textbook and the paper cites nothing for it.** The
   Anderson (1954) / Kubo (1954) / Kubo (1969) chain gives the exact relaxation
   function whose short- and long-time limits are the printed case structure.
   Citations owed; these predate arXiv and Crossref, so check them against
   `tools/verify_citations.py` before they enter the bibliography.
2. **A shallower novelty check missed strictly closer prior art.** The parent
   `ce-self-consistency-real-spectrum` was checked one day earlier and called
   Part A textbook, citing Golub and Van Loan. Garbe and Wei arXiv:2605.02314
   Theorem 1.6 gives the same characterization as a *biconditional* for
   arbitrary word length, and had been on arXiv since 4 May. Recorded on the
   parent as a correction.
3. **Published prior art may close a gap a claim self-flags as open.** Garbe and
   Wei's "only if" direction would supply an actual proof for the k ≥ 3
   breakdown that `ce-second-iterate-real-spectrum` currently supports by
   "generically" plus one numerical witness. Prior art as a *gift*, not a loss —
   worth a prover pass.
4. **`arXiv:1503.01826` is Siemssen's thesis**, not a standalone two-author
   preprint. The repository's bibliography key correctly cites the journal
   article; the exploratory reference was the loose one.

**The methodological finding is (2), and it generalises.** A novelty verdict is
an answer at a given search effort, not a durable fact. L5 prevents *unchecked*
claims; it cannot prevent *insufficiently* checked ones, and one day's gap was
enough to flip a verdict. Every `novelty.status` should be read together with its
`searched` date and the depth of the pass that produced it. This is a gap in the
lint set with no mechanical fix — a staleness lint (L6-style) could flag old
checks, but nothing can flag a shallow one.

### The first promotion

`ce-euclidean-vacuum-at-fixed-point` was promoted speculation → conjecture on
2026-07-25, the first claim to pass the gate rather than be extracted through it.

All five criteria were met, and the novelty check that gated it settled a
question two previous passes had left open — at full text, with an answer neither
anticipated. The strongest candidate prior art (Pinamonti–Siemssen) turns out to
be neither of the two structures previously guessed: a state *functional* is fixed
once and the contraction runs on a single variable, and the resulting states are
adiabatic order zero, explicitly **not** Hadamard or Bunch–Davies. Better still,
the extension is *structurally excluded* rather than merely unattempted — their
renormalization constants are chosen specifically to cancel the higher-derivative
anomaly term, which is the very mechanism driving the Starobinsky fixed point.

Two things about this promotion are worth stating plainly, because both cut
against the tidy version:

**The generator did not produce it.** The generator proposed a Sorkin–Johnston
version, which was killed outright. The *defense* pass constructed this reframing
while arguing against that death. The generative tier produced it through its
adversarial half, not its generative half — which is consistent with, and
sharpens, the n=2 finding that value comes from the investigation a speculation
provokes rather than from any being right.

**Promotion did not resolve the caveat.** Falsifier (ii) — the instability, a
lifetime of order 10⁻⁴² s — remains independently fatal to this as a claim about
physically realised backgrounds. Promotion records a well-formed conjecture worth
holding, not a description of anything realised. The conjecture tier is
explicitly a resting place, and a claim resting there indefinitely is the design
working, not a stalled promotion.
