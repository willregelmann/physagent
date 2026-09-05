# Attack pass on Attempt C — "Hierarchies from the tree of histories"

**Target:** `/home/will/Projects/physagent/attempt-C-tree-hierarchy.md` (position agent C, explorer fan-out).
**Date:** 2026-09-05.
**Role:** Attack pass (Pass 1 of METHODOLOGY "No Idea Is Eliminated Without a Defense"). Flaws only; no verdict. A steelman agent answers this list.

All numerics below were re-run independently (scripts in the appendix; the repo's `programs/co-emergence/tests/toy_model.py` was imported for the θ checks). External references used to attack are web-verified unless marked.

---

## Flaws

### The committed mechanism (§5, the e-fold ladder)

**1. §5, construction. The "depth" is not a tree depth; the tree contributes nothing to the ladder.**
$k=\ln(a/a_{\rm root})$ is a continuous coordinate along a *single* WKB branch. There are no rungs: nothing places a branch point at $a=a_{\rm root}e^{k}$ for integer $k$, and the attempt's own §1 definition requires a map from *nodes* (decoherence events) to scales. $H(a)=H_{\rm Star}e^{-2k}$ is the FRW Hubble rate of one radiation branch, i.e. $\Lambda^{1/2}$ times a dimensionless position label. The ladder therefore answers the mass test "no": every value it produces is $\Lambda^{1/2}\,f(a)$, and the label $f$ is exactly the per-species input the attempt then says is missing (§5, "selection"). The tree structure (branchings, root, orientation) enters nowhere in the formula. *Severity: structural.*

**2. §5, depths. The depth accounting silently drops the de Sitter phase, which is the only part of the branch that starts at the root.**
By definition $k=\ln(a/a_{\rm root})$ counts from the cap's equator, but the quoted depths (top 17.1, electron 23.5, …) are counted from the *end* of the anomaly-driven de Sitter stage. That stage is the flat ladder ($r=1$) the attempt itself calls "no hierarchy," and it contributes $N_{\rm inf}=H\tau$ e-folds. With the repo's lifetime window $\tau\in[10^{-42},10^{-40}]$ s (`fpe-fixed-point-is-inflationary`) and $a_2=10^4$: $N_{\rm inf}\in[0.19,18.6]$ for $H=M_P/\sqrt{a_2}$ (the form the attempt uses in §2/§5) and $[4.4,441]$ for the repo's printed $H^2=180\pi M_P^2/a_2$. So the depth of the electron rung *from the root* is $23.5+N_{\rm inf}$, undetermined to within one to three orders of magnitude in e-folds. The §9(c) caveat ("reheating drop of $n$ orders") is a different, smaller effect. *Severity: factual / structural.* (Script A2.)

**3. §5, construction. The framework's own post-decay branch is closed and $\Lambda$-free, hence recollapses; the ladder's reachable depth is bounded by $2N_{\rm inf}$ and "root-ward = smaller $a$" stops being an order at turnaround.**
The root is a half-$S^4$, so the branch has $S^3$ slices; the curvature is anomaly-sourced with no cosmological term (the attempt's §5 says exactly this: pure HH with a $\Lambda$ would stay de Sitter, the framework's root decays). A closed radiation universe leaving de Sitter at $a_{\rm end}=e^{N_{\rm inf}}a_{\rm root}$ turns around at $a_{\max}=H_{\rm end}a_{\rm end}^2=e^{2N_{\rm inf}}a_{\rm root}$, where $H=0$: the ladder bottoms out at $m=0$ at finite depth $2N_{\rm inf}$, not at $H_{0,\rm obs}$. The electron rung ($N_{\rm inf}+23.5\le 2N_{\rm inf}$) exists only if $N_{\rm inf}\ge 23.5$, and $H_{0,\rm obs}$ at depth 67.8 needs $N_{\rm inf}\ge 34$; with the attempt's own $H=M_P/\sqrt{a_2}$ and the repo's lifetime window, $N_{\rm inf}\le 18.6$ — neither rung is reached. The alternative is to add $\Lambda_{\rm obs}$ by hand, which is the second scale the attempt says the ladder avoids. Past turnaround, two nodes at the same $a$ are incomparable under "root-ward = decreasing conformal factor," so the tree order is not even a partial order on the branch. *Severity: structural.* (Script A2; standard closed-FRW turnaround.)

**4. §5, "record" reading. There is no branch point at $H=m_s$; the "species' branch point" is the solution of $H(a)=m_s$, a relabeling of the missing input.**
$H=m_t$ occurs at $T\approx1.1\times10^{10}$ GeV and $H=m_e$ at $T\approx1.9\times10^{7}$ GeV (radiation, $g_*\sim100$). Nothing happens to the top or the electron at those epochs; both masses are set at the electroweak transition, $T\sim10^2$ GeV, when $H\sim10^{-14}$ GeV $\ll m$. So "mass is a record of $H$ at the branch point where the species froze" names no decoherence event, no node, and no mechanism. It is the statement "$k_s\equiv\tfrac12\ln(H_{\rm Star}/m_s)$" — the definition of the address, not its origin. *Severity: structural.* (Script A2.)

**5. §5, literal-reading exclusion. Wrong rate, right conclusion.**
$\dot m/m=\dot H/H$ today is $-(1+q_0)H_0\approx-3\times10^{-11}\,\mathrm{yr^{-1}}$, not $-2H_0$ (radiation scaling does not hold today). The conclusion survives against the now-verified bound $\dot G/G=(7.1\pm7.6)\times10^{-14}\,\mathrm{yr^{-1}}$ (Hofmann & Müller, CQG **35**, 035015, 2018): $m\propto H$ at fixed $G$ makes $Gm^2$ drift at $\sim6\times10^{-11}\,\mathrm{yr^{-1}}$, three orders above the bound. *Severity: factual, minor.*

**6. §5 / §7, "$w=1/3$ from conformality … a field-content assumption the repo already makes."** The repo records the fixed point's existence and instability, not what follows its decay; reheating into radiation is imported from standard cosmology (Starobinsky's own model passes through a scalaron-dominated, matter-like stage first). The "universal ratio" is also not universal along the branch: it is $1\to e^{3/2}\to e^{2}\to e^{3/2}\to1$ across de Sitter, scalaron, radiation, matter, $\Lambda$ epochs. The ladder is standard thermal history relabeled. *Severity: background / scope.*

