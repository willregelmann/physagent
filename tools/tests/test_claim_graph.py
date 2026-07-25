"""
Tests for the claim graph.

The lint tests are not hypotheticals. Each one encodes a defect that actually
reached `main` in this repository and was found by the 2026-07-24 independent
audit (`explorations/governance/2026-07-24-interim-audit.md`). The acceptance
criterion for the whole design is this file: if the lint suite does not catch
these, the schema is wrong.
"""

import datetime as dt
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from claim_graph import (  # noqa: E402
    Claim,
    Graph,
    ParseError,
    lint_L1_tier_inversion,
    lint_L2_cross_object,
    lint_L4_step_escape,
    lint_L5_novelty,
    lint_L6_citation_staleness,
    lint_L7_dead_dependency,
    lint_L8_cycle,
    lint_L9_formal_integrity,
    lint_L10_formal_build,
    lint_L11_bridge,
    mechanical_coverage,
    parse_frontmatter,
    run_lints,
    validate_schema,
)


def claim(text: str, name: str = "x") -> Claim:
    data, body = parse_frontmatter("---\n" + text.strip() + "\n---\n")
    return Claim(data, body, f"/fake/programs/p/claims/{name}.md")


def codes(findings):
    return {f.code for f in findings}


# ── Parser ─────────────────────────────────────────────────────────


def test_parser_handles_the_full_schema_shape():
    data, body = parse_frontmatter(
        """---
id: a-claim
tier: rigorous
statement: >
  A folded scalar that runs
  across two lines.
object:
  name: F
  space: C^N
hypotheses:
  - gamma in R
  - h in R^N
depends_on:
  - id: other
    role: load-bearing
    transfers: cross-object
    justification: null
cites:
  - key: someone
    verified: {at: 2026-01-01, by: full-text}
novelty:
  status: novel
  found: []
---
Body text.
"""
    )
    assert data["statement"] == "A folded scalar that runs across two lines."
    assert data["object"]["space"] == "C^N"
    assert data["hypotheses"] == ["gamma in R", "h in R^N"]
    assert data["depends_on"][0]["role"] == "load-bearing"
    assert data["depends_on"][0]["justification"] is None
    assert data["cites"][0]["verified"]["by"] == "full-text"
    assert data["novelty"]["found"] == []
    assert body == "Body text."


def test_parser_rejects_rather_than_silently_misreads():
    with pytest.raises(ParseError):
        parse_frontmatter("no fence here\n")
    with pytest.raises(ParseError):
        parse_frontmatter("---\nid: a\n")  # unterminated


# ── L1 / L2: the CE-13 defect ──────────────────────────────────────
#
# prop:riem_classical, before PR #162, asserted Rigorous uniqueness on the
# strength of the companion paper's Banach contraction — which is permanently
# Sketch, and is about the field-theoretic semiclassical Einstein equation on
# manifolds, not the finite map F on C^N. Two distinct defects, one edge.


CE13_DEPENDENCY = """
id: fpe-banach-contraction
program: fixed-point-existence
tier: sketch
status: live
statement: >
  The semiclassical Einstein equation admits a Banach contraction on field
  configurations over a manifold with compact Cauchy surfaces.
object:
  name: SCE_map
  space: field configurations on M
falsifier: an explicit non-contractive configuration in the stated norm
consequence: existence and uniqueness of a self-consistent metric
novelty: {status: novel}
"""

CE13_DEFECT = """
id: ce-riem-classical-unique
program: co-emergence
tier: rigorous
status: live
statement: >
  The self-consistency fixed point psi* is unique in (C^N, ||.||_2).
object:
  name: F_toy
  space: C^N
depends_on:
  - id: fpe-banach-contraction
    role: load-bearing
    transfers: same-object
falsifier: two distinct fixed points of F for the same parameters
consequence: uniqueness underwrites the classicality argument
novelty: {status: novel}
"""


def test_L1_catches_rigorous_resting_on_sketch():
    g = Graph([claim(CE13_DEPENDENCY, "fpe-banach-contraction"),
               claim(CE13_DEFECT, "ce-riem-classical-unique")])
    findings = lint_L1_tier_inversion(g)
    assert len(findings) == 1
    assert "tier inversion" in findings[0].message
    assert "fpe-banach-contraction" in findings[0].message


