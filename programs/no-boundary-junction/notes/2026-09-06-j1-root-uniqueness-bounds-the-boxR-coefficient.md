# J-1: does the junction constrain the □R / R² coefficient? Yes — root uniqueness bounds it above, and the bound caps the root's depth at a few e-folds

**Date:** 2026-09-06
**Milestone:** J-1 of `programs/no-boundary-junction/OBJECTIVES.md` (#215 step 1). Standing assumption: conformal field content with a₂ ≡ (N_S + 11N_F + 62N_V)/2 ≥ 10⁶, an explicit input.
**Role:** interactive session, experimenter-directed. Exploration note (Markdown, exploratory-tier citations, how-checked stated inline).
**Correction (2026-09-06, same day, before any downstream use):** the anomaly-action regularization in the original §3.2 (Einstein-static-universe reference with an 8(σ′² − 1) subtraction) dropped cap-dependent boundary terms and overstated the action gap by a factor 2–20. Found by the position-H agent of the J-6 debate and verified independently by the lead with a compact-reference (round S⁴) Riegert functional. §3.2–3.3 and every number derived from them are replaced below; the existence threshold, the caps' geometry, the recollapse, and the ordering of the two caps are unaffected, and the dominance conclusion survives because a ≥ 5.6 × 10³ makes even the corrected gap decisive. Units: H₀ = 1 for the anomaly-driven de Sitter fixed point, G a = π with a = a₂/180 the Euler anomaly coefficient in the Duff normalization; ε is the total □R coefficient of the trace equation in Hubble units, ε = H₀²/M² with M the scalaron mass (step-0 note §2.2; Linde's M⁻² = −k₃/(2880π²)).

---

## Summary

**Result (outcome (a) of the J-1 done-condition, in inequality form).** In FRW minisuperspace with the anomaly-induced effective action plus the R² counterterm, the Euclidean solutions regular at the pole form a one-parameter family; the round S⁴ is a real, regular, K = 0 junction for *every* value of ε, so the real-junction condition alone fixes nothing. But for the unstable sign ε > 0 — the sign the de Sitter exit requires — a second reflection-symmetric regular cap exists once ε exceeds a threshold ε_c ∈ (0.35, 0.36): Hawking–Hertog–Reall's "double bubble," symmetric about its neck. Its Euclidean action is *lower* than the sphere's by a small finite gap already at birth (ΔI ≈ −0.12 a at ε = 0.36, reaching ≈ −1.3 a at ε = 1 and ≈ −3.3ε a for large ε; with a ≥ 5.6 × 10³ even the gap at birth is e^{680}-level dominance), and its real Lorentzian continuation across the neck is a closed universe of radius a_neck < 1 that recollapses within a fraction of a Hubble time. Hence, under the no-boundary Euclidean weighting, **the S⁴ is the unique and dominant real root of the junction iff 0 < ε < ε_c ≈ 0.355**, equivalently the scalaron must be heavier than ≈ 1.7 H₀, equivalently the R² coefficient in natural units is bounded, |β_tot| = ε a₂/(1440π²) ≲ 25 at a₂ = 10⁶. That bound caps the root's de Sitter depth: N_inf(ε_c) ≈ ln(M_P/H₀)/λ₊(ε_c) ≈ 5 e-folds at a₂ = 10⁶ (6.5 at 10⁷), against the ≈ 370-unit coefficient sixty e-folds would need. *(Family count, reality condition, action normalization, and the scaling identity I_EH = −2a: Rigorous, sympy-verified identities. Existence threshold, action ordering, recollapse: Rigorous (numerical) within minisuperspace. "Dominant root" and the N_inf bound: Sketch — they assume the Euclidean weight e^{−I} and the step-0 seed estimate.)*

**What it means.** The junction does constrain the coupling — not to a value but to a window, and through root *dominance* rather than through the reality condition. The mechanism is structural, not numerical: the sign of the R² term that makes de Sitter unstable is the sign for which the Euclidean action is unbounded below on high-curvature configurations, so the no-boundary measure prefers small, high-curvature caps whose Lorentzian continuations never inflate. Root uniqueness of the tree argument (J-6) and a long inflationary root are incompatible for this junction under Euclidean weighting. No hierarchy is generated (a bound is not a scale), so the mass-spectrum residue of #216 is unchanged; what is new is that the framework's second gravitational number is no longer free.

**Adaptations this points to** (per the standing instruction): (1) J-6 must decide the saddle prescription — under a Lorentzian / Picard–Lefschetz definition (Feldbrugge–Lehners–Turok; Di Tucci–Lehners) the set of contributing saddles and their weights change, and the double bubble's role must be redone there before the bound is treated as final; (2) the flat-topped cap born at ε_c (peak = neck, a degenerate equator with a″ = 0) is a new geometry with a possible analytic handle; (3) the hierarchy question moves to Level-0/1 data, unchanged from #216.

---

## 1. Setup

### 1.1 The equation

Euclidean closed FRW, ds² = dτ² + a(τ)² dΩ₃². Curvature invariants computed symbolically from the metric (§7, script 1; verified on the round sphere a = sin τ: R = 12, E₄ = 24, □R = 0):

R = −6(a a″ + a′² − 1)/a²,  E₄ = 24(a′² − 1) a″/a³,  C² = 0,  □R = a⁻³ (a³ R′)′.

