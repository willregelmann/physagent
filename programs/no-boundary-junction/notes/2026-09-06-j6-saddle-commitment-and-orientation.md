# J-6: the saddle commitment, and what orientation the junction actually supplies

**Date:** 2026-09-06
**Milestone:** J-6 of `programs/no-boundary-junction/OBJECTIVES.md` (#215 step 3), made load-bearing by J-1: the bound on the □R coefficient rests on which saddles the no-boundary state sums over and with which sign. Standing assumption: conformal field content with a₂ ≥ 10⁶, an explicit input.
**Role:** interactive session, experimenter-directed. Exploration note; exploratory-tier citations with how-checked stated inline. No new numerics beyond J-1's; the content is a structured commitment with its consequences named.

---

## Summary

1. **Two prescriptions, two orderings.** The two real caps of J-1 (the round S⁴ and the symmetric double bubble, actions I_S⁴ = −a(5 + 4ε) and I_DB ≈ I_S⁴ − a(4ε + 2.6) for ε > ε_c ≈ 0.355) enter the no-boundary state with weight e^{−I} under the Hartle–Hawking sign and e^{+I} under the tunneling sign. Under the first the double bubble dominates above ε_c (J-1); under the second the sphere dominates at every ε, by the same factor inverted. The two published definitions of the state realize exactly these two signs: the real-lapse Lorentzian path integral evaluated by Picard–Lefschetz theory picks the tunneling sign and comes with unsuppressed tensor perturbations, a problem Feldbrugge–Lehners–Turok show is generic for adiabatic matter, not a feature of the Einstein–Λ action; Di Tucci–Lehners's Robin boundary term restores the Hartle–Hawking sign by redefining the sum as geometries of approximately zero initial size with Euclidean initial momentum. *(Sketch; each step verbatim-sourced below.)*
2. **The Robin prescription admits both caps.** Its condition fixes the Euclidean momentum at the pole, which in our variables is pole regularity a′(0) = 1; both caps satisfy it identically, and the shooting parameter c₃ that distinguishes them is invisible to it. So under the Robin definition both caps contribute with the Hartle–Hawking sign, and J-1's ordering stands. *(Sketch, from the pole series of J-1 §1.2 and Di Tucci–Lehners's condition.)*
3. **Commitment (recommended; the experimenter accepts or amends at merge): the Hartle–Hawking sign, implemented by the Robin / Euclidean-momentum definition.** It is the only definition compatible with the reframing's premise that the root is the state of minimum excitation, and it is the definition under which the no-boundary state is a well-defined sum over stable saddles. Consequence, inherited from J-1 in full: the sphere is the unique dominant root iff 0 < ε < ε_c, the scalaron is heavier than ≈ 1.7 H₀, and the root's de Sitter depth is ≈ 5–7 e-folds. Adopting the tunneling sign instead would rescue the sphere's dominance at the cost of the premise and of semiclassical control of perturbations; restricting the sum to the sphere by fiat (which is what the trace-anomaly-inflation literature does in practice) is a choice the program declines to make silently. *(Judgment.)*
4. **Orientation: the junction supplies a time orientation, not an arrow, and not one the tree adds.** Root-ward on a Lorentzian branch is the causal past with Σ as initial boundary — timelike curves end on Σ with no timelike continuation (signature-change-boundary, Rigorous given the fixed background) — a foliation-free partial order on events that survives recollapse. The minisuperspace order "decreasing conformal factor" is withdrawn (foliation-dependent; fails at turnaround). The record arrow is a separate, state-dependent fact: Hawking 1985 claimed it points away from the low-excitation end and reverses at recollapse; Page 1985 disputed and Hawking–Laflamme–Lyons 1993 retracted the reversal; what survives is an arrow that points away from the low-excitation end throughout. The rooted-tree combinatorics re-expresses these two facts and derives neither (the #216 finding). *(Sketch by citation, as in #216 §6d.)*
5. **Root uniqueness, clarified.** The tree argument needs each history to have one root, which every real junction supplies; it does not need the state to have one cap. Two caps give a superposition of two trees at different 3-geometries (radius 1 versus a_neck < 0.8), each with its own orientation and no interference between them. What multiplicity does is decide which tree is probable — and under the committed sign above ε_c that is the double bubble's, whose history recollapses in under a Hubble time and carries no records at all. So "root uniqueness" in the experimenter's sense is a statement about dominance, and J-1 is its content.

---

## 1. The two signs and the two caps

Write the no-boundary amplitude for a real junction as a sum over the regular caps that reach it, each weighted by exp(∓I_half) with I_half = I/2 for a reflection-symmetric cap. J-1 established (Rigorous (numerical), minisuperspace):

| ε | I_S⁴/a | I_DB/a | HH sign: (I_DB − I_S⁴)/a, negative ⇒ DB dominates | tunneling sign: sphere dominates by e^{+…a} |
|---|---|---|---|---|
| 0.36 | −6.44 | −9.15 | −2.71 | 2.71 |
| 1 | −9 | −15.15 | −6.15 | 6.15 |
| 5 | −25 | −47.59 | −22.59 | 22.59 |
| 10 | −45 | −87.64 | −42.64 | 42.64 |

With a = a₂/180 ≥ 5.6 × 10³ every entry is an exponent of order 10⁴ or more: whichever sign is adopted decides the dominant cap absolutely. The question is therefore not numerical but definitional, and the two definitions on record give opposite answers.

### 1.1 The real-lapse Lorentzian definition (tunneling sign)

Feldbrugge, Lehners and Turok integrate the minisuperspace action over real lapse N ∈ (0, ∞) and evaluate by Picard–Lefschetz theory. For Einstein–Λ with q = a², the action after integrating out q is S⁽⁰⁾[q₁; 0, N] = 2π²(N³Λ²/36 + N(3 − Λq₁/2) − 3q₁²/(4N)); the relevant saddle is N_s = (3/Λ)(i + √(Λq₁/3 − 1)), and the weighting is "e^{−12π²/Λ − i4π²√(Λ/3)(q₁ − 3/Λ)^{3/2}}", i.e. the suppression Vilenkin proposed, inverting Hartle–Hawking's e^{+12π²/Λ}. The tensor-mode propagator is then "an inverse Gaussian distribution": large perturbations are favored. And the authors show "the problem of unbounded perturbations, at small wavelengths, is unavoidable" for "a fluid more general than a cosmological constant" satisfying an adiabatic equation of state, "using the Friedmann constraint rather than specific action forms." (All quotations from the ar5iv rendering, **verified this session**; the paper's existence and abstract were verified in the #216 cycle.)

Consequence for the two caps, at Sketch level: if the same contour rule applies to the saddles of the anomaly-plus-R² minisuperspace — an assumption, since the fourth-order action is not quadratic in q and its lapse integral has not been analyzed — both caps enter with e^{+I} and the sphere dominates by e^{(4ε + 2.6)a}. The bound of J-1 disappears, but the state is the tunneling one, and the minimum-excitation premise of the reframing is false for it by FLT's perturbation result.

### 1.2 The Robin / Euclidean-momentum definition (Hartle–Hawking sign)

Di Tucci and Lehners add a boundary term at the initial surface, "S_tot = S + αq₀ + q₀²/(2β)", so that the condition there is "ℬ ≡ (3π²/N)q̇₀ + α + q₀/β = 0", coupling initial size and initial momentum. "For α = −6π²i" the saddle geometries start at zero size — "requiring that at least one of the saddle point geometry starts out at zero size corresponds to a specific value of α" — and for sufficiently large negative-imaginary β "the Hartle-Hawking saddle point becomes the only relevant one," giving "G[q₁, 0]_Robin = e^{+4π²/(H²ℏ) − i4π²H/ℏ(q₁ − 1/H²)^{3/2}}": the positive Hartle–Hawking exponent, and "the path integral … are approximated by stable Hartle-Hawking saddle point geometries." The interpretation is "an initial coherent state, albeit one with a Euclidean momentum α", with "Δq₀ = √|β| ∼ 1/H, Δp₀ = ℏ/√|β| ∼ ℏH", and the authors are explicit that "the present implementation of the no-boundary proposal effectively corresponds to a redefinition … the sum is redefined to be over geometries with approximately zero initial size and approximately Euclidean initial momentum." No extension beyond Einstein–Λ is discussed. (Quotations from the ar5iv rendering, **verified this session**.)

**Both caps satisfy the redefined condition.** In our variables (J-1 §1.2) every regular cap has a = τ + c₃τ³ + …, i.e. q = a² = τ² + 2c₃τ⁴ + …. In the gauge ds² = N²dt²/q + q dΩ₃² used by Di Tucci–Lehners, proper distance from the pole is τ = ∫N dt/√q, so q ≈ Nt near the pole and dq/dt → N: a finite Euclidean momentum at zero size, fixed by a′(0) = 1 alone. The shooting parameter c₃, which separates the sphere (c₃ = −1/6) from the double bubble (c₃ ≈ −0.35), enters q only at order τ⁴ and is invisible to the Robin condition. So under the Robin definition the sum includes both caps with the Hartle–Hawking sign, and J-1's ordering holds: the double bubble dominates for ε > ε_c. *(Sketch: this transcribes the Robin condition to our variables; a Picard–Lefschetz analysis of the fourth-order lapse integral with the Robin term — which would also settle whether further complex saddles compete — is the open computation, §4.)*

## 2. The commitment

The program's root premise (README, scope; the experimenter's tree argument) is that the Euclidean cap is the state of minimum excitation. That premise selects the Hartle–Hawking sign, and among the definitions on record only the Robin / Euclidean-momentum definition delivers that sign from a path integral with stable saddles. **Recommended commitment: the Hartle–Hawking sign via the Robin definition**, with the following stated consequences:

- J-1's bound is in force: the sphere is the unique dominant real root iff 0 < ε < ε_c ≈ 0.355, i.e. the scalaron mass exceeds ≈ 1.7 H₀, i.e. |β_tot| ≲ 25 at a₂ = 10⁶; the root's de Sitter depth is ≈ 5–7 e-folds.
- Above ε_c the no-boundary state is dominated by a cap whose real history is a closed universe that recollapses within a Hubble time. The sphere is a subdominant saddle there; using it anyway is the trace-anomaly-inflation literature's practice (Hawking–Hertog–Reall: "we shall not have much to say about the new instanton"), and this program records it as a choice it does not make.
- The reframing's own aims — a derived reflection surface (J-3, J-4), WKB time on the branches (J-5), a causal orientation (§3) — do not need a long inflationary root and are unaffected. What the commitment removes is the option of reading the anomaly root as the origin of sixty e-folds of inflation within the no-boundary state.

The alternative commitment (tunneling sign) is recorded, not adopted: it restores the sphere's dominance at every ε and forfeits the minimum-excitation premise and semiclassical control of perturbations.

## 3. Orientation, records, and root uniqueness

**Orientation (Sketch, on Rigorous fixed-background input).** On each Lorentzian branch, take Σ as the initial boundary. The signature-change-boundary program established, for the fixed background, that timelike geodesics reach Σ at finite proper time with no timelike continuation, while spacelike curves cross (Rigorous given the fixed background; the crossing-as-geodesic step is Sketch). "Root-ward" is then the causal past: x ≼ y iff x lies in the causal past of y, with Σ the set of minimal elements. This is a partial order on events, defined without a foliation, invariant under the ℤ₂ that exchanges the two WKB branches of the conjugate saddle pair (which flips the sign of the WKB phase, not the causal structure), and unaffected by recollapse. It is a time *orientation*. The minisuperspace version — order by decreasing conformal factor — is withdrawn: it presupposes a slicing and stops being an order at turnaround, and the framework's post-decay branch is closed and Λ-free (#216 §6d).