def test_L2_catches_undeclared_cross_object_transfer():
    """The subtler half: the objects genuinely differ, so declaring the edge
    same-object is itself the defect."""
    g = Graph([claim(CE13_DEPENDENCY, "fpe-banach-contraction"),
               claim(CE13_DEFECT, "ce-riem-classical-unique")])
    findings = lint_L2_cross_object(g)
    assert len(findings) == 1
    assert "objects differ" in findings[0].message
    assert "C^N" in findings[0].message


def test_L2_requires_written_justification_for_declared_transfers():
    src = CE13_DEFECT.replace("transfers: same-object", "transfers: cross-object")
    g = Graph([claim(CE13_DEPENDENCY, "fpe-banach-contraction"),
               claim(src, "ce-riem-classical-unique")])
    findings = lint_L2_cross_object(g)
    assert len(findings) == 1
    assert "no justification" in findings[0].message


def test_the_post_162_repair_passes_both_lints():
    """PR #162 split the proposition: part (a) is Rigorous and needs no
    uniqueness at all; part (b) is Sketch and states the non-transfer."""
    fixed = """
id: ce-riem-classical-real
program: co-emergence
tier: rigorous
status: live
statement: >
  F sends all of C^N into R^N_{>0}; hence every fixed point of F is
  real-valued, regardless of uniqueness.
object:
  name: F_toy
  space: C^N
hypotheses:
  - gamma in R
  - h in R^N
  - alpha_j and beta in R
falsifier: a complex-valued fixed point of F under the stated hypotheses
consequence: Riemannian conditioning yields real conditional density matrices
novelty: {status: novel}
"""
    g = Graph([claim(CE13_DEPENDENCY, "fpe-banach-contraction"),
               claim(fixed, "ce-riem-classical-real")])
    assert lint_L1_tier_inversion(g) == []
    assert lint_L2_cross_object(g) == []


# ── L4: the interference-metric defect ─────────────────────────────
#
# prop:interference_metric part (c) asserted
#     x^dag (rho + rho^T) x = 2 Re(x^dag rho x)
# which is false for Hermitian non-real rho. Counterexample reproduced during
# the audit: rho = [[1, i], [-i, 1]], x = (1, i) gives 4 on the left, 0 on the
# right. The identity holds for *real* x — the author almost certainly had the
# real-vector argument in mind and generalised the quantifier without
# rechecking. That is exactly a step whose hypotheses are narrower than its
# claim's.


INTERFERENCE_DEFECT = """
id: ce-interference-metric
program: co-emergence
tier: rigorous
status: live
statement: >
  supp(rho) is contained in supp(Re rho), so I_S(rho) = S(rho || Re rho) is
  finite for every density matrix.
hypotheses:
  - rho is Hermitian
  - rho is positive semidefinite
  - x in C^d
internal_steps:
  - step: "x^dag (rho + rho^T) x = 2 Re(x^dag rho x)"
    hypotheses: [x in R^d]
falsifier: a density matrix whose support escapes that of its real part
consequence: the interference metric is well defined on all states
novelty: {status: prior-art, found: [xue_imaginarity]}
"""


def test_L4_catches_a_step_proved_only_for_real_vectors():
    g = Graph([claim(INTERFERENCE_DEFECT, "ce-interference-metric")])
    findings = lint_L4_step_escape(g)
    assert len(findings) == 1
    assert "x in R^d" in findings[0].message
    assert "narrower" in findings[0].message


def test_L4_accepts_the_step_once_the_narrowing_is_justified():
    """The audit supplied two repairs. Either one is a written justification
    for using the narrowed step at full generality."""
    repaired = INTERFERENCE_DEFECT.replace(
        "    hypotheses: [x in R^d]",
        "    hypotheses: [x in R^d]\n"
        "    justification: >\n"
        "      Not needed at full generality: rho^T is PSD by part (a), so both\n"
        "      terms of x^dag (rho + rho^T) x are individually non-negative and a\n"
        "      zero sum forces each to vanish.",
    )
    g = Graph([claim(repaired, "ce-interference-metric")])
    assert lint_L4_step_escape(g) == []


