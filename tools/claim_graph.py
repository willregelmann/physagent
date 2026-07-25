#!/usr/bin/env python3
"""
claim_graph.py — the claim graph: loader, validator, and lint suite.

The repository's research state is a graph of *claims*. Each claim is a
Markdown file with YAML-subset frontmatter under `programs/<name>/claims/`.
Edges are typed: a claim depends on other claims, cites external sources, and
may be discharged by a formal (Lean) node.

This tool exists because the defects that actually reached `main` in this
project were *relational*, not arithmetic: a Rigorous claim leaning on a
Sketch one; a contraction proved for a different map on a different space; a
proof step valid only for real vectors asserted for complex ones; a citation
never re-examined after the day it was added. Every one of those is a graph
condition, so every one is mechanically checkable. That is the whole thesis.

What this tool cannot do: make a claim true. It makes *inconsistencies between
claims* visible and cheap to find. A wrong derivation with correct dependencies
passes every lint here, and that is what adversarial review is for.

Stdlib only, deliberately — matching tools/verify_citations.py, so CI needs no
dependency install.

Usage:
    python tools/claim_graph.py lint            # run all lints, non-zero on error
    python tools/claim_graph.py lint --warn     # include warnings in output
    python tools/claim_graph.py show <id>       # print one claim, resolved
    python tools/claim_graph.py query --tier rigorous --since 2026-06-09
    python tools/claim_graph.py coverage <id>   # mechanical coverage of closure
    python tools/claim_graph.py stats
"""

from __future__ import annotations

import argparse
import datetime as _dt
import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Tiers ──────────────────────────────────────────────────────────
#
# Two lifecycles share one ladder. Generative: speculation -> conjecture,
# gated on the conjecture criteria (falsifiable / novel / consequential /
# consistent / reachable). Verification: conjecture -> sketch -> rigorous,
# gated on proof. A claim resting at `conjecture` forever is a success, not a
# failure, and the demotion machinery does not touch that tier.

TIERS = ["speculation", "conjecture", "sketch", "rigorous"]
TIER_INDEX = {t: i for i, t in enumerate(TIERS)}
STATUSES = ["live", "dead", "superseded", "withdrawn"]
KINDS = ["informal", "formal"]
ROLES = ["load-bearing", "context"]
TRANSFERS = ["same-object", "cross-object"]
NOVELTY = ["unchecked", "novel", "prior-art", "independent-rederivation"]
VERIFIED_BY = ["full-text", "abstract", "none"]

# Mathlib's standard axioms. Anything else in a `#print axioms` audit means the
# formalization rests on something the reader did not agree to.
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}

CITATION_TTL_DAYS = 365



# ── Section 1: YAML-subset frontmatter parser ──────────────────────
#
# A deliberately small subset, parsed strictly. Anything the parser does not
# recognise raises rather than being silently dropped — a gate that quietly
# misreads its input is worse than no gate. Supported: nested maps, lists of
# scalars, lists of maps, inline flow lists/maps of scalars, folded (>) and
# literal (|) block scalars, and # comments.


class ParseError(Exception):
    pass


def _scalar(text: str):
    t = text.strip()
    if t.startswith("[") and t.endswith("]"):
        inner = t[1:-1].strip()
        return [_scalar(x) for x in _split_flow(inner)] if inner else []
    if t.startswith("{") and t.endswith("}"):
        inner = t[1:-1].strip()
        out = {}
        for part in _split_flow(inner):
            if ":" not in part:
                raise ParseError(f"flow map entry without ':': {part!r}")
            k, v = part.split(":", 1)
            out[k.strip()] = _scalar(v)
        return out
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
        return t[1:-1]
    low = t.lower()
    if low in ("null", "~", ""):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    return t


def _split_flow(text: str) -> list[str]:
    """Split a flow sequence on commas not nested inside brackets or quotes."""
    parts, buf, depth, quote = [], [], 0, None
    for ch in text:
        if quote:
            if ch == quote:
                quote = None
            buf.append(ch)
            continue
        if ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch in "[{":
            depth += 1
            buf.append(ch)
        elif ch in "]}":
            depth -= 1
            buf.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if "".join(buf).strip():
        parts.append("".join(buf).strip())
    return parts


