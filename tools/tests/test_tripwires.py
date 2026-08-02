"""
Tests for tools/tripwires.py, in particular T6 (routine liveness).

The T6 regression test below is not a hypothetical: on 2026-08-02 a bad
MODEL_<ROLE> variable killed six of ten autonomy routines for a week while
the other four (on no override) kept succeeding on schedule, and the
fleet-wide version of T6 never fired because *some* routine always
succeeded somewhere in the window. If this suite does not fail against the
old fleet-wide implementation, the regression test is not encoding the
actual defect.
"""

import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tripwires  # noqa: E402


REF_NOW = dt.datetime(2026, 8, 2, 12, 0, tzinfo=dt.timezone.utc)


def iso(hours_ago: float, ref: dt.datetime = REF_NOW) -> str:
    return (ref - dt.timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(name: str, conclusion: str, hours_ago: float) -> dict:
    return {"name": name, "conclusion": conclusion, "createdAt": iso(hours_ago)}


def patch_gh(monkeypatch, runs):
    """Stub tripwires.gh so t6_liveness sees a fixed `gh run list` response,
    regardless of the args it was called with."""
    monkeypatch.setattr(tripwires, "gh", lambda *a, **kw: runs)
    monkeypatch.setattr(tripwires, "_now", lambda: REF_NOW)


# ── T6: liveness ─────────────────────────────────────────────────────


def test_t6_ok_when_every_role_with_attempts_has_a_recent_success(monkeypatch):
    runs = [
        run("autonomy-worker", "success", 2),
        run("autonomy-worker", "failure", 26),
        run("autonomy-reviewer", "success", 1),
        run("autonomy-responder", "success", 3),
    ]
    patch_gh(monkeypatch, runs)
    result = tripwires.t6_liveness()
    assert result.state == "ok"


def test_t6_fires_on_a_partial_fleet_outage_the_old_fleet_wide_check_missed(monkeypatch):
    # worker/reviewer/red-team/governor/generator/adversary: every recent
    # attempt failed. responder/steward: succeeding on schedule throughout.
    # This is exactly the 2026-08-02 shape.
    runs = [
        run("autonomy-worker", "failure", 4),
        run("autonomy-worker", "failure", 28),
        run("autonomy-reviewer", "failure", 1),
        run("autonomy-reviewer", "failure", 12),
        run("autonomy-red-team", "failure", 20),
        run("autonomy-governor", "failure", 30),
        run("autonomy-generator", "failure", 5),
        run("autonomy-adversary", "failure", 6),
        run("autonomy-responder", "success", 3),
        run("autonomy-steward", "success", 2),
    ]
    patch_gh(monkeypatch, runs)
    result = tripwires.t6_liveness()
    assert result.state == "FIRED"
    dead = set(result.data.keys()) - {
        role for role, d in result.data.items() if d["successes"]
    }
    for role in ("worker", "reviewer", "red-team", "governor", "generator", "adversary"):
        assert role in dead, f"{role} should be reported dead, got {result.data}"
    for role in ("responder", "steward"):
        assert role not in dead


def test_t6_does_not_fault_a_role_with_no_attempts_in_its_own_window(monkeypatch):
    # explorer's window is 384h; a run 200h ago is well inside it and is its
    # only attempt on record, so it must not be counted as dead even though
    # it hasn't fired again since.
    runs = [
        run("autonomy-worker", "success", 2),
        run("autonomy-explorer", "success", 200),
    ]
    patch_gh(monkeypatch, runs)
    result = tripwires.t6_liveness()
    assert result.state == "ok"


def test_t6_excludes_infrastructure_workflows(monkeypatch):
    runs = [
        run("autonomy-event-dispatch", "failure", 1),
        run("autonomy-identity-probe", "failure", 1),
        run("autonomy-worker", "success", 2),
    ]
    patch_gh(monkeypatch, runs)
    result = tripwires.t6_liveness()
    assert result.state == "ok"
    assert "event-dispatch" not in result.data
    assert "identity-probe" not in result.data


def test_t6_unknown_when_query_fails(monkeypatch):
    monkeypatch.setattr(tripwires, "gh", lambda *a, **kw: None)
    result = tripwires.t6_liveness()
    assert result.state == "UNKNOWN"


def test_t6_unknown_when_no_autonomy_runs_at_all(monkeypatch):
    patch_gh(monkeypatch, [{"name": "tests", "conclusion": "success", "createdAt": iso(1)}])
    result = tripwires.t6_liveness()
    assert result.state == "UNKNOWN"
