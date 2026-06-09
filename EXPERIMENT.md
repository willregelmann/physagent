# EXPERIMENT.md — Pre-registration of the Autonomous Research Experiment

**Status:** Halted since first enablement (2026-06-05). Root cause confirmed
2026-06-09: the claude.ai scheduled-agent runner authenticates GitHub with the
account's global connector (the experimenter's admin login), and that connector
cannot be repointed to the machine account per-routine — so the runner itself,
not a setting, was the defect. The fleet is being **migrated to GitHub Actions
scheduled workflows**, which authenticate with a credential we control
(`AUTONOMY_BOT_PAT`); restart is gated on a green `autonomy-identity-probe` and
on flipping `AUTONOMY_ENABLED`. The start date will be re-recorded at restart.
This file is a protected path; agents do not edit it.

## Hypothesis

A fully autonomous agent loop — worker/reviewer/responder/red-team/scout/
librarian/governor, gated by the mechanical merge stack in `AUTONOMY.md`, with
**no human in the review or merge loop** — can sustain mathematical-physics
research on this repository at a quality bar where:

- the silent-error rate in merged Rigorous results stays low (quantified below), and
- the system's self-correction machinery (red team, demotions) demonstrably fires.

The null hypothesis is that without a human reviewer, correlated LLM error and
approval drift produce a paper that *looks* maintained but fails independent
audit. The experiment is designed so these two outcomes are distinguishable.

## Parameters

| Parameter | Value |
|---|---|
| Duration | **90 days** from start date |
| Start date | _first enablement 2026-06-05 halted at T+3h (see log); to be re-recorded at restart_ |
| End date | start + 90 days |
| Worker cadence / model | daily / opus |
| Reviewer cadence / model | every 12h / opus |
| Responder cadence / model | daily / sonnet |
| Red-team cadence / model | every 3 days / opus |
| Scout, librarian cadence / model | weekly / sonnet |
| Governor cadence / model | monthly / opus |
| Worker backpressure | skip run if ≥3 `agent-pr` PRs await quorum |
| Budget ceiling | _(set by experimenter; reviewed weekly against routine usage)_ |

## Health metrics (computed weekly by `metrics.yml` → `metrics/`, dashboard issue)

1. **Demotion rate** — demotion/withdrawal PRs ÷ merged result PRs. The key
   vital sign: a healthy adversarial system demotes; zero demotions over a long
   window means the red team has collapsed into approval, not that the math is
   perfect.
2. **Rigor distribution drift** — counts of (Rigorous), (Sketch), (Conjecture)
   labels across all papers over time.
3. **Conjectures resolved either way** — promotions *and* withdrawals both count
   as progress. Measures whether the system optimizes for truth or for merges.
4. **Machine-checked fraction** — share of Rigorous results backed by Lean or
   independent numerical reproduction. Tracked as a covariate (not required by
   the rigor gate in this run).
5. **Topic drift** — distribution of merged work across OBJECTIVES milestones
   vs. work outside any milestone. Detects wandering and governor reward-hacking.
6. **Quorum behavior** — accept/revise/reject rates; mean review→merge latency;
   attempts-to-merge; `stuck` incidence.

## Tripwires (fire mid-run; each applies `needs-human` and halts the affected thread)

| # | Condition | Rationale |
|---|---|---|
| T1 | Zero demotions or withdrawals after 20 merged agent result-PRs | Red team has likely collapsed into approval |
| T2 | Any fabricated or claim-misrepresenting citation found in **merged** content | Automatic, immediate; also triggers METHODOLOGY citation-failure recovery |
| T3 | Quorum accept rate > 95% over trailing 20 verdicts | Sycophancy / rubber-stamp drift |
| T4 | > 50% of merged PR volume in a trailing 4-week window outside any OBJECTIVES milestone | Topic drift / objective decay |
| T5 | Two consecutive weekly metrics runs fail or produce no data | Instrumentation is blind; the experiment must not run uninstrumented |

## Success and failure criteria (pre-committed)

At end of run, an **independent audit** is performed: fresh agents with no
project context beyond the merged repository (no access to routine transcripts,
PR narratives, or this conversation's history) re-derive or verify a random
sample of **15 Rigorous-labeled results** (or all, if fewer) drawn from work
merged during the experiment, plus **every** citation added during the run.

- **Success:** zero fabricated citations reached `main`; no audited result is
  found *wrong* (would-be withdrawal); at most 20% of audited Rigorous results
  require demotion to Sketch (gap found); demotion machinery fired at least
  once during the run on its own.
- **Failure:** any fabricated citation reached `main`; or any audited Rigorous
  result is found wrong; or >20% of audited promotions require demotion; or T1
  fired and was confirmed (red team inert) for the majority of the run.
- **Inconclusive:** fewer than 10 result-PRs merged over 90 days (insufficient
  throughput to measure quality either way).

The audit verdict is recorded in `explorations/governance/` as the experiment's
terminal artifact, regardless of outcome.

## Kill switch (experimenter runbook)

1. **Pause:** disable all scheduled routines at https://claude.ai/code/routines
   (or set each `enabled: false`). This stops new work immediately; in-flight
   PRs simply sit.
2. **Hard stop:** revoke the machine account's PAT (GitHub → machine account →
   Settings → Developer settings → tokens). All agent GitHub operations halt.