class _Parser:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.i = 0

    def _cur(self):
        while self.i < len(self.lines):
            raw = self.lines[self.i]
            if not raw.strip() or raw.lstrip().startswith("#"):
                self.i += 1
                continue
            return len(raw) - len(raw.lstrip()), raw.strip()
        return None, None

    def _block_scalar(self, indent: int, fold: bool) -> str:
        out = []
        while self.i < len(self.lines):
            raw = self.lines[self.i]
            if raw.strip() and (len(raw) - len(raw.lstrip())) <= indent:
                break
            out.append(raw[indent + 2:] if len(raw) > indent + 2 else raw.strip())
            self.i += 1
        text = "\n".join(out).rstrip()
        if fold:
            paras = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text)]
            return "\n\n".join(p for p in paras if p)
        return text

    def parse_map(self, indent: int) -> dict:
        out: dict = {}
        while True:
            ind, line = self._cur()
            if line is None or ind < indent:
                return out
            if ind > indent:
                raise ParseError(f"unexpected indent at line {self.i + 1}: {line!r}")
            if line.startswith("- "):
                return out
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
            if not m:
                raise ParseError(f"line {self.i + 1} is not `key: value`: {line!r}")
            key, val = m.group(1), m.group(2)
            self.i += 1
            if val in (">", ">-", "|", "|-"):
                out[key] = self._block_scalar(indent, fold=val.startswith(">"))
            elif val == "":
                nind, nline = self._cur()
                if nline is not None and nind > indent:
                    out[key] = (
                        self.parse_list(nind) if nline.startswith("- ")
                        else self.parse_map(nind)
                    )
                else:
                    out[key] = None
            else:
                out[key] = _scalar(val)

    def parse_list(self, indent: int) -> list:
        out: list = []
        while True:
            ind, line = self._cur()
            if line is None or ind < indent or not line.startswith("- "):
                return out
            if ind > indent:
                raise ParseError(f"unexpected indent at line {self.i + 1}: {line!r}")
            rest = line[2:].strip()
            self.i += 1
            if rest in (">", ">-", "|", "|-"):
                # A bare block scalar as a list item: `- >` with the folded text
                # indented beneath it. Continuation sits at indent+2, aligned
                # under the "- ", same as a map value's block.
                out.append(self._block_scalar(indent, fold=rest.startswith(">")))
                continue
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", rest)
            if m and not rest.startswith(("[", "{")):
                item: dict = {}
                key, val = m.group(1), m.group(2)
                if val in (">", ">-", "|", "|-"):
                    item[key] = self._block_scalar(indent + 2, fold=val.startswith(">"))
                elif val == "":
                    nind, nline = self._cur()
                    if nline is not None and nind > indent + 2:
                        item[key] = (
                            self.parse_list(nind) if nline.startswith("- ")
                            else self.parse_map(nind)
                        )
                    else:
                        item[key] = None
                else:
                    item[key] = _scalar(val)
                nind, nline = self._cur()
                if nline is not None and nind > indent:
                    item.update(self.parse_map(nind))
                out.append(item)
            else:
                out.append(_scalar(rest))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a claim file into (frontmatter dict, body markdown)."""
    if not text.startswith("---"):
        raise ParseError("file does not begin with a `---` frontmatter fence")
    lines = text.split("\n")
    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break
    if end is None:
        raise ParseError("unterminated frontmatter fence")
    data = _Parser(lines[1:end]).parse_map(0)
    return data, "\n".join(lines[end + 1:]).strip()


# ── Section 2: Model ───────────────────────────────────────────────


class Claim:
    def __init__(self, data: dict, body: str, path: str):
        self.data = data
        self.body = body
        self.path = path
        self.rel = os.path.relpath(path, REPO_ROOT)

    def __getitem__(self, k):
        return self.data.get(k)

    @property
    def id(self) -> str:
        return self.data.get("id") or ""

    @property
    def tier(self) -> str:
        return self.data.get("tier") or ""

    @property
    def tier_index(self) -> int:
        return TIER_INDEX.get(self.tier, -1)

    @property
    def kind(self) -> str:
        return self.data.get("kind") or "informal"

    @property
    def status(self) -> str:
        return self.data.get("status") or ""

    @property
    def deps(self) -> list[dict]:
        return [d for d in (self.data.get("depends_on") or []) if isinstance(d, dict)]

    @property
    def load_bearing_deps(self) -> list[dict]:
        return [d for d in self.deps if d.get("role") == "load-bearing"]

    @property
    def cites(self) -> list[dict]:
        return [c for c in (self.data.get("cites") or []) if isinstance(c, dict)]

    @property
    def hypotheses(self) -> list[str]:
        return [h for h in (self.data.get("hypotheses") or []) if isinstance(h, str)]

    @property
    def internal_steps(self) -> list[dict]:
        return [s for s in (self.data.get("internal_steps") or []) if isinstance(s, dict)]

    @property
    def is_stub(self) -> bool:
        return self.data.get("extraction") == "stub"


class Graph:
    def __init__(self, claims: list[Claim]):
        self.claims = claims
        self.by_id: dict[str, Claim] = {}
        for c in claims:
            if c.id:
                self.by_id[c.id] = c

    @classmethod
    def load(cls, root: str = REPO_ROOT) -> tuple["Graph", list["Finding"]]:
        claims, findings = [], []
        pattern = os.path.join(root, "programs", "*", "claims", "*.md")
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf-8") as f:
                text = f.read()
            try:
                data, body = parse_frontmatter(text)
            except ParseError as e:
                findings.append(Finding("E000", "error", os.path.relpath(path, root),
                                        f"unparseable frontmatter: {e}"))
                continue
            claims.append(Claim(data, body, path))
        graph = cls(claims)
        # id must match filename, and be unique
        seen: dict[str, str] = {}
        for c in graph.claims:
            stem = os.path.splitext(os.path.basename(c.path))[0]
            if c.id != stem:
                findings.append(Finding("E001", "error", c.rel,
                                        f"id {c.id!r} does not match filename {stem!r}"))
            if c.id in seen:
                findings.append(Finding("E002", "error", c.rel,
                                        f"duplicate id {c.id!r} (also {seen[c.id]})"))
            seen[c.id] = c.rel
        return graph, findings

    def closure(self, claim_id: str, load_bearing_only: bool = True) -> set[str]:
        """Transitive dependency closure, following edges that carry weight."""
        seen, stack = set(), [claim_id]
        while stack:
            cid = stack.pop()
            c = self.by_id.get(cid)
            if not c:
                continue
            deps = c.load_bearing_deps if load_bearing_only else c.deps
            for d in deps:
                did = d.get("id")
                if did and did not in seen:
                    seen.add(did)
                    stack.append(did)
        return seen

    def dependents(self, claim_id: str) -> list[Claim]:
        """Everything that would be put in question by demoting `claim_id`."""
        return [c for c in self.claims
                if any(d.get("id") == claim_id for d in c.load_bearing_deps)]


class Finding:
    def __init__(self, code: str, severity: str, where: str, message: str):
        self.code = code
        self.severity = severity  # "error" | "warn"
        self.where = where
        self.message = message

    def __repr__(self):
        return f"{self.severity.upper():5s} {self.code}  {self.where}: {self.message}"

    def as_dict(self):
        return {"code": self.code, "severity": self.severity,
                "where": self.where, "message": self.message}


# ── Section 3: Schema validation ───────────────────────────────────

REQUIRED_ALWAYS = ["id", "program", "tier", "status", "statement"]
REQUIRED_AT_CONJECTURE = ["falsifier", "consequence", "novelty"]


def _norm_hyp(h: str) -> str:
    """Normalise a hypothesis for syntactic comparison. Deliberately crude —
    these fields are free text pretending to be machine-comparable, so the
    comparison ships as a warning, never a merge block."""
    return re.sub(r"[^a-z0-9]+", "", h.lower())


def validate_schema(graph: Graph) -> list[Finding]:
    out: list[Finding] = []

    def err(c, code, msg):
        out.append(Finding(code, "error", c.rel, msg))

    for c in graph.claims:
        for field in REQUIRED_ALWAYS:
            if not c.data.get(field):
                err(c, "E010", f"missing required field {field!r}")
        if c.tier and c.tier not in TIER_INDEX:
            err(c, "E011", f"unknown tier {c.tier!r} (expected one of {TIERS})")
        if c.status and c.status not in STATUSES:
            err(c, "E012", f"unknown status {c.status!r}")
        if c.kind not in KINDS:
            err(c, "E013", f"unknown kind {c.kind!r}")

        if c.tier_index >= TIER_INDEX["conjecture"] and c.status == "live":
            for field in REQUIRED_AT_CONJECTURE:
                if not c.data.get(field):
                    err(c, "E014",
                        f"tier {c.tier!r} requires {field!r} "
                        "(the conjecture gate: falsifiable / novel / consequential)")

        for d in c.deps:
            if not d.get("id"):
                err(c, "E015", "depends_on entry without an id")
            elif d["id"] not in graph.by_id:
                err(c, "E016", f"depends_on unknown claim {d['id']!r}")
            if d.get("role") not in ROLES:
                err(c, "E017",
                    f"depends_on {d.get('id')!r}: role must be one of {ROLES}")
            if d.get("transfers") and d["transfers"] not in TRANSFERS:
                err(c, "E018",
                    f"depends_on {d.get('id')!r}: transfers must be one of {TRANSFERS}")

        for ct in c.cites:
            if not ct.get("key"):
                err(c, "E019", "cites entry without a key")
            v = ct.get("verified")
            if isinstance(v, dict) and v.get("by") and v["by"] not in VERIFIED_BY:
                err(c, "E020",
                    f"cites {ct.get('key')!r}: verified.by must be one of {VERIFIED_BY}")

        nov = c.data.get("novelty")
        if isinstance(nov, dict) and nov.get("status") not in NOVELTY + [None]:
            err(c, "E021", f"novelty.status must be one of {NOVELTY}")

        if c.kind == "formal" and not isinstance(c.data.get("formal"), dict):
            err(c, "E022", "kind: formal requires a `formal:` block")

    return out


# ── Section 4: Lints ───────────────────────────────────────────────
#
# Each lint below traces to a defect that actually reached `main` in this
# repository. The mapping is recorded in tools/claim_graph.md and exercised as
# regression fixtures in tools/tests/test_claim_graph.py.


def _today() -> _dt.date:
    return _dt.date.today()


def _as_date(v) -> _dt.date | None:
    if not v:
        return None
    try:
        return _dt.date.fromisoformat(str(v).strip())
    except ValueError:
        return None


def lint_L1_tier_inversion(g: Graph) -> list[Finding]:
    """A load-bearing dependency at a lower tier than the claim it supports.

    Origin: prop:riem_classical asserted Rigorous uniqueness on the strength of
    a Banach contraction that is permanently Sketch (milestone CE-13)."""
    out = []
    for c in g.claims:
        if c.status != "live" or c.tier_index < 0:
            continue
        for d in c.load_bearing_deps:
            dep = g.by_id.get(d.get("id", ""))
            if dep and 0 <= dep.tier_index < c.tier_index:
                out.append(Finding(
                    "L1", "error", c.rel,
                    f"tier inversion: {c.tier} claim rests on {dep.tier} claim "
                    f"{dep.id!r} via a load-bearing edge"))
    return out


def lint_L2_cross_object(g: Graph) -> list[Finding]:
    """A load-bearing dependency on a claim about a different object or space,
    with no written justification for the transfer.

    Origin: the same CE-13 defect — the companion contraction is about a
    field-theoretic map on manifolds, not the finite map F on C^N."""
    out = []
    for c in g.claims:
        if c.status != "live":
            continue
        for d in c.load_bearing_deps:
            dep = g.by_id.get(d.get("id", ""))
            declared = d.get("transfers")
            if declared == "cross-object" and not d.get("justification"):
                out.append(Finding(
                    "L2", "error", c.rel,
                    f"cross-object transfer to {d.get('id')!r} with no justification"))
            elif dep and declared == "same-object":
                a, b = c.data.get("object") or {}, dep.data.get("object") or {}
                if isinstance(a, dict) and isinstance(b, dict) and a and b:
                    if (a.get("name") != b.get("name")) or (a.get("space") != b.get("space")):
                        out.append(Finding(
                            "L2", "error", c.rel,
                            f"declared same-object transfer to {dep.id!r}, but objects "
                            f"differ: {a.get('name')}/{a.get('space')} vs "
                            f"{b.get('name')}/{b.get('space')}"))
    return out


def lint_L3_hypothesis_escape(g: Graph) -> list[Finding]:
    """A dependency requires a hypothesis its dependent never states.

    Warning, not error: `hypotheses` is free text and the comparison is
    syntactic."""
    out = []
    for c in g.claims:
        if c.status != "live" or not c.hypotheses:
            continue
        mine = {_norm_hyp(h) for h in c.hypotheses}
        for d in c.load_bearing_deps:
            dep = g.by_id.get(d.get("id", ""))
            if not dep:
                continue
            for h in dep.hypotheses:
                if _norm_hyp(h) not in mine:
                    out.append(Finding(
                        "L3", "warn", c.rel,
                        f"dependency {dep.id!r} requires hypothesis {h!r}, "
                        f"not stated by this claim"))
    return out


def lint_L4_step_escape(g: Graph) -> list[Finding]:
    """An internal proof step invoking hypotheses narrower than the claim's,
    with no justification for using it at the claim's full generality.

    Origin: prop:interference_metric asserted
    x^dag (rho + rho^T) x = 2 Re(x^dag rho x), which holds only for real x,
    while the surrounding claim quantifies over complex x. Also the shape of
    prop:nohilbert, which argues two constructions and concludes 'any'."""
    out = []
    for c in g.claims:
        if c.status != "live":
            continue
        mine = {_norm_hyp(h) for h in c.hypotheses}
        for s in c.internal_steps:
            extra = [h for h in (s.get("hypotheses") or [])
                     if isinstance(h, str) and _norm_hyp(h) not in mine]
            if extra and not s.get("justification"):
                out.append(Finding(
                    "L4", "error", c.rel,
                    f"step {str(s.get('step'))[:60]!r} assumes {extra} — narrower than "
                    f"the claim's hypotheses — with no justification for applying it "
                    f"at full generality"))
    return out


def lint_L5_novelty(g: Graph) -> list[Finding]:
    """No claim reaches conjecture or above with novelty unchecked.

    Origin: CE-1's interference metric is the relative entropy of imaginarity
    (Xue et al. 2021) and was carried as an original contribution."""
    out = []
    for c in g.claims:
        if c.status != "live" or c.tier_index < TIER_INDEX["conjecture"]:
            continue
        nov = c.data.get("novelty")
        status = nov.get("status") if isinstance(nov, dict) else None
        if status not in (None, "unchecked"):
            continue
        out.append(Finding(
            "L5", "error", c.rel,
            f"tier {c.tier!r} with novelty {status or 'absent'!r}: "
            "prior art must be searched before a claim is labelled"))
    return out


def lint_L6_citation_staleness(g: Graph) -> list[Finding]:
    """Load-bearing citations verified only against an abstract, or expired.

    Origin: nothing in the gate stack ever re-examines a citation already on
    `main` — verify_citations checks existence, claim-support is diff-scoped.
    Two misattributions (geroch, thm:exotic) sat green from March to July."""
    out = []
    today = _today()
    for c in g.claims:
        if c.status != "live":
            continue
        for ct in c.cites:
            if ct.get("role") != "load-bearing":
                continue
            v = ct.get("verified") if isinstance(ct.get("verified"), dict) else {}
            key = ct.get("key")
            by = v.get("by")
            if by in (None, "none"):
                out.append(Finding("L6", "error", c.rel,
                                   f"load-bearing citation {key!r} has no verification record"))
                continue
            if by == "abstract":
                out.append(Finding(
                    "L6", "warn", c.rel,
                    f"load-bearing citation {key!r} verified against abstract only; "
                    "polarity and scope need full text"))
            exp = _as_date(v.get("expires"))
            at = _as_date(v.get("at"))
            if exp is None and at is not None:
                exp = at + _dt.timedelta(days=CITATION_TTL_DAYS)
            if exp is not None and exp < today:
                out.append(Finding("L6", "warn", c.rel,
                                   f"citation {key!r} verification expired {exp}"))
    return out


def lint_L7_dead_dependency(g: Graph) -> list[Finding]:
    """A live claim resting on something dead, withdrawn, or superseded.

    This is demotion propagation as a lint: kill a node and every dependent
    lights up immediately, instead of waiting for a monthly sweep to notice."""
    out = []
    for c in g.claims:
        if c.status != "live":
            continue
        for d in c.load_bearing_deps:
            dep = g.by_id.get(d.get("id", ""))
            if dep and dep.status != "live":
                out.append(Finding(
                    "L7", "error", c.rel,
                    f"live claim rests on {dep.status} claim {dep.id!r}"))
    return out


def lint_L8_cycle(g: Graph) -> list[Finding]:
    """Circular load-bearing dependencies."""
    out, colour = [], {}

    def visit(cid, path):
        state = colour.get(cid)
        if state == "done":
            return
        if state == "open":
            cycle = " -> ".join(path[path.index(cid):] + [cid])
            out.append(Finding("L8", "error", g.by_id[cid].rel,
                               f"dependency cycle: {cycle}"))
            return
        colour[cid] = "open"
        c = g.by_id.get(cid)
        if c:
            for d in c.load_bearing_deps:
                did = d.get("id")
                if did in g.by_id:
                    visit(did, path + [cid])
        colour[cid] = "done"

    for c in g.claims:
        visit(c.id, [])
    return out


def lint_L9_formal_integrity(g: Graph) -> list[Finding]:
    """A formal node with a `sorry`, or resting on non-standard axioms."""
    out = []
    for c in g.claims:
        if c.kind != "formal":
            continue
        f = c.data.get("formal") or {}
        if f.get("sorry_free") is not True:
            out.append(Finding("L9", "error", c.rel,
                               "formal node is not asserted sorry-free"))
        axioms = f.get("axioms") or []
        extra = [a for a in axioms if a not in STANDARD_AXIOMS]
        if extra:
            out.append(Finding("L9", "error", c.rel,
                               f"formal node rests on non-standard axioms: {extra}"))
    return out


def lint_L10_formal_build(g: Graph) -> list[Finding]:
    """A formal node whose build result is missing, failing, or stale.

    Origin: programs/co-emergence/lean/ exists, is pinned, and is asserted
    sorry-free in a LaTeX remark — and no CI job has ever re-run it."""
    out = []
    today = _today()
    for c in g.claims:
        if c.kind != "formal":
            continue
        f = c.data.get("formal") or {}
        lb = f.get("last_built") if isinstance(f.get("last_built"), dict) else None
        if not lb:
            out.append(Finding("L10", "error", c.rel,
                               "formal node has no build record; a machine check "
                               "nobody re-runs is an attestation, not a check"))
            continue
        if lb.get("result") != "pass":
            out.append(Finding("L10", "error", c.rel,
                               f"last build result {lb.get('result')!r}"))
        at = _as_date(lb.get("at"))
        if at and (today - at).days > 30:
            out.append(Finding("L10", "warn", c.rel,
                               f"last built {at} ({(today - at).days}d ago)"))
    return out


def lint_L11_bridge(g: Graph) -> list[Finding]:
    """A formal node discharging an informal claim without a reviewed bridge.

    Lean proves a formal statement; the paper makes an informal one. The
    correspondence is where errors hide and Lean cannot check it — so it is
    declared, tiered, and adversarially reviewed like any other claim. This is
    L2's cross-object transfer with one object formal and one not."""
    out = []
    for c in g.claims:
        if c.kind != "formal":
            continue
        discharges = c.data.get("discharges") or []
        if not discharges:
            continue
        bridge = c.data.get("bridge") if isinstance(c.data.get("bridge"), dict) else None
        if not bridge or not bridge.get("claim"):
            out.append(Finding("L11", "error", c.rel,
                               f"discharges {discharges} with no declared bridge "
                               "from the formal statement to the paper's claim"))
            continue
        rev = bridge.get("reviewed")
        if not (isinstance(rev, dict) and rev.get("by")):
            out.append(Finding("L11", "error", c.rel,
                               "bridge is unreviewed; it cannot raise the tier of "
                               f"{discharges}"))
    return out


