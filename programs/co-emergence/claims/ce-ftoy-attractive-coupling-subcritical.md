---
id: ce-ftoy-attractive-coupling-subcritical
program: co-emergence
tier: speculation
status: live
statement: >
  For real gamma > 0 (attractive self-consistency weighting, the sign opposite
  every instance tested to date, all fixed at gamma = -1 or -2) F_toy's unique
  fixed point loses stability through a subcritical flip bifurcation rather
  than the supercritical one established at gamma = -1: onset produces a
  finite-amplitude jump to a period-2 cycle, with a finite beta-window of
  bistability (stable fixed point and stable cycle coexisting) below the
  crossing, rather than a continuous cycle-amplitude bound growing
  continuously as sqrt(beta - beta_flip) from zero.
object:
  name: F_toy
  definition: "F(psi)_sigma = exp(gamma R_sigma(psi)) / ||exp(gamma R(psi))||_2"
  space: the probability simplex (real branch, gamma real)
hypotheses:
  - gamma real and strictly positive
  - A symmetric
  - h in R^N
  - beta swept across the flip eigenvalue crossing at -1
depends_on:
  - id: ce-toy-fixed-point-multiplicity
    role: context
    transfers: same-object
    justification: >
      Same object F_toy; explicitly not the same question. That dead
      speculation asked whether a SECOND fixed point of F exists at the
      cycling parameters (killed: exactly one root found by exhaustive
      root-finding). This asks whether a second stable ATTRACTOR (a cycle)
      can coexist with the unique fixed point in a finite parameter window -
      a bistability question the multiplicity search did not address, since
      it searched for additional roots of F, not additional attracting sets
      of the iteration.
  - id: ce-riem-classical-unique
    role: context
    transfers: same-object
    justification: >
      Same F_toy object at a different, unexplored sign of gamma; the
      uniqueness claim there is stated and evidenced only for the tested
      gamma = -1, -2 branch and does not cover gamma > 0.
falsifier: >
  Track the cycle amplitude near the flip crossing for several gamma > 0
  values; a continuous onset with amplitude growing as sqrt(beta - beta_flip)
  from exactly zero, matching the gamma = -1 supercritical result, or the
  absence of any beta-window where both the fixed point and a period-2 cycle
  are simultaneously stable under forward and backward beta sweeps, falsifies
  the subcritical claim.
consequence: >
  A subcritical transition would mean self-consistency selection is
  history-dependent (hysteretic) for attractive coupling: which configuration
  F_toy's iteration lands on would depend on initial conditions near the
  transition, not only on beta and gamma. That is a genuinely different
  selection-principle gap from the multiplicity question already closed
  (a second fixed point), and would matter for any argument that treats "the"
  self-consistent solution as the map's unique attractor rather than merely
  its unique fixed point.
provenance: {born: 2026-08-03, born_by: generator}
---

Every real-gamma instance in the record — [[ce-toy-fixed-point-multiplicity]],
[[ce-riem-classical-unique]], [[ce-second-iterate-real-spectrum]] — fixes
gamma at -1 or -2 (repulsive self-consistency weighting: R appears with a
negative sign in the exponent). The opposite-sign branch has not been swept in
any recorded instance. Bistability (coexisting fixed point and cycle) is a
structurally different failure mode from the multiplicity question the
generator already asked and lost: that speculation was about a second FIXED
point of F; this is about a second stable ATTRACTOR of the iteration, which a
uniqueness-of-fixed-points result does not by itself exclude.

Axiom check: purely an internal statement about the toy model's Riemannian
branch (gamma real, theta = 0); no background metric, foliation, or time
parameter is invoked — F_toy is a discrete self-map, and "history-dependence"
here means dependence on the iteration's starting point, not on any physical
time evolution. No axiom violation is apparent. Flagged honestly: if
subcritical, describing the outcome as "selection" already presupposes F_toy's
iteration is the relevant dynamical process picking out the physical
configuration, a reading the paper's own framing licenses but this claim does
not re-derive.
