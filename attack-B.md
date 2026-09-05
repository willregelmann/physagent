# Attack pass — Attempt B (precedent check, then dimensional transmutation on the Lorentzian branch)

**Target:** `/home/will/Projects/physagent/attempt-B-precedent-transmutation.md`
**Date:** 2026-09-05
**Role:** Attack (Pass 1 of "No Idea Is Eliminated Without a Defense"). No verdict is rendered here; every item is written so the steelman can try to rescue it.

Line numbers below refer to the attempt file. Scripts and outputs are inline; PDFs of HHH 2008, HHR 2001, Álvarez-Luna et al. 2023, Di Tucci–Lehners 2019, Ji 1995 and Asselmeyer-Maluga–Król 2018 were fetched and text-extracted this session (quotes are from the extracted text).

---

## Flaws

### 1. The "flat modulus" claim is false: the cap weight depends on $g^2$ perturbatively, not only through instantons
- **Location:** line 50 ("its coupling enters the saddle action only through instanton sectors"), line 52 ("the no-boundary weight is flat in $g^2$ to that accuracy… the sharpest form of the position"), line 85 (kill condition 1: "the $g$-dependence of the no-boundary weight is $O((\Lambda_{\rm QCD}a_0)^{b_0}) \sim 10^{-120}$").
- **Flaw:** The instanton identity bounds only the $k\neq0$ sectors; the $k=0$ sector's effective action on $S^4$ depends on $g^2$ from two loops on, polynomially, so the $g$-dependence of the weight is $O(1)$–$O(N_c^2)$ in the exponent, roughly $10^{120}$ times larger than claimed.
- **Evidence:** (i) Standard perturbation theory: the two-loop vacuum diagrams of Yang–Mills on a sphere of radius $a_0$ give a free-energy term $\delta I = g^2(1/a_0)\,N_c(N_c^2-1)\,\kappa$ with $\kappa$ a pure number (the only scale is $a_0$, and $\int_{S^4}\sqrt g\,a_0^{-4}=8\pi^2/3$). With $g^2\approx0.29$, $N_c=3$ this is $O(1)$–$O(10)$ in the exponent of the weight: not flat. (ii) The closest exactly solvable case, $\mathcal N=4$ SYM on $S^4$, localizes to a Gaussian matrix model (Pestun, Commun. Math. Phys. 313, 71 (2012), arXiv:0712.2824 — existence verified by search; formula from memory) whose $g$-dependence is a power of $g^2$, and Gerchkovitz–Gomis–Komargodski (JHEP 11 (2014) 001, arXiv:1405.7271 — verified by search) show the finite part of even-dimensional sphere partition functions is scheme-dependent through local counterterms, so the coupling-dependence of the weight is not even a scheme-independent quantity absent extra symmetry. (iii) The gauge term of the anomaly itself contributes on the cap: $\langle\tfrac{\beta}{2g}F^2\rangle_{S^4} = -\tfrac{b_0 g^2}{16\pi^2}\langle F^2\rangle_{S^4}\neq0$ with $\langle F^2\rangle_{S^4}\propto N_v a_0^{-4}$, i.e. a $g^2$-dependent shift of $H_0^2$ of relative size $b_0 g^2/16\pi^2 = 7\times0.285/158 \approx 1.3\%$; small, but it contradicts "the curvature part fixes $H_0$" as a $g$-independent statement and "flat".
- **Severity:** structural (this is the sentence the attempt calls its sharpest form).

### 2. Even if flat, "the root weights $g^2$ flatly" has no referent; and where the weight *does* act on a modulus, the attempt's own precedent says it selects an extremum
- **Location:** line 52; §4.1 (line 85).
- **Flaw:** In the no-boundary state $g^2$ is a parameter of the action, not a South-Pole datum like HHH's $\phi_0$; the wave function is a functional of boundary fields, and there is no measure over $g^2$ for the cap to be flat in — the statement is vacuous unless $g^2$ is promoted to a field (dilaton), in which case flaw 1 applies and the only precedent the attempt itself lists for a weight acting on a scale-setting modulus (Baum–Hawking/Duff, line 23) is that the weight drives the modulus to an extremum.
- **Evidence:** The attempt's kill condition 1 ("a proof that the cap must weight $g^2$ nontrivially… I see no candidate") is therefore not a remote possibility but the default once "modulus" is given any operational meaning; HHH 2008 (verified) shows the weight $\exp(-2I_R)$ with $I_R\approx-\pi/(2(H\mu\phi_R(0))^2)$ (their eq. 5.6) selecting the *lowest* available scale — the same mechanism would select $g^2$ to whatever extremizes $\delta I(g^2)$, not leave it free.
- **Severity:** structural.

