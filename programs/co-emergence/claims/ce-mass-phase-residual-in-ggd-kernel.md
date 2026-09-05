---
id: ce-mass-phase-residual-in-ggd-kernel
program: co-emergence
tier: speculation
status: live
statement: >
  Because mass requires Lorentzian signature (ce-mass-signature) and Lorentzian
  signature carries the complex self-consistency phase theta (the CE-10
  theta-signature identification), a genuinely massive two-branch superposition
  cannot supply the gaussian-gravitational-decoherence noise kernel
  N_0000(x, x') exactly as the real bilinear (c^4/4) Delta_rho(x) Delta_rho(x')
  that ggd-noise-kernel derives: writing each branch's expected stress-energy
  with its self-consistency-weight phase factor explicit produces a residual
  term of order sin(theta) that survives in N_0000 for any pair of branches
  whose co-emergence phases differ, vanishing only in the theta -> 0
  (Riemannian, hence per ce-mass-signature formally massless) limit.
object:
  name: N_0000(x, x'), decomposed via each branch's self-consistency phase theta
  space: expectation values of the stress-energy operator T00 over the two branches entering the Einstein-Langevin analysis
hypotheses:
  - each branch is a genuinely massive configuration (Lorentzian per ce-mass-signature)
  - a curved, dynamical, generically symmetry-free 4-manifold
  - each branch's co-emergence phase theta is well defined and, in general, differs between the two branches
  - non-relativistic stress-energy operator T00 = c^2 rho(x - X_CM)
  - orthogonal branches
  - each branch has definite centre-of-mass position
depends_on:
  - id: ce-mass-signature
    role: load-bearing
    transfers: cross-object
    justification: >
      Different object (a particle-classification argument on a curved
      manifold vs. an expectation-value calculation on branch densities); the
      claim borrowed is the identification mass <-> Lorentzian signature, not
      any structure of the mass-shell argument itself. Note this dependency
      currently carries an audit verdict of "demote" (Wigner's flat-space
      classification applied to a curved, generically symmetry-free
      manifold); this speculation is exposed to that same gap and does not
      independently repair it.
  - id: ggd-noise-kernel
    role: load-bearing
    transfers: cross-object
    justification: >
      Different object (a semiclassical stress-energy expectation-value
      identity vs. this speculation's proposed phase-dependent correction to
      it); the two formalisms have never been checked for mutual consistency
      across the program boundary, which is exactly what this speculation
      tests.
falsifier: >
  Recompute N_0000 keeping the self-consistency phase explicit in each
  branch's T00 expectation value (writing the branch amplitude with its
  e^{i theta} weight factor rather than treating Delta_rho as a real classical
  density difference from the outset). Expectation values of a Hermitian
  operator in any physical state are real by construction; if the phase
  factors cancel identically for exactly this reason, with no residual
  sin(theta) surviving in N_0000 to any order, the speculation is falsified
  outright.
consequence: >
  If a real residual term survives, GGD's noise kernel is incomplete for any
  branch pair with differing co-emergence phase, predicting an additional
  decoherence channel set by theta rather than by Delta_rho alone -
  potentially discriminating from Delta_rho-only. If the residual does not
  survive (the more likely outcome a priori, given that T00 expectation
  values are manifestly real), this would be the first explicit check that
  co-emergence's mass/signature construction and GGD's stress-energy
  construction are mutually consistent where they overlap - a cross-program
  consistency question neither program's record currently addresses.
provenance: {born: 2026-08-03, born_by: generator}
---

A cross-program consequence: no existing claim connects co-emergence's
mass-signature identification to gaussian-gravitational-decoherence's noise
kernel, and the two frameworks have never been checked against each other at
the point where they should overlap - both concern the stress-energy content
of a massive superposition.

Axiom check, stated honestly rather than resolved: combining the two
requires specifying at what point in "time" theta is evaluated, since GGD's
T00 expectation value is defined at a Schrödinger-picture instant on a fixed
background time slice, while co-emergence's theta is a property of a
self-consistent FIXED POINT of a timeless map, not of a state's evolution.
Treating "the branch's theta at the moment N_0000 is evaluated" as
well-defined risks smuggling a preferred-time identification between GGD's t
and co-emergence's fixed-point locus that neither program's axioms license.
This is flagged as a genuine hole in how the two objects would even be
compared, not resolved here - a speculation that violates an axiom in its own
construction is still worth proposing, per the generator's own criteria,
provided the violation is named rather than hidden.
