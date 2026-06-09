The semiclassical Einstein equation admits self-consistent solutions exactly via the Starobinsky trace-anomaly fixed point, and conditionally via Schauder on globally hyperbolic spacetimes with compact Cauchy surfaces. A perturbative Banach-contraction argument targeting kappa ~ (m/M_P)^2 for massive fields is at Sketch level: its earlier Rigorous label was withdrawn after review identified gaps in the kernel bound and contraction estimate. An earlier claim that the Planck scale emerges as the validity boundary is withdrawn pending a corrected estimate.

# Fixed-Point Existence of Self-Consistent Semiclassical Gravity

**Status:** Pre-submission draft

## In plain English

Einstein's equations say matter tells spacetime how to curve. Quantum
mechanics says matter is fuzzy — it has no single definite arrangement.
"Semiclassical gravity" is the proposal that spacetime curves in response to
the *average* of that fuzziness, with no need to quantize gravity itself.
Critics have long suspected this picture is not even self-consistent. This
paper argues that it is: there exist geometries that exactly reproduce
themselves — the curvature sourced by quantum matter living on the geometry
is that same geometry. The result is exact in a known cosmological example
(Starobinsky), and conditional in the most general case (one assumption
remains open). The argument for geometries near ordinary classical spacetimes
with massive particles was previously claimed to be airtight; a review found
specific holes in that proof, so it is now honestly labeled a sketch — the
strategy is laid out, but several steps remain to be filled in. An earlier
claim that the theory's breakdown scale (the Planck scale) could be *derived*
from the mathematics has been withdrawn: the formula behind it contains an
error, and fixing it is open work. Massless particles such as light are not
yet covered. None of this says nature actually works this way — only that
the framework's internal coherence is partly established and partly open.

## Results

1. **Exact (Starobinsky, 1980).** The trace anomaly on FRW spacetime yields an exact de Sitter fixed point. The de Sitter stage is unstable (its decay is the graceful-exit mechanism); only existence is used here. An earlier "stable attractor" claim misstated the source and has been corrected. **(Rigorous)**
2. **Perturbative (Banach contraction).** Near classical solutions admitting a compact Cauchy surface, with massive fields, a contraction argument targets constant kappa ~ (m/M_P)^2 << 1 via a Hadamard decomposition of the response kernel. **(Sketch — demoted from Rigorous, 2026-06).** Identified gaps: (M1) dimensional inconsistency in the kappa chain (the derivation gives kappa ∝ 1/R while the displayed formula gives kappa ∝ R); (M3) the non-local kernel bound substitutes a spatial elliptic resolvent for the Lorentzian (hyperbolic) variation problem; (M4) the local coefficient scaling ħm² is asserted, not derived, and fails for mass-independent anomaly counterterms; (M5) the Banach self-mapping step is missing.
3. **Non-perturbative (Schauder).** On globally hyperbolic spacetimes with compact Cauchy surfaces, the Schauder fixed-point theorem guarantees existence under six assumptions, five established and one conjectural (uniform stress-energy bound). **(Conditional on A3)** — the written proof additionally has two flagged repairable gaps (M6: the fixed-point set is not closed/convex as defined; M7: the radius-selection argument is incorrect).

The previously claimed derivation of the Planck scale as the framework's validity boundary is withdrawn (it contradicted the paper's own kappa formula either way; see Section 7 of the paper). The massless case (photons, gluons) remains open — the exponential decay invoked for the non-local kernel bound requires m > 0.

## Explorations

- `explorations/2026-03-02-A1-Hs-bound-derivation.md` -- Hadamard-decomposition derivation of the H^s operator-norm bound for Lemma 1 (promoted Sketch → Rigorous in PR #26; **verdict withdrawn 2026-06**, see status note in the file — the record is retained per METHODOLOGY.md).

## Relationship to other programs

This paper is the Level 2 anchor for the self-consistency hierarchy / co-emergence program. **Note (2026-06): the Banach contraction that co-emergence cites as its rigorous Level 2 anchor is now Sketch, not Rigorous** — co-emergence claims that lean on it should be checked (METHODOLOGY.md issue relations: this demotion *informs* co-emergence). The signature-blindness observation (the contraction argument works on both Lorentzian and Riemannian manifolds) survives at Sketch level.

## Build

```bash
pdflatex index.tex
```
