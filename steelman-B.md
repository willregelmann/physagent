# Steelman pass — Attempt B (precedent check, then dimensional transmutation on the Lorentzian branch)

**Target:** `/home/will/Projects/physagent/attempt-B-precedent-transmutation.md`, against `/home/will/Projects/physagent/attack-B.md`
**Date:** 2026-09-05
**Role:** Steelman (Pass 2 of METHODOLOGY.md's "No Idea Is Eliminated Without a Defense"). For each of the attack's twenty flaws: fatal / solvable gap / narrower-but-viable / framing, with the rescue actually attempted. Flaw numbers are the attack's.

Sources re-read this session: `programs/co-emergence/index.tex` (Axioms, lines 159–252; "Weakening the mass assumption," 1219–1348; OS section, 1815–1840), `programs/fixed-point-existence/index.tex` (95–175), the five claim files named in the brief, the two March 2026 explorations, `asselmeyer-maluga-verification.md`. PDFs of Asselmeyer-Maluga–Król (arXiv:1801.10419), Di Tucci–Lehners (arXiv:1903.06757), Ji (hep-ph/9410274), Hawking–Hertog–Reall (hep-th/0010232) and Ruberman's Floer-homology notes were fetched and text-extracted with `pdftotext`; quotes below are from the extracted text. Numerics are inline.

---

## Numerics used throughout

```python
# nums.py (condensed)
MP=1.2209e19; LQCD=0.25; b0=7.0
def req(H0): ln=log(H0/LQCD); g2=8*pi**2/(b0*ln); return ln, g2, 4*pi/g2
# H0 conventions:
#  attempt  MP/sqrt(1e5)              H0=3.86e16 GeV  ln=39.6  g2=0.285  alpha_s=1/44.1
#  printed  sqrt(180pi/1e5)*MP        H0=9.18e17 GeV  ln=42.7  g2=0.264  alpha_s=1/47.6
#  printed/16pi variant               H0=1.29e17 GeV  ln=40.8  g2=0.277  alpha_s=1/45.4
#  MP                                 H0=1.22e19 GeV  ln=45.3  g2=0.249  alpha_s=1/50.5
# Lambda^(6) instead of 0.25: L=0.09 -> 1/48.8 ; L=0.04 -> 1/49.7
# cap action |I_E| = pi/(G H0^2):  attempt-H0: 3.1e5 ; printed-H0: 5.6e2
#   1% shift of H0^2 -> delta I = 3.1e3 (attempt) / 5.6 (printed)
# gauge-anomaly relative size b0 g2/(16 pi^2) = 0.0126
# width in g2 needed to fix LQCD to a factor e: d(g2)/g2 = b0 g2/(8 pi^2) = 0.025
# dS phase: 1/H0 = 7e-43 s ; 60 e-folds = 4e-41 s ; 1/LQCD = 2.6e-24 s
# H0/LQCD = 1.5e17 (attempt) / 3.7e18 (printed)  -- NOT 1e20
# fractional-instanton weight (LQCD/H0)^(b0*cs): cs=1/60 -> 10^-2.2 ; cs=1/120 -> 10^-1.1 ; cs=1 -> 10^-130
# AM-K check: theta=3/(2*9/280)=46.67; 1+th+th^2/2+th^3/6=18075; E_P/18075=6.75e14 GeV (paper 0.67e15)
#   E_P*exp(-1/(2*(1/60)))/18075 = 63.2 GeV (paper 63); exponent 1/(2CS)=30
#   if 8pi^2/(b0 g2)=30 then g2=0.376, alpha_s=1/33
# orders of magnitude (mass units) junction->hadron 18.6, ->electron 21.3, ->0.05 eV neutrino 28.3
```

---

## Flaw-by-flaw

### 1. "Flat modulus" is false: perturbative $g^2$-dependence of the cap weight
**Verdict: narrower-but-viable as a decoupling statement; the "flat" wording is dead.**

The attack is right on the substance and I will not defend the sentence. Two independent sources of $g^2$-dependence exist even before two loops: (i) the one-loop measure itself. Rescaling $A\to gA$ turns the Gaussian into a $g$-independent one at the cost of a Jacobian, so $F=-\log Z\supset-\tfrac12(N_c^2-1)\zeta_{\rm vec}(0)\log g^2$, with $\zeta(0)$ an $O(1)$ number per field tied to the integrated anomaly; (ii) the gauge term of the anomaly, $\tfrac{\beta}{2g}\langle F^2\rangle$, which shifts $a_{\rm eff}$ by a relative $b_0g^2/16\pi^2\times O(1)\approx1.3\%$ (the attack's estimate; I reproduce the prefactor). What the attack did not do is propagate (ii) through the cap action $I=-\pi/(GH_0^2)$: a $1\%$ shift of $H_0^2$ is $\delta I\approx0.01|I|$, which is $\approx6$ with the printed coefficient and $\approx3\times10^3$ with the attempt's own $H_0$. So the attack's "$O(1)$–$O(N_c^2)$ in the exponent" is if anything an *underestimate*.

Two things cut the other way, and they matter for what survives. First, the attack's own citation undermines the sharpness of its number: Gerchkovitz–Gomis–Komargodski (verified, abstract) state that in even dimensions the finite, coupling-dependent part of the sphere partition function "is typically regularization-dependent and unphysical" absent extra symmetry. Neither "flat" nor "$\delta I\approx0.01|I|$" is scheme-independent; the scheme is fixed by the same finite $R^2$ counterterm (HHR eq. 2.9, verified) that the exit needs. Second, what *is* scheme-independent is the structure: the dependence is a log plus a power series in $g^2$, and the dependence on $\Lambda_{\rm QCD}$ itself is through $(\Lambda_{\rm QCD}a_0)^{b_0|k|}\sim10^{-120}$–$10^{-130}$ (the attempt's identity, which holds).

**Narrowed statement (Sketch).** *The cap amplitude is sensitive to the gauge sector perturbatively, through $g^2(a_0^{-1})$, and is insensitive to the transmuted scale $\Lambda_{\rm QCD}$ itself. If $g^2$ is a parameter of the action, the cap constrains nothing about it. If $g^2$ were a cap modulus, the leading dependence is monotone (linear in $g^2$ at the first order that is not a log), so a Baum–Hawking-type extremization drives it to an endpoint: either strong coupling at the junction ($\Lambda_{\rm QCD}\to H_0$, no hierarchy) or $g^2\to0$ ($\Lambda_{\rm QCD}\to0$). Which endpoint depends on the sign of $\langle F^2\rangle_{\rm ren}$ on $S^4$, not computed here. An interior extremum from the competition of the $\log g^2$ (one-loop) and linear (two-loop/anomaly) terms is not excluded, but by loop counting it sits at $g^2\sim O(16\pi^2/N_c)$, i.e. strong coupling, and is scheme-dependent.*

Does the narrowed statement still do the attempt's work? Half of it. It does the *locating* work: the hierarchy is not a cap observable, and nothing at the root prefers or disprefers it. It does **not** do the rhetorical work of "flat modulus," and it converts the attempt's kill condition 1 from "no candidate" (attack right: this is the default once $g^2$ is dynamical) into a statement that $g^2$ must be a fixed parameter of the branch's field theory. Making $g^2$ dynamical is a kill, not a rescue, unless a stabilizing potential is added by hand, which is one more input.

### 2. "The root weights $g^2$ flatly" has no referent; a weight on a modulus selects an extremum
**Verdict: attack right; framing error that is fatal to the wording, not to the attempt.**

Conceded. $g^2$ is a parameter of the action, not a South-Pole datum like HHH's $\phi_0$; there is no measure over it. Given flaw 1, the only honest content is: *the no-boundary structure neither fixes nor constrains $g^2$.* Read that way the attempt's position is true and modest, and it matches the March synthesis's own prediction that the spectrum "may require additional input (field content, coupling constants)."

### 3. "$\mu_*=H_0$ is fixed by the junction (Rigorous)" is empty
**Verdict: framing; the Rigorous label was attached to a tautology.**

Conceded: $\Lambda_{\rm QCD}$ is RG-invariant, so where one quotes $g^2$ is a convention. Two things survive. (a) The cap-side reading of the identity is a true statement about the cap: the density of instantons of size $\sim a_0$ on the cap is $(\Lambda_{\rm QCD}a_0)^{b_0}$; that it is true at every scale is what makes it useless for selection, which is flaw 1 again. (b) The RG-invariance is *helpful* for flaw 6 below: because the scale is defined at every point of the block, the location of confinement is immaterial to the scale. Correct statement: *$\Lambda_{\rm QCD}$ is a property of the gauge sector on the whole block, cap included; the junction curvature is one convenient place to quote $g^2$, nothing more.*

### 4. Importing $SU(3)$ violates Axiom 2; the attempt contradicts itself
**Verdict: framing; the attack overreaches on "forbids," the attempt's self-contradiction is real and repaired by rewording.**

Axiom 2 as written (`index.tex:172-179`): "The *fundamental* description contains no fixed metric, no preferred foliation, no assumed symmetry group ... at the deepest level, metric structure and matter both emerge from topology (Conjecture)." The paper's Level-2 effective description already takes field content as input, and the paper says so: $a_2$ requires a species list; Conjecture `conj:mass_generation` requires species with $\xi\neq1/6$; and Remark `rem:xi_running` (lines 1305–1348) uses the one-loop Standard-Model $\beta_\xi$ *with the electroweak gauge couplings $g,g'$ explicitly*, i.e. the paper already imports $SU(2)\times U(1)$ structure at Level 2 for a naturality argument, and states "We do not claim to have derived the Standard Model" (line 246). Further, a list of $N_v=12$ interacting massless vectors already entails a 12-dimensional gauge group (Lorentz-invariant interacting massless spin-1 requires coupling to conserved currents; standard, not searched this session). So $b_0$ is one more datum of the *same category* (the non-abelian structure constants beyond the dimension count), not a new category. The March synthesis explicitly anticipated "coupling constants" as the additional input.

What the attack gets right: "the junction fixes $b_0$ once a group is specified" is wrong; the specification fixes it. Reworded: *$b_0$ is a Level-2 input of the same kind as $a$, $c$ and $\xi$; the junction fixes nothing about it. This is consistent with the paper's stated status, and no more an Axiom-2 violation than the paper's own Remark `rem:xi_running`.*

### 5. Double standard between HHH ("needs input $m$") and transmutation ("needs input $g^2$")
**Verdict: narrower-but-viable.**

The genuine distinction the attempt failed to state is *sensitivity*: with a dimensionful input $m$, the output is $O(m)$ and nothing below the input appears; with a dimensionless $O(1)$ input, the output is $H_0e^{-8\pi^2/b_0g^2}$, eighteen orders below the only dimensionful scale with no small number put in. That is the technical-naturalness distinction and it is real. The attack is right that it is a property of QCD, established in flat space, with no dependence on cap, junction or branch. So "the hierarchy is generated on the branch" must become *"the hierarchy is generated by the gauge sector wherever it lives; the cap–branch geometry neither supplies nor obstructs it."* The honest answer to the question as posed is **no**, and the attempt's real product is the precise minimal residue: one dimensionless number, $\alpha_s(\mu_*)\in[1/50,1/44]$ across the repo's $H_0$ conventions, with sensitivity $\Delta g^2/g^2=b_0g^2/8\pi^2\approx2.5\%$ per e-fold of $\Lambda_{\rm QCD}$.

### 6. Branch too short: dS phase lasts $10^{-42}$–$10^{-40}$ s; confinement is post-exit; "$10^{20}$" is wrong
**Verdict: narrower-but-viable; the factual errors are conceded.**

Conceded: $H_0/\Lambda_{\rm QCD}=1.5\times10^{17}$ (attempt's $H_0$) or $3.7\times10^{18}$ (printed), not $10^{20}$; HHH's condition (3.13) is WKB classicality, not duration; the anomaly-driven dS segment lasts $\sim60/H_0\approx4\times10^{-41}$ s (reproduced above) against $1/\Lambda_{\rm QCD}=2.6\times10^{-24}$ s; and HHR (verified, lines 156–161) place the matter-dominated FRW phase with "particle production and (p)reheating" after the instability.

The rescue the brief proposes is viable and costs little that was not already lost. Because $\Lambda_{\rm QCD}$ is RG-invariant (flaw 3), the *scale* is defined on the whole block; only the *phenomenon* of hadron mass requires a region where the curvature has fallen below $\Lambda_{\rm QCD}^2$, which in the repo's model is the post-exit FRW region. That region is part of the Lorentzian branch in the reframing under exploration ("Lorentzian classical histories branch off"), even though the fixed-point program itself uses only existence (`fixed-point-existence/index.tex:160`). The cost: (i) "the junction fixes $\mu_*$" is gone (it was empty anyway); (ii) "the state is fixed by cap regularity" is gone (flaw 7); (iii) the exit requires $d<0$, i.e. HHR's finite $R^2$ counterterm with coefficient of order $10^8$ (HHR, verified, lines 316–336 and 1638), an input beyond $(\Lambda,G,a,c)$ that the *reframing* needs regardless of this attempt, and that must be counted.

### 7. The state in which $\langle F^2\rangle$ is evaluated is not the one cap regularity fixes
**Verdict: framing plus concession.**

Attack right that the attempt overreached: Halliwell–Hawking 1985 concerns scalar and metric harmonics, and the gluon condensate is the infrared vacuum reached after reheating and cooling through $T_c$. But the overreach was unnecessary. The *scale* $\Lambda_{\rm QCD}$ and the hadron spectrum are properties of the theory's vacuum, not of the cosmological state; the post-reheating state relaxes to that vacuum below $T_c$. The narrowed attempt needs only that the branch contains a low-curvature region in which the gauge sector is in, or relaxes to, its vacuum, which is standard cosmology. The repo's `ce-euclidean-vacuum-at-fixed-point` gate does not bear on this, because that claim is about the exact dS point. Where the state *does* matter is the co-emergence Level-3 use (mass shell, Page–Wootters clock), and that is Conjecture 2's business with $m_{\rm eff}$, not this attempt's.

### 8. OS reconstruction reinstated as mechanism; Lorentzian form factor needs a prescription
**Verdict: concede OS (and it dissolves under the narrowing); framing on the form factor.**

The attempt's §4.2 did make OS across the curved junction the source of the state, which the March record kills (`2026-03-02-signature-mass-codependence.md`: "OS-as-mechanism dead, OS-as-evidence alive"; `index.tex:1826-1831`). Under the narrowing of flaw 7 the state is no longer sourced from the cap, so OS is not needed. On the form factor: the attack is right that $\log(\Box/\mu^2)$ on the Lorentzian branch requires an in-in or in-out prescription, which is a time orientation; but the $\beta$-function and $\Lambda_{\rm QCD}$ are prescription-independent (prescriptions differ in the dissipative parts of the form factor, not in the coefficient of the log). So "orthogonal to Halliwell/Banks" was overclaimed for the *location of the phenomenon* (see 6 and 20) and is correct for the *scale*.

### 9. Scope: only $\Lambda_{\rm QCD}$; the electroweak scale and fundamental masses untouched
**Verdict: narrower-but-viable, and worth recording.**

The attack is right that the "(mass terms)" on line 43 silently carries the whole Standard-Model hierarchy. The honest narrowed claim: *transmutation supplies exactly one of the required scales, the hadronic one; via the trace identity (Ji, verified, eq. 36) that is $(1-b)M_N\approx780$–$830$ MeV of the nucleon's 939 MeV; the electroweak vev and every fundamental fermion mass are the Standard Model's own hierarchy problem, which the reframing neither creates nor solves.* Whether this answers the mass test as the experimenter posed it: in mass units the junction-to-hadron gap is 18.6 orders, junction-to-electron 21.3, junction-to-neutrino 28.3 (printed $H_0$); the attempt covers the first only. (A "60 orders" figure corresponds to energy-density or $m^4$ language, or to the observed $\Lambda$, which `fpe-fixed-point-is-inflationary` records as a different object from the repo's $H_0$.)

One honest widening exists and should be stated as a Conjecture: in a classically scale-invariant completion the electroweak scale is itself transmuted, either by Coleman–Weinberg in an enlarged scalar sector (Meissner–Nicolai 2007, verified) or by a hidden strongly coupled sector (Hur–Ko 2011, verified: "all mass scales in the model arising from the hidden sector scale"), following Bardeen's 1995 argument (existence verified). In such a completion *every* Standard-Model mass reduces to dimensionless couplings at $\mu_*$, and the junction must carry a *set* of $O(1)$ numbers and nothing dimensionful beyond $(\Lambda,G)$. That is the maximal honest form of "the branch generates the hierarchy": it generates the *form* $e^{-1/g^2}$ for as many scales as there are asymptotically free or radiatively broken sectors, and never the numbers.

### 10. The fixed-point existence result is for conformal matter; an asymptotically free sector is not conformal on the cap; exit needs $d<0$
**Verdict: solvable gap (existence), with a concrete route; shared cost (exit).**

What the FPE claim actually assumes (`fpe-starobinsky-existence.md`): "FRW/cosmological setting; conformal matter with $a_2>0$." Starobinsky's mechanism needs two things: a dS-invariant state so that $\langle T_{ij}\rangle=\tfrac14g_{ij}\langle T\rangle$ (HHR eq. 1.5, verified: "the symmetry of the vacuum implies that the expectation value of the energy momentum tensor can be expressed in terms of its trace"), and a trace that is a pure number times $H^4$. For an asymptotically free sector at weak coupling on the cap ($a_0^{-1}\gg\Lambda_{\rm QCD}$), the Euclidean state defined by the $S^4$ path integral is dS-invariant, dimensional analysis plus RG invariance give $\langle T\rangle=H^4\tilde F(g^2(H))$ with $\tilde F=-24a+O(b_0g^2/16\pi^2)$, and the fixed-point condition becomes $H^2=3/(8\pi G\tilde F(g^2(H)))$. Since $g^2(H)$ varies logarithmically, this has a root near the conformal one by continuity, shifted by $\approx1\%$. Classical conformality of Yang–Mills is what makes the *only* non-decoupling non-conformality the running, and HHR's own remark (verified, line 141) is the relevant one: fields are "effectively conformally invariant if their masses are negligible compared to the spacetime curvature." Route: compute $\langle F^2\rangle_{\rm ren}$ for a free gauge field on $S^4$ at one loop, assemble $a_{\rm eff}$, exhibit the root. Rigor target: Sketch, promotable.

On HHR's use of $\mathcal N=4$: the attack's reading is half right. They use it for AdS/CFT control at strong coupling; the verified sentence "our results are actually independent of the Yang-Mills coupling" (line 192) is a statement about $\mathcal N=4$'s exact $a,c$, not a requirement of the mechanism; their eqs. (2.6)–(2.8) are the free-field counting. On $d<0$: conceded as an input the reframing needs; see flaw 6.

### 11. The worked $H_0$ drops the $180\pi$ and misattributes the convention
**Verdict: factual; conceded.**

With the printed coefficient, $H_0=9.2\times10^{17}$ GeV, $\ln(H_0/\Lambda_{\rm QCD})=42.7$, required $\alpha_s=1/47.6$; the "$16\pi$ discrepancy" variant in `fpe-starobinsky-coefficient.md` gives $1.3\times10^{17}$ GeV and $1/45.4$. The range $[1/50,1/44]$ across conventions is what should be quoted. No conclusion changes; the attribution was wrong.

### 12. The "self-consistent with known physics" check is tautological; wrong $\Lambda$
**Verdict: conceded.**

Plugging the measured $\Lambda_{\rm QCD}$ into one-loop running and comparing with one-loop running of the measured $\alpha_s(M_Z)$ is QCD checked against itself. With $\Lambda^{(6)}=0.04$–$0.09$ GeV the required value moves to $1/49$–$1/50$; the attack's threshold-matched run gives $1/46$ at $4\times10^{16}$ GeV. The only non-tautological content is that the *measured* coupling run to the junction is a number of order $1/40$–$1/50$, which fixes the target any adaptation must hit.

### 13. HHH: factor 6 in $H_{\rm eff}^2$; dropped $\mu>3/2$ qualifier
**Verdict: conceded (units mismatch); minor.**

In HHH's variables ($G=1$, $\phi=(4\pi/3)^{1/2}\Phi$) the Friedmann equation gives $H^2=m^2\phi^2$, consistent with their "effective cosmological constant $3m^2(\phi_R(0))^2$" that the attack verified; the $/6$ is the reduced-Planck-unit form. Not re-fetched this session. The $\mu>3/2$ qualifier should be added. The "modulus, not hierarchy" verdict stands.

### 14. Ji 1995: anomaly share is $(1-b)/4$, not the whole chiral-limit mass
**Verdict: framing (a citation-label error); the attack overreaches on "content mismatch."**

Verified from Ji's text: eq. (5) $\hat T^{\mu\nu}=\tfrac14g^{\mu\nu}[(1+\gamma_m)\bar\psi m\psi+\tfrac{\beta(g)}{2g}F^2]$; eq. (9) $\langle P|\hat T^{\mu\nu}|P\rangle=\tfrac14g^{\mu\nu}M$; and eq. (36), verbatim: "$\langle P|\bar\psi m\psi+\tfrac{\beta(g)}{2g}F^2|P\rangle=M$, which is an explicit form of Eq. (11)." So in the chiral limit the matrix element of the anomaly *operator* is the whole nucleon mass, and Ji's numbers say so: $(1-b)M=779$–$832$ MeV (eqs. 33, 38). The attack is right that Ji's *Hamiltonian decomposition* (eqs. 21–28, Table I) assigns the anomaly *energy* $(1-b)/4\to M/4$ (190–210 MeV). Both statements are in Ji; they are two different decompositions of the same $M$. The attempt's sentence mislabels the trace identity as "Ji's decomposition." Fix: cite "the trace identity (Ji eq. 36)" for the whole-mass statement and "Ji's Hamiltonian decomposition" for $M/4$; SVZ is not needed. The physics point, that every piece scales with $\Lambda_{\rm QCD}$, holds either way. No conclusion changes.

### 15. Adaptation (2): the Di Tucci–Lehners Robin analogy is loose and adds a parameter
**Verdict: attack right; fatal for "fixes $g^2$"; a definable construction exists, but it is the input relocated.**

Di Tucci–Lehners verified from the text: $q(t)$ "is the squared scale factor, while $N(t)$ is the lapse function"; $S_{\rm tot}=S+\alpha q_0+q_0^2/(2\beta)$; $B\equiv\tfrac{3\pi^2}{N}\dot q_0+\alpha+\tfrac{q_0}{\beta}=0$; "the initial size $\bar q_0$ vanishes at one (or more) of the saddle points if $\alpha=\pm6\pi^2i$ or $\beta=0$ ... we will consider $\alpha=-6\pi^2i$"; "corresponds to a specific value of $\alpha$ but leaves $\beta$ free"; "$\beta$ has to be negative imaginary"; and "$\Delta q_0=\sqrt{|\beta|}\sim1/H$ ... the uncertainty must be shared between the initial size and the initial momentum, with the uncertainty being of order the Hubble length." Two corrections to the attack's framing, neither of which rescues the adaptation: $\beta$ is not arbitrary but fixed in order of magnitude by consistency ($|\beta|\sim H^{-2}$, with "an upper bound on $|\beta|$"), and the Robin term lives at the *nucleation point* $q_0\to0$, not at the junction, so the attempt misplaced it.

The gauge analogue: the attack's three obstacles hold. The one gauge-invariant boundary functional on a 3-surface that carries coupling-type data is the Chern–Simons functional with a *complex* coefficient. Ruberman (verified): "$\int_X{\rm tr}(F_A\wedge F_A)\pmod{8\pi^2\mathbb Z}$ depends only on the gauge equivalence class of $A|_Y$," and with the Bogomolny bound (textbook, not searched) the bulk action of an (anti-)self-dual configuration on the cap is $(8\pi^2/g^2)(k+cs)$ with $cs$ the normalized boundary CS value. So a "Robin gauge datum" is the complexified $\theta$, i.e. the holomorphic coupling $\tau=\theta/2\pi+4\pi i/g^2$ restricted to the self-dual sector: specifying it *is* specifying $g^2$. Real construction; not a derivation; one more input, as the attack says.

### 16. Adaptation (1): disconnected from the repo's record; the one published attempt (AM–K) was missed and is non-exponential
**Verdict: attack partly overreaches on the mechanism; right on the repo record; the adaptation gains a definite candidate object but still no fixing mechanism.**

Asselmeyer-Maluga–Król, Mod. Phys. Lett. A (2019), arXiv:1801.10419, verified from the extracted text. Their eq. (2): $a=a_0\cdot\exp\!\big(\tfrac{3}{2\,CS(\Sigma(2,5,7))}\big)$, an *exponential in the inverse* Chern–Simons invariant, which the authors stress is the unusual placement ("In all cases, the Chern-Simons term is not a denominator of a fraction. In the presented approach, hyperbolic geometry explains how the CS term appears"). Their eq. (4) for the GUT scale is the truncated series $\Delta E=E_P/(1+\vartheta+\vartheta^2/2+\vartheta^3/6)$ with $\vartheta=3/(2CS)=140/3$, $CS(\Sigma(2,5,7))=9/280$, giving $0.67\times10^{15}$ GeV (reproduced: $E_P/18075=6.75\times10^{14}$). Their eq. (5) for the second scale is $M=E_P\exp\!\big(-\tfrac{1}{2CS(P\#P)}\big)/(1+\vartheta+\ldots)\approx63$ GeV with $CS(P\#P)=1/60$ (reproduced: $e^{-30}\times6.75\times10^{14}=63.2$ GeV). So the attack's "truncated polynomial, not $e^{-1/g^2}$" describes eq. (4) only; eqs. (2) and (5) have exactly the $e^{-1/x}$ form with a topological rational $x$ in the denominator, and the exponent $30$ is within a factor $1.4$ of the $40$–$45$ the attempt needs (outside the attempt's own $\pm5$ band). The attack's "not a gauge coupling" stands: $CS$ is a rational number, there is no $\beta$-function, no running, and no scale dependence. The derivation of eq. (2) rests on the hyperbolic geometry of the Casson handle in their earlier papers, which the repo's verification pass marked Sketch/unverified; I did not verify it, and repo Verdict 1 ("Can we rely on it? No") stands.

What the rescue gains for adaptation (1): a *named* Level-0/1 quantity. The only rigid topological datum that multiplies $1/g^2$ in the cap's gauge action is the CS invariant of a flat connection on the junction 3-manifold (Ruberman, verified, plus the Bogomolny bound), which requires $\pi_1(\Sigma)\neq0$; the reframing's round $S^3$ junction has none. On a Brieskorn-type junction the fractional-instanton weight is $(\Lambda_{\rm QCD}/H_0)^{b_0cs}$, which for $cs=1/60$ or $1/120$ is $10^{-2.2}$ or $10^{-1.1}$, *not* negligible, unlike the integer sectors' $10^{-130}$. But this weights topological sectors; it does not fix $g^2$. Note the two "CS routes" are different objects: AM–K's is coupling-like (CS in the denominator, unverified derivation), Floer's is action-like (CS in the numerator, rigorous, no selection). For the record, identifying AM–K's exponent with $8\pi^2/(b_0g^2)$ gives $\alpha_s=1/33$ against the required $1/44$–$1/50$; I record this as numerology and do not use it, the same discipline the attempt applied to its $1/a$ line. Cost of the route: a non-simply-connected junction is a different Level-0 setup from the cap the question posits, and the repo's own note that closed simply-connected 4-manifolds with nontrivial intersection form cannot be Lorentzian must be revisited for it.

### 17. $\theta$ omitted from the input accounting
**Verdict: conceded; minor.** The accounting is short by one. At the junction the $\theta$-term becomes the boundary CS term, the same object as in 15 and 16.

### 18. "$^{(3)}R$ is a covariant scalar" hides a distinguished surface
**Verdict: framing; conceded.** The surface is distinguished by construction (the reframing hands it over). The 4-scalar $R=4\Lambda$ gives the same $\mu_*$ up to $O(1)$, invisible in a logarithm of $40$, so the *scale* is foliation-free even though the *surface* is not.

### 19. Fradkin–Tseytlin row: two-loop $f_2^2$ dependence; Avramidi–Barvinsky correction
**Verdict: conceded; not load-bearing.** Avramidi–Barvinsky 1985 existence and abstract verified ("in the case of the positive definite euclidean action the theory is shown to be asymptotically free"); the specific claim about the $R^2$-sector coupling was not verified by the attack or by me.

### 20. The mechanism depends on branch evolution the attempt disowns
**Verdict: framing / narrower.**

No evolution parameter is *input*: "the block contains a region with curvature $\ll\Lambda_{\rm QCD}^2$" is a constraint-level property of the solution, in Axiom 1's own language ("constraints on the structure of the four-dimensional block"). The attack is right that the repo has no result about that region and that the attempt's "not used" was overclaimed: the branch geometry beyond the dS segment *is* used. The existence of the low-curvature region is supplied by citation (Starobinsky's decay to FRW; HHR verified), the reheating state by standard cosmology, and the exit by the $d<0$ input of flaw 10. Solvable, with the cost stated.

---

## Surviving form of the attempt

**S0. Answer to the mass test (Sketch-level negative, with a precise residue).** From $(\Lambda,G)$ alone, the cap–branch structure generates no scale other than $\Lambda^{1/2}$ (the repo's $H_0\sim M_P/\sqrt{a_2}$, coefficient Sketch) and $M_P$. An exponentially separated scale can live on the branch only as the transmuted scale of an asymptotically free sector, and its value is fixed by one dimensionless datum per scale, which the geometry neither supplies, prefers, nor obstructs.

**S1 (Rigorous, standard QFT).** For an asymptotically free sector with $b_0>0$, $\Lambda=\mu\,e^{-8\pi^2/(b_0g^2(\mu))}$ is RG-invariant and independent of signature, foliation and state; it is a property of the theory on the whole block, cap included.

**S2 (Rigorous arithmetic, given the Sketch $H_0$).** Matching the hadronic scale requires $\alpha_s(H_0)\in[1/50,1/44]$ across the repo's $H_0$ conventions, with sensitivity $\Delta g^2/g^2\approx2.5\%$ per e-fold of $\Lambda_{\rm QCD}$; no combination of $G\Lambda$, $\ln(3\pi/G\Lambda)$, $a$, $c$ yields the exponent $40$–$45$.

**S3 (Sketch): non-selection.** The cap amplitude depends on $g^2(a_0^{-1})$ perturbatively (a $\log g^2$ from the measure, then a term $\sim b_0g^2/16\pi^2\times O(1)$ of $a_{\rm eff}$, i.e. $\delta I\approx0.01|I_{\rm cap}|$, scheme-dependent per GGK with the scheme fixed by the $R^2$ counterterm) and on $\Lambda_{\rm QCD}$ itself only through $(\Lambda_{\rm QCD}a_0)^{b_0}\sim10^{-120}$. Hence: if $g^2$ is a parameter the cap constrains nothing; if $g^2$ were a modulus, the leading dependence is monotone and extremization drives it to an endpoint (either kills the hierarchy), with an interior extremum possible only at strong coupling by loop counting. Replaces "flat modulus."

**S4 (Sketch): existence with an asymptotically free sector.** dS invariance and RG invariance give $H^2=3/(8\pi G\tilde F(g^2(H)))$; a root exists near the conformal one; shift $\approx1\%$. Route stated under flaw 10.

**S5 (Sketch / standard): location.** Hadron mass is realized where the curvature is $\ll\Lambda_{\rm QCD}^2$, i.e. post-exit; the dS segment lasts $\sim60/H_0\approx4\times10^{-41}$ s; the exit requires $d<0$ (an $R^2$ counterterm, input); the operative state is the cooled post-reheating vacuum, not the cap's ground state.

**S6 (Conjecture): scope.** Transmutation supplies the hadronic scale only. In a classically scale-invariant completion (Bardeen; Meissner–Nicolai; Hur–Ko) the electroweak scale and hence all Standard-Model masses are also transmuted, so the junction must carry a set of dimensionless couplings and nothing dimensionful beyond $(\Lambda,G)$. The branch supplies the *form* $e^{-1/g^2}$, never the numbers.

**S7 (Conjecture): the sharpened adaptation.** The only rigid Level-0/1 datum that enters the cap's gauge action multiplying $1/g^2$ is the Chern–Simons invariant of a flat connection on the junction 3-manifold, which requires $\pi_1(\Sigma)\neq0$ and weights topological sectors as $(\Lambda_{\rm QCD}/H_0)^{b_0cs}$ (non-negligible for $cs\sim1/60$) without fixing $g^2$. Asselmeyer-Maluga–Król's denominator-CS exponential is a distinct, unverified structure that happens to produce an exponent of 30. The falsifiable target is unchanged: produce $\ln(H_0/\Lambda)\approx40$–$45$ from Level-0/1 data. Nothing found does so.

Everything in the attempt's original "commit" that is stronger than S0–S7 (flat modulus; junction fixes $\mu_*$; junction fixes $b_0$; hierarchy generated on the branch; state from cap regularity; OS across the junction; Robin datum fixes $g^2$) does not survive.

## What the rescue could not do

1. Compute $\langle F^2\rangle_{\rm ren}$ for a free gauge field on $S^4$ (sign and magnitude): it fixes the sign of $dH_0^2/dg^2$, hence which endpoint a dynamical $g^2$ would be driven to, and it is the one-loop input to S4.
2. Compute the two-loop $S^4$ free energy of Yang–Mills in a fixed scheme and decide whether the $\log g^2$ versus linear competition has an interior extremum anywhere in the perturbative range; my loop-counting estimate puts it at strong coupling and is not a result.
3. Find any mechanism that fixes $g^2(H_0)$: none. AM–K's eq. (2) was not verified beyond reproducing their numbers; the Floer route weights sectors only; the Robin route is the input relocated.
4. Extend the FPE existence claim to an asymptotically free sector at the level of the claim file (S4 is a route, not a result).
5. Supply a repo-level result about the post-exit branch; S5 rests on citation to Starobinsky/HHR and on standard cosmology.
6. Check that a classically scale-invariant completion (S6) is consistent with Remark `rem:xi_running`'s one-loop $\beta_\xi$; not examined.
7. Reflection positivity on the hemisphere: no longer needed for the *scale*; still open for the Level-3 uses, unchanged from the attempt's own list.

## Citations used

| Reference | Status this session | Used for |
|---|---|---|
| Asselmeyer-Maluga & Król, "A topological approach to Neutrino masses by using exotic smoothness," Mod. Phys. Lett. A (2019), arXiv:1801.10419 | **Verified, full text (pdftotext).** Eqs. (2)–(5), $CS(\Sigma(2,5,7))=9/280$, $CS(P\#P)=1/60$, $0.67\times10^{15}$ GeV, 63 GeV; numbers reproduced. Derivation of eq. (2) not verified. | Flaw 16, S7 |
| Di Tucci & Lehners, PRL 122, 201302 (2019), arXiv:1903.06757 | **Verified, full text.** $q$ = squared scale factor; $S_{\rm tot}$; $B=0$; $\alpha=\pm6\pi^2i$; $\beta$ free, negative imaginary, bounded, $\Delta q_0\sim1/H$. | Flaw 15 |
| Ji, PRL 74, 1071 (1995), hep-ph/9410274 | **Verified, full text.** Eqs. (5), (9), (11), (21), (36); Table I; $bM=160/107$ MeV. | Flaw 14, S6 |
| Hawking, Hertog & Reall, PRD 63, 083504 (2001), hep-th/0010232 | **Verified, full text.** Eq. (1.5); lines 141, 156–164, 192, 316–336, 1638, 1967–1977. | Flaws 6, 7, 10, 20; S4, S5 |
| Ruberman, "An introduction to Floer homology" (Simons Center notes) | **Verified, full text.** $\int_X{\rm tr}(F\wedge F)\bmod8\pi^2\mathbb Z$ depends only on $A|_Y$; CS defined as that residue; ASD equation as gradient flow. | Flaws 15, 16; S7 |
| Gerchkovitz, Gomis & Komargodski, JHEP 11 (2014) 001, arXiv:1405.7271 | **Verified, abstract.** Even-$d$ finite part of sphere partition function "regularization-dependent and unphysical" absent extra symmetry. | Flaw 1, S3 |
| Meissner & Nicolai, Phys. Lett. B 648, 312 (2007), hep-th/0612165 | **Verified, abstract.** Classically conformal SM with right-chiral neutrinos and enlarged scalar sector; radiative (CW) breaking generates the hierarchy. | Flaw 9, S6 |
| Hur & Ko, PRL 106, 141802 (2011), arXiv:1103.2571 | **Verified, abstract (search snippet).** Hidden QCD-like sector, dimensional transmutation, "all mass scales ... arising from the hidden sector scale." | Flaw 9, S6 |
| Bardeen, "On naturalness in the standard model," FERMILAB-CONF-95-391-T (1995) | **Verified, existence** (Fermilab preprint archive, CDS record); content from secondary citations only. | Flaw 9, S6 |
| Avramidi & Barvinsky, Phys. Lett. B 159, 269 (1985) | **Verified, existence and abstract** (INSPIRE). | Flaw 19 |
| Hartle, Hawking & Hertog 2008 (arXiv:0803.1663) | Not re-fetched; attack's verbatim quotes accepted; the factor-6 point checked by the $G=1$ algebra. | Flaw 13 |
| Bogomolny bound $S_{\rm YM}\ge(8\pi^2/g^2)|k|$ with equality for (anti-)self-dual connections; Weinberg's theorem on interacting massless spin-1 | **Textbook; not searched this session.** | Flaws 4, 15, 16 |
| Repo-internal: `fpe-starobinsky-existence.md`, `fpe-starobinsky-coefficient.md`, `fpe-fixed-point-is-inflationary.md`, `fpe-constant-h-rigidity.md`, `ce-euclidean-vacuum-at-fixed-point.md`, the two March 2026 explorations, `asselmeyer-maluga-verification.md` | Read this session. | Throughout |
