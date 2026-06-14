# FPE-1: The massless case — spectral-gap IR control, conformal coupling, and the obstruction that actually binds

**Date:** 2026-06-14
**Issue:** #66 (milestone FPE-1)
**Author:** worker routine (model claude-opus-4-8)
**Status of cited results:** read against the post-#72 record. The kernel bound
(Lemma 1, `lem:kernel_bound`) and the perturbative existence theorem (Theorem 2,
`thm:banach`) are **Sketch**, not Rigorous; the `ħm²/(4π)²` coefficient is gap
**M4** (asserted, not derived) and the exponential-decay step is gap **M3**
(spatial elliptic resolvent substituted for the Lorentzian hyperbolic variation
problem). The 2026-03-02 exploration this builds on had its Sketch→Rigorous
verdict **withdrawn** in 2026-06. Everything below treats the `m>0` bound as a
*conjectured* baseline, per the governor's 2026-06-11 correction comment on #66.

---

## 0. Question and headline finding

FPE-1 asks whether the perturbative (Banach) contraction extends to massless
fields — the Standard Model photon and gluon — or whether `m > 0` is sharp.
The paper currently states the massless case is open because, for `m = 0`, "the
non-local kernel decays only algebraically, the Hilbert–Schmidt bound may
diverge, and the argument breaks down."

**Headline finding (Sketch + documented obstruction).** That stated obstruction
is *flat-space intuition imported into a compact-Σ setting where it does not
bind.* On a compact Cauchy surface the spatial Laplacian has discrete spectrum
with a spectral gap `λ₁(Σ) > 0`, and the massless Green's function on a
**3-dimensional** Σ is Hilbert–Schmidt despite its `d^{-1}` singularity (Direction
A, §2). The dimensionful replacement for `m²` is `λ₁(Σ)` (or, for a conformally
coupled field on positively curved Σ, the effective mass `ξR`, Direction B, §3),
both with the correct `[mass]²` dimension. The flat-space IR divergence is
recovered exactly as `Σ` decompactifies and the gap closes, `λ₁ → 0` (§2.3).

The genuine conclusion (Direction C, §4) is therefore **not** an
independent massless obstruction. The step that actually fails at `m = 0` is the
*same* M3 hyperbolic→elliptic substitution that already blocks the massive case:
the analysis below, like Step 4 of Lemma 1, lives at the level of the *spatial
elliptic resolvent on Σ*, the very object M3 flags as not the correct Lorentzian
one. **FPE-1 is downstream of FPE-4, not parallel to it.** Once M3 is repaired,
the contraction extends to massless conformally coupled scalars on compact Σ
essentially for free, with `m² → max(ξR, λ₁(Σ))`. One sub-case remains genuinely
open even after M3: the **zero mode** — the minimally coupled (`ξ = 0`) massless
scalar on a Ricci-flat / non-positively-curved compact Σ, and the gauge-field
zero-momentum sector (§4.2).

So Theorem 2's restriction to `m > 0` is **not sharp** as stated; the honest
restriction is "`m > 0`, *or* a positive infrared gap supplied by `ξR > 0` or by
`λ₁(Σ)` with the constant mode controlled," contingent on the M3 repair.

---

## 1. Setup and what "the massless case" inherits

The contraction is controlled by `κ = 8πG · ‖(G_lin)^{-1}‖ · sup_{K_ρ}
‖K^red‖_{H^s→H^{s-2}}` (Theorem 2). The matter enters only through
`‖K^red‖_{H^s→H^{s-2}}`, decomposed (Lemma 1) into:

- a **local** part `K^red_loc = Σ_{|γ|≤2} a_γ(x) ∂^γ`, bounded by `‖a_γ‖_{L^∞}`
  (Step 3); and
- a **non-local** part `K_nl`, a smooth integral operator bounded by its
  Hilbert–Schmidt (= `L²(Σ×Σ)`) norm (Step 4).

In the massive case both prefactors were written as `ħm²/(4π)²`. The massless
question is whether either part loses control as `m → 0`. I take Σ to be a
**compact Riemannian 3-manifold** (the spatial Cauchy surface; `n := dim Σ = 3`)
throughout, since that is the regime in which Lemma 1 and Theorem 2 are stated
(compact Cauchy surface, Rellich–Kondrachov compactness of `K_ρ`).

---

## 2. Direction A — compact-Σ spectral gap

