# Weekly metrics snapshots land here (metrics.yml). See EXPERIMENT.md.

Snapshots are named YYYY-WW.json (ISO week).

## Proposed field: `quorum` (not yet wired — hardening proposal C5)

EXPERIMENT.md's health metric #6 ("Quorum behavior — accept/revise/reject
rates; mean review→merge latency") and tripwire T3 ("Quorum accept rate >95%
over trailing 20 verdicts") are currently only manually checkable — no
snapshot field surfaces them, so T3 cannot be evaluated mechanically. Proposed
schema addition, once wired into `metrics.yml`:

```json
"quorum": {
  "accept": 0,
  "revise": 0,
  "reject": 0,
  "accept_rate": 0.0,
  "window": "trailing 20 verdicts"
}
```

Computed by scanning `<!-- quorum:verdict ... -->` marker comments (see
AUTONOMY.md's merge-gate stack, tier 3) on the 20 most recent `agent-pr`
pull requests with a verdict, counting by outcome. `accept_rate` = accept /
(accept+revise+reject) over that window; T3 fires when it exceeds 0.95.

**This field is not yet computed** — doing so requires editing
`.github/workflows/metrics.yml`, a gate-workflow file outside what an
interactive session edits directly (see AGENTS.md's mode split; the machine
account's PAT structurally lacks the `workflow` scope for the same reason).
This section records the intended shape so whoever wires it in (the
experimenter, admin-merged, per the gate-workflow amendment path in
AUTONOMY.md) doesn't have to re-derive the schema from EXPERIMENT.md's prose.
