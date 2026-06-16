# FPE-4: The Banach contraction gaps — M3 is a structural obstruction, M1 is a hidden-reference-scale artifact

**Date:** 2026-06-16
**Issue:** #103 (milestone FPE-4)
**Author:** worker routine (model claude-opus-4-8)
**Method:** two independent position investigations on the M3 question (run in
parallel, blind to each other, to fight anchoring on the 2026-06-14 FPE-1
conclusion) plus a focused dimensional verification of M1, synthesized below.
Both position files are retained in full (§§A, B) per METHODOLOGY — the losing
position is part of the record.
**Status of cited results:** read against the post-#72 record. Lemma 1
(`lem:kernel_bound`) and Theorem 2 (`thm:banach`) are **Sketch**. This
exploration does not promote anything; it establishes *direction* (which gap is
structural and why), and the companion `index.tex` edits in the same PR record
the conclusion at Sketch level.

---

## 0. Question and headline finding

FPE-4 asks whether the four gaps that demoted the perturbative Banach
contraction in PR #72 — M1 (dimensional inconsistency in the κ chain), M3
(hyperbolic→elliptic substitution), M4 (asserted local-coefficient scaling),
M5 (missing self-mapping bound) — can be closed (Outcome A: re-promote to
Rigorous) or whether one is structural (Outcome B: documented obstruction).

**Headline finding (Outcome B).** The four gaps are not on equal footing.

1. **M3 is a structural obstruction to the single-slice spatial-resolvent
   strategy of Lemma 1 / Theorem 2 as written.** The non-local response kernel
   `δ⟨T̂(x)⟩/δg(y)` is mediated by a *Green operator of the Lorentzian
   hyperbolic operator* `(□_g + m² + ξR)`, whose support is the causal past
   `J⁻(x)` (Rigorous — this is an operator-support statement, not a decay
   estimate). The spatial elliptic resolvent `(−Δ_Σ + m² + ξR|_Σ)⁻¹` that
   Step 4 substitutes is a different operator (elliptic vs. hyperbolic,
   functions on Σ vs. distributions on M, spacelike-exponential decay vs.
   light-cone support). No reduction of the Lorentzian kernel to a spatial
   operator on Σ is constructed. **A repair requires geometric input beyond the
   proof's assumptions A1–A6 — specifically a controlled global foliation — and
   is therefore foliation-restricted** (Sketch for "requires"; Rigorous for "is
   not closed as written and the obvious repair needs a foliation").

2. **The two independent positions converged.** Even the position constructed to
   make the *strongest possible repair case* (§A) concluded that M3 is
   repairable only into a **foliation-dependent, slab-local Volterra contraction
   in a time-weighted energy norm**, requiring a new assumption (A7: uniform
   causal-slab control) beyond A1–A6 and recovering only *local-in-time*
   existence — i.e. a *different theorem* from the single-slice spatial bound,
   in a different norm, valid on a preferred foliation. The structural position
   (§B) reached the same operative statement from the other direction. The
   disagreement is only over the word "structural"; the mathematics agreed.

3. **This is exactly the Meda–Pinamonti–Siemssen (MPS) precedent's shape, and it
   is foliation-restricted** (verified, §§A.2, B.3). MPS 2021 and
   Pinamonti–Siemssen 2015 contract in a norm over an interval of *cosmological
   time* on the *Hubble function* `H(t)`, exploiting homogeneous FLRW slicing to
   collapse the PDE to a 1D integral equation in `t`. The contraction is a
   time-weighted (Volterra) estimate tied to a preferred cosmological foliation,
   **not** a single-Cauchy-surface `H^s(Σ)` bound. The only known route to a
   Lorentzian contraction comes equipped with precisely the structure A1–A6 do
   not supply — positive evidence the structure is *needed*, not incidental.

4. **M3 and M8 share a root — two faces of one obstruction.** A genuine spatial
   reduction of the response kernel would also resolve M8 (the conflation of a
   spacetime fixed point of `F` with a fixed point of data on a chosen Σ, whose
   gauge-equivalence is never constructed). Until Σ is shown pure gauge, no
   spatial-resolvent bound is licensed; the implication M3-closure ⟹ M8-closure
   is clear (the converse is weaker), so both gaps arise from the same missing
   spatial-reduction step.

5. **M1 is a hidden-reference-scale artifact, separately diagnosable (§C).** The
   displayed `κ = (1/2π)(m/M_P)²ℓ_P²R` mixes two incompatible reference scales —
   `μ²~m²` in the kernel bound and `μ²~R` in the inverse-operator norm `C_inv` —
   and the eq.-level equality silently sets `R = ℓ_P⁻²` (the Planck-curvature
   substitution, applied once per factor of `ℓ_P²R`). With a *single* explicit
   Sobolev reference scale μ the chain is consistent and gives a
   **R-independent** `κ ~ (m/M_P)²` (graceful flat-space limit `R→0`, no lower
   bound on R required) for `μ²~m²`, or `κ ~ ℓ_P²R` for `μ²~R` — but the latter
   forces the kernel scale to `ħR/(4π)²`, which is exactly Gap M4's objection.
   M1 cannot be closed by bookkeeping alone: it forces a physical choice of μ
   that collides with M4. The displayed formula is **an artifact, not a
   derivation.**

**Consequence for the program.** FPE-4's done-condition is met via Outcome B.
The perturbative contraction is **permanently Sketch** pending geometric input
beyond A1–A6; a foliation-restricted repair (the A7 / MPS-style route) is the
honest path forward and would have to be labeled "Rigorous on [a controlled
global foliation]," not simply "Rigorous." This is recorded in `index.tex`
(§3 gap notes, §4 (A6), §7, §open), the program README, and the co-emergence
Level-2 anchor in the same PR.

