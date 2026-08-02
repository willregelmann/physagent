#!/usr/bin/env python3
"""
tripwires.py — mechanical evaluation of the EXPERIMENT.md tripwires.

WHY THIS EXISTS. The pre-registration names T1–T5 as "the only in-run safety
net" (Known design risk #3). They were never mechanically evaluated. metrics.yml
says "the governor reads these files; tripwires T1-T5 are evaluated against
them" — and the governor is a routine, runs weekly, and dies in exactly the
failure modes the tripwires exist to catch. This was flagged on 2026-06-09 as
"deferred (minor): no automated tripwire evaluator" and was still the
load-bearing gap when the fleet went dark for eleven days behind green
dashboards in July 2026.

Every metric in EXPERIMENT.md is a ratio or distribution over *merged
artifacts*. When production goes to zero they do not alarm — they go stale. That
outage is why T6 exists: it is the only tripwire that fires on the absence of
work rather than on its content.

Deliberately reads GitHub directly rather than the metrics/ snapshots, so it
does not inherit the blind spot it is meant to catch.

Stdlib only, matching tools/verify_citations.py and tools/claim_graph.py.

Usage:
    python tools/tripwires.py                 # evaluate and report
    python tools/tripwires.py --json
    python tools/tripwires.py --exit-nonzero  # exit 1 if any tripwire fires
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys

# Read from the environment so this runs correctly in CI and from a clone
# without editing. The fallback is the repository this tool was written for.
REPO = os.environ.get("GITHUB_REPOSITORY") or "willregelmann/physagent"

# EXPERIMENT.md §Tripwires. T6 is not pre-registered; it was added after the
# 2026-07-14 outage, and is labelled as such wherever it is reported.
T1_MIN_RESULT_PRS = 20
T3_ACCEPT_RATE_MAX = 0.95
T3_WINDOW = 20
T4_DRIFT_MAX = 0.50
T4_WINDOW_DAYS = 28
T6_LIVENESS_HOURS = 48


def gh(*args: str, default=None):
    """Call gh and parse JSON. Returns `default` on any failure — this tool must
    never wedge the workflow, and a failed query is reported as UNKNOWN rather
    than silently treated as a passing tripwire."""
    try:
        out = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=120)
        if out.returncode != 0:
            return default
        return json.loads(out.stdout) if out.stdout.strip() else default
    except Exception:
        return default


def _now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _parse(ts: str) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except Exception:
        return None


class Result:
    def __init__(self, code, name, state, detail, data=None):
        self.code = code
        self.name = name
        self.state = state          # FIRED | ok | UNKNOWN | MANUAL
        self.detail = detail
        self.data = data or {}

    def as_dict(self):
        return {"code": self.code, "name": self.name, "state": self.state,
                "detail": self.detail, **({"data": self.data} if self.data else {})}


# ── T6: liveness ───────────────────────────────────────────────────
#
# Not pre-registered. Added because the fleet failed 51 consecutive runs over
# eleven days on a single cause and nothing noticed: metrics ran green (it does
# not touch the failing credential path), the digest ran green, and every other
# tripwire is a ratio over merged work, which goes stale rather than alarming
# when production stops.
#
# ORIGINALLY fleet-wide: FIRED only if *zero* autonomy-* runs succeeded
# anywhere in the window. Found insufficient on 2026-08-02: a bad MODEL_<ROLE>
# variable killed six of ten roles (worker/reviewer/red-team/governor/
# generator/adversary) for a week while responder/scout/librarian/steward —
# on no override, hence unaffected — kept succeeding on schedule. That alone
# was enough to hold the fleet-wide check at "ok" the entire time; nothing
# fired. Rewritten per-role: each role gets its own liveness window sized to
# its own registered cadence (see each autonomy-<role>.yml's cron and
# EXPERIMENT.md §Parameters), and T6 FIRES if any role that has actually
# attempted a run in its window has zero successes in it — a role that
# simply hasn't been scheduled yet within its own window is not evaluable,
# not a defect, and is not counted either way.

T6_ROLE_WINDOWS_HOURS = {
    "worker": 48,
    "reviewer": 48,
    "responder": 48,
    "generator": 48,
    "adversary": 48,
    "steward": 48,
    "red-team": 96,     # every 3 days
    "scout": 192,       # weekly
    "librarian": 192,   # weekly
    "governor": 192,    # weekly light pass; the workflow itself still fires weekly
    "explorer": 384,    # biweekly, self-gated to even ISO weeks
}
# Infrastructure, not research routines — excluded from per-role liveness.
T6_EXCLUDED_ROLES = {"event-dispatch", "identity-probe"}


def t6_liveness() -> Result:
    runs = gh("run", "list", "--repo", REPO, "--limit", "200",
              "--json", "name,conclusion,createdAt")
    if runs is None:
        return Result("T6", "routine liveness", "UNKNOWN",
                      "could not query workflow runs")
    routine = [r for r in runs
               if str(r.get("name", "")).startswith("autonomy-")
               and str(r.get("name", ""))[len("autonomy-"):] not in T6_EXCLUDED_ROLES]
    if not routine:
        return Result("T6", "routine liveness", "UNKNOWN",
                      "no autonomy-* runs in the queried window")

    by_role: dict[str, list] = {}
    for r in routine:
        role = str(r.get("name", ""))[len("autonomy-"):]
        by_role.setdefault(role, []).append(r)

    per_role_data = {}
    dead_roles = []
    for role, role_runs in by_role.items():
        window_hours = T6_ROLE_WINDOWS_HOURS.get(role, T6_LIVENESS_HOURS)
        cutoff = _now() - dt.timedelta(hours=window_hours)
        recent = [r for r in role_runs
                  if (_parse(r.get("createdAt", "")) or _now()) >= cutoff]
        ok = [r for r in recent if r.get("conclusion") == "success"]
        entry = {"window_hours": window_hours, "recent_runs": len(recent),
                  "successes": len(ok)}
        if recent and not ok:
            last_ok = next((r for r in role_runs if r.get("conclusion") == "success"), None)
            since = None
            if last_ok:
                t = _parse(last_ok.get("createdAt", ""))
                if t:
                    since = round((_now() - t).total_seconds() / 3600, 1)
            entry["hours_since_last_success"] = since
            dead_roles.append(role)
        per_role_data[role] = entry

    if dead_roles:
        detail = (
            f"{len(dead_roles)} role(s) attempted a run but had zero successes inside "
            f"their own liveness window: {', '.join(sorted(dead_roles))}"
        )
        return Result("T6", "routine liveness", "FIRED", detail, per_role_data)

    total_ok = sum(d["successes"] for d in per_role_data.values())
    evaluated = [role for role, d in per_role_data.items() if d["recent_runs"]]
    return Result(
        "T6", "routine liveness", "ok",
        f"{total_ok} successful run(s) across {len(evaluated)} role(s) with attempts "
        "in their respective liveness windows", per_role_data)


# ── T1: red team collapsed into approval ───────────────────────────

def t1_demotions() -> Result:
    prs = gh("pr", "list", "--repo", REPO, "--state", "merged", "--limit", "400",
             "--json", "number,labels")
    if prs is None:
        return Result("T1", "demotion machinery", "UNKNOWN", "could not query merged PRs")
    def has(pr, label):
        return any(l.get("name") == label for l in pr.get("labels", []))
    agent = [p for p in prs if has(p, "agent-pr")]
    corrections = [p for p in agent if has(p, "demotion") or has(p, "withdrawn")]
    if len(agent) < T1_MIN_RESULT_PRS:
        return Result("T1", "demotion machinery", "ok",
                      f"{len(agent)} merged agent PRs — below the {T1_MIN_RESULT_PRS} "
                      "threshold at which this tripwire becomes evaluable",
                      {"agent_prs": len(agent), "corrections": len(corrections)})
    if corrections:
        return Result("T1", "demotion machinery", "ok",
                      f"{len(corrections)} demotion/withdrawal PR(s) across "
                      f"{len(agent)} merged agent PRs",
                      {"agent_prs": len(agent), "corrections": len(corrections)})
    return Result("T1", "demotion machinery", "FIRED",
                  f"zero demotions or withdrawals across {len(agent)} merged agent PRs — "
                  "the red team has likely collapsed into approval",
                  {"agent_prs": len(agent), "corrections": 0})


# ── T3: sycophancy / rubber-stamp drift ────────────────────────────

VERDICT_RE = re.compile(r"<!--\s*quorum:verdict\s+(accept|revise|reject)\b")


def t3_accept_rate() -> Result:
    prs = gh("pr", "list", "--repo", REPO, "--state", "all", "--limit", "40",
             "--json", "number,labels")
    if prs is None:
        return Result("T3", "quorum accept rate", "UNKNOWN", "could not query PRs")
    agent = [p for p in prs
             if any(l.get("name") == "agent-pr" for l in p.get("labels", []))]
    verdicts: list[str] = []
    for pr in agent:
        if len(verdicts) >= T3_WINDOW:
            break
        comments = gh("api", f"repos/{REPO}/issues/{pr['number']}/comments",
                      "--jq", "[.[].body]", default=[])
        for body in comments or []:
            m = VERDICT_RE.search(str(body))
            if m:
                verdicts.append(m.group(1))
    if len(verdicts) < T3_WINDOW:
        return Result("T3", "quorum accept rate", "ok",
                      f"only {len(verdicts)} verdict(s) found — below the "
                      f"{T3_WINDOW}-verdict window at which this becomes evaluable",
                      {"verdicts": len(verdicts)})
    window = verdicts[:T3_WINDOW]
    rate = window.count("accept") / len(window)
    state = "FIRED" if rate > T3_ACCEPT_RATE_MAX else "ok"
    return Result("T3", "quorum accept rate", state,
                  f"accept rate {rate:.0%} over the trailing {len(window)} verdicts"
                  + (" — above the 95% sycophancy threshold" if state == "FIRED" else ""),
                  {"accept_rate": round(rate, 3), "window": len(window)})


# ── T5: instrumentation blindness ──────────────────────────────────

def t5_metrics() -> Result:
    runs = gh("run", "list", "--repo", REPO, "--workflow", "metrics.yml",
              "--limit", "6", "--json", "conclusion,createdAt")
    if runs is None:
        return Result("T5", "metrics instrumentation", "UNKNOWN",
                      "could not query metrics runs")
    if len(runs) < 2:
        return Result("T5", "metrics instrumentation", "ok",
                      f"only {len(runs)} metrics run(s) on record")
    last_two = [r.get("conclusion") for r in runs[:2]]
    if all(c != "success" for c in last_two):
        return Result("T5", "metrics instrumentation", "FIRED",
                      f"two consecutive metrics runs did not succeed: {last_two} — "
                      "the experiment must not run uninstrumented",
                      {"last_two": last_two})
    return Result("T5", "metrics instrumentation", "ok",
                  f"most recent metrics runs: {last_two}", {"last_two": last_two})


# ── T2, T4: not mechanically decidable here ────────────────────────

def t2_citations() -> Result:
    return Result(
        "T2", "citation integrity", "MANUAL",
        "Not mechanically decidable. verify-citations checks existence only, and "
        "claim-support is diff-scoped, so neither detects a real paper attached to "
        "a claim it does not support — the defect class that put `geroch` and "
        "`thm:exotic` on main from March to July 2026. Requires an adversarial "
        "content pass. Track via the claim graph's L6 lint, which flags "
        "load-bearing citations verified by abstract only, expired, or unrecorded.")


def t4_drift() -> Result:
    prs = gh("pr", "list", "--repo", REPO, "--state", "merged", "--limit", "200",
             "--json", "number,labels,mergedAt")
    if prs is None:
        return Result("T4", "topic drift", "UNKNOWN", "could not query merged PRs")
    cutoff = _now() - dt.timedelta(days=T4_WINDOW_DAYS)
    recent = [p for p in prs
              if (_parse(p.get("mergedAt") or "") or dt.datetime.min.replace(
                  tzinfo=dt.timezone.utc)) >= cutoff
              and any(l.get("name") == "agent-pr" for l in p.get("labels", []))]
    return Result(
        "T4", "topic drift", "MANUAL",
        f"{len(recent)} agent PRs merged in the trailing {T4_WINDOW_DAYS} days. "
        "Attributing each to an OBJECTIVES milestone requires reading PR bodies "
        "against milestone IDs and is not mechanised here. Note the redesign "
        "replaces OBJECTIVES-as-closure-conditions (see docs/CONSOLIDATION.md "
        "step 4), which will change what this tripwire should measure.",
        {"agent_prs_in_window": len(recent)})


ALL = [t6_liveness, t1_demotions, t3_accept_rate, t5_metrics, t2_citations, t4_drift]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Evaluate the EXPERIMENT.md tripwires.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--exit-nonzero", action="store_true",
                    help="exit 1 if any tripwire FIRED (for use as a gate)")
    args = ap.parse_args(argv)

    results = [fn() for fn in ALL]
    fired = [r for r in results if r.state == "FIRED"]
    unknown = [r for r in results if r.state == "UNKNOWN"]

    if args.json:
        print(json.dumps({"generated_at": _now().isoformat(),
                          "fired": [r.code for r in fired],
                          "results": [r.as_dict() for r in results]}, indent=2))
    else:
        for r in results:
            mark = {"FIRED": "FIRED ", "ok": "ok    ", "UNKNOWN": "UNKNOWN", "MANUAL": "manual"}[r.state]
            print(f"{mark} {r.code}  {r.name}")
            for line in (r.detail or "").split(". "):
                if line.strip():
                    print(f"         {line.strip().rstrip('.')}.")
        print()
        if fired:
            print(f"{len(fired)} tripwire(s) FIRED: {', '.join(r.code for r in fired)}")
            print("Per EXPERIMENT.md, a fired tripwire applies `needs-human` and halts the")
            print("affected thread. `needs-human` is a halt, not a suggestion, and only the")
            print("experimenter removes it. This tool does not apply labels — surfacing is")
            print("mechanical, halting is a decision.")
        else:
            print("No tripwires fired.")
        if unknown:
            print(f"{len(unknown)} could not be evaluated: {', '.join(r.code for r in unknown)}"
                  " — treat as unknown, not as passing.")

    return 1 if (args.exit_nonzero and fired) else 0


if __name__ == "__main__":
    sys.exit(main())
