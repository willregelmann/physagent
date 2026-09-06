# Step 0 of #215: which junction is operative, and how deep is the root?

**Date:** 2026-09-05
**Issue:** #215 (experimenter-priority tracking issue for the Euclidean-cap / signature-change-junction program), step 0. Follows the explorer synthesis `2026-09-05-junction-mass-scale.md` (PR #216), which found that every attempt in that cycle had measured masses against a junction whose semiclassical validity nobody had checked.
**Role:** interactive session, experimenter-directed. Exploration, not a paper result: labels are given per claim; every external reference is exploratory-tier (Markdown), with how it was checked stated inline.
**Deliverables (per #215):** (i) the junction scale as a function of field content, with the two coefficient conventions reconciled and the field-content assumption stated; (ii) the de Sitter depth of the root, N_inf, from the fixed point's own instability; (iii) which junction the program commits to; and a recommendation on a program directory.

---

## Summary

1. **The junction scale is fixed by one weighted field count, and the paper's coefficient is standard.** With a₂ ≡ (N_S + 11N_F + 62N_V)/2 (N_F Dirac), the printed H₀² = 180π/(G a₂) equals H₀² = 360π M_P²/(N_S + 11N_F + 62N_V), i.e. H₀² = 2880π² M̄_P²/(N_S + 11N_F + 62N_V) in reduced Planck units. It reproduces the standard conformal-scalar de Sitter anomaly, Hawking–Hertog–Reall's eq. (2.19) for N=4 super-Yang–Mills (a₂ = 45N² → H² = 4π/(N²G)), and Linde's H₀⁻² = k₂/(2880π²) with k₂ = 2a₂. The "16π discrepancy" recorded in `fpe-starobinsky-coefficient` and #168 is 8π (Planck-mass convention) × 2 (definition of a₂ versus k₂). *(Rigorous arithmetic given the standard anomaly coefficients; see §1.)*
2. **For Standard-Model field content the junction is Planckian.** a₂ ≈ 498 gives H₀ ≈ 1.07 M_P ≈ 5.3 M̄_P. The range a₂ ∈ [10³, 10⁵] recorded in `fpe-fixed-point-is-inflationary` gives H₀/M̄_P ∈ [0.38, 3.8]. A semiclassical cap (H₀ ≤ 0.1 M̄_P) needs a₂ ≳ 1.4 × 10⁶, a weighted field count of order 3 × 10⁶ — for example N=4 super-Yang–Mills with N ≳ 180, or a pure gauge sector with ~5 × 10⁴ vector fields. *(Rigorous arithmetic; the 0.1 threshold is a convention — Sketch.)*
3. **The de Sitter depth of the root is not a property of the fixed point.** Linearizing the trace equation with a constant total □R coefficient gives one decaying mode and a pair whose sign is set by that coefficient; for the unstable sign the growth rate in Hubble units is λ₊ = [−3 + √(9 + 4M²/H₀²)]/2, with M the scalaron mass the □R coefficient defines (Linde: M⁻² = −k₃/(2880π²)). The number of e-folds before exit is N_inf ≈ ln(H₀/δH_i)/λ₊ ≈ 3(H₀²/M²) ln(M_P/H₀) for M ≪ H₀. **N_inf is set by the same free □R / R² coefficient that sets the exit scale.** Sixty e-folds at a₂ = 10⁶ needs M ≈ 0.44 H₀. Steps 0(ii) and 1 of #215 are therefore one question: the junction's free modulus controls both the depth of the root and the scale of the branch. *(Algebra Rigorous by sympy; the seed estimate and the use of the trace equation alone are Sketch; consistent with Hawking–Hertog–Reall's verbatim "by varying the coefficient of the R² counter term we can adjust the duration of inflation".)*
4. **Recommended commitment: junction A, the anomaly-driven fixed point, with large field content stated as an explicit input (a₂ ≥ 10⁶).** It is the only junction the framework's own equations produce. The alternatives are to import the observed Λ (junction B: not a fixed point of anything in the record, and sixty orders away) or to give up the semiclassical reframing (junction C). The cost of A is honest and should be written into every downstream done-condition: the field content is far from the Standard Model, and the required mass exponents against this junction are p ≈ 5–9 (a₂ = 10⁶), integer-ish, not the small rationals of the observed-Λ junction. *(Judgment; presented for the experimenter's acceptance at merge.)*
5. **Program directory:** recommended, after this PR merges, as `programs/no-boundary-junction/` with `notes/` only (early-stage convention), seeded by this note and the #216 synthesis, with OBJECTIVES mirroring #215. Proposal in §5; not executed here.

