---
id: fpe-starobinsky-existence
program: fixed-point-existence
tier: rigorous
status: live
statement: >
  An exact constant-H de Sitter fixed point of the semiclassical Einstein
  equation exists for conformal matter with trace anomaly coefficient a2 > 0,
  and is unstable.
hypotheses:
  - FRW/cosmological setting
  - conformal matter with a2 > 0
cites:
  - key: starobinsky
    role: load-bearing
    supports: >
      Quantum one-loop conformal-matter corrections admit nonsingular solutions
      beginning in a de Sitter state.
    verified: {at: 2026-07-24, by: abstract, expires: 2027-07-24}
  - key: capper_duff
    role: context
    supports: existence of the trace anomaly in dimensional regularization
    verified: {at: 2026-07-24, by: full-text, expires: 2027-07-24}
falsifier: an FRW conformal-matter model with a2 > 0 and no constant-H solution
consequence: >
  Self-consistent solutions of the semiclassical Einstein equation exist exactly,
  not only perturbatively.
novelty: {status: unchecked}
tex: {file: programs/fixed-point-existence/index.tex, label: sec:starobinsky}
provenance: {born: 2026-06-26, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Existence re-derived independently from the trace-anomaly structure: the Weyl
    tensor vanishes identically on FRW (conformally flat) and all curvature
    invariants are constant on exactly-constant-H de Sitter, so scheme-dependent
    box-R terms vanish and a purely algebraic H0^4 relation remains. "Exact" is
    the correct characterization. A literature search initially surfaced claims
    that "the Starobinsky model admits no exact de Sitter solution"; traced to the
    later f(R) = R + R^2/6M^2 model, where R = 0 is forced - a different model.
    The paper cites the correct 1980 anomaly-induced paper for the correct claim.
  confidence: medium-high
  caveat: >
    The paywalled 1980 primary text could not be reached; the instability claim
    rests on secondary corroboration rather than the source itself. Hence
    verified.by is recorded as `abstract`, not `full-text`.
---

See [[fpe-starobinsky-coefficient]] for the part the paper correctly keeps at
Sketch.