def test_L4_also_catches_the_nohilbert_quantifier_shape():
    """prop:nohilbert claims 'any formulation' while arguing exactly two
    constructions — the same defect wearing different clothes."""
    src = """
id: ce-nohilbert
program: co-emergence
tier: rigorous
status: live
statement: >
  Any formulation taking a Hilbert space with inner product as fundamental
  violates the timeless axiom.
hypotheses:
  - an arbitrary quantum gravity formulation
internal_steps:
  - step: the inner product requires a Cauchy surface
    hypotheses: [the standard QFT Fock-space construction]
  - step: unitary evolution requires a time parameter
    hypotheses: [evolution given by U(t2, t1)]
falsifier: a covariant Hilbert-space construction with no preferred slice
consequence: the framework must not take a Hilbert space as input
novelty: {status: novel}
"""
    findings = lint_L4_step_escape(Graph([claim(src, "ce-nohilbert")]))
    assert len(findings) == 2  # algebraic QFT / GNS escapes both


# ── L5: the CE-1 rediscovery ───────────────────────────────────────


def test_L5_blocks_a_labelled_claim_with_novelty_unchecked():
    src = INTERFERENCE_DEFECT.replace(
        "novelty: {status: prior-art, found: [xue_imaginarity]}",
        "novelty: {status: unchecked}")
    findings = lint_L5_novelty(Graph([claim(src, "ce-interference-metric")]))
    assert len(findings) == 1
    assert "prior art must be searched" in findings[0].message


def test_L5_allows_speculation_without_a_novelty_check():
    """The generative tier is meant to be cheap. Prior art is required to
    become a conjecture, not to have a thought."""
    src = """
id: some-speculation
program: co-emergence
tier: speculation
status: live
statement: maybe the boundary carries a Carrollian structure
"""
    assert lint_L5_novelty(Graph([claim(src, "some-speculation")])) == []


# ── L6: citations nobody re-examines ───────────────────────────────


def test_L6_flags_abstract_only_verification_of_a_load_bearing_citation():
    """Both citation passes in the audit split on exactly this: the abstract
    reader passed a misattribution the full-text reader caught."""
    src = """
id: ggd-anastopoulos-caution
program: gaussian-gravitational-decoherence
tier: sketch
status: live
statement: field-theoretic treatments caution against classical noise sources
cites:
  - key: anastopoulos_hu
    role: load-bearing
    supports: caution against stress-energy variance as a classical noise source
    verified: {at: 2026-07-01, by: abstract, expires: 2027-07-01}
falsifier: the source making no such caution
consequence: constrains how the noise kernel may be justified
novelty: {status: novel}
"""
    findings = lint_L6_citation_staleness(Graph([claim(src, "ggd-anastopoulos-caution")]))
    assert any("abstract only" in f.message for f in findings)


def test_L6_flags_expired_verification():
    """The geroch and thm:exotic misattributions sat green on main from March
    to July because nothing re-examines a citation after the day it lands."""
    stale = (dt.date.today() - dt.timedelta(days=400)).isoformat()
    expired = (dt.date.today() - dt.timedelta(days=35)).isoformat()
    src = f"""
id: ce-signature-time
program: co-emergence
tier: rigorous
status: live
statement: timelike paths terminate at the degenerate surface, spacelike cross
cites:
  - key: geroch
    role: load-bearing
    supports: global hyperbolicity implies a topological splitting
    verified: {{at: {stale}, by: full-text, expires: {expired}}}
falsifier: a globally hyperbolic spacetime with no such splitting
consequence: local worldline time without a global foliation
novelty: {{status: novel}}
"""
    findings = lint_L6_citation_staleness(Graph([claim(src, "ce-signature-time")]))
    assert any("expired" in f.message for f in findings)


def test_L6_errors_when_a_load_bearing_citation_has_no_record_at_all():
    src = """
id: c
program: p
tier: sketch
status: live
statement: s
cites:
  - key: unchecked_source
    role: load-bearing
    supports: something
falsifier: f
consequence: c
novelty: {status: novel}
"""
    findings = lint_L6_citation_staleness(Graph([claim(src, "c")]))
    assert any(f.severity == "error" for f in findings)


# ── L7: demotion propagation ───────────────────────────────────────


