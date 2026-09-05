# Steelman pass on Attempt A — "First-principles scale counting at the no-boundary junction"

**Target:** `/home/will/Projects/physagent/attempt-A-scale-counting.md`, against `/home/will/Projects/physagent/attack-A.md`
**Date:** 2026-09-05
**Role:** Steelman / defense pass (Pass 2 of METHODOLOGY "No Idea Is Eliminated Without a Defense"). For each of the attack's eighteen flaws: verdict, then the strongest honest rescue or a plain concession, with evidence. Line references `attempt:NN` / `attack:§N` as in the two files. Two scripts and their output are at the end; every number below comes from them or from the attack's script (which I re-ran mentally against mine; they agree where they overlap).

Summary verdict up front: the attack is right on the arithmetic (flaws 1, 6, 9), on the labels (3, 8, 11, 14, 17), and on the two structural collapses (1, 12a). It overreaches in three places — the citation polarity in flaw 3, the "never 0.16" argument in flaw 10, and the "no tension" reading it does not draw in flaw 13 — and in each of those the correct argument reaches a *sharper* negative than the attack stated. What survives is not the attempt's committed position ("the exponent lives in the state on Σ") but a set of four specific negatives plus a re-identified adaptation, stated in the "Surviving form" section.

---

## Flaw-by-flaw

### 1. ρ_Σ = (3/8π)M_P²H² is false with Λ input, tautological at the anomaly point

**Verdict: the attack is right; the "for free" relation is fatal as a mechanism. A narrower statement survives as a recorded negative.**

The arithmetic is not in dispute: with Λ input and K = 0, a_Σ = 1/H, the Friedmann constraint gives 8πGρ_Σ = 3H² − Λ = 0. The 2.2 meV is (Λ/8πG)^{1/4}, the cosmological-constant number, not a junction output. Conceded.

The brief asks whether any non-tautological reading of "the state on Σ carries the exponent" exists. I tried three:

- **Free fields, no-boundary state.** Halliwell–Hawking 1985 (verified: APS/PubMed summary) show the inhomogeneous modes start in their ground state as a consequence of the no-boundary condition — the state on Σ is the Euclidean (Bunch–Davies) vacuum, fixed by the geometry and the action with *no continuous parameter*. For conformal fields on the SO(5)-symmetric cap, ⟨T_μν⟩ = ¼⟨T⟩g_μν with ⟨T⟩ the local anomaly, so ρ_Σ = a_2H⁴/(480π²), and the constraint 3H² = 8πGρ_Σ reproduces exactly the printed H₀² = 180π/(G a_2) (script 1, block E). The attempt's §6(a) kill computation is therefore already finished, and it kills: (a) and (b) of §3 collapse to the fixed-point equation.
- **Massive free fields.** ⟨T_μν⟩ in the Bunch–Davies state on dS is known in closed form (Bunch–Davies 1978, in the repo bib) and carries the renormalization scale μ; this is flaw 2's territory. Still one equation.
- **Interacting fields.** HHH08 (attack-verified): the no-boundary weight selects φ₀ at the lower bound of the classical ensemble; the scale is V(φ₀)'s, imported.

So "the state on Σ" ⊆ "(geometry, action couplings)"; the attack's collapse to dimensional analysis is correct for the *positive* claim. What survives is the *negative*: **the no-boundary state adds no continuous datum beyond the action's couplings** (Rigorous by citation, HH85 + HHH08, for free fields and for the φ₀ label). That is a specific fact about the reframing's premise — the premise was that Σ might carry the mass datum — and belongs in the record even though the attempt's pointer is empty.

### 2. ρ_Σ = ρ(m) requires fixing the Λ counterterm

**Verdict: the attack is right in substance; one correction to its phrasing, which does not help the attempt.**

The correction: the counterterm is a dimensionless coefficient, Λ_bare = c_Λ M_P⁴ with the subtraction scale μ = M_P (which uses only G, already present). So adaptation (2) requires "fix a coupling, c_Λ = 0", which is *consistent* with the attempt's closing sentence (attempt:334-335), not contradictory as attack:§2 says. But it changes nothing: with c_Λ = 0 the bootstrap 3H² = 8πG ρ_BD(m, H; M_P) is one equation in (H, m). For m ≪ H the m⁴ log term is a correction of relative size ~(m/H)⁴/a_2 to the anomaly term; for m ≫ H the field decouples from a_2. No second relation appears at either end. The Zel'dovich Gm⁶ relation additionally assumes the m⁴ term is discarded and is ~7 orders too large by Zel'dovich's own account (Rugh–Zinkernagel, attack-verified). Adaptation (2) is closed: it was the cosmological-constant problem restated at Σ.

### 3. n is not gauge

**Verdict: the attack is right on the label; its Hayward citation has the polarity backwards; and the brief's proposed rescue (n as the dimensionless datum for a coupling) fails for a concrete reason — n is invariant but inert.**

*Invariance (Rigorous).* Under x⁰ ↦ f(x⁰) with f′(0) ≠ 0, λ̃ = λ(f)(f′)², so the order of vanishing n of g₀₀ (equivalently of det g) at Σ is preserved. The attempt's proper chart ũ = sgn(x⁰)|u| has dũ/dx⁰ = √|λ| → 0 at Σ; it is not a chart of the same smooth structure. In that chart g₀₀ = −sgn(ũ): the attempt's "n and c drop out" argument silently moved from the smooth degenerate class to the discontinuous class. Conceded.

