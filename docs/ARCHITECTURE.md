# Architecture: an application whose runtime is GitHub

This repository is not code hosted on GitHub. It is an application **running
on** GitHub: GitHub Actions is its compute, the label system is its state
machine, issues and pull requests are its database, branch protection is its
authorization layer, and the merged repository tree is its production state.
The "users" of the application are seven autonomous agent routines and one
human experimenter; its workload is a theoretical-physics research program.

This document is descriptive, not normative. The normative documents keep
their own vocabulary: [`AUTONOMY.md`](../AUTONOMY.md) is the constitution
(policy), [`EXPERIMENT.md`](../EXPERIMENT.md) is the pre-registration
(spec + changelog + incident log), [`METHODOLOGY.md`](../METHODOLOGY.md) is
the schema for research content. Where this document and those disagree,
those win.

## The mapping

| Application concept | Implementation |
|---|---|
| Compute / runtime | GitHub Actions runners executing headless Claude Code sessions ([`autonomy-routine.yml`](../.github/workflows/autonomy-routine.yml)) |
| Processes | Seven routines — durable *roles* ([`automation/routines/`](../automation/routines/)), ephemeral *invocations* (one Actions run each) |
| Scheduler | cron triggers per role (`autonomy-<role>.yml`), with deliberate redundancy (reviewer double-fire) |
| Event bus | GitHub events: a quorum verdict comment dispatches the responder; an agent-PR push dispatches the reviewer ([`autonomy-event-dispatch.yml`](../.github/workflows/autonomy-event-dispatch.yml)). Cron remains the guaranteed backstop |
| State machine | The label system: `agent-ready` → claim (assignee lock) → `agent-pr` → per-SHA verdict → merged / `stuck` / `needs-human`. Transitions table in [`AUTONOMY.md`](../AUTONOMY.md) |
| Database | Issues, PRs, and the repository tree. Durable, queryable (`gh` is the query language), transactional (a merge is a commit, in both senses) |
| Schema | METHODOLOGY's rigor system: every result typed **Rigorous / Sketch / Conjecture**; demotions are migrations; withdrawn records are tombstones (never deleted) |
| Authorization | Branch protection (required checks, no direct pushes) + machine-account PAT scopes (write, not admin; no `workflow` scope) + the four-tier merge-gate stack |
| Service account | The machine account (repo variable `AUTONOMY_BOT`), asserted at runtime by an identity guard that refuses to act under any other login |
| Policy engine | The gate stack: deterministic tier (tests, paper builds, citation existence) → semantic tier (LLM claim-support evaluator) → quorum tier (adversarial verdict markers, per-SHA) → constitutional tier (retired 2026-07-12 to a no-op; gate-workflow files remain structurally protected by PAT scope, other protected paths no longer require approval) |
| Feature flag / kill switch | Repo variable `AUTONOMY_ENABLED`; one flip stops the fleet. Full kill-switch runbook in `EXPERIMENT.md` |
| Configuration | Repo variables (identity, switches) and secrets (PAT, model credentials, SMTP) |
| Observability | [Metrics dashboard issue](https://github.com/willregelmann/self-consistency/issues/67) (weekly snapshots → `metrics/`), [Breakthrough digest issue](https://github.com/willregelmann/self-consistency/issues/87) (weekly plain-English digest), Tier-A alert emails, Actions logs as traces |
| Release process | Workflow and constitution changes are deploys: experimenter-authored PRs, admin-merged, each recorded in the `EXPERIMENT.md` log |
| Incident log / postmortems | The same log — the 2026-06-05 identity halt, gate amendments, and instrumentation fixes are its entries |
| Integration test | The pre-registered terminal audit: fresh agents with no project context re-verify a sample of merged Rigorous results and every citation added during the run |

The deepest part of the mapping: **the research content is the application
state, and the methodology is its schema.** A rigor label is a type
annotation. A demotion PR is a schema-checked migration. The red team is a
fuzzer over production state. The audit is an integration test run against
production data by a clean client.

## Life of a contribution

The core request path, annotated with the GitHub primitive that implements
each step:

1. **Issue filed** (`agent-ready`) — by the scout from an OBJECTIVES
   milestone, the governor, or the experimenter (`experimenter-priority`
   jumps the queue). *Primitive: issue + label.*
2. **Claim** — the worker assigns the machine account before any work; a
   7-day-stale assignment is reclaimable. *Primitive: issue assignee as a
   lock.*
3. **Branch + PR** — `program/issue-N-description`, PR body carries the
   four self-checks and rigor labels, labeled `agent-pr`. *Primitive: branch,
   PR, label.*
4. **Deterministic tier** — pytest (×2), pdflatex per paper, citation
   existence against Crossref/arXiv. *Primitive: required status checks.*
5. **Semantic tier** — `claim-support`: an isolated LLM evaluator checks that
   load-bearing citations support the claims attached to them, diff-scoped so
   pre-existing defects of `main` warn rather than block. *Primitive:
   required check wrapping an LLM call.*
6. **Quorum tier** — the reviewer posts a machine-readable verdict marker
   bound to the head SHA (`accept` / `revise` / `reject`); a push voids it.
   Rigor promotions additionally require an independent stress-test marker.
   *Primitive: comment markers + a gate that parses them.*
7. **Revision loop** — a `revise` verdict event-dispatches the responder; its
   push event-dispatches the reviewer. Round-trip latency is minutes, with a
   ≥5-verdict circuit breaker that drops a long loop back to cron pace.
   *Primitive: `issue_comment` / `pull_request` events.*
8. **Merge** — GitHub auto-merge fires mechanically when all required checks
   pass. No agent and no human presses the button. *Primitive: auto-merge +
   branch protection.*
9. **Post-merge audit** — the red team prioritizes never-audited Rigorous
   results; its product is demotion PRs, which re-enter this same pipeline.
   *Primitive: the loop, applied to itself.*

## Identity and authority

Every agent operation authenticates as the machine account, whose PAT has
write access but not admin and deliberately lacks the `workflow` scope —
agents structurally cannot author changes to the gates that judge them. The
runner asserts the effective login at startup and refuses to act on mismatch
(the check whose absence caused the 2026-06-05 identity incident). The
experimenter holds the complementary powers: kill switch, budget, PAT
revocation, `needs-human` clearance, and the admin override that is the only
deploy path for gate workflows (protected-path approval more broadly was
retired 2026-07-12 — see `AUTONOMY.md` Amendment procedure). The event-dispatch
fast path holds no authority at all —
it presses, via the default workflow token, the same dispatch button the
scheduler presses.

## Designed-for failure modes

Observed failures and the mechanisms that absorb them — each of these has
actually fired at least once:

- **Dropped cron fires** (GitHub silently skips scheduled runs): reviewer
  double-fire, a responder watchdog that re-dispatches a missed review cycle,
  and the event-driven fast path, which removes the dependency on cron for
  the hot loop.
- **Model-budget exhaustion** (session limits kill a routine mid-run): the
  runner detects the limit message, sleeps through resets ≤90 minutes away
  and retries once, otherwise fails loudly and defers to the next fire.
- **Blind instrumentation** (metrics that "succeed" while reporting nothing):
  tripwire T5 halts the experiment if weekly metrics fail or go empty twice
  running; the 2026-06-12 label-count fix is the case study in why.
- **Reviewer-loop churn** (serial non-exhaustive revise rounds): the
  ≥5-verdict circuit breaker bounds the fast path; verdict-exhaustiveness
  discipline is a logged open amendment.
- **Runaway or compromised agents**: the gate stack is independent of agent
  cooperation (an unlabeled machine-account research PR *fails* rather than
  skips quorum), protected paths require human approval, and `needs-human` is
  a one-way halt only the experimenter clears.

## Watching it run

- **Live queue:** [open `agent-pr` PRs](https://github.com/willregelmann/self-consistency/pulls?q=is%3Apr+is%3Aopen+label%3Aagent-pr) and [`agent-ready` issues](https://github.com/willregelmann/self-consistency/issues?q=is%3Aissue+is%3Aopen+label%3Aagent-ready)
- **Vital signs:** [Metrics dashboard](https://github.com/willregelmann/self-consistency/issues/67) — demotion rate is the one to watch (a healthy adversarial system demotes)
- **Plain English:** [Breakthrough digest](https://github.com/willregelmann/self-consistency/issues/87), weekly
- **Traces:** the [Actions tab](https://github.com/willregelmann/self-consistency/actions) — every agent invocation is a public log
- **Changelog & incidents:** the log table in [`EXPERIMENT.md`](../EXPERIMENT.md)
