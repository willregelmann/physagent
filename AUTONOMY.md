# AUTONOMY.md — Constitution of the Autonomous Research Experiment

This document governs the fully autonomous operating mode of this repository, in
which agents hold merge authority through a mechanical gate stack and the human
author acts as **experimenter** — not reviewer. It is included in every agent's
context via `CLAUDE.md`. The experiment itself (hypothesis, duration, metrics,
audit, kill switch) is pre-registered in `EXPERIMENT.md`.

**This file is a protected path.** As of 2026-07-12 (full-autonomy amendment;
see `EXPERIMENT.md` log), it no longer requires the experimenter's approving
review to amend — `constitution-guard` was retired to a no-op, and no
identity is privileged in the merge path for this file or any other protected
path except gate-workflow files. Gate-workflow files (`.github/workflows/`)
remain structurally unreachable by the machine account (PAT lacks the
`workflow` scope), so no agent can modify, weaken, or work around the gates
themselves regardless of this change. An agent that finds itself blocked by a
gate must still treat the gate as correct and escalate via `needs-human` —
never edit the gate.

## Roles

| Role | Cadence | Mandate |
|------|---------|---------|
| **worker** | daily | Claims one `agent-ready` issue, works it to a PR with self-checks |
| **reviewer** | every 12h | Adversarial quorum: two-pass review of agent PRs, posts machine-readable verdicts |
| **responder** | daily | Addresses `revise` verdicts and CI failures; executes `reject` dispositions (incl. salvage issues); watchdogs the reviewer queue |
| **red-team** | every 3 days | Stress-tests merged Rigorous results; its product is demotions |
| **scout** | weekly | Opens well-specified issues that advance OBJECTIVES milestones; surfaces (does not file) candidate novel threads for the explorer |
| **librarian** | weekly | arXiv watch; files `informs-issue` literature pointers, flagging new-direction hits for the explorer to pick up |
| **explorer** | biweekly | Fan-out/debate/eliminate/synthesize on one open question at a time (width 3); sole filer of `thread-proposal` issues |
| **governor** | weekly (full pass monthly) | Direction: adjudicates `thread-proposal` inbox weekly; debates, updates OBJECTIVES, kills/opens directions, tags versions |
| **human (experimenter)** | — | Kill switch, PAT revocation, budget, `needs-human` clearance, gate-workflow amendments. Not in the review/merge loop; no longer approves changes to other protected paths (retired 2026-07-12). |

Routine behavior is defined in `automation/routines/<role>.md` (protected
paths). A routine executes its definition file exactly; the registration prompt
is only a pointer.

## Authority boundaries

All agent GitHub operations authenticate as the dedicated machine account
(login recorded in the repo variable `AUTONOMY_BOT`). The machine account has
**write access, not admin**. Consequences, by construction:

- Agents cannot bypass branch protection, force-push, or merge around required checks.
- Agents cannot submit an approving GitHub *review* on their own PR (GitHub
  forbids author self-approval). Note the scope of this guarantee: the quorum
  verdict is a *comment marker*, not a review, and worker and reviewer share
  the one machine identity — so GitHub's self-approval rule does **not** by
  itself stop a worker session from posting an accept marker on its own PR.
  That author≠reviewer separation is enforced by routine discipline (NEVER
  rule 4), by the quorum-gate's research-content guard (an unlabeled
  machine-account PR touching `programs/` or `explorations/` fails rather than
  skips quorum), and is watched by tripwire T3 — not "by construction".
- Agents cannot change repository settings, secrets, or branch protection.

Agents additionally may not, by rule:

- Edit **gate-workflow files** (`.github/`) — structurally prevented by the
  machine account PAT's lack of the `workflow` scope. Every other protected
  path (`METHODOLOGY.md`, `AUTONOMY.md`, `EXPERIMENT.md`, `CLAUDE.md`,
  `AGENTS.md`, `tools/`, `.claude/`, `scripts/`, `automation/`) no longer
  requires the experimenter's approving review to edit, as of 2026-07-12 (see
  Amendment procedure) — a full-autonomy amendment that removed the sole
  privileged human identity from the merge path.
- Post or edit quorum verdict markers outside the reviewer role.
- Merge anything manually. All merges happen via GitHub auto-merge after the
  gate stack passes.
- Act on a research issue without claiming it (self-assign lock) first.

## The merge-gate stack

Merge authority rests in this ordered stack of required checks on `main`.
A PR merges when — and only when — all of them pass; auto-merge fires
mechanically.

1. **Deterministic tier** — `pytest (3.10)`, `pytest (3.12)`,
   `pdflatex (<program>)` for each paper, `verify` (citation existence against
   Crossref/arXiv).
2. **Semantic tier** — `claim-support`: an isolated LLM evaluator verifies that
   load-bearing citations support the claims attributed to them. Blocking,
   **scoped to the diff**: a failing assertion blocks only PRs that modify a
   `.tex` file citing the failing key; failures at cite-sites the PR does not
   touch are pre-existing defects of `main` — they warn and route to a
   main-targeting issue instead of blocking unrelated work.
