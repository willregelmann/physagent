#!/usr/bin/env bash
# Quality gate for the research-as-code workflow.
#
# Wired to the TeammateIdle and TaskCompleted hook events (see
# .claude/settings.json). It blocks a teammate from going idle, or a task from
# being marked complete, while there are uncommitted changes to tracked source
# files (papers, tooling, tests). METHODOLOGY.md asks that work happen in
# coherent commits; this enforces that a unit of work isn't "finished" with the
# derivation left unsaved in the working tree.
#
# NON-REPEATING BY DESIGN (added 2026-07-24, after an incident).
#
# The hook inspects the whole working tree, not the idling agent's own changes,
# because nothing available to it can attribute a dirty file to an agent. That
# is tolerable for a nudge and intolerable for a loop: on 2026-07-24 a
# report-only `generator` subagent — which by mandate edited nothing — was
# blocked repeatedly over another session's uncommitted files, could not
# satisfy the hook by any action within its mandate, escalated twice, and
# eventually committed work it had not authored in order to get unstuck. It
# reported honestly and its diligence was real; the failure was an
# unsatisfiable gate, not a badly behaved agent. See the EXPERIMENT.md log.
#
# The fix is not to weaken the check but to stop it repeating: the same dirty
# set blocks ONCE. If an agent is told to commit a set of files and that exact
# set is still dirty next time, blocking again communicates nothing new — the
# agent has already been told, and either cannot act (not its work) or has
# decided not to (not a coherent commit). Repeating only removes its ability to
# stop. A changed dirty set is new information and blocks again.
#
# Exit 0  -> allow (clean, not applicable, or already reported this exact set)
# Exit 2  -> block, with guidance on stderr
# Any other exit code is treated as a non-blocking error by Claude Code, so this
# script fails OPEN: internal errors never wedge the workflow.

set -u

# Claude Code passes hook context as JSON on stdin; we don't need it (we use the
# project dir env var), but consume it so the writer doesn't see a broken pipe.
cat >/dev/null 2>&1 || true

root="${CLAUDE_PROJECT_DIR:-$PWD}"
cd "$root" 2>/dev/null || exit 0

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Staged, unstaged, or untracked changes to tracked-source paths.
changed="$(
  git status --porcelain --untracked-files=all 2>/dev/null \
    | sed 's/^...//' \
    | grep -E '^(programs/.*\.tex$|tools/.*$|programs/.*/tests/.*\.py$)' \
    || true
)"

[ -n "$changed" ] || exit 0

# State lives under .git/, which is never committed and is per-clone. Keyed on
# the dirty set itself, so the block fires again the moment that set changes.
git_dir="$(git rev-parse --git-dir 2>/dev/null)" || exit 0
state="${git_dir}/require-clean-sources.last"

fingerprint="$(printf '%s' "$changed" | sort | cksum 2>/dev/null | tr -d ' \n')"
[ -n "$fingerprint" ] || exit 0   # fail open if cksum is unavailable

if [ -f "$state" ] && [ "$(cat "$state" 2>/dev/null)" = "$fingerprint" ]; then
  {
    echo "Note: uncommitted source changes are still present —"
    echo "$changed" | sed 's/^/  /'
    echo
    echo "Already reported for this exact set; not blocking again. If these are"
    echo "not yours to commit, say so and stop — that is the correct outcome."
  } >&2
  exit 0
fi

printf '%s' "$fingerprint" > "$state" 2>/dev/null || true

{
  echo "Blocked: uncommitted changes to tracked source files —"
  echo "$changed" | sed 's/^/  /'
  echo
  echo "Commit the work (one coherent step per commit, per METHODOLOGY.md)"
  echo "before going idle or marking this task complete."
  echo
  echo "If these files are NOT yours — another session's in-flight work, or"
  echo "changes you did not author — do not commit them. Say so and stop."
  echo "This check will not block you a second time on the same set."
} >&2
exit 2
