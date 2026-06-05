# Autonomous routines

Definitions for the scheduled agents that run the autonomous research
experiment (`AUTONOMY.md`, `EXPERIMENT.md`). Each routine is registered as a
claude.ai scheduled agent whose prompt is a thin pointer; **behavior lives in
these files**, which are version-controlled and constitutionally protected.

## Registration

Register each routine with this pointer prompt (replace `<role>`):

> You are the `<role>` routine of the self-consistency autonomous research
> experiment. Read `automation/routines/<role>.md` in this repository and
> execute it exactly. Read `AUTONOMY.md` first.

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