**7. §2, "natural depth (20–70 e-folds)."** That number is the inflationary e-fold count — a de Sitter, $r=1$, flat-ladder quantity — borrowed to motivate the depth of the *radiation* ladder ($r=e^2$). Two different branches; the coincidence claimed in §5 ("universal ratio and natural depth coincide") is an equivocation. Likewise Feigenbaum $\delta$ is the ratio of successive bifurcation-*parameter* intervals, not of a physical scale between levels ($\alpha$ is the orbit-scale ratio); the trilemma table treats both as "ratio per level" without saying which plays $m({\rm child})/m({\rm parent})$. *Severity: presentational.*

### The bifurcation tree of $F$ (§3)

**8. §3.2 "Consequence," §3.2 C.2 last sentence, §8 table: "exactly one branching," "Depth: 1," "one branching because it has one root" — false; the unique fixed point flips $N-1$ times.**
All $N-1$ nontrivial eigenvalues of $DG|_T$ decrease without bound in $\beta$ (they scale like $-\beta$), so each crosses $-1$. Canonical $N=4$ instance: flips at $\beta=0.648020,\ 1.848777,\ 2.218503$ (bisection, Script B). Each spawns a genuine period-2 orbit: Newton on $G\circ G$ from the flip eigendirection at $\beta=1.869$ and $2.239$ returns minimal-period-2 orbits at distance $0.061$ and $0.065$ from the fixed point (Script C). The record's "zoo" — up to 7 coexisting attracting 2-cycles (`ce-riem-classical-unique`, correction 4 of 2026-07-25) — reproduces here (1 at $\beta=2,5$; 5 at 20; 7 at 40 and 100, from 40 starts), and 7 attracting 2-cycles cannot come from 3 flips: disconnected folds of $G^{\circ2}$ *do* occur. So mechanism (iii) generates $N-1$ branch scales $\beta_i$ with $O(1)$ ratios ($2.85$, $1.20$) — "undefined" in the table is wrong, and the attempt never mentions the zoo. None of this rescues a cascade, but the attempt's characterization of the tree of $F$ is factually wrong on the repo's own record. *Severity: factual + structural.*

**9. §3.2 / §8 table "Dead, structurally (Rigorous)": overclaim of what C.1 proves.**
C.1 excludes flip and Neimark–Sacker *of the 2-cycle* (multipliers $\ge0$, real). It does not bound the number of branchings (flaw 8), does not exclude a fold-born period-4 orbit (conceded), and once such an orbit exists its multipliers come from $D(G^{\circ4})=S(a)MS(d)MS(c)MS(b)M$, whose inner $S$-sequence is not a palindrome — nothing then stops a cascade starting at period 4. "Never observed" rests on the attempt's census, which iterates from 3 starts per $\beta$ and so sees attracting orbits with large basins only (the zoo needed 40 starts). My Newton census on $G^{\circ3}$ and $G^{\circ4}$ (300 starts, 8 values $\beta\in[1,400]$) found no period-3 or period-4 orbit, stable or unstable — the prediction holds, but as numerics. "Dead structurally" is at most "no doubling route from the 2-cycle (Rigorous); no other route found (numerical)." *Severity: scope / presentational.*

