# Attempt A — First-principles scale counting at the no-boundary junction

**Role:** Position agent (explorer fan-out, width 3). **Technique:** dimensional
and constraint counting of the junction data, with a worked numerical
estimate. **Committed position:** the branch structure by itself produces no
hierarchy; the exponent that a mass hierarchy needs is the *degree of
homogeneity* of a relation between junction curvature and a matter-side
quantity, and such a relation can only live in the *state on Σ*, not in the
geometry of Σ. That is a pointer, not a defeat.

Conventions: $\hbar = c = 1$; $M_P = G^{-1/2} = 1.22\times10^{19}$ GeV
(non-reduced; using the reduced mass shifts every exponent below by
$< 0.01$). $H$ denotes the Hubble rate of the de Sitter branch at the
junction; $\varepsilon \equiv (H/M_P)^2 = GH^2$. All "Rigorous" labels are
dimensional-analysis or constraint-counting statements unless stated.

---

## 1. The premise, made precise

**(Rigorous.)** The Hartle–Hawking state~[HH83] is
$\Psi[h_{ij},\phi] = \int \mathcal{D}g\,\mathcal{D}\phi\; e^{-I_E}$ with
$I_E = -\tfrac{1}{16\pi G}\int\sqrt{g}\,(R-2\Lambda) - \tfrac{1}{8\pi G}\oint\sqrt{h}\,K + I_{\rm matter}$.
The constants are $G$ **and** $\Lambda$ (plus matter parameters). Two
dimensionful constants of dimensions $[L]^2$ and $[L]^{-2}$ form exactly one
dimensionless ratio,
$$\varepsilon = \tfrac{1}{3}\Lambda\ell_P^2 = (H/M_P)^2, \qquad H^2 = \Lambda/3 .$$
So "the only dimensionful input is $\Lambda$" is true only in Planck units,
where it means: *every scale is $M_P \times F(\varepsilon)$ for some function
$F$*. The mass test is then the question of which exponents
$p$ in $m = M_P\,\varepsilon^{p}\times O(1)$ the junction can select. Two are
free: $p = 0$ ($M_P$) and $p = 1/2$ ($H$).

**(Rigorous.)** The dominant saddle for pure gravity $+\Lambda$ is the round
$S^4$ of radius $a_0 = \sqrt{3/\Lambda} = 1/H$, cut at its equator
$\Sigma = S^3$. Its action is $I_E(S^4) = -3\pi/(G\Lambda)$ (with
$R = 4\Lambda$, ${\rm Vol}(S^4) = 24\pi^2/\Lambda^2$); the half-sphere has
$K = 0$ on $\Sigma$, so no boundary term, and
$$|\Psi_{HH}|^2 \sim e^{3\pi/(G\Lambda)} = e^{\pi/(GH^2)} = e^{\,S_{dS}},$$
$S_{dS}$ the Gibbons–Hawking horizon entropy~[GH77]. **The single
dimensionless number the Euclidean root carries is $1/\varepsilon \simeq
S_{dS}/\pi$**, and it enters exponentially.

**(Rigorous.)** In the framework's own version of the junction
(`programs/fixed-point-existence/index.tex`, `sec:starobinsky`), $\Lambda$ is
not input: the anomaly-driven de Sitter fixed point has
$H_0^2 \sim M_P^2/|a_2|$, so $\varepsilon_J \sim 1/|a_2|$ is *computed* from a
field-counting integer (coefficient Sketch and possibly off by $16\pi$; see
`claims/fpe-starobinsky-coefficient.md`). Thus the premise fails twice: there
are two scales, not one; and in this framework the ratio between them is an
output of field content, not a free constant.

### Worked numbers

Two junctions must be distinguished, because the repo already records that
they are different objects sixty orders apart
(`claims/fpe-fixed-point-is-inflationary.md`):