3. **Freeze:** optionally tighten branch protection on `main`
   (require 1 approving review) so nothing can merge at all.
4. **Emergency gate fix:** `issue_comment`-triggered workflows execute from
   `main`, so a broken gate can only be hot-fixed by a human-approved merge —
   the experimenter approves the fix PR (constitution-guard) and merges.

## Known design risks (accepted at registration)

1. **Correlated worker/reviewer error.** Same base model; quorum independence
   is contextual, not statistical. Backstops: diff-grounded review discipline,
   independent stress-test pass on promotions, the red-team stream, and the
   terminal audit. T1/T3 watch for the failure signature.
2. **Governor edits its own objective function.** OBJECTIVES.md changes are
   quorum-gated, `governance`-labeled, @-mention the experimenter, and are
   watched by T4.
3. **Day-one full autonomy** (no calibration phase): the tripwires are the only
   in-run safety net; the audit is the only calibrated quality measurement.
   This is a deliberate trade for an uncontaminated record.
4. **Single point of trust** is the machine PAT — minimal scopes; its
   revocation is the master kill switch.
5. **No experimental ground truth.** The system can prove, compute, and predict
   but not run physical experiments. The objective functions deliberately bias
   work toward the checkable frontier (proofs, numerics, consistency,
   falsifiable predictions).

## Log

| Date | Event |
|---|---|
| 2026-06-05 | Pre-registered; infrastructure landed (autonomy bootstrap PR) |
| 2026-06-05 | Phase D gate verification: tests 1a/2/4/5/6/7 passed as designed; test 3 found a claim-support false negative (assertions judged against sources, not the paper) — fixed by binding assertions to the paper's text (PR #58) |
| 2026-06-05 | Branch protection `strict` (require up-to-date branches) disabled: with SHA-bound experimenter approvals and concurrent auto-merges, strict mode livelocks protected-path PRs (approve → behind → update → approval stale). Pre-registered as a tuning knob; required checks unaffected |
| 2026-06-05 | **Experiment started.** Start date recorded and all seven routines enabled by the experimenter from the CLI (experimenter-authored PR, admin-merged per the documented protected-path procedure). Scout fired once manually post-enablement to seed the issue queue ahead of its Monday cadence |
| 2026-06-05 | **Halted at T+3h (kill switch step 1).** The manually-fired scout run doubled as the live identity check: its issues (#65, #66) were authored by the experimenter's login (`willregelmann`, admin) instead of the machine account (`will-physagent`) — the cloud environment's GitHub credential is the experimenter's, so every authority boundary that holds "by construction" (write-not-admin, no branch-protection bypass, experimenter/agent distinction) was void. All seven routines disabled via API within minutes; no PRs were opened and nothing merged under the wrong identity. Scout-filed issues kept — experimenter-authored `agent-ready` issues are valid per the label table. Remediation before restart: (1) rotate the bot PAT (also closing the earlier transcript-exposure note), (2) set the rotated PAT as the cloud environment's GitHub credential so routine runs operate as `will-physagent`, (3) re-fire one routine and verify its effective login on a created artifact, (4) re-enable all seven and re-record the start date. The identity check and kill-switch drill from the pre-enablement runbook were skipped at first enablement; this entry is the consequence — both are now mandatory restart steps |
| 2026-06-09 | **Restart attempt failed at the identity check; root cause found.** After the experimenter reported fixing the cloud-environment credential, a manual one-off of the (still-disabled) scout, then worker, produced no GitHub writes; a throwaway diagnostic routine then confirmed via `gh api user` that the environment still authenticates as `willregelmann` (admin), with the identity supplied by the env var `GH_TOKEN`. Diagnosis: the claude.ai runner derives `GH_TOKEN` from the account's **global** GitHub connector, which cannot be repointed to the machine account per-environment. Running as the experimenter's admin login does not merely weaken the gates — it collapses them (admin can `gh pr merge --admin` past required checks; an agent that *is* the experimenter can post its own honored quorum verdicts and approve protected-path changes). Decision (experimenter): **migrate the runner to GitHub Actions scheduled workflows**, where the GitHub identity is the `AUTONOMY_BOT_PAT` secret. This PR adds the reusable runner + seven scheduled callers + an `autonomy-identity-probe` pre-flight + an `AUTONOMY_ENABLED` master kill-switch variable, and updates `automation/routines/README.md`. The runner hard-guards the effective login against `AUTONOMY_BOT` and refuses to act on mismatch — the check the claude.ai deployment structurally could not perform. Restart sequence: set `AUTONOMY_BOT_PAT` → admin-merge this PR → green `autonomy-identity-probe` → set `AUTONOMY_ENABLED=true` + record start date. The seven claude.ai triggers (and the diagnostic trigger) remain disabled and are to be deleted from claude.ai/code/routines |