**Records (Sketch, by citation; verified in the #216 cycle).** Hartle–Hawking 1983 says nothing about records. Hawking 1985 argued the thermodynamic arrow in the no-boundary state points away from the low-excitation end and reverses at maximum expansion; Page 1985 disputed the reversal; Hawking–Laflamme–Lyons 1993 retracted it ("contrary to an earlier claim, the density perturbations do not get small again at the other end"). What stands: the record arrow points away from the low-excitation end and does not reverse. "Root" in the experimenter's sense is that end. This is a property of the state, not of the tree.

**What the tree adds (nothing beyond re-expression).** A rooted tree's partial order is the causal order read on decohered histories; its root is the junction; "records point root-ward" is the surviving Hawking–Laflamme–Lyons statement. The tree derives neither. The #216 finding stands: the tree argument re-expresses the branch's causal structure and the state's record arrow; it does not supply an orientation of its own. Acyclicity (no recoherence) remains a hypothesis.

**Root uniqueness, clarified.** Each real junction roots one tree. Two caps give two trees at different 3-geometries (radius 1 and a_neck < 0.8), which do not interfere; orientation is well defined within each. Uniqueness is therefore not what orientation needs. It is what *probability* needs: the dominant cap decides which tree the no-boundary measure favors, and under the committed sign that is the double bubble's above ε_c — a history too short to contain records, so the record arrow has nothing to act on there. Below ε_c the sphere's tree is unique and dominant, with a short but ordinary inflating branch.

## 4. What this note does not do (open computations, named)

1. **Picard–Lefschetz analysis of the fourth-order minisuperspace.** The lapse integral for the anomaly-plus-R² action (J-1 §3.1) with and without the Robin term: which complex saddles exist beyond the two real caps, which thimbles the contour picks, and whether the double bubble's thimble is relevant. This is the computation that would replace §1's transcription by a result. It is well posed and finite in minisuperspace; it has not been done here or, to this program's knowledge, in the literature (FLT's generalization covers adiabatic fluids, not higher-derivative gravity).
2. **Perturbations around the double bubble.** Hawking–Hertog–Reall did not analyze them ("the lack of an analytical solution makes dealing with perturbations of this instanton rather difficult"); whether the double bubble is a stable saddle in the Robin sense is untested.
3. **The record arrow on a branch of depth 5–7 e-folds.** Whether Hawking–Laflamme–Lyons's non-reversal survives a root this shallow, with reheating within a few Hubble times, is not addressed.