**Signature consequence (informs co-emergence; filed as a thread proposal).**
The M3 obstruction is *signature-dependent*: `□_g` is hyperbolic on a Lorentzian
manifold (light-cone support — M3 binds) but *elliptic* on a Riemannian manifold
(where a spatial-resolvent-type bound is legitimate). The co-emergence paper's
"signature-blind contraction" (`κ ~ (m/M_P)²` identical for both signatures,
Remark `rem:signature_blind`) is therefore, at the level of the *proof
strategy*, precisely the Lorentzian-vs-Riemannian conflation M3 identifies: the
estimate that is legitimate on the Riemannian side is being imported to the
Lorentzian side. This does not refute signature-blindness of *existence* (the
Starobinsky and round-`S⁴` fixed points are both exact), but it does mean the
*Banach-contraction support* for signature-blindness is exactly where M3 bites.
Raised as a `thread-proposal` for governor adjudication, not worked here.

---

## 1. Why this is Outcome B, not Outcome A — and what is NOT claimed

- **Existence is not refuted.** Theorem 1 (de Sitter / Starobinsky, Rigorous in
  this paper) and MPS (FLRW, verified) establish existence where the geometry
  supplies a time function. The claim is narrow: the *single-slice
  spatial-resolvent proof strategy* (Lemma 1 / Theorem 2 as written) has a
  structural gap A1–A6 cannot close for general globally hyperbolic backgrounds
  with compact Σ. "This proof is obstructed" — not "no proof exists." This keeps
  consistency with Theorem 1.
- **A general-background contraction is not proven impossible.** It is claimed
  only that any repair requires structure beyond A1–A6 (a controlled global
  foliation / homogeneous slicing, or an M8 gauge-equivalence construction) and
  is to that extent foliation-restricted. The strong "cannot *ever* be closed"
  is Sketch/Conjecture; what is Rigorous is the operator-support statement and
  the A1–A6-insufficiency statement.
- **The obstruction is mass-independent.** `λ₁(Σ)` and `ξR` control the *spatial*
  (elliptic) operator — the very operator M3 says is wrong — so the compact-Σ
  spectral gap cannot cure a causal-support problem. This is consistent with
  FPE-1 (2026-06-14) §4.1: the binding obstruction is the shared M3, not a
  massless-specific IR failure. FPE-1 is downstream of FPE-4, confirmed.