### 2.1 The non-local kernel is Hilbert–Schmidt at `m = 0` (Sketch)

On a compact Riemannian `n`-manifold the Green's function of `-Δ_Σ` (projected
off the constant zero mode) has the universal short-distance behaviour of the
Euclidean fundamental solution,
```
G₀(x,y) ~ c_n · d_Σ(x,y)^{2-n}      (n ≥ 3),   smooth for x ≠ y,
```
with `c_3 = 1/(4π)`; for `n = 3`, `G₀ ~ 1/(4π d_Σ(x,y))`. (Standard heat-kernel /
parametrix asymptotics on closed manifolds; **[exploratory, unverified]** Gilkey,
*Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, and
any elliptic-PDE text e.g. Taylor PDE I Ch. 7.)

**Claim (Rigorous, elementary).** For `n = 3`, `G₀ ∈ L²(Σ × Σ)`, i.e. `-Δ_Σ^{-1}`
is Hilbert–Schmidt. *Proof.* Off-diagonal `G₀` is smooth and Σ compact, so the
only question is integrability near the diagonal. With `|G₀|² ~ (4π)^{-2}
d_Σ^{-2}` and the 3-dimensional volume element `~ r² dr dΩ` (`r = d_Σ`),
```
∫_{d_Σ < ε} |G₀(x,y)|² dV(y)  ~  (4π)^{-2} ∫₀^ε r^{-2} · 4π r² dr
                              =  (4π)^{-1} ε  <  ∞,
```
uniformly in `x`; integrating the (bounded) result over the compact Σ gives
`‖G₀‖²_{L²(Σ×Σ)} < ∞`. ∎

The exponent bookkeeping generalises: `|G₀|² ~ d^{2(2-n)}` against `d^{n-1} dr`
gives integrand `d^{3-n} dr`, integrable near `0` iff `n < 4`. So the massless
Green's function is Hilbert–Schmidt on a 3-dimensional Cauchy surface, **marginal**
(log-divergent) at `n = 4`, and fails for `n ≥ 5`. This is exactly the
dimension-count asserted in issue #66, now checked. The "Hilbert–Schmidt bound
may diverge" worry in the paper's massless remark is a statement about *infinite
volume* (§2.3), **not** about the `m → 0` limit on a fixed compact Σ.

The response kernel `K_nl` is not the bare resolvent but is built from it (the
variation `δW/δg` is mediated by the resolvent, Step 4 / 2026-03-02 exploration
§3). At the level of HS-boundedness the conclusion transfers: `K_nl` inherits the
resolvent's `d^{-1}` singularity dressed with smooth geometric coefficients, so it
remains in `L²(Σ×Σ)` on a compact 3-manifold. **(Sketch — same gaps as the massive
Step 4; see §4.1.)**

### 2.2 The replacement for `m²`, and dimensional analysis

With `m = 0` the only positive scale controlling the resolvent is the **spectral
gap** `λ₁(Σ) > 0` (smallest positive eigenvalue of `-Δ_Σ`), via
`‖(-Δ_Σ)^{-1}‖_{op, (const)^⊥} = 1/λ₁(Σ)`. The natural massless bound is therefore
```
‖K^red‖_{H^s→H^{s-2}}  ≲  C_K · ħ · λ₁(Σ) / (4π)²        (Sketch),
```
i.e. `m² ↦ λ₁(Σ)`. **Dimensional check:** in `ħ = c = 1`, `[λ₁] = [length]^{-2} =
[mass]²`, so `ħ λ₁/(4π)²` carries `[mass]²` — identical dimensions to the massive
`ħm²/(4π)²`. ✓ This satisfies the issue's requirement to identify the dimensionful
replacement for `m²`.

Two caveats, both flagged as gaps in §4:

- The factor `λ₁` controls the resolvent on `(const)^⊥` only; the **zero mode**
  needs separate treatment (§4.2).
- Whether the *local* part (Step 3) also collapses to a `λ₁`/`R` scale rather than
  `m²` is the M4 question, addressed in §3.2: at `m = 0` it does, via the anomaly.

### 2.3 Flat-space limit check (consistency)

Decompactify Σ toward `ℝ³` — concretely a flat 3-torus of side `L`, `λ₁ =
(2π/L)² → 0`. Two things happen together:

