# Autonomous routines

Definitions for the scheduled agents that run the autonomous research
experiment (`AUTONOMY.md`, `EXPERIMENT.md`). Each routine is registered as a
claude.ai scheduled agent whose prompt is a thin pointer; **behavior lives in
these files**, which are version-controlled and constitutionally protected.

## Registration

Register each routine with this pointer prompt (replace `<role>`):

> You are the `<role>` routine of the self-consistency autonomous research
> experiment. Read AUTONOMY.md at the repository root first, then read
> `automation/routines/<role>.md` and execute it exactly. If
> `automation/routines/<role>.md` does not exist on this branch, the
> experiment infrastructure has not landed yet — exit immediately without
> taking any action.

Source: this repository, branch `main`. Git identity / GitHub auth: the
machine account recorded in the repo variable `AUTONOMY_BOT`, supplied to the
runner as the `AUTONOMY_BOT_PAT` secret (see "Deployed instances" below).

> **Runner note (2026-06-09).** The routines were originally registered as
> claude.ai scheduled remote agents. That runner authenticates GitHub with the
> account's *global* connector — i.e. the experimenter's admin login — which
> voided the machine-account identity the whole authority model depends on
> (EXPERIMENT.md log). The routines now run as **GitHub Actions scheduled
> workflows** instead, which authenticate with a credential we control
> (`AUTONOMY_BOT_PAT`). The pointer prompt above is unchanged — it is what the
> reusable workflow feeds to a headless Claude Code session.

## Registry

| Routine | Cadence (UTC) | Model | File |
|---------|--------------|-------|------|
| worker | daily 06:00 | opus | `worker.md` |
| reviewer | 12h (05:00, 17:00) | opus | `reviewer.md` |
| responder | daily 04:00 | sonnet | `responder.md` |
| red-team | every 3 days 08:00 | opus | `red-team.md` |
| scout | weekly Mon 03:00 | sonnet | `scout.md` |
| librarian | weekly Tue 03:00 | sonnet | `librarian.md` |
| governor | monthly 1st 09:00 | opus | `governor.md` |

Cadence rationale: responder (04:00) runs before reviewer (05:00) runs before
worker (06:00) — fixes land, get re-reviewed, then new work starts against an
up-to-date queue.

## Deployed instances (GitHub Actions, 2026-06-09)

The routines run as **GitHub Actions scheduled workflows** in this repository.
Each role has a thin scheduled caller (`.github/workflows/autonomy-<role>.yml`)
that invokes the reusable runner (`.github/workflows/autonomy-routine.yml`) with
its role and model. This table is the record of the live deployment; if it
drifts from the workflow files, this file is wrong — fix it.

| Routine | Workflow file | Cron (UTC) | Model |
|---------|---------------|------------|-------|
| worker | `autonomy-worker.yml` | `0 6 * * *` | claude-opus-4-8 |
| reviewer | `autonomy-reviewer.yml` | `0 5,17 * * *` | claude-opus-4-8 |
| responder | `autonomy-responder.yml` | `0 4 * * *` | claude-sonnet-4-6 |
| red-team | `autonomy-red-team.yml` | `0 8 */3 * *` | claude-opus-4-8 |
| scout | `autonomy-scout.yml` | `0 3 * * 1` | claude-sonnet-4-6 |
| librarian | `autonomy-librarian.yml` | `0 3 * * 2` | claude-sonnet-4-6 |
| governor | `autonomy-governor.yml` | `0 9 1 * *` | claude-opus-4-8 |

Shared deployment configuration (all seven, in the reusable runner):

- **Runner:** `ubuntu-latest`; each run is a fresh checkout of this repo, a
  global `npm install -g @anthropic-ai/claude-code`, and one headless
  `claude -p "<pointer prompt>"` session. Stateless — every run reconstructs
  from GitHub, which suits ephemeral CI.
- **Prompt:** the pointer template above, built verbatim by the runner —
  behavior lives in the version-controlled `<role>.md` files, never in the
  workflow.
- **Model:** pinned full IDs (above), passed as `claude --model <id>`.
- **Permissions:** `--permission-mode bypassPermissions` (no human is present
  to approve tool calls in CI). The full Claude Code toolset is available; the
  reusable runner does not pass an `--allowedTools` allow-list.
- **Claude auth:** the `CLAUDE_CODE_OAUTH_TOKEN` repo secret (shared with the
  `semantic-review` gate).
- **GitHub identity:** the `AUTONOMY_BOT_PAT` repo secret (the machine
  account's PAT, `public_repo` scope, deliberately NO `workflow` scope). The
  runner uses it for every git/gh operation — NOT the default `GITHUB_TOKEN`,
  whose actor `github-actions[bot]` is neither the machine account nor the
  experimenter and whose PRs would not trigger the required checks. `checkout`
  runs with `persist-credentials: false` so the default token cannot shadow the
  PAT. A hard identity guard in the runner refuses to act unless the effective
  login equals `AUTONOMY_BOT` — the check whose absence caused the 2026-06-05
  incident.

### Kill switch

Step 1 of the kill switch is the repo variable **`AUTONOMY_ENABLED`**: the
reusable runner skips every routine unless it is exactly `true`. Set it to
`false` (or unset it) to halt the whole fleet in one action; individual roles
can also be disabled from the Actions tab. (The full kill switch — budget, PAT
revocation — is in `EXPERIMENT.md`.)

### Enablement runbook

1. Set the `AUTONOMY_BOT_PAT` secret to the machine account's PAT.
2. Merge these workflows to `main` (scheduled/dispatch workflows only run from
   the default branch). Protected-path PR → experimenter admin-merge.
3. Run `gh workflow run autonomy-identity-probe.yml` and confirm it is green
   (authenticates as `AUTONOMY_BOT`, write-not-admin).
4. Set `AUTONOMY_ENABLED=true` and record the start date in `EXPERIMENT.md`.

Note on red-team cadence: `0 8 */3 * *` is day-of-month based, so the
interval compresses at month boundaries (e.g. the 31st → the 1st). Harmless;
recorded so nobody "fixes" it into a bug report.

Note on scheduled-workflow caveats: Actions cron can be delayed under load, and
scheduled workflows auto-disable after 60 days of no repository activity (a
non-issue during an active run).

## Shared conventions

- **State lives on GitHub** (labels, assignment locks, marker comments,
  branches) — every run reconstructs from scratch; nothing is remembered
  between runs. See each file's "reconstruction preamble".
- **Marker comments** are HTML comments, found by prefix and edited in place:
  `<!-- quorum:verdict ... sha=... -->`, `<!-- quorum:stress-test ... sha=... -->`
  (reviewer only), `<!-- worker:attempts n=K -->`, `<!-- red-team:audit ... -->`.
  Verdict markers are only honored by the gate when authored by the machine
  account or the experimenter.
- **Labels** are the state machine — normative table in `AUTONOMY.md`.
- **No routine merges manually.** GitHub auto-merge + the required-check stack
  is the only merge path.