def lint_L12_toolchain_drift(g: Graph) -> list[Finding]:
    """A formal node pinned to a different toolchain than the repo's."""
    out = []
    for c in g.claims:
        if c.kind != "formal":
            continue
        f = c.data.get("formal") or {}
        program = c.data.get("program")
        pin_path = os.path.join(REPO_ROOT, "programs", str(program), "lean", "lean-toolchain")
        if not os.path.exists(pin_path):
            continue
        with open(pin_path, encoding="utf-8") as fh:
            pin = fh.read().strip()
        if f.get("toolchain") and f["toolchain"] != pin:
            out.append(Finding("L12", "warn", c.rel,
                               f"toolchain {f['toolchain']!r} differs from repo pin {pin!r}"))
    return out


def lint_L13_tex_sync(g: Graph) -> list[Finding]:
    """A claim at sketch or above must appear in the paper at a matching tier.

    The paper stays prose; the graph stays authoritative about tier. This
    catches the drift where the .tex says Rigorous and the graph says Sketch."""
    out = []
    tex_cache: dict[str, str] = {}
    for c in g.claims:
        if c.status != "live" or c.tier_index < TIER_INDEX["sketch"]:
            continue
        tex = c.data.get("tex") if isinstance(c.data.get("tex"), dict) else None
        if not tex or not tex.get("file"):
            out.append(Finding("L13", "warn", c.rel,
                               f"tier {c.tier!r} claim has no `tex:` site recorded"))
            continue
        path = os.path.join(REPO_ROOT, str(tex["file"]))
        if path not in tex_cache:
            if not os.path.exists(path):
                out.append(Finding("L13", "error", c.rel,
                                   f"tex file {tex['file']!r} does not exist"))
                tex_cache[path] = ""
            else:
                with open(path, encoding="utf-8") as fh:
                    tex_cache[path] = fh.read()
        content = tex_cache[path]
        label = tex.get("label")
        if content and label and f"\\label{{{label}}}" not in content:
            out.append(Finding("L13", "error", c.rel,
                               f"tex label {label!r} not found in {tex['file']}"))
    return out


