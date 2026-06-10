# C1: Intersection Form to Metric Signature Bridge

**Date:** 2026-03-02
**Type:** Research exploration
**Outcome:** Negative result — the intersection form does not determine metric signature. Moreover, a fundamental topological obstruction prevents the manifolds where intersection forms are most powerful from admitting Lorentzian metrics at all.

---

## Question

Does an indefinite intersection form with signature $(1, b_2^-)$ on a smooth 4-manifold imply that compatible metrics must be Lorentzian? Can the Hirzebruch signature theorem $\sigma(\mathcal{M}) = \frac{1}{3}p_1(\mathcal{M})$ connect the intersection form to metric signature via Pontryagin classes?

## Finding

**No, and worse than expected.** There is not merely an absence of a theorem — there is an active obstruction.

### The Euler characteristic obstruction

A closed manifold $M^n$ admits a Lorentzian metric if and only if it admits a nowhere-vanishing vector field, which (by the Poincaré-Hopf theorem) holds if and only if $\chi(M) = 0$ (Geroch 1968, Steenrod 1951).

For a closed simply-connected 4-manifold with intersection form $Q$ of rank $b_2$:
$$\chi(M) = 2 + b_2$$
since $b_0 = b_4 = 1$, $b_1 = b_3 = 0$ (by simple connectivity and Poincaré duality).

Therefore $\chi(M) \geq 2$ for any closed simply-connected 4-manifold, and $\chi \geq 3$ whenever $Q$ is nontrivial ($b_2 \geq 1$).

**Consequence:** No closed simply-connected 4-manifold with a nontrivial intersection form admits a Lorentzian metric.

### Why this is devastating

The hierarchy paper's Level 0 relies on Freedman's classification (1982) and Donaldson's constraints (1983), which apply to closed simply-connected 4-manifolds. These are exactly the manifolds where:

- The intersection form classifies the homeomorphism type (Freedman)
- The intersection form constrains which smooth structures exist (Donaldson)
- Uncountably many exotic smooth structures live (Taubes 1987)

But these are also exactly the manifolds that **cannot be Lorentzian**. The machinery that makes the topological level powerful is incompatible with the metric-level requirement.

### Escape routes investigated

**1. Non-compact manifolds (exotic $\mathbb{R}^4$'s).** These have $\chi = 1$ (or can be arranged to have $\chi = 0$), so they can be Lorentzian. But $H_2(\mathbb{R}^4) = 0$, so the intersection form is trivial. The intersection form machinery simply does not apply.

**2. Manifolds with boundary.** Can have $\chi = 0$ and nontrivial $H_2$. But:
- Freedman's classification does not apply directly
- The intersection form is no longer unimodular (Poincaré duality fails for manifolds with boundary)
- Exotic smooth structure classification is much less developed

**3. Non-simply-connected manifolds.** Can have $\chi = 0$ with nontrivial topology (e.g., $T^4$ has $\chi = 0$). But:
- Freedman's classification requires $\pi_1 = 0$
- The intersection form does not classify the manifold
- The exotic smooth structure landscape is harder to characterize

**4. Pontryagin class / Hirzebruch route.** The Hirzebruch signature theorem $\sigma = \frac{1}{3}p_1$ connects the intersection form signature to a characteristic class of the tangent bundle. But characteristic classes are topological invariants — they cannot distinguish Riemannian from Lorentzian metrics on the same manifold. The tangent bundle $TM$ has the same Pontryagin classes regardless of the signature of the fiber metric.

### What the intersection form signature actually means

The intersection form signature $\sigma = b_2^+ - b_2^-$ is a topological invariant counting the difference between positive and negative eigenvalues of $Q$ on $H_2(M; \mathbb{Z})$. It constrains which smooth structures exist (Donaldson: a definite form on a smooth manifold must be diagonal). But it says nothing about the metric on the tangent spaces. The word "signature" is a coincidence of terminology, not a mathematical connection.

## Implication for the Gate Decision

C1 is negative. Combined with B1 (also negative), the Phase 2 gate decision is **outcome 3**: the hierarchy cannot derive Lorentzian signature from its current structure. Per the research plan:

> "Both fail: The hierarchy cannot derive Lorentzian signature. The paper must retreat to 'signature assumed' and flag this as the primary open problem. Level 0 is substantially revised."

## Possible Directions Forward

1. **Accept signature as an additional axiom.** Add "the manifold admits a Lorentzian metric" to Level 0. This is honest but weakens the topological program — the signature would not be derived from topology.

2. **Shift to non-compact or bounded manifolds.** Abandon the closed simply-connected setting. Work with manifolds with boundary or non-compact manifolds where Lorentzian metrics exist. This sacrifices the Freedman classification and most of the intersection form machinery. It may require entirely different topological tools.

3. **Wheeler's biconformal gauging.** (From B1 ancillary finding.) Wheeler showed that gauging SO(4,2) on Euclidean space produces Lorentzian signature on submanifolds. This is a conformal-geometric mechanism, not a topological one. It would need to be integrated with the hierarchy at a different level. [UNVERIFIED — needs paper-grade verification.]

4. **Cobordism / manifolds-with-corners approach.** Instead of a single closed 4-manifold, the physical spacetime could be a cobordism between 3-manifolds. Cobordisms naturally have $\chi = 0$ possible (e.g., a cylinder $\Sigma \times [0,1]$ has $\chi = 0$ when $\chi(\Sigma) = 0$). The exotic smooth structure program extends to cobordisms in interesting ways.

5. **Reformulate Level 0 entirely.** The intersection form may not be the right topological invariant for constraining the hierarchy. Other candidates: surgery-theoretic invariants, homotopy type, fundamental group structure.

## References (exploratory, unverified unless noted)

- Geroch (1968), "Spinor structure of space-times in general relativity, I," J. Math. Phys. 9, 1739. [unverified]
- Steenrod (1951), "The Topology of Fibre Bundles," Princeton. [unverified]
- Freedman (1982), J. Differential Geometry 17, 357. [verified — see MEMORY.md]
- Donaldson (1983), J. Differential Geometry 18, 279. [verified — see MEMORY.md]
- Taubes (1987), J. Differential Geometry 25, 363. [verified — see MEMORY.md]
- Hirzebruch (1966), "Topological Methods in Algebraic Geometry," Springer. [unverified]
