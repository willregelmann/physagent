# Attack pass on Attempt A — "First-principles scale counting at the no-boundary junction"

**Target:** `/home/will/Projects/physagent/attempt-A-scale-counting.md`
**Date:** 2026-09-05
**Role:** Attack pass (Pass 1 of METHODOLOGY "No Idea Is Eliminated Without a Defense"). Flaws only; no survive/eliminate verdict. Every flaw is located, evidenced, and severity-tagged so the steelman can answer it.

Conventions: line numbers `attempt:NN` refer to the target file; repo paths are relative to the repo root. Web-verified sources are listed in the final section; anything I lean on that I could not verify is marked.

---

## Flaws

### 1. The "free" junction relation ρ_Σ = (3/8π) M_P² H² is either false or a tautology, depending on where Λ sits

**Location:** attempt:184-190 (§3, "The junction supplies one such relation for free"), attempt:232 (§4 row ρ_Σ^{1/4}), attempt:288-292 (§6a kill computation).

**Flaw:** The attempt's own row-4 constraint (attempt:104) is 3ℋ_Σ² + 3/a_Σ² = 8πGρ_Σ + Λ, and its own §1 (attempt:23) has Λ as an explicit input in I_E. Evaluating that constraint with the attempt's own stated junction values ℋ_Σ = 0, a_Σ = 1/H, H² = Λ/3 gives ρ_Σ = 0, not (3/8π)M_P²H². The relation at attempt:187 is obtained by dropping Λ from the constraint and letting ρ_Σ play its role, i.e. by identifying ρ_Σ ≡ Λ/(8πG). Under that identification the relation is the definition of ρ_vac, not a junction output.

**Evidence (computation):**
```
closed-slice Friedmann constraint on Σ:  ȧ²/a² + 1/a² = (8πG/3)ρ + Λ/3
at the HH equator: ȧ = 0, a = a_0 = sqrt(3/Λ)  ⇒  1/a_0² = Λ/3
⇒  Λ/3 = (8πG/3)ρ_Σ + Λ/3  ⇒  ρ_Σ = 0.
(numerically: 8πG ρ_Σ = 3H² − Λ = 3H² − 3H² = 0; see script output line "rho_Sigma with Lambda input".)
```
In the anomaly-driven case (junction (ii)) there is no bare Λ, and ρ_Σ = ⟨T_nn⟩ = ρ_anom ∝ a_2 H⁴; the constraint 3/a_0² = 8πG ρ_anom(H) *is* the fixed-point equation that defines H_J (`programs/fixed-point-existence/index.tex:129-135`). So ρ_Σ = (3/8π)M_P²H_J² holds there, but as the definition of H_J. The attempt's §6(a) says this collapse "might" be the outcome of an SCE computation; no computation is needed — it is already the case at the level of the constraint. "Against junction (i) it is literally ρ_Λ^{1/4} = 2.2 meV" (attempt:189-190) is the statement that (Λ/8πG)^{1/4} = 2.2 meV, i.e. the cosmological-constant-problem number, not a junction-generated scale.

**Severity:** structural (this is the only "for free" relation the position offers).

### 2. The matter-side relation ρ_Σ = ρ(m) requires fixing the cosmological-constant counterterm — a second dimensionful constant, which §6(b) says is not needed

**Location:** attempt:190-195 (ρ = m⁴, ρ = Gm⁶), attempt:319-328 (adaptation 2), attempt:334-335 ("not a second dimensionful constant").

**Flaw:** For a field of mass m in the semiclassical Einstein equation, ⟨T_μν⟩ contains a divergent m⁴ log(m/μ) g_μν piece that is absorbed into the renormalized Λ; the renormalized Λ (together with the R² and C² coefficients) is a free parameter of the SCE, not an output. The FPE paper's own regularization discussion lists exactly these counterterms (`programs/fixed-point-existence/index.tex:355`: "the variation of the R²-, C²-, and Euler-type counterterms"). Writing "ρ = m⁴ (vacuum energy of a field of mass m saturates the constraint)" therefore presupposes that Λ_bare has been chosen so that the finite remainder is m⁴ — a choice of a dimensionful constant. The same holds for Zel'dovich's ρ ~ Gm⁶: Rugh–Zinkernagel (verified, fn. 13 and eq. 16) present it as a heuristic that already assumes the m⁴ term is discarded, and they record that Zel'dovich himself found it ~7 orders too large. So adaptation (2) is not "a relation living in the state on Σ"; it is "fix the Λ counterterm by hand", which contradicts the attempt's closing thesis (attempt:334-335).

**Severity:** structural.

### 3. "n and c are coordinate artifacts (Rigorous)" is false for n; n is a smooth-structure invariant

**Location:** attempt:109 (row 9), attempt:111-120 (the boxed argument), attempt:253-255 (§5: "§2 shows the chart data (n,c) drop out").

**Flaw:** Under a smooth reparametrization x⁰ ↦ f(x⁰) with f'(0) ≠ 0, λ̃ = λ/(f')², so the order of vanishing of λ (equivalently of det g, a density of weight 2) at Σ is invariant. The proper variable u ∝ (x⁰)^{(n+2)/2} is not a diffeomorphism at Σ — the SCB note itself says so ("degenerates only at Σ", `programs/signature-change-boundary/notes/2026-06-17-expanding-region-note.md` §1) — and the glued ũ = sgn(x⁰)|u| chart is only C^{⌊(n+2)/2⌋}, which the attempt concedes at attempt:117-119. Passing to ũ is therefore a change of differential structure, not a coordinate change. That is exactly the distinction the repo's paper-grade-verified junction literature draws:

- Hayward (gr-qc/9303034, verified): "any differentiable function N of t with differentiable inverse would represent the same differential structure as N = t. ... N = t is such a function and N = ε is not" — where N = ε (sign function) is precisely the attempt's proper-time chart on both sides.
- The standard definition of *transverse* type change is d_p(det g) ≠ 0 on Σ, "this condition does not depend on the choice of the coordinates" (Aguirre–Fernández–Lafuente, arXiv:math/0609838, verified, citing Kossowski–Kriele). n = 1 is transverse; n > 1 is not. Kossowski–Kriele's 1994 geodesic-extendability results are stated for the transverse case only (title verified), so which n one has decides whether their theorems apply — the SCB seed note explicitly flags this ("whether their extension results cover this profile, step for step, has not been checked", `2026-06-05-fixed-background-note.md` §4).
- The SCB seed note's July audit: "the degeneracy at Σ is *invariant*, not a chart artifact" (§3, Consequence).
- Internal to the SCB notes: the indicial roots {0, 1+n/2} and the connection residue Γ⁰₀₀ = n/(2x⁰) depend on n and are the same from both sides (seed note §3, §5; expanding note §4).

What is true: c is gauge (x⁰ → αx⁰ sends c → c α^{n+2}); n is dimensionless. So the row's *scale* conclusion ("none") may survive, but the Rigorous label is wrong, and the §5 argument that "the SCB profile is a chart description of an invariant surface" rests on it. The attempt's own fallback — that (n,c) are "Level 1 in the hierarchy" data — concedes the point: in the co-emergence paper Level 1 is the smooth-structure level with its own measure μ* (`programs/co-emergence/index.tex:1443-1493`), a physical level, not gauge.

**Severity:** factual (label) feeding an axiom-level argument (flaw 4).

### 4. "Σ = {det g = 0} (equivalently the totally geodesic equator, K = 0, in HH)" conflates two constructions, and neither selects a single surface by a scalar condition

**Location:** attempt:247-257 (§5, preferred-foliation bullet).