| Junction | $H_J$ | $\varepsilon_J$ | $\log_{10}\varepsilon_J$ |
|---|---|---|---|
| (i) HH with the observed $\Lambda$ | $1.4\times10^{-33}$ eV | $1.4\times10^{-122}$ | $-121.9$ |
| (ii) anomaly-driven (repo's fixed point), $a_2\in[10^3,10^5]$ | $10^{-1}$–$10^{-3}\,M_P$ | $10^{-2}$–$10^{-5}$ | $-2$ to $-5$ |
| (ii$'$) CMB-normalised Starobinsky inflation (external, for reference) | $\sim10^{13}$–$10^{14}$ GeV | $\sim10^{-11}$–$10^{-10}$ | $-11$ to $-10$ |

Required exponent $p = \log(m/M_P)/\log\varepsilon_J$:

| Mass | $m$ | $\log_{10}(m/M_P)$ | $p$ vs (i) | $p$ vs (ii), $\varepsilon_J=10^{-4}$ | $p$ vs (ii$'$), $\varepsilon_J=10^{-10}$ |
|---|---|---|---|---|---|
| $\rho_\Lambda^{1/4}$ | 2.2 meV | $-30.7$ | **0.252** | 7.7 | 3.1 |
| neutrino (heaviest, $\gtrsim$) | 0.05 eV | $-29.4$ | 0.241 | 7.3 | 2.9 |
| electron | 0.511 MeV | $-22.4$ | 0.184 | 5.6 | 2.2 |
| pion | 140 MeV | $-19.9$ | **0.164** | 5.0 | 2.0 |
| proton | 938 MeV | $-19.1$ | 0.157 | 4.8 | 1.9 |
| Higgs | 125 GeV | $-17.0$ | 0.139 | 4.2 | 1.7 |
| EW vev | 246 GeV | $-16.7$ | 0.137 | 4.2 | 1.7 |

Two data points stand out against junction (i). The Weinberg–Zel'dovich
relation $m^3 \simeq \hbar^2 H_0/(Gc) = M_P^2 H_0$~[W72, Z67] is *exactly*
$p = 1/6$ (it evaluates to 60 MeV; $A\approx 12$ for the pion — "order one"
only loosely). And $\rho_\Lambda^{1/4} = (3\Omega_\Lambda/8\pi)^{1/4}(M_P H_0)^{1/2}$
is *exactly* $p = 1/4$ — the neutrino/dark-energy coincidence. The electroweak
scale sits at $p\approx1/7$, matching no simple rational. I treat all three
as numerological data points, per the brief, and use them only to calibrate
what kind of exponent a mechanism would have to produce: **against (i),
small rational exponents $1/6$–$1/4$; against (ii), integer-ish exponents
$4$–$8$.** These are qualitatively different targets and the two junctions
cannot be conflated.

---

## 2. Exhaustive enumeration of junction data

The invariant junction data are $(\Sigma, h_{ij}, K_{ij}, \phi_A|_\Sigma,
\pi_A|_\Sigma)$ modulo ${\rm Diff}(\Sigma)$, subject to the Hamiltonian and
momentum constraints, plus the dimensionless parameters of the action. The
FLRW minisuperspace is used below only to *evaluate* each item; the count
itself does not assume a symmetry (Axiom 2, `ax:nobackground`).

| Datum | Dimensionful? | Selected or modulus? | Combination with $\varepsilon$ | Label |
|---|---|---|---|---|
| Intrinsic 3-geometry $h_{ij}$ of $\Sigma$; invariants ${}^{(3)}R = 6/a_0^2 = 2\Lambda$, ${\rm Vol} = 2\pi^2 a_0^3$ | yes: one length $a_0 = 1/H$ | selected by the saddle | ${}^{(3)}R\,\ell_P^2 = 6\varepsilon$; ${\rm Vol}/\ell_P^3 \sim \varepsilon^{-3/2}$ | Rigorous |
| Harmonic tower on $\Sigma$: scalar Laplacian eigenvalues $l(l+2)/a_0^2$; on the full $S^4$ cap, $(l(l+3) + m^2/H^2)H^2$ | yes: $H\sqrt{l(l+2)}$ | tower selected; **which $l$ is physical is not** | spans $H\cdots M_P$ at $l \sim \varepsilon^{-1/2}$; $\sim\varepsilon^{-3/2}$ modes below Planck cutoff | Rigorous (spectrum); "selection of $l$" is nothing |
| Extrinsic curvature $K_{ij}$ — HH case | $K = 0$ | forced: $K=0$ is the *reality condition* for a real Lorentzian continuation (FLRW: $a(\tau_0 + z)$ must be even in $z$) | none | Rigorous (FLRW); Sketch (general) |
| $K_{ij}$ — SCB weakened junction (bounded proper rate $\mathcal H_\Sigma = K_\Sigma/3$, note §2) | yes: $K_\Sigma$, a second length$^{-1}$ | **modulus** unless sourced; Hamiltonian constraint on $\Sigma$: $3\mathcal H_\Sigma^2 + 3/a_\Sigma^2 = 8\pi G\rho_\Sigma + \Lambda$ | $K_\Sigma/H$ free; $p_K = \log(K_\Sigma/M_P)/\log\varepsilon$ undetermined | Sketch |
| Matter values $\phi_{A,0}$ (HHH branch labels) | mass-dim 1, but a shift-symmetry modulus for free massless fields | modulus; becomes a scale only via $V(\phi)$ | $H(\phi_0)^2 = \tfrac{8\pi G}{3}V(\phi_0)$ — imports $V$'s scales | Rigorous |
| Matter momenta $\pi_A|_\Sigma$ | HH: $\pi = 0$ (same reality condition) | forced | none | Rigorous (FLRW) |
| Anomaly coefficients $a, c$ (field counting) | no | selected by field content | $\varepsilon_J \sim 1/a_2$ | Rigorous |
| Curvature couplings $\xi_A$; gauge/Yukawa couplings $g_i$ | no | moduli of the action | $m^2_{\rm eff} = 12(\xi - \tfrac16)H^2$ → $p = 1/2$ exactly (`eq:meff`, `conj:mass_generation`) | Rigorous (formula) |
| Lapse degeneracy order $n$ and coefficient $c$ in $\lambda \simeq -c\,{\rm sgn}(x^0)|x^0|^n$ | $c$ has dimension $[L]^{-n}$ but is **pure gauge** (below) | coordinate artifact | none | Rigorous |

**$n$ and $c$ are coordinate artifacts (Rigorous).** Under $x^0 \mapsto
\tilde x^0(x^0)$, $\lambda\,(dx^0)^2 = \tilde\lambda\,(d\tilde x^0)^2$. The SCB
note's own proper variable $u = \tfrac{2\sqrt c}{n+2}(x^0)^{(n+2)/2}$ turns the
metric into $-du^2 + a^2(u)\,d\vec x^{\,2}$ with no trace of $c$ or $n$; the
same on the Euclidean side with $v$. Every metric invariant is a function of
proper distances and therefore independent of $(n, c)$. What $(n, c)$ do encode
is the smoothness class of the *chart* across $\Sigma$: the glued proper
coordinate $\tilde u = {\rm sgn}(x^0)|u|$ is $C^{\lfloor (n+2)/2\rfloor}$ in
$x^0$. That is a statement about the atlas (Level 1 in the hierarchy), not
about any scale.

**The single Rigorous conclusion of the enumeration.** For pure gravity
$+\Lambda$ $+$ free conformal matter with the Hartle–Hawking junction, the
junction carries exactly one length ($a_0$) and one dimensionless number
($\varepsilon$), and every dimensionful junction quantity is
$M_P\,\varepsilon^{k/2}\times$(integer-valued function of field content) with
$k \in \{0, 1, 2, 3, \dots\}$ arising only from $a_0$, its volume, and the
harmonic tower. There is no tree-level junction quantity with $p \notin
\tfrac12\mathbb{Z}$, and none with $p = k/2$, $k \ge 2$, other than powers of
the volume (which are not masses).

**Independence from the root-uniqueness dispute (Rigorous, trivially).** The
count is per root. If the Euclidean integral has several saddles~[FLT17] or is
defined with Robin data~[DTL19], each junction carries the same enumerated data;
a forest counts like a tree. The mass test does *not* depend on the
experimenter's uniqueness premise — except in one place, §3(d) below, where
multiplicity is actually what would help.

---

## 3. What the WKB branch structure can do with the data

**(a) A continuum of branches is a spectrum, not a hierarchy (Rigorous).**
Hartle–Hawking–Hertog's classical branches~[HHH08] are labelled by $\phi_0$
with $H(\phi_0)^2 = \tfrac{8\pi G}{3}V(\phi_0)$ and no-boundary weight
$e^{+3\pi/(G H(\phi_0)^2)}$, favouring the *lowest* $H$. A hierarchy is a set of
fixed ratios; a modulus-labelled family gives none. Discreteness enters only
through discrete extrema of $V$, whose ratios are $V$'s own — imported, not
generated.

**(b) The tower gives a spectrum of scales $H\sqrt{l(l+2)}$ from $H$ to
$M_P$ (Rigorous), but nothing selects $l$.** A particle of mass $m$ would be
$l \sim m/H = \varepsilon^{p-1/2}$; for the electron against junction (i),
$l \sim 10^{39}$. A selection rule on $l$ is the missing ingredient, and pure
gravity has none.

**(c) Mass enters the cap as a dimensionless offset (Rigorous).** On $S^4$ the
spectrum of $-\Box + m^2 + \xi R$ is $\big(l(l+3) + 12\xi + m^2/H^2\big)H^2$.
The OS-reconstructed Hilbert space across $\Sigma$~[OS, already in the repo bib]
therefore encodes any mass only through $\delta = m^2/H^2$, a number that is
*zero for every geometric junction datum*. Light masses $m \ll H_J$ are
complementary-series representations, perfectly admissible on the Lorentzian
branch, but their $\delta$ must be supplied by the matter action. This is the
precise sense in which "the cap knows only $H$": not that it cannot host other
scales, but that it generates no $\delta \ne 0$.

**(d) Exponentially small numbers exist at the root, but only between saddles
(Sketch).** The one exponential the state carries is $e^{S_{dS}}$. A *ratio* of
saddle weights $e^{-\Delta I/\hbar}$, $\Delta I \propto 1/\varepsilon$, is the
only junction-native number of the form needed for a hierarchy; with
$\varepsilon_J \sim 10^{-2}$ and $\Delta I = c\,S_{dS}$, $M_P e^{-c S_{dS}}$
reaches $10^{-22}M_P$ (the electron) for $c \approx 0.16$. This is numerology,
but its *form* is the point: a hierarchy of this kind requires a second saddle
contributing to the same branch — the very multiplicity the tree argument
wants to exclude. Honest tension, recorded; not resolved here.

### Candidate structural condition that would fix $p$ — the homogeneity lemma

**(Rigorous, dimensional.)** Any relation homogeneous of degree $k$ of the
form $m^k = M_P^{\,k-j}H^{\,j}$ selects $p = j/(2k)$. So "what fixes $p$" is
"what fixes the degree of the relation defining $m$." Degree 1 ($m \propto H$)
is the framework's `eq:meff`, $p = 1/2$. Degree 2 ($m^2 \propto M_P H$) gives
$p = 1/4$. Degree 3 ($m^3 \propto M_P^2 H$) gives $p = 1/6$.

**(Sketch.)** The junction supplies one such relation for free: the
Hamiltonian constraint on $\Sigma$ with $K_\Sigma = 0$ and $a_\Sigma = 1/H$ reads
$\rho_\Sigma = \tfrac{3}{8\pi}M_P^2 H^2$ — the junction energy density is
$M_P^2H^2$, hence $\rho_\Sigma^{1/4} = M_P\varepsilon^{1/4}\times O(1)$. That is
*structurally* $p = 1/4$. Against junction (i) it is literally
$\rho_\Lambda^{1/4} = 2.2$ meV. Whether this is a *mass* depends on a
matter-side relation $\rho_\Sigma = \rho(m)$:
- $\rho = m^4$ (vacuum energy of a field of mass $m$ saturates the constraint):
  $p = 1/4$;
- $\rho = G m^6$ (Zel'dovich's gravitational self-energy of vacuum pairs
  \cite{Z67}, as quoted by Rugh–Zinkernagel): $p = 1/6$, the Weinberg relation.

So the candidate condition is: **the state on $\Sigma$ has a vacuum energy
$\langle T_{00}\rangle_\Sigma$ that (a) saturates the junction constraint and
(b) is a homogeneous function of a single matter scale.** (a) is the
framework's own SCE self-consistency evaluated *on $\Sigma$*; (b) is a
property of the OS-reconstructed state, i.e. Level-3 data. This condition
does not exist in the repo yet; what it would require is stated in §6(b).

**(Sketch.)** A second, weaker mechanism exists inside the paper's own
equations. Because $\beta_\xi \propto (\xi - \tfrac16)$ (`eq:beta_xi`),
$(\xi - \tfrac16)(\mu) \approx (\xi-\tfrac16)(M_P)\,(\mu/M_P)^{\gamma}$ with
$\gamma = [12\lambda + 2Y_2 - \dots]/16\pi^2 \approx 0.03$. Evaluating
`eq:meff` at $\mu = m_{\rm eff}$ gives $m^{2-\gamma} = 12(\xi_P - \tfrac16)H^2M_P^{-\gamma}$,
i.e. $p = 1/(2-\gamma)$. This is a genuine, framework-internal shift of the
exponent away from $1/2$ — but $p = 0.508$, not $5$; reaching $p = 5$ would
need $\gamma \approx 1.8$, a non-perturbative anomalous dimension for
$(\xi - \tfrac16)R\phi^2$. Named, and not available.

**(Sketch.)** The anomaly–decoupling bootstrap
$1/\varepsilon = \sum_i c_i\,f\!\big(m_i^2/(\varepsilon M_P^2)\big)$, $f(0)=1$,
$f\to0$ by decoupling (position-2 §5), is *one* equation in $N+1$ unknowns
$(\varepsilon, m_1,\dots,m_N)$. It fixes $\varepsilon_J$ given the spectrum; it
cannot fix the spectrum. Every hierarchy-generating condition must add $N$
equations, and the enumeration says the geometry of $\Sigma$ has none to add.

---

## 4. Table of candidate scales

| Candidate | How it arises | $p$ (rel. $\Lambda^{1/2}$, $M_P$) | What selects it | Status |
|---|---|---|---|---|
| $H_J$ | saddle radius $a_0$; anomaly fixed point | $1/2$ | field content via $a_2$ (framework) or $\Lambda$ (HH) | Rigorous (existence); coefficient Sketch |
| $m_{\rm eff} = \sqrt{12(\xi-\frac16)}\,H_J$ | `eq:meff` on the branch | $1/2$ | $\xi$, a modulus | Rigorous (formula) |
| $m_{\rm eff}$ with running $\xi$ | `eq:beta_xi` | $1/(2-\gamma) \approx 0.508$ | SM couplings at $M_P$ | Sketch |
| $H_J\sqrt{l(l+2)}$ | harmonic tower on $\Sigma$ | continuum from $1/2$ to $0$ | nothing selects $l$ | Rigorous (tower); Conjecture (selection) |
| $K_\Sigma$ | SCB junction with bounded $\mathcal H_\Sigma \ne 0$ | undetermined | matter density on $\Sigma$ via constraint; modulus otherwise; **$=0$ in HH by reality** | Sketch |
| $\rho_\Sigma^{1/4}$ | Hamiltonian constraint on $\Sigma$ | $1/4$ | automatic; is a *mass* only if $\rho_\Sigma = m^4$ (state-side) | Sketch |
| $(M_P^2H_J)^{1/3}$ | $\rho_\Sigma = Gm^6$ (self-energy relation) | $1/6$ | state-side relation; unverified mechanism | Conjecture |
| $M_P e^{-8\pi^2/(b g^2_\Sigma)}$ | dimensional transmutation of a marginal coupling at $\Sigma$ | not a power of $\varepsilon$ | $g_\Sigma$, a modulus; $b$ is field counting (same data as $a_2$) | Rigorous (mechanism, [CW73]); Conjecture (that $\Sigma$ fixes $g_\Sigma$) |
| $M_P e^{-c\,S_{dS}}$ | ratio of saddle weights | not a power of $\varepsilon$ | needs a second saddle on the branch | Conjecture |
| $H(\phi_0)$ | HHH branch label | continuum | $V(\phi)$, imported | Rigorous |

Reading down the "what selects it" column: **every entry with $p \ne 1/2$ is
selected by something that is either a modulus of the action or a property
of the state on $\Sigma$.** Nothing with $p \ne 1/2$ is selected by the
geometry of the junction.

---

## 5. Axiom check

- **Preferred foliation (Axiom 2).** $\Sigma$ is $\{\det g = 0\}$ in the
  degenerate-metric description (equivalently the totally geodesic equator,
  $K = 0$, in HH): the level set of a diffeomorphism-invariant scalar, exactly
  as a minimal surface or an apparent horizon is. A foliation is a
  one-parameter *family* with an ordering; a single surface selected by a
  scalar condition — including a self-consistency condition — is not one. What
  *would* violate the axiom is defining $\Sigma$ by a chart (“$x^0 = 0$”); §2
  shows the chart data $(n,c)$ drop out, so the SCB profile is a chart
  description of an invariant surface. Verdict: no smuggling, provided the
  selection condition is stated invariantly (it is, as $\det g = 0$ or
  $K = 0$).
- **Symmetry assumption.** The FLRW minisuperspace was used to evaluate, not
  to count. The count is invariant. But the *reality condition* $K=0$ was only
  derived in FLRW ("$a$ even in $z$"); its general form is Sketch, and with
  matter the HHH saddles are complex, so the real junction is the exception —
  the SCB program's real degenerate surface and HHH's complex saddle are
  different objects glued differently (junction conditions vs analytic
  continuation). Flagged, not resolved.
- **Time evolution (Axiom 1).** None used. The RG "running" of $\xi$ and $g$ is
  scale dependence of correlators on the block, not evolution. WKB time on a
  branch is the Hamilton–Jacobi flow, derived, consistent with the paper's
  Page–Wootters stance (`sec:coemergence`). The tree's root-ward order was not
  used in the count at all.
- **Preferred observer.** The static-patch temperature $H/2\pi$~[GH77] is
  observer-dependent and was deliberately not used; $S_{dS}$ was used only as
  the saddle action, which is invariant.
- **Background structure.** $G$ (equivalently $M_P$) remains the framework's
  one undischarged dimensionful input, and every $p$ above is measured
  against it. HH additionally inputs $\Lambda$; the framework replaces that
  with field content. The mass test is therefore, at bottom, a test of
  whether anything other than $M_P$ and integers is input.

---

## 6. Closing sections

### (a) What would kill this attempt

The position's positive content is the pointer "the exponent-fixing relation
lives in the state on $\Sigma$, not in its geometry." It dies if that pointer
is shown empty. The specific computation: run the framework's SCE
self-consistency *on $\Sigma$* for free conformal matter in the OS-reconstructed
state and show that $\langle T_{00}\rangle_\Sigma$ is *identically* the
anomaly-driven $\Lambda_{\rm eff}M_P^2/8\pi$, with no independent matter-side
relation $\rho(m)$ — i.e. that (a) and (b) of §3 collapse to a tautology
($\rho_\Sigma$ is $M_P^2H_J^2$ because $H_J$ was defined by $\rho_\Sigma$).
Combined with a demonstration that the SCB regular class forces $K_\Sigma \to 0$
dynamically (closing the $K_\Sigma$ row) and that no marginal coupling is
fixed at $\Sigma$ (closing the transmutation row), every $p \ne 1/2$ entry in
§4 is a modulus and the junction generates exactly one scale. That is a
finite computation; the first part is essentially the massless-limit
bootstrap that `2026-03-03-mass-gap-synthesis.md` lists as its highest
priority next step, evaluated at $\Sigma$.

### (b) If negative, the adaptation it points to

The second scale needed at the junction is **not a second dimensionful
constant**. It is one of three things, in order of how much they demand:

1. **A dimensionless marginal coupling $g_\Sigma$ at the junction, plus
   dimensional transmutation.** This is the only known mechanism that turns
   $O(1)$ dimensionless data into a hierarchy without tuning [CW73]. The
   $\beta$-function coefficient $b$ is field counting — the *same* data that
   fixes $a_2$ and hence $\varepsilon_J$ — so a single field content already
   determines both the junction scale and the *rate* of transmutation. What
   it does not determine is the initial condition $g(M_P)$. Where it would
   have to come from: a fixed-point condition on $g$ at $\Sigma$, of the same
   type as the framework's Level-2 fixed point (a UV-critical coupling
   selected by self-consistency rather than input). Nothing in the repo does
   this; it is the natural "Level-2 map extended to couplings" — the extended
   map $G(g,m_{\rm eff})$ that position-2 §3 already gestured at, with $g$
   now meaning a gauge coupling.
2. **A state-side relation $\rho_\Sigma = \rho(m)$** (§3), giving rational
   $p = 1/(2k)$. This needs the OS-reconstructed state on $\Sigma$ to be
   constructed explicitly (the reflection surface is $\Sigma$ itself, per the
   reframing), and its vacuum energy computed — Level-3 data, i.e. the
   repo's Open Problem 2 (`README.md`). It reproduces $p = 1/4$ and, via
   Zel'dovich's relation, $p = 1/6$ *against junction (i) only*; against the
   anomaly junction (ii) it yields Planck-adjacent scales and does nothing for
   the hierarchy. So this route is available only if the physically relevant
   junction is the low-$\Lambda$ one, which the repo's current fixed point is
   not.
3. **A nonzero $K_\Sigma$ under the SCB weakened junction**, sourced by a
   matter density on $\Sigma$. This is a second length, but a modulus unless
   (1) or (2) fixes the density. It is the cheapest formally and the emptiest
   physically.

The adaptation, stated once: *the junction must fix a coupling, not a
constant.* The reframing as it stands fixes only $\varepsilon_J$.

### (c) What is underspecified

- The Starobinsky coefficient is Sketch and dimensionally unconventional
  (`fpe-starobinsky-coefficient.md`); $\varepsilon_J$ is known only to within
  $\sim 16\pi$ and $a_2$ to two orders. The (ii) column of the exponent table
  moves by $\pm1$ accordingly.
- The reality condition $K = 0 \Leftrightarrow$ "$a$ even in $z$" is FLRW-only.
  Its covariant statement, and whether the SCB bounded-$\mathcal H$ class is
  compatible with *any* analytic-continuation gluing, is open.
- The decoupling function $f$ in the bootstrap was not computed; position-2's
  $(H/m)^4$ is unverified.
- Inhomogeneous junction data ($h_{ij}$ with structure) carry a spectrum of
  curvature radii; in HH these perturbations sit in their ground state
  (Halliwell–Hawking 1985 — **unverified**, not cited) and add no selected
  scale, but this was not checked here.
- The Károlyházy-type relation $\delta x^3 \sim \ell_P^2 L$, which would
  reproduce $p = 1/6$ from an uncertainty argument, is known to me only from
  memory (**unverified**, not cited) and was not used.
- Whether the OS reflection across a *derived* $\Sigma$ is even positive is the
  reframing's own open problem, prior to anything here.

---

## References (all web-verified 2026-09-05 unless marked)

- [HH83] J. B. Hartle and S. W. Hawking, "Wave function of the Universe,"
  Phys. Rev. D **28**, 2960 (1983). Verified: authors, title, venue, year;
  supports the no-boundary definition and $S^4$ saddle used in §1.
- [HHH08] J. B. Hartle, S. W. Hawking, T. Hertog, "The classical universes of
  the no-boundary quantum state," Phys. Rev. D **77**, 123537 (2008),
  arXiv:0803.1663. Verified; supports the $\phi_0$-labelled branches and
  classicality condition in §3(a).
- [FLT17] J. Feldbrugge, J.-L. Lehners, N. Turok, "No smooth beginning for
  spacetime," Phys. Rev. Lett. **119**, 171301 (2017). Verified; supports the
  multiple-saddle/ill-definedness point in §2 and §3(d).
- [DTL19] A. Di Tucci and J.-L. Lehners, "No-boundary proposal as a path
  integral with Robin boundary conditions," Phys. Rev. Lett. **122**, 201302
  (2019), arXiv:1903.06757. Verified; supports the Robin-data rescue in §2.
- [GH77] G. W. Gibbons and S. W. Hawking, "Cosmological event horizons,
  thermodynamics, and particle creation," Phys. Rev. D **15**, 2738 (1977).
  Verified; supports $S_{dS} = \pi/(GH^2)$.
- [HaH90] J. J. Halliwell and J. B. Hartle, "Integration contours for the
  no-boundary wave function of the universe," Phys. Rev. D **41**, 1815 (1990).
  Verified (existence); referenced only for the complex-contour point in §5.
- [CW73] S. Coleman and E. Weinberg, "Radiative corrections as the origin of
  spontaneous symmetry breaking," Phys. Rev. D **7**, 1888 (1973). Verified;
  supports dimensional transmutation as a mechanism in §4/§6.
- [W72] S. Weinberg, *Gravitation and Cosmology* (Wiley, 1972). Existence
  verified; the relation $m_\pi^3 \simeq \hbar^2 H_0/(Gc)$ is attributed to
  this book by multiple secondary sources, which quote Weinberg calling it
  "so far unexplained." **Page/section not independently verified**; treat
  the attribution as exploratory-tier.
- [Z67] Ya. B. Zel'dovich, "Cosmological constant and elementary particles,"
  JETP Lett. **6**, 316 (1967); and "The cosmological constant and the theory
  of elementary particles," Sov. Phys. Usp. **11**, 381 (1968) (republished
  Gen. Rel. Grav. 2008). Existence verified. The $\rho \sim Gm^6c^4/\hbar^4$
  estimate is confirmed via S. Rugh and H. Zinkernagel, "The quantum vacuum
  and the cosmological constant problem," arXiv:hep-th/0012253 (verified),
  who quote it with page reference; **primary text not read**.
- Repo-internal: `programs/co-emergence/index.tex` (`ax:timeless`,
  `ax:nobackground`, `eq:meff`, `conj:mass_generation`, `eq:beta_xi`);
  `programs/fixed-point-existence/index.tex` (`sec:starobinsky`) and
  `claims/fpe-starobinsky-coefficient.md`, `claims/fpe-fixed-point-is-inflationary.md`;
  `programs/signature-change-boundary/notes/2026-06-17-expanding-region-note.md` §2;
  `programs/co-emergence/explorations/2026-03-03-mass-gap-synthesis.md` (verdicts, next steps);
  `programs/co-emergence/explorations/2026-03-03-position2-self-consistent-mass.md` §§3–5.