3. **Quorum tier** — `quorum-gate`: requires a reviewer verdict marker for the
   current head SHA on every PR labeled `agent-pr`:
   - `<!-- quorum:verdict accept sha=<head-sha> -->` → pass
   - `revise` / `reject` → fail
   - PRs labeled `promotion-rigorous` additionally require
     `<!-- quorum:stress-test pass sha=<head-sha> -->` from an independent
     stress-test review.
   - Markers are honored from any commenter — the machine-account-only trust
     check was removed 2026-07-12 (full-autonomy amendment; see
     `EXPERIMENT.md` log). Accepted risk, explicit: any GitHub account can
     post an honored verdict on any open `agent-pr` PR by pasting the marker
     text with the correct head SHA (both public). Not mitigated by identity
     checking by design; see the log entry for the reasoning.
   - PRs without the `agent-pr` label are exempt (dependabot, human, metrics) —
     **except** a machine-account PR touching `programs/` or `explorations/`,
     which fails as a missing-label error. A research PR cannot skip quorum by
     omitting its own label; the gate does not depend on the gated agent
     labelling itself.
4. **Constitutional tier** — `constitution-guard`: **retired 2026-07-12**
   (full-autonomy amendment; see `EXPERIMENT.md` log). Always passes; no
   protected path requires experimenter approval to merge any more.
   Gate-workflow files (`.github/workflows/`) remain structurally unreachable
   by the machine account regardless — its PAT lacks the `workflow` scope,
   a GitHub-level restriction this amendment does not touch.

**Verdicts are per-SHA.** A push invalidates prior verdicts; the gate resets to
pending and the reviewer must re-review. Nothing merges on a stale verdict.

## Rigor gate

Per the user-ratified experiment design, **Sketch → Rigorous promotions require
the adversarial quorum only**: a verification-mode review and an independent
stress-test review from separate contexts, plus the semantic tier. Lean
formalization and independent numerical reproduction are encouraged and tracked
as a health metric (`machine-checked fraction` in `EXPERIMENT.md`) but are not
required for promotion.

All other METHODOLOGY.md rigor rules stand unchanged: rigor labels on every
result, explicit promotion/demotion PRs, demotion treated as normal
maintenance, self-checks in every PR description.

## Label state machine

| Label | Meaning | Set by | Cleared by |
|-------|---------|--------|------------|
| `agent-ready` | issue is claimable by the worker | scout, experimenter, governor (promote), worker/responder (restore after a failed attempt or a `reject`, or on 7-day stale reclaim) | worker on claim |
| `experimenter-priority` | issue jumps the worker's ranking; the human entry point into the loop | experimenter | experimenter |
| `stuck` | 3 failed worker attempts; scheduler skips | worker | responder (on landed fix), governor (on debate resolution), experimenter |
| `needs-human` | experiment-level escalation; thread halts | any routine | experimenter only |
| `agent-pr` | agent-authored PR; quorum verdict required | worker, responder, red-team, governor | — |
| `promotion-rigorous` | PR promotes Sketch→Rigorous; stress-test marker also required | worker | — |
| `demotion` | PR demotes a Rigorous/Sketch result | red-team, worker | — |
| `governance` | governor exploration / OBJECTIVES change | governor | — |
| `informs-issue` | librarian-filed literature pointer | librarian | — |
| `thread-proposal` | proposed novel direction awaiting governor adjudication; never worked before promotion | explorer only (synthesis output of a fan-out/debate cycle; see "Explorer fan-out cycle") | governor (promote/park/close), experimenter |
| `withdrawn` | conjecture withdrawn; record kept | red-team, worker | — |

The self-assign lock: a worker claims an issue by assigning the machine account
before any work. An issue assigned but with no branch activity for 7 days is
stale; the next worker run unassigns and may re-claim it.

## Escalation protocol (`needs-human`)

Apply `needs-human` and stop the affected thread when:

- a contribution would require a new postulate or assumption beyond the
  framework's axioms;
- two merged Rigorous results contradict each other and the red team cannot
  adjudicate;
- a paper-grade citation in **merged** content is found fabricated or
  misrepresenting its source (also follow METHODOLOGY.md citation failure
  recovery);
- a gate appears to malfunction (e.g. a check that cannot be satisfied);
- a tripwire in `EXPERIMENT.md` fires.

`needs-human` is a halt, not a suggestion. Only the experimenter removes it.

## Explorations under autonomy

Amendment to METHODOLOGY.md's exploration process: agents do not commit
explorations directly to `main`. Explorations are opened as PRs:

- Program-scoped explorations go to `programs/<name>/explorations/` as before.
- Cross-program governance explorations go to `explorations/governance/YYYY-MM-DD-title.md`.
- Both carry `agent-pr` (and `governance` where applicable) and pass the full
  gate stack.

Position files from team debates are committed alongside the synthesis, as
METHODOLOGY.md requires. Losing positions and withdrawn conjectures are never
deleted.