---

## A. Position — "M3 is repairable" (strongest repair case)

*Developed independently and blind to Position B. Reproduced because it is the
positive content of the conclusion: it tells the program exactly what a repair
would have to look like.*

**Construction (Sketch).** The error in Step 4 is not that the spatial elliptic
resolvent is *wrong*, but that it is the *static* reduction; the correct object
is the *retarded* inverse of the hyperbolic operator, controlled by a finite-time
energy estimate rather than by spatial decay. Fix a foliation `M ⊃ Σ_t`,
`t ∈ [0,T]`. The variation solves the inhomogeneous retarded problem
`(□_g + m² + ξR)δW₂ = J[δg]`, `δW₂ = E^ret_g J[δg]`, with `E^ret_g` the retarded
Green operator (unique on a globally hyperbolic spacetime; Bär–Ginoux–Pfäffle,
*Wave Equations on Lorentzian Manifolds* — **[exploratory, unverified; standard]**).
Do not bound `E^ret` by a spatial resolvent kernel; use the Klein–Gordon **energy
inequality** with Grönwall on the time slab, equivalently the **time-weighted
norm** `‖u‖²_σ = ∫₀^T e^{−2σt}‖u(t)‖²_{H^s(Σ_t)} dt`, in which the retarded
(Volterra, lower-triangular-in-time) operator is bounded `H^{s−2}_σ → H^s_σ` with
norm `≤ C/σ` for `σ > Λ`. The light-cone contribution is controlled not by
suppression but by *finite causal volume* on `[0,T]`; the mass/curvature scale
`m² + ξR` enters the Grönwall constant `Λ`, recovering `(m/M_P)²` through the
slab and energy constants rather than through spatial exponential decay. (Sketch
— the energy estimate is standard; composition with point-splitting and
uniformity over `K_ρ` are gaps.)

**Foliation-dependence verdict (stated plainly).** The construction *is*
foliation-dependent: the time-weighted norm, the energy, the slab `[0,T]`, and
the Volterra structure all require a choice of Cauchy foliation and hence a
global time function. This is exactly MPS's structure (verified: MPS 2021,
DOI 10.1007/s00023-021-01067-8; Pinamonti–Siemssen 2015, CMP 334, 171–191 —
the inverse "has the form of a retarded product, respecting causality," and the
traced Einstein equation becomes a fixed-point equation solved by Banach on a
finite time interval). Defense offered: global hyperbolicity is *equivalent* to
the existence of a smooth Cauchy time function (Bernal–Sánchez —
**[exploratory, unverified; standard]**), so the repair uses *a* foliation the
framework already granted itself, not a *preferred* one, and the fixed point is
foliation-covariant even if the estimate is not foliation-invariant.

**Additional assumption required — named.** **(A7) Uniform causal-slab control:**
there exist a Cauchy temporal function `t : M → [0,T]` with compact level sets
and constants `N_max, Λ < ∞` such that, uniformly for all `g ∈ K_ρ`, the lapse
`N ≤ N_max` and the foliation's energy-growth constant `Λ(g) ≤ Λ`. Strictly
weaker than homogeneity (bounded geometry of *one* foliation over `K_ρ`, not
constant geometry); plausibly derivable from (A2)+(A4) on compact `K_ρ` but not
derived here.

**Honest weakest points (from the repair position itself).** (1) (A7)'s
uniformity over `K_ρ` is exactly the hard analysis, only conjectured. (2) The
σ-weight buys contraction at the cost of an `e^{ΛT}` factor: only *local-in-time*
existence is recovered — the *global* Theorem 2 is not, matching MPS getting
solutions only up to a singularity. (3) Composition of the energy bound with the
coincidence-limit point-splitting operator at the correct `H^s→H^{s−2}` index is
asserted, not shown. (4) MPS's collapse to a 1D time-integral equation is
genuinely special to homogeneity; off homogeneous slicing the cross-term between
time-Volterra and per-slice elliptic control is the least-verified link
(Conjecture).

