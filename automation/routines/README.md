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
machine account recorded in the repo variable `AUTONOMY_BOT`. Create routines
**disabled**; enable only after the Phase D verification checklist passes (see
the bootstrap PR).

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

## Deployed instances (registered 2026-06-05)

The routines are deployed as claude.ai scheduled remote agents, managed at
<https://claude.ai/code/routines>. This table is the record of the live
deployment; if it drifts from what is actually registered, this file is wrong —
fix the file. Disabling these routines is **step 1 of the kill switch**
(`EXPERIMENT.md`).

| Routine | Trigger ID | Cron (UTC) | Model |
|---------|-----------|------------|-------|
| autonomy-worker | `trig_012ZLL1t2j7peNzGAadXymML` | `0 6 * * *` | claude-opus-4-8 |
| autonomy-reviewer | `trig_013PE7Dp6EFji5d9NefgAx4X` | `0 5,17 * * *` | claude-opus-4-8 |
| autonomy-responder | `trig_01PC2vVYcWUQ7qJQsb4Gf8MV` | `0 4 * * *` | claude-sonnet-4-6 |
| autonomy-red-team | `trig_01DFgXG9eZ37bPLVgtSGLq7x` | `0 8 */3 * *` | claude-opus-4-8 |
| autonomy-scout | `trig_013qHNtEy8nxjKdw8nfmiYFT` | `0 3 * * 1` | claude-sonnet-4-6 |
| autonomy-librarian | `trig_01F12Zj6gbcru4XycQRfg4Dq` | `0 3 * * 2` | claude-sonnet-4-6 |
| autonomy-governor | `trig_01FEAuqs6FbCKC6TEgCDhYPP` | `0 9 1 * *` | claude-opus-4-8 |

Shared deployment configuration (all seven):

- **Environment:** Anthropic cloud (`env_011CTQhm6jdCKJ3Tu9TnXTLe`); each run
  is a fully isolated remote session with a fresh checkout of this repo @ `main`.
- **Prompt:** the pointer template above, verbatim — behavior lives in the
  version-controlled `<role>.md` files, never in the registration.
- **Allowed tools:** `Bash, Read, Write, Edit, Glob, Grep, Task, WebSearch, WebFetch`.
- **MCP connections:** explicitly cleared (least privilege — no external
  connectors).
- **Created disabled**; enabled only after the Phase D gate verification in
  `EXPERIMENT.md` passed, with the experiment start date recorded there.
- **Identity:** runs authenticate to GitHub with the environment's credential.
  `quorum-gate` honors verdict markers only from the login in the
  `AUTONOMY_BOT` repo variable (`will-physagent`) or the experimenter — if a
  routine's effective login differs, fix the routine's auth or the variable,
  in that order of preference.

Note on red-team cadence: `0 8 */3 * *` is day-of-month based, so the
interval compresses at month boundaries (e.g. the 31st → the 1st). Harmless;
recorded so nobody "fixes" it into a bug report.

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
