---
description: "Run the explorer routine's fan-out/attack/steelman/synthesize cycle interactively"
arguments:
  - name: question
    description: "The question to explore (optional — if omitted, pick per explorer.md §1's source order)"
    required: false
---

You are running the `explorer` routine's full cycle interactively, on demand, rather than waiting for its biweekly cron (`automation/routines/explorer.md`). **That file is the single source of truth for the process** — read it now, in full, before doing anything else. This command is a thin interactive-mode wrapper around it: same fan-out width, same two-pass attack/steelman discipline, same scratch-tier mechanics, same three possible outputs — with two interactive-mode differences from a live cron run, both there to keep you (not a scheduled job) in the loop before anything becomes visible on GitHub:

1. **Pause before any GitHub-visible action** (opening the synthesis PR, filing a thread-proposal issue, opening a citation-correction PR) and confirm with the experimenter first, via `AskUserQuestion`, instead of firing automatically.
2. **Disclose interactive-mode provenance** in the synthesis file's closing process note, matching the convention already used in this repo's other same-session Explorations (e.g. `explorations/governance/2026-07-19-ggd-stationary-noise-vs-fpe-m3.md`).

Also read `METHODOLOGY.md` and `AUTONOMY.md` now if you haven't already this session — `explorer.md` assumes them as context.

## Step 1: Reconstruction preamble

Follow `explorer.md` §0 exactly: read every `programs/*/OBJECTIVES.md` and each program's `explorations/` directory (recent entries, watching for a named-but-unmilestoned gap); check the current `thread-proposal`/`informs-issue` inbox via `gh issue list` (remember the label-filtered query bug documented in `metrics.yml`'s own comments — fetch unfiltered with `--json labels` and filter in `jq`, don't trust `gh issue list --label X` under this token); check recent comments on the "Red-team log" tracking issue and recent scout/responder run comments for noted-but-unfiled candidate questions. If ≥3 `thread-proposal` issues are already open, stop and tell the user the inbox is stocked — don't manufacture a fourth.

## Step 2: Pick one question

If `$ARGUMENTS` names a specific question, use it — but still state explicitly which of `explorer.md` §1's source categories it falls under (or that the experimenter is overriding the source order directly, which is fine; `experimenter-priority` reasoning applies here by analogy even though this is an interactive command, not a label).

If `$ARGUMENTS` is empty, follow §1's preference order yourself: (a) a prerequisite an existing Exploration already named as blocking but which no milestone owns; (b) an `informs-issue` pointer opening a new direction; (c) a question noted by scout/red-team/responder per §0; (d) a cross-program tension visible only by reading multiple programs' records together. State which one you picked and why, in one paragraph, before proceeding — this is the moment to catch "this is really a milestone in disguise, that's scout's queue, not this command's" per §1's own warning.

## Step 3: Fan out (width 3, per §2 — do not widen it)

Create the scratch branch now (`scratch/explorer/YYYY-MM-DD-<topic-slug>`, off current `main`) — you'll commit into it as attempts/attacks/steelmans complete, not all at once at the end.

Dispatch **three** parallel fresh-context Agent-tool calls (`subagent_type: general-purpose`), each self-contained (they have none of this conversation's context — give each the question, the relevant file paths to read directly, and enough background that they don't need you). Each must commit to one **genuinely different technique or approach** — not three framings of the same idea — in the spirit of METHODOLOGY's Position-agent role: propose a specific structure, label every claim Rigorous/Sketch/Conjecture, honestly name what's underspecified, don't hedge toward a middle ground. Tell each attempt explicitly that it won't see its two siblings.

When choosing the three techniques, actively look for approaches that would catch different failure modes — e.g. one technique that directly re-derives from first principles, one that checks precedent/existing results for a direct match, one that stress-tests via an explicit worked estimate. Three variations on the same technique is not width 3 in the sense this step needs.

## Step 4: Attack, then steelman — per attempt, pipelined

Per `explorer.md` §3 and METHODOLOGY's "No Idea Is Eliminated Without a Defense": no attempt dies on one pass alone.

