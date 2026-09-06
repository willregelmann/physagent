# Attack pass on Position T (tunneling sign via the real-lapse Lorentzian contour)

**Target:** `scratchpad/j6/position-T.md` (2026-09-06). **Date:** 2026-09-06. **Role:** Pass 1 (adversarial critique) of METHODOLOGY's "No Idea Is Eliminated Without a Defense"; no verdict is rendered. Every flaw carries a location, the evidence, and a severity tag. Scripts and outputs are in `scratchpad/j6/attackT/` (the position's scripts were re-run there on an isolated copy so its own pickles were not overwritten). Units as in the position: H₀ = 1, G a = π, actions per a, ε = 1 unless stated.

---

## Flaws

### 1. Items 2–3, §2.4, §1.3(iii) — the positivity F(p) > 0 is the condition for a Euclidean vacuum on the *Hartle–Hawking* sheet; on the tunneling sheet the tensor form is −F, and "compatibility with Vilenkin–Yamada" means flipping the modes back by hand with a boundary term. Position T is a hybrid, not FLT's definition.
- **The flaw.** The position's own sheet language (§3.1: the tunneling sign is the a′(0) = −1 branch, "where I → −I") applies to the *whole* action, background plus quadratic modes: on the −1 sheet the tensor quadratic form is −F(p) < 0 for every p ≥ 2. So §2.4's "the Euclidean vacuum of the tensor modes on the cap exists iff the Euclidean quadratic form is positive-definite on the cap — the condition F(p) > 0" is a statement about the +1 (HH) sheet. Item 2 says exactly this for the tunneling saddle ("the inverse Gaussian is steeper"). Items 2 and 3 therefore contradict each other unless a boundary term re-flips the modes — which is what VY's term does, and what FLT's App. B says it does.
- **Evidence (verified this session, ar5iv/arXiv):** VY 2018 impose the condition at a → 0 (η → −∞) and say of the modes it selects: "The mode functions ν_n(τ) selected by the boundary condition diverge at τ→−∞. This may look worrisome, but we note that R_n± and the wave function are well behaved at a→0." FLT Universe 2018 App. B ("Remark on the new tunneling proposal"): the VY term "has precisely the effect of cancelling the divergence of the action of the c₂ mode, while rendering that of the c₁ mode infinite"; "With their new proposal, one would then be led to pick out the stable c₂ mode", which "tends to infinity as τ^{−k−1}" at a = 0. VY-II abstract: the tunneling state is "a transition amplitude from a universe of vanishing size with the scalar field in the state of Euclidean vacuum" — a state imposed at the initial boundary, not the regular solution on the tunneling saddle.
- **Consequences.** (a) §1.3(i) "definitional economy" fails: the real-lapse integral is not "the one integral convergent without a choice" once a mode boundary term whose only justification is the Gaussian answer is added — the position's own criticism of H ("a parameter and a sign whose only justification is the answer they produce") applies verbatim to VY's term. (b) The two positions are structurally symmetric: each adds a Robin-type term to flip one sector (H the background, T the modes), which the position half-concedes ("Both sides of the debate add a boundary term") and then ignores in its ranking of reasons. (c) The position "commits" to FLT's definition for the background and to a DTL-style redefinition for the fluctuations.
- **Severity:** structural (the crux).

