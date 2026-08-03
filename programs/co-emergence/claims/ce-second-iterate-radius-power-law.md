---
id: ce-second-iterate-radius-power-law
program: co-emergence
tier: speculation
status: live
statement: >
  The second-iterate spectral radius rho_2(beta) of D(G o G) at the F_toy
  attracting fixed point decays as a power law rho_2(beta) ~ C beta^{-1} for
  beta well past the flip onset, with C independent of N, driven by the
  Jacobian's spectral weight concentrating onto a single direction aligned
  with the dominant softmax component as the fixed point sharpens toward a
  simplex vertex.
object:
  name: D(G o G)
  definition: "D(G o G)(a) = S(e) M S(b) M, with S(p) = diag(p) - p p^T, b = G(a), e = G(b)"
  space: tangent space of the probability simplex
hypotheses:
  - gamma real
  - gamma = -1
  - the marginal-coupling matrix A symmetric
  - the softmax form induced by the self-consistency weight
  - beta swept at least two orders of magnitude past the flip onset
  - h in R^N
depends_on:
  - id: ce-second-iterate-real-spectrum
    role: load-bearing
    transfers: same-object
    justification: >
      Same object, D(G o G); this speculation proposes a specific rate for the
      decay that claim's own gaps field records as unexplained ("does not
      explain WHY the second-iterate spectral radius decays to ~0.037 rather
      than merely staying below 1").
falsifier: >
  Fit log(rho_2(beta)) against log(beta) across at least two decades of beta at
  several N; a fitted exponent that is not close to -1 (say outside
  [-1.3, -0.7]), or that drifts systematically with N, falsifies the power law
  as stated. The recorded data point rho_2 ~ 0.037 near beta ~ 50 is a single
  sample and does not by itself confirm or refute a specific exponent.
consequence: >
  A clean inverse-beta law would give the missing mechanism the parent claim
  flags as absent (the failed Rayleigh-quotient bound diverges instead), and
  would let ce-riem-classical-unique's bound on the exact-to-bound contraction
  ratio be re-derived analytically rather than only observed to fall to
  1e-310 at large beta. A non-power-law or N-dependent exponent would instead
  show the decay is not a single universal mechanism, narrowing what
  ce-second-iterate-real-spectrum's palindrome argument can be said to explain.
provenance: {born: 2026-08-03, born_by: generator}
---

Mined from [[ce-second-iterate-real-spectrum]]'s own gaps field and the
Rayleigh-quotient failure recorded on [[ce-riem-classical-unique]] ("the bound
diverges... because the smallest eigenvalue of S(e) tends to zero as the cycle
concentrates near a simplex vertex"). That failure is itself evidence for the
concentration mechanism proposed here, but a divergent bound is not a
convergent rate, and no exponent has been fit.

Axiom check: this is a purely internal statement about the toy model's
Jacobian at gamma real (Riemannian branch, theta = 0); it does not invoke a
background metric, a preferred foliation, or unitary time evolution — F_toy is
iterated as a discrete self-map with no time parameter involved. No axiom
appears to be smuggled. The one honesty flag: "concentrating near a simplex
vertex" describes the *attracting* orbit's location, which is itself an
empirical fact about this map (not assumed here), carried over unchanged from
the parent claim's evidence record.