1. The prefactor `ħ λ₁/(4π)² → 0`.
2. The HS norm of `G₀` **diverges**: on `ℝ³`, `∫ |G₀(0,y)|² d³y = ∫ (4πr)^{-2}
   4π r² dr = (4π)^{-1} ∫₀^∞ dr = ∞`. The `d^{-1}` tail is harmless near the
   diagonal but non-integrable at infinity.

So the bound is finite for any compact Σ purely *because* the gap is open, and it
degenerates exactly as the gap closes. This reproduces the known statement that
on Minkowski the massless response kernel is IR-divergent at zero momentum
(`p → 0` is the `λ₁ → 0` continuum analogue). The compactness is doing genuine
work, and the massless flat-space divergence is recovered in the right limit. ✓
This is the **flat-space-limit acceptance criterion** of #66, met.

(Order of magnitude: for a closed universe of curvature radius `a`, `λ₁ ~ a^{-2}
~ R`, so `κ ~ 8πG · ħR/(4π)² · C_inv ~ (ℓ_P/a)² ≪ 1` whenever the curvature
radius is super-Planckian — the same smallness the massive case gets from
`(m/M_P)²`, with `m ↦ 1/a`. ✓)

---

## 3. Direction B — conformal coupling and the trace anomaly

### 3.1 Conformal coupling supplies a real mass gap where `R|_Σ > 0` (Sketch)

The field equation is `(□_g + m² + ξR)φ = 0`; the conformally coupled massless
scalar has `m = 0, ξ = 1/6` (in `d = 4`). The reduction that Step 4 performs
replaces the wave operator by a spatial elliptic operator whose potential carries
the `ξR` term — schematically `(-Δ_Σ + ξR|_Σ + …)`, the ellipsis being
extrinsic-curvature / lapse-shift terms from the 3+1 split (kept schematic; see
§4.1). **Where the relevant curvature combination is positive, `ξR|_Σ > 0` acts
as an effective mass²:**
```
m_eff²  =  ξ R|_Σ  >  0,        decay rate  √(ξR),
```
restoring genuine exponential decay of the resolvent kernel with **no appeal to
`λ₁` and no zero mode**. The massless obstruction simply does not arise for a
conformally coupled scalar on a positively curved compact slice. The replacement
prefactor is `ħ ξR/(4π)²` (dimensions `[mass]²` ✓).

This is the physically important case: closed FLRW (`k = +1`) has `R|_Σ > 0`, and
the Starobinsky fixed point (Result 1, Rigorous) lives precisely on conformal
matter on FRW — so the conformally coupled massless field is exactly the matter
content for which the program already has its one exact result. Direction B says
the *perturbative* contraction has no massless obstruction there either, modulo
M3.

Where `R|_Σ ≤ 0` (flat or negatively curved slices), `ξR` gives no positive
shift and one falls back on `λ₁(Σ)` (Direction A) plus the zero-mode caveat.

### 3.2 The trace anomaly fixes the local-part scale at `ħR/(4π)²` (Sketch, and this is M4)

For the local part (Step 3), the massive case asserted `‖a_γ‖_{L^∞} ≲
ħm²/(4π)²` — gap M4 already notes this fails for the mass-independent anomaly
counterterms, which scale as `ħR/(4π)²`. At `m = 0` there is *no* `m²` scale left,
so the local coefficients are governed **entirely** by the trace anomaly and the
curvature counterterms: the `R²`, `C²`, and Euler-density variations in `C_{μν}[g]`
contribute local terms `~ ħR/(4π)²`. The trace anomaly is non-zero even at `m = 0`
(it is the `a₂` Euler-density coefficient that drives the Starobinsky de Sitter
stage). Thus:
```
‖K^red_loc‖_{H^s→H^{s-2}}  ≲  C_loc · ħ R / (4π)²        (m = 0).
```
Note the massless local scale `ħR/(4π)²` and the massless non-local scale
`ħλ₁/(4π)²` **coincide in order of magnitude** (`λ₁ ~ R` on a slice whose
curvature radius sets its size), so the combined massless bound is a clean
`κ ~ 8πG · ħR/(4π)² · C_inv`. This is the same `ħR/(4π)²` scale that M4 says the
massive bound *cannot avoid*: i.e. at the level of the bound's magnitude, the
massless case and the curvature-counterterm part of the massive case are the same
computation. **This is why FPE-1 and FPE-4/M4 are not separable.**