## 5. Consequences for the program

- **J-6 done-condition:** met as "documents that the tree re-expresses the orientation" (the negative branch of the done-condition) plus the saddle commitment, with its consequences inherited from J-1.
- **J-1's bound is final relative to the program's commitment**, and provisional relative to open computation 1.
- **J-3 (junction selection beyond regularity):** the reflection-symmetric points are now known to be exactly two for ε > ε_c and one below; what selects among the great S³'s of a given cap is still the branch, not the cap (unchanged from #216 §6d).
- **Upstream note for `fixed-point-existence`:** the anomaly-plus-R² Euclidean sector's two-instanton structure and its sign dependence should be recorded when that program next touches the Starobinsky section (J-2-style small PR).

## Self-checks

- **Consistency:** every quantitative statement is J-1's, unchanged; the sign dichotomy is pure bookkeeping on e^{∓I}; the FLT and DTL quotations are verbatim from the ar5iv renderings and match the polarities recorded in the #216 cycle.
- **Limiting cases:** ε < ε_c: one cap, both prescriptions agree on the sphere ✓; ε → 0: family degenerates to the sphere ✓; ε < 0: no exit, no competitor ✓.
- **Hidden assumptions:** the Robin condition transcribed at leading order in τ (disclosed; the fourth-order lapse integral is open computation 1); the causal order uses the fixed-background crossing result (disclosed); no evolution parameter is introduced — orientation is a partial order on events, the record arrow a property of the state.

## References (exploratory tier; how checked)

- J. Feldbrugge, J.-L. Lehners, N. Turok, "No smooth beginning for spacetime," PRL 119, 171301 (2017), arXiv:1705.00192 — action, saddle, weighting, inverse-Gaussian tensor propagator, and the adiabatic-fluid generalization quoted from the ar5iv rendering this session; existence and polarity verified in the #216 cycle.
- A. Di Tucci, J.-L. Lehners, "No-boundary proposal as a path integral with Robin boundary conditions," PRL 122, 201302 (2019), arXiv:1903.06757 — Robin term, α = −6π²i, the relevant-saddle statement, the propagator with positive exponent, the coherent-state interpretation and the "redefinition" sentence quoted from the ar5iv rendering this session; existence and polarity verified in the #216 cycle.
- J.-L. Lehners, "Review of the no-boundary wave function," Phys. Rep. 1022, 1 (2023), arXiv:2303.08802 — Picard–Lefschetz saddle structure and dominance rule (Sec. 2.2) read this session; the Robin section was not retrieved.
- S. W. Hawking, T. Hertog, H. S. Reall, PRD 63, 083504 (2001) — "we shall not have much to say about the new instanton" and the perturbation remark, verified this session (J-1).
- S. W. Hawking, PRD 32, 2489 (1985); D. N. Page, PRD 32, 2496 (1985); S. W. Hawking, R. Laflamme, G. W. Lyons, PRD 47, 5342 (1993) — verified with polarity in the #216 cycle (attack pass on attempt C).
- `programs/signature-change-boundary/notes/2026-06-05-fixed-background-note.md` — the crossing asymmetry (repo-internal).