As soon as each individual attempt completes (don't wait for its siblings — pipeline this), dispatch that attempt's **attack pass**: a fresh-context agent whose only job is to find flaws (structural, axiom violations, dependence on something already known false or ruled out elsewhere in the repo). Critically — this is the specific instruction added to `explorer.md` after this routine's first live cycle found a shared blind spot across all three attempts — **if the attempt claims some structure or dependency "doesn't apply" or "doesn't exist," have the attack pass check that claim against the target paper's own disclosed assumptions/limitations list line by line, not just against its headline equations.** Give the attack pass the full attempt text and the relevant file paths; it does not render a survive/eliminate verdict.

Once an attempt's attack pass returns, dispatch that attempt's **steelman pass**: a second, independent fresh-context agent, given the attempt and the attack's specific flaws (not the attack's framing or conclusion) — its job is a genuine rescue attempt: is each flaw fatal, or a solvable gap, a narrower-but-viable restriction, or a framing problem? It must actually try, not rubber-stamp either side. If a real, load-bearing citation surfaces during either pass that changes the shape of the argument (as happened in the first live cycle — a citation one attack pass found materially undercut a premise two sibling attempts shared), verify it yourself directly before it goes further, the same way you would in any other exploration this session.

Do not wait for all three attempts before starting attack/steelman on the ones already done — the point of pipelining is that attempt 1's attack can run while attempt 3 is still being generated.

## Step 5: Record eliminations, keep survivors

An attempt is **eliminated** only if its steelman pass concludes the flaw is genuinely fatal — not repairable, not a narrower-but-viable version. For each elimination, append one entry to `programs/<name>/explorations/eliminated.md` (create if absent, append-only, on the scratch branch):

```
<!-- explorer:attempt outcome=eliminated date=YYYY-MM-DD topic="<question>" -->
Attempt: <one-line description>. Attacked: <the specific flaw>. Steelmanned: <what was
tried, and why it still failed>. Scratch record: <branch>@<commit-sha>.
```

A rescued attempt (even narrowed or restated) survives to Step 6 carrying its corrected, narrowed form — not its original unqualified claim.

Commit all attempt/attack/steelman content plus any `eliminated.md` entries to the scratch branch and push it. **This branch is never merged and never deleted** — it's the working-memory record; only the synthesis becomes a permanent, gated artifact.

## Step 6: Synthesize

If zero attempts survive: that's a complete, valid outcome per `explorer.md` §4. Skip to Step 7's "documented negative" path — do not force a synthesis out of three dead ends.

If at least one survives: write the synthesis yourself, in the interactive lead's voice (same pattern as this session's other same-day Explorations — you do not need to spawn a dedicated synthesis subagent for this if you already hold full context from orchestrating the passes above). Run it as METHODOLOGY's Synthesis-agent role does: adversarial critique across what survived, defense assessment, convergence, and an honest account of what remains underspecified. If two or more attempts' surviving claims appear to agree, explicitly check whether that agreement reflects genuine independent verification or a shared blind spot none of the attack passes caught — state which, with reasoning, don't just report the convergence at face value.

## Step 7: Produce exactly one output, after checking with the experimenter

Per `explorer.md` §4, the synthesis produces exactly one of:

- **A `thread-proposal` issue** — the default when a surviving finding identifies a real, falsifiable direction no milestone covers. Draft the full body (spec in `AUTONOMY.md` "Thread proposals": what was observed with references, why no milestone covers it, a falsifiable first step, declared relations) before asking.
- **A committed Exploration PR** (`programs/<name>/explorations/YYYY-MM-DD-<title>.md`, or `explorations/governance/` for cross-program findings) — when the synthesis itself is the deliverable (a documented negative that closes a direction, or a finding with no further action needed). Draft the full file before asking.
- **Nothing beyond the scratch-branch elimination record** — if zero attempts survived (Step 6).

If the synthesis surfaced a concrete, independent citation or textual defect in a paper (distinct from the main question — this happened in the routine's first live cycle) draft that as a separate small correction PR candidate too.

Before opening anything on GitHub, present your draft(s) to the user and ask via `AskUserQuestion` which of the drafted artifacts to actually open (issue / PR / both / neither), plus whether to open them yourself now or let the user review first. Do not push the synthesis file, open the issue, or open any correction PR until the user has confirmed — this is the one place this command deliberately runs slower than the scheduled cron would.

## Hard rules (same as `explorer.md`, restated for this interactive context)

- One question, three attempts, one synthesis-or-nothing per invocation of this command.
- Never label a scratch-branch attempt `agent-ready` or work it as a claimed issue.
- Never skip an elimination-ledger entry, including on a zero-survivor run.
- Never delete the scratch branch, a ledger entry, or a closed thread-proposal.
- Never edit `OBJECTIVES.md`, `METHODOLOGY.md`, `AUTONOMY.md`, `EXPERIMENT.md`, or another routine's definition file from this command — if the synthesis concludes one of these needs to change, say so and let the experimenter decide separately, same as any other Exploration this session.