def test_L7_lights_up_every_dependent_the_moment_a_claim_dies():
    """This is CE-13's whole content, computed instead of discovered weeks
    later by a monthly sweep."""
    dead = CE13_DEPENDENCY.replace("status: live", "status: withdrawn")
    g = Graph([claim(dead, "fpe-banach-contraction"),
               claim(CE13_DEFECT, "ce-riem-classical-unique")])
    findings = lint_L7_dead_dependency(g)
    assert len(findings) == 1
    assert "withdrawn" in findings[0].message


def test_dependents_query_answers_what_a_demotion_puts_in_question():
    g = Graph([claim(CE13_DEPENDENCY, "fpe-banach-contraction"),
               claim(CE13_DEFECT, "ce-riem-classical-unique")])
    deps = g.dependents("fpe-banach-contraction")
    assert [d.id for d in deps] == ["ce-riem-classical-unique"]


# ── L8: cycles ─────────────────────────────────────────────────────


def test_L8_detects_a_dependency_cycle():
    a = """
id: a
program: p
tier: sketch
status: live
statement: a
depends_on: [{id: b, role: load-bearing}]
falsifier: f
consequence: c
novelty: {status: novel}
"""
    b = """
id: b
program: p
tier: sketch
status: live
statement: b
depends_on: [{id: a, role: load-bearing}]
falsifier: f
consequence: c
novelty: {status: novel}
"""
    findings = lint_L8_cycle(Graph([claim(a, "a"), claim(b, "b")]))
    assert findings and "cycle" in findings[0].message


# ── L9 / L10 / L11: Lean nodes ─────────────────────────────────────


LEAN_GOOD = """
id: lean-purity-decrease
program: co-emergence
kind: formal
tier: rigorous
status: live
statement: purity m L theta <= purity m L 0
formal:
  decl: CoEmergence.EntropyExcess.purity_decrease
  toolchain: leanprover/lean4:v4.31.0
  axioms: [propext, Classical.choice, Quot.sound]
  sorry_free: true
  last_built: {at: TODAY, by: ci, result: pass}
bridge:
  to: ce-entropy-excess-a
  claim: >
    Lean's rho m L theta is the paper's M(theta)^dag M(theta); trace_rho_sq
    certifies that sum |rho_jk|^2 is Tr(rho^2) via Hermiticity.
  reviewed: {by: adversary, at: TODAY}
discharges: [ce-entropy-excess-a]
falsifier: a counterexample to the formal statement
consequence: part (a) is mechanically discharged
novelty: {status: novel}
""".replace("TODAY", dt.date.today().isoformat())


def test_L9_rejects_a_formal_node_with_sorry_or_extra_axioms():
    bad = LEAN_GOOD.replace("sorry_free: true", "sorry_free: false")
    assert any("sorry-free" in f.message
               for f in lint_L9_formal_integrity(Graph([claim(bad, "lean-purity-decrease")])))

    axm = LEAN_GOOD.replace("[propext, Classical.choice, Quot.sound]",
                            "[propext, Classical.choice, Quot.sound, sorryAx]")
    findings = lint_L9_formal_integrity(Graph([claim(axm, "lean-purity-decrease")]))
    assert any("non-standard axioms" in f.message for f in findings)


def test_L10_rejects_a_formal_node_nobody_has_rebuilt():
    """The live case: programs/co-emergence/lean/ is pinned and asserted
    sorry-free in a LaTeX remark, and no CI job has ever re-run it."""
    nobuild = LEAN_GOOD.replace(
        "  last_built: {at: %s, by: ci, result: pass}\n" % dt.date.today().isoformat(), "")
    findings = lint_L10_formal_build(Graph([claim(nobuild, "lean-purity-decrease")]))
    assert any("no build record" in f.message for f in findings)
    assert any("attestation, not a check" in f.message for f in findings)


def test_L11_requires_a_reviewed_bridge_before_lean_can_raise_a_tier():
    unreviewed = LEAN_GOOD.replace(
        "  reviewed: {by: adversary, at: %s}\n" % dt.date.today().isoformat(), "")
    findings = lint_L11_bridge(Graph([claim(unreviewed, "lean-purity-decrease")]))
    assert any("unreviewed" in f.message for f in findings)