---

## 4. Direction C — what actually obstructs, stated precisely

### 4.1 The binding obstruction is M3, identical to the massive case (documented)

Every estimate above (and every estimate in the massive Step 4) is performed on
the **spatial elliptic resolvent on Σ**: `(-Δ_Σ + m² + ξR|_Σ)^{-1}` for the
massive/conformal case, `(-Δ_Σ)^{-1}|_{(const)^⊥}` for the minimally coupled
massless case. Gap M3 states that this is *not* the correct object: the variation
`δW/δg^{αβ}(y)` is governed by the **Lorentzian hyperbolic** operator `(□_g + m² +
ξR)`, whose solution operator has light-cone support, and a metric perturbation in
the *causal past* of `x` influences `W(x,x)` with **no exponential (and, at
`m = 0`, no algebraic-`λ₁`) suppression** — the spatial-resolvent decay is the
wrong decay. No reduction of the response kernel to a spatial operator on Σ has
been constructed in either case.

**Consequence.** The massless question is *not* independent of the contraction
repair. There is no separate "massless IR obstruction": on a compact Cauchy
surface the IR is controlled by `λ₁(Σ)` (Direction A) or `ξR` (Direction B), so
the only thing that fails at `m = 0` that does not already fail at `m > 0` is the
zero mode (§4.2). The principal gap — the hyperbolic→elliptic substitution — is
shared. **FPE-1 should be sequenced after FPE-4 (M3); a repair of M3 that produces
a genuine spatial reduction of the Lorentzian response kernel will determine the
massless case at the same stroke**, with `m² ↦ max(ξR, λ₁(Σ))`.

This also answers the issue's "structural vs. technical" question directly: the
massless difficulty is **technical and shared**, not a structural non-existence of
the contraction. There is no evidence here of massless runaway solutions beyond
the Horowitz high-frequency runaways already excluded by assumption A5; the
contraction's smallness parameter `κ ~ (ℓ_P/a)²` stays `≪ 1` in the sub-Planckian
regime with `m² → R`, so the iteration does not diverge for that reason.

### 4.2 The one genuinely massless-specific residue: the zero mode (documented obstruction)

The single feature with no massive analogue is the **constant zero mode** of
`-Δ_Σ`. For `m > 0` the operator `-Δ_Σ + m²` is strictly positive and invertible;
for the minimally coupled massless scalar (`ξ = 0`) the constant function is a
genuine zero mode and `(-Δ_Σ)^{-1}` is undefined on it. Disposition by field:

- **Conformally coupled scalar, `R|_Σ > 0`:** no zero mode — `ξR` lifts it
  (§3.1). *Covered.*
- **U(1) / gauge field (photon, gluon):** the zero-momentum longitudinal mode is
  **pure gauge**; on the physical (transverse) subspace the relevant operator has
  no normalizable constant mode. So gauge invariance is expected to remove the
  zero-mode obstruction, but this requires a gauge-fixed reduction of the response
  kernel that is **not carried out here**. *(Conjecture — plausible, not shown.)*
- **Minimally coupled massless scalar (`ξ = 0`) on Ricci-flat / non-positively
  curved compact Σ** (e.g. a flat 3-torus): the homogeneous mode is a true zero
  mode with no restoring term. Here `λ₁(Σ) > 0` still controls `(const)^⊥`, but
  the constant mode of the source is not contracted. **This is the sharp residual
  open case.** *(Documented obstruction.)* It is, however, physically marginal:
  the SM has no fundamental minimally coupled massless scalar, and the realised
  spatial geometry is not exactly Ricci-flat.

### 4.3 Consistency with Meda–Pinamonti–Siemssen (acceptance criterion)

Their FLRW Banach contraction (`meda_pinamonti_siemssen`) is for **massive** fields
on homogeneous cosmological slicing. The massless extension consistent with their
framework is exactly Direction B: on closed FLRW, `R|_Σ > 0`, so a conformally
coupled massless field acquires `m_eff² = ξR` and their massive estimates apply
verbatim with `m² → ξR`. Two consistency points, both honest:

1. Their bounds are symmetry-reduced to homogeneous slices; our `λ₁(Σ)` / `ξR`
   control likewise uses a **chosen Σ** and is therefore **foliation-dependent** —
   exactly the dependence the governor's 2026-06-11 note flags for any M3 repair.
   A massless contraction established this way must be labeled "valid on a
   preferred (homogeneous / constant-`R|_Σ`) foliation," pending M3.
