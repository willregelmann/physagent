# CE-4: Does the two-loop β_ξ shift the conformal fixed point?

**Date:** 2026-06-24
**Type:** Research exploration (literature verdict + structural argument)
**Issue:** #30 (CE-4)
**Paper anchor:** `programs/co-emergence/index.tex`, Remark 9 (`rem:xi_running`),
eq. (`eq:beta_xi`); bears on Conjecture 2 (`conj:mass_generation`).
**Outcome:** Conditional positive for the "fixed point shifts" branch. The
conformal value of the non-minimal coupling is **not** an all-orders RG fixed
point and is **not** protected by any unbroken symmetry. Every explicit
higher-loop curved-space calculation that exists (all for *pure* λφ⁴) shows the
conformal value failing to be preserved beyond one loop. **But** (i) no
two-loop β_ξ has been published for the Standard Model or any gauge–Yukawa
theory, and (ii) in the massless theory the breaking is partly
renormalization-scheme-dependent. The honest verdict is therefore **Sketch**,
not Rigorous: the *generic-expectation* half of Remark 9's dichotomy is now
backed by explicit calculation and a symmetry argument, but the
SM-specific "inaccessible" conclusion cannot be asserted at Rigorous level.

---

## 1. The question

The co-emergence mass-generation argument (Remark 9, Conjecture 2) turns on
whether conformal coupling $\xi = 1/6$ — where a scalar acquires no
curvature-induced effective mass, $m_{\mathrm{eff}}^2 = (\xi - 1/6)R = 0$ — is a
fine-tunable point or a dynamically inaccessible one. At one loop the Standard
Model β-function is~[Markkanen et al.]