**Net.** The strongest repair case concedes the operative point: Theorem 2 *as
written* is not recovered; the repair is a different, foliation-restricted,
local-in-time theorem requiring A7.

---

## B. Position — "M3 is structural" (strongest obstruction case)

*Developed independently and blind to Position A.*

**Precise statement (Rigorous core).** The nonlocal part of `K(x,y) =
δ⟨T̂(x)⟩/δg(y)` is the image of a source under a Green operator of the normally
hyperbolic operator `(□_g + m² + ξR)`. Every Green operator (retarded/advanced/
Feynman) on a globally hyperbolic spacetime has support set by causal structure:
`supp G^ret(x,·) = J⁻(x)` (Bär–Ginoux–Pfäffle — **[exploratory, unverified;
standard]**). Hence the coincidence-limit `K(x,x)` receives unsuppressed
contributions from `δg(y)` for every `y ∈ J⁻(x)`. The exponential-decay estimate
`|(−Δ_Σ + m² + ξR)⁻¹(x,y)| ≤ C e^{−m d_Σ(x,y)}` Step 4 invokes is a property of
the *elliptic* resolvent on a single Riemannian slice and controls only
spacelike-Σ decay. The two operators differ in principal symbol, domain, and
support. **Minimal statement:** *Lemma 1 Step 4 estimates the wrong operator; the
bound is not established, because reducing the Lorentzian kernel to an `H^s(Σ)`
operator requires a spatial reduction that is never constructed.*

**Why A1–A6 are insufficient.** A reduction "kernel on M ⟶ spatial operator on Σ
with controllable decay" presupposes a canonical decomposition of the Lorentzian
Green operator into time-evolution off a chosen Σ — i.e. a global time function
`t : M → ℝ` (or symmetry making slice-data evolution autonomous). A1 (Hadamard
state), A2 (continuous metric dependence), A3 (uniform T-bound; itself only
Conjecture), A4 (elliptic linearized-Einstein inverse on the slice), A5
(Parker–Simon order reduction — lowers derivative order but a 2nd-order
hyperbolic operator still has `J⁻(x)`-supported Green operators), A6 (the
contraction bound itself) — none foliate M. Global hyperbolicity gives *some*
Cauchy surface and `M ≅ ℝ × Σ` topologically, but does not single out a
foliation, and the framework's no-preferred-observer commitments forbid
smuggling one in. The choice of Σ in §3 is unjustified background structure —
the content of Gap M8.

**MPS is foliation-restricted (verified).** Pinamonti–Siemssen 2015 (CMP 334,
171–191, DOI 10.1007/s00220-014-2099-5) and Meda–Pinamonti–Siemssen 2021 (AHP
22, 3965–4015, DOI 10.1007/s00023-021-01067-8), both **[verified]**, work on flat
FLRW, solve a coupled integral-functional equation for the Hubble function `H(t)`
and the quantum state over an interval of cosmological time, and apply Banach in
a time-interval norm. Homogeneity collapses the metric DOF to `a(t)` and builds
the state adiabatically along the *same* cosmological time. Remove homogeneity
and both load-bearing features fail: the perturbation becomes a field on M with
no canonical time and the kernel becomes the full `J⁻(x)`-supported Lorentzian
operator. Their technique does not, as stated, survive removal of homogeneity
(Sketch for the structural points; Conjecture for "no homogeneity-free
adaptation exists" — a CMC-foliation adaptation might recover a time-norm
contraction, but that would itself be geometric input beyond A1–A6, *supporting*
the foliation-restricted thesis).

**Boundary of the claim.** Existence is not refuted (Theorem 1, MPS). The claim
is the single-slice spatial strategy as written is obstructed; a repair needs
structure beyond A1–A6 and is foliation-restricted. Mass-independent (the spectral
gap controls the wrong operator).

