# Attack pass on the J-7a note (`notes/2026-09-08-j7a-boundary-problems-defined.md`)

**Role:** attack pass only (METHODOLOGY "No Idea Is Eliminated Without a Defense", pass 1). No verdicts, no fixes beyond naming what is wrong. A separate steelman pass receives this file.
**Date:** 2026-09-08. **Units:** as in the note (H₀ = 1, actions per a, ε = H₀²/M², v = da/dτ, q = a²).
**Scripts written for this pass** (all in `scratchpad/j7/`, prefix `atk_`, outputs alongside): `atk_hj_fine.py/.out` (finer-step Hamilton–Jacobi recheck), `atk_family.py/.out` (completeness of the real a = 2 family; fate after recontraction; neck-class caps; the on-shell (a,R) action along the family), `atk_cone.py/.out` (sign of the cone coefficient at small v; scheme independence of the anomaly-sector log coefficient; the smoothing family's pole data), `atk_census.py/.out` (path dependence of the fixed-(a,v) census; stopped after saddles sphere/A/B once the point was made — saddle C's real-axis-first path overflows).
**Sources read in full or at passage level:** the note; J-6 synthesis (§1.4, §1.7, §2.4, §3.2, §9); J-1 note; `position-H.md`, `steelman-H.md`, `position-T.md`, `steelman-T.md` (grep + passages); `j6/ccaps.py`, `j6/steelmanH/invariant.py`, all `j7/*.py` and `.out`; `dh09.txt` (Dyer–Hinterbichler) and `fs95.txt` (Fursaev–Solodukhin) at the cited passages.

