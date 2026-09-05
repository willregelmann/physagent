# Attempt C — Hierarchies from the tree of histories: construction and stress test

**Explorer fan-out, position agent C. Date: 2026-09-05. Program: co-emergence (inputs from fixed-point-existence and signature-change-boundary).**

**Question (the mass test).** In a no-boundary reading of the framework the dimensionful inputs at the junction are $\Lambda$ and $G$. Can the branch structure of the Lorentzian tree of histories generate any scale other than $\Lambda^{1/2}$ (the Starobinsky $H_0$)? If not, a second scale is needed at the junction.

**Position (committed).** The rooted tree generates exactly one hierarchy with no new dimensionful input: the *e-fold ladder* along a non-de Sitter WKB branch, $H(a_k) \propto a_k^{-3(1+w)/2}$ with $a_k = a_{\rm root}e^{k}$. Its ratio per level is universal for a given equation of state ($e^{2}$ on a radiation branch) and its natural depth (20–70 e-folds) is the depth the gap needs. Every other tree mechanism fails on ratio or on depth, and the bifurcation-tree version (the repo's own map $F$) fails *structurally*: I prove below that its second-iterate Jacobian is positive semidefinite, so the tree of $F$ has exactly one branching and can never cascade. The e-fold ladder passes the ratio and depth tests but fails the *selection* test: the tree supplies rungs, not which rung a species sits on. The missing input is one dimensionless depth $k_s$ per species, fixed at the branch point where that species' mass is recorded. That is the "second scale at the junction," and it is a set of order-20 numbers rather than a scale.

---

## 1. Formalizing the tree

**Nodes, edges, root.** A node is a decoherent, coarse-grained classical history segment (a WKB branch $\Psi \approx A e^{iS}$, flow $\nabla S$); an edge is "child is a refinement of parent that became decoherent from its siblings"; the root is the Euclidean cap, the regular half-$S^4$ of radius $a_{\rm root} = \sqrt{3/\Lambda}$ joined at the degenerate-lapse, $K = 0$ equator — Hartle–Hawking's "state of minimum excitation" \[HH83\]. Three candidates for what the branch points are: **(i)** decoherence branchings on a WKB branch (events, not hypersurfaces; located by couplings and masses already present — this tree *carries* scales, it does not make them); **(ii)** nested signature-change or tunneling events, each with its own $\Lambda_k$ (§4); **(iii)** the bifurcation tree of the self-consistency map $F$ (§3).

**Orientation (Rigorous, combinatorial).** A rooted tree carries the order "$x \preceq y$ iff $x$ lies on the unique root-to-$y$ path." This needs a distinguished root — structural: the unique locus where the lapse degenerates and $K = 0$ — and acyclicity, which is *not* automatic: recohering histories, or two WKB branches through the same 3-geometry, make a graph, not a tree. The tree argument needs a no-recoherence hypothesis (Gell-Mann–Hartle medium decoherence; unverified as a citation).

**Definition.** A tree mechanism *generates a hierarchy* if some map from nodes to scales has $m(\text{root}) \sim \Lambda^{1/2}$ and $m(\text{child})/m(\text{parent}) = r^{-1}$ with $r$ fixed by structure, so depth-$k$ nodes carry $\Lambda^{1/2} r^{-k}$.

## 2. The arithmetic of the mass test

Two readings of $\Lambda$ give different gaps (script A):

| Gap | Orders |
|---|---|
| $M_P \to H_{0,\rm obs}$ (the "60 orders") | 60.9 |
| $M_P \to H_{\rm Star}$ (`fpe-fixed-point-is-inflationary`, $a_2 = 10^4$) | 2.0 |
| $H_{\rm Star} \to m_t,\ m_p,\ m_e,\ m_\nu$ | 14.8, 17.1, 20.4, 27.4 |
| $m_e \to H_{0,\rm obs}$ | 38.5 |

The repo's claim graph places the framework's $\Lambda$ at the Starobinsky scale, so the operative gap is **15–27 orders**; I carry both.

**Depth versus ratio (Rigorous arithmetic).** Bridging $D$ orders in depth $k$ needs $r = 10^{D/k}$: for $D = 60$, $k = 1$ needs $10^{60}$, $k = 10$ needs $10^{6}$, $k = 90$ needs $4.64$, $k = 138$ needs $e$, $k = 199$ needs $2$. Universal constants: Feigenbaum $\delta = 4.6692$ \[F78\] needs depth $89.7$ ($32.9$ for the 22-order $M_P \to m_e$ gap); Feigenbaum $\alpha = 2.5029$ needs $150.6$; period-doubling's own factor 2 needs $199$; one e-fold needs $138$; $e^{2}$ needs $69$. **No universal $O(1)$ ratio bridges the gap without depth of order $10^2$.** Every mechanism faces the trilemma: depth $O(1)$ and an astronomically large $r$ (only an exponential of an action can do it, §4c); depth $O(10^2)$ and an explanation of that depth; or unbounded depth and a selection principle.

## 3. Mechanism (iii): the bifurcation tree of $F$ — dead, and now structurally so

### 3.1 Reproduction

Script B runs the repo's map (`programs/co-emergence/tests/toy_model.py`) in the magnitude representation $q_\sigma = |\psi_\sigma|^2$, where $F$ becomes $G(q) = \mathrm{softmax}(2\gamma(h + Aq + \beta q))$, $A_{\sigma\sigma'} = \sum_j \alpha_j[\sigma_j = \sigma'_j]$, canonical $h = (1.0, 0.7, 0.5, 1.2)$, $\alpha = (0.5, 0.3)$, $\gamma = -1$.

- Periods over $\beta \in [0.3, 10^4]$ (140 values, 3 starts): **{1, 2} only**, as `ce-feigenbaum-cascade` (dead) records.
- $\beta_{\rm flip} = 0.648020$ by bisection on the $DG$ eigenvalue crossing $-1$, matching `ce-riem-classical-unique` (correction of 2026-07-25) to six digits; spectrum at the flip $\{-1, 0, -0.450, -0.270\}$.
- Along the whole period-2 branch the second-iterate multipliers stay in $[0, 0.972]$; the minimum real multiplier is $-0.0000$. Period 4 needs $-1$.
- **$\theta$ is dynamically inert (Rigorous).** For real $h, \alpha, \beta$, $|e^{\gamma R_\sigma}|^2 = e^{2\mathrm{Re}(\gamma)R_\sigma}$, so magnitudes see only $\mathrm{Re}\,\gamma$ and the phase is slaved, $\arg\psi^*_\sigma = \theta R_\sigma + \text{const}$ (the mechanism behind eq. `im_frac_reduction`). Script B: the complex map at $\theta \in \{0, 1, 3\}$ tracks the real $q$-map to $10^{-16}$ over 3000 iterates. Complexifying $h, \alpha, \beta$ keeps $\mathrm{Im}\,R$ affine in $q$ with symmetric coefficients, so the class is unchanged. **The bifurcation tree of $F$ is signature-blind**; it cannot be the Lorentzian tree of histories because it is identical on the Riemannian side.

### 3.2 New result: the second-iterate Jacobian is positive semidefinite

`ce-second-iterate-real-spectrum` (Sketch) proves real spectrum and records the gap that it "does not explain WHY the period caps at 2." This closes it.

**Claim C.1 (Rigorous, given the tangent-space reduction the repo already uses).** With $S(p) = \mathrm{diag}(p) - pp^{\mathsf T}$ and $M = 2\gamma(A + \beta I)$, $A$ symmetric: on the tangent hyperplane, where $S$ is positive definite at interior points, $DG(a) = S(b)M$ with $b = G(a)$ and $D(G\circ G)(a) = S(e)MS(b)M$, $e = G(b)$. Then
$$S(e)^{1/2} M S(b) M S(e)^{1/2} = XX^{\mathsf T}, \qquad X = S(e)^{1/2} M S(b)^{1/2},$$
using only $M = M^{\mathsf T}$. So **$D(G\circ G)$ is similar to a Gram matrix: real spectrum $\ge 0$ at every point of the domain.** A flip of a 2-cycle needs multiplier $-1$: impossible. Separately, for $\gamma < 0$, $\beta \ge 0$, $\alpha_j \ge 0$, $M$ is negative semidefinite ($A$ is a nonnegative sum of block all-ones matrices; script B prints $\mathrm{spec}\,A = \{0, 0.6, 1.0, 1.6\}$), so $DG \simeq S^{1/2}MS^{1/2}$ has spectrum $\le 0$: **a fixed point can lose stability only by flip, never by fold.** For $\gamma > 0$: fold-only. Script C, 500 random tangent-space Jacobians, $\beta \in [0.1, 10^3]$: $DG \in [-92.2, 3\times10^{-14}]$, $\min\mathrm{spec}\,D(G\circ G) = -4\times10^{-11}$, $XX^{\mathsf T}$ identity to $7\times10^{-8}$, $|\mathrm{Im}| < 3\times10^{-15}$.

**Consequence.** The tree of $F$ has exactly one branching and no second branching can occur by period-doubling. The only remaining route to period 4 is a saddle-node of $G^{\circ 4}$ disconnected from the flip — not excluded by C.1, never observed. Depth: **1**; ratio: undefined. Feigenbaum universality was never available: the renormalization fixed point behind $\delta$ needs iterates that can both fold and flip, and here the parities are locked.

**Side result C.2 (Sketch; every step named, one step is the repo's recorded coordinate gap).** C.1 proves the uniqueness `ce-riem-classical-unique` leaves open. Every fixed point is nondegenerate ($1 \notin \mathrm{spec}\,DG$) with Lefschetz index $\mathrm{sign}\det(I - DG) = +1$ since $I - DG$ has eigenvalues $\ge 1$. The closed simplex is a compact contractible ENR and $G$ maps it into its interior, so the Lefschetz–Hopf index sum is $1$. Hence **exactly one fixed point** for all $\beta \ge 0$, $\alpha_j \ge 0$, $\gamma < 0$, any real $h$, any $N$ and $\mathrm{dims}$. The repo had the index sum and one index; C.1 makes *all* indices $+1$. The unfilled step is the ambient-versus-reduced coordinate write-up that `ce-self-consistency-real-spectrum` already lists. The same fact kills the cascade and proves uniqueness: **the tree of $F$ has one branching because it has one root.**

### 3.3 What a cascade would need: dropping reciprocity

C.1 uses only $M = M^{\mathsf T}$: reciprocal coupling between smooth structures. Script D breaks it with $W = A + \kappa K$ ($K$ antisymmetric), $W = A + \kappa T$ ($T$ strictly lower-triangular: ancestor $\to$ descendant only, a literally tree-directed coupling), and random $W$.

- Tree-directed, $\beta = 5$: the fixed point's multipliers become a complex pair, the 2-cycle gives way to an **invariant circle** (no period $\le 2000$; Lyapunov exponents $(+0.000, -1.64)$) with mode-locking windows (period 28 at $\kappa = 1.8$, period 9 at $3.5$), then a stable fixed point at $\kappa \ge 6$. This is the **Neimark–Sacker** route the symmetric theorem excludes.
- Antisymmetric admixture: period $2 \to 3$ at $\kappa \approx 3.5$, all Lyapunov exponents negative.
- Random $W$: periods 1, 2, one quasi-periodic case; **no positive Lyapunov exponent, no period 4, 8, … anywhere.**

Non-reciprocity unlocks quasi-periodicity and odd periods, **not a Feigenbaum cascade**, which would further need a non-monotone one-dimensional reduction, i.e. a weight that is not a monotone exponential of a quadratic form. In framework terms: a self-consistency map with a *retarded* (non-symmetric) kernel — the causal Green operator of `fpe-banach-contraction`'s setting rather than the toy map's symmetric marginal kernel — gets invariant-circle branch structure, not a doubling cascade. And a retarded kernel presupposes the orientation the tree is meant to derive, unless the asymmetry *is* the ancestor relation — the $T$ case, which gives a circle, not a hierarchy.

## 4. Mechanism (ii): a nested no-boundary tree

**(a) Anomaly recursion (Sketch, computed).** Let $H_{k+1} = M_P/\sqrt{a_2(H_k)}$ with $a_2$ the anomaly coefficient of the fields light at $H_k$ (`fpe-starobinsky-coefficient`, order of magnitude only). With $a_2 \in [1, 10^5]$ the staircase lives in $[M_P/316, M_P]$: **2.5 orders, independent of depth.** Dead.

**(b) Brown–Teitelboim steps (Rigorous by citation; negative for the test).** Membrane nucleation lowers $\Lambda$ in fixed *additive* steps set by the membrane charge and stops near $\Lambda \approx 0$ \[BT88\]. Arithmetic, not geometric, and the step is a new dimensionful input — the second scale imported by hand.

**(c) Instanton-weight transmutation (Conjecture, computed; lands on an open repo defect).** The one way an $O(1)$-depth tree bridges 60 orders is $m \sim M_P e^{-|I_E|}$ with $|I_E| = 3\pi/(G\Lambda) = \pi M_P^2/H^2$ for the full $S^4$. Targets: $|I_E| = 138$ for 60 orders, $51$ for $m_e/M_P$, $39$ for $m_t/M_P$. At the Starobinsky scale $|I_E| = c\,a_2$ with $c$ set by the anomaly normalization — precisely the open correctness defect on `fpe-starobinsky-coefficient` (dimensional inconsistency; $16\pi$ discrepancy with Linde's form; issue #133). Repo prefactor: $|I_E| = a_2/180 \in [5.6, 556]$; $a_2 = 2.5\times10^4$ gives $138.9 \Rightarrow 10^{-60.3}$, $a_2 = 10^4$ gives $10^{-24.1} \approx m_e/M_P$. Canonical $H \sim M_P/\sqrt N$: $|I_E| = \pi a_2 \ge 3\times10^3$, $e^{-|I_E|} \le 10^{-1400}$. **Verdict:** not excluded by the repo's numbers, not selected by them, and decided entirely by #133. It also needs a mechanism by which a *rest mass* equals a tunneling weight (the gauge-theory instanton archetype); none exists in the framework.

## 5. Mechanism (iv): the e-fold ladder — the mechanism I commit to

**Construction (Sketch).** In pure Hartle–Hawking with only $\Lambda$ and $G$ every branch is de Sitter forever: the ladder is flat, **no hierarchy at all**. The framework differs in one repo-grounded way: its root is the trace-anomaly de Sitter, which is unstable (`fpe-fixed-point-is-inflationary`: "Rigorous-by-citation instability," lifetime $10^{-42}$–$10^{-40}$ s) and decays into the conformal fields that sourced it. On that branch $H \propto a^{-2}$, so with $a_k = a_{\rm root}e^{k}$,
$$m_k \equiv H(a_k) = H_{\rm Star}\,e^{-2k}, \qquad r = e^{2}\ (\text{radiation}),\ e^{3/2}\ (\text{dust}),\ 1\ (\text{de Sitter}).$$
The ratio is fixed by structure ($w = 1/3$ from conformality), not by a new dimensionful input; $k = \ln(a/a_{\rm root})$ is a superspace coordinate, not a time coordinate. Depths from $H_{\rm Star}$ ($a_2 = 10^4$): **top 17.1, electron 23.5, neutrino 31.5, $H_{0,\rm obs}$ 67.8 e-folds.** This is the one mechanism where a universal ratio and a natural depth of order $10^1$–$10^2$ coincide, and where the depth is a quantity the tree actually has.

**What it is not (Rigorous, standard).** $H(a_k)$ is a hierarchy of *energies*. It becomes a hierarchy of *rest masses* only if a species' mass is a **record** of the curvature scale at the branch point where the species froze, $m_s = H(a_{k_s})$. So "mass is the conformal factor, set at the junction" must mean *set at the species' branch point*; the literal reading predicts $\dot m/m = -2H_{0,\rm obs} \sim 10^{-10}\,\mathrm{yr}^{-1}$ relative to $M_P$, against lunar-laser-ranging bounds on $\dot G/G$ at the $10^{-13}\,\mathrm{yr}^{-1}$ level (unverified reference). The record reading is also what lets "records point root-ward" do work: a mass *is* a root-ward record.

**Where it fails: selection.** Nothing in the ladder puts the electron at $k = 23.5$ and the top at $17.1$. Curvature masses $m_{\rm eff}^2 = (\xi - \tfrac16)R$ (eq. `meff`) track $H$ and vanish on the radiation branch ($R = 0$), so they cannot freeze on their own; and the RG cannot make the per-species factor: with the repo's one-loop $\beta_\xi$ (eq. `beta_xi`, bracket $\approx 4.8$), $(\xi - \tfrac16) \propto \mu^{0.030}$, so 19 orders of running changes it by $0.26$ and a $10^{-40}$ suppression needs $1316$ orders of $\mu$. **The missing input is one dimensionless depth $k_s$ per species** — the Yukawa hierarchy relocated into tree depth. That is the precise content of "a second scale is needed": not a second *scale* (the ladder already has $H_{\rm Star}$ and $M_P$) but a *per-species address* on it.

## 6. Root uniqueness: the FLT / Di Tucci–Lehners dispute and the conjugate pair

**The dispute, polarity-checked (both abstracts verified).** Feldbrugge, Lehners and Turok \[FLT17\]: "the Lorentzian path integral for quantum cosmology with a positive cosmological constant is meaningful in this approach, but the Euclidean version is not," and with geometries starting from zero size "primordial tensor (gravitational wave) fluctuations are unsuppressed" — the side *against* a stable no-boundary root with a Dirichlet ($a = 0$) initial condition. Di Tucci and Lehners \[DTL19\], the rescuing side: "it was demonstrated by Feldbrugge et al. that the sum over all universes starting from zero size results in an unstable saddle point geometry. Here we show that … path integrals with a specific family of Robin boundary conditions overcome this problem. These path integrals are manifestly convergent and are approximated by stable Hartle-Hawking saddle point geometries. The price to pay is that the off-shell geometries do not start at zero size. The Robin boundary conditions may be interpreted as an initial state with Euclidean momentum." Further rounds exist (an FLT "no rescue" reply, 2018 — title only, unverified).

**Which side the framework commits to.** Di Tucci–Lehners, necessarily: the framework's junction is specified by a condition on the *expansion rate*, not on size. The `signature-change-boundary` expanding-region note finds junction regularity needs only a bounded proper expansion rate $\mathcal H = a'/(a\sqrt{|\lambda|})$, weaker than $K = 0$; a Robin condition fixes a combination of $a$ and its momentum, an initial Euclidean momentum. Both are momentum-type conditions; that they coincide at leading order is a Conjecture, not derived here. The negative that matters: the Robin parameter in \[DTL19\] is fixed by $\Lambda$, so **the rescue adds no scale.** Root uniqueness and the mass test are independent.

**Two saddles, one root (Sketch).** The classical-regime wave function is a sum over a complex-conjugate saddle pair, $\Psi \approx Ae^{iS} + Ae^{-iS}$ (contour analysis: \[HaHa90\], existence verified, specific passage not retrieved). Both share the same real cap and weight; they differ by the sign of $S$, the orientation of $\nabla S$. The tree order is "toward smaller conformal factor," the *same* for both. So the pair gives one root and two WKB orientations, and the tree order is invariant under the exchange — exactly `ce-theta-conjugation` (Rigorous): $\theta \to -\theta$ is entrywise conjugation, spectrum unchanged, "a harmless orientation convention." **Commitment:** a two-saddle root reproduces "orientation is a convention" for the *WKB* orientation and leaves the *tree* orientation untouched; they are different structures. Only two roots with *different real caps* — a landscape, not the no-boundary state — would break the argument.

## 7. Axiom check

- **Does "records point root-ward" smuggle evolution?** Partly. The tree order is combinatorial, but *which* events are branch points is decided by decoherence along $\nabla S$: branching order and WKB order are one order read twice. Not fatal — $S$ is a phase, structure, not a coordinate — but the tree *re-expresses* the WKB orientation rather than deriving it independently. What it adds is the record asymmetry, via the root being the minimum-excitation state \[HH83\].
- **Structure or WKB time?** The order comes from the DeWitt supermetric's one timelike direction, the conformal factor: root-ward is decreasing conformal factor. This is a preferred direction in *superspace*, which Axiom 2 does not forbid (it foliates superspace, not the 4-manifold), and it is why "mass is the conformal factor" and "the ladder is indexed by $\ln a$" are one statement.
- **Preferred foliation?** In minisuperspace yes (branch points are $a = $ const). In full superspace no: the tree orders histories, not manifold points. The brief's argument is a minisuperspace argument and inherits the foliation; the escape is the decoherent-histories formulation, where acyclicity (§1) becomes a hypothesis.
- **Hidden background?** $\Lambda$, $G$ by construction; the ladder adds $w = 1/3$, a field-content assumption the repo already makes, not a background.

## 8. Summary table

| Mechanism | Ratio per level | Set by | Depth for 60 / 22 orders | Status |
|---|---|---|---|---|
| (iii) bifurcation tree of $F$ | undefined (one branching, ever) | $M$ symmetric-definite (C.1) | — | **Dead, structurally** (Rigorous) |
| (iii′) $F$ with non-reciprocal kernel | none (invariant circle, locking) | asymmetry $\kappa$ | — | Dead for cascades (numerical); NS route confirmed |
| Feigenbaum $\delta$ (any cascade) | 4.669 | universal | 90 / 33 | Ratio fine, depth unexplained |
| (ii-a) anomaly recursion | $\le 10^{2.5}$ total | $a_2 \in [1, 10^5]$ | never | Dead (Sketch) |
| (ii-b) Brown–Teitelboim | additive | membrane charge | — | Needs imported scale |
| (ii-c) $e^{-|I_E|}$ | $e^{-c\,a_2}$ | anomaly coefficient (#133) | 1 / 1 | Open; hinges on #133 |
| (iv) e-fold ladder, radiation branch | $e^{2}$ | $w = 1/3$ | 69 / 25 | **Alive for rungs; needs per-species $k_s$** |
| (iv) e-fold ladder, de Sitter branch | 1 | — | never | Dead (pure HH has no ladder) |
| RG of $\xi - \tfrac16$ | $\mu^{0.03}$ | one-loop bracket 4.8 | 1316 orders in $\mu$ | Dead |

## 9. Closing sections

### (a) What would kill this attempt

1. A proof that post-Starobinsky histories recohere generically: no tree, only a graph, and root-ward is undefined.
2. A demonstration that the framework's $\Lambda$ must be the observed one: the branch is then de Sitter at $10^{-33}$ eV, the ladder runs *upward* from $H$ to masses, and the record reading inverts.
3. Resolution of #133 to the canonical $H \sim M_P/\sqrt N$: kills (ii-c) outright ($e^{-3000}$).
4. A period-4 orbit of the repo's map born by fold of $G^{\circ 4}$: would not overturn C.1 but would reopen a cascade route; I predict none exists.
5. A per-species mechanism fixing $k_s$ from the root alone would *complete* rather than kill the attempt; its absence kills the strong form "the tree generates the mass spectrum."

### (b) If negative, the adaptation it points to

The negative is precise: the tree generates the *ladder*, not the *addresses*. What is needed is a label $k_s \in \{17, 23, 31, \ldots\}$ per species, from one of three places. **(1)** The anomaly coefficient's normalization (#133), if (ii-c) survives: a single number $c\,a_2 \approx 40$–$140$ covering the top-to-electron window is the cheapest possible outcome and is decided by a computation already on the repo's books. **(2)** The perturbation spectrum of the root — the Bunch–Davies-type state on the cap — the only structure at the junction beyond $\Lambda$ and $G$, whose mode-by-mode freezing depth is the natural candidate for $k_s$ (Conjecture; no computation here). **(3)** Failing both, an explicit second input at the junction, which is the Yukawa sector by another name. On the map side, $F$ needs a non-reciprocal kernel to have any branch structure beyond one flip (§3.3), and even then it gets an invariant circle; the ladder lives on the WKB branch, not in $F$.

### (c) What is underspecified

- Acyclicity (no-recoherence) is assumed, not derived.
- The SCB bounded-expansion-rate condition equals a Robin condition: conjecture.
- Conjugate-pair statement: standard, specific passage in \[HaHa90\]/\[Le23\] not verified.
- "Mass is a record of $H$ at the branch point" is my reading of the experimenter's phrase; the literal reading is excluded by mass-constancy bounds I did not verify to the reference.
- C.2's ambient-coordinate write-up (the repo's recorded gap).
- Ladder depths assume $a_2 = 10^4$ and $H_{\rm end} \approx H_{\rm Star}$; a reheating drop of $n$ orders shifts every depth by $1.15n$ e-folds.
- Generality of the {1, 2} period cap beyond $N = 4$: see script E below.

---

## Scripts and output (inline; numpy/scipy; no files created)

### Script A — parameter-free arithmetic (§2, §4, §5)

```python
import numpy as np; L10=np.log(10.0)
for name,r in (("delta",4.669201609),("alpha",2.502907875),("2",2.0),("e",np.e),("e^2",np.e**2)):
    print(name, 60*L10/np.log(r), 22*L10/np.log(r))                     # depth for 60 / 22 orders
for a2 in (1e3,1e4,2.5e4,1e5): print(a2, a2/180, np.pi*a2)              # |I_E|: repo prefactor vs canonical
print(60*L10, 22*L10, 17*L10)                                            # target |I_E|
g=4.8/(16*np.pi**2); print(g, 40/g)                                      # xi-1/6 anomalous dimension; orders for 1e-40
MP=1.22e28; H0=1.5e-33; HS=MP/np.sqrt(1e4)                               # eV
for name,m in (("top",1.73e11),("proton",9.38e8),("electron",5.11e5),("nu",0.05),("H0obs",H0)):
    print(name, np.log10(HS/m), 0.5*np.log(HS/m))                        # gap; e-folds on H ~ a^-2
```
Output: depths $\delta$ 89.7/32.9, $\alpha$ 150.6/55.2, 2: 199.3/73.1, $e$: 138.2/50.7, $e^2$: 69.1/25.3. $|I_E|$ repo: 5.6, 55.6, 138.9, 555.6; canonical: 3142, 31416, 78540, 314159; targets 138.2/50.7/39.1. Anomalous dimension 0.0304; 1316 orders. $\log_{10}(H_{\rm Star}/m)$: 14.8, 17.1, 20.4, 27.4, 59.0; e-folds 17.1, 19.7, 23.5, 31.5, 67.8.

### Script B — repo map: period census, flip, 2-cycle multipliers, θ-inertness (§3.1)

```python
import numpy as np, sys; sys.path.insert(0,'programs/co-emergence/tests'); from toy_model import CoEmergenceModel
from scipy.optimize import root, brentq
h=np.array([1.0,0.7,0.5,1.2]); dims=(2,2); alphas=(0.5,0.3); gam=-1.0; N=4
idx=np.array(np.unravel_index(np.arange(N),dims)).T; A=np.zeros((N,N))
for j,a in enumerate(alphas): A+=a*(idx[:,j][:,None]==idx[:,j][None,:])
def G(q,b): z=2*gam*(h+A@q+b*q); z-=z.max(); w=np.exp(z); return w/w.sum()
def DG(q,b): p=G(q,b); return (np.diag(p)-np.outer(p,p))@(2*gam*(A+b*np.eye(N)))
def period(b,q0,nwarm=40000,maxp=64,tol=1e-9):
    q=q0.copy()
    for _ in range(nwarm): q=G(q,b)
    tr=[q]
    for _ in range(maxp): q=G(q,b); tr.append(q)
    for p in range(1,maxp+1):
        if np.linalg.norm(tr[p]-tr[0])<tol: return p,tr
    return -1,tr
rng=np.random.default_rng(0); betas=np.logspace(np.log10(0.3),4,140)
print(sorted(set(period(b,rng.dirichlet(np.ones(N)))[0] for b in betas for _ in range(3))))
def fp(b):
    res=lambda x:(G(np.append(x,1-x.sum()),b)-np.append(x,1-x.sum()))[:N-1]
    x=root(res,np.ones(N-1)/N,tol=1e-14).x; return np.append(x,1-x.sum())
bflip=brentq(lambda b:np.linalg.eigvals(DG(fp(b),b)).real.min()+1,0.3,2.0,xtol=1e-10); print(bflip, np.linalg.eigvals(DG(fp(bflip),bflip)))
for b in np.logspace(np.log10(0.66),4,25):
    p,tr=period(b,rng.dirichlet(np.ones(N))); ev=np.linalg.eigvals(DG(tr[1],b)@DG(tr[0],b)); print(b,p,np.sort(ev.real))
for theta in (0.0,1.0,3.0):
    mdl=CoEmergenceModel(dims,h,list(alphas),5.0,gam+1j*theta); psi=rng.normal(size=N)+1j*rng.normal(size=N); psi/=np.linalg.norm(psi); q=np.abs(psi)**2; d=0
    for _ in range(3000): psi=mdl.F_map(psi); q=G(q,5.0); d=max(d,np.abs(np.abs(psi)**2-q).max())
    print(theta,d)
```
Output: periods `[1, 2]`; $\beta_{\rm flip} = 0.648020$, spectrum `[-1, -0, -0.44975, -0.27045]`; 2-cycle multipliers (sorted real parts): $\beta = 0.66$: `[0, 0.074, 0.203, 0.972]`; $4.9$: `[0, 0.00002, 0.157, 0.463]`; $54$: `[0, 0, 0, 0.037]`; $\beta \ge 121$: all $\approx 0$; branch minimum $-0.0000$, maximum $|{\rm mult}| = 0.972$. $\theta$-check: $6.7\times10^{-16}$, $5.6\times10^{-16}$, $4.4\times10^{-16}$.

### Script C — tangent-space PSD verification (§3.2)

```python
import numpy as np; from scipy.linalg import sqrtm, null_space      # h, A as in B; G(q,b,gam) as in B with gam explicit
U=null_space(np.ones((1,N))); S=lambda p: np.diag(p)-np.outer(p,p); rng=np.random.default_rng(11)
for gam in (-1.0,+1.0):
    mx=-1e9; mn=1e9; mn2=1e9; im=0; idn=0
    for b in np.logspace(-1,3,25):
        M=2*gam*(A+b*np.eye(N)); Mt=U.T@M@U
        for _ in range(20):
            a=rng.dirichlet(np.ones(N)*rng.uniform(0.2,3)); bb=G(a,b,gam); e=G(bb,b,gam); Sb=U.T@S(bb)@U; Se=U.T@S(e)@U
            assert np.linalg.norm(U.T@(S(bb)@M)@U-Sb@Mt)<1e-12       # reduction exact: S annihilates the constant vector
            e1=np.linalg.eigvals(Sb@Mt); e2=np.linalg.eigvals(Se@Mt@Sb@Mt)
            mx=max(mx,e1.real.max()); mn=min(mn,e1.real.min()); mn2=min(mn2,e2.real.min()); im=max(im,abs(e1.imag).max(),abs(e2.imag).max())
            Se12=np.real(sqrtm(Se)); Sb12=np.real(sqrtm(Sb)); X=Se12@Mt@Sb12; idn=max(idn,np.linalg.norm(Se12@Mt@Sb@Mt@Se12-X@X.T))
    print(gam,mn,mx,mn2,im,idn)
```
Output: $\gamma = -1$: $DG \in [-92.2, 3.0\times10^{-14}]$, $\min\mathrm{spec}\,D(G\circ G) = -4.0\times10^{-11}$, $\max|\mathrm{Im}| = 3.0\times10^{-15}$, identity residual $7.1\times10^{-8}$. $\gamma = +1$: $DG \in [-3.9\times10^{-14}, 175.2]$, $\min\mathrm{spec}\,D(G\circ G) = -1.5\times10^{-17}$, residual $3.2\times10^{-14}$. $\mathrm{spec}\,A = \{0, 0.6, 1.0, 1.6\}$.

### Script D — non-reciprocal kernels (§3.3)

```python
# G, DG as in B with W in place of A (M = 2*gam*(W+b*I)); period search to 2000 after 30000 warm-up; two-exponent Benettin Lyapunov.
T=np.tril(np.ones((N,N)),-1); B=np.random.default_rng(7).normal(size=(N,N)); K=(B-B.T)/2; K/=abs(np.linalg.eigvals(K)).max()
for kappa in (1.0,1.5,1.8,2.0,2.5,3.0,3.5,4.0,5.0,6.0,8.0): report(W=A+kappa*T, beta=5.0)     # period, (L1,L2), fixed-point multipliers
for kappa in (2.0,2.5,3.0,3.5,4.0,6.0,8.0,12.0):              report(W=A+kappa*K, beta=5.0)
for seed in range(3): W=rng.normal(size=(N,N)); W/=abs(np.linalg.eigvals(W)).max(); [report(W,b) for b in (1,2,5,10,20,50)]
```
Output, tree-directed $W = A + \kappa T$, $\beta = 5$ ($\kappa$: period, $(L_1, L_2)$, fixed-point multipliers): 1.0: 2, $(-0.64, -0.72)$, real $\{-2.89, -2.80, -1.73\}$; 1.5: none, $(-0.000, -1.25)$, $-2.76 \pm 0.24i$; 1.8: **28**, $(-0.002, -1.49)$; 2.0: none, $(+0.000, -1.64)$, $-2.65 \pm 0.33i$; 2.5–3.0: none, $(\approx 0, -2.0\ldots-2.4)$; 3.5: **9**; 4.0–5.0: none, $(\approx 0, -2.1\ldots-1.1)$; 6.0: 1, $-0.85 \pm 0.53i$; 8.0: 1. Antisymmetric $W = A + \kappa K$, $\beta = 5$: $\kappa \le 3.0$ period 2; $\kappa \ge 3.5$ period **3**, Lyapunov exponents negative. Random $W$ (3 seeds, $\beta \in \{1, \ldots, 50\}$): periods 1, 2, one quasi-periodic case ($L_1 = -0.00$); **no positive Lyapunov exponent, no period 4, 8, … anywhere.**

### Script E — generality scan ($N$ up to 16)

```python
# 12 instances: dims in {(2,2),(2,2,2),(3,3),(2,2,2,2)} x 3 seeds; h~U[0.5,1.5], alpha~U[0.2,0.8]; gam in {-0.5,-1,-2,-5};
# 16 log-spaced betas in [0.3,1e3]; period search to 64 (tol 1e-7) after 6000 warm-up iterates; union of periods reported.
```
Output: 768 solves; union of periods `[-1, 1, 2]`; the single `-1` (no period found) is instance dims $(2,2,2,2)$, seed 2, $\gamma = -1$, at $\beta = 2.609$. Follow-up on that instance: its fixed-point multiplier there is $-1.00002$, i.e. the grid point sits $2\times10^{-5}$ past that instance's flip; with $3\times10^5$ warm-up iterates the period is exactly 2 ($\|G^{\circ 2}(q) - q\| = 1.4\times10^{-13}$). Critical slowing down at onset — the trap `ce-riem-classical-unique` records — not a new period. **All 12 instances, $N \in \{4, 8, 9, 16\}$, $\gamma \in \{-0.5, -1, -2, -5\}$: periods {1, 2} only**, consistent with C.1.

---

## References (verified by web search unless marked)

- \[HH83\] J. B. Hartle and S. W. Hawking, "Wave function of the Universe," Phys. Rev. D **28**, 2960 (1983). Verified (APS). Used for: the no-boundary ground state as "state of minimum excitation"; compact positive-definite four-geometries with the three-geometry as only boundary.
- \[HaHa90\] J. J. Halliwell and J. B. Hartle, "Integration contours for the no-boundary wave function of the universe," Phys. Rev. D **41**, 1815 (1990). Existence and stated aims verified (ADS/APS). **Conjugate-saddle-pair passage not verified** (full text not retrieved).
- \[FLT17\] J. Feldbrugge, J.-L. Lehners, N. Turok, "No Smooth Beginning for Spacetime," Phys. Rev. Lett. **119**, 171301 (2017), arXiv:1705.00192. Verified (APS + arXiv abstract). Polarity: *against* a stable no-boundary saddle from zero size; affirming passages quoted in §6.
- \[DTL19\] A. Di Tucci and J.-L. Lehners, "No-Boundary Proposal as a Path Integral with Robin Boundary Conditions," Phys. Rev. Lett. **122**, 201302 (2019), arXiv:1903.06757. Verified (APS + arXiv abstract). Polarity: *for* a stable Hartle–Hawking saddle under Robin conditions; affirming passages quoted in §6.
- \[Le23\] J.-L. Lehners, "Review of the No-Boundary Wave Function," Phys. Rep. **1022**, 1 (2023), arXiv:2303.08802. Existence verified; not used for any specific claim.
- \[F78\] M. J. Feigenbaum, "Quantitative universality for a class of nonlinear transformations," J. Stat. Phys. **19**, 25 (1978). Verified (Springer/ADS); $\delta = 4.669201609\ldots$ for a quadratic maximum.
- \[BT88\] J. D. Brown and C. Teitelboim, "Neutralization of the cosmological constant by membrane creation," Nucl. Phys. B **297**, 787 (1988). Verified (ADS/Semantic Scholar); affirming content: $\Lambda$ reduced stepwise by membrane nucleation, process stops near zero.
- Unverified, flagged: Gell-Mann–Hartle medium decoherence (exact statement not checked); FLT 2018 "No rescue for the no boundary proposal" (title only); lunar-laser-ranging $\dot G/G$ bound (value from memory).

**Repo results used:** `programs/co-emergence/index.tex` Axioms 1–3 (lines 163–186), §Finite toy model incl. eq. `im_frac_reduction`, §Weakening the mass assumption eqs. `meff`, `beta_xi`, Remark `xi_running`; `claims/ce-toy-fixed-point-multiplicity.md` (dead; flip at the unique fixed point), `claims/ce-feigenbaum-cascade.md` (dead; period caps at 2), `claims/ce-second-iterate-real-spectrum.md` (Sketch; real spectrum, gap "why the cap"), `claims/ce-self-consistency-real-spectrum.md` (Sketch; coordinate gap), `claims/ce-riem-classical-unique.md` (Sketch; $\beta_{\rm flip} = 0.648020$; Lefschetz sum $= 1$; uniqueness open), `claims/ce-theta-conjugation.md` (Rigorous); `programs/fixed-point-existence/claims/fpe-starobinsky-coefficient.md` (Sketch; open dimensional-convention defect; #133), `fpe-fixed-point-is-inflationary.md` (Sketch; $H \sim M_P/\sqrt N$); `programs/signature-change-boundary/README.md` (bounded proper expansion rate suffices for junction regularity); `programs/co-emergence/explorations/2026-03-03-mass-gap-synthesis.md` §"Structural convergence" 5 and §"Verdict 2" (single scale $\sim H_0$; spectrum needs additional structure).