---

## 1. The junction scale as a function of field content

### 1.1 Conventions, unified

The trace anomaly of conformal matter, in the form used across the modern literature (Duff 1994, eq. 31 — full text verified by the attack pass on attempt C of the #216 cycle, 2026-09-05):

⟨T^μ_μ⟩ = (1/(16π²)) [ c C² − a E₄ ] + (□R term),  a = (N_S + 11N_F + 62N_V)/360,  c = (N_S + 6N_F + 12N_V)/120,

with N_S real scalars, N_F Dirac fermions (a Weyl fermion counts 1/2), N_V vector fields. On de Sitter with Hubble rate H: C² = 0, E₄ = R_μνρσ² − 4R_μν² + R² = 24H⁴ − 144H⁴ + 144H⁴ = 24H⁴, so ⟨T⟩ = −24aH⁴/(16π²) = −3aH⁴/(2π²).

The fixed-point-existence paper writes ⟨T⟩ = −a₂H⁴/(120π²) (`index.tex` §Starobinsky). Matching: a₂/(120π²) = 3a/(2π²) ⟹ **a₂ = 180a = (N_S + 11N_F + 62N_V)/2.** (The paper's own rigor note says a₂ = 2880π² a, which is the same statement with the 1/(16π²) kept outside a.)

The trace of the semiclassical Einstein equation, −R = 8πG⟨T⟩, on de Sitter (R = 12H²) with no bare Λ:

12H₀² = 8πG · a₂H₀⁴/(120π²) ⟹ **H₀² = 180π/(G a₂) = 360π M_P²/(N_S + 11N_F + 62N_V)**, M_P = G^{−1/2}.

In reduced units M̄_P² = M_P²/(8π): **H₀² = 2880π² M̄_P²/(N_S + 11N_F + 62N_V).**

### 1.2 Three independent checks

| Check | Source | Result |
|---|---|---|
| One conformal scalar (a₂ = 1/2) | Standard de Sitter result ⟨T⟩ = −H⁴/(240π²) for the conformally coupled massless scalar (Bunch–Davies; from memory, **not re-verified this session**) | −(1/2)H⁴/(120π²) = −H⁴/(240π²) ✓ |
| N=4 SU(N) super-Yang–Mills: N_S = 6N², N_F = 2N² (4N² Weyl), N_V = N² → a₂ = 45N² | Hawking–Hertog–Reall 2001, hep-th/0010232, eq. (2.19): R² = N²G/(4π), H = R⁻¹ (**verified this session** from the ar5iv rendering) | H₀² = 180π/(45N²G) = 4π/(N²G) ✓ |
| Linde 2025, arXiv:2509.01675: H₀⁻² = k₂/(2880π²), "Planck mass units M_P = 1" (**verified this session** at full text; k₂'s definition in terms of species is not given there — "a contribution of each type of particles is O(1)") | reduced-unit formula above | H₀⁻² = (N_S + 11N_F + 62N_V)/(2880π² M̄_P²) ⟹ **k₂ = 2a₂**, provided Linde's M_P is the reduced mass, which is his standard convention ✓ |

**Conclusion for #168 (Sketch → Rigorous-by-two-independent-normalizations, pending the unreachable 1980 primary):** the printed coefficient is correct as written once a₂ is defined as half the weighted field count; the recorded 16π discrepancy is 8π × 2. The a₂ > 0 positivity condition is automatic for standard conformal matter (all three weights positive).

### 1.3 Numbers

| Field content | N_S + 11N_F + 62N_V | a₂ | H₀/M_P | H₀/M̄_P |
|---|---|---|---|---|
| Standard Model (no ν_R): 4, 22.5, 12 | 995.5 | 498 | 1.07 | 5.3 |
| Standard Model + 3 ν_R: 4, 24, 12 | 1012 | 506 | 1.06 | 5.3 |
| Recorded range floor, a₂ = 10³ | 2000 | 10³ | 0.75 | 3.8 |
| Recorded range ceiling, a₂ = 10⁵ | 2 × 10⁵ | 10⁵ | 0.075 | 0.38 |
| Semiclassical (H₀ = 0.1 M̄_P) | 2.8 × 10⁶ | 1.4 × 10⁶ | 0.020 | 0.10 |
| N=4 SYM, N = 180 | 2.9 × 10⁶ | 1.46 × 10⁶ | 0.020 | 0.098 |
| a₂ = 10⁷ | 2 × 10⁷ | 10⁷ | 0.0075 | 0.038 |

*(Rigorous arithmetic.)* Two consequences for the record: (a) `fpe-fixed-point-is-inflationary`'s hypothesis "a₂ ~ 1e3 to 1e5, realistic magnitude" places the fixed point at or above the reduced Planck scale; "realistic" should read "large-N", and the claim's derivation field should carry the reduced-unit number. (b) The Standard Model is nowhere near the semiclassical regime; the framework's Level-2 fixed point exists for Standard-Model content but is a Planckian object there.

**Semiclassical validity, as an explicit input.** Taking H₀ ≤ 0.1 M̄_P as the criterion (curvature R = 12H₀² ≤ 0.12 M̄_P²; a convention, Sketch): a₂ ≥ 1440π²/0.01 ≈ 1.4 × 10⁶. Hawking–Hertog–Reall state the same requirement verbatim: the universe "can be nucleated semi-classically by a cosmological instanton that is much larger than the Planck scale provided there are sufficiently many matter fields" (**verified this session**). The framework does not derive field content (the paper's Axiom 2 says matter emerges from topology, labelled Conjecture; the March 2026 synthesis records field content as an admitted input). Large field content is therefore an input this program must state, not a result it can claim.

**Mass exponents against junction A.** With ε_J = (H₀/M_P)² = 180π/a₂: at a₂ = 10⁶, log₁₀ε_J = −3.25 and the required exponents p = log(m/M_P)/log ε_J are: electroweak scale 5.1, electron 6.9, neutrino 9.0, ρ_Λ^{1/4} 9.5; at a₂ = 10⁷ they drop by a factor 0.76. Integer-ish, as the #216 synthesis anticipated for this junction; the small rationals 1/6–1/4 belong to the observed-Λ junction only.

## 2. The de Sitter depth of the root

### 2.1 Setup

The trace equation on flat FRW, with the anomaly's E₄ term and a total □R coefficient β_tot (the scheme-dependent anomaly b′ term plus whatever R² counterterm is present — the two are not separable, since the variation of ∫√g R² contributes only to the trace and only through □R):

R = (G a₂/(360π)) E₄ − 8πG β_tot □R,   R = 6(Ḣ + 2H²),  E₄ = 24H²(Ḣ + H²),  □R = −(R̈ + 3HṘ).

De Sitter H = H₀ solves it iff 12H₀² = (Ga₂/(360π))·24H₀⁴, i.e. H₀² = 180π/(Ga₂) as in §1; the □R term vanishes identically there, which is why the fixed point's existence is independent of β_tot (`fpe-starobinsky-existence`, audit finding).

### 2.2 Linearization (Rigorous, sympy-checked; script in §6)

With H = H₀ + δ, δ ∝ e^{λH₀t}, and ε ≡ 8πG β_tot H₀² (sign convention: the sign of ε is the sign of the □R coefficient as it enters the trace equation above), the characteristic polynomial factors:

(λ + 4)(ε λ² + 3ε λ − 1) = 0.

So: λ = −4 (a decaying mode, present for any β_tot), and λ² + 3λ − 1/ε = 0. For ε < 0 both roots have negative real part and de Sitter is stable; for ε > 0 (the sign Hawking–Hertog–Reall call d < 0 for their R² counterterm; the same statement in their convention) there is exactly one growing mode,

**λ₊ = [−3 + √(9 + 4/ε)]/2** (in units of H₀),  λ₊ ≈ 1/√ε for ε ≪ 1,  λ₊ ≈ 1/(3ε) for ε ≫ 1.

*(Consistency: this reproduces the structure of Starobinsky's 1980 stability analysis as summarized by Hawking–Hertog–Reall — "the de Sitter solution is unstable" for one sign of the counterterm coefficient, and "by varying the coefficient of the R² counter term we can adjust the duration of inflation" — both verified verbatim this session. The 1980 primary text remains unreached, as the record notes.)*

**Identification of ε.** In reduced units (8πG = 1) the □R coefficient defines the scalaron mass, M² = 1/|β_tot| — in Linde's notation ⟨T⟩ ⊃ (k₃/(2880π²))□R and M⁻² = −k₃/(2880π²) (**verified this session**), so β_tot = k₃/(2880π²) and

**ε = H₀²/M².**

The two dimensionless numbers of the framework's gravitational sector are exactly Linde's two coefficients: k₂ = 2a₂ fixes H₀; k₃ (equivalently α_{R²}) fixes M and hence both the exit and, below, the depth. This is the "α_{R²}" the #216 synthesis named as the first coupling the junction should be asked about, now with its standard name and normalization.

### 2.3 The depth (Sketch)

A deviation seeded at δH_i grows as e^{λ₊H₀t}; the quasi-de Sitter phase ends when δH ~ H₀, after

**N_inf ≈ ln(H₀/δH_i)/λ₊.**

The seed is not fixed by the fixed point either. The natural estimate for a no-boundary root — the quantum uncertainty of H at the Hubble scale, δH_i/H₀ ~ H₀/M_P — gives ln(H₀/δH_i) = ln(M_P/H₀) = ½ ln(a₂/180π) (3.7 at a₂ = 10⁶; 4.9 at 10⁷). Then

N_inf ≈ ½ ln(a₂/180π) · [−3 + √(9 + 4M²/H₀²)]⁻¹ · 2  ≈  3 (H₀²/M²) ln(M_P/H₀)  for M ≪ H₀.

| a₂ | ln(M_P/H₀) | ε = H₀²/M² for N_inf = 60 | M/H₀ | equivalent β_tot = ε a₂/(1440π²) |
|---|---|---|---|---|
| 10⁵ | 2.6 | 7.6 | 0.36 | 54 |
| 10⁶ | 3.7 | 5.2 | 0.44 | 370 |
| 10⁷ | 4.9 | 3.9 | 0.51 | 2700 |

Reading: a root that lasts long enough to matter needs a scalaron somewhat lighter than H₀, i.e. a □R coefficient of order 10²–10³ in the natural normalization — large, exactly as Starobinsky's R² model needs a large R² coefficient. **Nothing in the framework fixes it; N_inf is a function N_inf(a₂, β_tot) of the free modulus, and "compute N_inf from the root's own instability" (the adaptation attempt C named) reduces to "fix β_tot", which is #215 step 1.**

Caveats, all Sketch: (i) the linearization is on flat slices; the first e-fold from the closed-slice equator (a₀ = 1/H₀) differs at O(1), irrelevant for N_inf ≫ 1; (ii) only the trace equation is used, following Starobinsky's analysis; the 00-constraint adds a radiation-like integration constant that does not alter the mode structure; (iii) the seed estimate is standard but not derived here; (iv) the exit is into a scalaron-dominated, then radiation, closed and Λ-free branch, per the #216 synthesis §6d — the ladder's reach 2N_inf inherits everything above.

## 3. Which junction the program commits to

| Option | What it is | Cost | Verdict |
|---|---|---|---|
| **A. Anomaly-driven fixed point, large field content (a₂ ≥ 10⁶)** | the framework's own Level-2 exact solution, made semiclassical by field content as in Hawking–Hertog–Reall | field content is an explicit input far from the Standard Model; mass exponents needed are p ≈ 5–9; the root's depth and exit scale both hang on the free □R coefficient | **Recommended.** The only junction the framework's equations produce; every downstream question (α_{R²}, OS across the equator, WKB on the branches) is well posed on it |
| B. Observed-Λ junction | Hartle–Hawking with Λ = Λ_obs | Λ_obs is not a fixed point of anything in the record (matching it would need a₂ ~ 10¹²⁴, `fpe-fixed-point-is-inflationary`); the framework's Level-2 result has no Λ input; adopting it imports the cosmological constant by hand | Rejected as the program's junction; retained only as the comparison case for the small-rational exponents (Weinberg–Zel'dovich) — a different test, to be kept separate |
| C. Planckian cap (Standard-Model content as is) | the fixed point at H₀ ≈ M_P | the semiclassical S⁴ cap, K = 0 equator, WKB branches and reflection positivity are all outside their validity; the reframing does not apply | Rejected; recorded so that nobody re-derives it |

**Commitment (recommended; the experimenter accepts or amends at merge):** junction A, with the standing assumption *"conformal field content with a₂ ≥ 10⁶ (weighted count N_S + 11N_F + 62N_V ≥ 2 × 10⁶), stated as an input"* written into every done-condition of #215 steps 1–3. Where a result depends on the value of a₂, it is computed as a function of a₂ and its validity range stated.

**What this changes upstream.** (a) `fpe-fixed-point-is-inflationary` should say "large-N" rather than "realistic" and carry the reduced-unit scale. (b) The co-emergence paper's m_eff ~ √(12(ξ − 1/6)) H₀ (`conj:mass_generation`) is, on junction A, a Planck-adjacent mass unless a₂ is large; the thesis's activation is unaffected, its scale is not what the paper's prose suggests. (c) The March 2026 mass-gap synthesis's "single scale ~H₀" is now "single scale H₀(a₂) with a₂ an input ≥ 10⁶."

## 4. Self-checks

- **Dimensional analysis:** H₀² = 180π/(G a₂) has dimensions of G⁻¹ = M_P², a₂ dimensionless ✓; ε = 8πGβ_totH₀² dimensionless ✓; N_inf dimensionless ✓.
- **Limiting cases:** a₂ → ∞ gives H₀ → 0 (flat space; the fixed point degenerates to the H = 0 double root recorded in `fpe-instability-as-static-modulus`) ✓; β_tot → 0 gives λ₊ → ∞ (instantaneous exit; the de Sitter phase has no duration without a □R term) and β_tot → ∞ gives λ₊ → 0 (eternal de Sitter) ✓, matching Hawking–Hertog–Reall's "if d = 0 inflation never ends" only in their sign convention — the sign bookkeeping between conventions is the one place a reader should recheck; a₂ = 45N² reproduces HHR eq. (2.19) ✓; a₂ = 1/2 reproduces the conformal-scalar de Sitter anomaly ✓.
- **Consistency with the record:** existence and instability of the fixed point (Rigorous by citation) are used, not re-derived; the coefficient's Sketch status is upgraded by two independent secondary normalizations, not by the primary; no merged result is contradicted; `fpe-fixed-point-is-inflationary`'s qualitative claim is confirmed and its "realistic" hypothesis corrected.
- **Order of magnitude:** Standard-Model content Planckian ✓ (this is the textbook reason the anomaly model needs large N); sixty e-folds needs β_tot ~ 10²–10³ ✓ (the same largeness as the R² model's coefficient).
- **Hidden assumptions:** flat-slice linearization (disclosed); trace equation alone (disclosed; Starobinsky's own route); seed δH_i/H₀ ~ H₀/M_P (disclosed, Sketch); no time evolution is asserted beyond the classical instability of a solution — the "depth" is the number of e-folds of a classical branch, a block property; no preferred foliation beyond FRW minisuperspace, inherited from the reframing and disclosed in #216 §4.

## 5. Proposed program directory (not executed here)

`programs/no-boundary-junction/` — status "Early notes"; `README.md` with scope (*self-consistency at a signature-change junction between a no-boundary Euclidean cap and Lorentzian branches; downstream of signature-change-boundary's fixed-background results and of fixed-point-existence's anomaly fixed point; upstream of co-emergence's mass, time and Hilbert-space questions*), `OBJECTIVES.md` with milestones J-0 (this note; done on merge), J-1 (α_{R²} / k₃ junction constraint — #215 step 1, now including N_inf as part of its done-condition), J-2 (side promotions, #215 steps 2a–2c), J-3 (junction selection beyond regularity), J-4 (reflection positivity across the K = 0 equator), J-5 (Page–Wootters gap localization), J-6 (orientation in its causal-order form; saddle-uniqueness commitment); `notes/` seeded with this file and a pointer to the #216 synthesis. Relations: informs co-emergence Open Problem 1, `conj:mass_generation`; informs FPE (`fpe-fixed-point-is-inflationary`, #168); informs SCB-6; contradicts nothing.

## 6. Script (sympy; run 2026-09-05)

```python
import sympy as sp
t,s=sp.symbols('t s'); H0,lam,eps=sp.symbols('H0 lambda epsilon',positive=True); q=sp.Symbol('q')
H=H0+s*q*sp.exp(lam*H0*t)
R=6*(sp.diff(H,t)+2*H**2); E4=24*H**2*(sp.diff(H,t)+H**2); boxR=-(sp.diff(R,t,2)+3*H*sp.diff(R,t))
B=sp.Symbol('B'); coeff=sp.Rational(1,2)/H0**2      # G a2/(360 pi) = 1/(2 H0^2) at the fixed point
eq=R-coeff*E4-B*boxR                                # trace equation; B = 8 pi G beta_tot (sign as it enters here)
assert sp.simplify(eq.subs(s,0))==0                 # de Sitter is a solution
lin=sp.simplify(sp.diff(eq,s).subs(s,0)/(q*sp.exp(lam*H0*t)))
print(sp.factor(sp.expand(lin.subs(B,eps/H0**2)/H0)))   # -> 6*(lambda + 4)*(epsilon*lambda**2 + 3*epsilon*lambda - 1)
```
Output: `6*(lambda + 4)*(epsilon*lambda**2 + 3*epsilon*lambda - 1)`.

## References (exploratory tier; how checked)

- A. A. Starobinsky, Phys. Lett. B 91, 99 (1980) — in the FPE bibliography; primary text unreached (record). Used only through the repo's Rigorous-by-citation existence/instability claim.
- M. J. Duff, "Twenty years of the Weyl anomaly," Class. Quantum Grav. 11, 1387 (1994), hep-th/9308075, eq. (31) — full text verified by the attack pass on attempt C, 2026-09-05 (scratch branch `scratch/explorer/2026-09-05-junction-mass-scale`, attack-C.md); not re-fetched here.
- S. W. Hawking, T. Hertog, H. S. Reall, "Trace anomaly driven inflation," Phys. Rev. D 63, 083504 (2001), hep-th/0010232 — eq. (2.19), the instability/counterterm statements, and the "sufficiently many matter fields" sentence verified this session from the ar5iv rendering.
- A. Linde, "Alexei Starobinsky and Modern Cosmology," arXiv:2509.01675 — H₀⁻² = k₂/(2880π²), M⁻² = −k₃/(2880π²), "Planck mass units M_P = 1," and the ~10¹⁰-species remark verified this session at full text; the species-decomposition of k₂ is not given there.
- T. S. Bunch and P. C. W. Davies, Proc. R. Soc. A 360, 117 (1978) — the conformal-scalar de Sitter ⟨T⟩ used as a check; **from memory, not verified this session**.
- A. Vilenkin, Phys. Rev. D 32, 2511 (1985) — existence verified (APS/PubMed/OSTI); content not used.
