---
id: ce-toy-fixed-point-multiplicity
program: co-emergence
tier: speculation
status: dead
statement: >
  In the parameter regime where F's iteration settles into a period-2 limit
  cycle, F possesses at least two distinct fixed points exchanged by the same Z2
  structure generating the cycle - so non-convergence reflects genuine
  multiplicity of self-consistent solutions rather than one unstable solution.
object:
  name: F_toy
  definition: "F(psi)_sigma = exp(gamma R_sigma(psi)) / ||exp(gamma R(psi))||_2"
  space: C^N
hypotheses:
  - gamma in R
  - h in R^N
  - the cycling regime, beta >~ 5-10 and |gamma| >~ 2
falsifier: >
  Non-iterative root-finding in the cycling regime. Finding exactly one fixed
  point falsifies multiplicity.
consequence: >
  Would have shown self-consistency alone does not select a unique universe at
  those parameters, requiring an additional principle.
provenance: {born: 2026-07-24, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-24
  cause: >
    Conflation of fixed points of F with fixed points of F composed with itself.
    The cycle points satisfy F(a) = b and F(b) = a but ||F(a) - a|| = 1.14 - they
    are period-2 points, not fixed points. Direct root-finding then found exactly
    ONE fixed point of F across ~1800 multistart Newton solves plus homotopy
    continuation from the known-unique branch with no fold en route. The actual
    mechanism is a flip (period-doubling) bifurcation of that unique fixed point,
    with a real eigenvalue crossing -1 at beta ~ 0.698.
  defense_attempted: yes
  defense_findings: >
    The defense extended the search two further orders of magnitude in beta
    (500, 2000, 10000): always exactly one root, converging to the uniform point
    as beta grows, matching the analytic expectation. It confirmed no exact Z2
    symmetry exists (23/23 permutations fail) and added a topological argument
    excluding the claimed structure independently of any search.
  no_narrowed_form: >
    Explicitly none. A narrowed version would only restate S3's negation.
---

Killed, and it was the most productive of the five. Its investigation produced
[[ce-self-consistency-real-spectrum]], strengthened [[ce-riem-classical-unique]]
with a Lefschetz index argument and a much wider search, and closed the audit's
open beta=160 conditioning item.