### 3. "The junction fixes $\mu_* = H_0$ (Rigorous)" is empty: $\Lambda_{\rm QCD}$ is RG-invariant, and the instanton identity holds at every $\mu$
- **Location:** lines 48–52 (item (i); the boxed identity; "the cap 'knows' the hierarchy only as the exponential smallness of its own topological sectors").
- **Flaw:** $\Lambda_{\rm QCD}=\mu\,e^{-8\pi^2/(b_0g^2(\mu))}$ is independent of $\mu$ at one loop by construction; choosing to quote the coupling at $\mu=H_0$ fixes nothing physical, and $e^{-8\pi^2|k|/g^2(\mu)}=(\Lambda_{\rm QCD}/\mu)^{b_0|k|}$ is true for any $\mu$ — the cap "knows" the hierarchy exactly as much as any other scale does.
- **Evidence:** With the attempt's own numbers, if $g^2(H_0)$ were $1$ instead of $0.29$ the instanton weight would be $10^{-34}$ and $\Lambda_{\rm QCD}\approx10^{11}$ GeV; nothing about the cap changes. The whole hierarchy sits in the input $g^2(H_0)$; the attempt's §4 (line 90) concedes this, but §2 presents (i) as a "Rigorous" thing the junction fixes.
- **Severity:** structural / presentational.

### 4. Importing a gauge group and representations violates the letter of Axiom 2, and the attempt contradicts itself on whether this is new input
- **Location:** line 50 (item (ii), "Rigorous, standard"); §3 bullet 4 (line 81: "This is *not* new input relative to the paper… But $b_0$ needs the group and representations, which $a, c$ do not").
- **Flaw:** $a, c$ need only the spin counts $(N_s, N_D, N_v)$; $b_0$ needs $C_2(G)$ and $T(R)$ for a specific group and representations — the axiom text says "no assumed symmetry group", so this is exactly the category of input the paper forbids, and the bullet that says "not new input" concedes in its next sentence that it is.
- **Evidence:** `programs/co-emergence/index.tex:173-179` (Axiom `ax:nobackground`: "no fixed metric, no preferred foliation, no assumed symmetry group… matter both emerge from topology (Conjecture)"); `index.tex:1270-1275` (the paper states Conjecture 2 "does not derive the field content, the curvature coupling constants, the mass spectrum, or fermion masses"). "The junction fixes $b_0$ once a group is specified" means the specification fixes it, not the junction.
- **Severity:** axiom.

### 5. Double standard: HHH is dismissed as "a modulus needing input $m$", but the attempt's scale needs input $g^2(H_0)$ with the same logical status
- **Location:** line 13 (verdict on HHH: "built from the input $m$… Nothing below the inputs is generated"); line 9 and line 46 ("the hierarchy is generated on the branch"); line 90 (concession).
- **Flaw:** By the criterion the attempt applies to HHH, transmutation also generates nothing below its inputs — $\Lambda_{\rm QCD}$ is a function of the input $g^2(H_0)$ exactly as $H_{\rm eff}$ is of $m$; the only difference (exponential vs. polynomial sensitivity to the input) is a property of QCD, established in flat space, with no dependence on the cap, the junction, or the branch.
- **Evidence:** The attempt's own §4 line 90 ("relocates… to where does $g^2(H_0)\approx4\pi/44$ come from"). The honest answer to the question posed ("can the branch structure generate any scale other than $\Lambda^{1/2}$?") is therefore *no*, and the "commit" is really adaptation (1)–(3).
- **Severity:** structural / scope.