ALL_LINTS = [
    lint_L1_tier_inversion,
    lint_L2_cross_object,
    lint_L3_hypothesis_escape,
    lint_L4_step_escape,
    lint_L5_novelty,
    lint_L6_citation_staleness,
    lint_L7_dead_dependency,
    lint_L8_cycle,
    lint_L9_formal_integrity,
    lint_L10_formal_build,
    lint_L11_bridge,
    lint_L12_toolchain_drift,
    lint_L13_tex_sync,
]


def run_lints(g: Graph) -> list[Finding]:
    out = validate_schema(g)
    for fn in ALL_LINTS:
        out.extend(fn(g))
    order = {"error": 0, "warn": 1}
    return sorted(out, key=lambda f: (order.get(f.severity, 2), f.code, f.where))


# ── Section 5: Derived measures ────────────────────────────────────


def mechanical_coverage(g: Graph, claim_id: str) -> dict:
    """Fraction of the load-bearing dependency closure discharged by a valid
    formal node.

    Deliberately not 'does this claim have a Lean file' — that is satisfied by
    a formalization which assumes everything interesting. Assumed hypotheses
    are edges, and edges are counted."""
    c = g.by_id.get(claim_id)
    if not c:
        return {"claim": claim_id, "error": "unknown claim"}
    nodes = {claim_id} | g.closure(claim_id)
    discharged = set()
    for f in g.claims:
        if f.kind != "formal":
            continue
        problems = (lint_L9_formal_integrity(Graph([f]))
                    + lint_L10_formal_build(Graph([f])))
        if any(p.severity == "error" for p in problems):
            continue
        for d in (f.data.get("discharges") or []):
            if d in nodes:
                discharged.add(d)
    covered = len(discharged)
    total = len(nodes)
    return {
        "claim": claim_id,
        "closure_size": total,
        "mechanically_discharged": sorted(discharged),
        "coverage": round(covered / total, 3) if total else 0.0,
    }


