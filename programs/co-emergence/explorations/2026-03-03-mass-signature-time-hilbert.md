# Exploration: Mass, Signature, Time, and Hilbert Space as Co-Emergent

**Date:** 2026-03-03
**Type:** Conceptual synthesis
**Outcome:** A unified reframing of the signature problem. Mass, Lorentzian signature, local time, and local Hilbert space are four aspects of a single structure that emerges from cross-level self-consistency.

---

## Observations

Three established facts and one conjecture motivate this synthesis.

### 1. Mass is the common feature of GR and QFT

In GR, mass-energy is the source of curvature: $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$. In QFT, mass defines the spectrum: massive particles are irreducible representations of the Poincaré group with $p^2 = -m^2$ (Wigner 1939). Mass is the one concept that appears in both theories with the same physical meaning. It is the bridge.

### 2. Massive and massless particles have fundamentally different geodesics

- **Massive particles** follow timelike geodesics. They experience proper time $d\tau^2 = -g_{\mu\nu} dx^\mu dx^\nu > 0$.
- **Massless particles** follow null geodesics. Proper time along a null geodesic is zero.

This is not interpretation. It is the geodesic equation applied to the two cases. The distinction between timelike and null IS the Lorentzian signature. On a Riemannian manifold, all geodesics have the same character — there is no timelike/null/spacelike trichotomy.

### 3. GR prohibits universal time evolution

General relativity proves there is no universal time parameter. Clocks at different locations in a gravitational field tick at different rates (gravitational time dilation, experimentally confirmed). Any formulation that reintroduces a universal clock contradicts established physics (FRAMEWORK.md, Axiom 2).

But mass provides **local** time. A massive particle carries a clock: its proper time along its worldline. This is not universal — it is worldline-dependent, local, and exists only for massive objects. Massless particles do not carry clocks.

### 4. Hilbert space is not fundamental (Conjecture)

The Hilbert space formalism depends on a time parameter:
- The Schrödinger equation $i\hbar\, \partial|\psi\rangle/\partial t = H|\psi\rangle$ requires $t$.
- The inner product $\langle\psi|\phi\rangle$ is defined on a spatial slice at fixed $t$.
- Unitarity ($\langle\psi(t)|\phi(t)\rangle = \langle\psi(0)|\phi(0)\rangle$) requires a preferred foliation.

If there is no universal time (observation 3), there is no universal Hilbert space. But if mass provides local time (observation 2 + 3), then a local Hilbert space exists for massive subsystems — subsystems that carry their own clocks.

---

## The co-emergence thesis

These four concepts are not independent. They are a single structure seen from four angles:

$$\text{mass} \;\longleftrightarrow\; \text{Lorentzian signature} \;\longleftrightarrow\; \text{local time} \;\longleftrightarrow\; \text{local Hilbert space}$$

Each requires the others:

- **Without mass:** No timelike geodesics → no proper time → no local clocks → no Hilbert space formalism. The conformal structure (null cones) exists, but the full metric is undetermined within its conformal class. The signature distinction is meaningless — there is nothing to distinguish "timelike" from "spacelike."

- **Without Lorentzian signature:** No timelike/null/spacelike trichotomy → the parameter $m^2$ in the field equation $(\Delta + m^2)\phi = 0$ shifts the Laplacian spectrum but does not define a mass shell, a dispersion relation, or propagating degrees of freedom. The parameter exists; the physics does not.

- **Without local time:** No $\partial/\partial t$ → no Schrödinger equation → no unitary evolution → no Hilbert space. This is not a deficiency to be repaired; it is the correct description at the fundamental level (Axiom 2).

- **Without Hilbert space:** No quantum mechanics for subsystems → no $\langle\hat{T}_{\mu\nu}\rangle$ → no self-consistent semiclassical gravity. Level 2 of the hierarchy requires an effective quantum theory to source the Einstein equation.

The circle closes: mass → signature → time → Hilbert space → $\langle T_{\mu\nu}\rangle$ → gravity → mass.

---

## Implications for the hierarchy

### The signature problem dissolves into the mass problem

The hierarchy doesn't have four independent open problems (signature, measure, marginalization, Hilbert space). It has **one**: where does mass come from? If the self-consistency constraints at Levels 0–1 generate field content with a mass gap, everything else follows:

- Mass gap → hyperbolicity of the wave operator → Lorentzian signature (the only signature that supports propagation on a mass shell)
- Mass → timelike geodesics → local proper time (local clocks for massive subsystems)
- Local proper time → local Hilbert space (the Schrödinger formalism applies for subsystems with clocks)
- Local Hilbert space → $\langle\hat{T}_{\mu\nu}\rangle$ → Level 2 SCE fixed point (already established, Rigorous)