### 6. "Branch long enough" is argued from the wrong model, and in the repo's model the branch's de Sitter phase is $10^{16}$–$10^{18}$ times shorter than $1/\Lambda_{\rm QCD}$
- **Location:** §3 bullet 3 (line 80: "proper length $\gg 1/\Lambda_{\rm QCD}\approx10^{20}a_0$… HHH's classicality condition guarantees long-lived classical branches"); §4.3 (line 87: "HHH [1] rules this out").
- **Flaw:** HHH's classicality is the WKB gradient condition (3.13) for scalar-driven minisuperspace histories with $\mu>3/2$ and says nothing about duration or post-inflationary evolution; the cap the question actually posits (the repo's Starobinsky/HHR instanton) has a de Sitter branch that is unstable with lifetime $10^{-42}$–$10^{-40}$ s, versus $1/\Lambda_{\rm QCD}=2.6\times10^{-24}$ s, so confinement is not a property of the branch off this junction but of the FRW region reached only through the instability and reheating.
- **Evidence:** HHH 2008 extracted text line 457: "$|\nabla_A I_R|\ll|\nabla_A S|$ (3.13)"; HHR 2001 extracted text lines 156–160 (verified): "Starobinsky showed that the de Sitter solution is unstable, but could be long-lived, and decays into a matter dominated FRW universe… This inflation would be followed by particle production and (p)reheating"; repo: `programs/fixed-point-existence/claims/fpe-fixed-point-is-inflationary.md` (lifetime $10^{-42}$–$10^{-40}$ s), `programs/co-emergence/claims/ce-euclidean-vacuum-at-fixed-point.md` (gate: "the exact eternal solution is unstable… INDEPENDENTLY FATAL as a physical claim"), `programs/fixed-point-existence/index.tex:124,160` ("Only existence of the exact fixed point is relied upon"). Also the number: $H_0/\Lambda_{\rm QCD}=4\times10^{16}/0.25=1.6\times10^{17}$, so the branch must be $\gtrsim10^{17}a_0$, not $10^{20}a_0$.
- **Severity:** structural (the mechanism runs on a branch evolution the repo has no result about) plus factual (the $10^{20}$).