**10. §3.2, first paragraph: misquotes the record and misdescribes what C.1 adds.**
`ce-second-iterate-real-spectrum` does not record the gap "does not explain WHY the period caps at 2"; its listed gap is "Does not explain WHY the second-iterate spectral radius decays to ~0.037," and its `consequence` field already claims the cap is explained ("Explains, rather than merely observes, why the period caps at 2"). The record's *derivation* already writes $Z=S(e)^{1/2}MS(b)MS(e)^{1/2}$ as "a palindrome of self-transpose factors," and its cited prior art is titled "A characterization for **positive semi-definite** matrix products" ($LL^{\mathsf T}$ form). PSD is thus one line from the record; what C.1 genuinely adds is the bifurcation consequence — the 2-cycle cannot flip or Neimark–Sacker — which is a *better* explanation of the cap than the record's (the record's "$k\ge3$ breakdown" does not exclude period 4; C.1 does). The attempt claims the wrong novelty. *Severity: presentational / factual.*

**11. §3.2 "Feigenbaum universality was never available: the renormalization fixed point behind $\delta$ needs iterates that can both fold and flip."** Wrong reason. The doubling cascade is a sequence of flips of $G^{\circ2^n}$; folds are not required (they produce periodic windows). The correct reason is C.1 itself. *Severity: presentational.*

**12. §3.1 θ-inertness: the extension to complex parameters is not inertness.**
For real $h,\alpha,\beta$ the claim holds (flaw-free; see "Claims that held"). But "Complexifying $h,\alpha,\beta$ keeps Im $R$ affine … so the class is unchanged" conflates class-preservation with inertness: the magnitude map becomes ${\rm softmax}(2\,{\rm Re}\gamma\,{\rm Re}R-2\theta\,{\rm Im}R)$ and depends on $\theta$. Verified with `toy_model.py` (which stores $h$ as complex): $h+0.3i(1,-1,0.5,0.2)$, $\beta=5$: magnitude fixed point $(0.0137,0.0001,0.876,0.110)$ at $\theta=0$ vs $(0.048,0.00003,0.834,0.118)$ at $\theta=1$. *Severity: presentational, minor.*

**13. §3.3, "tree-directed coupling."** A strictly lower-triangular $T$ on the flattened index of smooth structures encodes a total order on smooth structures, not a tree, and has no relation to the tree of histories; the "ancestor → descendant" label is decorative. The Neimark–Sacker finding stands on its own. *Severity: presentational, minor.*

### The instanton-weight route (§4c) and #133

**14. §4c, sign. The no-boundary weight is an enhancement, not a suppression.**
$I_E(S^4)<0$; the weight is $e^{-I_E}=e^{+|I_E|}$. Lehners' review eq. (173) (verified, see citations): $\Psi\approx e^{+12\pi^2/\hbar\Lambda}[e^{-i\cdots}+e^{+i\cdots}]$. Writing $m\sim M_Pe^{-|I_E|}$ uses the tunneling-proposal sign. Inside the HH root the attempt is built on, "instanton-weight transmutation" has the wrong sign before one asks for a mechanism. *Severity: structural.*

**15. §4c, action. $|I_E|=\pi M_P^2/H^2$ is the pure-$\Lambda$ $S^4$ action; the framework's root has no $\Lambda$.**
For the anomaly-driven $S^4$ the on-shell Einstein–Hilbert part is $-(1/16\pi G)\int R\sqrt g=-2\pi/(GH^2)=-2a$ (twice the attempt's $-\pi/GH^2$, since there is no $-2\Lambda$ in the integrand), and the conformal fields' effective action adds a scheme-dependent $4a\ln(H/\mu)$ on $S^4$ (its $\ln$-derivative is the integrated anomaly). So "$|I_E|=a_2/180$" is not the action of the framework's own root; my derivation, Sketch. *Severity: factual.*

**16. §4c "decided entirely by #133" — stale and wrong target.**
(a) #133 is **closed** (2026-07-17, "Superseded by #168"); #168 is open, `agent-ready`, no PRs. (b) #133/#168 concern the *citation and unit convention* of the printed coefficient, not its value: the comment closing #133 records that PR #134 re-derived $H_0^2=180\pi/(Ga_2)$ two ways. I checked it against Duff's eq. (31) (verified): $b'=-[N_S+11N_F+62N_V]/(360(4\pi)^2)$, and $E|_{dS}=24H^4$ give $a_2=\tfrac12(N_S+11N_F+62N_V)$ and $H^2=\pi M_P^2\cdot360/(N_S+11N_F+62N_V)$ — the repo's formula is the standard one. Hence the number is fixed by field content, not by a convention issue: for the Standard Model ($N_S=4$, $N_F=22.5$, $N_V=12$) $a_2\approx498$, $H\approx1.07\,M_P$ (super-Planckian, outside semiclassical validity — HHR 2001's "provided there are sufficiently many matter fields"), and $|I_E|=a_2/180\approx2.8$, $e^{-2.8}\approx0.06$: no hierarchy. Landing in the attempt's window $|I_E|\in[39,138]$ needs $N_S+11N_F+62N_V\in[1.4\times10^4,5\times10^4]$, i.e. of order 230–800 extra vector fields. The route is decided by $a_2$'s value — a field-content input, which *is* the "second input" — not by #133. *Severity: factual / structural.* (Script A2.)

**17. §2 gap table: "$M_P\to H_{\rm Star}$ (`fpe-fixed-point-is-inflationary`, $a_2=10^4$): 2.0 orders."**
That node's own formula is $H=\sqrt{180\pi/a_2}\,M_P=0.24\,M_P$ (0.62 orders); "$H\sim M_{\rm Pl}/\sqrt N$" there is a heuristic with $N\ne a_2$. The attempt uses the heuristic in §2/§5 (Script A: `HS=MP/np.sqrt(1e4)`) and the printed prefactor in §4c, a factor $23.8$ in $H$ and $1.6$ e-folds in every depth, without saying so. *Severity: factual, minor.*

### Root uniqueness and orientation (§6, §7)

**18. §6 "Which side the framework commits to. Di Tucci–Lehners, necessarily" — the analogy misplaces the condition and inverts the polarity.**
DTL's Robin condition is imposed at the *initial* end of the off-shell geometries (the abstract: "the off-shell geometries do not start at zero size … an initial state with Euclidean momentum"), i.e. at the would-be South Pole. The SCB condition (bounded proper expansion rate $\mathcal H$) is a *curvature-regularity* condition on a fixed classical background at the signature-change surface, which in the HH geometry is the *equator*, where $K=0$ exactly (a totally geodesic $S^3$) — stronger than bounded $\mathcal H$, so SCB's "weaker" condition selects nothing there. The attempt's root, "the regular half-$S^4$," presupposes regularity at $a=0$: that is the zero-size setup FLT attack, not DTL's. The framework does not commit to DTL; if anything its stated root sits on the FLT-attacked side. Also "the Robin parameter in [DTL19] is fixed by $\Lambda$" is not in the abstract, which speaks of "a specific family of Robin boundary conditions"; unverified. *Severity: structural / factual.*

**19. §6 "Two saddles, one root" confirms rather than escapes §7's concession.**
Lehners' review p. 101 (verified): the wave function "is a sum over two complex conjugate contributions … in a sense time flows in opposite directions in both saddles," and the two saddles decohere as the universe grows (his §5.3, citing his ref. [27]). The tree order "toward smaller conformal factor" is the same for both saddles precisely because it is the intrinsic-time ($a$) orientation. By the attempt's own §1 acyclicity criterion — "two WKB branches through the same 3-geometry make a graph, not a tree" — the conjugate pair, which shares every $a={\rm const}$ 3-geometry, is that case. *Severity: axiom / presentational.*

**20. §7, second bullet: "a preferred direction in superspace, which Axiom 2 does not forbid (it foliates superspace, not the 4-manifold)."**
Superspace is the space of 3-geometries; "the conformal factor of a node" presupposes a 3-slice. The paper's own text treats this as the violation (`index.tex` ≈ lines 197–206: even Wheeler–DeWitt "smuggl[es] in the foliation through the back door"). The "full superspace / decoherent-histories escape" is not constructed: no function on histories (4-geometries) is offered to play "conformal factor." And $k=\ln(a/a_{\rm root})$ is monotone along the WKB flow, i.e. it is the intrinsic time; "$k$ is a superspace coordinate, not a time coordinate" contradicts the same section's "one timelike direction." METHODOLOGY's "time evolution sneaking back in" warning fires. *Severity: axiom.*

**21. §1/§7 "records point root-ward … via the root being the minimum-excitation state [HH83]" — HH83 says nothing about records, and the no-boundary record arrow is contested exactly where flaw 3 bites.**
The thermodynamic/record arrow in the no-boundary state is Hawking, PRD **32**, 2489 (1985), disputed by Page, PRD **32**, 2496 (1985), and retracted in the relevant part by Hawking–Laflamme–Lyons, PRD **47**, 5342 (1993): "contrary to an earlier claim, the density perturbations do not get small again at the other end of the Universe's history" — on a recollapsing branch records do *not* point toward smaller $a$. With flaw 3 (the framework's own branch is closed and $\Lambda$-free), "records point root-ward" fails on that branch past turnaround. The HH83 citation supports "ground state," not "record asymmetry." *Severity: citation content-mismatch + structural.*

### Minor factual items

**22. §4b Brown–Teitelboim.** The additive steps are in the 4-form flux (charge $e$); $\Lambda_{\rm eff}\propto\Lambda_{\rm bare}+F^2/2$, so $\Delta\Lambda=e(2F-e)/2$ shrinks along the staircase — not "fixed additive steps" in $\Lambda$. Conclusion (not geometric; needs $e$ as input) unchanged. *Presentational.*

**23. §5 RG arithmetic.** 19 orders of running at exponent $0.0304$ changes $(\xi-\tfrac16)$ by a factor $10^{0.58}=3.8$, not "by 0.26." Conclusion (1316 orders needed) unchanged. *Factual, minor.*

**24. §3.3 "the causal Green operator of `fpe-banach-contraction`'s setting."** `ce-riem-classical-unique` records that this result explicitly does *not* transfer to the toy map; using it even as an analogy for "what $F$ would need" should say so. *Scope, minor.*

---

## Claims that held

**C.1 (PSD of the second-iterate Jacobian) — holds as mathematics.** I tried: (i) the reduction. With $U$ an orthonormal basis of $\mathbf 1^\perp$, $S(p)(I-UU^{\mathsf T})=S(p)\mathbf 1\mathbf 1^{\mathsf T}/N=0$, so $U^{\mathsf T}S(b)MU=(U^{\mathsf T}S(b)U)(U^{\mathsf T}MU)$ and, inserting $UU^{\mathsf T}+\mathbf 1\mathbf 1^{\mathsf T}/N$ between $M$ and $S(b)$ and using $\mathbf 1^{\mathsf T}S(b)=0$, $U^{\mathsf T}S(e)MS(b)MU=S_eM_rS_bM_r$ with $S_e,S_b\succ0$ (interior points, which $G$ guarantees) and $M_r=M_r^{\mathsf T}$. That is the whole "coordinate gap"; it is three lines. (ii) The Gram form $S_e^{1/2}M_rS_bM_rS_e^{1/2}=XX^{\mathsf T}$, $X=S_e^{1/2}M_rS_b^{1/2}$ — correct, needs only $M_r$ symmetric. (iii) Numerics: reduction exact to $1.3\times10^{-13}$ relative, $\min{\rm spec}\,D(G\circ G)|_T=-2.4\times10^{-11}$ over 900 random interior points, $\beta\in[0.1,10^3]$ (Script B). (iv) The consequence "no flip, no Neimark–Sacker of the 2-cycle" is valid; a $+1$ crossing of $G\circ G$ at a 2-cycle yields fixed points of $G\circ G$ (period $\le2$), never period 4. Novelty is the consequence, not the algebra (flaw 10).

**C.2 (uniqueness) — holds, and is essentially complete, not a Sketch.** I tried to break each step: $A=\sum_j\alpha_jP_j$ with $(P_j)_{\sigma\sigma'}=[\sigma_j=\sigma'_j]=\sum_v\mathbf 1_{S_v}\mathbf 1_{S_v}^{\mathsf T}$ is PSD for any dims and $\alpha_j\ge0$ (spectrum here $\{0,0.6,1.0,1.6\}$); $M_r=U^{\mathsf T}MU$ is NSD for $\gamma<0,\beta\ge0$; $DG|_T\simeq S^{1/2}M_rS^{1/2}$ NSD, so ${\rm spec}(I-DG|_T)\ge1$, $\det>0$, index $+1$, every fixed point nondegenerate hence isolated; $G$ continuous on the closed simplex into its interior, Lefschetz number 1; sum of indices $=1$ forces exactly one fixed point. The bijection to the paper's $F$ on $\mathbb C^N$ is immediate for $\gamma\in\mathbb R$: every fixed point of $F$ is a positive real unit vector (Prop. `riem_classical`(a)) and $\psi\mapsto|\psi|^2$ matches fixed points of $F$ with fixed points of $G$. Numerically ${\rm spec}\,DG|_T\in[-92.2,3\times10^{-14}]$ across the scan and the fixed point continues to the uniform point without fold (Script B). This closes the uniqueness `ce-riem-classical-unique` leaves open for $\gamma<0,\ \beta\ge0,\ \alpha_j\ge0$, any real $h$, any $N$ — an independent finding worth recording regardless of the attempt's fate. (What it does *not* give: uniqueness for $\gamma>0$, where $M$ is PSD and folds are allowed.)

**θ-inertness for real $h,\alpha,\beta$ — holds.** From the paper's definition $R_\sigma(\psi)=h_\sigma+\sum_j\alpha_jM_j(\sigma_j)+\beta|\psi_\sigma|^2$ with $M_j$ marginals of $|\psi|^2$ (`index.tex` proof of Prop. `riem_classical`; `toy_model.py` `curvature`), $R$ depends on $\psi$ only through $|\psi|^2$; $|F(\psi)_\sigma|^2=e^{2{\rm Re}\gamma R_\sigma}/\sum e^{2{\rm Re}\gamma R}=G(|\psi|^2)_\sigma$. Verified against `CoEmergenceModel.F_map` at $\theta\in\{0,1,3\}$, $\beta\in\{0.4,5,40\}$: max deviation $3$–$6\times10^{-16}$ per step (Script B). The attempt's script tests the same identity.

**$\beta_{\rm flip}=0.648020$ — reproduced** to six digits by bisection on the $DG$ eigenvalue; spectrum at the flip $\{-1.001,-0.451,-0.271,0\}$ at $\beta=0.650$.

**Prediction 4 (no fold-born period-4 orbit) — held under a stronger test than the attempt ran.** Newton on $G^{\circ3}-{\rm id}$ and $G^{\circ4}-{\rm id}$, 300 Dirichlet-random starts each at $\beta\in\{1,3,5,10,20,40,100,400\}$, keeping only roots of minimal period 3 or 4: none (Script C). Unstable orbits would have been found by this method; the iteration-based census could not see them.

**Conjugate-pair statement (§6) — now verified**, via [Le23] rather than [HaHa90]: eq. (173) exhibits the de Sitter no-boundary amplitude as $e^{+12\pi^2/\hbar\Lambda}$ times two complex-conjugate phases, and p. 101 states both saddles have the same weight with "time flow[ing] in opposite directions." The attempt listed [Le23] as "not used for any specific claim"; it is the citation this claim needs.

**Ladder and trilemma arithmetic — reproduced** (depths 17.1/19.7/23.5/31.5/67.8 e-folds at $H=M_P/100$; $r$-versus-depth table; $|I_E|$ targets 138.2/50.7/39.1; anomalous dimension 0.0304).

**LLR exclusion of the literal reading — holds** with the verified bound (flaw 5 corrects only the rate).

---

## Citations re-verified

| Ref | Existence | Content match to the use made |
|---|---|---|
| [HH83] Hartle & Hawking, PRD **28**, 2960 (1983) | Verified (APS) | Supports "ground-state amplitude … compact positive-definite four-geometries with the three-geometry as boundary." The phrase "state of minimum excitation" not verified verbatim (abstract says "ground state"). **Does not support** "records point root-ward" (flaw 21). |
| [HaHa90] Halliwell & Hartle, PRD **41**, 1815 (1990) | Verified (APS/ADS/PubMed) | Abstract is about contour choice; conjugate-pair passage not retrieved. Not needed: [Le23] eq. (173) supplies it. |
| [FLT17] Feldbrugge, Lehners, Turok, PRL **119**, 171301 (2017), arXiv:1705.00192 | Verified (APS, arXiv) | Abstract quotes in §6 accurate; polarity (against a stable saddle from zero size) correct. |
| [DTL19] Di Tucci & Lehners, PRL **122**, 201302 (2019), arXiv:1903.06757 | Verified (APS, arXiv) | Abstract quotes accurate; polarity correct. "Robin parameter fixed by $\Lambda$" **not in the abstract** ("a specific family"); unverified. Condition is at the initial end, not the equator (flaw 18). |
| FLT 2018 "No rescue…" | **Now verified:** Feldbrugge, Lehners, Turok, "No rescue for the no boundary proposal: Pointers to the future of quantum cosmology," PRD **97**, 023509 (2018), arXiv:1708.05104 | Abstract: "no choice of complex contour for the lapse which avoids this problem." Upgrade from "title only." |
| [Le23] Lehners, Phys. Rep. **1022**, 1 (2023), arXiv:2303.08802 | Verified (arXiv, ADS); full text retrieved | Eq. (173) and p. 101 support the conjugate-pair claim and the **positive** exponent $e^{+12\pi^2/\hbar\Lambda}$ (flaw 14). Should be load-bearing, not "not used." |
| [F78] Feigenbaum, J. Stat. Phys. **19**, 25 (1978) | Verified (Springer/ADS) | $\delta=4.669201609\ldots$ for a quadratic maximum. Correct. |
| [BT88] Brown & Teitelboim, Nucl. Phys. B **297**, 787 (1988) | Verified (ScienceDirect/Semantic Scholar) | Stepwise reduction of $\Lambda_{\rm eff}$ by membrane nucleation: correct. Steps are additive in flux, not in $\Lambda$ (flaw 22). |
| LLR bound | **Verified:** Hofmann & Müller, CQG **35**, 035015 (2018) | $\dot G/G=(7.1\pm7.6)\times10^{-14}\,{\rm yr^{-1}}$. Replaces the attempt's "from memory" $10^{-13}$. |
| Gell-Mann–Hartle medium decoherence | Not checked here | Attempt flags as unverified; not load-bearing for this pass. |
| *Attack-side references:* Duff, CQG **11**, 1387 (1994), arXiv:hep-th/9308075 | Verified; eq. (31) read from the PDF | $b'=-[N_S+11N_F+62N_V]/(360(4\pi)^2)$ (flaw 16). |
| Hawking, Hertog, Reall, PRD **63**, 083504 (2001) | Verified (APS/arXiv) | "Nucleated … provided there are sufficiently many matter fields" (flaw 16). |
| Hawking, PRD **32**, 2489 (1985); Page, PRD **32**, 2496 (1985); Hawking, Laflamme, Lyons, PRD **47**, 5342 (1993) | Verified (APS/arXiv gr-qc/9301017) | HLL abstract: density perturbations "do not get small again at the other end," contrary to Hawking 1985 (flaw 21). |
| GitHub #133 / #168 | Verified via `gh api` | #133 closed 2026-07-17 ("Superseded by #168"); #168 open, `agent-ready`, no PRs (flaw 16). |

---

## Appendix — scripts and output (numpy/scipy; nothing written except this file)

### Script B — map reproduction, θ-inertness (real and complex $h$), all flips, C.1 reduction, zoo

```python
import numpy as np, sys; sys.path.insert(0,'programs/co-emergence/tests')
from toy_model import CoEmergenceModel
from scipy.optimize import root, brentq; from scipy.linalg import null_space
h=np.array([1.0,0.7,0.5,1.2]); dims=(2,2); alphas=(0.5,0.3); N=4
idx=np.array(np.unravel_index(np.arange(N),dims)).T; A=np.zeros((N,N))
for j,a in enumerate(alphas): A+=a*(idx[:,j][:,None]==idx[:,j][None,:])
def G(q,b,gam=-1.0): z=2*gam*(h+A@q+b*q); z-=z.max(); w=np.exp(z); return w/w.sum()
def S(p): return np.diag(p)-np.outer(p,p)
def DG(q,b,gam=-1.0): return S(G(q,b,gam))@(2*gam*(A+b*np.eye(N)))
rng=np.random.default_rng(0)
for theta in (0.0,1.0,3.0):                       # |F psi|^2 == G(|psi|^2), real h
    for b in (0.4,5.0,40.0):
        mdl=CoEmergenceModel(dims,h,list(alphas),b,-1.0+1j*theta); psi=rng.normal(size=N)+1j*rng.normal(size=N); psi/=np.linalg.norm(psi); d=0
        for _ in range(200): q=np.abs(psi)**2; psi=mdl.F_map(psi); d=max(d,np.abs(np.abs(psi)**2-G(q,b)).max())
        print(theta,b,d)
hc=h+0.3j*np.array([1,-1,0.5,0.2])               # complex h: theta is NOT inert
for theta in (0.0,1.0):
    mdl=CoEmergenceModel(dims,hc,list(alphas),5.0,-1.0+1j*theta); psi=rng.normal(size=N)+1j*rng.normal(size=N); psi/=np.linalg.norm(psi)
    for _ in range(3000): psi=mdl.F_map(psi)
    print("complex h",theta,np.abs(psi)**2)
def fp(b):
    res=lambda x:(G(np.append(x,1-x.sum()),b)-np.append(x,1-x.sum()))[:N-1]
    x=root(res,np.ones(N-1)/N,tol=1e-14).x; return np.append(x,1-x.sum())
prev=None; crossings=[]
for b in np.concatenate([np.linspace(0.1,3,59),np.linspace(3.2,60,285)]):
    ev=np.sort(np.linalg.eigvals(DG(fp(b),b)).real)
    if prev is not None: crossings+=[(i,b) for i in range(N) if (prev[i]+1)*(ev[i]+1)<0]
    prev=ev
for i,b in crossings: print("flip",i,brentq(lambda x:np.sort(np.linalg.eigvals(DG(fp(x),x)).real)[i]+1,b-0.25,b+0.05,xtol=1e-10))
U=null_space(np.ones((1,N))); worst=0; mn2=1e9           # C.1: reduction exactness and PSD
for b in np.logspace(-1,3,30):
    M=-2*(A+b*np.eye(N)); Mr=U.T@M@U
    for _ in range(30):
        a=rng.dirichlet(np.ones(N)*rng.uniform(0.2,3)); bb=G(a,b); e=G(bb,b); Sb=U.T@S(bb)@U; Se=U.T@S(e)@U
        full=U.T@(S(e)@M@S(bb)@M)@U; red=Se@Mr@Sb@Mr
        worst=max(worst,np.linalg.norm(full-red)/max(1,np.linalg.norm(full))); mn2=min(mn2,np.linalg.eigvals(red).real.min())
print("reduction",worst,"min eig",mn2)
def period(b,q0,nwarm=40000,maxp=64,tol=1e-9):
    q=q0.copy()
    for _ in range(nwarm): q=G(q,b)
    tr=[q]
    for _ in range(maxp): q=G(q,b); tr.append(q)
    for p in range(1,maxp+1):
        if np.linalg.norm(tr[p]-tr[0])<tol: return p,tr
    return -1,tr
for b in (2.0,5.0,20.0,40.0,100.0):                 # the zoo
    cyc=[]
    for s in range(40):
        p,tr=period(b,rng.dirichlet(np.ones(N)))
        if p==2:
            pt=min(tr[0],tr[1],key=lambda v:tuple(np.round(v,6)))
            if not any(np.linalg.norm(pt-c)<1e-6 for c in cyc): cyc.append(pt)
    print("beta",b,"distinct attracting 2-cycles",len(cyc))
```
Output: real-$h$ θ-check $3.3$–$5.6\times10^{-16}$ at every $(\theta,\beta)$; complex $h$: $\theta=0$ → $(0.0137,0.0001,0.8764,0.1098)$, $\theta=1$ → $(0.0480,0.00003,0.8336,0.1183)$; ${\rm spec}\,A=\{0,0.6,1.0,1.6\}$; fixed-point spectra $\beta=0.65$: $\{-1.0012,-0.4506,-0.2713,0\}$, $\beta=2$: $\{-1.761,-1.073,-0.896,0\}$, $\beta=40$: $\{-20.92,-20.06,-19.81,0\}$; **flips at $\beta=0.648020,\ 1.848777,\ 2.218503$**; reduction $1.26\times10^{-13}$, $\min$ eig $-2.38\times10^{-11}$; zoo: 1, 1, 5, 7, 7 attracting 2-cycles at $\beta=2,5,20,40,100$.

### Script C — later flips spawn 2-cycles; Newton census for period 3 and 4

```python
def Gn(q,b,n):
    for _ in range(n): q=G(q,b)
    return q
def fp_of(n,b,q0):
    res=lambda x:(Gn(np.append(x,1-x.sum()),b,n)-np.append(x,1-x.sum()))[:N-1]
    sol=root(res,q0[:N-1],tol=1e-13); q=np.append(sol.x,1-sol.x.sum())
    return q, sol.success and np.all(q>0) and np.linalg.norm(Gn(q,b,n)-q)<1e-10
def minimal_period(q,b,n):
    for p in range(1,n+1):
        if np.linalg.norm(Gn(q,b,p)-q)<1e-8: return p
    return n
for bflip in (1.848777,2.218503):
    b=bflip+0.02; q=fp(b); ev,V=np.linalg.eig(DG(q,b)); v=np.real(V[:,np.argmin(abs(ev+1))]); v-=v.mean()
    q2,ok=fp_of(2,b,q+0.05*v/np.linalg.norm(v)); print(b,ok,minimal_period(q2,b,2),np.linalg.norm(q2-q))
rng=np.random.default_rng(3)
for b in (1.0,3.0,5.0,10.0,20.0,40.0,100.0,400.0):
    found={3:set(),4:set()}
    for n in (3,4):
        for s in range(300):
            q,ok=fp_of(n,b,rng.dirichlet(np.ones(N)*rng.uniform(0.1,3)))
            if ok and minimal_period(q,b,n)==n: found[n].add(tuple(np.round(min([Gn(q,b,k) for k in range(n)],key=lambda v:tuple(np.round(v,6))),6)))
    print(b,len(found[3]),len(found[4]))
```
Output: $\beta=1.8688$: 2-cycle found, minimal period 2, distance $0.0613$; $\beta=2.2385$: found, period 2, distance $0.0650$. Period-3 / period-4 orbits: **0 / 0** at every $\beta$ tested.

### Script A2 — conventions, instanton actions, inflation e-folds, freeze epochs, rates

```python
import numpy as np; MP=1.2209e28; hbar=6.582e-16; H0=67.4/3.0857e19; H0eV=H0*hbar
for a2 in (1e3,1e4,1e5):
    Hc=MP/np.sqrt(a2); Hr=np.sqrt(180*np.pi/a2)*MP
    print(a2,Hc,Hr,Hr/Hc,np.pi*MP**2/Hc**2,np.pi*MP**2/Hr**2,[(t,Hc/hbar*t,Hr/hbar*t) for t in (1e-42,1e-40)])
HS=MP/np.sqrt(1e4)
for k,m in (("top",1.73e11),("proton",9.38e8),("electron",5.11e5),("nu",0.05),("H0",H0eV)): print(k,np.log10(HS/m),0.5*np.log(HS/m))
for k,m in (("top",1.73e11),("electron",5.11e5)): print(k,(m**2*MP**2*90/(8*np.pi**3*100))**0.25/1e9,"GeV")
print(-(1-0.55)*H0*3.156e7, -2*H0*3.156e7, 10**(19*4.8/(16*np.pi**2)))
S=4+11*22.5+62*12; a2=S/2; print("SM a2",a2,"H/MP",np.sqrt(180*np.pi/a2),"|I_E| repo",a2/180)
```
Output: $H_{\rm repo}/H_{\rm can}=23.8$ for all $a_2$; $|I_E|$ (canonical, repo) $=(3142,5.56)$, $(31416,55.6)$, $(314159,556)$ for $a_2=10^3,10^4,10^5$; $N_{\rm inf}=H\tau$ at $a_2=10^4$: canonical $(0.19,18.6)$, repo $(4.4,441)$ for $\tau=(10^{-42},10^{-40})$ s; depths (radiation) top 17.1, proton 19.7, electron 23.5, $\nu$ 31.5, $H_0$ 67.8; $H=m_t$ at $T=1.13\times10^{10}$ GeV, $H=m_e$ at $1.94\times10^{7}$ GeV; $\dot m/m$: $-3.1\times10^{-11}$ vs $-1.38\times10^{-10}\ {\rm yr^{-1}}$; RG factor over 19 orders $3.78$; SM: $a_2=497.75$, $H/M_P=1.066$, $|I_E|=2.77$.