$$16\pi^2\,\beta_\xi = \left(\xi - \tfrac16\right)\!\left[12\lambda + 2Y_2 - \tfrac32 g'^2 - \tfrac92 g^2\right],$$

proportional to $(\xi - 1/6)$ in its entirety, so $\xi = 1/6$ is an exact
one-loop fixed point. Remark 9 states a dichotomy:

- **If the fixed point shifts at two loops** ($\beta_\xi$ acquires a term that
  does not vanish at $\xi = 1/6$), then $\xi = 1/6$ is *inaccessible* and mass
  generation follows with no assumption about field content.
- **If it persists to all orders**, then $\xi = 1/6$ is a measure-zero point
  requiring a naturality argument to exclude.

CE-4 asks for a literature verdict (verified citations) plus a structural
argument, and the consequence for Conjecture 2 either way.

## 2. Literature verdict

**There is no published two-loop β_ξ for the Standard Model, or for any
realistic gauge–Yukawa–scalar theory, in curved spacetime.** Remark 9's
statement to that effect is correct and is confirmed by an exhaustive
non-discovery across the curved-space RG literature (Buchbinder–Odintsov–Shapiro
school, Hathrell line, the recent heat-kernel multiloop work). What exists at
two loops is restricted to **pure single-scalar λφ⁴**.

**For pure λφ⁴, the conformal value is not preserved beyond one loop.** Three
mutually consistent statements:

1. **Explicit two-loop β_ξ (Carneiro & von Gersdorff 2024, their eq. (40)):**
   with $\ell \equiv \lambda/(16\pi^2)$ and their sign convention (conformal
   point at the zero of the one-loop term),
   $$\beta_\xi = \left(\tfrac16 + \xi\right)\ell - \left(\tfrac{7}{36} + \tfrac{5}{6}\xi\right)\ell^2.$$
   The one-loop term vanishes at the conformal value; **the two-loop term does
   not**. Evaluating explicitly at their conformal point $\xi = -1/6$:
   $$\beta_\xi\big|_{\xi=-1/6} = 0 - \left(\tfrac{7}{36} - \tfrac{5}{36}\right)\ell^2 = -\tfrac{1}{18}\,\ell^2,$$
   a nonzero residual with coefficient $1/18 \approx 0.056$. (Convention caveat:
   this paper writes the curvature coupling with the opposite sign of `index.tex`,
   so its conformal zero is at $\xi = -1/6$; the load-bearing,
   convention-independent fact is that the $O(\ell^2)$ piece is nonzero at the
   conformal point. The authors state agreement with Brown & Collins.)

2. **Structural form (Odintsov 1993; Brown & Collins 1980):** the curved-space
   β_ξ has the general structure
   $$\beta_\xi = \left(\xi - \tfrac16\right)\gamma + \Delta\beta_\xi,$$
   where $\Delta\beta_\xi$ is **independent of $\xi$** and **first appears at
   two loops**. Brown & Collins originally showed that $\xi$ obeys an
   *inhomogeneous* RG equation — an additive, coupling-driven source term — which
   is exactly what a strictly "$(\xi-1/6)$-only" β_ξ would forbid.

3. **NLO fixed-point statement (Martini & Zanusso 2019):** verbatim — using
   "naively the dimensionally regulated scheme at the next-to-leading order
   (NLO) and a straightforward subtraction … the above value [$\xi=1/6$] is
   *not* a fixed point to order $\epsilon$."

**Important scheme caveat.** Martini & Zanusso also note that "the freedom …
of redefining the potential $U(\phi,R)$ by a copy of the one-loop counterterms
can be exploited to ensure that [$\xi=1/6$] is the fixed point at NLO"
(crediting Jack). So in the *massless* conformal theory there *exists* a
renormalization scheme in which $\xi=1/6$ remains an NLO fixed point: the
breaking is not scheme-invariant there. The genuine, scheme-independent
breaking is associated with **mass-dependent (decoupling) schemes** — where the
clean $(\xi-1/6)$ factorization is a high-energy limit modified by factors
$\mu^2/(m^2+\mu^2)$ (Gorbar–Shapiro) — and with the explicit nonzero
conformal-point term above. The SM has masses, so the mass-dependent picture is
the physically relevant one.

## 3. Structural / symmetry argument

**There is no symmetry that forces $\beta_\xi \propto (\xi - 1/6)$ to all
orders.** The reasoning:

- The one-loop proportionality is a structural fact about the heat-kernel
  coefficient $a_2$ (the term $(\tfrac16 - \xi)R$ in the Seeley–DeWitt
  expansion), **not** an all-orders Ward identity. It is a one-loop accident in
  the same sense that many one-loop relations are.

- The candidate all-orders protector is **Weyl (conformal) invariance**:
  $\xi = 1/6$ is precisely the value making the *massless* classical action
  Weyl-invariant in $d=4$, so $(\xi - 1/6)$ is the order parameter for conformal
  breaking. If that symmetry were exact at the quantum level, it would force
  $(\xi-1/6)$ to renormalize multiplicatively and $\xi=1/6$ to be a fixed point
  to all orders.

- **But Weyl invariance is anomalous in four-dimensional curved spacetime.**
  The trace (conformal) anomaly breaks exactly this symmetry at the quantum
  level, so there is no exact Ward identity protecting the proportionality.
  This is why the naive NLO calculation finds $\xi=1/6$ is not a fixed point,
  and why restoring it requires a scheme choice rather than following
  automatically.

**This is internally consistent with — and sharpens — the framework's own
mechanism.** Remark 9 already observes that "the symmetry that would protect
$\xi = 1/6$ is the same symmetry whose breaking generates the curvature in the
first place." The literature now supplies the explicit content of that remark:
the conformal anomaly that drives the Starobinsky background $R = 12H_0^2$ is
the *same* anomaly that destabilizes $\xi = 1/6$. The framework's curvature
source and its $\xi$-destabilizer are one object. What was a naturality slogan
is now backed by (a) an explicit two-loop calculation in the tractable
(pure-scalar) case and (b) the anomaly argument for why no all-orders
protection can exist.

## 4. Consequence for Remark 9 and Conjecture 2

**Verdict on the dichotomy.** The structural and explicit-calculation evidence
points to the *first* branch — the conformal value is not an all-orders fixed
point. However, two honest qualifications keep this at **Sketch**, not
Rigorous, and forbid asserting "inaccessible" for the SM:

1. **Field content.** The only explicit higher-loop curved-space β_ξ is for
   pure λφ⁴. The SM (gauge + Yukawa) two-loop β_ξ is unpublished. Gauge and
   Yukawa couplings explicitly break conformal invariance and would, if
   anything, add further non-$(\xi-1/6)$ structure — but this is an expectation,
   not a computed result.

2. **Scheme dependence in the massless limit.** In the massless theory the NLO
   shift can be removed by a finite scheme redefinition (Jack; Martini–Zanusso).
   The scheme-independent breaking lives in the mass-dependent / decoupling
   description, which is the physically correct one for the SM but has not been
   pushed to an explicit two-loop SM β_ξ.

**Consequence for Conjecture 2 (`conj:mass_generation`).** Conjecture 2 is
**not** upgraded to a theorem by this work, and should remain a Conjecture. What
*is* strengthened is its weakest premise — that $\xi \neq 1/6$ is the generic
situation. Before this exploration, "generic" rested on a one-loop fixed-point
plus a naturality slogan. After it:

- The conformal value is *not* symmetry-protected (anomaly argument, Sketch).
- Every explicit higher-loop curved-space calculation that exists shows it
  shifting (pure λφ⁴, Rigorous *for that theory*).

So the "$\xi = 1/6$ is non-generic" claim moves from *naturality-only* to
*naturality plus explicit-calculation-in-the-tractable-case plus
symmetry-argument-for-no-protection*. The residual gap — an explicit two-loop
SM β_ξ — is exactly the calculation Remark 9 already flags as unpublished, and
nothing here closes it.

## 5. Recommended follow-up

A **paper-text PR** could sharpen Remark 9 to:

- cite the explicit pure-scalar two-loop result (Carneiro–von Gersdorff;
  Brown & Collins; Odintsov) for the statement that the conformal value is not
  preserved beyond one loop in the one theory where the calculation has been
  done;
- promote the existing "same symmetry" sentence into the explicit anomaly
  argument of §3, citing the Weyl-anomaly structure;
- keep, unchanged, the honest statement that the SM-specific two-loop β_ξ is
  unpublished and that the "inaccessible" branch is therefore not established.

That is a separate issue-and-PR cycle (new paper-grade citations → semantic
claim-support gate), per METHODOLOGY's rule that explorations set direction and
PRs establish paper results. This exploration does not itself edit `index.tex`.
The new bibliographic entries (Carneiro–von Gersdorff, Martini–Zanusso,
Brown & Collins, Odintsov, Hathrell) would need full paper-grade verification at
that point; their status as used here is recorded in §6.

## 6. Verified-citation list

Tiers per METHODOLOGY: this is an exploration, so references are exploratory
tier; verification status is recorded honestly for any later promotion to
paper-grade.

| Reference | Role here | Status |
|---|---|---|
| T. Markkanen, S. Nurmi, A. Rajantie, S. Stopyra, "The 1-loop effective potential for the Standard Model in curved spacetime," *JHEP* **06** (2018) 040, arXiv:1804.02020 | One-loop SM β_ξ (eq. `eq:beta_xi`) | **VERIFIED** (already paper-grade in `index.tex`; bib data + (ξ−1/6) structure confirmed) |
| I. Carneiro, G. von Gersdorff, "The Heat Kernel in Riemann Normal Coordinates and Multiloop Feynman Graphs in Curved Spacetime," arXiv:2408.04005 (2024) | Explicit two-loop β_ξ for pure λφ⁴ (their eq. 40), nonzero at conformal point | **VERIFIED** (title/authors + eq. 40 read from full text; journal-of-record JHEP **12** (2024) 140 reported but not independently re-confirmed) |
| R. Martini, O. Zanusso, "Renormalization of multicritical scalar models in curved space," *Eur. Phys. J. C* **79** (2019) 203, arXiv:1810.06395, DOI 10.1140/epjc/s10052-019-6721-8 | NLO: ξ=1/6 not a fixed point in naive DR; scheme freedom (Jack) restores it; conformal invariance anomalous | **VERIFIED** (bib data + verbatim quotes read from full text) |
| L. S. Brown, J. C. Collins, "Dimensional renormalization of scalar field theory in curved space-time," *Annals of Physics* **130** (1980) 215 | Original inhomogeneous RG equation for ξ | **PARTIAL** (title/journal/volume/pages confirmed via INSPIRE/ScienceDirect; inhomogeneous-RG content from secondary description, not direct read) |
| S. D. Odintsov, "Two-loop effective potential in quantum field theory in curved space-time," *Phys. Lett. B* **306** (1993) 233, arXiv:gr-qc/9302004 | Structural form β_ξ = (ξ−1/6)γ + Δβ_ξ, Δβ_ξ ξ-independent and first at two loops | **VERIFIED** (bib data from arXiv); content from abstract + secondary excerpts — **PARTIAL** at quote level |
| S. J. Hathrell, "Trace anomalies and λφ⁴ theory in curved space," *Annals of Physics* **139** (1982) 136 | All-orders trace-anomaly RG technology; natural home for an all-orders ξ statement | **PARTIAL** (bib data verified; full text inaccessible, internal claims not directly read) |
| E. V. Gorbar, I. L. Shapiro, "Renormalization Group and Decoupling in Curved Space" (II), arXiv:hep-ph/0303124 / JHEP line | Mass-dependent scheme: (ξ−1/6) factorization is a UV limit, modified by decoupling | **PARTIAL** (existence/topic verified; in-paper β_ξ text not directly read) |
| I. L. Shapiro, J. de Morais Teixeira, A. Wipf, "On the functional renormalization group for the scalar field on curved background with non-minimal interaction," *Eur. Phys. J. C* **75** (2015) 262, arXiv:1503.00874 | Non-perturbative FRG: ξ runs only weakly in pure scalar theory | **VERIFIED** (bib data); fixed-point characterization beyond abstract — **PARTIAL** |
| I. L. Buchbinder, S. D. Odintsov, I. L. Shapiro, *Effective Action in Quantum Gravity*, IOP Publishing (1992) | Standard monograph for curved-space ξ renormalization and the conformal anomaly | **PARTIAL** (book existence/authors/publisher/year verified; page-level claims not read) |

**Did not verify / corrected:** a "Jack & Parker" two-loop β_ξ paper (as named
in the issue's approach list) could not be located; the relevant curved-space
scalar background-field paper is **I. Jack, H. Osborn**, *Nucl. Phys. B*
**234** (1984) 331 (PARTIAL — full authors confirmed; paper title not directly
read and should be confirmed before any paper-grade use). The scheme-freedom
reference Martini–Zanusso credit to "Jack 1983" was not bibliographically
pinned and should also be resolved before any paper-grade use.

## 7. Self-checks

- **Dimensional analysis.** All couplings ($\lambda, \xi, g, g', y_t$) are
  dimensionless in $d=4$; $\ell = \lambda/16\pi^2$ is dimensionless; β-functions
  are dimensionless. The two-loop expression in §2 is dimensionally homogeneous.
  ✓
- **Limiting cases.** Dropping the $O(\ell^2)$ term recovers the one-loop
  $\beta_\xi \propto (\xi - 1/6)$ and reproduces the Markkanen et al. form in
  the pure-λφ⁴ truncation (gauge/Yukawa set to zero). ✓
- **Consistency.** Compatible with Remark 9's existing claim that no SM two-loop
  β_ξ is published (§2 confirms it), and with the framework's trace-anomaly
  mechanism (§3 shows the destabilizing anomaly and the curvature-sourcing
  anomaly are the same object) — no contradiction with any merged result. The
  scheme caveat (§2) prevents over-claiming, consistent with the demotion
  discipline applied to CE-3. ✓
- **Order-of-magnitude.** The two-loop coefficient *at the conformal point* is
  $1/18 \approx 0.056$ (from the explicit evaluation $-(7/36 - 5/36) = -1/18$;
  see §2 item 1). With $\ell \sim \lambda/16\pi^2 \sim 10^{-2}$ for SM-scale
  $\lambda$, the conformal-point β_ξ is $\sim (1/18)\,\ell^2 \sim 6 \times
  10^{-6}$ — perturbatively small but nonzero, so the shift is real but not
  large; the "inaccessible" conclusion would depend on RG running over many
  decades, not a large local slope. ✓

## 8. Bottom line

The conformal coupling $\xi = 1/6$ is **not** an all-orders RG fixed point and
is **not** symmetry-protected; the would-be protector (Weyl invariance) is
anomalous in 4D — the same anomaly the framework uses to source curvature. The
only explicit higher-loop curved-space calculations (pure λφ⁴) show it shifting.
This **strengthens** Conjecture 2's premise that $\xi \neq 1/6$ is generic from
naturality-only to naturality-plus-calculation-plus-symmetry-argument, but does
**not** prove the "inaccessible" branch for the SM, because no SM two-loop β_ξ
exists and the massless-theory shift is partly scheme-dependent. Conjecture 2
remains a Conjecture. Net rigor of this exploration's verdict: **Sketch**.