**Flaw, four parts:**
(a) *Not equivalent.* In the Hartle–Hawking gluing the metric is non-degenerate at the equator; the Lorentzian region is reached by analytic continuation, not through a degenerate surface. In the SCB construction K is not required to vanish (attempt's own row 4). Two different surfaces defined by two different conditions in two different constructions; the attempt's §5 bullet 2 admits they are "different objects glued differently" and then §5 bullet 1 treats them as one condition.
(b) *K = 0 does not select a single surface in the round S⁴.* Every great S³ is totally geodesic. What picks out "the" equator is the argument of Ψ[h_ij] — the 3-geometry on which the wavefunction is evaluated — i.e. the choice of slice. That is precisely the "inner product on a spatial slice, smuggling in the foliation through the back door" objection the co-emergence paper raises against Wheeler–DeWitt in its own prop:nohilbert (`programs/co-emergence/index.tex:184-208`).
(c) *In SCB, Σ is prescribed, not selected.* Seed note §1 ("λ is prescribed. We do not derive λ"), §9.1; expanding note §7.2 ("The §2 condition is a fixed-background curvature statement, not a selection principle"). The attempt's "a single surface selected by a scalar condition — including a self-consistency condition" describes a construction that does not exist in the repo.
(d) *The analogy backfires.* det g is a scalar density of weight 2, not a scalar (its zero set is invariant, so the conclusion is repairable, but the sentence is wrong as written). Worse, apparent horizons — offered as the model of an invariantly selected surface — are slicing-dependent: Wald–Iyer 1991 (verified) exhibit Cauchy slicings of Schwarzschild containing no outer trapped surfaces at all.

**Severity:** axiom (Axiom 2, preferred foliation) — this is the bullet that clears the attempt on Axiom 2, and it does not hold as argued.

### 5. The axiom check on WKB/branch time contradicts the paper's own text, and misses the Σ + Hamilton–Jacobi-flow foliation

**Location:** attempt:265-269 (§5 "Time evolution (Axiom 1)"), attempt:270-272 ("Preferred observer").

**Flaw:** The attempt says WKB time on a branch is "the Hamilton–Jacobi flow, derived, consistent with the paper's Page–Wootters stance." The co-emergence paper says the opposite at `programs/co-emergence/index.tex:115-127`: "every known formulation of ĤΨ = 0 introduces hidden temporal or foliation structure at some stage of its derivation ... the WKB semiclassical limit inserts time via Born–Oppenheimer adiabaticity." The paper's Page–Wootters stance is a Level-3, subsystem-conditioned, measure-theoretic time (def:measure_pw, index.tex ≈932-945; §"Page–Wootters at Level 3", ≈1786-1800), not a global HJ time on a minisuperspace branch. Structurally: a selected Σ plus the HJ flow emanating from it is a Gaussian-normal foliation of each Lorentzian branch by level sets of the HJ function — a preferred foliation anchored on a preferred surface. The brief's question ("does the single-surface argument survive when the reframing also puts WKB time on every branch emanating from that surface?") is not addressed; the attempt asserts the two are separately fine and never checks their combination.

Also on the preferred-observer bullet: ρ_Σ = T_μν n^μ n^ν, used throughout §3, is the energy density measured by the observer with 4-velocity n normal to Σ — an observer-dependent quantity. The attempt claims observer-dependent quantities were "deliberately not used."

**Severity:** axiom (Axioms 1 and 2).

### 6. The junction (ii) numbers match no normalization the repo records, and the (ii) exponent column is wrong by far more than the stated ±1

**Location:** attempt:62 (table row (ii)), attempt:67-75 (column "p vs (ii), ε_J = 10⁻⁴"), attempt:84-86 ("integer-ish exponents 4–8"), attempt:339-342 (§6c: "moves by ±1").

**Flaw:** With the printed coefficient H_0² = 180π M_P²/|a_2| (`fpe-starobinsky-coefficient.md`) and the recorded range a_2 ∈ [10³, 10⁵] (`fpe-fixed-point-is-inflationary.md`), ε_J = 565/a_2 ∈ [5.7×10⁻³, 0.57] and H_J ∈ [0.075, 0.75] M_P. The attempt's row gives H_J = 10⁻¹–10⁻³ M_P and ε_J = 10⁻²–10⁻⁵, which (i) are mutually inconsistent (that H_J range implies ε_J ∈ [10⁻², 10⁻⁶]) and (ii) match neither 180π/a_2, nor 1/a_2 ([10⁻³, 10⁻⁵]), nor 180π/(16π a_2) ([1.1×10⁻², 1.1×10⁻⁴]). The reference column uses ε_J = 10⁻⁴, which under the printed coefficient needs a_2 ≈ 5.7×10⁶, outside the recorded range. Recomputed exponents:

| mass | p at ε_J=10⁻⁴ (attempt) | p at ε_J=5.7×10⁻³ (a_2=10⁵, printed coeff.) | p at ε_J=0.57 (a_2=10³, printed coeff.) |
|---|---|---|---|
| electron | 5.6 | 10.0 | 92 |
| pion | 5.0 | 8.9 | 82 |
| EW vev | 4.2 | 7.4 | 68 |

"Integer-ish exponents 4–8" becomes "10 to 90", and at a_2 = 10³ the junction sits at H_J ≈ 0.75 M_P, where the semiclassical S⁴/dS geometry is not trustworthy at all. The §6(c) statement that the (ii) column "moves by ±1" understates this by an order of magnitude in p.

**Severity:** factual.

### 7. Junction (ii) is the exact anomaly fixed point, which the repo records as never physically operative; the attempt never mentions the instability, and its "exhaustive" enumeration omits the couplings that govern what replaces it

**Location:** attempt:44-51 (§1 third paragraph), attempt:62, attempt:107 (row "anomaly coefficients"), attempt:122-130 ("single Rigorous conclusion"), attempt:63 ("(ii') ... external, for reference").

**Flaw:** The repo records the exact constant-H solution as unstable with a quasi-de Sitter lifetime of 10⁻⁴² to 10⁻⁴⁰ s (`fpe-fixed-point-is-inflationary.md`, closing paragraph) and gates a claim about the state at that fixed point as "INDEPENDENTLY FATAL as a physical claim" for exactly this reason (`programs/co-emergence/claims/ce-euclidean-vacuum-at-fixed-point.md`, `gate:` block). The attempt treats junction (ii) as "the framework's own version of the junction" and measures every mass against its ε_J, without once naming the instability. Consequences: (a) the Lorentzian branch at H_J lasts ~10⁻⁴² s, so "a particle of mass m on that branch" has no operational content; (b) after the instability the curvature scale is set by the R² (and C²) counterterm coefficients — dimensionless moduli of the gravitational effective action that are *not* field counting (`programs/fixed-point-existence/index.tex:355`). These are absent from the §2 enumeration, which lists only (a, c, ξ_A, g_i). The R² coefficient is exactly what fixes the (ii') Starobinsky scale ≈10¹³ GeV that the attempt files as "external": it is internal to the framework's own effective action. So the "single Rigorous conclusion" ("the junction carries exactly one length") omits a datum, and the closing adaptation "the junction must fix a coupling, not a constant" already has a concrete instance in the framework — the R² coupling — that the attempt did not analyze.

**Severity:** structural (dependence on something the repo has ruled out as operative) + factual (incomplete enumeration).

### 8. The "(Rigorous)" label on "ε_J ~ 1/|a_2| is computed from a field-counting integer" is not supported

**Location:** attempt:44-51.

**Flaw:** (i) The coefficient is Sketch, dimensionally inconsistent as printed, and the claim file records "two independent lines of evidence that the printed coefficient formula is wrong rather than merely under-specified" (`fpe-starobinsky-coefficient.md`, novelty note + defect). The attempt parenthetically notes "Sketch and possibly off by 16π" and still labels the paragraph Rigorous. (ii) a_2 is rational, not an integer. (iii) "The framework's own version of the junction" — a Euclidean S⁴ anomaly fixed point glued to Lorentzian dS with the same H — is nowhere established: the Riemannian S⁴ self-consistency is asserted only in a Remark by citation (`programs/co-emergence/index.tex:1548-1560`, citing Bunch–Davies, which computes ⟨T⟩ on Lorentzian dS), and the March synthesis lists "Riemannian comparison: construct the analogous Starobinsky self-consistent solution on the round S⁴" as an *undone* next step (`2026-03-03-mass-gap-synthesis.md`, "Lower priority", item 5). (iv) The paragraph's "the premise fails twice: there are two scales, not one" argues against a premise the brief did not state — the brief names "Λ and G as the dimensionful inputs."

**Severity:** presentational (label) + factual.

### 9. Factor-3 error in the HHH branch weight; §3(a) contradicts §1

**Location:** attempt:145-146 vs attempt:39.

**Flaw:** §1 has |Ψ|² ~ e^{3π/(GΛ)} = e^{π/(GH²)} (correct). §3(a) writes the branch weight as e^{+3π/(G H(φ_0)²)}, which is the §1 formula with Λ replaced by H² instead of 3H². Check against HHH08 eq. (4.10) (verified): I = (3π/2H²)∫dτ a(a² − 1) for φ = 0; with a = sin τ over the half-sphere, ∫₀^{π/2} sin τ (sin²τ − 1) dτ = −1/3, so I_half = −π/(2H²) and e^{−2I_R} = e^{π/H²} in their units (G absorbed), i.e. e^{π/(GH²)}.

**Severity:** factual (minor, but it is a displayed formula labelled Rigorous).

### 10. The "ratio of saddle weights" parameter c is not a modulus; it is quantized by the saddle spectrum, and no known saddle gives 0.16

**Location:** attempt:167-175 (§3d), attempt:235 (§4 row), attempt:136-137.

**Flaw:** ΔI between saddles of the same Euclidean action is fixed by geometry/topology. For the pure-Λ pair that FLT17/DTL19 discuss (the two continuations of the same hemisphere; FLT17 verified: the weighting is inverted "from e^{+12π²/ħΛ} to e^{−12π²/ħΛ}"), the weights are e^{±S_dS}, ratio e^{−2S_dS} (c = 2). For distinct topologies with R_μν = Λ g_μν: S²×S² (Nariai) has I = −2π/(GΛ) and CP² (Fubini–Study) has I = −9π/(4GΛ) against I(S⁴) = −3π/(GΛ), giving c = 1/3 and c = 1/4 respectively [my computation from Vol(S²×S²) = 16π²/Λ², Vol(CP²) = 18π²/Λ²; standard but not web-verified here]. Resulting scales at ε_J = 10⁻²: M_P e^{−S_dS/3} ≈ 10⁻⁴⁵ M_P, M_P e^{−S_dS/4} ≈ 10⁻³⁴ M_P, M_P e^{−2S_dS} ≈ 10⁻²⁷² M_P. Nothing near 10⁻²² M_P, and c is not tunable. The "honest tension" the attempt records (needs a second saddle on the same branch) is not the real obstacle; the real obstacle is that ΔI/S_dS takes a discrete set of O(1) values.

**Severity:** structural (the only exponential mechanism in the table has no instantiation).

### 11. §3(c) labels an OS-reconstruction statement "Rigorous" using a flat-space theorem the paper itself says does not apply, and adaptation (2) depends on a claim the repo has gated as blocked

**Location:** attempt:157-165, attempt:319-323, attempt:355-356.

**Flaw:** [OS] proves reconstruction for E(4)-invariant Schwinger functions with a global reflection hyperplane. The co-emergence paper: "the OS axioms require a flat Euclidean background with E(4) invariance and a global reflection hyperplane — fixed background structure that violates Axiom 2 ... the reflection hyperplane defines a preferred direction that becomes time after Wick rotation, which violates Axiom 1" (`programs/co-emergence/index.tex:1823-1830`), and the March debate's surviving verdict is "OS-as-mechanism dies, OS-as-evidence survives" (`2026-03-02-signature-mass-codependence.md`, Pass 2). Reflection positivity of a free field across the S⁴ equator may well be true, but it is not what [OS] establishes, and the attempt's own §6(c) concedes "whether the OS reflection across a derived Σ is even positive is the reframing's own open problem." The Rigorous label can cover the S⁴ spectrum (l(l+3) + 12ξ + m²/H²)H² and nothing else in that paragraph. Further, "the OS-reconstructed state on Σ constructed explicitly" (adaptation 2) is the content of `ce-euclidean-vacuum-at-fixed-point.md`, which the repo holds at Conjecture with `gate: blocked` and an independently fatal falsifier; the attempt does not cite it although it was in the brief's context list.

**Severity:** presentational (label) + dependence on a gated claim.

### 12. The positive content reduces to dimensional analysis, and adaptation (1) imports a UV fixed point by hand

**Location:** attempt:5-9 (committed position), attempt:197-202, attempt:238-241, attempt:306-318 (adaptation 1), attempt:334-335.

**Flaw:** (a) "The exponent lives in the state on Σ, not the geometry." For the HH state of free fields the state on Σ is the Euclidean vacuum, fixed by the same action and the same geometry; the attempt's own §3(c) says the cap "generates no δ ≠ 0." So the state carries no data beyond (H, M_P, field content, couplings of the action). "The state on Σ" is not an independent reservoir; the sentence is equivalent to "with inputs {G, Λ, field content} only functions of those exist; any other scale needs another input in the matter action." That is dimensional analysis, which the attempt already labelled Rigorous at attempt:21-32; restating it as a "pointer" adds no content.
(b) Condition (a) at attempt:197-199 ("⟨T_00⟩_Σ saturates the junction constraint") is automatically satisfied at any self-consistent fixed point — it is the fixed-point equation (flaw 1) — so it constrains nothing. Condition (b) ("homogeneous in a single matter scale") fails for conformal matter at the fixed point in the trivial direction: ρ_anom ∝ a_2 H⁴ is homogeneous of degree 4 in the *only* scale H, giving p = 1/2 again.
(c) Adaptation (1): Coleman–Weinberg transmutation with b from field content and g(M_P) from "a fixed-point condition on g at Σ of the same type as the framework's Level-2 fixed point." That g(M_P) is the entire hierarchy-determining input; "the same field content fixes both a_2 and b" is true but trivial (both are one-loop counting numbers) and leaves it undetermined. Selecting g(M_P) by a UV self-consistency condition is asymptotic safety/UV-fixed-point physics imported by assertion; the only repo antecedent, position-2 §3's "extended map G(g, m_eff)", was a Conjecture that the synthesis assessed as "only determines the self-consistent value of an already-nonzero mass — it doesn't generate mass from nothing" (`2026-03-03-position2-self-consistent-mass.md` §3, Rigorous paragraph; synthesis Verdict 2). The attempt says "nothing in the repo does this"; nothing in the attempt does it either.

**Severity:** structural (tautology check requested by the brief).

### 13. The K_Σ ≠ 0 "modulus" (row 4, adaptation 3) is excluded by the junction literature the repo has already paper-grade verified; the proposed kill computation is Hayward's theorem

**Location:** attempt:104, attempt:231, attempt:293-294, attempt:329-332, attempt:343-345.

**Flaw:** (a) The SCB expanding note's §2 condition is a fixed-background *curvature-boundedness* condition with "no dynamics, no backreaction" and "not a selection principle" (expanding note, Status and scope; §7.1-7.2). It says nothing about whether ℋ_Σ ≠ 0 is compatible with the field equations. (b) For a smooth degenerate signature change, the Einstein-equation junction condition is K_ab = 0: Hayward (verified): "A straightforward calculation shows that a well defined Ricci tensor requires the standard junction condition, namely vanishing of the second fundamental form of the junction surface"; Hayward 1992 (verified abstract): "the spatial metric and the Klein–Gordon field required to be instantaneously stationary at the junction"; Kossowski–Kriele derived vanishing extrinsic curvature as necessary in the smooth case (Dray–Hellaby's comment, verified, disputes it only by adopting *less restrictive smoothness*, i.e. the discontinuous class). (c) The only route to K_Σ ≠ 0 is Ellis et al.'s discontinuous approach, which Hayward shows omits the singular part (24) of the field equations, and for which Hellaby–Dray themselves show conservation laws fail — all recorded in the SCB seed note's Relation-to-existing-work section, with the Hayward attribution corrected in the July red-team audit. (d) In the HH gluing K = 0 is the reality condition (the attempt's own row 3). So under both gluings the attempt names, K_Σ = 0 is forced, and "a second length K_Σ" is not a modulus of any consistent junction in the record. The §6(a) call for "a demonstration that the SCB regular class forces K_Σ → 0 dynamically" is, for the smooth class, already answered by Hayward. (e) Minor: the row-4 constraint carries a 3/a_Σ² term (closed slices, HH's S³) while both SCB notes are flat-slice; the two are spliced without comment.

**Severity:** factual (contradicted by verified literature) + dependence.

### 14. "K = 0 forced ... Rigorous (FLRW)" holds only for FLRW with pure Λ; with any dynamical scalar there is no real junction at all

**Location:** attempt:103, attempt:106, attempt:122-130, attempt:258-264.

**Flaw:** HHH08 (verified, §III.C): "there are no real extrema when the scalar field is non-zero except for special 'false-vacuum' potentials. In general the extrema are necessarily complex. There is thus generally no meaningful notion of a Euclidean instanton nucleating the universe. ... The transition is not sharp as in the zero scalar field case, but rather spread out over a region." So the label "Rigorous (FLRW)" on rows 3 and 6 should read "Rigorous (FLRW, pure Λ or φ at an extremum of V)". The attempt concedes this in §5 bullet 2 but the table and the "single Rigorous conclusion" (which needs a real HH junction) do not carry the restriction. The restriction matters: the "framework's own version" (ii) needs backreacting matter, which is exactly the case in which the real junction does not exist.

**Severity:** factual (label scope).

### 15. The "exhaustive enumeration" is an ADM initial-data set on a slice — the 3+1 description the paper lists as foliation-smuggling — and its "forced" rows were established in a minisuperspace that is itself a slicing choice

**Location:** attempt:93-97, attempt:258-260.

**Flaw:** (Σ, h_ij, K_ij, φ_A, π_A) subject to the Hamiltonian and momentum constraints is canonical ADM data on a Cauchy surface. The paper: "The canonical ADM approach requires a 3+1 decomposition" is the first item in its list of formulations that "introduce hidden temporal or foliation structure" (`programs/co-emergence/index.tex:115-127`), and prop:nohilbert ground (1) is the same point. The attempt states "the count itself does not assume a symmetry (Axiom 2)"; it does assume a slice, which is the Axiom 2 issue the brief asked about. Both "forced" entries (K = 0, π = 0) were derived in FLRW minisuperspace, whose homogeneous slicing is a foliation choice. This is arguably inherited from the reframing rather than introduced by the attempt, but the attempt's axiom check should name it and does not.

**Severity:** axiom (inherited; disclosure gap).

### 16. §3(a) and §3(d) depend on the HH sign, contradicting §2's "independence from the root-uniqueness dispute"

**Location:** attempt:132-137 vs attempt:143-149, 167-175.

**Flaw:** The per-root *count* is sign-independent, as claimed. But "favouring the lowest H" (§3a) and the exponential ratio (§3d) are not: FLT17 (verified) finds the Lorentzian path integral inverts the weighting to e^{−12π²/ħΛ}, which favours the *largest* Λ, and DTL19's Robin conditions are needed to restore the HH sign. §2 claims independence for the whole mass test "except in one place, §3(d)"; §3(a) is a second place.

**Severity:** presentational (scope).

### 17. The "single Rigorous conclusion" contradicts row 2 of its own table

**Location:** attempt:122-130 vs attempt:102, 151-155, 230.

**Flaw:** The conclusion says every dimensionful junction quantity is M_P ε^{k/2} × (integer-valued function of field content) and "there is no tree-level junction quantity with p ∉ ½ℤ." Row 2 and §3(b) say the harmonic tower H√(l(l+2)) spans every p in [0, 1/2] continuously, and §4 lists it as "continuum from 1/2 to 0." The intended reconciliation ("nothing selects l") is a statement about selection, not about existence; as written the Rigorous conclusion is false by the attempt's own row 2. Also "integer-valued" is wrong twice: a_2 is rational, √(l(l+2)) is not integer.

**Severity:** presentational (internal inconsistency in a Rigorous-labelled statement).

### 18. Smaller items

- attempt:78-79: "A ≈ 12 for the pion — 'order one' only loosely." Recomputed: (m_π/60 MeV)³ = 12.7. Fine as stated; but note the relation is then off by an order of magnitude in the *cube*, i.e. a factor 2.3 in the mass, which the attempt should say plainly.
- attempt:207: γ = [12λ + 2Y_2 − …]/16π² ≈ 0.03 uses the paper's EW-scale bracket (+4.8) as if constant from M_P to m; in the SM the bracket's ingredients run substantially (λ turns negative near 10¹⁰ GeV). Does not change the conclusion p ≈ 1/2; noted for completeness.
- attempt:100-109: the topology of Σ and of the cap is a discrete junction datum (HH allows any compact 3-manifold; sums over topologies give the other saddles of flaw 10). It is omitted from the "exhaustive" table. Not a scale, but the table claims exhaustiveness.

---

## Claims that held

I tried to break each of the following and could not.

1. **S⁴ action and no-boundary weight.** I_E(S⁴) = −3π/(GΛ) from R = 4Λ, Vol = 24π²/Λ² (recomputed); half-sphere has K = 0 so no GHY term; |Ψ|² = e^{3π/(GΛ)} = e^{π/(GH²)} = e^{S_dS} with S_dS = A/4G = π/(GH²) (GH77 verified for the entropy–area identification). Cross-checked against HHH08 eq. (4.10) (flaw 9 is that §3(a) then mis-transcribes it).
2. **Junction (i) numbers and exponent column.** H_0 = 1.44×10⁻³³ eV, ε_i = 1.39×10⁻¹²², log₁₀ ε_i = −121.86; p values reproduce to three digits (script below). The Weinberg relation gives 59.8 MeV and p = 1/6 exactly; ρ_Λ^{1/4} = (3Ω_Λ/8π)^{1/4}(M_P H_0)^{1/2} = 2.24 meV and p = 1/4 exactly (p_numerical = 0.252 from the prefactor). Zel'dovich's ρ ~ Gm⁶ ⇒ m = (M_P²H)^{1/3} ⇒ p = 1/6 (algebra checked).
3. **Homogeneity lemma** m^k = M_P^{k−j}H^j ⇒ p = j/(2k). Trivially correct.
4. **Running-ξ exponent.** From eq:beta_xi as written (`programs/co-emergence/index.tex:1305-1310`), (ξ−1/6)(μ) = (ξ−1/6)(M_P)(μ/M_P)^γ with γ = 4.8/16π² = 0.0304; evaluating eq:meff at μ = m gives m^{2−γ} = 12(ξ_P−1/6)H²M_P^{−γ}, p = 1/(2−γ) = 0.508; γ = 1.8 for p = 5. Rederived; correct. (Sketch label appropriate.)
5. **Spectra.** S³ Laplacian l(l+2)/a_0²; S⁴ operator −□ + m² + ξR has spectrum (l(l+3) + 12ξ + m²/H²)H²; l ~ ε^{−1/2} reaches M_P; ~ε^{−3/2} modes below cutoff; electron needs l ~ 10^{38.6}. All correct.
6. **c is gauge.** x⁰ → αx⁰ maps c → cα^{n+2}; c can be set to 1. (n is not — flaw 3.)
7. **Per-root count is independent of saddle multiplicity.** Correct for the count itself (flaw 16 is only about §3a/§3d).
8. **§3(a) "a modulus-labelled family is a spectrum, not a hierarchy"** and HHH08's "the NBWF universally favors histories with φ_0 near the lower bound φ_c" (verified) — correct under the HH sign.
9. **The anomaly–decoupling bootstrap is one equation in N+1 unknowns.** Correct as a counting statement.
10. **CW73 dimensional transmutation as a mechanism** (verified) and DTL19's Robin rescue (verified) are cited accurately for what they are used for.
11. **The attempt's disclosure in §6(c)** is accurate as far as it goes (coefficient Sketch, K = 0 FLRW-only, decoupling function unverified, Halliwell–Hawking and Károlyházy unverified, OS positivity open). The gaps are that flaws 1, 2, 7, 13 are not among the disclosures.

## Computations (script and output)

```python
import numpy as np
hbar_eVs = 6.582119569e-16
H0_SI = 67.4e3/3.0857e22            # s^-1
H0 = hbar_eVs*H0_SI                 # eV
MP = 1.220890e19*1e9                # eV, non-reduced
eps = (H0/MP)**2
print("H0 [eV] =", H0); print("eps_i =", eps, "log10 =", np.log10(eps))
masses = {"rho_L^1/4":2.2e-3,"nu":0.05,"electron":0.511e6,"pion":139.57e6,
          "proton":938.27e6,"Higgs":125.1e9,"vev":246e9}
for name,m in masses.items():
    x = np.log10(m/MP)
    print(f"{name:10s} log10(m/MP)={x:7.2f} p_i={x/np.log10(eps):.4f} "
          f"p(1e-4)={x/-4:.2f} p(1e-10)={x/-10:.2f} p(5.7e-3)={x/np.log10(5.7e-3):.1f} p(0.57)={x/np.log10(0.57):.0f}")
mW = (MP**2*H0)**(1/3); print("Weinberg m =", mW/1e6, "MeV ; (m_pi/m)^3 =", (139.57e6/mW)**3)
OmL=0.69; print("rho_L^{1/4} =", (3*OmL/(8*np.pi))**0.25*np.sqrt(MP*H0)*1e3, "meV")
for a2 in [1e3,1e4,1e5]:
    print(f"a2={a2:.0e}: eps(180pi/a2)={180*np.pi/a2:.2e} H/MP={np.sqrt(180*np.pi/a2):.3f} "
          f"eps(1/a2)={1/a2:.1e} eps(180pi/(16pi a2))={180/(16*a2):.2e}")
for eps_j in [1e-2, 5.7e-3, 0.57, 1e-4]:
    S = np.pi/eps_j; print(f"eps_J={eps_j}: S_dS={S:.1f}, c for 1e-22 MP = {22*np.log(10)/S:.3f}, "
                            f"MP e^-S_dS = 10^{-S/np.log(10):.0f} MP")
gamma = 4.8/(16*np.pi**2); print("gamma =", gamma, " p = 1/(2-gamma) =", 1/(2-gamma))
# Hamiltonian constraint on Sigma with Lambda as input (H=1 units): 8piG rho = 3/a^2 - Lambda, a=1/H, Lambda=3H^2
print("8piG rho_Sigma =", 3*1.0**2 - 3*1.0**2)
# HHH08 eq (4.10) half-sphere integral, phi=0, a=sin(tau)
from scipy.integrate import quad
print("int_0^{pi/2} sin(t)(sin^2 t - 1) dt =", quad(lambda t: np.sin(t)*(np.sin(t)**2-1), 0, np.pi/2)[0])
# saddle actions relative to S^4: I = -(2 Lambda/16 pi G) Vol ; ratios
print("I(S2xS2)/I(S4) =", (16*np.pi**2)/(24*np.pi**2), " I(CP2)/I(S4) =", (18*np.pi**2)/(24*np.pi**2))
```
Output:
```
H0 [eV] = 1.4377e-33
eps_i = 1.3867e-122 log10 = -121.858
rho_L^1/4  log10(m/MP)= -30.74 p_i=0.2523 p(1e-4)=7.69 p(1e-10)=3.07 p(5.7e-3)=13.7 p(0.57)=126
nu         log10(m/MP)= -29.39 p_i=0.2412 p(1e-4)=7.35 p(1e-10)=2.94 p(5.7e-3)=13.1 p(0.57)=120
electron   log10(m/MP)= -22.38 p_i=0.1836 p(1e-4)=5.59 p(1e-10)=2.24 p(5.7e-3)=10.0 p(0.57)=92
pion       log10(m/MP)= -19.94 p_i=0.1636 p(1e-4)=4.99 p(1e-10)=1.99 p(5.7e-3)= 8.9 p(0.57)=82
proton     log10(m/MP)= -19.11 p_i=0.1569 p(1e-4)=4.78 p(1e-10)=1.91 p(5.7e-3)= 8.5 p(0.57)=78
Higgs      log10(m/MP)= -16.99 p_i=0.1394 p(1e-4)=4.25 p(1e-10)=1.70 p(5.7e-3)= 7.6 p(0.57)=70
vev        log10(m/MP)= -16.70 p_i=0.1370 p(1e-4)=4.17 p(1e-10)=1.67 p(5.7e-3)= 7.4 p(0.57)=68
Weinberg m = 59.84 MeV ; (m_pi/m)^3 = 12.69
rho_L^{1/4} = 2.244 meV
a2=1e+03: eps(180pi/a2)=5.65e-01 H/MP=0.752 eps(1/a2)=1.0e-03 eps(180pi/(16pi a2))=1.12e-02
a2=1e+04: eps(180pi/a2)=5.65e-02 H/MP=0.238 eps(1/a2)=1.0e-04 eps(180pi/(16pi a2))=1.12e-03
a2=1e+05: eps(180pi/a2)=5.65e-03 H/MP=0.075 eps(1/a2)=1.0e-05 eps(180pi/(16pi a2))=1.12e-04
eps_J=0.01: S_dS=314.2, c for 1e-22 MP = 0.161, MP e^-S_dS = 10^-136 MP
eps_J=0.0057: S_dS=551.2, c for 1e-22 MP = 0.092, MP e^-S_dS = 10^-239 MP
eps_J=0.57: S_dS=5.5, c for 1e-22 MP = 9.191, MP e^-S_dS = 10^-2 MP
eps_J=0.0001: S_dS=31415.9, c for 1e-22 MP = 0.002, MP e^-S_dS = 10^-13644 MP
gamma = 0.030396  p = 1/(2-gamma) = 0.50772
8piG rho_Sigma = 0.0
int_0^{pi/2} sin(t)(sin^2 t - 1) dt = -0.33333
I(S2xS2)/I(S4) = 0.6667  I(CP2)/I(S4) = 0.75
```
(Output above is from running exactly the script shown; values lightly trimmed for width. For reference, at ε_J = 10⁻² the exponents are electron 11.2, pion 10.0, vev 8.4.)

---

## Citations re-verified

All checked 2026-09-05 by web search/fetch; "content match" means the source supports the specific use in the attempt.

| Key | Existence | Content match to attempt's use | Notes |
|---|---|---|---|
| HH83 Hartle & Hawking, PRD 28, 2960 (1983) | Verified (APS DOI 10.1103/PhysRevD.28.2960) | Yes for the no-boundary definition (compact positive-definite 4-geometries bounded by the 3-geometry). | Fine. |
| HHH08 Hartle, Hawking, Hertog, PRD 77, 123537 (2008), arXiv:0803.1663 | Verified | Yes for φ_0-labelled classical ensemble, classicality condition, "universally favors histories with φ_0 near the lower bound." **Also establishes flaw 14** (no real extrema with nonzero scalar field; transition "not sharp ... spread out over a region") and **flaw 9** (eq. 4.10 normalization). | Attempt uses it correctly for §3(a) modulo the factor 3. |
| FLT17 Feldbrugge, Lehners, Turok, PRL 119, 171301 (2017), arXiv:1705.00192 | Verified | Yes for "Euclidean integral ill-defined / Lorentzian picks a different saddle"; verified text: weighting inverted "from e^{+12π²/ħΛ} to e^{−12π²/ħΛ}", perturbations get "an inverse Gaussian weighting". **Bears on flaw 16.** | |
| DTL19 Di Tucci & Lehners, PRL 122, 201302 (2019), arXiv:1903.06757 | Verified | Yes: Robin boundary conditions, "approximated by stable Hartle–Hawking saddle point geometries". | |
| GH77 Gibbons & Hawking, PRD 15, 2738 (1977) | Verified | Yes: horizon area as entropy; S_dS = A/4G = π/(GH²) follows. | |
| HaH90 Halliwell & Hartle, PRD 41, 1815 (1990) | Verified (APS) | Used only for the complex-contour point; content matches. | Attempt lists it but never cites it in-text. |
| CW73 Coleman & Weinberg, PRD 7, 1888 (1973) | Verified (APS) | Yes: radiative symmetry breaking / dimensional transmutation. | |
| W72 Weinberg, *Gravitation and Cosmology* (1972) | Existence verified | The relation m_π³ ≈ ħ²H_0/(Gc) and the phrase "so far unexplained" are attributed to **p. 620** by a secondary source (arXiv:0803.1309). Primary page not read. | Attempt's "exploratory-tier" flag is correct; the page number is now available. |
| Z67/Z68 Zel'dovich, JETP Lett. 6, 316 (1967); Sov. Phys. Usp. 11, 381 (1968); GRG republication 2008 | Existence verified (ADS/OSTI/Springer) | Rugh–Zinkernagel, *Stud. Hist. Phil. Mod. Phys.* 33, 663 (2002), arXiv:hep-th/0012253 (verified, full text): fn. 13 gives ρ_0 ~ Gm²/λ × 1/λ³ = Gm⁶c⁴/ħ⁴; eq. (16) Λ ~ G²m_p⁶/ħ⁴ with "([74] p. 384)"; records Zel'dovich's own remark that it is ~7 orders too large. | Content matches the attempt's use; **flaw 2** notes the heuristic assumes the m⁴ term is discarded. |
| [OS] Osterwalder–Schrader (repo bib) | In repo bib | **Does not support** the curved-Σ reconstruction claim at attempt:159 (flaw 11); the repo's own text says so. | |
| Hayward, CQG 9, 1851 (1992); and "Junction conditions for signature change", gr-qc/9303034 | Verified (IOP; arXiv) | Used *against* the attempt (flaw 13, flaw 3): K_ab = 0 required; N = t vs N = ε are different differential structures. | Already paper-grade in SCB seed note. |
| Kossowski & Kriele, CQG 10, 2363 (1993); Proc. R. Soc. A 444, 297 (1994) | Verified (via Dray–Hellaby comment GRG 28, 1401 (1996) and JSTOR/RSPA listing) | Smooth vs discontinuous type change inequivalent; vanishing extrinsic curvature derived as necessary in the smooth case; 1994 results stated for transverse type change. Primary 1993 text not read; comment and Hayward's summary used. | Used against flaws 3 and 13. |
| Aguirre, Fernández, Lafuente, arXiv:math/0609838 | Verified (full text) | Definition: transverse type change ⇔ d_p(det g) ≠ 0, "does not depend on the choice of the coordinates." | Used against flaw 3. |
| Wald & Iyer, PRD 44, R3719 (1991) | Verified (APS/PubMed) | Cauchy slicings of Schwarzschild with no outer trapped surfaces. | Used against flaw 4(d). |
| Halliwell–Hawking 1985; Károlyházy | Not verified (attempt flags both as unverified and does not use them) | — | Nothing to check. |
| markkanen_sm_curved (eq:beta_xi source) | In repo bib; not re-verified here | The attempt uses the paper's equation as written; my check of the bracket at the EW scale (≈5.0 with λ≈0.13, y_t≈0.99, g'²≈0.13, g²≈0.42) is consistent with the paper's +4.8. | Not load-bearing for any flaw. |
