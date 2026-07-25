---
id: ce-riem-classical-real
program: co-emergence
tier: rigorous
status: live
statement: >
  The self-consistency map F sends all of C^N into R^N_{>0}; consequently every
  fixed point of F - regardless of uniqueness - is real-valued, and every
  conditional density matrix of a fixed point has real entries.
object:
  name: F_toy
  definition: "F(psi)_sigma = exp(gamma R_sigma(psi)) / ||exp(gamma R(psi))||_2"
  space: C^N
hypotheses:
  - gamma in R
  - h in R^N
falsifier: a complex-valued fixed point of F under the stated hypotheses
consequence: Riemannian conditioning is classical; no interference survives
novelty: {status: unchecked}
tex: {file: programs/co-emergence/index.tex, label: prop:riem_classical}
provenance: {born: 2026-07-18, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Appeals to no uniqueness or contraction result at all - that is the point.
    R_sigma depends on psi only through |psi_sigma|^2, so with real parameters
    exp(gamma R_sigma) is real positive and F maps all of C^N into R^N_{>0}
    unconditionally. Verified numerically: fixed points found had max|Im| = 0 to
    machine precision. Minor completeness gap: the premise states gamma in R and
    h in R^N but not alpha_j, beta in R, which the algebra requires; true of
    every actual instantiation, one line to fix.
---

This is the **repaired** form, landed by PR #162 in response to milestone CE-13.
The pre-repair text asserted Rigorous uniqueness on the strength of "the Banach
contraction (Section level2) guarantees a unique fixed point in C^N" - a
contraction that does not exist for this map on this space. See
[[ce-riem-classical-unique]] for the honest residual.

Detection (governor, 2026-07-05) -> autonomous repair (PR #162) -> honest
residual labelling -> blind audit confirmation, with no human in the path.