### 7. The state in which $\langle F^2\rangle$ must be evaluated is not the one cap regularity fixes
- **Location:** §3 bullet 1 (line 78: "the no-boundary condition fixes the branch's mode functions in the Euclidean ground state [3], so the vacuum on the branch is fixed by cap regularity"); §4.2; §6 "The state".
- **Flaw:** The gluon condensate that gives hadron mass is the non-perturbative IR vacuum at curvature $\ll\Lambda_{\rm QCD}^2$, reached after exit and reheating through a thermal QCD plasma cooling through $T_c$; the Euclidean ground state at the junction is the perturbative vacuum of a sector that is effectively conformal there, and Halliwell–Hawking 1985 concerns the ground state of inhomogeneous scalar/metric modes at the pole — nothing in it, or in the repo, carries a state through an instability exit and reheating.
- **Evidence:** HHR 2001 conclusion (extracted lines 1966–1968, verified): "During the de Sitter phase, particle masses would have been small compared with the space-time curvature so matter fields would have been classically conformally invariant"; HH 1985 abstract (verified via APS/PubMed listing): "inhomogeneous or anisotropic modes start off in their ground state… until their wavelength exceeds the horizon size… then amplified" — the body treats a massive scalar plus metric harmonics, no gauge sector (from my reading of the paper's structure; abstract only re-verified this session). The repo's own record of the Euclidean vacuum at the fixed point (`ce-euclidean-vacuum-at-fixed-point.md`) is a Conjecture whose instability gate is marked fatal for physically realised backgrounds.
- **Severity:** structural / axiom (the state is fixed by dynamics the attempt calls "not used").

### 8. OS reconstruction is reinstated as the *mechanism* supplying the branch state, the use the March debate killed; and the Lorentzian form factor is not foliation-free
- **Location:** §4.2 (line 86: "The state in which $\langle F^2\rangle$ is defined is supposed to come from Osterwalder–Schrader reconstruction across the junction"); §3 bullet 1 (line 78: "$\log(\Box/\mu^2)$… defined on the block without a foliation"); §3 bullet 3 (Halliwell/Banks "orthogonal").
- **Flaw:** The surviving verdict of `2026-03-02-signature-mass-codependence.md` is "OS-as-mechanism dead (background dependence), OS-as-evidence alive in the flat-space limit", and `index.tex:1815-1840` says the same; the attempt makes OS across a curved $K=0$ junction the source of the state. Separately, $\log(\Box/\mu^2)$ is unambiguous only on the elliptic cap; on the Lorentzian branch it requires a Green's-function prescription (Feynman, retarded/in-in), which is a time orientation — so the branch-side running is not "defined on the block without a foliation", and the Halliwell/Banks question is not orthogonal.
- **Evidence:** Exploration cited above ("What does not survive: 1. OS reconstruction as the signature bridge mechanism"); `index.tex:1826-1831` ("the OS axioms require a flat Euclidean background with $E(4)$ invariance… the reflection hyperplane defines a preferred direction that becomes time"). The Lorentzian-prescription point is standard nonlocal-effective-action lore (Barvinsky–Vilkovisky in-in form factors); no citation verified this session.
- **Severity:** axiom.

### 9. Scope: the mechanism produces $\Lambda_{\rm QCD}$ only; the electroweak scale and every fundamental-particle mass are outside it, and §6 does not say so
- **Location:** line 9 ("the hierarchy is generated on the branch"); line 43 ("(mass terms)" in the anomaly); §6 "Two meanings of mass" (line 108).
- **Flaw:** Transmutation gives hadron masses; the Higgs vev $v=246$ GeV — hence $m_W, m_Z, m_h$, all current quark masses, charged-lepton masses, and neutrino masses (Dirac or seesaw) — is an input mass parameter in the Standard Model, not a transmuted scale, and its hierarchy to $H_0$ ($\sim10^{-14}$) is untouched; the "(mass terms)" on line 43 silently carries the whole problem, and §6 lists only $m_{\rm eff}$ and $\Lambda_{\rm QCD}$ as the two meanings.
- **Evidence:** The attempt's own criterion at line 19 ("answers 'where does $M_P$ come from,' not 'why is $m\ll M_P$'") applied to itself: it answers "why $\Lambda_{\rm QCD}\ll H_0$ given $\alpha_s(H_0)$", not "why particle masses $\ll$ junction scale". The March synthesis split it invokes (line 52) explicitly says the spectrum "may require additional input (field content, coupling constants)" — the attempt supplies one such input and calls the result generation.
- **Severity:** scope.

### 10. The HHR "precedent" is already in the repo, and the consequence it actually carries is missed: the fixed point needs *conformal* matter, and an asymptotically free sector is not conformal
- **Location:** §1(e)(i) (line 23), precedent-table row "Hawking–Hertog–Reall 2001", line 49 ("$H_0\sim M_P/\sqrt{|a_2|}$ (coefficient Sketch)").
- **Flaw:** The repo records HHR 2001 with full text (`fpe-constant-h-rigidity.md`: instanton radius fixed by $N$, "no continuous modulus… the claim should cite HHR"; `fpe-starobinsky-existence.md`; `fpe-fixed-point-is-inflationary.md`), so the precedent check adds nothing; what it should have flagged is that HHR use $\mathcal N=4$ SYM *because* the anomaly-driven de Sitter solution is a conformal-matter result (repo hypothesis "conformal matter with a2 > 0"), whereas a sector with $\beta\neq0$ on the cap has $\langle T^\mu{}_\mu\rangle\supset\tfrac{\beta}{2g}\langle F^2\rangle\neq0$ (flaw 1(iii)), so the Rigorous-by-citation existence result does not cover the field content the attempt needs on the cap. Further, the exit the attempt needs (flaw 6) requires the $\Box R$ coefficient $d<0$, set by an $R^2$ counterterm — an input beyond $(\Lambda, G, a, c)$.
- **Evidence:** HHR extracted lines 328–336 (footnote 3: "We shall often refer to the $\mathcal N=4$ Yang-Mills theory as a CFT even though it is not conformally invariant on the four sphere"; "If $d=0$ then inflation never ends… We shall therefore include the finite counter term"); lines 1975–1977 ("In order for the de Sitter phase to be unstable, it is necessary for the coefficient $d$… to be negative… We therefore included a $R^2$ counterterm").
- **Severity:** structural.

### 11. The worked $H_0$ drops the $180\pi$ and misattributes the result to "the paper's own convention"
- **Location:** line 54 ("$H_0\sim10^{-2.5}M_P\approx4\times10^{16}$ GeV (the repo's $M_P/\sqrt{|a_2|}$ with $a_2\sim10^5$ in the paper's own convention)").
- **Flaw:** The printed coefficient is $H_0^2=180\pi/(G|a_2|)$, so $a_2=10^5$ gives $H_0=\sqrt{180\pi/10^5}\,M_P=0.075\,M_P\approx9\times10^{17}$ GeV, not $10^{-2.5}M_P$.
- **Evidence:**
  ```
  a2=1e5: H0=MP/sqrt(a2)=3.858e16 GeV, ln(H0/LQCD)=39.6
          with 180pi: H0=9.174e17 GeV, log10(H0/MP)=-1.12, ln(H0/LQCD)=42.7
  ```
  Effect: $\alpha_s(H_0)$ required becomes $1/47$; inside the attempt's own $\pm3$ tolerance (line 104), so the conclusion survives, but the attribution is wrong and the Sketch coefficient (`fpe-starobinsky-coefficient.md`, possible extra $16\pi$, dimensional defect) is not what was used.
- **Severity:** factual (minor).

### 12. The "self-consistent with known physics" check is tautological and uses the wrong $\Lambda$
- **Location:** lines 54–63.
- **Flaw:** Plugging $\Lambda_{\rm QCD}=0.25$ GeV into the one-loop formula with $b_0=7$ *is* the one-loop running of $\alpha_s$, so agreement with "$\alpha_s$ near the GUT scale" is guaranteed; it is evidence about QCD, not about the junction. Also $0.25$ GeV is $\Lambda^{(3)}$-like; with $n_f=6$ the one-loop $\Lambda^{(6)}\approx0.04$–$0.09$ GeV (shifts $\ln$ by $\sim1$–$2$).
- **Evidence:** Independent one-loop run from $\alpha_s(M_Z)=0.118$ with $n_f=5$ to $m_t$ then $n_f=6$:
  ```
  mu=4.0e16 GeV: 1/alpha_s = 46.1 ; mu=9.0e17: 49.6 ; mu=1.2e19: 52.5
  one-loop Lambda^(6) from alpha_s(m_t) = 0.043 GeV
  ```
  versus the attempt's required $1/44$ at $4\times10^{16}$ GeV.
- **Severity:** presentational.

### 13. HHH readings: a factor 6 in $H_{\rm eff}^2$ and a dropped $\mu>3/2$ qualifier
- **Location:** line 13 ("$H_{\rm eff}^2\simeq\Lambda/3+m^2\phi_0^2/6$"; "Classicality at late times… requires $\phi_0>\phi_0^c$").
- **Flaw:** In HHH's variables ($\phi=(4\pi/3)^{1/2}\Phi$, $G=1$; their eq. 4.3b) the effective cosmological constant is $3m^2\phi_R(0)^2$ (their text after eq. 5.6), so $H_{\rm eff}^2=\Lambda/3+m^2\phi_0^2$ — the $/6$ is the reduced-Planck-unit expression for a different normalization. And the lower bound $\phi_0^c$ exists only for $\mu>3/2$ models; for $\mu<3/2$ "$\gamma$ remains finite for all $\phi_0$".
- **Evidence:** HHH extracted lines 649–665 (units, eq. 4.3), 911–915 (eq. 5.6 and "effective cosmological constant $3m^2(\phi_R(0))^2$"), 958–965 (Fig. caption: "$\mu<3/2$ models… where $\gamma$ remains finite for all $\phi_0$… $\mu>3/2$ models… $\gamma$ diverges at a critical value $\phi_0^c$… tends to 1.27 as $\Lambda\to0$, independently of the value of $m^2$").
- **Severity:** factual (minor; the "modulus, not hierarchy" verdict is unaffected).

### 14. Citation content: Ji 1995 says the anomaly term is one quarter of $M_N$ in the chiral limit, not its "chiral-limit value"
- **Location:** line 44 ("Ji's decomposition [12], in which the nucleon mass $M_N=\langle N|T^\mu{}_\mu|N\rangle$ receives its chiral-limit value from the anomalous term"); reference 12.
- **Flaw:** Ji's Hamiltonian decomposition assigns the trace-anomaly piece $(1-b)/4$ of the mass, exactly $M/4$ in the chiral limit, the rest being quark and gluon kinetic/potential energy; the "whole mass from the anomaly via the trace identity" statement is the Shifman–Vainshtein–Zakharov-type argument, i.e. reference 11, which the attempt says it did not re-read and "leans on [12] instead".
- **Evidence:** Ji extracted text line 233: "from the trace anomaly. It contributes $(1-b)/4$ fraction of the mass"; line 329: "In the chiral limit, the gluon energy from the trace anomaly ($M/4$)…"; line 389 (table): "trace anomaly … $(1-b)/4$ … 190 … 210 [MeV]". The physical point (all terms scale with $\Lambda_{\rm QCD}$) survives; the attribution does not.
- **Severity:** factual (citation content mismatch on a load-bearing reference).

### 15. Adaptation (2) is a loose analogy to Di Tucci–Lehners and, taken literally, adds a parameter rather than fixing $g^2$
- **Location:** §5 item 2 (line 97).
- **Flaw:** DTL's Robin term is $S_{\rm tot}=S+\alpha q_0+q_0^2/(2\beta)$ on the *squared scale factor* $q$ at the initial surface, with $\alpha$ forced to $-6\pi^2 i$ by requiring a no-boundary saddle ($\bar q_0=0$) and $\beta$ a genuinely new parameter — it does not determine a bulk coupling, it introduces a boundary one. A gauge analogue faces three obstacles the attempt does not address: a boundary term quadratic in $A$ is not gauge-invariant; the gauge-invariant boundary functionals on a 3-surface (Chern–Simons, or a self-duality relation $E^i=\kappa B^i$) carry $\theta$-type data, not $1/g^2$; and $1/g^2$ multiplies a *bulk* term, which no boundary datum sets. So (2) is precisely "add one more input", and not the input needed.
- **Evidence:** DTL extracted lines 41, 131–150 (verified): "$q(t)$ is the squared scale factor, while $N(t)$ is the lapse"; "$S_{\rm tot}=S+\alpha q_0+\frac{q_0^2}{2\beta}$"; "$B\equiv\frac{3\pi^2}{N}\dot q_0+\alpha+\frac{q_0}{\beta}=0$"; "the initial size $\bar q_0$ vanishes at one (or more) of the saddle points if $\alpha=\pm6\pi^2 i$… we will consider $\alpha=-6\pi^2 i$". The gauge-invariance/$\theta$ observations are my construction (standard, but no citation verified this session).
- **Severity:** structural (for the adaptation).

### 16. Adaptation (1) is disconnected from anything the repo established, and the one published attempt in exactly this direction was missed and uses a non-exponential mechanism
- **Location:** §5 item 1 (line 96: "the Asselmeyer-Maluga direction… the adaptation I recommend pursuing: a self-consistency condition at Level 1 that fixes $g^2(H_0)$, tested by whether it lands within a factor $\sim2$ of $1/44$"); §1(e) (line 23: "no result deriving a particle-mass hierarchy from a no-boundary or tunneling geometry").
- **Flaw:** The repo's record on this direction is negative for reliance (synthesis Verdict 1: "Can we rely on it? No"; verification report Claim 6 "UNVERIFIED… Do NOT cite Mostow rigidity → mass"), and no candidate Level-1 quantity that could evaluate to $\approx0.29$ is named, so the "falsifiable target" has nothing to falsify. Moreover Asselmeyer-Maluga–Król have published a derivation of a two-scale hierarchy (GUT $\approx0.67\times10^{15}$ GeV, electroweak) and neutrino masses from Chern–Simons invariants of Brieskorn spheres in exotic $S^3\times\mathbb R$ — the precedent for adaptation (1) — and their scale formula is $\Delta E=E_{\rm Planck}/(1+\vartheta+\vartheta^2/2+\vartheta^3/6)$, a truncated polynomial in a topological number, not $e^{-1/g^2}$ and not a gauge coupling. Silence would not be a flaw; recommending a direction whose only published instance produces scales by a different mechanism, without checking it, is.
- **Evidence:** `programs/co-emergence/explorations/2026-03-03-mass-gap-synthesis.md` (Verdict 1); `programs/co-emergence/explorations/asselmeyer-maluga-verification.md:114-133, 224-246`; T. Asselmeyer-Maluga, J. Król, "A topological approach to Neutrino masses by using exotic smoothness", arXiv:1801.10419 (full text fetched this session; abstract and eqs. (3)–(4) at extracted lines 34, 355–372; journal version not verified).
- **Severity:** structural (for the adaptation).

### 17. The junction-number table omits the one dimensionless datum a gauge sector on $S^4$ actually carries: $\theta$
- **Location:** §2 table (lines 65–74); §5 item 1 ("instanton number is $c_2$… a topological datum; the *coupling* is not").
- **Flaw:** Once instanton sectors on the cap are invoked (line 50) the weight is $\sum_k e^{ik\theta}e^{-8\pi^2|k|/g^2}(\ldots)$ and $\theta$ is a further input of the same sector; the attempt's accounting of inputs ($\Lambda, G$, then $g^2$) is short by one, and the only topological/boundary quantities it can point to (flaw 15) are $\theta$-type, which do not set $\Lambda_{\rm QCD}$.
- **Evidence:** Standard; no citation needed. The table's own arithmetic is correct (see "Claims that held").
- **Severity:** scope (minor).

### 18. "$^{(3)}R=6/a_0^2=2\Lambda_{\rm eff}$, a covariant scalar" is the intrinsic curvature of the one distinguished hypersurface
- **Location:** line 48.
- **Flaw:** $^{(3)}R$ is a scalar *on* $\Sigma$, not a 4-scalar (the 4-scalar is $R=4\Lambda$); the matching is foliation-free only because the setup hands the attempt one preferred surface, which should be said rather than hidden behind "covariant".
- **Evidence:** Arithmetic itself is right (round $S^3$ of radius $a_0$: $^{(3)}R=6/a_0^2$; $\Lambda=3/a_0^2$).
- **Severity:** presentational.

### 19. The Fradkin–Tseytlin row repeats flaw 1 at lower stakes and omits the Avramidi–Barvinsky correction
- **Location:** line 21 ("on a conformally flat cap… that coupling does not even enter the saddle action, so the cap cannot weight it"); references 13–14.
- **Flaw:** $C^2$ vanishes classically on $S^4$, but the two-loop effective action depends on $f_2^2$ (same argument as flaw 1); and Avramidi–Barvinsky 1985 corrected the FT one-loop coefficients (the $R^2$-sector coupling is not asymptotically free in the corrected result) — the attempt cites both as if concordant. Second half from memory; not re-verified this session.
- **Severity:** factual (minor; the row is not load-bearing).

### 20. "Time sneaking in": the argument does depend on the branch's evolution even though it disowns the time parameter
- **Location:** §3 bullet 3 (line 80).
- **Flaw:** "RG time is not cosmic time" is correct, but the physical content of confinement requires a region of the block where the curvature has fallen by $\sim34$ orders relative to the junction ($H_0^2/\Lambda_{\rm QCD}^2\approx2.6\times10^{34}$), which in the repo's model exists only via Starobinsky's instability and exit — the dynamics the fixed-point program explicitly does not use — so the mechanism's location on the block is fixed by an evolution the attempt calls "not used".
- **Evidence:** See flaw 6 evidence; `programs/fixed-point-existence/index.tex:160`.
- **Severity:** axiom (Axiom 1 / hidden evolution), overlapping flaw 6.

---

## Claims that held

- **All numbers in §2 reproduce.** Script and output:
  ```
  attempt's H0 = 4e16 GeV: ln(H0/LQCD) = 39.61
  b0=7 (nf=6): g2 = 0.285, alpha_s = 0.0227 = 1/44.1
  mu=MP: ln = 45.33, alpha_s = 1/50.5
  instanton weight exp(-b0*ln) -> log10 = -120.4
  G*Lambda_eff = 3.0e-5 ; ln(3pi/(G Lambda)) = 12.66 ; 3pi/(G Lambda) = 3.1e5
  exp(-1/(G Lambda)) -> log10 = -14476 ; exp(-12.66) -> 10^-5.5
  SM a = 2.77-2.81, c = 2.36-2.43 (N_s=4, N_D=22.5 or 24, N_v=12)
  g2 = 1/a = 0.357: exp(-8pi^2/(b0 g2)) -> 10^-13.7
  ```
  Also $\xi f^4\sim10^{-33}$ for $m_S/M_P\sim10^{-17}$ from eq. (3.21): holds.
- **The one-loop identity** $e^{-8\pi^2|k|/g^2(\mu)}=(\Lambda_{\rm QCD}/\mu)^{b_0|k|}$ holds (it is a tautology of the one-loop definition, at any $\mu$ — see flaw 3 for what that implies).
- **Reading of HHH 2008:** condition (3.13), $\phi_0^c\to1.27$ independent of $m^2$, eq. (5.6) for $I_R$, the "$3m^2(\phi_R(0))^2$" identification, and "without further constraints the NBWF universally favors histories with $\phi_0$ near the lower bound $\phi_0^c$" are all verbatim in the paper. The verdict "modulus, not hierarchy" is correct.
- **Reading of Álvarez-Luna et al.:** Lagrangian (3.1), $\bar M_{\rm Pl}^2=\xi\langle\phi\rangle^2$, and $m_S^2=\frac{\bar M_{\rm Pl}^2}{8\pi^2}\xi(9f_0^4\xi^2+4f_0^4+20f_2^4)$ (their 3.21) are exactly as quoted; the "loop factor, not exponential" verdict is correct.
- **Tree partial order not used:** checked; the transmutation argument never invokes the rooted-tree orientation. (It does invoke branch evolution — flaw 6/20 — which is a different thing.)
- **$^{(3)}R=6/a_0^2=2\Lambda_{\rm eff}$, $\mu_*=a_0^{-1}=H_0$:** arithmetic holds.
- **The relocation concession (§4, line 90)** is honest and, in my reading, is the actual result of the attempt.
- **The negative arithmetic in the junction-number table** (no combination of $G\Lambda$, $\ln(3\pi/G\Lambda)$, $a$, $c$ gives $\ln\approx39$) holds; I tried $\ln(1/G\Lambda)=10.4$, $\sqrt{1/G\Lambda}=183$, $a\cdot c$, $a/c$, $2\pi a$: nothing lands near 39 either.
- **Halliwell–Hawking 1985** is correctly summarized at the abstract level.

## Citations re-verified (content, not just existence)

| Ref | Outcome |
|---|---|
| [1] HHH 2008, PRD 77, 123537, arXiv:0803.1663 | **Verified, full text.** (3.13), 1.27, (5.6), "$3m^2(\phi_R(0))^2$", "universally favors… $\phi_0^c$" all present. Attempt's $H_{\rm eff}^2$ has a factor 6 and omits the $\mu>3/2$ qualifier (flaw 13). |
| [2] HHH 2008, PRL 100, 201301 | Existence verified via [1]'s abstract ("heavily biased towards small amounts of inflation"); PRL itself not fetched. |
| [3] Halliwell–Hawking 1985, PRD 31, 1777 | **Verified, abstract** (APS/PubMed listing). Body content (scalar+metric harmonics only, no gauge sector) from my reading, not re-fetched. |
| [4] Coleman–Weinberg 1973 | Not re-verified this session (textbook; not load-bearing). |
| [5] Álvarez-Luna et al., JHEP 2023, 232, arXiv:2212.01785 | **Verified, full text.** Eqs. (3.1), (3.20)–(3.21) exactly as quoted. |
| [6] Riegert 1984 | Existence and abstract-level content verified by search. |
| [7] Antoniadis–Mottola 1992 | Existence and abstract-level content verified by search. |
| [8] AMM 1992 | Not re-verified this session (not load-bearing). |
| [9] Barvinsky–Wachowski 2023, PRD 108, 045014, arXiv:2306.03780 | **Verified, abstract.** "exhibits a kind of a metamorphosis to the nonlocal form factors of the so-called partners" present; the attempt's polarity reading (form factors, not transmutable running) is consistent with the abstract. |
| [10] Collins–Duncan–Joglekar 1977, PRD 16, 438 | Existence verified; abstract-level content ("form of the anomaly in the trace… interacting fermions and non-Abelian gauge bosons") verified via OSTI listing. "Trace soft on shell iff at a zero of $\beta$" not re-read. |
| [11] SVZ 1978 | Not re-verified; the attempt itself flags it as not re-read — but it is the reference that actually supports the sentence at line 44 (flaw 14). |
| [12] Ji 1995, PRL 74, 1071, hep-ph/9410274 | **Verified, full text.** Decomposition as stated; anomaly share is $(1-b)/4$, $M/4$ in the chiral limit — **content mismatch** with the attempt's use (flaw 14). |
| [13] Fradkin–Tseytlin 1982 | Existence and abstract ("asymptotically free in all essential coupling constants") verified by search. |
| [14] Avramidi–Barvinsky 1985 | Not re-verified this session. |
| [15] HHR 2001, PRD 63, 083504, hep-th/0010232 | **Verified, full text.** Quote present verbatim in abstract. Additional content the attempt did not use: $\mathcal N=4$ SYM as (non-)CFT, instability and decay to FRW with (p)reheating, $R^2$ counterterm needed for exit (flaws 6, 7, 10). |
| [16] Feldbrugge–Lehners–Turok 2017 | Not re-verified this session (not load-bearing). |
| [17] Di Tucci–Lehners 2019, PRL 122, 201302, arXiv:1903.06757 | **Verified, full text.** Quote present verbatim; Robin term is on the squared scale factor $q_0$ with $\alpha$ fixed at $-6\pi^2 i$ (flaw 15). |
| [18] Baum 1983 / Hawking 1984 / Duff 1989 | Existence verified by search (titles, journals, pages). Duff's specific argument not re-read; the attempt's paraphrase is consistent with my recollection but unverified. |
| [19] Hartle–Hertog 2013, PRD 88, 123516, arXiv:1309.0493 | **Verified, abstract.** Anthropic conditioning on a landscape with varying $\Lambda$ and $Q$, as stated. |
| Extra (attack-side) | Pestun 2012 (CMP 313, 71; arXiv:0712.2824) and Gerchkovitz–Gomis–Komargodski 2014 (JHEP 11 (2014) 001; arXiv:1405.7271): existence and abstract-level content verified by search; used in flaw 1. Asselmeyer-Maluga–Król arXiv:1801.10419: full text fetched; used in flaw 16; journal version not verified. |