**One-paragraph orientation.** The note's central analytic result (§2: Q = (ε/4)a²R, P = p_a^{ESU}, anomaly sector contributing nothing to Q) survives every attack I could mount, including an independent off-shell derivation and a finer-step numerical recheck (flaws 13–14 below are cosmetic). The fixed-(q,R) tables (§4) reproduce. What does not survive is (i) the note's headline sign asymmetry for conical initial data (§7: the tunneling sign is *not* protected for ε < 1 — the note's own formula says so), (ii) the interpretation that "the regular-pole restriction" rescues the Hartle–Hawking sign (the family that diverges is regular at the pole), (iii) the framing of the real-v line as the "natural" contour of the (q,R) problem (in Ostrogradsky canonical quantization the transform is over real Lorentzian v_L, i.e. imaginary Euclidean v — the note's "adaptation" is the default and its "obstruction" is a statement about a contour neither surviving position uses), (iv) the single-saddle truncation behind "Ψ_T ∝ e^{+9.45a}", (v) the mis-stated mechanism of the contracting-side divergence, (vi) the claim that the radius marginal needs no boundary term because P_R = 0 at flat balls (P_R ≠ 0 there; it vanishes at v = 0 cuts — J-1's junctions), and (vii) the census ranking's path/sheet dependence. Several "unaffected" claims are too quick.

---

## 1. §7 / §0 item 6 / README row 44 — "under the tunneling sign cones are suppressed automatically" is false for ε < 1, including throughout H's window and at the note's own test value ε = 0.3

**Claim attacked.** §0 item 6: "under the tunneling sign cones are suppressed automatically"; §7 bullet 1: "Under e^{+I} sharp cones are suppressed automatically. This is a sign asymmetry of the off-shell construction"; README row 44: "automatic under the tunneling sign".

**Flaw.** The note's own coefficient, c(v,ε) − c(1,ε) = −(v−1)²[3ε(v+1)² + (v−1)(v+3)]/(4v), is **positive** for v < v*(ε) where 3ε(1+v*)² = (1−v*)(3+v*), so the smoothed-cone action goes to **+∞** logarithmically there and e^{+I} is **unbounded**. The note even states the condition for −∞ ("for v < 1 whenever 3ε(1+v)² > (1−v)(3+v)") and then asserts the opposite regime is harmless. The v → 0⁺ limit of the coefficient is (3/4)(1−ε)/v: for every ε < 1 narrow cones are infinitely *enhanced* under e^{+I}, and the more needle-like the cone the worse. At ε = 1 exactly the threshold sits at v* = 0, which is why the note's test grid (v = 0.8, 0.9, 1.1, 1.2, 2 at ε = 0.3, 1) never saw it.

**Evidence.** `atk_cone.out` (1): thresholds v* = 0.512, 0.451, 0.392, 0.265, 0.085, 0.000 at ε = 0.25, 0.3, 0.355, 0.5, 0.8, 1. At ε = 0.3: c(v)−c(1) = +8.60, +3.44, +1.01, +0.32 at v = 0.05, 0.1, 0.2, 0.3. Quadrature on the note's own smoothing family reproduces it: ε = 0.3, v = 0.1: I(δ = 10⁻², 10⁻³, 10⁻⁴) = +44.36, +51.88, +59.77, slope dI/dln(1/δ) = +3.43 (sympy +3.44); v = 0.2: +1.007 (sympy +1.011). At ε = 1 all tested v give negative slopes, as the note found.

**Consequence.** There is no sign asymmetry of the off-shell construction in H's window: under e^{−I} the wide cones (v > 1) and the moderate narrow cones (v* < v < 1) are unbounded, under e^{+I} the needles (v < v*) are. The anomaly sector (the (v−1)³(v+3) piece, positive for v < 1) is what does it — a Casimir-like cost of a narrow cone that the tunneling weight turns into an enhancement. The rigor row "Conical initial data: log coefficient, sign, consequence for the two signs — Rigorous" is wrong in its last clause, and the T-side sentence of §9 ("the mirror image") is missing its own mirror.

**Severity: serious** (headline claim; false exactly where the note advertises its ε = 0.3 test).

## 2. §7 bullet 1 — "the Hartle–Hawking-sign state exists only with the regular-pole restriction imposed by definition": the diverging family *is* regular at the pole

**Claim attacked.** §7: "The obvious enlargement is to drop the pole regularity a′(0) = 1. For a cone a = vτ smoothed at scale δ (a = τ + (v − 1)(√(τ² + δ²) − δ)) …"; "the Hartle–Hawking-sign state exists only with the regular-pole restriction imposed *by definition* (as the no-boundary proposal does, but here it is load-bearing rather than aesthetic)"; §0 item 6 and README row 44 repeat it.

**Flaw.** The smoothing family does not drop pole regularity: a(0) = 0, a′(0) = 1, a″(0) = (v−1)/δ (`atk_cone.out` (3)). Every member is a regular-pole geometry; only the δ → 0 limit is a cone. The logarithm comes from the region δ ≪ τ ≪ 1 where R ∝ (1−v²)/τ² and a³R² ∝ 1/τ, not from the tip (the tip region contributes O(1): R ~ (v−1)/δ² over a volume ~ δ⁴). So the restriction "a′(0) = 1" does not bound the Hartle–Hawking exponent from below — the family that sends I → −∞ satisfies it. The only reading under which "regular-pole restriction" rescues anything is "restrict to the on-shell regular caps (the c₃ family)", i.e. no off-shell integral at all — which contradicts the section's own first sentence ("a saddle-point 'relevance' statement needs an off-shell integral") and reduces §7's conclusion to "the sum over saddles is a sum over saddles". What §7 actually shows is stronger and worse for both signs than the note says: the fourth-order action is unbounded (below under e^{−I}, above under e^{+I} for ε < 1, flaw 1) on regular-pole off-shell paths near every cone, so any definition of either state must be a thimble integral in which these directions are excluded by the contour, not by a pole condition. (J-6 §1.8 and steelman H flaw 5 already said this for the HH sign; the note walks it back.)

**Severity: serious** (interpretation of a Rigorous computation; the computation itself is fine).

## 3. §5 item 1 — the stated mechanism of the contracting-side divergence is backwards

**Claim attacked.** §5 item 1: "E_HH → +∞ at both ends of the real family (the runaway of J-6 §1.2 on the expanding side; **on the contracting side the boundary term +12ε|v| outruns I_inv**)" and "it is not cured by the boundary term — **the boundary term is what produces the contracting-side divergence**."

**Flaw.** E_HH = −I_inv + 12εv with v < 0 on the contracting side, so the boundary term contributes −12ε|v| — negative, *opposing* the divergence. The divergence is −I_inv → +∞: at v = −7.51, −9.80 (ε = 1) the note's own table has I_inv = −103.5, −171.8 (−I_inv ≈ 1.8v²) against 12εv = −90.1, −117.6 (`vfamily.out`). The contracting-side blow-up is the same R² runaway as the expanding side (the recontracting caps that reach a = 2 with large |v| have grown to a_max = 4.9, 5.6 and carry a large negative R² action), and the boundary term *slows* it. The conclusion (divergence) stands; the physics sentence is wrong and it propagates: "not cured by the boundary term — the boundary term is what produces" should read "the boundary term reduces the divergence on this side but cannot overcome a quadratic runaway with a linear term".

**Severity: minor–serious** (wrong mechanism in a headline paragraph; the number is right).

## 4. §5 / §0 item 4 / §9 — the v-transform integrand uses a single saddle of the (a,v) problem at each real v; "Ψ_T(4,12) ∝ e^{+9.45a}" and "global maximum on the real line" rest on that truncation

**Claim attacked.** §5: "The Laplace transform of §3 is a one-dimensional integral over the real regular caps through a₁ = 2"; item 3: "Under e^{+I} the real-v integral converges and the recontracting cap is its global maximum on the real line: Ψ_T(4,12) ≈ e^{+9.45a} × Gaussian"; §9 T bullet: "its dominant saddle at de Sitter data is a non-classical cap with a growing amplitude e^{+9.45a}".

**Flaw.** The transform's integrand is Ψ(a,v), which the note itself writes as Σ_saddles e^{∓I_inv}. At real (2, v) the note evaluates only the *real* cap. The J-6 census found ≥ 18 complex regular caps at a single (a,v) data point with Re I_inv from −58 to +22 (§6 of the note); no search for complex caps at real (2, v) was made. Under e^{+I} any complex cap at (2, v) with Re I_inv above the real cap's (the F-type saddles at +22 exist at the Lorentzian data) would dominate the integrand and displace the "global maximum"; under e^{−I} any complex cap below the real cap's I_inv would change E_HH(v) pointwise (the divergence conclusion survives, since one divergent term suffices absent cancellation, but the "minimum at the recontracting cap" shape does not automatically). The rigor row labels item 3 "Rigorous (numerical) on the scanned family"; it is a saddle-point evaluation with an unjustified one-term truncation and should be Sketch/Conjecture. The same truncation is hidden in "E_HH(v)" being called *the* exponent.

**Severity: serious** for §5.3 and the §9 T bullet; minor for §5.1.

## 5. §5, §8, §9, §0 item 4 — the real-v line is called the (q,R) problem's "natural" contour and the imaginary-v line an "adaptation"; canonically it is the reverse, and neither surviving position uses the real-v line

**Claim attacked.** §8: "the (q, R) problem's natural real-v contour fails for the Hartle–Hawking sign (divergent) and, for the tunneling sign, converges onto a growing non-classical cap"; §0 item 4: "Neither sign defines Ψ(q, R) from the real Euclidean family alone … Both are obstructions in the (q, R) representation; the adaptation is stated in §8"; §8 "The adaptation": "the v-contour taken along the Lorentzian line v ∈ iℝ".

**Flaw.** In Ostrogradsky canonical quantization the passage from the configuration representation Ψ(a, v_L) to the mixed representation Ψ(a, Q) is the Fourier transform over the real Lorentzian configuration variable v_L = da/dt, kernel e^{−iQ_L v_L}. With τ = it, v = da/dτ = −i v_L and Q = ∂I/∂v = ∂S/∂v_L = Q_L (both equal (ε/4)a²R), so e^{−iQ_L v_L} = e^{+Qv} on v ∈ iℝ. That is exactly the note's "adaptation" — kernel sign included — and it is the default, not a repair. The real-Euclidean-v line is natural only for a path integral over real Euclidean four-geometries; H′ (DTL's Robin condition on a Lorentzian lapse integral) and T′ (FLT's real-lapse contour) are both Lorentzian-contour definitions, so for both the cut datum v — an interior variable of the (a,R) problem — is real Lorentzian, i.e. imaginary Euclidean. Consequences: (a) §5's "Ψ_HH(q,R) is not defined by real Euclidean data" is true but is a statement about a contour no surviving position proposed, so "obstruction" overstates it; (b) the T bullet of §9 attacks T′ with a contour T′ never used — on an FLT-type contour the exponent starts at Re = 0 and FLT's theorem (J-6 §9.2) forbids a relevant saddle with Re(exponent) = +9.45, which the note's last §9 sentence concedes while §0 item 4 states "giving Ψ_T(4,12) ∝ e^{+9.45a}" flatly; (c) §8's "Then Ψ(q, R) inherits whatever contour the (a, v) problem is given" is false as stated: the cut datum v is an *additional* integration variable in the (a,R) problem whose contour must be specified independently of the (a,v) problem's interior contour — the imaginary line is a (standard) choice, not an inheritance. What §5 establishes, stripped of the framing: on the Euclidean-real-v line the recontracting cap is a relevant saddle (its anti-thimble is that line, so its intersection number with it is ±1) of a divergent integral under e^{−I}, and of a convergent one under e^{+I} — a fact about one non-canonical contour.

**Severity: serious** (framing/overreach that shapes the "obstruction" and the J-7b plan; the numerics are untouched).

## 6. §8 — "The 'radius marginal' (flat balls at R = 0) needs no new boundary term (P_R = 0 there)": P_R does not vanish at the flat ball; it vanishes at v = 0 cuts, which changes which caps are the marginal's saddles

**Claim attacked.** §8 "Defined": "The 'radius marginal' (flat balls at R = 0) needs no new boundary term (P_R = 0 there) but its measure remains undefined"; §4: "Flat balls (R = 0) and neck-data saddles (v = 0) have vanishing boundary term; nothing in J-6 §1.2 or §1.9 changes."

**Flaw.** The note's own §3 gives P_R = −(ε/4)a²v. At the flat ball v = 1, so P_R = −(ε/4)a² ≠ 0 (= −1 at a = 2, ε = 1). What vanishes at the flat ball is the *boundary term* −vQ = −(ε/4)a²Rv (because R = 0), not the momentum conjugate to R. The note conflates the two. This matters because the two marginals have different saddles: the marginal over v of Ψ(a,v) (natural boundary condition Q = 0 ⇔ R = 0) is stationary on flat balls — steelman H's flaw-1 statement — whereas the marginal over R of Ψ(a,R) (natural boundary condition P_R = 0 ⇔ v = 0) is stationary on the *turning-point caps with K = 0*, i.e. exactly the reflection-symmetric cuts of J-1's closed instantons. Position H (line 117) had this right: "p_{a′}-type for the Ostrogradsky choice, K = 0 for the (q, R) choice with its Legendre boundary term". The note's "radius marginal" is therefore misidentified, and its §4 claim that flat balls are unaffected mixes a true statement (boundary term = 0 at R = 0) with a false one (P_R = 0). Related and unrecorded (`atk_family.out` (c)): the on-shell fixed-(a,R) action along the real family at its own (a = 2, R) is **bounded below** — I_(a,R) = −4.39 (min, near the v ≈ 0 cap, ε = 1), −2.44 (ε = 0.3) — and goes to +∞ at both ends (+1629 at c₃ = 2, +173 at c₃ = −0.0005, ε = 1), while I_inv → −∞ there. J-6 §1.2's "real regular caps' local action unbounded below for ε > 0" is thus a (a,v)-representation statement; in the (a,R) representation the same caps have no runaway. "Nothing in J-6 §1.2 changes" is not true of how §1.2 must now be read.

**Severity: serious** (an explicit "does not apply" claim that is false, and it inverts which caps the (q,R) marginal selects — with a direct link to J-1's K = 0 junctions the note should have seen).

## 7. §4 / §0 item 3 — "at late times the sphere is the lowest of the known saddles of Ψ(q,R)" is conditional on a Sketch-level exclusion the note declines to re-examine, and the pair's ε-continuation silently failed

**Claim attacked.** §0 item 3 (labelled Rigorous (numerical)): "at late times the sphere is the lowest of the known saddles of Ψ(q, R) for every ε in H's window and above it"; §4: "The complex pair remains below the sphere by 0.1–0.4a throughout H's window (1.4a at ε = 1); steelman H's constant-lapse exclusion of it is unaffected by this note and is not re-examined here."

**Flaw.** By the note's own table the complex pair has Re I_(a,R) below the sphere's at every ε tabulated (gap −0.11 … −0.37 in the window, −1.39 at ε = 1) and is "not tracked" in q. It is removed only by steelman H's sheet criterion ("not a constant-lapse geometry ⟺ passes through zero size"), which steelman H labels Sketch and lists under "What the rescue could not do" item 2 ("verified on the complex pair at three ε values; should be … stated as a general property"). At (9,12) steelman H found a complex pair "untested for constant lapse". So "lowest of the known saddles" is Rigorous (numerical) only among {sphere, recontracting cap}; among the *known* saddles it is conditional on an unproved exclusion. Separately, `ar_table.out` shows the pair's Newton continuation at ε = 0.7 and 1.0 converging to a copy of the sphere on another sheet (v = −1.7321i, I_inv = +3505.9, +3505.3), i.e. a failed continuation; the note's table cell "see §6 note" (ε = 0.70) points to nothing — §6 is the census and contains no such note — and the ε = 1 entry (−4.394) is imported from `invariant.out` (d) rather than from the table's own run. `av_fix.py` (still running) is where the repair lives; the note does not say so.

**Severity: serious** for the headline's label; **cosmetic** for the dangling cross-reference.

## 8. §6 / §0 item 5 — the twelve census values are path/sheet-dependent and no constant-lapse test was applied; "sixth-highest" is miscounted

**Claim attacked.** §6: "12 are evaluated in the invariant scheme; the sphere is sixth-lowest under e^{−I} … and sixth-highest under e^{+I}"; "At fixed (a, v) the sphere is extremal under neither sign"; README row 41 states this as a fact.

**Flaw.** (a) J-6 §1.3 required that "the remaining competitors need the same [constant-lapse] test" before being called anything; the note ranks them without it. `atk_census.out`: saddle A on the straight path and on the vertical-then-horizontal path gives Re I_inv = −5.58 (gauge found), but on the real-axis-then-vertical path the same endpoint (a = 3, v = −i√8, so the same sheet of a(τ)) gives Re I_inv = −92.5 with the gauge solve failing; saddle B on the real-axis-first path lands on a different sheet of a(τ) altogether (a = 0.60 − 0.42i). So the straight path is not homotopic to the real-axis-first path relative to the singularities of a(τ), and the note gives no criterion for which path is the admissible (constant-lapse) one. The "Numerical observation" label is honest as far as it goes, but "extremal under neither sign" is drawn from values whose sheet is unspecified. (b) Count: six saddles (B, G, E, D, L, F) lie above the sphere, so it is *seventh*-highest, as §6's own sentence "six lie above it" implies; §0 item 5 says sixth. (c) Six of eighteen — including P, J-6's named adversary — remain unevaluated; the note's ranking claim is robust to them only in the weak sense that "not extremal" cannot be undone by adding saddles, which is the one thing the six cannot change.

**Severity: serious** for (a); **cosmetic** for (b), (c).

## 9. §3 — the Laplace-transform kernel has the wrong sign for both signs (typo relative to the note's own §5 and scripts)

**Claim attacked.** §3: "Ψ_∓(a, R) = ∫_𝒞 dv exp[∓(ε/4)a²Rv] Ψ_∓(a, v), Ψ_∓(a, v) ≈ Σ e^{∓I_inv}, whose v-saddle condition Q(a, v) = (ε/4)a²R …".

**Flaw.** With the upper sign the integrand is e^{−(I_inv + Qv)}, whose saddle is ∂I_inv/∂v = −Q, i.e. R(v) = −R_prescribed, and whose value is not e^{−I_(a,R)}. The kernel that gives the stated saddle condition and reproduces I_(a,R) = I_inv − vQ is exp[**±**(ε/4)a²Rv]. `vfamily.py`'s header ("Psi_HH(a,R) = int dv e^{−I_inv + (eps/4)a²Rv}") and E_HH = −I_inv + 12εv use the correct sign, so the numerics are unaffected. The sign is load-bearing for J-7b (the direction of the phase along v ∈ iℝ and which half-plane the transform converges in).

**Severity: minor** (typo in a formula that J-7b will copy).

## 10. §3 — δI_(a,R) = P δa − (ε/4)a²v δR misstates the a-momentum of the (a,R) problem

**Claim attacked.** §3: "I_(a,R) = I_inv − v Q … δI_(a,R) = P δa − (ε/4) a² v δR, with no further term because Q has no v-dependence at fixed (a, R)".

**Flaw.** δ(−vQ) = −Q δv − v(∂Q/∂a) δa − v(∂Q/∂R) δR = −Q δv − (ε/2)aRv δa − (ε/4)a²v δR, so δI_(a,R) = [P − (ε/2)aRv] δa − (ε/4)a²v δR. The a-momentum at fixed R is P − (ε/2)aRv, not P. Nothing downstream uses it, but "no further term" is wrong and the Ostrogradsky bookkeeping of the (a,R) problem — which J-7b's lapse integral needs — is incomplete.

**Severity: minor.**

## 11. §10 rigor labels — "Rigorous given 1" for the wavefunction relation, and "Rigorous (numerical)" for a contour-dependent saddle evaluation

**Claim attacked.** Rigor table: "I_(a,R) = I_inv − (ε/4)a²Rv; canonical and Laplace relations; identification with the F(R) GHY term — Rigorous given the previous row"; "Ψ_T(4,12) ∝ e^{+9.45a} — Rigorous (numerical) on the scanned family"; "Conical initial data: log coefficient, sign, consequence for the two signs — Rigorous".

**Flaw.** The Legendre relation and the DH identification are rigorous (verified below). The *Laplace* relation between wavefunctions assumes a semiclassical kernel, a regular-cap saddle sum for Ψ(a,v) (whose off-shell completion J-6 §1.8 says is missing), and a contour the note admits it does not supply — Sketch under METHODOLOGY's definitions, not Rigorous. "Ψ_T ∝ e^{+9.45a}" is a one-saddle evaluation (flaw 4) on a non-canonical contour (flaw 5) — Conjecture-grade. The cone row's "consequence for the two signs" is false (flaw 1). METHODOLOGY: "An agent must never claim a result is proven when it has only been sketched."

**Severity: minor** (labelling), but three rows.

## 12. §5 item 2 — the Picard–Lefschetz reading omits the consequence of "the real line is its anti-thimble"

**Claim attacked.** §5 item 2: "The recontracting cap is a minimum of E_HH along the real line … Its steepest-descent contour for e^{−I} is transverse to the real axis; the real line is its anti-thimble. Whether the sphere's thimble … is reached from any admissible contour is precisely the relevance question."

**Flaw.** In Picard–Lefschetz the intersection number of a saddle with the defining contour is that of its *anti-thimble* (upward flow) with the contour. A saddle whose anti-thimble *is* the contour has n = ±1: it is maximally relevant. So on the real-v line the recontracting cap is relevant under both signs (under e^{−I} because the real line is its anti-thimble; under e^{+I} because it is its thimble); the difference between the signs on that contour is convergence, not relevance. The note's sentence reads as if transversality of the thimble were evidence against the cap; it is the opposite. The second-derivative sign (d²E_HH/dv² = −ε dR/dv > 0) is correct and confirmed by the table (R rises from 5.0 to 24.7 as v falls from −0.22 to −7.5).

**Severity: minor** (a reading, not a number; but it is the reading J-7b is told to extend).

## 13. §2 — the Hamilton–Jacobi table's 0.4 % entries are a step-size artifact the note left standing, and "10⁻⁸ on the smooth displacements" describes the less informative direction

**Claim attacked.** §0 item 1: "Verified by Hamilton–Jacobi … to 10⁻⁸ relative on the smooth displacements"; §2 table row 2 (Q numerical 12.05 vs 11.99994; P −17.90 vs −17.759) with the explanation "the coarser δc₃ step on the steepest part of the family".

**Evidence.** `atk_hj_fine.out`: with dc₃ = 10⁻⁴ the displacement is da = 0.097 (5 % of a) and dv = 0.22; at dc₃ = 10⁻⁵, 10⁻⁶, 10⁻⁷ the solved (P, Q) converge to (−17.760479, 12.000460), (−17.759054, 11.999946), (−17.759040, 11.999941) against theory (−17.759043, 11.999942). The same at the ε = 0.3 cap (3.599992 vs 3.599992) and the expanding-side point. A mixed displacement (dc₃ = 10⁻⁶ with δτ₁ = 10⁻⁴) agrees to 1.5 × 10⁻⁹. So the explanation is right and the discrepancy is gone at the proper step — the note should have run it. On the wording: the δτ₁ displacement moves along the solution, where dI/dτ₁ = L = Pv + Qa″ − H by the Ostrogradsky identity; it therefore tests H = 0 and I_inv − I_ESU = F(v) along the cap, but by itself cannot separate P from Q. The direction that pins (P, Q) is δc₃, whose precision in the note's table is 10⁻⁵–10⁻³, not 10⁻⁸.

**Severity: cosmetic** (the result is confirmed to 10⁻⁶ by this pass).

## 14. §2 — the analytic identification: checked independently, no flaw; the "Sketch" label is conservative

**Checked.** In σ(θ) variables on [0, π/2]: a = e^σ sinθ, v = σ_θ sinθ + cosθ, aa″ = sinθ(σ_θθ sinθ + σ_θ cosθ − sinθ), so ∂(aa″)/∂σ_θθ = sin²θ and the local Lagrangian's momentum conjugate to σ_θ is p_v sinθ → p_v at θ = π/2 (the lead's "is d(aa″)/dσ_θθ = sinθ?" — it is sin²θ for aa″ and sinθ for the momentum after the dτ = e^σ dθ Jacobian; the note's sentence is right about the momentum). R² term: ∂/∂a″[−(3ε/4)(1−aa″−v²)²/a] = (3ε/2)(1−aa″−v²) = (ε/4)a²R (the 3ε/(3ε+1) rescaling removes the "+1" exactly). KS: ∂/∂σ_θθ[(1/8)sin³θ·8σ_θθσ_θ²] = sin³θ σ_θ² → v²; HHJ: ∂(−σ_θ³/3)/∂σ_θ = −v²; cancel. The a-momentum: p_σ^{KS} = ∂L/∂σ_θ − d/dθ(∂L/∂σ_θθ) = 3v − v³ at π/2; adding the local p_a with the (3ε) coefficient and comparing with p_a^{ESU} (local with (3ε+1) plus the ESU anomaly's 2v/a − (va″ + aa‴)/2) gives p_a^{ESU} − p_a^{inv} = 0 identically, off-shell. So P = p_a^{ESU} and Q = (ε/4)a²R are the Ostrogradsky momenta of I_inv as a functional, not merely on-shell; the frame constant C* does not enter because the gauge θ(cut) = π/2 makes the map cap ↦ σ(θ) on the fixed interval a bijection (backward integration of dθ/dτ = sinθ/a from any C reaches θ = 0 at the pole), and the pole terms vanish (σ_θ(0) = 0, densities ∝ sin³θ; local p_a^{loc} = O(τ)). Frame independence of Γ_KS + HHJ is a cocycle identity, hence off-shell. **No flaw.** The HJ check is not circular: the 2×2 solve returns the numerical gradient of a given function on the two-parameter family, and its agreement with a closed-form (P, Q) evaluated from (a, v, a″, a‴) at the cut is non-trivial.

## 15. §3 — the DH boundary term, sign and normalization: checked independently, no flaw

**Checked.** Legendre direction: for δI = Q δv the function stationary at fixed Q is I − vQ; δ(I − vQ) = −v δQ. Correct as written. Minisuperspace check of the GHY structure in this signature and orientation: ∫√g R = −12π²∫(a²a″ + av² − a)dτ = −12π²[a²v] + 12π²∫(av² + a); 2∮√h K with K = 3v/a (outward normal ∂_τ) gives +12π²a²v; sum = 12π²∫(a + av²) — the first-order form, so the "+2∮√h K" sign convention holds in Euclidean minisuperspace and I_EH = −(1/16πG)(…) matches ccaps' −(3/4)a(1+v²) per a. R² piece: p_v = ∂/∂a″[2π²βa³R²] = −24π²βa²R = (ε/4)a²R with β = −ε/(96π²); and 2∮√h F′_{R²}K = 4β·2π²a³R·3v/a = 24π²βa²Rv = −(ε/4)a²Rv = −vQ. Consistent. DH's Euclidean form (their §7: S_E + S_0 = −∫√g F(R) − 2∮√h F′(R)K) flips bulk and boundary together, so the relative sign transfers. Passages verified verbatim in `dh09.txt`: eq. (5.16); "the variation of the four-dimensional Ricci scalar be held fixed on the boundary. This corresponds to holding the scalar field fixed in the equivalent scalar-tensor theory" (l. 102–104); "there is in general no such boundary term with this property [18] … R now carries the scalar degree of freedom, so we must set δR = 0 on the boundary as well" (l. 1499–1502). Polarity: DH argue *for* the (h,R) Dirichlet problem with this term and against the δg-only view; the note's use is on their side. Conventions: mostly-plus, outward normal (l. 126–129). **No flaw.**

## 16. §7 — scheme independence of the cone coefficient is asserted by omission; it holds, but the note computes in a scheme that is not I_inv

**Claim attacked.** §7: the coefficient is computed with `ostro.py`'s ESU/Riegert Lagrangian (R² coefficient (3ε+1), anomaly 2σ_ηη² + 8σ_η² + 8), which is the J-1 scheme, not the invariant one; the rigor row calls it Rigorous for "the off-shell construction" of I_inv.

**Evidence.** `atk_cone.out` (2): the KS a-anomaly functional on the unit-S⁴ reference (the anomaly sector of I_inv, `dens10`'s GKS) on the cone a = vτ, with tan(θ/2) = Kτ^{1/v}, has log coefficient −(v−1)³(v+3)/(4v) — identical to the anomaly-sector part of the note's coefficient, (v−1)²/v − (v²−1)²/(4v). ESU-anomaly − (1/288π²)∫R² − KS = 2 = the ESU regular-pole divergence c(1) that the note subtracts. So the coefficient is scheme-independent after the subtraction, and the note's number is I_inv's. Not a flaw in the result; a gap in the argument that the steelman can close with this line.

**Severity: minor.**

## 17. §4 / §9 — "withdrawn at late times" and "confined to a corner" understate what survives at the junction data

**Claim attacked.** §9 H bullet: "Steelman H's strongest objection … is withdrawn at late times and confined to ε < 0.33, q < q*(ε) ≤ 9.5"; §0 item 3: "everywhere else the sphere is lower".

**Flaw.** The crossover ε* = 0.330 lies *inside* H's window (1/4, 0.355): for 0.25 < ε < 0.33, at the note's own test data (4,12) — one Hubble time after the junction — the cap is still lower by up to 0.61a, which the note's order-of-magnitude line calls decisive (e^{6×10⁵} at a₂ = 10⁶). Steelman H's item 5 claimed dominance "at every large three-sphere"; the note refutes that (q > q*), which is a fair "at late times". But the summary's "for every ε in H's window and above it" hides the q-condition, and "confined to a corner" describes most of the window at the data every J-6 table used. Also the extrapolation "q grows without bound, so at late times the sphere is the lowest" rests on four points in q at ε = 1 and 0.3 (the Newton lost the cap at q = 16 and 25 respectively, `ar_table.out`).

**Severity: minor** (framing; the numbers are honest).

## 18. §0 / §1 — minor factual and cross-reference slips

- §0 item 5: "sixth-highest under e^{+I}" — seventh (flaw 8b).
- §4 table: "see §6 note" at ε = 0.70 — no such note exists (flaw 7).
- Units paragraph: "the universal constant −(1/288π²)∫√g R²|_{S⁴} = −4/3 (ε = 1)" — the constant is ε-independent (144 × 8π²/3 ÷ 288π² = 4/3); the qualifier is spurious. The hemisphere value 2/3 is what makes I_inv(sphere) = −(1 + 2ε) from −(5/3 + 2ε).
- §11: "the attribution of the specific boundary functional used here to their eq. (126) is steelman H's and is not re-verified" — honest, but the whole of Result 1 rests on that boundary term's −σ_θ³/3 coefficient; a re-verification of HHJ (126)'s (8/3)τ_n³ coefficient and sign was cheap and was not done.

**Severity: cosmetic.**

## 19. Hidden-assumption check (METHODOLOGY stress-test requirement)

- **Time evolution / preferred foliation:** the imaginary-v contour fixes a real Lorentzian expansion rate at the cut; this is a boundary datum, not a bulk foliation, and minisuperspace already fixes the slicing. No new smuggling — but it *is* a choice that privileges the Lorentzian real section of the Ostrogradsky configuration space, and the note calls it an inheritance (flaw 5c).
- **Background structure:** the unit-S⁴ reference drops out of I_inv up to a constant (J-6 §1.7); the cone computation in the S⁴ frame confirms it for singular poles too (flaw 16). Clean.
- **Preferred observer:** none introduced.
- **Sign selection:** the note says "Nothing here selects a sign"; flaw 1 shows it briefly did, in §7, and wrongly.

## 20. Attack lines that failed (recorded so the steelman need not re-run them)

- **Other real caps at a = 2.** `atk_family.out` (a): every cap with −1/6 < c₃ < 0 that recontracts through a = 2 ends at an irregular pole (a → 0 at τ = 4.1–8.4) with no neck and no third crossing, at ε = 1 and 0.3. (b): neck-class caps c₃ = −0.2 … −5 never reach a = 2 (a_max ≤ 1.13) at either ε. Within c₃ ∈ (−5, 2] the real a = 2 family is exactly the note's, joined once at v = 0; the join is C¹ (dI_inv/dv = Q continuous). "E_HH → +∞ at both ends" is a monotone extrapolation, as the note says.
- **The (q,R) problem as H posed it.** Position H (line 117) explicitly names "the (q, R) choice with its Legendre boundary term"; steelman H's (4,12) table used I_inv without it and J-6 §1.4/§9 flagged the check as pending. The note is a correction of H's number inside H's own problem, not a change of problem. The constant-lapse (sheet) criterion is a property of the (c₃, τ₁) solution and is orthogonal to the boundary term; the recontracting cap passes it in `lapse_path.out`.
- **Fursaev–Solodukhin.** Quoted passage verbatim at `fs95.txt` l. 77–79; (2.31)–(2.33) with divergent Y(α) and regularization-dependent I₂(α) at l. 777–779. Used as analogy only, as stated.
- **ε*, q*, the (q,R) tables, the E_HH tables:** reproduce from `ar_table.out`, `qcross.out`, `vfamily.out`, `vfine.out`.

---

### Severity summary

| # | Section | Flaw | Severity |
|---|---|---|---|
| 1 | §7, §0.6, README | tunneling sign is not protected against cones for ε < 1 (needles have I → +∞) | serious |
| 2 | §7 | "regular-pole restriction" does not rescue e^{−I}; the diverging family is regular at the pole | serious |
| 3 | §5.1 | contracting-side divergence attributed to the boundary term; it is the R² runaway, boundary term opposes it | minor–serious |
| 4 | §5.3, §9 | single-saddle truncation of Ψ(a,v) behind "Ψ_T ∝ e^{+9.45a}" | serious |
| 5 | §5, §8, §9, §0.4 | real-v line called "natural", imaginary-v line an "adaptation"; canonically reversed; obstruction overstated; "inherits the contour" false | serious |
| 6 | §8, §4 | P_R ≠ 0 at flat balls; the R-marginal's saddles are v = 0 cuts; (a,R) on-shell action bounded below on the real family | serious |
| 7 | §4, §0.3 | "lowest of the known saddles" conditional on a Sketch-level exclusion; pair continuation failed silently | serious / cosmetic |
| 8 | §6, §0.5 | census values path/sheet-dependent, no constant-lapse test; "sixth-highest" is seventh | serious / cosmetic |
| 9 | §3 | Laplace kernel sign reversed (typo vs §5) | minor |
| 10 | §3 | a-momentum of the (a,R) problem misstated | minor |
| 11 | §10 | three rigor labels too high | minor |
| 12 | §5.2 | PL reading omits that anti-thimble = contour means relevant | minor |
| 13 | §2 | 0.4 % table entries were a step artifact (now confirmed to 10⁻⁶); "10⁻⁸" wording | cosmetic |
| 14 | §2 | analytic identification — no flaw (independently derived, off-shell) | — |
| 15 | §3 | DH term, sign, normalization, polarity — no flaw | — |
| 16 | §7 | scheme independence not shown (it holds) | minor |
| 17 | §4, §9 | "withdrawn / corner" understates what survives in most of the window at the junction data | minor |
| 18 | various | cross-reference and count slips | cosmetic |
