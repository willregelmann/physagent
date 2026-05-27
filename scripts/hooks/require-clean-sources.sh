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
# Exit 0  -> allow (clean, or not applicable)
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

if [ -n "$changed" ]; then
  {
    echo "Blocked: uncommitted changes to tracked source files —"
    echo "$changed" | sed 's/^/  /'
    echo
    echo "Commit the work (one coherent step per commit, per METHODOLOGY.md)"
    echo "before going idle or marking this task complete."
  } >&2
  exit 2
fi

exit 0