### The Riemannian fixed point fails at Level 3, not Level 2

The Banach contraction analysis (B1 result, confirmed in this session) shows that the contraction constant $\kappa \sim (m/M_P)^2$ is the same on both Riemannian and Lorentzian manifolds. The self-consistency map has fixed points on both signatures. This is not a bug — it is informative.

The Riemannian fixed point passes Level 2 (the SCE is satisfied) but fails Level 3: there are no timelike geodesics, no proper time, no local clocks, and therefore no local Hilbert space. The marginalization of the smooth-structure measure cannot produce a density matrix because there is no time parameter to define the Hilbert space it would act on.

Signature is selected not by any single level, but by the requirement that **all levels be simultaneously consistent** — precisely the content of Axiom 1.

### Levels are resolutions, not stages

This must be stated with emphasis because the co-emergence thesis is especially vulnerable to the "temporal stages" misreading (FRAMEWORK.md warning). The statement "mass gap → Lorentzian signature → local time → local Hilbert space" reads as a causal chain. It is not. These are simultaneous aspects of the self-consistent block, expressed in the only order available to linear text.

The block does not first acquire a mass gap, then a signature, then time, then quantum mechanics. It satisfies all constraints at all levels at once. The chain is our explanation, not its construction.

---

## What this does NOT solve

1. **The mass gap origin.** Where does mass come from? This is now the single most important open problem. The Asselmeyer-Maluga program (exotic smooth structures generating gravitational sources and fermion fields from pure topology) is the closest prior art but is unverified. Without a mechanism for the mass gap, the co-emergence thesis is a conditional: IF mass, THEN everything else.

2. **The marginalization conjecture.** Even granting local Hilbert spaces for massive subsystems, the mathematical mechanism by which marginalizing $\mu^*$ produces a density matrix is unspecified.

3. **Vacuous circle vs productive fixed point.** The co-emergence of mass, signature, time, and Hilbert space is presented as a fixed point. But not every circle is a productive fixed point. The difference is whether the coupled system has nontrivial solutions accessible by iteration (Conjecture 1.1). The existence of the physical universe proves a solution exists. The hierarchy's constraints must be shown to select it.

---

## Rigor assessment

- **Observations 1–3:** Rigorous. These are established physics/mathematics.
- **Conjecture (observation 4):** Conjecture. The claim that Hilbert space is emergent is well-motivated but unproven. The Page-Wootters mechanism provides a partial model; the full marginalization conjecture is open.
- **Co-emergence thesis:** Conjecture. The connections are individually established, but the claim that they form a self-selecting fixed point is not proven. The conditional form ("IF mass gap THEN the rest follows") is at the Sketch level; the unconditional form is Conjecture.
- **Riemannian failure at Level 3:** Sketch. The argument that Riemannian fixed points cannot support Level 3 is plausible and structurally sound, but the marginalization conjecture at Level 3 is not sufficiently developed to make this rigorous.

---

## Relationship to prior explorations

- **B1 (negative):** Level 2 does not distinguish signatures → confirmed by Banach contraction analysis. The co-emergence thesis explains WHY: the signature selection operates at the cross-level constraint, not at Level 2 alone.
- **C1 (negative):** Intersection form does not force Lorentzian signature → the co-emergence thesis abandons the direct topological route. The signature bridge passes through mass, not through the intersection form.
- **Signature-mass codependence debate:** The co-emergence thesis subsumes and sharpens the debate's joint fixed-point conjecture. Position 3's "nontrivial fixed points only for Lorentzian" becomes "Level 3 consistency only for Lorentzian," which is a more precise claim.

---

## Concrete next steps

1. **Verify the Asselmeyer-Maluga program.** Does exotic smooth structure on $\mathbb{R}^4$ generate massive field content? This is the critical antecedent. Paper-grade citation verification required.

2. **Formalize the Level 3 failure for Riemannian signature.** State precisely what "local Hilbert space requires local time" means mathematically. Can the Page-Wootters mechanism be adapted to show that conditioning on a massive clock subsystem requires Lorentzian signature?

3. **Rewrite Section 8 of the hierarchy paper.** Replace the intersection form → metric signature conjecture with the co-emergence thesis. State the Signature Selection Principle as: nontrivial cross-level self-consistency requires Lorentzian signature with $m > 0$.
