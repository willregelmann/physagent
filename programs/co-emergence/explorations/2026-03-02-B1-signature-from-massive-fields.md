# B1: Lorentzian Signature from Massive Field Content

**Date:** 2026-03-02
**Issue:** #6
**Type:** Research exploration
**Outcome:** Negative result — Level 2 self-consistency does not distinguish metric signatures

---

## Question

Does the self-consistency fixed point of the SCE *require* Lorentzian signature when the field content includes massive fields? Specifically, does the Banach contraction fail on a Riemannian manifold?

## Finding

**No.** The Banach contraction argument carries over to Riemannian manifolds with the same scaling $\kappa \sim (m/M_P)^2 \ll 1$. Every ingredient in the proof has a Riemannian analogue that is mathematically simpler:

- Hyperbolic field equation → elliptic (all eigenvalues positive, unique vacuum)
- Hadamard state selection → automatic (no ambiguity)
- Global hyperbolicity + Cauchy surface → compact manifold (no causal structure needed)
- Hadamard parametrix → Seeley-DeWitt expansion (same structure)

The renormalization toolkit on Riemannian manifolds is well-established (Vassilevich 2003, Birrell-Davies 1982). The trace anomaly has the same form. The mass gap controls non-local kernel decay identically. The SCE has self-consistent solutions on both Lorentzian and Riemannian manifolds.

## Implication for the Gate Decision

B1 is negative. Level 2 self-consistency does not distinguish signatures. Signature must be derived at Level 0 (topology) or via a mechanism outside the current hierarchy.

This does not kill the program — it narrows the search. Per the research plan gate decision, the program survives if C1 succeeds (intersection form → signature bridge).

## Ancillary Finding: Wheeler's Biconformal Gauging

James T. Wheeler (Utah State) has shown rigorously that gauging SO(4,2) on Euclidean space produces Lorentzian signature on submanifolds (arXiv:1808.07083, 0811.0112). The mechanism: quotient the conformal group by the Weyl subgroup, identify orthogonal Lagrangian submanifolds, and these automatically acquire Lorentzian metric. This is a geometric theorem, not a physical argument. It offers a potential alternative mechanism for signature emergence that may connect to the topological level. [UNVERIFIED — Wheeler references need paper-grade verification before citation in .tex files.]

## References (exploratory, unverified unless noted)

- Vassilevich (2003), "Heat kernel expansion: user's manual," Physics Reports 388, 279. [unverified]
- Birrell & Davies (1982), "Quantum Fields in Curved Space," Cambridge. [unverified]
- Wheeler (2018), arXiv:1808.07083. [unverified]
- Wheeler (2008), arXiv:0811.0112, "The existence of time." [unverified]