2. Nothing here contradicts MPS: where they have a result (massive FLRW) we agree;
   where we extend (massless conformal on positively curved compact Σ) they are
   silent, and the extension is `m² → ξR` within their own method. ✓

---

## 5. Self-checks (METHODOLOGY rigor checklist)

- **Dimensional analysis.** `m²` is replaced by `λ₁(Σ)` (Direction A) or `ξR`
  (Direction B), both `[mass]²` in `ħ = c = 1`; `ħλ₁/(4π)²` and `ħξR/(4π)²` match
  the massive `ħm²/(4π)²`. ✓ (§2.2, §3.1)
- **Limiting cases.** (i) `m → 0` on fixed compact Σ: bound stays finite,
  controlled by `λ₁`/`ξR` (§2). (ii) Volume → ∞ (`λ₁ → 0`): bound degenerates and
  the Minkowski IR divergence is recovered (§2.3). (iii) `R|_Σ > 0` conformal: the
  massive estimates apply with `m² → ξR` (§3.1). ✓
- **Consistency.** No contradiction with MPS (§4.3); no new postulate beyond the
  framework's axioms (only standard spectral geometry on the existing compact-Σ
  setup); the analysis sits at the same spatial-resolvent level as the existing
  Step 4, so it does **not** claim more than the M3-gapped massive argument does.
  ✓
- **Order-of-magnitude.** `κ ~ (ℓ_P/a)² ≪ 1` for super-Planckian curvature radius,
  matching the massive `(m/M_P)²` with `m ↦ 1/a`. ✓ (§2.3)

## 6. Outcome and recommendation

**Outcome for FPE-1 (both clauses of the done-condition met):**

- *Alternative-contraction clause (Sketch).* A massless contraction argument that
  does **not** require `m > 0`: on a compact 3-dimensional Cauchy surface the
  non-local kernel is Hilbert–Schmidt (§2.1) and the bound's mass scale is replaced
  by `λ₁(Σ)` or, for a conformally coupled field on positively curved Σ, by `ξR`
  (§2.2, §3.1), with the local part fixed at `ħR/(4π)²` by the trace anomaly
  (§3.2). All at Sketch level, carrying exactly the massive case's M3/M4 gaps and
  no new ones.
- *Documented-obstruction clause.* The massless case does **not** differ
  structurally from the massive case: the binding obstruction is the shared M3
  hyperbolic→elliptic substitution (§4.1), not a massless-specific IR failure
  (the paper's stated `m → 0` obstruction is a finite-volume artifact, §2.3). The
  only genuinely massless-specific residue is the zero mode (§4.2), sharp only for
  a minimally coupled `ξ = 0` scalar on Ricci-flat compact Σ and for the
  not-yet-gauge-fixed gauge sector.

**Recommendation — no `index.tex` edit this run.** The clean statement
("Theorem 2's `m > 0` is not sharp; replace `m² → max(ξR, λ₁(Σ))` once M3 is
repaired") is contingent on FPE-4, so editing Lemma 1 / Theorem 2 now would
encode a conclusion that rests on an open gap. The correct paper update is a
*single* edit folded into the FPE-4 (M3) repair PR: when the response kernel is
genuinely reduced to a spatial operator, state the massless extension in the same
PR with `m² → max(ξR, λ₁(Σ))` and the zero-mode caveat. Until then the paper's
"massless open" remark should be **re-pointed**, not removed — see the
thread-proposal note below.

**Suggested governance/sequencing signal:** mark **FPE-4 informs FPE-1**, and note
in the FPE-1 milestone that the massless extension is expected to fall out of the
M3 repair rather than need independent work, with the zero-mode sub-case as the
only residue. (Recorded as an observation for the governor; this exploration does
not edit OBJECTIVES.)

---

*References used above are textbook spectral-geometry / elliptic-PDE facts and are
flagged **[exploratory, unverified]** where a specific source is named; none are
promoted to paper-grade and none enter `index.tex`. The internal citations
(`meda_pinamonti_siemssen`, the trace-anomaly `a₂` coefficient, assumption A5,
gaps M3/M4) refer to results already in `programs/fixed-point-existence/index.tex`.*

routine: worker · model: claude-opus-4-8
