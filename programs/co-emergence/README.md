# Co-Emergence of Mass, Signature, Time, and Hilbert Space

**Status:** Draft

## In plain English

Why does time exist, and why does quantum mechanics run on imaginary numbers?
This program studies a model where the universe is a single, static,
four-dimensional block — no built-in clock — and asks what structures it
*must* contain to be consistent with itself. The central finding so far: in a
small, exactly solvable model, self-consistency with a time-like (Lorentzian)
geometry forces the wavefunction to develop complex phases — the raw
ingredient of quantum interference — while a space-like (Riemannian) geometry
stays purely classical. Pieces of this are rigorously proven (for small
subsystems); much of the rest rests on extensive numerical evidence. The
headline thesis — that mass, time, geometry, and quantum mechanics emerge
together as a package — remains a conjecture, and is labeled as one.

Mass, Lorentzian signature, local time, and local Hilbert space are four aspects of one structure. None exists without the others. They co-emerge as the unique cross-level self-consistent configuration of a four-dimensional block manifold with no evolution parameter, no background structure, and no fundamental Hilbert space.

## Paper structure

The paper leads with proved results, then develops the interpretive framework:

- **Section 3 (Lorentzian phases and the entropy excess):** The mathematical core. The Lorentzian self-consistency map produces complex phases locked to magnitudes in the fixed-point wavefunction (~25–40% imaginary content, set by θ, the spread of h, the system size N, and the alignment convention — *not* by subsystem rank — via an exact reduction to the magnitude spectrum; stable through N=256), absent in the Riemannian case. The phase-induced lemma proves a purity decrease for all subsystem ranks and S_Lor > S_Riem for rank-2 subsystems (Rigorous), for any magnitude profile that is not multiplicatively separable across the bipartition; the general-rank von Neumann excess fails for extreme entry ratios and survives only as a bounded-ratio conjecture. A finite toy model confirms composition, Born rule, and imaginary subsystem coherences through N=16, with the full 68% entropy excess arising entirely from phase structure.

- **Section 4 (The co-emergence thesis):** The interpretive framework. Mass requires Lorentzian signature (Wigner); signature provides local time; local time enables local Hilbert space (Page-Wootters); Hilbert space closes the loop via stress-energy. The mass assumption is weakened: the conformal trace anomaly generates effective mass for non-conformally coupled fields (Conjecture 2).

- **Section 5 (The self-consistency hierarchy):** Four-level hierarchy (topological → smooth → metric → effective QM). Level 2 is signature-blind; signature selection operates at the cross-level constraint.

## Relationship to other programs

- **`fixed-point-existence`** — Companion paper. Provides the Level 2 anchor: Banach contraction for massive fields (Sketch — demoted from Rigorous, 2026-06), Starobinsky exact solution for conformal matter (Rigorous), Schauder existence (conditional). Results are cited, not re-derived.

- **`self-consistency-hierarchy`** (removed 2026-03, commit 782414f) — Previous version of this paper; the program directory no longer exists. The hierarchy framework originated there, and the co-emergence thesis emerged from its explorations (B1, C1, signature-mass debate, mass gap debate). Those explorations were restored from git history into this program's `explorations/` directory (2026-06), where they remain the research record for the results table below.

## Key results

| Result | Status | Source |
|--------|--------|--------|
| Phase-induced entropy excess (rank 2) | **Rigorous** | Lemma in paper; Lean scalar step verified (`lean/`, CE-5): binary-entropy monotonicity machine-checked; three structural links (spectral identification, S=Srank2(σ₁²), Fact 2) are explicit hypotheses, not re-derived |
| Phase-induced purity decrease (all ranks) | **Rigorous** | Lemma in paper / general-rank exploration; Lean-verified (`lean/`, CE-5) |
| Interference metric I_S = S(Re ρ) − S(ρ): zero iff ρ is real (in the smooth-structure basis) | **Rigorous** | Prop. in paper §3 |
| Toy model: composition, Born rule, interference (N=4–16) | **Rigorous** (numerical) | Toy model exploration |
| ψ* imaginary fraction = exact functional of Born spectrum and θ (eq. im_frac_reduction); ~25–40% (N-, h-, θ-, alignment-dependent, *not* rank-dependent), → analytic large-N limit, below Haar baseline | **Rigorous** (reduction) / **Rigorous** (numerical) | Imaginary-fraction exploration (2026-06-18) / scaling & mixed-dims studies |
| S_Lor/S_Riem ≈ 1.68, entirely from phases | **Rigorous** (numerical) | Scaling study |
| vN entropy excess (general rank) | **Refuted** in general (3×3 counterexample, extreme entry ratios); survives as bounded-entry-ratio Conjecture | General-rank exploration (100k+ moderate-ratio tests, 0 violations) |
| Level 2 is signature-blind (massive) | Sketch (underlying Banach contraction demoted 2026-06) | B1 exploration |
| Level 2 is signature-blind (massless) | Rigorous | Massless fixed-point exploration |
| Intersection form cannot force Lorentzian | Rigorous (obstruction) | C1 exploration |
| Self-consistent mass generation (ξ ≠ 1/6) | Sketch | Mass gap exploration |
| Co-emergence thesis | Conjecture | Paper Section 4 |

## Open problems

1. **Mass gap origin.** Where does mass come from? Conjecture 2 reduces the assumption from "massive fields" to "non-conformally coupled fields." Residual question: can ξ ≠ 1/6 be derived from Levels 0–1?

2. **Level 3 formalization.** The Born rule result is kinematic; the open question shifts from algebraic structure (confirmed) to dynamical aspects (unitary evolution, measurement). Reformulating Page-Wootters without a fundamental Hilbert space would promote co-emergence from Conjecture to Sketch.

3. **Level 0 manifold class.** Which 4-manifolds can be both Lorentzian and topologically rich? Closed simply-connected manifolds are obstructed (χ ≥ 3). Alternatives: non-compact (exotic R⁴), manifolds with boundary, non-simply-connected.

4. **Level 1 measure.** Natural measure on Sm(M) without metric input.

5. **Analytical open questions.** Why S_Lor/S_Riem ≈ 1.68? General rank proof of entropy excess lemma. (The imaginary fraction → 0.25 question is resolved: it numerically converges to ≈0.25 (opt-align) as N → ∞ with h ~ U[0.5,1.5]; the max-align large-N limit ≈0.40 is analytic via eq:im_frac_reduction.)

## Build

```bash
pdflatex index.tex
```