### 2. §3.3, item 5, §4 "Dominant real root" — the saddle set of Ψ(a₁ = 3, K₁ = −i√8) is not {sphere}; widening the position's own search window finds ≥ 18 complex regular caps at these data with Re I/a from −59.5 to +17.8, on both sides of the sphere's −4.5. Under e^{+I} the sphere is not the largest-weight saddle; under the position's own weight rule a saddle with Re I = +17.8 beats it by e^{22a} ≈ e^{1.2 × 10⁵} at a₂ = 10⁶.
- **Evidence.** `attackT/dS_search.py`, `dS_search2.py` (the position's `dbdata_lib.py` shooting and 2-D Newton, J-1 scheme, ε = 1, straight complex paths, same |a| events), starting from c₃ ∈ [−1, 3] (real and complex) and T with |Im T| up to 14 instead of ≤ 2.5. Distinct converged solutions (residual < 10⁻¹⁰; six re-polished to 10⁻¹³ with a halved pole cutoff in `verify_dS.py`, all stable to 4 digits, min |a| along the path = the pole cutoff, i.e. the paths never re-approach a = 0):

| c₃ | T | Re I/a (J-1) | Im I/a |
|---|---|---|---|
| −1/6 (sphere; also T + 2πk copies, same action) | π/2 + 1.763i | −4.50 | −38.18 |
| −0.0611 − 0.0747i | 0.958 − 7.518i | −8.28 | +13.08 |
| −0.0780 − 0.0809i | 3.647 − 7.552i | −4.17 | +13.38 |
| 0.0118 − 0.0001i | −6.007 − 4.177i | −18.55 | −62.57 |
| 0.0062 + 0.0068i | 4.932 + 3.048i | **+1.29** | −27.18 |
| −0.1608 + 0.1173i | −4.089 − 8.821i | −0.36 | +11.03 |
| −0.0246 + 0.0909i | 2.969 − 8.244i | **+16.19** | −75.72 |
| −0.0744 − 0.0938i | 0.234 + 9.330i | −59.51 | +66.84 |
| 0.0085 − 0.0012i | 9.343 + 6.326i | **+17.76** | −89.36 |
| (nine more in `dS_search2.out`) | | between | |

  The range of Re I widens with |Im T| in both directions; no bound above or below was reached. The position's "one saddle in the searched basin" (§3.3) is an artifact of the basin (c₃ ∈ [−0.5, 0.3], |Im T| ≤ 2.5).
- **Consequence.** "Dominant" under e^{+I} at fixed data requires the Picard–Lefschetz relevance analysis that the position labels its central Conjecture (§3.4) and has not done; without it the headline (sphere unique and dominant at every ε; J-1's bound lifted) is unsupported by the position's own method, and at face value contradicted. Existence of these saddles is scheme-independent (the ODE is); their actions are scheme-sensitive (flaw 16).
- **Severity:** structural.

### 3. Item 4, §1.3(ii), §4 "Upstream FPE" — "under e^{−I} the no-boundary measure has no dominant saddle at all" conflates three different objects and is one-sided.
- **Flaw.** The runaway family of §3.3 consists of real caps cut at a₁ = 3 with *real* K₁ = 0.65…36: these are saddles of Ψ(3, K₁) at real Euclidean data, not at the dS-history data (3, −i√8), and with K ≠ 0 they are not junctions of any real history. By the position's own §3.2–3.3 ("the two caps live at disjoint data and never compete at the same argument of Ψ"; dominance is the measure on real histories) they compete with the sphere under *neither* sign in either object the position endorses. They compete only in a K₁-marginal Ψ(a₁), which the position never defines and whose relevance §3.2 denies. And the symmetric statement now holds for T: over the complex saddle set at the dS data, Re I is unbounded above as far as searched (flaw 2), so "the tunneling weight suppresses the runaway" is true for the real family and false for the saddle set. Item 4's "structural argument for Position T that J-1 did not have" therefore does not discriminate between the signs.
- **Evidence.** §3.3 table (re-run `realcaps.rerun.out`: identical); `dS_search2.out`.
- **Severity:** structural.

### 4. §3.4 (the Conjecture and its Sketch) — there is no integral for the "convergent contour" to be a contour of, and the sphere is not a critical point of the only candidate.
- **Flaw.** At fixed (a₁, K₁) the caps reaching the data are isolated points (c₃*, T*): nothing is integrated, so no endpoint "pushes the contour onto a sheet." In the one-parameter family at fixed a₁ (a K₁-marginal), the sphere is *not* stationary — the position's own §3.2: P₂ = (a sech²η/4π²)(6ε + 1) ≠ 0 (I re-derived P₂ = ∂L/∂σ″ = (a/16π²)4σ″ − 72κ(1 − σ″ − σ′²): on the sphere it is exactly the position's value; at flat space, σ″ = 0 and 1 − σ″ − σ′² = 0, so P₂ = 0). So the c₃-family integral has flat space (c₃ = 0) as its stationary point at a₁ = 3 — confirmed numerically: I along the real family is maximal at c₃ ≈ 0 (`runaway_corr.out`: corrected I/a = −4.109 at 0, −4.111 at ±0.001…0.002, falling on both sides) — and no thimble of that integral "reaches the sphere." Falsifier 1's "descent flow of Re(iS) from the real c₃-line on both sheets" is not well posed as stated (which K₁?).
- **Severity:** structural.

### 5. §3.1 (labelled Rigorous), item 5 — the "Casimir-type term" bookkeeping is wrong by a factor 2, and the position's equations of motion and its action values come from two different Lagrangians that differ by a term that is −∞ on every regular cap.
- **Evidence (`attackT/esu_const.py`, sympy; anomaly bracket 2σ″² + 8σ′² + C).** On the round sphere at fixed N_E: C = −8 (J-1's 8(σ′² − 1)): EL_q = 8/(π²t²(t − 4)²) ≠ 0, Ostrogradsky η-energy H_η = a/π². C = 0 (unregularized 8σ′²): EL_q = 4/(π²t²(t − 4)²) ≠ 0, H_η = a/(2π²). C = +8 (8(σ′² + 1)): EL_q = 0, H_η = 0. The position's text says "J-1's Lagrangian (with 8(σ′² − 1)) has the sphere as a fixed-N solution *only after* adding the term (a/2π²) per unit η": adding a/(2π²) to J-1's gives C = 0, which still fails; the fix is +a/π² (C: −8 → +8). The position's own `el_onshell.py` uses `+8` (line 8) — the script is right, the prose is not. This is the same fix the sibling attack found (8(σ′² + 1)).
- **The deeper problem.** With C = +8 the action is ∫(a/16π²)(…+16)dη → −∞ at the pole of every regular cap (the position says so: "logarithmically divergent at the no-boundary point for every path"). Every finite number in §3.1–3.3 — I(T), the FLT-endpoint actions, the saddle actions, the runaway table — was computed with C = −8 (`lapse_action.py` line 14, `complexcaps.py` `Lreg`), i.e. with the Lagrangian on which the sphere is *not* a fixed-N solution and whose constraint fails (its `dL_t/dN` on the sphere is printed by `lapse_action.py` and is nonzero; not reported in §6). §3.2's δI = −H_η δT + P₂ δK₁ "with H_η = 0 after the Casimir term is included" is applied to the C = −8 actions. The constant is an artifact of the non-compact ESU reference: the corrected S⁴-reference functional of PR #222 has no constant and no divergence, and the position derived no lapse-gauge equation from it. "Casimir-type energy of the conformal S³" is decoration (its coefficient a per unit η does not match a Casimir energy, and the corrected scheme has no such term).
- **Severity:** factual (factor 2) + structural (Rigorous label spans two inconsistent Lagrangians; the "fixed-N Gaussian does not exist" argument leans on an ESU artifact for its Casimir half).

### 6. §3.3 "Scheme robustness" — the cap-dependent anomaly shift is not logarithmic; it grows like ≈ 9–10 % of |I|.
- **Evidence (`attackT/runaway_corr.py`, S⁴-reference functional, pole-anchored frame as in the corrected sphere formula).** Real family reaching a₁ = 3, ε = 1:

| c₃ | K₁ | R(T) | I/a (J-1) | I_EH+R²/a | Γ/a (corrected anomaly) | I/a (corrected) |
|---|---|---|---|---|---|---|
| −0.005 | 0.66 | 1.09 | −7.49 | −7.30 | +2.80 | −4.50 |
| 0 (flat ball) | 1.00 | 0 | −6.75 | −6.75 | +2.64 | **−4.11 (sup)** |
| 0.05 | 2.36 | −7.0 | −16.8 | −18.8 | +3.9 | −14.8 |
| 0.1 | 3.15 | −13.3 | −36.7 | −41.0 | +6.5 | −34.4 |
| 0.3 | 5.28 | −39.2 | −174.9 | −191.7 | +23.1 | −168.6 |
| 0.5 | 6.85 | −66.6 | −388 | −423 | +47 | −376 |
| 0.7 | 8.19 | −95.4 | −666 | −724 | +77 | −647 |
| 1 | 9.92 | −140 | −1193 | −1293 | +131 | −1161 |
| 10 | 36.1 | −1876 | −58656 | −63221 | +5163 | −58058 |

  Γ grows as a power (∝ |I_R²|), as it must — the Riegert functional's 2σΔ₄σ contains an R²-like local piece — and the scheme *difference* (corrected − J-1) also grows: +2.6 (c₃ = 0), +32 (1), +599 (10). The runaway and its sign survive (a held claim), but the stated reason ("a logarithm cannot compete") is false, and the "4a ln r" scaling applies to rescaled compact caps, not to cut high-curvature ones.
- **Severity:** factual.

### 7. §3.3 table, §5 falsifier 4 — "the runaway is monotone in c₃" is false, and the printed row that shows it was omitted.
- **Evidence.** `realcaps.py` prints c₃ = +0.010: T = 2.704, K₁ = 1.415, I/a = −7.297 (`realcaps.rerun.out`); the position's table jumps from 0 (−6.75) to 0.05. So I rises from −7.52 (c₃ = −0.005) to −6.75 (0) and falls again; the J-1-scheme maximum is at c₃ ≈ +0.002 (−6.72), the corrected one at c₃ = 0 (−4.11). Falsifier 4 ("none found; the runaway is monotone") is a non-monotone family with an interior maximum — flat space.
- **Severity:** factual / presentational (selective omission).

### 8. §2.2–2.3, §3.3, §5 item 6 — reduced and non-reduced Planck masses are mixed.
- **Evidence.** §3.3: "a₂ = 10⁶ (H₀ ≈ 0.02 M̄_P)": H₀² = 2880π² M̄_P²/(2a₂) gives M̄_P² = a₂/(1440π²) = 70.4 (H₀ = 1), i.e. H₀ = 0.119 M̄_P; 0.02 is H₀/M_P (step-0 table). The tensor cutoff "l = 40 ≈ M_P/H₀" (§2.3, `tensorF.py` prints 42.1) is the non-reduced mass; the curvature criterion "|R(T)| < M̄_P²" (§3.3) uses the reduced one — a factor √(8π) ≈ 5 inconsistency in what "Planckian" means across sections. With M̄_P² = 70.4 the runaway stays sub-Planckian up to c₃ ≈ 0.5 (R = −66.6), not 0.7 (R = −95.4).
- **Severity:** factual (minor).

### 9. §2.3 "Verdict", item 2 — the "steeper by F(l)/(l² + 3l + 6) at every l" factor conflates the S⁴ harmonic label with FLT's S³ label, misidentifies the Einstein piece, and treats a nonlocal operator as a local fourth-order ODE.
- **Evidence.** HHR (3.79) verified: the local piece is (1/16πGR²)[2θθ − ¼θ∇²θ], which on ∇²H = (2 − p(p+3))H gives (p² + 3p + 6)/4 — the pure Einstein–Hilbert expansion, not the Einstein–Λ TT operator (Lichnerowicz − 2Λ on the unit S⁴ is p(p+3); the −6 sits in Ψ's polynomial). FLT's exponent l(l+1)(l+2)φ₁²/(2ℏH²) is for an S³ harmonic l with a time profile; a degree-p S⁴ harmonic decomposes into l ≤ p. The half-manifold on-shell action of the nonlocal CFT piece is a Dirichlet-to-Neumann object, not the closed-sphere eigenvalue ratio; and §2.3(iii)'s "fourth-order mode equation … two-parameter family … Ostrogradsky pair" describes the *local* truncation, whereas HHR handle Ψ(p) only as a harmonic sum continued via p′ = i(p + 3/2) (verified). The position labels the half-sphere step Sketch and then bolds a "Verdict" with a numerical factor "at every l."
- **Severity:** scope / presentational.

### 10. §2.1 "Rigorous by citation" — HHR's F is the strong-coupling N=4 form with a = c and a specific local polynomial; the program's theory is free conformal matter with c/a ∈ [0.58, 3] and its own local finite parts; the κ ↔ α map was only checked through the equations of motion.
- **Evidence.** Position §2.1 concedes the c-scaling and the "(Sketch for content other than N=4)"; but the polynomial p⁴ + 2p³ − 5p² − 10p − 6 in (3.77) is a *local* term and theory-dependent, and the label on item 2 is "Rigorous (numerical) on the sphere." Direct comparison of the R² coefficients (HHR: αN²/(192π²) = αa/(48π²) with a = N²/4; J-1: κ = −a(3ε + 1)/(288π²)) gives α = −ε/2 − 1/6, not −ε/2: the offset is the scheme's local □R/R² content, which the EOM matching absorbs but the position does not state. (The EOM matching itself holds — see "held", item 1.)
- **Severity:** presentational / scope.

### 11. §2 — the scalar sector is omitted, and HHR's own statement puts inhomogeneous negative modes on the sphere for 0 < ε < 1/4.
- **Evidence.** HHR (verified): "If α < −1/8 then only the homogeneous (p = 0) negative mode remains." With α = −ε/2 this is ε > 1/4; for 0 < ε < 1/4 the scalar form (2α∇² − 1)(∇² + 4) has negative modes at every p ≥ 2 with p(p+3) < 1/ε (e.g. p = 2 for ε < 0.1). The position's "the sphere is the unique dominant real root at every ε > 0" (§4) never examines whether the sphere is a one-negative-mode saddle in the sector where the R² term actually acts; the tensor sector alone cannot settle "at every ε."
- **Severity:** scope.

### 12. §3.1, §4 "J-6 orientation", §5 axiom check — "I(T) is even in T, so the sign is a branch of √g, not an orientation" is a non sequitur.
- **Evidence.** I(T) is a polynomial in cos T; I(T) = I(−T) is the identity ∫₀^{−T} f = ∫₀^{T} f for the odd integrand f = L_η/a (L_η even, a = sin τ odd) — a reparametrization, not an operation on the geometry. The operation that flips the sign is N_E → −N_E at fixed q(t): `attackT` sympy check, L_t(−N) + L_t(N) = 0 for both C = ±8 (L_t is odd in N), i.e. reversing the Euclidean lapse *is* the sheet flip a → −a (dη = dτ/a). The two descriptions are one ℤ₂; evenness in T does not separate them. The defensible statement is FLT's — the sign is fixed by convergence at N → 0⁺ and N → ∞, and the (0, ∞) and (−∞, ∞) contours give the same sign — which the axiom check does not invoke. "No arrow is added by the contour" may be right, but not for the reason given; and N > 0 does orient the lapse from the no-boundary point to Σ (coincident with #216 §6d's orientation, which should be said rather than denied).
- **Severity:** axiom / presentational.

### 13. §1.3(iii), §4 "J-4" row, item on "State of minimum excitation" — "J-4 gains a premise" is backwards.
- **Flaw.** VY's Euclidean-vacuum modes are singular at the pole of the tunneling geometry (VY's own sentence, flaw 1), so the cap's field state under T is *not* the regular Euclidean vacuum on the cap; and on the tunneling sheet the tensor form is negative-definite, so "the precondition for a reflection-positive Euclidean vacuum of the gravitons" fails on the position's own sheet. Under T, J-4's premise (Euclidean vacuum of free conformal fields on the round S⁴, regular) becomes a boundary condition imposed at a = 0 against the saddle's regular branch — weaker, not stronger.
- **Severity:** structural (downstream).

### 14. §1.3(iii), §0 — "implemented by a boundary term at the nucleation point" misdescribes VY.
- **Evidence.** VY 2018 impose the condition "at a→0" / "η→−∞"; VY-II: "from a universe of vanishing size." The nucleation point (a = H⁻¹) is not where the term lives. Also: VY's appendix treats the minimally coupled case, which they say is "equivalent to that of gravitational waves" — the position's "open for the graviton" underclaims VY (conservatively) but should say so.
- **Severity:** factual (minor).

### 15. §3.1 "Off-shell paths" — "the fixed-N q-integral of FLT does not exist in this theory" is argued from the *Euclidean* sign of a logarithmic divergence.
- **Flaw.** The R² log divergence on conical paths (checked: a = ατ gives a³R² = 36(α² − 1)²/(ατ), coefficient κ < 0) makes e^{−I} blow up in Euclidean signature; in the Lorentzian integral (N_E = iN, L_t(iN) = i × real on real q, the position's own check) it is a divergent *phase*, which is a convergence/oscillation question, not a damping one — and could as easily be read as a Lorentzian mechanism that kills conical paths. "What exists is the sum over regular caps" is a choice of domain, not a derivation; the Casimir half of the argument is an ESU artifact (flaw 5).
- **Severity:** scope.

### 16. §3.1, §3.3, §6 "Scheme note" — corrected actions of *cut* caps are frame-dependent, and on long complex paths the pole-anchored S⁴-reference is unusable.
- **Evidence.** The S⁴-reference Γ is Möbius-invariant only for compact caps; a cut at Σ makes Γ depend on the Möbius frame (θ = τ at the pole is one choice — the one under which the sphere's corrected I(T) has Γ = 0). `verify_dS.py`: the six extra dS-data saddles have corrected pole-frame Γ giving I_corr/a = +484, +2.3, −10.1, +9.0, −2.9 × 10⁵, +3.0 against J-1-scheme −8.3, −4.2, −18.6, +1.3, −0.4, +16.2. The two schemes differ by cut-dependent boundary terms that no one has fixed (Herzog–Huang–Jensen give the a-anomaly boundary terms; not transcribed by either position). The sphere's "exactly the half-sphere in either scheme" (§3.1) is a frame statement.
- **Severity:** scope (shared with H; bears on any corrected-scheme number at Lorentzian data).

### 17. §6 — selective reporting.
- `lapse_action.py` prints "dL_t/dN_E on the sphere (should vanish identically…)" followed by a nonzero expression; §6 reports the `I(T)` and endpoint lines from the same run and omits this one (the text's H_η discussion covers it only for C = 0, flaw 5). `realcaps.py`'s c₃ = +0.01 row is omitted (flaw 7). `saddles2.py`'s DB-data section returns no saddle (nested Newton fails at a′ = 0); the text correctly reroutes to `dbdata.py` but the §6 sentence "verbatim from `saddles2.out`, `dbdata.out`" hides that `saddles2.out` is empty there.
- **Severity:** presentational.

### 18. §0 item 5, §3.1 — the label "Rigorous, symbolic + numerical" covers the inconsistency of flaw 5; §4's "every ε" is computed at ε = 1 only.
- All saddle enumerations (§3.3) and the runaway table are ε = 1; the ε-dependence of the complex saddle set (flaw 2) is unexamined, yet §4 asserts dominance "at every ε > 0" and lifts J-1's bound for all ε.
- **Severity:** presentational / scope.

---

## Claims that held (what I tried and could not break)

1. **Tensor form and mapping.** `tensorF.py` re-run reproduces every printed number. Ψ(p) and F(p, α, β) match HHR (3.77) and (3.82) verbatim (ar5iv, this session); the digamma asymptotics give Ψ → 2p⁴ ln(p/2). α = −ε/2 is consistent with HHR (3.80) three ways: the (∇̂² + 4) factor gives λ ∈ {1, −4} on e^{λt} (matching step 0's (λ + 4) and the conformal-Killing root), (2α∇̂² − 1) = 0 gives λ² + 3λ = −1/(2α) = 1/ε, and HHR's m² = 1/(2α) = −1/ε is the tachyonic scalaron of |m| = M/H₀. F(p) > 0 for all p ∈ [2, 200] for β > −1.10 (F(2) = 263.6 + 240β + 20ε), and the negative window sits at β ≤ −2, far outside HHR's β > log 2 − 1 (verified sentence: "In order for tachyons to be absent in flat space, we had to choose β > log 2 − 1"). Within HHR's model this is Rigorous (numerical); the caveats are flaws 9–11.
2. **The sphere's truncated action.** Re-derived analytically: EH piece −1 + (3/4)c + (1/4)c³, J-1 anomaly piece −5/6 + (3/4)c + (1/12)c³, R² piece −(3ε + 1)(2/3 − c + c³/3), c = cos T; sums to the position's I(T)/a in both schemes, −(5 + 4ε) and −(10/3 + 4ε) at T = π; Re I at T = π/2 ± i arccosh a₁ is the constant term (cos T purely imaginary) — the half-sphere; the phase ∓[(7/4 + 3ε)y + (ε + 1/12)y³] checks. `verify_dS.py` reproduces −3.6667 − 37.948i along the complex path with Γ = 0 (pole frame).
3. **FLT bookkeeping.** `fltcheck.py` re-run: Im N_s > 0 ↔ Re(iS) = −4π² (suppressed). The (0, ∞) and (−∞, ∞) convergence argument (Re(iS) ≈ −3q₁² Im N/(4|N|²) as N → 0 decays for Im N > 0 on both half-lines) checks.
4. **The runaway under the HH weight is real and survives the correction.** Corrected-scheme I/a = −14.8, −34.4, −169, −1161 at c₃ = 0.05, 0.1, 0.3, 1 (table in flaw 6); unbounded below as c₃ → ∞. **The real family reaching a₁ = 3 has a finite supremum**: −4.11 (corrected, at flat space c₃ = 0), −6.72 (J-1, c₃ ≈ 0.002); caps with c₃ < −0.005 never reach a = 3 (a_max = 2.80 at −0.01). So on the *real* family there is no tunneling-side runaway; the tunneling-side problem is the complex saddle set (flaw 2).
5. **The +8 fix.** With 8(σ′² + 1) the sphere solves the fixed-N q-equation identically and H_η = 0 (my sympy, flaw 5); `el_onshell.py` re-run gives EL_t = 10⁻¹⁴ on the c₃ = −0.3 cap and 0.145 on the constraint-breaking perturbation. This is the sibling attack's fix; both positions' scripts agree, both positions' prose is loose.
6. **DB-data saddles.** `dbdata.py` re-run reproduces the four real saddles; in the corrected pole frame (`dbcorr.py`) they are −6.20 (symmetric DB half), −6.12 (asymmetric), −3.13 (small cap, c₃ = −0.606), −6.74 (large cap, c₃ = −0.254): the DB is neither the least- nor the most-suppressed under either sign, as the position says; the sphere's equator half is −3.67. The DB's continuation to a = 3 lands at T = 0.988 ± 1.518i, a′ = −0.70 ∓ 4.53i (re-run) — not the dS data.
7. **The sphere is a saddle at (3, −i√8)** with the stated action and, in the corrected pole frame, Re I = −3.67; the K₁ = +i√8 conjugate exists. What failed is uniqueness (flaw 2).
8. **Quotations.** Every FLT/DTL/VY/HHR sentence the position quotes that I re-fetched is verbatim (table below).

## Citations re-verified (content and polarity)

| Reference | Fetched | Outcome |
|---|---|---|
| Hawking–Hertog–Reall, PRD 63, 083504 (2001), hep-th/0010232 | ar5iv full text | (2.9) S_ct = αN²/(192π²)∫√g R²; (3.15) with β and "The finite part of this term is arbitrary"; (3.77) Ψ(p) verbatim; (3.80) ψ(2α∇̂² − 1)(∇̂² + 4)ψ; (3.81)–(3.82) F verbatim; (3.79) local piece 2θθ − ¼θ∇²θ (⇒ p² + 3p + 6 is EH without the Λ-like term); "β > log 2 − 1" (tachyon-free flat space); m² = 1/(2α), "tachyon"; "If α < −1/8 then only the homogeneous (p = 0) negative mode remains"; "if α < 0 … two regular compact instantons"; Lorentzian continuation via p′ = i(p + 3/2). Polarity as used ✓; see flaws 9–11 for scope. |
| FLT, PRL 119, 171301 (2017), 1705.00192 | ar5iv | All four principled-case sentences verbatim ✓; G_φ ∝ exp[l(l+1)(l+2)φ₁²/(2ℏH²)] "inverse Gaussian" ✓; "unavoidable" ✓; mode condition = q(0) = 0 with finite, stationary action ✓. Polarity ✓ (tunneling sign; unsuppressed perturbations). |
| FLT, PRD 95, 103508 (2017), 1703.02076 | arXiv abstract | Verbatim: "unambiguously determines which semiclassical saddle point solutions are relevant" and "precisely the inverse of the famous Hartle-Hawking result" ✓. |
| FLT, PRD 97, 023509 (2018), 1708.05104 | arXiv abstract | "prove there is no choice of complex contour for the lapse which avoids this problem"; "extra, non-perturbative corrections" ✓. |
| FLT, Universe 4, 100 (2018), 1805.01609, App. B "Remark on the new tunneling proposal" | ar5iv | Boundary-term and τ^{−2k−4}/"out of control" sentences verbatim ✓; **adds**: the VY term picks "the stable c₂ mode," which "tends to infinity as τ^{−k−1}" at a = 0; conclusion "proposed rescue … also fails." Polarity: FLT against VY ✓ (as the position flags). No later FLT reply to VY-II found (one search; not claimed absent). |
| Vilenkin–Yamada, PRD 98, 066003 (2018), 1808.02032 | ar5iv | Condition at a → 0 (η → −∞), not at the nucleation radius (flaw 14); "conformally coupled massive scalar" in the text, minimally coupled (≡ gravitational waves) in an appendix; **the selected modes "diverge at τ→−∞"** (flaw 1); lapse N real positive; saddles N± = iH⁻²(1 ∓ √(1 − H²a₁²)). Polarity: fluctuations well behaved with their condition ✓. |
| Vilenkin–Yamada, PRD 99, 066010 (2019), 1812.08084 | arXiv abstract | Verbatim, incl. "transition amplitude from a universe of vanishing size with the scalar field in the state of Euclidean vacuum." Polarity ✓ (conformal scalar exact; backreaction finite, contra FLT). |
| Di Tucci–Lehners, PRD 98, 103506 (2018), 1806.07134 | arXiv abstract | "We confirm that the fluctuations are unstable, even in this restricted context" ✓. |
| Di Tucci–Lehners, PRL 122, 201302 (2019), 1903.06757 | ar5iv | "redefined to be over geometries with approximately zero initial size and approximately Euclidean initial momentum" ✓; HH exponent e^{+4π²/(ℏH²)}, "Gaussian distributed perturbations" ✓; "off-shell geometries do not start at zero size" ✓. Polarity ✓. |
| Di Tucci–Lehners–Sberna, PRD 100, 123543 (2019), 1911.06701 | arXiv abstract | Verbatim final sentence ("all current working examples … abandon the notion of a sum over compact and regular geometries, and point to the importance of an initial Euclidean momentum") ✓. |
| Hawking–Luttrell 1984; Duff 1994; Salvio 2018; Lehners 2023 | not re-fetched | Used by the position as flagged (snippet / prior cycle / summary-level / not cited); non-load-bearing; no issue. |
| Herzog–Huang–Jensen, JHEP 01 (2016) 162 | not fetched here | Named by the lead and the sibling attack for the boundary terms of flaw 16; not used by the position. |

## Scripts (all in `scratchpad/j6/attackT/`)
- Re-runs of the position's `tensorF.py`, `fltcheck.py`, `realcaps.py`, `dbdata.py`, `el_onshell.py`, `lapse_action.py`, `saddles2.py` → `*.rerun.out` (all reproduce the position's printed numbers; `lapse_action.rerun.out` shows the unreported nonzero `dL_t/dN`).
- `esu_const.py` — ESU-frame constant C ∈ {−8, 0, +8}: EL_q(sphere), dL_t/dN, Ostrogradsky H_η (flaw 5).
- `runaway_corr.py` → `runaway_corr.out` — real family at a₁ = 3 in both schemes; sup/inf; M̄_P² threshold (flaws 6–8, held 4).
- `dbcorr.py` → `dbcorr.out` — corrected pole-frame actions of the four DB-data saddles and the sphere half (held 6).
- `dS_search.py`, `dS_search2.py`, `verify_dS.py` → `*.out` — the complex saddle set at (3, −i√8) (flaw 2, 16).
- Inline sympy: L_t odd in N (flaw 12).