def record_build(program: str, result: str, date: str,
                 root: str = REPO_ROOT) -> list[str]:
    """Write a build result into each formal node's `formal.last_built`.

    CI verifies the Lean development; this is how the graph learns that it did.
    Without it L10 fires and mechanical coverage reads zero even while the build
    is green — the check runs but the record does not know, which is the same
    class of gap as a machine check nobody re-runs.

    Edits the frontmatter line-wise rather than round-tripping the parser, which
    would reflow every file it touched. Idempotent: returns the ids actually
    changed, so a caller can skip opening a no-op pull request.
    """
    changed = []
    entry = f"  last_built: {{at: {date}, by: ci, result: {result}}}"
    pattern = os.path.join(root, "programs", program, "claims", "*.md")
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
        try:
            start = next(i for i, L in enumerate(lines) if L.rstrip() == "formal:")
        except StopIteration:
            continue                                   # not a formal node
        end = start + 1
        while end < len(lines) and (lines[end].startswith("  ") or not lines[end].strip()):
            end += 1
        block = lines[start + 1:end]
        existing = next((i for i, L in enumerate(block)
                         if L.startswith("  last_built:")), None)
        if existing is not None:
            if block[existing].rstrip() == entry:
                continue                               # already current
            block[existing] = entry
        else:
            while block and not block[-1].strip():      # keep trailing blanks last
                block.pop()
            block.append(entry)
        lines[start + 1:end] = block
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        changed.append(os.path.splitext(os.path.basename(path))[0])
    return changed