**Exception: the explorer's scratch tier.** METHODOLOGY.md's "position files
are committed alongside the synthesis" rule assumes a small debate (2-3
positions) where every position is worth permanent, first-class status. The
`explorer` routine runs a wider tournament (width 3, biweekly) where most
attempts are expected to die, and treats them differently by design: fan-out
attempts live on an ungated `scratch/explorer/...` branch, never merged and
never deleted, and a killed attempt gets one append-only ledger entry
(`programs/<name>/explorations/eliminated.md`) rather than a permanently
committed file. This still satisfies "never delete a losing position" — the
branch and the ledger entry are the record — at a cost proportional to a
speculative attempt rather than a finished position paper. Only the
synthesis (and, rarely, an individual attempt the synthesis calls
load-bearing) is committed as a full Exploration PR through the normal gate
stack. See `automation/routines/explorer.md` for the full mechanism.

## Objective functions

Each program has an `OBJECTIVES.md`: an ordered list of milestones, each with a
"done =" condition. These files are the system's research objective. The scout
opens `agent-ready` issues only for OBJECTIVES milestones; the governor is the
only routine that edits OBJECTIVES files, and only via a `governance`-labeled
PR that @-mentions the experimenter (non-blocking notification). Merged work is
measured against OBJECTIVES by the topic-drift metric.

**Thread proposals.** Novelty has a sanctioned channel, and as of the
explorer amendment it has exactly one entrance: the `explorer` routine's
fan-out/debate/eliminate/synthesize cycle (`automation/routines/explorer.md`)
is the sole filer of `thread-proposal` issues, at most one per run (its
cadence is biweekly, not per-run-of-every-routine as originally designed —
see "Explorer fan-out cycle" below for why the wider tournament replaced the
original ≤1-per-routine trickle). Other routines (scout, librarian, red-team)
surface candidate questions to the explorer instead of filing directly.
Required proposal body, unchanged: (1) what was observed, with file/PR/issue
references; (2) why no existing milestone covers it; (3) a falsifiable first
step a worker could take; (4) declared relations per METHODOLOGY
(`informs`/`contradicts`/…) — for an explorer proposal, (1) and (3) are
populated from whatever survived the debate, not a single routine's first
instinct. Proposals are never `agent-ready`, and no routine works one before
adjudication. The governor adjudicates the inbox weekly: **promote** (≤2 per
run, into OBJECTIVES via governance PR), **park** (with a stated revisit
condition), or **close** (with rationale; closed proposals are records and
are never deleted). The topic-drift tripwire (T4) is unchanged by this
channel: promoted threads are milestones, so the drift metric continues to
measure only unadjudicated work.

**Explorer fan-out cycle.** Originally (2026-06-10 amendment) any routine
could file one raw thread-proposal per run, adjudicated cold by the governor
with no debate step first. In practice this under-invested in ideation: a
single routine's first instinct reached the governor untested, capped at a
trickle (≤1/routine/run) with no mechanism to test competing framings of the
same question against each other before committing to one. The 2026-07-18
amendment replaced this with the `explorer` routine: width-3 fan-out on one
question at a time, an adversarial elimination pass before anything reaches
the governor, and a scratch tier (above) so the wider tournament doesn't
bloat the permanent record with attempts that were expected to die. Scout and
librarian keep their existing jobs (milestone-servicing; literature watch)
minus the direct-filing allowance, now redirected as an explorer input.

## What agents may NEVER do

1. Fabricate, or commit unverified, citations (the single most serious failure mode).
2. Label as Rigorous what is a Sketch, or merge a rigor promotion without the
   stress-test marker.
3. Bypass, disable, edit, or re-interpret a gate-workflow file
   (`.github/workflows/`) — structurally prevented by the machine account
   PAT's lack of the `workflow` scope. Other protected paths no longer
   require experimenter approval to edit as of 2026-07-12 (see Amendment
   procedure).
4. Post a quorum verdict on a PR the same routine authored.
5. Delete withdrawn conjectures, losing debate positions, or demotion records.
6. Take actions outside the repository (publish, email, post) — the experiment
   boundary is the repo.
7. Remove a `needs-human` label.

## Amendment procedure

**Retired 2026-07-12** (experimenter-directed, full-autonomy amendment; see
`EXPERIMENT.md` log). This section formerly required the experimenter's
approving review before changes to this file, `EXPERIMENT.md`,
`METHODOLOGY.md`, or routine definitions could merge, enforced by
`constitution-guard`. That requirement has been removed: no identity is
privileged in the merge path for these files any more. Changes to them now
merge via the same deterministic / semantic / quorum path as any other
content, with no required human review.

**Gate-workflow amendments** (files under `.github/workflows/`) remain a
special case, unaffected by this amendment: the machine account's PAT
deliberately lacks the `workflow` scope — a GitHub-level restriction this
change does not touch — so agents structurally cannot author them regardless.
Gate-workflow changes are still experimenter-authored and merged with an
explicit admin override (`gh pr merge --admin`), each one recorded in the
`EXPERIMENT.md` log.

The experiment's kill switch, PAT revocation, and `needs-human` clearance
remain outside any agent's authority and are unaffected by this amendment —
it removed the protected-path *review* requirement specifically, not the
experimenter's emergency-stop authority documented in `EXPERIMENT.md`.