def test_a_well_formed_lean_node_passes():
    g = Graph([claim(LEAN_GOOD, "lean-purity-decrease")])
    assert lint_L9_formal_integrity(g) == []
    assert lint_L10_formal_build(g) == []
    assert lint_L11_bridge(g) == []


# ── Mechanical coverage ────────────────────────────────────────────


def test_coverage_counts_assumed_hypotheses_as_uncovered():
    """The entropy-excess pair is the worked example. Part (a) is fully
    discharged; part (b) is machine-checked only at the scalar step, with
    three structural links supplied as hypotheses — so it is Rigorous, but it
    is not 'machine-checked', and the graph says which."""
    part_a = """
id: ce-entropy-excess-a
program: co-emergence
tier: rigorous
status: live
statement: purity decreases under phase, for all ranks
falsifier: a counterexample matrix
consequence: the entropy excess has a proved first half
novelty: {status: novel}
"""
    part_b = """
id: ce-entropy-excess-b
program: co-emergence
tier: rigorous
status: live
statement: rank-2 entropy excess
depends_on:
  - {id: ce-eigenvalue-identification, role: load-bearing}
  - {id: ce-entropy-connection, role: load-bearing}
  - {id: ce-fact-2, role: load-bearing}
falsifier: a rank-2 counterexample
consequence: the entropy excess has a proved second half
novelty: {status: novel}
"""
    links = [
        f"""
id: {name}
program: co-emergence
tier: rigorous
status: live
statement: {name}
falsifier: f
consequence: c
novelty: {{status: novel}}
"""
        for name in ("ce-eigenvalue-identification", "ce-entropy-connection", "ce-fact-2")
    ]
    g = Graph(
        [claim(part_a, "ce-entropy-excess-a"), claim(part_b, "ce-entropy-excess-b"),
         claim(LEAN_GOOD, "lean-purity-decrease")]
        + [claim(s, s.split("id: ")[1].split("\n")[0]) for s in links]
    )
    assert mechanical_coverage(g, "ce-entropy-excess-a")["coverage"] == 1.0
    cov_b = mechanical_coverage(g, "ce-entropy-excess-b")
    assert cov_b["closure_size"] == 4
    assert cov_b["coverage"] == 0.0


def test_coverage_cannot_be_gamed_by_a_formalization_that_assumes_its_way():
    """A Lean node whose build is stale discharges nothing, however
    confidently the frontmatter asserts it."""
    stale = LEAN_GOOD.replace("result: pass", "result: fail")
    target = """
id: ce-entropy-excess-a
program: co-emergence
tier: rigorous
status: live
statement: s
falsifier: f
consequence: c
novelty: {status: novel}
"""
    g = Graph([claim(target, "ce-entropy-excess-a"),
               claim(stale, "lean-purity-decrease")])
    assert mechanical_coverage(g, "ce-entropy-excess-a")["coverage"] == 0.0


# ── Schema ─────────────────────────────────────────────────────────


def test_conjecture_gate_fields_are_required_at_conjecture_and_above():
    src = """
id: c
program: p
tier: conjecture
status: live
statement: something might be true
"""
    findings = validate_schema(Graph([claim(src, "c")]))
    missing = " ".join(f.message for f in findings)
    assert "falsifier" in missing
    assert "consequence" in missing
    assert "novelty" in missing


def test_dangling_dependency_is_an_error():
    src = """
id: c
program: p
tier: sketch
status: live
statement: s
depends_on: [{id: nonexistent, role: load-bearing}]
falsifier: f
consequence: c
novelty: {status: novel}
"""
    assert "E016" in codes(validate_schema(Graph([claim(src, "c")])))


# ── The real graph ─────────────────────────────────────────────────


def test_the_repository_graph_parses_and_lints():
    """Every claim file in programs/*/claims/ must at minimum parse and carry
    a valid schema. Lint errors are reported, not asserted absent — the graph
    is allowed to record known-open defects."""
    g, load_findings = Graph.load()
    assert not [f for f in load_findings if f.code == "E000"], \
        "unparseable claim files: " + str([f.message for f in load_findings])
    findings = run_lints(g)
    for f in findings:
        print(f)
    assert g.claims, "no claims extracted yet"