def stats(g: Graph) -> dict:
    live = [c for c in g.claims if c.status == "live"]
    dist = {t: sum(1 for c in live if c.tier == t) for t in TIERS}
    return {
        "claims_total": len(g.claims),
        "live": len(live),
        "stubs": sum(1 for c in g.claims if c.is_stub),
        "tier_distribution": dist,
        "by_status": {s: sum(1 for c in g.claims if c.status == s) for s in STATUSES},
        "formal_nodes": sum(1 for c in g.claims if c.kind == "formal"),
        "novelty_unchecked": sum(
            1 for c in live
            if c.tier_index >= TIER_INDEX["conjecture"]
            and (not isinstance(c.data.get("novelty"), dict)
                 or c.data["novelty"].get("status") in (None, "unchecked"))),
    }


# ── Section 6: CLI ─────────────────────────────────────────────────


def _cmd_lint(args) -> int:
    g, load_findings = Graph.load()
    findings = load_findings + run_lints(g)
    shown = [f for f in findings if args.warn or f.severity == "error"]
    if args.json:
        print(json.dumps([f.as_dict() for f in shown], indent=2))
    else:
        for f in shown:
            print(f)
        errors = sum(1 for f in findings if f.severity == "error")
        warns = sum(1 for f in findings if f.severity == "warn")
        print(f"\n{len(g.claims)} claims · {errors} error(s) · {warns} warning(s)"
              + ("" if args.warn else "  [--warn to show warnings]"))
        if args.soft and errors:
            print("[--soft] reporting only; exit 0 despite errors")
    if args.soft:
        return 0
    return 1 if any(f.severity == "error" for f in findings) else 0


