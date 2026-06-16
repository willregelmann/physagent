The semiclassical Einstein equation admits self-consistent solutions exactly via the Starobinsky trace-anomaly fixed point, and conditionally via Schauder on globally hyperbolic spacetimes with compact Cauchy surfaces. A perturbative Banach-contraction argument targeting kappa ~ (m/M_P)^2 for massive fields is **permanently at Sketch level at the stated generality**: its earlier Rigorous label was withdrawn after review identified gaps in the kernel bound and contraction estimate, and the governing gap (M3) is now established to be a structural obstruction — the response kernel is a Lorentzian hyperbolic Green operator with causal-past support, and reducing it to a single-Cauchy-surface bound requires a controlled global foliation beyond the proof's assumptions, so any repair is foliation-restricted. This does not refute existence (exact on de Sitter; FLRW via Meda–Pinamonti–Siemssen). An earlier claim that the Planck scale emerges as the validity boundary is withdrawn; the dimensional inconsistency behind it is now diagnosed as a hidden-reference-scale artifact: the corrected single-scale form kappa ~ (m/M_P)^2 is R-independent on the defensible reading (schematic — net scale tied to the joint M1+M4 repair), so no breakdown curvature is derived on that reading.

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
specific holes, so it is now honestly labeled a sketch. A closer look has now
shown that one of those holes is not a missing step but a genuine wall: the
quantum matter's response to a ripple in spacetime spreads along light cones —
it is a fundamentally spacetime, time-ordered effect — whereas the proof tried
to control it as if it lived on a single snapshot of space. Bridging that gap
needs an extra ingredient (a chosen slicing of spacetime into moments of time)
that the proof's assumptions do not provide, so the argument can only be rescued
in a form that is tied to such a slicing. This does *not* mean self-consistent
spacetimes fail to exist — they provably exist in the known cosmological example
and in expanding universes; it means this particular general proof strategy
cannot be made airtight without that extra ingredient. The separate claim that
the theory's breakdown scale (the Planck scale) could be *derived* from the
mathematics stays withdrawn: the formula behind it mixed up two different
reference scales, and once that is fixed the contraction strength appears not to depend
on curvature on the defensible single-scale reading (schematically — the net scale
is tied to the joint M1+M4 treatment), so no breakdown curvature is derived on
that reading. Massless particles such as
light hit the same wall. None of this says nature actually works this way — only
that the framework's internal coherence is partly established and partly walled
off.

## Results

1. **Exact (Starobinsky, 1980).** The trace anomaly on FRW spacetime yields an exact de Sitter fixed point. The de Sitter stage is unstable (its decay is the graceful-exit mechanism); only existence is used here. An earlier "stable attractor" claim misstated the source and has been corrected. **(Rigorous)**
2. **Perturbative (Banach contraction).** Near classical solutions admitting a compact Cauchy surface, with massive fields, a contraction argument targets constant kappa ~ (m/M_P)^2 << 1 via a Hadamard decomposition of the response kernel. **(Sketch — demoted from Rigorous, 2026-06; permanently Sketch at the stated generality, FPE-4 / #103).** The four gaps are not on equal footing (analysis: `explorations/2026-06-16-FPE4-M3-structural-obstruction.md`): **(M3) is a structural obstruction** — the non-local response kernel is a Green operator of the Lorentzian hyperbolic operator (causal-past support), so the single-Cauchy-surface spatial-resolvent strategy cannot be closed within the proof's assumptions A1–A6; a repair needs a controlled global foliation (beyond A1–A6) and is then foliation-restricted, yielding "Rigorous on a [homogeneous/controlled] slicing," local in time — the route Meda–Pinamonti–Siemssen take on FLRW. (M3) shares its root with the well-definedness gap (M8) — two faces of one obstruction — and is mass-independent (so it also binds the massless case). **(M1) is a hidden-reference-scale artifact** (diagnosed; the corrected single-scale form is schematic, net scale tied to the joint M4 repair): with a single explicit Sobolev scale μ the Sobolev-index mismatch is removed, giving kappa ~ (m/M_P)^2 (R-independent, schematic) for μ²~m², or kappa ~ ℓ_P²R for μ²~R — the latter forcing the local scale ħR, i.e. **(M4)**, so M1 and M4 are one joint repair. **(M5)** (the self-mapping bound) is a genuine technical gap any repair must still discharge. Existence itself is not refuted (Result 1; FLRW).
3. **Non-perturbative (Schauder).** On globally hyperbolic spacetimes with compact Cauchy surfaces, the Schauder fixed-point theorem guarantees existence under six assumptions, five established and one conjectural (uniform stress-energy bound). **(Conditional on A3)** — the written proof additionally has two flagged repairable gaps (M6: the fixed-point set is not closed/convex as defined; M7: the radius-selection argument is incorrect).

The previously claimed derivation of the Planck scale as the framework's validity boundary is withdrawn (the supporting formula mixed two Sobolev reference scales; once a single scale is fixed, the consistent kappa ~ (m/M_P)^2 is R-independent and no breakdown curvature is derived — see Section 7 and the (M1) diagnosis in Section 3). The massless case (photons, gluons) remains open, but is now understood to be blocked by the *same* structural M3 gap as the massive case (the compact-Σ spectral gap controls the wrong, spatial operator), not by an independent infrared failure (FPE-1, FPE-4).

## Explorations

- `explorations/2026-03-02-A1-Hs-bound-derivation.md` -- Hadamard-decomposition derivation of the H^s operator-norm bound for Lemma 1 (promoted Sketch → Rigorous in PR #26; **verdict withdrawn 2026-06**, see status note in the file — the record is retained per METHODOLOGY.md).
- `explorations/2026-06-14-FPE1-massless-case.md` -- The massless case (FPE-1, issue #66). Finds (Sketch) that on a compact 3-dimensional Cauchy surface the massless non-local kernel is Hilbert–Schmidt and the mass scale is replaced by the spectral gap λ₁(Σ) or, for conformal coupling on positively curved Σ, by ξR — so Theorem 2's `m > 0` is not sharp. The binding obstruction is the *shared* M3 hyperbolic→elliptic gap (FPE-1 is downstream of FPE-4), not a massless-specific IR failure; the only massless-specific residue is the zero mode of −Δ_Σ.
- `explorations/2026-06-16-FPE4-M3-structural-obstruction.md` -- FPE-4 (issue #103). Two independent position investigations (repairable vs. structural), run blind to each other, plus a dimensional verification of M1. Convergent finding: M3 is a **structural** obstruction to the single-slice spatial-resolvent strategy (the response kernel is a Lorentzian hyperbolic Green operator with causal-past support); any repair requires a controlled global foliation beyond A1–A6 and is foliation-restricted (matching the MPS FLRW route), recovering only local-in-time existence. M1 is a hidden-reference-scale artifact (diagnosed; corrected single-scale form schematic, net scale tied to joint M4 treatment). Both position files are retained in the document.

## Relationship to other programs

This paper is the Level 2 anchor for the self-consistency hierarchy / co-emergence program. **Note (2026-06): the Banach contraction that co-emergence cites as its rigorous Level 2 anchor is now Sketch, not Rigorous** — co-emergence claims that lean on it should be checked (METHODOLOGY.md issue relations: this demotion *informs* co-emergence). The signature-blindness observation (the contraction argument works on both Lorentzian and Riemannian manifolds) survives at Sketch level.

## Build

```bash
pdflatex index.tex
```
