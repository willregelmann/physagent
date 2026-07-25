---
id: ce-riem-classical-unique
program: co-emergence
tier: sketch
status: live
statement: >
  The self-consistency fixed point psi* is unique in (C^N, ||.||_2). Open: no
  independent contraction argument for F on C^N has been supplied.
object:
  name: F_toy
  definition: "F(psi)_sigma = exp(gamma R_sigma(psi)) / ||exp(gamma R(psi))||_2"
  space: C^N
hypotheses:
  - gamma in R
  - h in R^N
depends_on:
  - id: fpe-banach-contraction
    role: context
    transfers: cross-object
    justification: >
      Explicitly does NOT transfer. The companion result is a contraction for
      the field-theoretic semiclassical Einstein equation on manifolds with
      compact Cauchy surfaces, governed by a causal-past Green-operator kernel
      bound - a different map on a different space. Recorded as context so the
      non-transfer is part of the record, never as support.
falsifier: two distinct fixed points of F for the same parameters
consequence: >
  Uniqueness is not needed for the classicality result; only for statements
  about "the" fixed point.
novelty: {status: unchecked}
tex: {file: programs/co-emergence/index.tex, label: prop:riem_classical}
provenance: {born: 2026-07-18, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    The Sketch label is correct and the non-transfer statement is accurate.
    Independently validated by numerics: F is demonstrably NOT a global
    contraction at this generality - for beta >= ~5-10 with |gamma| >= 2 the
    local Lipschitz ratio exceeds 1 and fixed-point iteration settles into an
    exact period-2 limit cycle (beta = 40, gamma = -2). At the paper's actual
    tested parameters (beta = 0.4, gamma = -1) the worst-case ratio over 3000
    adversarial samples was ~0.21. Independent root-finding located only one
    fixed point wherever it succeeded - no counterexample to uniqueness itself.
    Had the paper claimed a general contraction, that claim would be FALSE.
evidence:
  - date: 2026-07-24
    by: adversary
    kind: numerical
    finding: >
      Exactly one fixed point of F found across ~1800 multistart Newton solves
      plus homotopy continuation from the known-unique low-parameter branch with
      no fold en route, extended to beta = 500, 2000 and 10000: always exactly
      one root, converging to the uniform point as beta grows, matching the
      analytic expectation. The period-2 cycling is a flip bifurcation of that
      single fixed point, with a real eigenvalue crossing -1 at beta ~ 0.698 -
      not evidence of a second solution. No exact permutation symmetry of F
      exists (23 of 23 tested fail).
  - date: 2026-07-24
    by: adversary
    kind: topological
    finding: >
      A proof-shaped partial result. The simplex is compact, convex and
      contractible and F maps it into its strict interior, so by Lefschetz-Hopf
      any continuous self-map has Lefschetz number 1 and the local indices of
      isolated non-degenerate fixed points sum to 1. The located fixed point has
      det(I - DG) = 71540 > 0, hence index +1, saturating the sum. A second fixed
      point related to the first by an exact symmetry would share its index by
      similarity, forcing the total to at least 2 and contradicting the
      constraint. This excludes a symmetric exchanged pair without any search.
proof_attempts_failed:
  - route: global Euclidean operator-norm bound
    result: >
      Softmax-Jacobian operator norm is exactly 1/2, achieved at boundary points.
      The criterion gives 1.34 even at beta = 0.4, gamma = -1 - the branch where
      the empirical Lipschitz ratio is ~0.21. Generic worst-case linear algebra
      provably cannot see the real mechanism.
  - route: invariant sub-region refinement
    result: still 1.34; the vertex-based lower bound is too conservative.
  - route: Hilbert projective metric
    result: >
      Yielded an exact identity worth keeping on its own -
      d_H(G(q1), G(q2)) = range(M(q1 - q2)), verified to 2e-15. But adversarial
      near-boundary search breaks the self-contraction badly and increasingly
      with beta: 1.20 at beta = 0.4, 2.80 at 2, 81 at 40, 321 at 160.
routes_unexplored:
  - Dobrushin-type coefficient of ergodicity exploiting A's actual sparsity rather than spectral norms
  - certified interval-arithmetic enumeration of roots, plausible at N = 4
  - Nussbaum-type nonlinear Perron-Frobenius on G composed with itself, which is isotone
---

The audit's verdict on the honesty of this label: *"it explicitly leaves this
open, which my numerics validate as the correct call."*

**Substantially better evidenced as of 2026-07-24, tier unchanged.** Still
Sketch — none of the three analytic routes closes, and numerical evidence is not
a proof. But the falsifier is now sharpened (a second root anywhere across
beta in [0.1, 10000] and gamma in [-5, -0.5], searched and not found in ~3000
solves), and the Lefschetz argument rules out the specific symmetric-pair
structure without sampling at all.

**An open item in the audit record is now closed.** The audit reported
root-finding failing from all seeds at beta = 160 and logged it as inconclusive
numerical conditioning. It was a float64 overflow artifact of the raw
exp(gamma R) representation; reducing to q = |psi|^2 makes F a well-conditioned
softmax map on the simplex, which converges and finds exactly one root. Nothing
was happening to the solution structure.

All of this came from the adversarial investigation of
[[ce-toy-fixed-point-multiplicity]], a speculation that was false.