def _cmd_show(args) -> int:
    g, _ = Graph.load()
    c = g.by_id.get(args.id)
    if not c:
        print(f"unknown claim {args.id!r}", file=sys.stderr)
        return 1
    print(json.dumps(c.data, indent=2, default=str))
    deps = g.dependents(c.id)
    if deps:
        print("\nDependents (demoting this claim puts these in question):")
        for d in deps:
            print(f"  {d.id}  [{d.tier}]")
    return 0


def _cmd_query(args) -> int:
    g, _ = Graph.load()
    rows = []
    for c in g.claims:
        if args.tier and c.tier != args.tier:
            continue
        if args.status and c.status != args.status:
            continue
        if args.program and c.data.get("program") != args.program:
            continue
        if args.since:
            prov = c.data.get("provenance") or {}
            born = _as_date(prov.get("born") if isinstance(prov, dict) else None)
            if not born or born < _dt.date.fromisoformat(args.since):
                continue
        rows.append(c)
    for c in rows:
        print(f"{c.id:42s} {c.tier:11s} {c.status:11s} {c.data.get('program')}")
    print(f"\n{len(rows)} claim(s)")
    return 0


def _cmd_coverage(args) -> int:
    g, _ = Graph.load()
    print(json.dumps(mechanical_coverage(g, args.id), indent=2))
    return 0