*Citation polarity (METHODOLOGY, polarity-sensitive citations).* Hayward gr-qc/9303034 §IV (full text, extracted and read) does **not** say that N = t and N = ε represent different differential structures — that is Ellis et al.'s claim, which Hayward rejects: "this cannot be correct, since there is only one such differential structure on the real line, usually represented by a function with non-vanishing derivative. In terms of the line-element (20), N = t is such a function and N = ε is not." His point is that N = ε is not a coordinate at all. Same conclusion for the attack (the ũ chart is illegitimate), wrong attribution; the attack's quoted sentence is accurate but its framing sentence is Ellis's position. Flagged so it is not copied forward.

*Smooth class (Rigorous).* If λ is smooth and vanishes to finite order, λ = (x⁰)ⁿ × (smooth, nonvanishing) with n a positive integer, and a sign change needs n odd. The SCB seed note already records that "for non-odd n the sgn profile is only finitely differentiable at Σ" (seed note §1). n = 1 is Kossowski–Kriele's transverse class (det g vanishing to first order; KK 1993a, CQG 10, 1157, verified existence, content at search-summary level), the only one their theorems cover; n ≥ 3 is non-transverse.

*Inertness (Rigorous given the fixed background).* Everything at Levels 2–3 is n-blind once written in proper variables: the seed note's ν = ½ reduction gives mode functions {sin ku, cos ku} / {e^{±kv}} with the proper variable absorbing n; the canonical momentum is π = ∓dφ/d(proper), so the Dray–Manogue–Tucker matching [φ] = [π] = 0 is n-independent; the on-shell action and the curvature invariants on each side are functions of the proper geometry only. n enters exactly three places: the smoothness class of the atlas across Σ (Level 1), geodesic extendability (KK 1994, transverse only, Sketch in the SCB note), and the expanding note's boxed condition — which in proper variables is just "a is C² in u". There is no local field-theoretic handle on n. So n cannot feed a coupling by any mechanism in the record; it does not relocate the problem, it is simply not a candidate. The row's scale conclusion "none" stands; the §5 argument that leaned on "n is gauge" must be rebuilt (flaw 4).

### 4. Σ = {det g = 0} vs the K = 0 equator; nothing selects a single surface

**Verdict: (a) framing, with a substantive correction; (b) solvable — the degeneracy-breaking can be stated correctly; (c) conceded; (d) conceded.**

(a) The reframing's junction has two candidate realizations, and they are different differential structures at Σ. The Hartle–Hawking gluing is analytic continuation: the metric is analytic in complex τ and non-degenerate at the equator. Written as a *real* gluing in proper coordinates on each side it has g_TT = +1 (T < 0), −1 (T > 0) — Hayward's N = ε class — with the scale factor only C¹ across Σ (a_E = cos(HT)/H, a_L = cosh(HT)/H: values and first derivatives match, second derivatives differ in sign). The SCB smooth degenerate class (n odd) is a different structure. They are not "equivalent"; the attempt conflated them. What *is* realization-independent is K = 0 — the reality condition in HH, Hayward/Kossowski–Kriele's junction condition in the smooth class (flaw 13). "Σ = {det g = 0}" is correct only in the SCB realization.

(b) The correct restatement. Σ is a **moment of time symmetry**, K_ij = 0 — a tensorial condition on the 4-geometry that selects a surface class, not a foliation, exactly as the t = 0 slice of Schwarzschild is invariantly distinguished without Schwarzschild having a preferred foliation. In the SO(5)-symmetric cap (pure Λ, or the anomaly fixed point with conformal matter) every great S³ satisfies it and SO(5) permutes them transitively: the choice of Σ is *gauge* under the isometry group, and nothing is preferred. What breaks the degeneracy is not the cap and not a scalar condition — it is the **branch**: the Starobinsky instability's growing mode is homogeneous, so the Lorentzian history departs from dS(H_J) along an SO(4)-symmetric direction, and the surviving SO(4) fixes retroactively which great S³ was Σ. That is a solution-selected surface, the same way an FLRW solution of GR has a comoving slicing without GR having a preferred foliation: Axiom-2-safe in the standard sense. With non-conformal matter at φ₀ ≠ 0 the saddle is complex and there is no real Σ at all (flaw 14). The attempt's "a single surface selected by a scalar condition — including a self-consistency condition" is withdrawn; the attack's (c) is right that no such condition exists in the record.

(d) det g is a density (zero set invariant; repairable). The apparent-horizon analogy is wrong (Wald–Iyer, attack-verified); the right analogy is the moment of time symmetry above.

### 5. WKB time contradicts the paper; Σ + HJ flow = a foliation

**Verdict: solvable gap, and the combination can be tested rather than asserted; the test is Gerlach 1969.**

