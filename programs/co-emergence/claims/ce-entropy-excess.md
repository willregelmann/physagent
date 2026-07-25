---
id: ce-entropy-excess
program: co-emergence
tier: rigorous
status: live
statement: >
  Phase-induced purity decrease and entropy excess: for M(theta)_ij =
  m_ij^(1+i theta) with m_ij > 0, purity is non-increasing in theta at all
  ranks, and for min(d_sub, d_env) = 2 the von Neumann entropy is
  non-decreasing.
object:
  name: rho_theta
  space: positive matrices under entrywise phase
hypotheses:
  - m_ij > 0 strictly
  - "part (b) additionally requires min(d_sub, d_env) = 2"
falsifier: a matrix with strictly positive entries violating either inequality
consequence: >
  Lorentzian (theta != 0) configurations carry strictly more entropy than their
  Riemannian counterparts; the entropy excess is the order parameter.
novelty:
  status: novel
  searched: 2026-07-24
  found: []
  note: >
    No paper studies M(theta)_ij = m_ij^(1+i theta) or proves purity/entropy
    monotonicity in theta for it. Adjacent standard fact: dephasing/pinching
    cannot decrease von Neumann entropy (Schur concavity under majorization;
    Bhatia, Matrix Analysis). Mechanism differs -- that is a unital channel,
    this is deterministic magnitude-dependent phase modulation on a
    rectangular matrix. Deliberately re-checked against this program's known
    past miss: the imaginarity resource theory (Xue et al. 2021, and
    arXiv:2103.01805 fetched in full) quantifies a single fixed state and
    does NOT parametrize a family in theta. Different object; not a second
    CE-1.
tex: {file: programs/co-emergence/index.tex, label: sec:entropy_excess}
provenance: {born: 2026-03-05, born_by: human}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Full proof re-derived independently by two auditors. Facts 1-3 and both
    parts correct; equality conditions correctly derived. The paper's
    Perron-Frobenius invocation is heavier machinery than needed - a pointwise
    triangle-inequality argument suffices. Self-contained: no external citation
    and no dependency on another paper result.
---

The general-rank entropy excess is **false** and was retracted; only the
corrected inequalities are claimed here. That retraction was itself produced by
an attempted Lean formalization — see [[lean-rank2-entropy-excess]].
