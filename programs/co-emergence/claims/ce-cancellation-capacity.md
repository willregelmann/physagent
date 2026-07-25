---
id: ce-cancellation-capacity
program: co-emergence
tier: rigorous
status: live
statement: >
  Cancellation capacity holds if and only if the mode operator is hyperbolic:
  elliptic modes give a strictly positive bounded solution that can never
  cancel, while hyperbolic modes satisfy phi(u + pi/omega) = -phi(u) for every
  polarization.
object:
  name: mode_ode
  space: solutions of phi'' = ±omega^2 phi on a half-line
hypotheses:
  - the operator type is elliptic or hyperbolic
  - omega is nonzero
depends_on:
  - id: scb-mode-analysis
    role: load-bearing
    transfers: cross-object
    justification: >
      The companion signature-change-boundary note supplies the nu = 1/2 Bessel
      reduction to elementary trigonometric/exponential form near the degenerate
      surface. Cited, not extended; the reduction is what makes these two
      elementary ODE facts the whole content of the claim.
falsifier: >
  An elliptic bounded mode admitting cancellation, or a hyperbolic polarization
  with no antiperiodic point.
consequence: >
  The signature dichotomy governs whether the self-consistency weight can cancel.
novelty: {status: unchecked}
tex: {file: programs/co-emergence/index.tex, label: sec:phase}
provenance: {born: 2026-06-22, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Both ODE facts re-derived independently and correct. The paper is careful
    about scope: the physical identification is separately labelled Sketch one
    paragraph later. Unflagged edge case, not demotion-worthy: omega = 0 (the
    m = k = 0 zero mode) collapses both ODEs to phi'' = 0 and the antiperiodicity
    argument degenerates.
---

Confirmed at high confidence. Note the `omega is nonzero` hypothesis is stated
here but not in the paper.