The paper's passage (index.tex:115-127) criticizes WKB time as a *derivation of quantum time* via Born–Oppenheimer adiabaticity from ĤΨ = 0. The attempt's sentence conflated that with the classical Hamilton–Jacobi flow on a branch. The precise statement: on a classical branch, the Einstein–Hamilton–Jacobi functional S[h_ij] plus constructive interference yields all ten Einstein equations with Tomonaga's many-time parametrization — Gerlach, Phys. Rev. 177, 1929 (1969) (verified: APS/ADS listing and abstract). So the HJ flow from Σ in *full* superspace is many-fingered: it reconstructs a 4-geometry, not a foliation, and Σ is an initial surface, which any Cauchy surface can be. The attack's "Gaussian-normal foliation anchored on Σ" appears only in minisuperspace, where superspace is one-dimensional and the HJ flow is a single parameter — an artifact of the FLRW ansatz (flaw 15), not of the reframing. The concrete test not done here: in HH85's perturbed minisuperspace the HJ function S[a, x_n] already depends on mode amplitudes, and many-fingeredness should be visible at linear order.

Conceded: the paper's Page–Wootters time is Level-3 and subsystem-conditioned; the attempt should have said "the branch's WKB proper time is the classical-limit time, and its relation to the paper's Level-3 time is the paper's own open problem." Also conceded, as presentational: ρ_Σ = T_μν n^μn^ν depends on n, but with K = 0 the unit normal to a tensorially defined surface is Σ-dependent only.

### 6. Junction (ii) numbers

**Verdict: factual, conceded; recomputed. The qualitative dichotomy survives; the specific numbers do not.**

Script 1, block A (a_2 ∈ {10³, 10⁴, 10⁵}):

| normalization | ε_J range | p(electron) | p(vev) |
|---|---|---|---|
| printed 180π/a_2 | 5.7×10⁻³ – 0.57 | 10 – 90 | 7.4 – 67 |
| 1/a_2 | 10⁻⁵ – 10⁻³ | 4.5 – 7.5 | 3.3 – 5.6 |
| 180/(16 a_2) | 1.1×10⁻⁴ – 1.1×10⁻² | 5.7 – 11.5 | 4.2 – 8.6 |

The attempt's "4–8" is the 1/a_2 normalization, not the printed one, and its own row (H_J = 10⁻¹–10⁻³ M_P, ε_J = 10⁻²–10⁻⁵) is internally inconsistent. Under the printed coefficient, a_2 = 10³ puts H_J at 0.75 M_P where semiclassics fails; the honest range is a_2 ≳ 10⁴. §6(c)'s "±1" is ±1 in log₁₀ε_J, which is a factor 2–10 in p. What survives: against (ii), p ≫ 1 under every normalization and no small rational appears; (i) and (ii) are different targets. That much was the attempt's point and it holds.

### 7. Instability; omitted R², C² couplings

**Verdict: solvable gap that strengthens the adaptation. The instability does not change the attempt's conclusion; it changes which scale is operative on the branch, and names the coupling.**