**Honest weakest points (from the obstruction position itself).** (1)
"Structural" is a claim about absence; what is Rigorous is "not closed as
written + obvious repair needs a foliation," while "cannot *ever* be closed by
any A1–A6 route" (e.g. an equal-time/Euclidean reformulation with a controlled
gap to the Lorentzian object, a route §open itself flags) is Sketch/Conjecture.
(2) "MPS cannot survive removal of homogeneity" is an inference from the
estimate's structure, not a proven no-go — but a CMC adaptation is *itself*
beyond A1–A6. (3) The renormalized, order-reduced kernel might have better
effective decay than the bare Green operator after point-splitting; the Rigorous
core (wrong operator, wrong support, no reduction constructed) stands regardless,
but "no suppression at all" should be read as "none established."

---

## C. M1 — dimensional verification (the hidden reference scale)

*Focused verification, independent of the M3 positions.*

**Units:** ħ = c = 1, [length] = [mass]⁻¹, R ~ [mass]², G = ℓ_P² = M_P⁻² ~
[mass]⁻². κ is the Lipschitz constant on dimensionless metric perturbations, so
**κ must be dimensionless.**

**The inconsistency (Rigorous).** Literal chain `8πG · C_inv · ‖K^red‖` with
`C_inv ~ 1/R` (`D = −2`) and `‖K^red‖ ≤ C_K ħm²/(4π)²` (`D = +2`), times `8πG`
(`D = −2`): total `D = −2`, i.e. `κ_literal = ℓ_P²m²/(2πR)` has dimension
[length]² and diverges as `R → 0`. Displayed RHS `(1/2π)(m/M_P)²ℓ_P²R` has
`D = 0` (dimensionless). The true ratio displayed/literal `= ℓ_P²R²` (dimension
[mass]², D=+2); the two expressions carry different dimensions so a direct "ratio
= 1" comparison is ill-posed. The key observation is that the literal and displayed
forms coincide in order of magnitude only when `R ~ ℓ_P⁻²` (Planck curvature,
where `ℓ_P²R² = 1` in Planck units) — the silent Planck-curvature substitution,
applied once per factor of `ℓ_P²R`.

**The hidden scale μ (Sketch→Rigorous).** A dimensionally homogeneous Sobolev
norm needs a reference mass: `‖u‖²_{H^t} = ⟨u, (μ²−Δ)^t u⟩`, so `‖A‖_{H^a→H^b}`
carries an explicit `μ^{a−b}` times the intrinsic dimension of A. `C_inv =
‖(G_lin)⁻¹‖_{H^{s−2}→H^s}` carries `μ⁻²`; its "1/R" is really `1/(spectral gap of
G_lin)`, equal to `1/R` only when the gap scale `μ²~R`. `‖K^red‖_{H^s→H^{s−2}}`
carries `μ^{+2}`; the asserted `ħm²/(4π)²` is legitimate only when `μ²~m²`.
**The current text uses two different implicit scales** (`μ²=R` in `C_inv`,
`μ²=m²` in the kernel) — which is exactly why the unbalanced `ℓ_P²R` appears.

**Verdict (Rigorous on the logic).** M1 is *conditionally* fixable, but only by
committing to a single μ in *both* factors, and the natural choices give
different κ:
- **`μ²~m²` (Compton):** `C_inv ~ 1/m²` (Sobolev-index contribution `μ⁻²` with
  `μ²~m²`), `‖K^red‖ ~ ħm²/(4π)²` ⟹ **`κ ~ (m/M_P)²`, R-independent** —
  *schematic*: the Sobolev-index factors `μ⁻²` and `μ⁺²` cancel, but the
  surviving net physical scale depends on the intrinsic dimensions of the operator
  product (the physical spectral gap of `G_lin` vs. the physical kernel size),
  which requires the joint (M1)+(M4) treatment to make precise. Flat-space limit
  `R → 0` graceful on this reading; matches the mass table in §3 as a schematic
  estimate.
- **`μ²~R`:** `C_inv ~ 1/R`, and consistency forces `‖K^red‖ ~ ħR/(4π)²` ⟹
  **`κ ~ ℓ_P²R`**, `→ 0` as `R → 0` (also graceful) — but the kernel scale is now
  `ħR`, not `ħm²`, destroying the `(m/M_P)²` headline. *This is exactly Gap M4.*