def _cmd_formal(args) -> int:
    """Emit the formal nodes as JSON, for CI to verify against.

    The graph is the single source of truth for what the Lean development is
    claimed to prove and on which axioms. CI builds its `#print axioms` check
    from this rather than from a hand-maintained list, so a declaration renamed
    in Lean — or misrecorded in a claim node — fails loudly instead of drifting.
    """
    g, _ = Graph.load()
    out = []
    for c in g.claims:
        if c.kind != "formal" or c.status != "live":
            continue
        if args.program and c.data.get("program") != args.program:
            continue
        f = c.data.get("formal") or {}
        out.append({
            "id": c.id,
            "program": c.data.get("program"),
            "decl": f.get("decl"),
            "axioms": f.get("axioms") or [],
            "sorry_free": f.get("sorry_free"),
            "discharges": c.data.get("discharges") or [],
        })
    print(json.dumps(out, indent=2))
    return 0


def _cmd_record_build(args) -> int:
    date = args.date or _dt.date.today().isoformat()
    changed = record_build(args.program, args.result, date)
    print(json.dumps({"program": args.program, "result": args.result,
                      "date": date, "changed": changed}, indent=2))
    return 0


def _cmd_stats(args) -> int:
    g, _ = Graph.load()
    print(json.dumps(stats(g), indent=2))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lint", help="validate the graph and run all lints")
    p.add_argument("--warn", action="store_true", help="include warnings")
    p.add_argument("--json", action="store_true")
    p.add_argument(
        "--soft", action="store_true",
        help="report findings but always exit 0. For landing the gate on a graph "
             "with a known-open backlog, so it can be wired as a required check "
             "before the backlog is burned down. Drop this flag to make it bite.")
    p.set_defaults(fn=_cmd_lint)

    p = sub.add_parser("show", help="print a claim and its dependents")
    p.add_argument("id")
    p.set_defaults(fn=_cmd_show)

    p = sub.add_parser("query", help="filter claims")
    p.add_argument("--tier", choices=TIERS)
    p.add_argument("--status", choices=STATUSES)
    p.add_argument("--program")
    p.add_argument("--since", help="ISO date; filters on provenance.born")
    p.set_defaults(fn=_cmd_query)

    p = sub.add_parser("coverage", help="mechanical coverage of a claim's closure")
    p.add_argument("id")
    p.set_defaults(fn=_cmd_coverage)

    p = sub.add_parser("formal", help="emit formal (Lean) nodes as JSON for CI")
    p.add_argument("--program", help="restrict to one program")
    p.set_defaults(fn=_cmd_formal)

    p = sub.add_parser("record-build",
                       help="write a CI build result into formal nodes' last_built")
    p.add_argument("--program", required=True)
    p.add_argument("--result", required=True, choices=["pass", "fail"])
    p.add_argument("--date", help="ISO date; defaults to today")
    p.set_defaults(fn=_cmd_record_build)

    p = sub.add_parser("stats", help="graph-level counts")
    p.set_defaults(fn=_cmd_stats)

    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