The enumeration must add the finite curvature counterterms. The repo's own FPE text lists them ("finite local curvature counterterms (involving R, R_{μανβ}R^{αβ}, □R)", FPE index.tex:226-242; "the R²-, C²-, and Euler-type counterterms in C_μν[g]", :354-355). In Starobinsky's structure the Euler coefficient (a_2, field counting) sets H_J; the □R/R² coefficient — a free finite counterterm — sets the scalaron mass and hence the post-instability quasi-de Sitter scale (Vilenkin 1985, PRD 32, 2511: existence verified, abstract not retrievable through the paywall; the two-parameter structure is stated here from the repo's counterterm list plus the standard form of the anomaly, not from the primary text). So the framework's gravitational sector carries **two** dimensionless numbers: a_2 (fixed by field content) and α_{R²} (a modulus). ε_J = f(a_2) is fixed; the second scale M/M_P = g(α_{R²}) is free. This is precisely the attempt's "the junction must fix a coupling, not a constant", with the coupling now named. The (ii′) row should be re-filed as internal, with M set by α_{R²}.

Conceded: "a particle of mass m on the branch at H_J" has no duration (repo lifetime 10⁻⁴²–10⁻⁴⁰ s), so the (ii) exponent column measures against a scale that exists only as the cap's radius. The honest split: **ε_J is the cap's number; α_{R²} is the branch's number.**

### 8. "Rigorous" on ε_J ~ 1/|a_2|

**Verdict: label conceded; (iii) is a one-line gap; (iv) framing.**

Existence Rigorous by citation, coefficient Sketch, a_2 rational — as the claim files say. (iii): the round-S⁴ anomaly fixed point with the same H_J follows from locality of the anomaly plus SO(5) invariance (⟨T_μν⟩ = ¼⟨T⟩g_μν on S⁴ as on dS, same equation R_μν = Λ_eff g_μν); a one-line derivation the repo has not written, not an open construction. (iv): the attempt argued against "only Λ", which the brief did not say; its observation that *in the framework* Λ is an output stands.

### 9. Factor 3

**Confirmed.** Script 1, blocks B and F: I(half S⁴) = −π/(2GH²), so |Ψ|² = e^{−2I} = e^{π/(GH²)} = e^{3π/(GΛ)}. §3(a)'s e^{3π/(GH(φ₀)²)} should read e^{π/(GH(φ₀)²)}. §3(a)'s conclusion (favours lowest H under the HH sign) is unchanged.

### 10. Saddle-ratio parameter c is discrete, never 0.16

**Verdict: the attack's conclusion is right; its argument is incomplete and contains one overreach. The route is closed by boundary data, not by discreteness.**

*Overreach.* c_needed = 22 ln10 · ε_J/π is ε_J-dependent. The discrete values c = ¼ (CP²) and ⅓ (S²×S²) reach the electron at ε_J = 0.0155 and 0.021, i.e. a_2 = 3.7×10⁴ and 2.7×10⁴ under the printed coefficient — inside the recorded range (script 1, block C). Discreteness alone does not close the route.

*What closes it (Rigorous, computed).* For boundary data Σ = round S³ of radius a the no-boundary saddles are the two S⁴ caps, and their actions are I_∓(a) = −(π/2GH²)[1 ∓ (1 − H²a²)^{3/2}] (script 1, block B, symbolic check against the GHY-corrected on-shell action). The ratio parameter c(a) = (1 − H²a²)^{3/2} is *continuous* — but it **vanishes at the K = 0 equator**, and for a > 1/H the two saddles are complex conjugates of equal modulus, so on the Lorentzian branch the same-boundary saddle ratio is a phase. The other Einstein topologies (CP², S²×S²; actions confirmed, block D) do not have round-S³ level sets (Berger spheres; S¹×S²), so their c-values belong to different boundary data, not to "a second saddle on the same branch". Quotients S⁴/Γ have boundary S³/Γ, a different Σ. (Sketch: I know no theorem excluding an Einstein metric on CP²∖B⁴ with a round S³ boundary; I only know the Fubini–Study metric does not have one.) Net: the exponential route is closed for pure Λ with round-S³ Σ, and the correct reason is that the only continuous saddle-ratio parameter vanishes exactly at the junction.

### 11. OS label; dependence on a gated claim

**Verdict: label overreach conceded; the reconstruction claim is a solvable gap with a route whose citation I could not verify.**

The OS theorem is flat-space and the paper says so; "Rigorous" covers only the S⁴ spectrum. The correct statement: the state on Σ is the Euclidean vacuum, whose reflection positivity across the S⁴ equator for free fields is what the de Sitter constructive literature uses (Figari–Høegh-Krohn–Nappi 1975 for S²/dS₂ — **from memory, not verified here**; the S^d free-field case is folklore I could not pin to a source). Jaffe–Ritter 2007 (verified) covers manifolds with a static Euclidean-time Killing vector and time reflection; S⁴ is not globally static, so it does not directly apply. So the route is named and the citation is missing. Two consequences the attack did not draw: for free fields that state is the Bunch–Davies vacuum, *already constructed* — so adaptation (2)'s "construct the OS state on Σ explicitly" is done, and it yields flaw 1's tautology; and the gated claim `ce-euclidean-vacuum-at-fixed-point` gates the *branch* (instability lifetime), not the *cap*, which is Euclidean and has no lifetime. Non-citation of the claim file: conceded.

### 12. Positive content is dimensional analysis; adaptation (1) imports a UV fixed point

**Verdict: (a) framing — the collapse is right, but a narrower non-vacuous claim exists; (b) conceded; (c) conceded as imported, with the concrete route named and its prior assessment recorded.**

(a) The narrowed claim I would keep is not dimensional analysis. It is four specific results:

- **N1** (Rigorous by citation, HH85 + HHH08). The no-boundary state contributes no continuous parameter beyond the action's couplings.
- **N2** (Rigorous, computed). The same-boundary saddle-ratio parameter vanishes at the K = 0 junction and is a phase on the Lorentzian side: no exponential hierarchy from saddle multiplicity for round-S³ Σ.
- **N3** (Rigorous given the fixed background and a smooth metric). In the smooth degenerate class, curvature regularity at Σ forces K_Σ = 0 (flaw 13).
- **N4** (Rigorous). n is a diffeomorphism invariant, an odd integer in the smooth class, and inert for every Level-2/3 quantity in proper variables (flaw 3).

Together: *the junction of a no-boundary geometry with free matter carries exactly one continuous dimensionless number, ε_J, plus discrete data (field content, n, topology of Σ); any hierarchy requires a coupling of the action — ξ_A, g_i, α_{R²}, or c_Λ — to be selected by something, and the record contains no selection principle.* Each of N1–N4 is falsifiable on its own and none is "with inputs {G, Λ} only functions of those exist."

(b) Condition (a) is the fixed-point equation and constrains nothing; condition (b) fails in the trivial direction (ρ_anom ∝ H⁴). Conceded.

(c) Adaptation (1) imports a UV fixed point. Conceded. The concrete route inside the framework is to extend Level 2 from the metric to (metric, couplings) with a fixed-point condition β_i(g*) = 0 — asymptotic safety by another name. The repo's only antecedent, position-2's extended map, was assessed in March as "only determines the self-consistent value of an already-nonzero mass — it doesn't generate mass from nothing" (position-2 §3, Rigorous paragraph, confirmed in the file). So adaptation (1) is Conjecture, requires a non-perturbative fixed point for matter couplings, and would be a new structural assumption beyond the three axioms — which METHODOLOGY says the experimenter decides, not a routine.

### 13. K_Σ ≠ 0 excluded by Hayward / Kossowski–Kriele; bearing on the SCB condition

**Verdict: the attack is right; it closes adaptation (3) in the smooth class outright. It does bear on the SCB expanding note — and the tension dissolves on computation, in Hayward's favour.**

Hayward: "a well defined Ricci tensor requires the standard junction condition, namely vanishing of the second fundamental form of the junction surface" (gr-qc/9303034 abstract, verified). Kossowski–Kriele 1993b: the Riemann tensor continues smoothly iff K = 0 and the limit of the evolution equations holds (search-level summary; Hayward's own summary at full-text line 515 agrees). For the discontinuous class, Hayward's full text (lines 337-341): Ellis et al. "obtain only the regular parts (23) whilst omitting the singular parts (24)".

*The SCB tension, computed (script 2).* Take the SCB profile λ = −c(x⁰)ⁿ with n odd and a smooth in x⁰ (the metric's own smoothness chart). ℋ = a′/(a√|λ|) and R = 6(ℋ̇ + 2ℋ²). Curvature bounded at Σ requires the first non-constant term of a to be of order ≥ n + 2: for n = 1, a = a₀ + bx³ gives ℋ → 0 but R → 27b/(a₀c) ≠ 0 finite, a = a₀ + bx⁴ gives R → 0; anything lower diverges. So **in the smooth class, curvature regularity ⇔ a − a₀ = O((x⁰)^{n+2}) = O(u²) ⇒ ℋ_Σ = 0, i.e. K_Σ = 0.** The expanding note's "bounded proper expansion rate" condition, restricted to smooth metrics, is *equivalent* to Hayward's K = 0; it is weaker only for a not smooth in the SCB chart (a′ ~ |x⁰|^{n/2}, a non-integer power for odd n). The note's own remark that de Sitter (ℋ ≡ H₀ ≠ 0) "sits in the regular class" is therefore a statement about a non-smooth profile: flat-slice dS glued at any surface has K = 3H₀ ≠ 0 and is outside the smooth class; the smooth junction for dS is the closed-slicing waist a = cosh(Hu)/H at u = 0 — which is the Hartle–Hawking equator. Recommendation for SCB: state that, for smooth a, the boxed condition implies ℋ_Σ = 0. The DMT-vs-Hayward dispute in the notes concerns the *field* momentum π_Σ; the *metric* condition K = 0 is not disputed within the smooth class.

So K_Σ is not a modulus of any consistent junction in the record: forced to zero by reality in HH, by Hayward/KK and by the computation above in the smooth SCB class, and available only in the discontinuous class that omits singular terms of the field equations. Adaptation (3) closed. The row-4 splice of closed and flat slices: conceded, minor.

### 14. "K = 0 forced, Rigorous (FLRW)" only for pure Λ or φ at an extremum

**Verdict: conceded on scope; narrower-but-viable — the real junction exists in exactly the framework's own case.**

HHH08 (attack-verified): no real extrema for φ₀ ≠ 0 except false-vacuum potentials. The label should read "Rigorous (FLRW; pure Λ_eff, or φ₀ at an extremum of V)". The framework's mechanism puts m_eff = √((ξ − ⅙)R) on fields at φ₀ = 0 with V(0) = 0 — an extremum — so case (ii) with conformal matter plus non-conformal scalars at φ₀ = 0 *is* inside the real-junction class. The worry applies only to fields with V(φ₀) ≠ 0.

### 15. The enumeration is ADM data on a slice

**Verdict: disclosure gap conceded; framing fix available.**

The count is of the moduli of the (cap, branch) pair — a 4-geometry with a K = 0 surface — evaluated on Σ for convenience; data on different surfaces are related by the field equations, so the count is slice-independent even though its presentation is not. The genuine Axiom-2 exposure is the FLRW minisuperspace in which the "forced" rows were derived; that is inherited from the reframing, and the attempt already flagged that the covariant form of the reality condition is open. The axiom check should have said so.

### 16. §3(a), §3(d) depend on the HH sign

**Conceded, presentational.** Both assume the HH sign; under FLT17's inverted weighting the favouring inverts; DTL19's Robin conditions restore it. §2's "except §3(d)" should read "except §3(a) and §3(d)".

### 17. "Single Rigorous conclusion" contradicts row 2

**Conceded.** Corrected statement: every SO(5)-invariant junction quantity is M_P ε^{k/2} × (rational function of field content); the harmonic tower is a continuum of non-invariant, l-labelled scales, none selected. "Integer-valued" → "rational".

### 18. Smaller items

All conceded. (m_π/59.8 MeV)³ = 12.7, a factor 2.3 in the mass, should be said plainly. γ ≈ 0.03 uses the EW-scale bracket as constant; the conclusion p ≈ ½ is insensitive. Topology of Σ is discrete junction data omitted from the table; Σ = S³/Γ needs quotient or orbifold caps and rescales S_dS by 1/|Γ| — a discrete rescaling, not a new continuous scale.

---

## Surviving form of the attempt

The committed position — "the exponent-fixing relation lives in the state on Σ, not in its geometry" — does **not** survive: the no-boundary state is a function of the geometry and the action (N1), so "state" and "geometry plus couplings" are the same reservoir. What survives is the negative it was pointing at, made precise:

> **(Sketch as a whole; components labelled.)** Let the junction be a no-boundary Euclidean cap with free matter, glued to a Lorentzian branch either by analytic continuation (HH) or as a smooth degenerate surface (SCB, n odd). Then:
> 1. *(Rigorous by citation)* the state on Σ contributes no continuous parameter beyond the action's couplings [HH85, HHH08];
> 2. *(Rigorous, computed)* the same-boundary saddle-ratio parameter c(a) = (1 − H²a²)^{3/2} vanishes at the K = 0 junction and is a phase on the Lorentzian side, so saddle multiplicity yields no exponential hierarchy for round-S³ Σ;
> 3. *(Rigorous given fixed background + smoothness)* K_Σ = 0 is forced in both gluings — by reality in HH, by Hayward/Kossowski–Kriele and by curvature regularity in the smooth SCB class — so K_Σ is not a modulus;
> 4. *(Rigorous)* the smooth-structure invariant n is an odd integer and inert for all Level-2/3 quantities in proper variables;
> 5. *(Rigorous, from the repo's own counterterm list; Sketch for the scale identification)* the framework's gravitational sector carries two dimensionless numbers — a_2 (field counting, fixes ε_J and the cap) and α_{R²} (free counterterm, fixes the scalaron mass and the post-instability branch scale).
>
> Hence the junction carries exactly one continuous dimensionless number, ε_J = f(a_2), and every other scale on the branch is M_P × (function of a coupling: ξ_A, g_i, α_{R²}, c_Λ). **A mass hierarchy requires a selection principle for a coupling; the record contains none.** The adaptation the negative points to is unchanged in words — *the junction must fix a coupling, not a constant* — and now has a named first instance: α_{R²}. Whether anything at Σ can fix α_{R²} is the open question; it is not answered by the attempt, by the attack, or here.

Two things the attempt got right that the attack confirms and I would keep verbatim: the homogeneity lemma, and the (i)/(ii) dichotomy (small rational exponents vs. p ≫ 1) as the calibration of what a mechanism would have to do — with the (ii) numbers replaced by the table in flaw 6.

## What the rescue could not do

1. **Cite S⁴ equatorial reflection positivity for the free field.** The route (constructive de Sitter literature, Figari–Høegh-Krohn–Nappi for d = 2) is from memory; no S⁴ source was verified. Until it is, "the Euclidean vacuum on Σ is reflection-positive" is exploratory-tier.
2. **Verify the two-parameter (a_2, α_{R²}) structure at the primary source.** Vilenkin 1985 is verified to exist; its abstract was behind a 403; Starobinsky 1980 is recorded in the repo as unreachable. The statement rests on the repo's FPE counterterm list and the standard anomaly form.
3. **Exclude Einstein metrics with round-S³ boundary on other topologies.** I only know the Fubini–Study and product metrics do not have such level sets; no theorem cited. Flaw 10's closure is Rigorous for the S⁴ caps and Sketch for the topology sum.
4. **Run the many-fingered-time check** for Σ + HJ flow in HH85's perturbed minisuperspace (flaw 5). The test is specified, not executed.
5. **State the covariant reality condition** for the HH gluing beyond FLRW (attempt §6(c), unchanged).
6. **Find a selection principle for α_{R²}** or any coupling at Σ. This is the adaptation's actual content and it is Conjecture territory; nothing here advances it.

## Citations used

**Verified (existence and, where stated, content):**
- Hartle & Hawking, PRD 28, 2960 (1983) — attack-verified; used for the no-boundary definition only.
- Halliwell & Hawking, "Origin of structure in the Universe," PRD 31, 1777 (1985) — verified (APS DOI 10.1103/PhysRevD.31.1777; PubMed summary): inhomogeneous modes start in their ground state as a consequence of the no-boundary state. Load-bearing for N1.
- Hartle, Hawking, Hertog, PRD 77, 123537 (2008) — attack-verified; used for φ₀ selection at the lower bound and for flaw 14.
- Gerlach, "Derivation of the ten Einstein field equations from the semiclassical approximation to quantum geometrodynamics," Phys. Rev. 177, 1929 (1969) — verified (APS/ADS; abstract: EHJ equation + constructive interference ⇒ ten Einstein equations, Tomonaga many-time parametrization). Load-bearing for flaw 5.
- Hayward, "Junction conditions for signature change," gr-qc/9303034 — verified, **full text read**: abstract sentence on vanishing second fundamental form; §IV lines 401-411 on N = t vs N = ε (Hayward *rejects* the "different differential structures" claim, attributing it to Ellis et al.); lines 337-341 on Ellis et al. omitting the singular parts. Polarity-checked.
- Hayward, CQG 9, 1851 (1992) — attack-verified; paper-grade in the SCB seed note.
- Kossowski & Kriele, "Signature type change and absolute time in general relativity," CQG 10, 1157 (1993) — verified existence and transverse-class content at search-summary level (det g vanishes to first order; hypersurface totally geodesic).
- Kossowski & Kriele, CQG 10, 2363 (1993) and Proc. R. Soc. A 444, 297 (1994) — verified existence; content (Riemann continues smoothly iff K = 0 plus the evolution-equation limit) at search-summary level and via Hayward's summary.
- Jaffe & Ritter, "Quantum field theory on curved backgrounds. I," Commun. Math. Phys. 270, 545 (2007), hep-th/0609003 — verified (abstract): OS quantization with a static Euclidean-time Killing vector and time reflection. Used only to say it does *not* directly cover S⁴.
- Vilenkin, "Classical and quantum cosmology of the Starobinsky inflationary model," PRD 32, 2511 (1985) — verified existence (APS DOI, PubMed); abstract not retrieved (403). Not load-bearing.
- Feldbrugge–Lehners–Turok PRL 119, 171301 (2017); Di Tucci–Lehners PRL 122, 201302 (2019); Gibbons–Hawking PRD 15, 2738 (1977); Coleman–Weinberg PRD 7, 1888 (1973); Rugh–Zinkernagel hep-th/0012253; Wald–Iyer PRD 44, R3719 (1991); Aguirre–Fernández–Lafuente math/0609838; Dray–Hellaby GRG 28, 1401 (1996) — attack-verified; relied on as the attack's evidence, not re-verified here.
- Repo-internal, read in full or at the cited lines: `programs/co-emergence/index.tex` (axioms 159-252, intro 110-130, mass section 1219-1348, Level 1 1443-1493, S⁴ remark 1548-1560, OS 1815-1835, Page–Wootters 928-948 and 1784-1802); `programs/fixed-point-existence/index.tex` (114-135, 226-242, 345-365); the three FPE claim files; `ce-euclidean-vacuum-at-fixed-point.md`; both SCB notes; the March synthesis 181-314; position-2 §3.

**Unverified (from memory; not relied on for any verdict):**
- Figari, Høegh-Krohn, Nappi (1975), P(φ)₂ on two-dimensional de Sitter via the Euclidean sphere — cited only as the route for flaw 11's gap.
- Starobinsky, Phys. Lett. B 91, 99 (1980) — in the repo bib; the □R-coefficient scheme-dependence is stated from general knowledge, not from the text.
- Bunch & Davies (1978) — in the repo bib; the massive ⟨T_μν⟩ closed form with μ-dependence is standard but not re-read.

---

## Scripts and output

### Script 1 — exponent table, cap action, saddle ratios, anomaly coefficient, factor 3

```python
import numpy as np, sympy as sp
MP=1.220890e19*1e9  # eV
masses={"electron":0.511e6,"pion":139.57e6,"vev":246e9,"rho_L^1/4":2.2e-3}
for a2 in [1e3,1e4,1e5]:
    for label,eps in [("180pi/a2",180*np.pi/a2),("1/a2",1/a2),("180/(16 a2)",180/(16*a2))]:
        row=" ".join(f"{k}:{np.log10(m/MP)/np.log10(eps):5.1f}" for k,m in masses.items())
        print(f"a2={a2:.0e} {label:12s} eps={eps:.2e} H/MP={np.sqrt(eps):.3f} | p: {row}")
th,r,G=sp.symbols('theta0 r G',positive=True); t=sp.symbols('t')
Lam=3/r**2
vol=2*sp.pi**2*r**4*sp.integrate(sp.sin(t)**3,(t,0,th))
bulk=-(Lam/(8*sp.pi*G))*vol
K=3*sp.cos(th)/(r*sp.sin(th))
gh=-(1/(8*sp.pi*G))*2*sp.pi**2*(r*sp.sin(th))**3*K
I=sp.simplify(bulk+gh)
print("I(theta0) =",I, "| check:", sp.simplify(I+(sp.pi*r**2/(2*G))*(1-sp.cos(th)**3)))
print("I(pi/2) =",sp.simplify(I.subs(th,sp.pi/2)),"  I(pi) =",sp.simplify(I.subs(th,sp.pi)))
for eps in [1e-2,5.7e-3,1.6e-2,2.1e-2]:
    S=np.pi/eps; print(f"eps_J={eps:.3g}: S_dS={S:.0f}  c_needed(1e-22)={22*np.log(10)/S:.3f}")
for c in [1/4,1/3,1/2]:
    eps=c*np.pi/(22*np.log(10)); print(f"c={c:.3f}: eps_J needed={eps:.4f}, a2 (printed coeff)={180*np.pi/eps:.2e}")
L=sp.symbols('Lambda',positive=True)
vols={"S4":24*sp.pi**2/L**2,"S2xS2":16*sp.pi**2/L**2,"CP2":18*sp.pi**2/L**2}
for k,v in vols.items():
    I=-(L/(8*sp.pi))*v
    print(k,"I*G =",sp.simplify(I),"  c =",sp.simplify(1-I/(-(L/(8*sp.pi))*vols['S4'])))
a2,H,Gs=sp.symbols('a2 H G',positive=True)
T=-a2*H**4/(120*sp.pi**2); rho=-T/4
print("rho_anom =",rho," ; H^2 =",[sp.simplify(s**2) for s in sp.solve(sp.Eq(3*H**2,8*sp.pi*Gs*rho),H) if s.is_positive])
```

Output (trimmed):
```
a2=1e+03 180pi/a2     eps=5.65e-01 H/MP=0.752 | p: electron: 90.4 pion: 80.5 vev: 67.4 rho_L^1/4:124.2
a2=1e+03 1/a2         eps=1.00e-03 H/MP=0.032 | p: electron:  7.5 pion:  6.6 vev:  5.6 rho_L^1/4: 10.2
a2=1e+03 180/(16 a2)  eps=1.12e-02 H/MP=0.106 | p: electron: 11.5 pion: 10.2 vev:  8.6 rho_L^1/4: 15.8
a2=1e+04 180pi/a2     eps=5.65e-02 H/MP=0.238 | p: electron: 17.9 pion: 16.0 vev: 13.4 rho_L^1/4: 24.6
a2=1e+04 1/a2         eps=1.00e-04 H/MP=0.010 | p: electron:  5.6 pion:  5.0 vev:  4.2 rho_L^1/4:  7.7
a2=1e+04 180/(16 a2)  eps=1.12e-03 H/MP=0.034 | p: electron:  7.6 pion:  6.8 vev:  5.7 rho_L^1/4: 10.4
a2=1e+05 180pi/a2     eps=5.65e-03 H/MP=0.075 | p: electron: 10.0 pion:  8.9 vev:  7.4 rho_L^1/4: 13.7
a2=1e+05 1/a2         eps=1.00e-05 H/MP=0.003 | p: electron:  4.5 pion:  4.0 vev:  3.3 rho_L^1/4:  6.1
a2=1e+05 180/(16 a2)  eps=1.12e-04 H/MP=0.011 | p: electron:  5.7 pion:  5.1 vev:  4.2 rho_L^1/4:  7.8
I(theta0) = pi*r**2*(3*cos(theta0) + cos(3*theta0) - 4)/(8*G) | check: 0
I(pi/2) = -pi*r**2/(2*G)   I(pi) = -pi*r**2/G
eps_J=0.01: S_dS=314  c_needed(1e-22)=0.161
eps_J=0.0057: S_dS=551  c_needed(1e-22)=0.092
eps_J=0.016: S_dS=196  c_needed(1e-22)=0.258
eps_J=0.021: S_dS=150  c_needed(1e-22)=0.339
c=0.250: eps_J needed=0.0155, a2 (printed coeff)=3.65e+04
c=0.333: eps_J needed=0.0207, a2 (printed coeff)=2.74e+04
c=0.500: eps_J needed=0.0310, a2 (printed coeff)=1.82e+04
S4 I*G = -3*pi/Lambda   c = 0
S2xS2 I*G = -2*pi/Lambda   c = 1/3
CP2 I*G = -9*pi/(4*Lambda)   c = 1/4
rho_anom = H**4*a2/(480*pi**2)  ; H^2 = [180*pi/(G*a2)]
```
(I(θ₀) = −(πr²/2G)(1 − cos³θ₀); with cos θ₀ = ∓√(1 − H²a²) this is I_∓(a) as quoted in flaw 10.)

### Script 2 — smooth SCB class: curvature regularity at Σ forces K_Σ = 0

```python
import sympy as sp
x=sp.symbols('x',positive=True); a0,b,c=sp.symbols('a0 b c',positive=True)
for n in [1,3]:
    for kp1 in range(1,n+4):
        a=a0+b*x**kp1; sq=sp.sqrt(c)*x**sp.Rational(n,2)
        Hc=sp.diff(a,x)/(a*sq); R=6*(sp.diff(Hc,x)/sq+2*Hc**2)
        print(f"n={n} a=a0+b x^{kp1}: Hcal(0)={sp.limit(Hc,x,0)}, R(0)={sp.limit(R,x,0)}, "
              f"R~{sp.simplify(R.series(x,0,2).removeO().as_leading_term(x))}")
```

Output:
```
n=1 a=a0+b x^1: Hcal(0)=oo, R(0)=-oo, R~-3*b/(a0*c*x**2)
n=1 a=a0+b x^2: Hcal(0)=0, R(0)=oo, R~6*b/(a0*c*x)
n=1 a=a0+b x^3: Hcal(0)=0, R(0)=27*b/(a0*c), R~27*b/(a0*c)
n=1 a=a0+b x^4: Hcal(0)=0, R(0)=0, R~60*b*x/(a0*c)
n=3 a=a0+b x^1: Hcal(0)=oo, R(0)=-oo, R~-9*b/(a0*c*x**4)
n=3 a=a0+b x^2: Hcal(0)=oo, R(0)=-oo, R~-6*b/(a0*c*x**3)
n=3 a=a0+b x^3: Hcal(0)=0, R(0)=oo, R~9*b/(a0*c*x**2)
n=3 a=a0+b x^4: Hcal(0)=0, R(0)=oo, R~36*b/(a0*c*x)
n=3 a=a0+b x^5: Hcal(0)=0, R(0)=75*b/(a0*c), R~75*b/(a0*c)
n=3 a=a0+b x^6: Hcal(0)=0, R(0)=0, R~126*b*x/(a0*c)
```
Bounded R at Σ needs the first non-constant term of a at order ≥ n + 2, i.e. a − a₀ = O(x^{n+2}) = O(u²); then ℋ_Σ = 0. A bounded nonzero ℋ_Σ would need a′ ~ x^{n/2}, impossible for a smooth in x when n is odd.
