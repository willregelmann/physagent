---
id: fpe-banach-contraction
program: fixed-point-existence
tier: sketch
status: live
statement: >
  The semiclassical Einstein equation admits a Banach contraction on field
  configurations, giving existence and uniqueness of a self-consistent metric
  perturbation with contraction constant kappa ~ (m/M_P)^2.
object:
  name: SCE_map
  definition: metric perturbations sourced by the semiclassical Einstein equation
  space: field configurations on a manifold with compact Cauchy surfaces
hypotheses:
  - m > 0
  - compact Cauchy surfaces
  - a Green-operator kernel bound in the stated norm
falsifier: an explicit non-contractive configuration in the stated norm
consequence: self-consistent solutions exist perturbatively and are unique
novelty: {status: unchecked}
tex: {file: programs/fixed-point-existence/index.tex, label: sec:banach}
provenance: {born: 2026-03-04, born_by: human}
rigor_ceiling:
  tier: sketch
  reason: >
    Permanently Sketch at this generality. Gap M3 is a structural obstruction:
    the Lorentzian hyperbolic Green operator has causal-past support, and any
    repair requires a global foliation beyond axioms A1-A6, which makes the
    result foliation-restricted rather than general. Documented rather than
    repaired (FPE-4, Outcome B, PR #109).
---

**This node is the reason the graph exists.** It is Sketch, permanently, and it
is about a *different map on a different space* from the finite-dimensional
`F_toy` used in co-emergence. Before PR #162, `co-emergence` asserted a Rigorous
uniqueness claim on the strength of this result - a tier inversion and a
cross-object transfer in a single edge. Both are now lint errors (L1, L2).

Demoting or restricting this claim lights up every dependent automatically; that
sweep is what milestone CE-13 did by hand, weeks after the fact.