The trace of the semiclassical Einstein equation with the anomaly's Euler term and a total □R coefficient, in units H₀ = 1 (so G a/(2π) · 24 = 12, i.e. the coefficient of E₄ is ½):

**R = ½ E₄ + ε □R.**  (T)

De Sitter (the round S⁴ of radius 1) solves (T) for every ε because □R ≡ 0 on it — this is why the fixed point's existence is ε-independent (`fpe-starobinsky-existence`, audit). The Lorentzian form of (T) is obtained by a′ → −i ȧ, a″ → −ä, a‴ → i a⃛; the result is real (script 3 asserts it), and its linearization about de Sitter is the step-0 polynomial (λ + 4)(ελ² + 3ελ − 1): ε > 0 is the unstable sign.

### 1.2 The regular family (Rigorous)

Regularity at the north pole (a → 0 with a′ → 1, no conical defect) admits the series a = τ + c₃τ³ + c₅τ⁵ + …; substituting into (T) gives at order τ²:

c₅ = c₃(6c₃ε + 6c₃ + 1)/(20ε),

and every higher coefficient is likewise determined by c₃. So the regular solutions form a **one-parameter family** labelled by c₃ (Hawking–Hertog–Reall's shooting parameter f‴(0) = 6c₃), with the sphere at c₃ = −1/6 (c₅ = 1/120 ✓). The no-boundary condition also kills the radiation constant of the 00-constraint (HHR: "the no boundary proposal has singled out a particular class of quantum states for us, namely those that do not contain any radiation" — **verified this session**), which is why the trace equation alone, with the regular series, is the complete problem. As ε → 0 the series degenerates (c₅ ∝ 1/ε): the fourth-order equation collapses to the second-order one and the family to the sphere alone.

### 1.3 The reality condition (Rigorous)

Equation (T) is invariant under τ → 2τ_e − τ (only even numbers of τ-derivatives occur). A solution whose Cauchy data at τ_e satisfy a′(τ_e) = a‴(τ_e) = 0 is therefore even about τ_e, and a(τ_e + it) is real: τ_e is a **real junction** (K = 0 there, and the Lorentzian continuation is a real closed FRW solution with ȧ = 0, ä = −a″(τ_e), a⃛ = 0). Conversely a real continuation needs all odd derivatives to vanish, so a′ = a‴ = 0 is necessary and sufficient. Two conditions on a one-parameter family: real junctions are isolated. Symmetry about τ_e also makes the full solution close smoothly at 2τ_e, so every real junction is half of a compact regular instanton; the converse fails (HHR's asymmetric double bubbles close smoothly but have no real junction).

## 2. The real caps

Shooting from the pole (§7, script 3; DOP853, rtol 10⁻¹⁰) over c₃ and ε, recording every extremum of a and the value of a‴ there:

- **ε < 0 (stable sign):** every regular solution has a single maximum; a‴ vanishes there only at c₃ = −1/6. The sphere is the only real cap. (Scanned ε = −0.5, −2; c₃ ∈ [−1, 0].)
- **0 < ε < ε_c:** same as above — single-peak solutions only; the sphere is the only real cap. (Scanned ε = 0.15, 0.20, 0.25, 0.30, 0.33, 0.35 with c₃ steps down to 5 × 10⁻⁴ around the birth point; at ε = 0.35 the family reaches an inflection — peak and neck coincide at c₃ = −0.346 — without crossing.)
- **ε > ε_c, ε_c ∈ (0.35, 0.36):** for c₃ below about −0.35 the solutions are double bubbles (maximum, minimum, maximum, closing), and a‴ at the neck changes sign at one c₃*(ε): the **symmetric double bubble**, a real junction at its neck. It is born at ε_c as a flat-topped cap (peak − neck = 4 × 10⁻⁴ at ε = 0.36) and develops a neck that shrinks like ≈ 0.58/√ε:

| ε | c₃* | a_peak | a_neck | τ_neck | neck continuation |
|---|---|---|---|---|---|
| 0.36 | −0.347204 | 0.8005 | 0.8001 | — | — |
| 0.40 | −0.350687 | 0.7819 | 0.7768 | — | — |
| 0.45 | −0.353077 | 0.7657 | 0.7497 | — | — |
| 0.50 | −0.354147 | 0.7543 | 0.7250 | 1.988 | recollapses, a_max = a_neck, t < 0.93 |
| 1 | −0.349489 | 0.7201 | 0.5585 | 2.106 | recollapses, t < 0.63 |
| 2 | −0.342261 | 0.7117 | 0.4095 | 2.169 | recollapses, t < 0.43 |
| 5 | −0.337009 | 0.7086 | 0.2619 | 2.204 | recollapses, t < 0.27 |
| 10 | −0.335180 | 0.7078 | 0.1849 | 2.214 | recollapses, t < 0.19 |

(a‴ at the neck ≤ 2 × 10⁻⁹ at the root in every row.) The Lorentzian continuation from the neck (script 3) is a closed universe that starts at its maximum radius and collapses to a → 0 within the quoted proper time — Hawking–Hertog–Reall's "rapidly collapses" (**verified this session**). No further symmetric solutions were found for c₃ ∈ [−1, 0.2]; solutions with c₃ ≥ 0 blow up (open-like) and are not compact.

This reproduces HHR's "if α < 0 then there are two regular compact instantons, namely the round four sphere and a new 'double bubble' instanton" (**verified**), adds the existence threshold, and identifies which double bubble is a junction.

## 3. The on-shell action

### 3.1 Minisuperspace action with exact normalization (Rigorous)

Write the metric as g = e^{2σ(η)} ḡ with ḡ the Einstein static universe dη² + dΩ₃² (conformal time; a = e^{σ}, σ′ = a_τ, σ″ = a a_ττ). The anomaly-induced (Riegert) action for the Euler anomaly on a conformally flat background reduces, since Ē₄ = □̄R̄ = 0 on ḡ and the Paneitz operator on functions of η is Δ̄₄σ = σ⁗ − 4σ″, to (a/16π²)∫√ḡ 2σΔ̄₄σ = (a/16π²)·2π²∫(2σ″² + 8σ′²)dη. The identity √g(E₄ − ⅔□R) = 4√ḡ Δ̄₄σ was checked symbolically against the τ-frame invariants of §1.1 (residual 0). With the Einstein–Hilbert term and an R² counterterm of coefficient κ,

L = −(6/(16πG)) e^{2σ}(1 + σ′²) + (a/16π²)(2σ″² + 8σ′²) + 36κ(1 − σ″ − σ′²)²  (per Vol(S³) = 2π²),

the Euler–Lagrange equation of L equals μ·√g·(T) *identically*, with μ = −a/(8π²), provided

**κ = −a(3ε + 1)/(288π²)**

(script 2; full residual 0). So κ = 0 is ε = −⅓, the Riegert functional's own −⅔□R; every other ε is an R² counterterm, and the unstable sign ε > 0 means κ < 0.

### 3.2 The anomaly action, computed with a compact reference (Rigorous)

The Riegert functional gives W[g] − W[ḡ] for g = e^{2σ}ḡ. With a *non-compact* reference (the Einstein static universe of §3.1) the by-parts steps that produce 2σ″² + 8σ′² leave boundary terms at η → ±∞ whose finite parts depend on the cap; the original version of this note subtracted the divergent ∫8 dη and dropped those terms, which is wrong by a cap-dependent amount (this is the correction recorded above). The unambiguous choice is the *round unit S⁴* as reference: every closed FRW cap is g = e^{2σ̂} ĝ with ĝ = sech²η (dη² + dΩ₃²) and σ̂ = ln(a(η) cosh η), which is smooth on the compact sphere, so there are no boundary terms and W[cap] − W[S⁴] = Γ[σ̂] with

Γ[σ̂] = (a/16π²) ∫√ĝ [ σ̂ Ê₄ + 2σ̂ Δ̂₄ σ̂ ],  Ê₄ = 24,  Δ̂₄ = □̂² − 2□̂ on the unit S⁴,

or, integrating by parts on the compact sphere (Rigorous): Γ/a = ⅛ ∫ [24 sech⁴η σ̂ + 2(σ̂″ − 2 tanh η σ̂′)² + 4 sech²η σ̂′²] dη, with primes d/dη = a d/dτ. Two identities check the normalization and sign: a sphere of radius r (σ̂ = ln r) gives Γ = 4a ln r, the Gauss–Bonnet value ∫√g⟨T⟩ = −4a integrated against the scale; and a Möbius boost of the sphere (a = sech(η − η₀), a conformal isometry) gives Γ = 0 to 10⁻¹⁶ (script 4). The shift ambiguity of conformal time is therefore harmless, as it must be.

**Scaling identity (Rigorous).** Under a constant rescaling a → λa of a compact regular solution, I_EH → λ² I_EH, the R² term is invariant, and Γ → Γ + 4a ln λ (the anomaly). A solution extremizes the action under this variation, so 2I_EH + 4a = 0: **I_EH = −2a for every compact regular cap**, sphere or double bubble. The numerics confirm it to 10⁻⁵ (script 4). The Einstein–Hilbert piece therefore never contributes to a difference between caps; only the anomaly piece Γ and the R² piece do.

**The sphere.** I_EH = −2a; Γ = 0 (it is the reference); R² piece 192κ·2π² = −(4/3)(3ε + 1)a. So, in this scheme, I(S⁴) = −a(10/3 + 4ε); the ε-slope −4a is ∫√g R² = 384π² on the unit sphere times dκ/dε (the on-shell Hellmann–Feynman relation). The absolute value carries the reference constant W[S⁴] and the scheme log noted in #216; differences at fixed ε do not.

### 3.3 The double bubble (Rigorous (numerical))

Computed on the half cap (pole to neck, doubled by symmetry) to avoid the numerically fragile south pole; the reflection symmetry at the neck holds to a‴ ≲ 10⁻⁴ at each root (script 4).

| ε | ΔR² piece /a | ΔΓ (anomaly) /a | ΔI/a = (I_DB − I_S⁴)/a | original (wrong) value | dominant (Euclidean weight) |
|---|---|---|---|---|---|
| 0.36 | −0.709 | +0.587 | **−0.122** | −2.709 | double bubble |
| 0.40 | −0.859 | +0.693 | −0.166 | −2.991 | double bubble |
| 0.45 | −1.050 | +0.822 | −0.228 | −3.319 | double bubble |
| 0.50 | −1.245 | +0.945 | −0.299 | −3.625 | double bubble |
| 1 | −3.237 | +1.922 | −1.314 | −6.152 | double bubble |
| 2 | −7.251 | +3.106 | −4.144 | −10.430 | double bubble |
| 5 | −19.277 | +4.843 | −14.434 | −22.590 | double bubble |
| 10 | −39.295 | +6.215 | −33.080 | −42.638 | double bubble |

The anomaly piece *opposes* the double bubble (Γ > 0: the cap's conformal factor relative to the sphere costs anomaly action), and the R² piece favors it by more; the sign of the total is set by the R² term for every ε > ε_c. **The gap is finite but small at birth** (−0.12a; the flat-topped cap at ε = 0.36 is close to the sphere in action, not in geometry) and grows to ≈ −3.3ε a at large ε. With a = a₂/180 ≥ 5.6 × 10³ the ratio of no-boundary weights e^{−ΔI} is ≥ e^{680} at birth and e^{7 × 10³} at ε = 1: dominance switches at ε_c as before, decisively, but by a factor two to twenty smaller in the exponent than the original note claimed. The independent computation by the position-H agent of the J-6 debate (compact reference, pole-cutoff convergence, finite-difference cross-check) reproduces every entry to three digits.

## 4. Interpretation

1. **Why the ordering is structural.** The Euclidean R² term contributes 36κ∫(1 − σ″ − σ′²)² dη = κ∫√g R²/(2π²) with κ < 0 for ε > −⅓: for the unstable sign the Euclidean action is unbounded below on high-curvature configurations. The double bubble is the regular saddle that exploits this — its neck is a region of large R — and its R² action decreases without bound as ε grows and the neck shrinks, faster than the anomaly piece (which opposes it) can compensate. The instability of de Sitter (Lorentzian) and the dominance of the small-neck cap (Euclidean) are the same sign choice seen twice.
2. **Root dominance, not the reality condition, is what constrains ε.** The reality condition admits the sphere at every ε and the double bubble at every ε > ε_c; neither selects a value. Uniqueness of the real root — the premise of the tree argument (J-6) and of the reframing's "single Euclidean state" — holds iff ε < ε_c. Dominance is stated in the no-boundary *measure* on histories (Hartle–Hawking–Hertog's e^{−2I_R} weighting): the two real junctions sit at different 3-geometries (radius 1 versus a_neck < 0.8), so at the sphere's own equator the double bubble does not contribute at all; what the measure compares is the inflating history against the recollapsing one.
3. **The bound and the depth.** ε < ε_c ≈ 0.355 ⟺ M > H₀/√ε_c ≈ 1.68 H₀ ⟺ |β_tot| < ε_c a₂/(1440π²) ≈ 25 (a₂ = 10⁶). Step 0 gave N_inf ≈ ln(M_P/H₀)/λ₊(ε) with λ₊ = [−3 + √(9 + 4/ε)]/2; at ε_c, λ₊ = 0.75 and N_inf ≈ 5.0 (a₂ = 10⁶), 6.5 (a₂ = 10⁷). Sixty e-folds needed ε ≈ 5 (step-0 table), where the double bubble dominates by e^{8 × 10⁴} (a₂ = 10⁶). **Under Euclidean weighting, a unique root and a long inflationary phase are mutually exclusive at this junction.** (Sketch: the seed estimate δH_i/H₀ ~ H₀/M_P is inherited from step 0; the bound on ε is Rigorous (numerical), its translation into e-folds is not.)
4. **What survives of the reframing's root.** For ε < ε_c the picture is exactly as proposed — one Euclidean state, the sphere, a K = 0 equator, an unstable de Sitter branch — but short: the branch exits within a few e-folds. For ε > ε_c the no-boundary state is dominated by a cap whose branch recollapses immediately; the sphere is a subdominant saddle. Either way the reframing cannot use the anomaly root to supply a long inflationary history without a change of saddle prescription.

**Caveats (all disclosed, none resolved here).** (i) Euclidean weighting: under the Lorentzian / Picard–Lefschetz definition of the no-boundary state the relevant saddles are picked by steepest-descent thimbles and the Euclidean sign can invert (Feldbrugge–Lehners–Turok 2017; Di Tucci–Lehners 2019 — verified earlier in this cycle); whether the double bubble contributes there, and with what sign, is J-6's saddle question and must be settled before the bound is treated as final. (ii) Minisuperspace: no perturbations; HHR note the double bubble's perturbation analysis is hard. (iii) Only reflection-symmetric caps are junctions; asymmetric compact instantons exist and contribute to Ψ at Euclidean-region data but not to any real history. (iv) ε is the total □R coefficient including the anomaly's scheme-dependent b′ term; the physical statement is about the sum, which is what the trace equation and the exit see. (v) The threshold ε_c and the actions are numerical; the S⁴ analytic check, the scaling identity I_EH = −2a, the two Riegert identities, and the a‴ ≈ 0 residuals bound the error at the 10⁻⁴ level, and ε_c is bracketed by direct scans on both sides. (vi) The original anomaly-action regularization was wrong; see the correction notice and §3.2.

## 5. Consequences for the program

- **J-1 done-condition:** outcome (a), as an inequality: the junction constrains k₃ (α_{R²}) through root dominance to 0 < ε < ε_c ≈ 0.355, i.e. M > 1.68 H₀. The resulting branch scale is not new (it is H₀ with a short de Sitter phase) and no exponent is generated; the mass residue of #216 stands.
- **J-6 is now load-bearing, not interpretive:** root uniqueness is a quantitative condition on the coupling under Euclidean weighting, and the Lorentzian prescription could change it. The saddle commitment should be made with the double bubble in hand.
- **Upstream:** `fixed-point-existence` should record that the anomaly-plus-R² theory's Euclidean sector has two regular symmetric instantons for ε > ε_c and that the physically required sign makes the action unbounded below on the double-bubble branch (HHR 2001 is the citation; the threshold and the action ordering are new here). `co-emergence`'s m_eff ~ √ξ H₀ is unaffected.
- **For the mass question (#216):** N_inf ≲ 5–7 removes the "reach" of any branch-side ladder from the anomaly root; the residue is unchanged.

## 6. Self-checks

- **Dimensional:** ε, c₃ (in H₀ = 1 units), I/a all dimensionless ✓; the physical action is I = a × (table value), a = a₂/180.
- **Limiting cases:** ε → 0: the family degenerates to the sphere (c₅ ∝ 1/ε) ✓; ε < 0: sphere only, de Sitter stable — no exit and no competitor, consistent ✓; ε = −⅓: κ = 0, the pure Riegert functional ✓; the sphere's action reproduces the Einstein–Hilbert piece −2π/(GH₀²) of #216's attack-C ✓; the Lorentzian linearization reproduces step 0 ✓.
- **Consistency with the record and literature:** HHR's two-instanton statement for α < 0, the "no radiation" selection, and the double bubble's rapid recollapse — all verified verbatim this session; the sphere's ε-independence matches `fpe-starobinsky-existence`; nothing merged is contradicted.
- **Numerical validation:** the sphere's Einstein–Hilbert and R² pieces are reproduced to 10⁻⁵ and its anomaly piece vanishes to 10⁻¹¹ with the compact-reference functional; the scaling identity I_EH = −2a holds to 10⁻⁵ on every double bubble; the Riegert functional reproduces 4a ln r on a rescaled sphere and vanishes on Möbius boosts to 10⁻¹⁶; a‴ at the neck vanishes to ≲ 10⁻⁴ at each root on the half-cap runs; the Euler–Lagrange/trace-equation match and the Riegert identity are exact symbolic identities. The first version of this note used a regularization that failed the Möbius test implicitly and was corrected the same day.
- **Hidden assumptions:** Euclidean weighting (disclosed, routed to J-6); FRW minisuperspace foliation (inherited from the reframing, disclosed in #216 §4); the seed estimate in N_inf (Sketch); no time evolution asserted beyond classical continuation of a saddle.

## 7. Scripts (numpy/scipy/sympy; run 2026-09-05/06)

### Script 1 — curvature invariants of Euclidean closed FRW
```python
import sympy as sp
tau,chi,th,ph=sp.symbols('tau chi theta phi')
a=sp.Function('a')(tau)
x=[tau,chi,th,ph]
g=sp.diag(1,a**2,a**2*sp.sin(chi)**2,a**2*sp.sin(chi)**2*sp.sin(th)**2)
ginv=g.inv()
n=4
Gam=[[[sp.simplify(sum(ginv[i,l]*(sp.diff(g[l,j],x[k])+sp.diff(g[l,k],x[j])-sp.diff(g[j,k],x[l])) for l in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]
def Riem(i,j,k,l):  # R^i_{jkl}
    e=sp.diff(Gam[i][j][l],x[k])-sp.diff(Gam[i][j][k],x[l])
    e+=sum(Gam[i][k][m]*Gam[m][j][l]-Gam[i][l][m]*Gam[m][j][k] for m in range(n))
    return sp.simplify(e)
Ric=sp.Matrix(n,n,lambda j,l: sp.simplify(sum(Riem(i,j,i,l) for i in range(n))))
R=sp.simplify(sum(ginv[j,l]*Ric[j,l] for j in range(n) for l in range(n)))
Ric2=sp.simplify(sum(Ric[j,l]*Ric[m,p]*ginv[j,m]*ginv[l,p] for j in range(n) for l in range(n) for m in range(n) for p in range(n)))
# Riemann squared
Rdown={}
for i in range(n):
  for j in range(n):
    for k in range(n):
      for l in range(n):
        Rdown[(i,j,k,l)]=sp.simplify(sum(g[i,m]*Riem(m,j,k,l) for m in range(n)))
Riem2=0
for i in range(n):
  for j in range(n):
    for k in range(n):
      for l in range(n):
        Riem2+=Rdown[(i,j,k,l)]**2*ginv[i,i]*ginv[j,j]*ginv[k,k]*ginv[l,l]
Riem2=sp.simplify(Riem2)
E4=sp.simplify(Riem2-4*Ric2+R**2)
C2=sp.simplify(Riem2-2*Ric2+R**2/3)
boxR=sp.simplify(sp.diff(a**3*sp.diff(R,tau),tau)/a**3)
print("R      =",sp.factor(R))
print("Ric^2  =",sp.factor(Ric2))
print("E4     =",sp.factor(E4))
print("Weyl^2 =",C2)
print("boxR   =",sp.factor(boxR))
# checks on the round S^4: a = sin(H tau)/H
H=sp.symbols('H',positive=True)
sub={a:sp.sin(H*tau)/H}
def ev(e): return sp.simplify(e.subs(a,sp.sin(H*tau)/H).doit())
print("S4 check: R=",ev(R)," E4=",ev(E4)," boxR=",ev(boxR))
import pickle; pickle.dump({'R':R,'E4':E4,'boxR':boxR,'Ric2':Ric2},open('curv.pkl','wb'))
```

### Script 2 — minisuperspace action: Riegert identity and normalization match
```python
import sympy as sp, pickle
eta=sp.symbols('eta'); s=sp.Function('sigma')(eta)
G,aa,kap,s1=sp.symbols('G a_anom kappa s1'); epsl=sp.symbols('epsilon')
sd=sp.diff(s,eta); sdd=sp.diff(s,eta,2)
X0,X1,X2=sp.symbols('X0 X1 X2')
L_EH=-(sp.Integer(6)/(16*sp.pi*G))*sp.exp(2*X0)*(1+X1**2)
L_an=s1*(aa/(16*sp.pi**2))*(2*X2**2+8*X1**2)
L_R2=36*kap*(1-X2-X1**2)**2
L=L_EH+L_an+L_R2
back={X0:s,X1:sd,X2:sdd}
EL=sp.diff(L,X0).subs(back)-sp.diff(sp.diff(L,X1).subs(back),eta)+sp.diff(sp.diff(L,X2).subs(back),eta,2)
EL=sp.expand(EL.doit())
# identity check: e^{4 sigma}(E4 - 2/3 box R) == 4 Delta4bar sigma on the ESU frame?
Rg=sp.exp(-2*s)*(6-6*sdd-6*sd**2)
boxRg=sp.exp(-4*s)*sp.diff(sp.exp(2*s)*sp.diff(Rg,eta),eta)
# get E4 honestly from the tau-frame invariants via the chain rule: use pickled E4 in terms of a(tau), convert with a(tau)=e^{sigma(eta)}, d/dtau = e^{-sigma} d/deta
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
A=[sp.exp(s)]
for k in range(4): A.append(sp.exp(-s)*sp.diff(A[-1],eta))   # A[k] = d^k a/dtau^k expressed in eta
rep={sp.Derivative(a,(tau,4)):A[4],sp.Derivative(a,(tau,3)):A[3],sp.Derivative(a,(tau,2)):A[2],sp.Derivative(a,tau):A[1]}
E4g=sp.simplify(d['E4'].subs(rep).subs(a,A[0]))
Rchk=sp.simplify(d['R'].subs(rep).subs(a,A[0])-Rg); print("R consistency (tau->eta):",Rchk)
boxchk=sp.simplify(d['boxR'].subs(rep).subs(a,A[0])-boxRg); print("boxR consistency:",boxchk)
ident=sp.simplify(sp.exp(4*s)*(E4g-sp.Rational(2,3)*boxRg)-4*(sp.diff(s,eta,4)-4*sdd)); print("Riegert identity residual:",ident)
TR=sp.expand(sp.simplify(sp.exp(4*s)*(Rg-sp.Rational(1,2)*E4g-epsl*boxRg)))   # trace equation * sqrt(g), H0=1 units (G a_anom = pi)
ELs=sp.expand(EL.subs(G,sp.pi/aa))
# match: EL = mu * TR. Compare coefficients of sigma'''' and of the no-derivative term
zero={sp.diff(s,eta,4):0,sp.diff(s,eta,3):0,sdd:0,sd:0}
mu=sp.simplify(ELs.subs(zero)/TR.subs(zero)); print("mu from no-derivative terms:",mu)
c4=sp.simplify(ELs.coeff(sp.diff(s,eta,4))/TR.coeff(sp.diff(s,eta,4))); print("ratio of sigma'''' coefficients:",c4)
sol=sp.solve([sp.Eq(c4,mu)],[kap],dict=True); print("kappa(eps,s1):",sol)
for S1 in (1,-1):
    for so in sol:
        resid=sp.simplify((ELs-mu*TR).subs(so).subs(s1,S1))
        print("s1=",S1," full residual:",resid)
pickle.dump({'L':L,'mu':mu,'sol':sol},open('action2.pkl','wb'))
```
Output: `R consistency 0`, `boxR consistency 0`, `Riegert identity residual 0`, `mu = -a_anom/(8*pi**2)`, `kappa = (-3*a_anom*epsilon - a_anom*s1)/(288*pi**2)` with `s1 = 1` giving `full residual 0`.

### Script 3 — regular family, real caps, actions, neck continuation
```python
import sympy as sp, pickle, numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq
d=pickle.load(open('curv.pkl','rb')); tau=sp.symbols('tau'); a=sp.Function('a')(tau)
R,E4,boxR=d['R'],d['E4'],d['boxR']; eps=sp.symbols('epsilon')
A0,A1,A2,A3,A4=sp.symbols('A0 A1 A2 A3 A4',real=True)
rep={sp.Derivative(a,(tau,4)):A4,sp.Derivative(a,(tau,3)):A3,sp.Derivative(a,(tau,2)):A2,sp.Derivative(a,tau):A1}
odeE=sp.numer(sp.together(R-sp.Rational(1,2)*E4-eps*boxR)).subs(rep).subs(a,A0)
FE=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeE,A4)[0],'numpy')
# Lorentzian continuation: a' -> -i adot, a''-> -addot, a'''-> i adddot, a''''-> addddot
I=sp.I
odeL=sp.expand(odeE.subs({A1:-I*A1,A2:-A2,A3:I*A3}))
assert not odeL.has(I), 'Lorentzian continuation not real'
FL=sp.lambdify((A0,A1,A2,A3,eps),sp.solve(odeL,A4)[0],'numpy')
c3s=sp.symbols('c3'); c5=c3s*(6*c3s*eps+6*c3s+1)/(20*eps)
c7=sp.solve(60*c3s**3*eps+36*c3s**3+9*c3s**2-136*c3s*c5*eps+120*c3s*c5+10*c5-448*sp.Symbol('c7')*eps,sp.Symbol('c7'))[0]
c5f=sp.lambdify((c3s,eps),c5); c7f=sp.lambdify((c3s,eps),sp.simplify(c7))
def rhsE(t,y,e): return [y[1],y[2],y[3],FE(y[0],y[1],y[2],y[3],e)]
def rhsL(t,y,e): return [y[1],y[2],y[3],FL(y[0],y[1],y[2],y[3],e)]
def run(c3,e,t0=2e-3,tmax=25.0,dense=False):
    C5,C7=c5f(c3,e),c7f(c3,e)
    y0=[t0+c3*t0**3+C5*t0**5+C7*t0**7, 1+3*c3*t0**2+5*C5*t0**4+7*C7*t0**6, 6*c3*t0+20*C5*t0**3+42*C7*t0**5, 6*c3+60*C5*t0**2+210*C7*t0**4]
    ext=lambda t,y,e: y[1]; ext.direction=0
    close=lambda t,y,e: y[0]-1e-4; close.terminal=True; close.direction=-1
    blow=lambda t,y,e: y[0]-40.0; blow.terminal=True
    s=solve_ivp(rhsE,(t0,tmax),y0,args=(e,),method='DOP853',rtol=1e-10,atol=1e-13,events=[ext,close,blow],dense_output=dense)
    return [(t,*y) for t,y in zip(s.t_events[0],s.y_events[0])],len(s.t_events[1])>0,s
def neck_a3(c3,e):
    ex,cl,s=run(c3,e); return ex[1][4] if len(ex)>=3 else np.nan
# action density per 2 pi^2, in units H0=1 with G a_anom = pi; report I/a_anom (multiply by a2/180 for the physical action)
def Ifull(sol,e,tmax):
    # L = -(6/(16 pi G)) e^{2s}(1+s'^2) + (a/16pi^2)(2 s''^2 + 8(s'^2-1)) + 36 kappa (1-s''-s'^2)^2 ; d eta = d tau / a
    # divide by a_anom: 1/G = a_anom/pi -> -(6/(16 pi^2)) ; (1/(16 pi^2)) ; kappa/a = -(3e+1)/(288 pi^2)
    ts=np.linspace(sol.t[0],tmax,20001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    sp1=A1; sp2=A*A2
    L=(-(6/(16*np.pi**2))*A**2*(1+sp1**2) + (1/(16*np.pi**2))*(2*sp2**2+8*(sp1**2-1)) + 36*(-(3*e+1)/(288*np.pi**2))*(1-sp2-sp1**2)**2)/A
    return 2*np.pi**2*trapezoid(L,ts)
def IS4(e): return -(5+4*e)   # analytic, per a_anom, full sphere
res={}
for e in (0.25,0.5,1.0,2.0,5.0,10.0):
    # S4 numeric check
    ex,cl,s=run(-1/6,e,dense=True); IS4num=Ifull(s,e,s.t_events[1][0])
    # bracket the neck-symmetric root
    grid=np.linspace(-0.50,-0.28,12); vals=[neck_a3(c,e) for c in grid]; br=None
    for i in range(len(grid)-1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1]<0: br=(grid[i],grid[i+1]); break
    if br is None:
        print(f"eps={e}: no root; vals",[round(v,2) if np.isfinite(v) else None for v in vals]); continue
    c3r=brentq(neck_a3,br[0],br[1],args=(e,),xtol=1e-9)
    ex,cl,s=run(c3r,e,dense=True); (t1,a1,_,a1dd,_),(t2,a2,_,a2dd,a2ddd)=ex[0],ex[1]
    tclose=s.t_events[1][0]; IDB=Ifull(s,e,tclose)
    # Lorentzian continuation from the neck: adot=0, addot=-a''_E, adddot=0
    yL=[a2,0.0,-a2dd,0.0]
    stopL=lambda t,y,e: y[0]-1e-3; stopL.terminal=True; stopL.direction=-1
    growL=lambda t,y,e: y[0]-50.0; growL.terminal=True
    sL=solve_ivp(rhsL,(0,60),yL,args=(e,),method='DOP853',rtol=1e-9,atol=1e-12,events=[stopL,growL])
    fate="recollapse" if len(sL.t_events[0]) else ("grows to 50" if len(sL.t_events[1]) else "neither by t=60")
    amax=sL.y[0].max()
    res[e]=dict(c3=c3r,a_peak=a1,tau_neck=t2,a_neck=a2,IS4=IS4(e),IS4num=IS4num,IDB=IDB,fate=fate,amax=amax,tL=sL.t[-1])
    print(f"eps={e:5.2f} c3*={c3r:+.6f} peak a={a1:.4f} neck a={a2:.4f} (tau={t2:.4f}, a'''={a2ddd:+.1e}) | I_S4/a: analytic {IS4(e):+.4f} numeric {IS4num:+.4f} | I_DB/a = {IDB:+.4f} | dI=(I_DB-I_S4)/a = {IDB-IS4(e):+.4f} -> {'S4 dominates' if IDB>IS4(e) else 'DOUBLE BUBBLE dominates'} | neck continuation: {fate}, a_max={amax:.3f} at t<={sL.t[-1]:.2f}",flush=True)
pickle.dump(res,open('caps.pkl','wb'))
```
Output (ε ≥ 0.5) is the table of §2–§3; the threshold scans (`thresh.py`, `thresh2.py`, same functions on finer c₃ grids at ε ∈ [0.15, 0.45]) gave: no three-extremum solution for ε ≤ 0.35 (inflection at ε = 0.35, c₃ = −0.346); symmetric double bubble at ε = 0.36 (c₃* = −0.347204, peak 0.8005, neck 0.8001, I/a = −9.1487), 0.40 (−0.350687; 0.7819/0.7768; −9.5913), 0.45 (−0.353077; 0.7657/0.7497; −10.1189).

## References (exploratory tier; how checked)

- S. W. Hawking, T. Hertog, H. S. Reall, "Trace anomaly driven inflation," Phys. Rev. D 63, 083504 (2001), hep-th/0010232 — the two-instanton statement for α < 0, the double bubble's shape and recollapse, "no radiation," and the free parameter f‴(0): quoted from the ar5iv rendering this session. Their eq. (2.18) as rendered there did not reproduce the round sphere for α ≠ 0, so it was not used; the equation solved here is the trace equation derived in §1.
- A. A. Starobinsky, Phys. Lett. B 91, 99 (1980) — primary unreached (record); used only through the repo's Rigorous-by-citation existence/instability claim.
- R. J. Riegert, Phys. Lett. B 134, 56 (1984) — existence and abstract-level content verified by the attack pass on attempt B of the #216 cycle; the Euler-anomaly functional's minisuperspace form is derived and checked here rather than quoted.
- M. J. Duff, CQG 11, 1387 (1994), eq. (31) — anomaly coefficients (verified at full text in the #216 cycle).
- A. Linde, arXiv:2509.01675 — H₀⁻² = k₂/(2880π²), M⁻² = −k₃/(2880π²) (verified at full text at step 0).
- J. Feldbrugge, J.-L. Lehners, N. Turok, PRL 119, 171301 (2017); A. Di Tucci, J.-L. Lehners, PRL 122, 201302 (2019) — cited for caveat (i) only; verified with polarity in the #216 cycle.

### Script 4 — compact-reference anomaly action, identities, scaling law, half-cap gaps (the correction)
```python
import numpy as np
from scipy.integrate import trapezoid, cumulative_trapezoid
src=open('caps.py').read().split("res={}")[0]; exec(src)
def half_pieces(e,c3):
    ex,cl,sol=run(c3,e,dense=True)
    tsym=ex[1][0] if len(ex)>=3 else ex[0][0]          # neck for DB, equator for sphere
    ts=np.linspace(sol.t[0],tsym,400001); Y=sol.sol(ts); A,A1,A2=Y[0],Y[1],Y[2]
    EH=2*2*np.pi**2*trapezoid((-(6/(16*np.pi**2))*A**2*(1+A1**2))/A,ts)
    R2=2*2*np.pi**2*trapezoid((36*(-(3*e+1)/(288*np.pi**2))*(1-A*A2-A1**2)**2)/A,ts)
    eta=cumulative_trapezoid(1/A,ts,initial=0); eta-=eta[-1]                       # eta=0 at the symmetric point
    s=np.log(A)+np.log(np.cosh(eta)); s1=A1+np.tanh(eta); s2=A*A2+np.cosh(eta)**-2
    G=2*0.125*trapezoid((24*np.cosh(eta)**-4*s + 2*(s2-2*np.tanh(eta)*s1)**2 + 4*np.cosh(eta)**-2*s1**2)/A,ts)
    # symmetry check at the symmetric point: a''' there
    return EH,R2,G,(ex[0][1], ex[1][1] if len(ex)>=3 else None, ex[1][4] if len(ex)>=3 else ex[0][4])
H={0.36:-0.122,0.40:-0.166,0.45:-0.228,0.5:-0.299,1.0:-1.314,2.0:-4.144,5.0:-14.43}
print("sphere half*2:",[f"{x:+.5f}" for x in half_pieces(1.0,-1/6)[:3]])
for e,c3 in ((0.36,-0.347204),(0.40,-0.350687),(0.45,-0.353077),(0.5,-0.354147),(1.0,-0.349489),(2.0,-0.342261),(5.0,-0.337009),(10.0,-0.335180)):
    EH,R2,G,(ap,an,a3)=half_pieces(e,c3); dI=(EH+2)+(R2+(4/3)*(3*e+1))+G
    print(f"eps={e:5.2f}: dEH={EH+2:+.2e} dR2={R2+(4/3)*(3*e+1):+.4f} dGamma={G:+.4f} => dI/a={dI:+.4f}  (H: {H.get(e,float('nan')):+.3f})  [a_peak={ap:.4f} a_neck={an:.4f} a'''_neck={a3:+.1e}]")
```
Output: sphere half×2 pieces (−1.99999, −5.33333 at ε = 1, +0.00000); the table of §3.3 with dEH ≤ 3 × 10⁻⁵ in every row. The identity checks (4 ln r; Möbius → 10⁻¹⁶) are in `anom_s4ref2.py` on the scratch record.