So the displayed `κ = (1/2π)(m/M_P)²ℓ_P²R` is **not defensible as written**: it
is the product of a `μ²=m²` kernel scale and a `μ²=R` inverse-operator gap, glued
by `R = ℓ_P⁻²`. **M1 cannot be closed by bookkeeping alone — it forces a physical
choice that collides with M4.** The linkage is nearly mechanical: fixing a single
global μ, the `μ²~R` reading immediately forces the kernel estimate to
`‖K^red‖ ~ ħR/(4π)²` (not `ħm²/(4π)²`), so the two gaps are inseparable in any
honest single-μ treatment. Recommend a joint M1+M4 treatment; the corrected
Sketch-level statement is `κ ≤ C·(m/M_P)²·f(μ²/m², ℓ_P²R)` with `f → const` for
`μ²~m²` and `f ~ ℓ_P²R` for `μ²~R`. The theorem needs an explicit single μ, not
a lower bound on R. The §7 Planck-boundary withdrawal is *confirmed*: with the
defensible `μ²~m²` reading κ is R-independent, so there is no derived breakdown
curvature at all.

---

## 2. Self-checks (METHODOLOGY rigor checklist)

- **Dimensional analysis.** κ dimensionless; literal chain is [length]², displayed
  is dimensionless, reconciled only by `R = ℓ_P⁻²` (§C). With a single explicit μ
  the chain is consistent; corrected κ stated. ✓
- **Limiting cases.** Flat space `R → 0`: with `μ²~m²`, `κ ~ (m/M_P)²`
  R-independent (graceful); the previous `κ ∝ 1/R` divergence was the artifact,
  not the physics (§C). de Sitter / `R ~ ℓ_P⁻²`: consistent with Theorem 1's
  domain in the `κ ≪ 1` regime (existence not refuted, §1). ✓
- **Consistency.** Does not contradict Theorem 1 (existence holds where a time
  function exists); does not contradict MPS (agrees on FLRW, where the
  foliation is supplied). No new postulate is *asserted* — the documented repair
  *would* need A7, which is precisely why this is a documented obstruction and
  not a repair (§1). ✓
- **Order-of-magnitude.** Corrected `κ ~ (m/M_P)²` reproduces the §3 mass table
  (`10⁻⁴⁵`–`10⁻³⁴`); foliation-restricted MPS-route κ on closed FLRW `~ (ℓ_P/a)²
  ≪ 1` for super-Planckian curvature radius. ✓

## 3. Outcome and recommendation

**Outcome B (documented obstruction), done-condition met.** M3 is the structural
gap; M1 is a separately-diagnosable reference-scale artifact (resolved at Sketch
level, joint with M4); M5 remains a genuine technical gap required for *any*
(foliation-restricted) repair. `index.tex`, README, and the co-emergence anchor
updated in the same PR to permanently-Sketch with the obstruction named.

**Sequencing signal for the governor.** A foliation-restricted repair (the
A7 / MPS-style time-weighted energy estimate) is the honest forward path and is
a well-posed FPE-4 follow-on; it would yield "Rigorous on a controlled global
foliation," local-in-time, not the general Theorem 2. M3 and M8 share their root
obstruction: the same spatial-reduction work would simultaneously close M8's
well-definedness gap. Recorded as an observation; OBJECTIVES edits are the
governor's.

---

*Internal references (`meda_pinamonti_siemssen`, `pinamonti_siemssen`,
`parker_simon`, assumptions A1–A6, gaps M1/M3/M4/M5/M8, Theorem 1) refer to
results in `programs/fixed-point-existence/index.tex`. MPS 2021 (AHP 22,
3965–4015) and Pinamonti–Siemssen 2015 (CMP 334, 171–191) verified via Springer
this run. Bär–Ginoux–Pfäffle and Bernal–Sánchez are cited
**[exploratory, unverified; standard]** and do not enter `index.tex`.*

routine: worker · model: claude-opus-4-8
