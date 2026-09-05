# Steelman pass on Attempt C — "Hierarchies from the tree of histories"

**Target:** `/home/will/Projects/physagent/attempt-C-tree-hierarchy.md`, answering `/home/will/Projects/physagent/attack-C.md`.
**Date:** 2026-09-05.
**Role:** Steelman / defense pass (Pass 2 of METHODOLOGY "No Idea Is Eliminated Without a Defense"). Verdict codes per flaw: **fatal** / **solvable gap** / **narrower-but-viable** / **framing**.

Everything numerical below was re-run from scratch (scripts S1–S6, appendix; the repo's `programs/co-emergence/tests/toy_model.py` is imported and its `F_map` is the object iterated). External references are web-verified unless marked. Where the attack is simply right I say so in one line.

**Headline.** The attack is right on the committed mechanism: the branch structure generates no scale other than $\Lambda^{1/2}$, and the strongest honest form of the attempt is a *negative* answer to the mass test with the adaptation named. The attack is also right about what C.1 does and does not prove, and about the miscount of branchings. But two things the attack left as "numerical" or "essentially complete" can be closed as **Rigorous**, both by routes the repo's own record pointed at and nobody executed: (i) the period of *every* periodic orbit of the toy map is 1 or 2, for **all** complex parameters, by an explicit Lyapunov function (new claim C.3 below, with full proof; prior art Marcus–Westervelt 1989 / Koiran 1994) — this is the "dead structurally" the attempt wanted and C.1 could not deliver; (ii) uniqueness of the fixed point (C.2) is Rigorous by strict convexity of an entropy-regularized potential, which turns out to be exactly Wang's Theorem 3 (arXiv:2605.15651, verified) — the route `ce-riem-classical-unique` recommended on 2026-07-24. On the tree/orientation side, the Hawking–Laflamme–Lyons retraction the attack cites *supports* a narrowed "records point root-ward" (root = the end where perturbations were in their ground state, constant through recollapse) and kills only the "root-ward = smaller $a$" definition.

---

## Flaw-by-flaw

### The committed mechanism (§5, e-fold ladder)

**1. The depth is a coordinate along one WKB branch; the tree contributes nothing. — Verdict: fatal for the claim as stated; narrower-but-viable only as a *discrete* rung set, which still fails the mass test.**
I tried to find a narrowing under which "the tree generates rungs" is a statement about the tree. The only one that holds up: the framework's root is a half-$S^4$, so every branch has $S^3$ slices, and perturbation modes are integer-labeled (harmonic number $n$). Mode $n$ exits the horizon in the de Sitter phase at $a_n = n\,a_{\rm root}$ (since $a_{\rm root}=1/H$), i.e. at $\ln(a/a_{\rm root}) = \ln n$ — a genuinely *discrete* sequence of decoherence events whose discreteness comes from the root's topology, not from FRW. Their re-entry scales on the radiation branch are $m_n = n/a_n' = n^2 H e^{-2N_{\rm inf}}$, a quadratic ladder $m_n = H\,(n/n_{\max})^2$, $n_{\max}\sim e^{N_{\rm inf}}$. So nodes exist and carry scales. But every scale is still $\Lambda^{1/2}\times$ (a dimensionless function of $n$, $N_{\rm inf}$, $a_2$), the ratio between adjacent rungs is $(1+1/n)^2\to1$ (dense, not geometric), and a species' rung is an integer $n_s$ nobody selects. The attack's core statement stands: the mass test is answered **no**. (Mode-by-mode decoherence at horizon exit is standard cosmology; I have not verified a specific citation for it and it is not load-bearing.)
*Honest residue:* "The branch structure generates no hierarchy; the ladder is the thermal history of one branch; what the tree adds is at most a discrete, integer-labeled rung set and a reach ($2N_{\rm inf}$, flaw 3), both dimensionless."

**2. Depth accounting drops the de Sitter phase. — Verdict: attack right (factual); the number it exposes is a computable property of the root, which is the adaptation.**
Recomputed (S4). With the repo's window $\tau\in[10^{-42},10^{-40}]$ s: $N_{\rm inf}=H\tau\in[0.19,18.5]$ for $H=M_P/\sqrt{a_2}$ and $[4.4,441]$ for the printed $H^2=180\pi M_P^2/a_2$ ($a_2=10^4$). The electron rung is at $N_{\rm inf}+23.5$ (canonical) or $N_{\rm inf}+25.0$ (printed) e-folds from the root, undetermined by the record. The rescue is not to fudge the window: $N_{\rm inf}=\tau_{\rm decay}/t_{\rm Hubble}$ is a dimensionless ratio the framework in principle computes from the anomaly-driven instability (Starobinsky 1980 gives the decay; my recollection is that the timescale is controlled by the scheme-dependent $\Box R$ coefficient — **unverified**). That computation is the named open item; see "What the rescue could not do."

**3. The post-decay branch is closed and $\Lambda$-free, so it recollapses; reach $\le 2N_{\rm inf}$; order breaks at turnaround. — Verdict: attack right on structure; the "neither rung is reached" conclusion depends on the loose window; the order problem is fixed by the causal-order definition in flaw 20.**
Reproduced (S4): $H^2(k)=H_{\rm dS}^2e^{-2k}[e^{-2k+4N_{\rm inf}}-1]$, zero at $k=2N_{\rm inf}$. Electron rung reached iff $N_{\rm inf}\ge23.5$; with the canonical $H$ and the literal window ($N_{\rm inf}\le18.5$) it is not, with the printed $H$ it is for $\tau\gtrsim5\times10^{-42}$ s. Any inflationary reading of the root needs $N_{\rm inf}\gtrsim60$ anyway, so the bound is an artifact of a window never meant to pin $N_{\rm inf}$ — but the *structural* points are untouched: the ladder bottoms out at $H=0$ at finite depth, and $H_{0,\rm obs}$ is unreachable without $\Lambda_{\rm obs}$, which is the second scale the attempt disclaims (this is the 60-order mismatch `fpe-fixed-point-is-inflationary` already records). On "two nodes at the same $a$ are incomparable past turnaround": true for the conformal-factor order; false for the causal order relative to $\Sigma$ (flaw 20), which remains a partial order on a globally hyperbolic recollapsing branch.

**4. "Species' branch point" names no event. — Verdict: fatal for the record reading as a *mechanism*; it survives only as the *definition* of the address.**
Conceded. $H=m_t$ at $T\approx10^{10}$ GeV and $H=m_e$ at $T\approx2\times10^{7}$ GeV are epochs at which nothing happens to those species. I looked for a repo-internal mechanism: the only curvature-set mass is $m_{\rm eff}^2=(\xi-\tfrac16)R$ (eq. `meff`), which vanishes on the radiation branch. "Mass is a record of $H$ at the branch point" is $k_s\equiv\tfrac12\ln(H/m_s)$, a relabeling. The attempt's own §5 said the ladder fails the selection test; the attack shows the "record" gloss adds nothing.

**5. Wrong rate, right conclusion. — Verdict: attack right (minor).** $\dot m/m=\dot H/H=-(1+q_0)H_0=-3.1\times10^{-11}\,{\rm yr^{-1}}$ (S4), three orders above the LLR bound $\dot G/G=(7.1\pm7.6)\times10^{-14}\,{\rm yr^{-1}}$ (Hofmann & Müller 2018, verified by the attack; not re-fetched). Literal reading excluded either way.

**6. $w=1/3$ is imported thermal history, not a repo assumption; the ratio is not universal along the branch. — Verdict: attack right (framing).** The repo records the fixed point and its instability, not reheating. The ladder is standard cosmology relabeled.

**7. "Natural depth 20–70 e-folds" equivocates de Sitter and radiation e-folds; Feigenbaum $\delta$ vs $\alpha$. — Verdict: attack right (presentational).** $\alpha=2.5029$ is the orbit-scale ratio; $\delta$ is a parameter-interval ratio; the trilemma table should have used $\alpha$ for $m({\rm child})/m({\rm parent})$ and said so. Depth 150.6 for 60 orders — the conclusion (depth $\sim10^2$ for any $O(1)$ ratio) is unchanged.

### The bifurcation tree of $F$ (§3)

**8. "Exactly one branching / depth 1" is false: the fixed point flips $N-1$ times and folds of $G\circ G$ occur. — Verdict: attack right (factual); corrected statement below; the attempt's *conclusion* (no hierarchy from mechanism iii) survives and is strengthened.**
Reproduced independently (S3, S5, S6). Flips of the unique fixed point of the canonical $N=4$ instance at $\beta=0.648020,\ 1.848777,\ 2.218503$; its tangent spectrum at $\beta=40$ is $\{-20.92,-20.06,-19.81\}\approx-2\beta/N$, so all $N-1$ multipliers cross $-1$. Complete census of ${\rm Fix}(G\circ G)$ — complete in the checkable sense that the Lefschetz–Hopf index sum over all points found equals 1 (S6; seeds on every face of the simplex in log coordinates):

| $\beta$ | fixed points of $G$ | 2-cycles (attracting) | unstable multipliers per 2-cycle | index sum |
|---|---|---|---|---|
| 5 | 1 | 5 (1) | 0,1,1,2,2 | 1 |
| 10 | 1 | 13 (3) | 0×3, 1×6, 2×4 | 1 |
| 20 | 1 | 19 (5) | 0×5, 1×9, 2×5 | 1 |
| 40 | 1 | 25 (7) | 0×7, 1×12, 2×6 | 1 |
| 100 | 1 | ≥22 (7) | — | −5 (census incomplete) |

Only 3 orbits are flip-born; the rest are fold-born. The record's "up to 7" zoo counts attracting orbits only; saddles outnumber them $\sim2.5:1$. **Corrected claim about the tree of $F$:** one root (unique fixed point, C.2); $N-1$ flip branchings of the root; an unbounded-with-$\beta$ number of fold births of 2-cycles; *no other branching of any kind* (C.1 forbids flip/Neimark–Sacker of 2-cycles; C.3 below forbids any period $\ge3$). The branch parameters $\beta_i$ have non-universal $O(1)$ ratios (2.85, 1.20) set by $(h,\alpha)$, and all cycle points live in a bounded simplex: mechanism (iii) generates *more* structure than the attempt said and *still* no scale hierarchy.

**9. "Dead structurally (Rigorous)" overclaims C.1. — Verdict: attack right about C.1; but the label is rescued by a different theorem (C.3), which makes the cascade exclusion Rigorous *and global*.**
The attack's decomposition — "no doubling from the 2-cycle (Rigorous); no other route found (numerical)" — is exactly what C.1 supports, and the attack's own Newton census (period 3/4: none) is reproduced (S3: none at $\beta\in\{2,5,20,40,100,400\}$). What closes the gap is not C.1 but the following.

> **Claim C.3 (period cap; Rigorous — proof in full).** Let $\mathrm{dims}$ be arbitrary, $N=\prod d_j$, and let $h\in\mathbb C^N$, $\alpha\in\mathbb C^k$, $\beta\in\mathbb C$, $\gamma\in\mathbb C$ be **arbitrary complex** parameters of the toy map $F(\psi)=w/\|w\|_2$, $w_\sigma=e^{\gamma R_\sigma(\psi)}$, $R_\sigma=h_\sigma+\sum_j\alpha_jM_j(\sigma_j)+\beta|\psi_\sigma|^2$ (`toy_model.py`). Then every periodic orbit of $F$ has period 1 or 2, and every orbit's $\omega$-limit set consists of fixed points of $F\circ F$. In particular there is no period-doubling cascade, no period-$\ge3$ orbit and no invariant circle, at any parameter values.
>
> *Proof.* (i) *Reduction.* With $q=|\psi|^2\in\Delta$ (the closed simplex), $R(\psi)=h+(A+\beta I)q$ is affine in $q$, $A=\sum_j\alpha_jP_j$, $(P_j)_{\sigma\sigma'}=[\sigma_j=\sigma'_j]$. Hence $|F(\psi)_\sigma|^2=e^{2\,{\rm Re}(\gamma R_\sigma)}/\sum_\tau e^{2\,{\rm Re}(\gamma R_\tau)}$, i.e. $q_{t+1}=G(q_t):={\rm softmax}(c+2Wq_t)$ with $c=2\,{\rm Re}(\gamma h)\in\mathbb R^N$ and $W={\rm Re}\big(\gamma(A+\beta I)\big)\in\mathbb R^{N\times N}$, which is **symmetric** because every $P_j$ and $I$ is symmetric. (Verified against `F_map` to $10^{-12}$ per step on 60 random instances with complex $h,\alpha,\beta,\gamma$; S1.) The phases of $\psi_{t+1}=F(\psi_t)$ are functions of $q_t$ alone, so the period of $(\psi_t)$ equals the period of $(q_t)$.
> (ii) *Variational step.* Let $\Phi(p)=\sum_\sigma p_\sigma\ln p_\sigma$ on $\Delta$ ($0\ln0=0$), continuous and strictly convex. For any $z\in\mathbb R^N$, $\arg\min_{p\in\Delta}[\Phi(p)-p^{\mathsf T}z]$ is unique, interior ($\partial_\sigma\Phi\to-\infty$ as $p_\sigma\to0$), and by the Lagrange condition $\ln p_\sigma+1-z_\sigma=\lambda$ equals ${\rm softmax}(z)$.
> (iii) *Lyapunov function on pairs.* $L(p,q):=\Phi(p)+\Phi(q)-2p^{\mathsf T}Wq-c^{\mathsf T}(p+q)$ on $\Delta\times\Delta$. By (ii), $L(G(q),q)\le L(p,q)$ for all $p$, with equality iff $p=G(q)$. By symmetry of $W$, $L(p,q)=L(q,p)$. Along an orbit, $L(q_{t+1},q_t)\le L(q_{t-1},q_t)=L(q_t,q_{t-1})$, equality iff $q_{t+1}=q_{t-1}$. So $\ell_t:=L(q_{t+1},q_t)$ is non-increasing and bounded below ($L$ is continuous on a compact set), hence convergent. (S1: max increase of $\ell_t$ over 60 instances $\times$ 4000 steps $=7\times10^{-15}$.)
> (iv) *Periods.* On a periodic orbit $\ell_t$ is periodic and non-increasing, hence constant, so $q_{t+1}=q_{t-1}$ for all $t$: the period divides 2.
> (v) *Limit sets.* Let $T(p,q)=(G(p),p)$ on $\Delta\times\Delta$; then $(q_{t+1},q_t)$ is a $T$-orbit and $L(T(x))\le L(x)$ with equality iff $G(p)=q$. The $\omega$-limit set $\Omega$ of a $T$-orbit is nonempty, compact, $T$-invariant, and $L\equiv\ell_\infty$ on $\Omega$. For $(p,q)\in\Omega$: $T(p,q)\in\Omega$ gives $L(T(p,q))=L(p,q)$, so $G(p)=q$; then $T(p,q)=(q,p)\in\Omega$ gives $G(q)=p$. Hence $q=G(G(q))$. $\square$
>
> If ${\rm Fix}(G\circ G)$ is finite (true whenever all its points are nondegenerate — generic, and the case at every parameter value tested), every orbit converges to a single fixed point or 2-cycle.

**Prior art (verified existence; content from abstracts):** Marcus & Westervelt, *Dynamics of iterated-map neural networks*, Phys. Rev. A **40**, 501 (1989): for symmetric connections the only attractors of the synchronous iterated map are fixed points and period-two cycles, via a Lyapunov function on consecutive states. Koiran, *Dynamics of discrete time, continuous state Hopfield networks*, Neural Computation **6**, 459 (1994): parallel iteration with symmetric weights converges to a cycle of length 1 or 2. C.3 is the softmax/entropy instance (the entropy is the Legendre conjugate of log-sum-exp, which is why no diagonal condition is needed). `ce-second-iterate-real-spectrum`'s novelty note says "the nearby literature shows cascades CONTINUING past period 2 in related map classes, so a cap at 2 is not the expected default" — for *symmetric synchronous* networks the cap at 2 is the expected default and has been a theorem since 1989; the record missed the connection. No Lyapunov-function route appears anywhere in the co-emergence claims (grep: none).

**Corrected label for §3:** mechanism (iii) is dead for cascades **(Rigorous, by C.3)**; dead for a scale hierarchy **(numerical: fold births at non-universal $O(1)$ spacings)**. C.3 also explains the attempt's §3.3: non-symmetric $W$ is precisely the failure of C.3's one hypothesis, so the observed Neimark–Sacker circles and period-3 orbits are what the theorem's negation permits. In framework terms: **a reciprocal self-consistency kernel cannot branch beyond period 2; branch structure richer than that requires a non-reciprocal kernel, which presupposes an orientation.** That is the attempt's §3.3 conclusion, now with the reason.

**10. Misquotes the record; claims the wrong novelty. — Verdict: attack right (factual).** The record's gap is "does not explain WHY the second-iterate spectral radius decays to ~0.037"; its `consequence` already claims the cap is explained. PSD is one line from the record's palindrome $Z=S_e^{1/2}MS_bMS_e^{1/2}=XX^{\mathsf T}$ with $X=S_e^{1/2}MS_b^{1/2}$ (S3 re-verifies: chain-rule $D(G\circ G)|_T$ equals $S_eM_rS_bM_r$ to $10^{-13}$; min eigenvalue $-2.7\times10^{-12}$; max $|{\rm Im}|$ $2\times10^{-14}$). What C.1 adds is the bifurcation consequence (2-cycles cannot flip or NS), now subsumed by C.3.

**11. Feigenbaum reason wrong. — Verdict: attack right.** The cascade is flips of $G^{\circ2^n}$; folds make windows. The correct reason is C.1/C.3.

**12. θ-inertness overstated for complex parameters. — Verdict: attack right on wording; corrected scope stated.** From the paper (Prop. `riem_classical`, hypotheses $\gamma\in\mathbb R$, $h\in\mathbb R^N$; §Finite toy model uses $h\sim{\rm Uniform}[0.5,1.5]$): the paper's scope is real $h,\alpha,\beta$, where θ is inert (magnitude map independent of θ, phases slaved to $\theta R_\sigma$). `toy_model.py` stores $h$ as complex and accepts complex $h$; then $c=2{\rm Re}(\gamma h)=-2{\rm Re}\,h-2\theta\,{\rm Im}\,h$ and the magnitude fixed point moves with θ (attack's example). The correct statement is C.3(i): the **class** — symmetric softmax iteration — is unchanged for all complex parameters, so the period cap (C.3) and uniqueness (C.2, under its definiteness condition on $W$) persist; **inertness** holds only for the paper's real parameters.

**13. "Tree-directed" $T$ is a total order on smooth structures, not a tree. — Verdict: attack right (label decorative).** The NS finding stands, and by C.3 it is now the *expected* behavior for a non-symmetric kernel.

### The instanton-weight route (§4c) and #133/#168

**14. Sign: the no-boundary weight is $e^{+|I_E|}$. — Verdict: attack right; fatal for (ii-c) as a mass mechanism in the HH reading.**
Verified three ways: (a) definition $\Psi_{\rm HH}\sim e^{-I_E}$ (Vilenkin, *Approaches to quantum cosmology*, PRD **50**, 2581 (1994), eq. 1.3, verified via ar5iv); (b) $I_E(S^4)=-(1/16\pi G)\int(R-2\Lambda)\sqrt g=-3\pi/(G\Lambda)=-\pi M_P^2/H^2<0$ (S4; half-sphere $-\pi M_P^2/2H^2$, i.e. $-12\pi^2/\Lambda$ in $8\pi G=1$ units); (c) the tunneling weight is $e^{-3/(8G^2\rho_v)}$ (Vilenkin 1994 eq. 3.17, verified) and $3/(8G^2\rho_v)=3\pi/(G\Lambda)$, HH differing "by a crucial difference in sign" (search-result text; Lehners' review eq. (173) as verified by the attack, not re-fetched here — the PDF exceeded the fetch limit). The narrowest residue: *relative* weights of two branches from one root, $e^{-(I_1-I_2)}$, can be suppressions, and in the HH state a nested-$\Lambda_k$ tree would weight branches as $e^{+3\pi/(G\Lambda_k)}$ — a hierarchy of *probabilities* favoring small $\Lambda$ (the standard "HH prefers empty universes" problem), not of masses. Mass $=$ tunneling weight needs a postulate the framework does not have; the attempt conceded this.

**15. $|I_E|=\pi M_P^2/H^2$ is the pure-$\Lambda$ action; the anomaly-driven root has no $\Lambda$. — Verdict: attack right.** Reproduced: the Einstein–Hilbert part on the $\Lambda$-free $S^4$ is $-2\pi M_P^2/H^2=-a_2/90$ at the fixed point, plus the conformal fields' $\ln(H/\mu)$ term whose coefficient is the integrated anomaly $\int\langle T\rangle\sqrt g=-a_2/45$ (S4; consistency check: stationarity of $-2\pi a^2/G+(a_2/45)\ln a$ in the radius reproduces $H^2=180\pi/(Ga_2)$ exactly). Either way $|I_E|=O(a_2)$, and with the sign of flaw 14 the route is dead regardless.

**16. "Decided entirely by #133" — stale and wrong target. — Verdict: attack right on the issue state and on the SM number; precise statement of what its verification does and does not establish:**
`gh issue view 168`: open, `agent-ready`, body "Supersedes #133"; #133 closed 2026-07-17. Reproduced from Duff's eq. (31) convention (S4): $a_2=\tfrac12(N_S+11N_F+62N_V)$, SM ($4,\,22.5,\,12$): $a_2=497.8$, $H/M_P=1.066$, $|I_{\rm EH}|=a_2/90=5.5$ — no hierarchy; the attempt's window $|I|\in[39,138]$ needs $N_S+11N_F+62N_V\in[7\times10^3,2.5\times10^4]$. The route hinges on field content, not on #168.
*What the attack's derivation establishes:* in natural units ($\hbar=c=1$, $G=M_P^{-2}$) the printed $H_0^2=180\pi/(Ga_2)$ follows from the standard field-content-summed Euler coefficient ($b'$ of Duff 1994) plus $E|_{dS}=24H^4$ plus the trace of the semiclassical Einstein equation — a third derivation, this one anchored to an external normalization, which is exactly the "field-content normalization" the paper's Rigor-status note says Capper–Duff does not supply. *What it does not establish:* it does not touch the dimensional-convention defect (remedy: state $\hbar=c=1$ at the equation — trivial, per the defect's own remedy line), and it does not adjudicate the "16π discrepancy with Linde's form." One observation for #168, **hypothesis only, not resolved here:** in reduced-Planck units ($8\pi G=1$) the printed formula reads $H^2=1440\pi^2/a_2=2880\pi^2/(N_S+11N_F+62N_V)$, which is Linde's $H^{-2}=k_2/2880\pi^2$ iff $k_2\equiv N_S+11N_F+62N_V=2a_2$. The recorded factor $16\pi=8\pi\times2$ would then be entirely conventional ($8\pi$ from $G=1$ vs $8\pi G=1$, $2$ from $k_2$ vs $a_2$). Whether that is Starobinsky's/Linde's $k_2$ is for #168 to check against the primary text.

**17. $H$ convention mixed ($M_P/\sqrt{a_2}$ vs $\sqrt{180\pi/a_2}\,M_P$). — Verdict: attack right (minor).** Ratio 23.8 in $H$, 1.6 e-folds in every depth (S4). Both sets of depths are given in flaw 2/3 above.

### Root uniqueness and orientation (§6, §7)

**18. The SCB ↔ Robin analogy misplaces the condition and inverts the polarity. — Verdict: attack right on the analogy (withdrawn); the *conclusion* "the framework needs the DTL side and the rescue adds no scale" survives on different grounds, as a narrower claim.**
Verified from DTL's full text (ar5iv): the condition is imposed at $t=0$, "$\mathcal B\equiv\frac{3\pi^2}{N}\dot q_0+\alpha+q_0/\beta=0$," with Dirichlet $q(1)=q_1$ at the final end; the Hartle–Hawking saddles arise for $\alpha=-6\pi^2i$ — a **pure number** (the Euclidean momentum that closes the geometry off), *not* fixed by $\Lambda$; the second parameter must lie in $1/(3\pi^2H^2)<|\beta|<1/(\pi^2H^2)$. So the attempt's "Robin parameter fixed by $\Lambda$" is wrong for $\alpha$ and only window-wise right for $\beta$. The SCB bounded-$\mathcal H$ condition is at the equator, where the HH geometry has $K=0$ exactly; it selects nothing there. Analogy withdrawn.
*Narrowed claim that holds:* the framework's root is required to be the minimum-excitation state (HH83 "ground state"), i.e. the saddle with **suppressed** fluctuations and weight $e^{+|I_E|}$; the FLT result (verified abstracts, both 2017 and the 2018 "No rescue") is that a Lorentzian path integral with Dirichlet $q_0=0$ does not deliver that saddle; DTL's Robin family does. So *if* the framework's Riemannian region is to be realized as a saddle of a Lorentzian path integral at all, the DTL side is the one it needs — and that side costs one parameter $\beta$ confined to a $\Lambda$-set window of width a factor 3, hence **no new scale**, though it is a new input. The framework as a block-universe proposal imposes regularity on the *classical* cap directly and need not commit to a path-integral definition; that is a framing point, not a derivation.

**19. Two saddles, one root confirms §7's concession. — Verdict: framing; attack right.** The conjugate pair is a $\mathbb Z_2$ that reverses WKB orientation and leaves the $a$-order invariant — which is to say the $a$-order *is* the intrinsic-time order, as the attempt's §7 already conceded. It is not a merge (recoherence) in the sense of the acyclicity criterion, so "graph not tree" is too strong; but nothing about orientation is derived from the pair. Lehners' review p. 101 / eq. (173) (attack-verified; my fetch of the ar5iv rendering did not reach that section) is the right citation and should replace [HaHa90] as load-bearing.

**20. Superspace preferred direction presupposes a slice; $k=\ln a$ is intrinsic time. — Verdict: narrower-but-viable via a foliation-free definition of "root-ward"; the ladder itself stays minisuperspace-bound.**
Attack right that "conformal factor of a node" needs a 3-slice, that the paper's own text (`index.tex` ≈ lines 197–206) treats the WDW slice as the back-door foliation, and that "$k$ is a superspace coordinate, not a time coordinate" contradicts "one timelike direction." The rescue: replace the conformal-factor order by the **causal order relative to $\Sigma$**. The SCB expanding-region note (§3, Rigorous on the fixed background) shows timelike geodesics reach $\Sigma$ at finite proper time and have no timelike continuation into the Riemannian region — $\Sigma$ is an initial boundary of every Lorentzian branch. On a globally hyperbolic branch the causal past relation is a partial order on *events* with no foliation, and $\Sigma$ fixes which of the two time orientations is "root-ward." This is a time *orientation*, which Axiom 1 (no evolution parameter) and Axiom 2 (no preferred foliation) do not forbid; it survives turnaround (flaw 3). What it does *not* do: derive anything beyond the causal structure the branch already has, or free the *ladder* from the slicing — $H(a)$ is a minisuperspace quantity and inherits the foliation. So the orientation argument narrows to: "the tree order is the causal order with $\Sigma$ as initial boundary; it re-expresses, not derives, the branch's time orientation."

**21. "Records point root-ward" cites HH83, which says nothing about records; HLL 1993 retracted the arrow reversal. — Verdict: citation mismatch conceded; on substance the attack overreaches — HLL *supports* the narrowed claim.**
Verified: Hawking, PRD **32**, 2489 (1985), abstract: the arrow "arises because in the proposed quantum state the Universe would have been smooth and homogeneous when it was small but irregular and inhomogeneous when it was large"; Page, PRD **32**, 2496 (1985) (existence); Hawking–Laflamme–Lyons, PRD **47**, 5342 (1993), abstract verbatim: "density perturbations … are small at one end of the universe's history, but grow larger and become non linear as the universe gets larger. Contrary to an earlier claim, the density perturbations do not get small again at the other end of the universe's history. They therefore give rise to a Thermodynamic Arrow of Time that points in a constant direction while the universe expands and contracts again. The Arrow of Time does not reverse at the point of maximum expansion." That is precisely "records point away from the end where the perturbations were in their ground state, throughout." What HLL kills is the identification root-ward $=$ smaller $a$ (Hawking 1985's version), i.e. the conformal-factor definition — the same one flaw 20 replaces. **Narrowed claim (Sketch, by citation to HLL):** on a closed no-boundary branch, the record arrow points away from the low-excitation end and does not reverse at recollapse; "root" must be defined as that end (equivalently, the causal-order initial boundary $\Sigma$), not as the locus of minimum $a$. Correct citations: Hawking 1985 + HLL 1993, not HH83. HLL note the direction is fixed only up to the anthropic choice of which end we call the past; for the tree that is the choice of root, which the junction $\Sigma$ makes structurally.

### Minor items

**22. Brown–Teitelboim steps are additive in flux, $\Delta\Lambda$ shrinks along the staircase. — Verdict: attack right (presentational); conclusion unchanged.**
**23. RG factor over 19 orders is $10^{0.578}=3.78$, not $0.26$. — Verdict: attack right (S4 reproduces 3.78); conclusion (1316 orders needed) unchanged.**
**24. `fpe-banach-contraction` explicitly does not transfer. — Verdict: attack right; the analogy should carry the non-transfer note. With C.3 the point is sharper anyway: symmetry of the kernel, not its provenance, is the load-bearing hypothesis.**

---

## Surviving form of the attempt

### (i) The mass-test mechanism — does not survive as a positive claim; survives as a precise negative with the adaptation named

**Result (Sketch; arithmetic Rigorous).** In the no-boundary reading with inputs $\Lambda$ and $G$, the branch structure of the Lorentzian tree generates **no scale other than $\Lambda^{1/2}$**. Every scale attached to any node of any branch is $\Lambda^{1/2}\,f$ with $f$ a dimensionless function of (a) the node's position on the branch, (b) the field content through $a_2$, and (c) the de Sitter depth $N_{\rm inf}=\tau_{\rm decay}/t_{\rm Hubble}$ of the root. What the tree contributes beyond FRW is dimensionless: discreteness of nodes (integer harmonic labels $n$ from the $S^3$ topology of the cap's slices, rungs $m_n=H(n/n_{\max})^2$) and reach ($2N_{\rm inf}$ e-folds on the framework's closed, $\Lambda$-free branch, bottoming at $H=0$). The instanton-weight route is excluded in the HH reading by sign ($e^{+|I_E|}$) and by magnitude ($|I_E|=O(a_2)$, SM $\approx5$). Hence **a second dimensionless input per species is needed** — a per-species address $n_s$ or $k_s$ — and the mass test is answered no.

**Named adaptations (ordered by cheapness):** (1) compute $N_{\rm inf}$ from the root's instability — it sets the number of rungs and the reach, and is a property of the framework's own fixed point, not an import; (2) the field content: $a_2$ sets $H$, and the harmonic spectrum of the cap sets the rung labels — the only structure at the junction beyond $\Lambda,G$ (the attempt's option (2), Bunch–Davies on the cap, is a version of this); (3) failing both, the per-species address is the Yukawa sector by another name, an explicit second input at the junction.

### (ii) The side results — C.1 correct but small; C.2 Rigorous by citation; new C.3 Rigorous

**C.1 (Rigorous, given the three-line reduction the attack supplied).** $D(G\circ G)|_T=S_eM_rS_bM_r\simeq XX^{\mathsf T}$, real spectrum $\ge0$ at every interior point, for real $\gamma$, symmetric $A$ (any $\alpha$), any $\beta$, any $N$. Consequence: a 2-cycle can be born only by a fold of $G\circ G$ or at a flip of the fixed point, and can never flip or Neimark–Sacker. Novelty: one line beyond `ce-second-iterate-real-spectrum`; the consequence is new but is now a corollary of C.3.

**C.2 (Rigorous).** Let $W={\rm Re}\big(\gamma(A+\beta I)\big)$ (real symmetric) and $c=2{\rm Re}(\gamma h)$. If $\lambda_{\max}(W|_{\mathbf 1^\perp})<1$ — in particular if ${\rm Re}\,\gamma<0$ and $A+\beta I\succeq0$ (e.g. $\alpha_j\ge0,\ \beta\ge0$; $A=\sum_j\alpha_jP_j$ is PSD for every $\mathrm{dims}$ since each $P_j=\sum_v\mathbf 1_{S_v}\mathbf 1_{S_v}^{\mathsf T}$; S2 checks 7 choices of dims) — then $F$ has **exactly one** fixed point in $\mathbb C^N$, for any $N$, any $\mathrm{dims}$, any real or complex $h$, any θ.
*Proof.* $E(q)=\Phi(q)-c^{\mathsf T}q-q^{\mathsf T}Wq$ on $\Delta$. Interior critical points of $E$ are exactly fixed points of $G$: $\nabla E=\ln q+\mathbf 1-c-2Wq\parallel\mathbf 1\iff q={\rm softmax}(c+2Wq)$. On the tangent space, ${\rm Hess}\,\Phi=\mathrm{diag}(1/q)\succeq2I$ (for $\sum v_\sigma=0$: $(\sum|v_\sigma|)^2\le\sum v_\sigma^2/q_\sigma$ by Cauchy–Schwarz and $(\sum|v_\sigma|)^2=4S^2\ge2\|v\|_2^2$ with $S=\sum_{v_\sigma>0}v_\sigma$; S5 samples: min eigenvalue 2.009–2.14), so ${\rm Hess}\,E|_T\succeq2(I-W|_T)\succ0$. $E$ is continuous on compact convex $\Delta$ and strictly convex, so it has a unique minimizer, interior (gradient of $\Phi$ blows up at the boundary), hence a critical point; a strictly convex function has no other critical point. Fixed points of $F$ correspond bijectively to fixed points of $G$ ($\psi\mapsto|\psi|^2$; conversely $\psi=F(\sqrt q)$ has $|\psi|^2=G(q)=q$ and phases ${\rm Im}(\gamma R(q))$). $\square$
*Prior art (verified content):* this is **Wang, arXiv:2605.15651, Theorem 3** verbatim in mechanism — potential $H(x)+\tfrac\beta2x^{\mathsf T}Wx+\beta b^{\mathsf T}x$, "entropy contributes curvature at least 2 along every tangent direction," strict concavity when $\kappa\le0$ or $\beta\kappa<2$, $\kappa=\lambda_{\max}(\Pi W\Pi|_T)$; under the dictionary $\beta_{\rm Wang}W_{\rm Wang}=2W$ the conditions coincide. `ce-riem-classical-unique` recommended checking exactly this on 2026-07-24; nobody did. So C.2 is Rigorous **by citation plus reproduced proof**, with **no novelty**; its value is that it closes the repo's open item (`ce-riem-classical-unique` Sketch → Rigorous under the stated condition, and Prop. `riem_classical`(b) in the paper). The attempt's Lefschetz route is a valid second proof once the attack's reduction is written out; it needs the same definiteness condition (index $+1$ requires ${\rm spec}(DG|_T)<1$, which holds since $\|S\|\le\tfrac12$ gives ${\rm spec}(S^{1/2}2W_rS^{1/2})\le\lambda_{\max}(W_r)<1$). Sharpness: the condition is sufficient, not necessary (S2: unique fixed point persists somewhat beyond it), and it genuinely fails for $\gamma>0$ (S2: up to 15 fixed points at $\gamma=0.5$, $\beta=10$) and for indefinite $A+\beta I$ with $\gamma<0$ (up to 11).

**C.3 (Rigorous; new to the repo; prior art Marcus–Westervelt 1989, Koiran 1994).** Stated and proved under flaw 9. Consequence for the record: `ce-feigenbaum-cascade` (dead, numerically) is dead by theorem; `ce-second-iterate-real-spectrum`'s "explains why the period caps at 2" is superseded by a global explanation that also excludes fold-born period 4 and all odd periods; the "routes_unexplored" entry "Nussbaum-type nonlinear Perron–Frobenius on $G\circ G$" is moot for the period question.

**Corrected bifurcation tree of $F$** (γ<0, $A+\beta I\succeq0$): one root (C.2); $N-1$ flips of the root (numerical: 0.648020, 1.848777, 2.218503 for the canonical instance), each spawning a 2-cycle; fold births of further 2-cycles whose number grows with $\beta$ (complete census 5/13/19/25 at $\beta=5/10/20/40$, of which 1/3/5/7 attracting); every 2-cycle has real nonnegative multipliers (C.1); no periodic orbit of period $\ge3$ (C.3). The "θ-inertness" statement holds for the paper's real parameters; for complex $h$ the magnitude fixed point depends on θ through $c$ but the class, and hence C.2/C.3, is unchanged.

### (iii) The tree/orientation argument — survives only as a re-expression, narrowed

1. **Orientation (Sketch, on the SCB fixed-background results):** on each Lorentzian branch, root-ward is the causal past direction with $\Sigma$ as initial boundary (timelike curves end on $\Sigma$, no timelike continuation). A partial order on events, foliation-free, surviving recollapse; a time orientation, not an evolution parameter. It derives nothing beyond the branch's causal structure. The minisuperspace version ("decreasing conformal factor") is foliation-dependent and fails past turnaround; withdrawn.
2. **Records (Sketch, by citation to Hawking 1985 and HLL 1993):** in the no-boundary state the thermodynamic/record arrow points away from the low-excitation end and does not reverse at maximum expansion. "Root" $=$ that end. The HH83 citation supports only "ground state" and is replaced.
3. **Root uniqueness (Conjecture, narrowed):** the framework's root must be the suppressed-fluctuation (HH-sign) saddle; among Lorentzian path-integral definitions only DTL-type Robin conditions deliver it (FLT 2017/2018 vs DTL 2019, polarities verified), at the cost of one parameter $\beta$ within a $\Lambda$-set window — no new scale. The SCB ↔ Robin analogy is withdrawn. The conjugate pair is a $\mathbb Z_2$ on WKB orientation under which the causal/$a$ order is invariant; no derivation of orientation follows from it. Acyclicity (no recoherence) remains an unproven hypothesis.

---

## What the rescue could not do

- **Compute $N_{\rm inf}$** for the anomaly-driven root from its own instability (Starobinsky 1980's decay; which anomaly coefficient controls it is stated from memory, unverified). This single dimensionless number sets the reach and rung count of the ladder and is the one piece of the depth accounting that is the framework's to compute.
- **Supply any selection rule** mapping a species to a harmonic label $n_s$ or depth $k_s$. None found in the repo's structures (curvature masses vanish on the radiation branch; the RG factor over 19 orders is 3.8). Without it the mass test is failed, full stop.
- **Rescue the instanton route** in any reading: the HH sign is an enhancement; a tunneling-sign reading would contradict the "minimum excitation" root; and $|I_E|=O(a_2)$ with SM $a_2\approx498$ gives $e^{-5.5}$.
- **Complete the 2-cycle census at $\beta=100$** (index sum $-5$): more repelling orbits exist than the face-seeded Newton finds. Not needed for any conclusion.
- **Verify Lehners' review eq. (173) and p. 101 directly** (PDF over the fetch limit; ar5iv rendering truncated). The sign is established independently (Vilenkin 1994 + the action computation); the conjugate-pair/decoherence passage rests on the attack's verification.
- **Prove that each of the $N-1$ fixed-point multipliers crosses $-1$ exactly once** in $\beta$ (numerically true; asymptotics $-2\beta/N$ suggest it; not proved).
- **Adjudicate the 16π question for #168.** The $8\pi\times2$ decomposition above is a hypothesis to test against Starobinsky's/Linde's definition of $k_2$, not a result.

---

## Citations used

**Verified (web, this pass):**
- Hawking, Laflamme, Lyons, "The origin of time asymmetry," Phys. Rev. D **47**, 5342 (1993), arXiv:gr-qc/9301017 — abstract quoted verbatim above (arrow constant through recollapse; "contrary to an earlier claim").
- Hawking, "Arrow of time in cosmology," Phys. Rev. D **32**, 2489 (1985) — APS abstract (smooth when small, irregular when large). Page, Phys. Rev. D **32**, 2496 (1985) — existence.
- Di Tucci & Lehners, "No-boundary proposal as a path integral with Robin boundary conditions," Phys. Rev. Lett. **122**, 201302 (2019), arXiv:1903.06757 — abstract and full text (ar5iv): condition at $t=0$, $\alpha=-6\pi^2i$, $\beta$ window $1/(3\pi^2H^2)<|\beta|<1/(\pi^2H^2)$.
- Vilenkin, "Approaches to quantum cosmology," Phys. Rev. D **50**, 2581 (1994), arXiv:gr-qc/9403010 — HH $\Psi\sim e^{-I_E}$ (eq. 1.3); tunneling nucleation probability $e^{-3/(8G^2\rho_v)}$ (eq. 3.17), favoring large $\rho_v$.
- Wang, "Sharp spectral thresholds for logit fixed points," arXiv:2605.15651 (2026) — Theorem 3 content (symmetric $W$, entropy-regularized potential, curvature $\ge2$, unique fixed point under $\kappa\le0$ or $\beta\kappa<2$); Theorem 2 is a contraction threshold, distinct from uniqueness.
- Marcus & Westervelt, "Dynamics of iterated-map neural networks," Phys. Rev. A **40**, 501 (1989) — existence (Semantic Scholar); content (symmetric connections → only fixed points and period-2 attractors, Lyapunov function) from the APS abstract as returned in search-result text, not fetched directly.
- Koiran, "Dynamics of discrete time, continuous state Hopfield networks," Neural Computation **6**, 459 (1994) — existence (Semantic Scholar); content (parallel iteration, symmetric weights → cycle of length 1 or 2) from search-result abstract text, not fetched directly.
- GitHub #168 (open, `agent-ready`, supersedes #133) — `gh issue view`.

**Verified by the attack pass and relied on as evidence, not re-fetched:** Lehners, Phys. Rep. **1022**, 1 (2023), eq. (173) and p. 101; Feldbrugge–Lehners–Turok PRL **119**, 171301 (2017) and PRD **97**, 023509 (2018); Hofmann & Müller CQG **35**, 035015 (2018); Duff CQG **11**, 1387 (1994) eq. (31); Hawking–Hertog–Reall PRD **63**, 083504 (2001).

**Unverified, flagged:** that the anomaly-driven de Sitter decay time is controlled by the $\Box R$ coefficient (memory); mode-by-mode decoherence at horizon exit as the branch points of the decoherent-histories tree (standard, no citation checked); Gell-Mann–Hartle medium decoherence (not load-bearing); Garbe–Wei arXiv:2605.02314 (record-reported, not needed here).

**Repo sources:** `programs/co-emergence/index.tex` Axioms (159–252), Prop. `riem_classical` and proof (1001–1060), §Finite toy model (688–803), §Weakening the mass assumption (1219–1348); `programs/co-emergence/tests/toy_model.py`; claims `ce-riem-classical-unique`, `ce-second-iterate-real-spectrum`, `ce-self-consistency-real-spectrum`, `ce-toy-fixed-point-multiplicity`, `ce-feigenbaum-cascade`, `ce-theta-conjugation`; `programs/fixed-point-existence/index.tex` §Cosmological fixed point (110–165) and claims `fpe-starobinsky-coefficient`, `fpe-fixed-point-is-inflationary`; `programs/signature-change-boundary/notes/2026-06-17-expanding-region-note.md` §§2–3.

---

## Appendix — scripts and output (numpy/scipy; nothing written except this file)

### S1 — Lyapunov function and period census, real and complex parameters (C.3)

```python
import numpy as np, sys
sys.path.insert(0,'/home/will/Projects/physagent/programs/co-emergence/tests')
from toy_model import CoEmergenceModel
def build_A(dims, alphas):
    N=int(np.prod(dims)); idx=np.array(np.unravel_index(np.arange(N),dims)).T; A=np.zeros((N,N),dtype=complex)
    for j,a in enumerate(alphas): A+=a*(idx[:,j][:,None]==idx[:,j][None,:])
    return A
def Phi(q): q=np.clip(q,1e-300,None); return float(np.sum(q*np.log(q)))
def L(p,q,c,Weff): return Phi(p)+Phi(q) - 2*p@Weff@q - c@(p+q)
def run(dims, h, alphas, beta, gamma, nsteps=4000, seed=0):
    N=int(np.prod(dims)); A=build_A(dims,alphas)
    Weff=np.real(gamma*(A+beta*np.eye(N))); c=2*np.real(gamma*np.asarray(h,dtype=complex))
    assert np.allclose(Weff,Weff.T)
    mdl=CoEmergenceModel(dims,h,list(alphas),beta,gamma); rng=np.random.default_rng(seed)
    psi=rng.normal(size=N)+1j*rng.normal(size=N); psi/=np.linalg.norm(psi); qs=[np.abs(psi)**2]; maxinc=-np.inf; Lprev=None
    for t in range(nsteps):
        psi=mdl.F_map(psi); q=np.abs(psi)**2; qs.append(q)
        z=c+2*Weff@qs[-2]; z=z-z.max(); sm=np.exp(z)/np.exp(z).sum(); assert np.abs(sm-q).max()<1e-12   # q_{t+1} = softmax(c + 2 W q_t)
        if t>=1:
            Lcur=L(qs[-1],qs[-2],c,Weff)
            if Lprev is not None: maxinc=max(maxinc,Lcur-Lprev)
            Lprev=Lcur
    tail=qs[-200:]; per=-1
    for p in range(1,65):
        if np.linalg.norm(tail[-1]-tail[-1-p])<1e-9: per=p; break
    return maxinc, per
rng=np.random.default_rng(1); worst=-np.inf; periods=set(); n=0
for dims in [(2,2),(2,2,2),(3,3),(2,2,2,2),(2,3,2)]:
    N=int(np.prod(dims))
    for trial in range(6):
        h=rng.uniform(0.5,1.5,size=N); alphas=rng.uniform(-0.8,0.8,size=len(dims)); beta=rng.choice([0.4,2.0,5.0,40.0,-3.0]); gam=rng.choice([-1.0,-2.0,0.7])
        mi,per=run(dims,h,alphas,beta,gam,seed=trial); worst=max(worst,mi); periods.add(per); n+=1
        h=rng.uniform(0.5,1.5,size=N)+1j*rng.uniform(-0.5,0.5,size=N); alphas=rng.uniform(0.2,0.8,size=len(dims))+1j*rng.uniform(-0.3,0.3,size=len(dims))
        beta=rng.choice([5.0,40.0])+1j*rng.uniform(-2,2); gam=-1+1j*rng.choice([0.0,1.0,3.0])
        mi,per=run(dims,h,alphas,beta,gam,seed=trial+100); worst=max(worst,mi); periods.add(per); n+=1
print("instances",n,"max increase of L along any orbit step:",worst,"periods observed:",sorted(periods))
```
Output: `instances 60 max increase of L along any orbit step: 7.1e-15 periods observed: [1, 2]` (negative $\alpha_j$, negative $\beta$, $\gamma>0$, and complex $h,\alpha,\beta,\gamma$ included).

### S2 — convexity route to uniqueness; scope boundaries (C.2)

```python
# build_A, softmax as above (real); tangent Hessian of E at q: diag(1/q) - 2 Weff restricted to 1^perp; Newton census of fixed points from 60-200 starts
for dims in [(2,2),(2,3),(3,3),(2,2,2),(4,5),(2,2,2,2),(3,4,2)]: print(dims, np.linalg.eigvalsh(build_A(dims, rng.uniform(0,1,len(dims)))).min())
for dims in [(2,2),(2,2,2),(3,3),(2,2,2,2)]:
    for beta in (0.4,5.0,40.0,1000.0):
        for gam in (-1.0,-5.0): ...  # count distinct fixed points of softmax(2 gam h + 2 gam (A+beta I) q)
# gamma>0 with A+beta I PSD; and gamma<0 with alphas=(-0.6,-0.4), beta in (-2,...,0.5)
```
Output: $\min{\rm eig}\,A\in[-10^{-12},0]$ for all seven dims (PSD, with the expected zero eigenvalue); **exactly 1 fixed point** in all 32 ($\mathrm{dims},\beta,\gamma<0$) cases with $\beta\in\{0.4,5,40,1000\}$; $\gamma>0$: 1, 3, 15 fixed points at $(\gamma,\beta)=(0.5,1),(0.5,3),(0.5,10)$, up to 13 at $\gamma\in\{2,4\}$; indefinite $A+\beta I$ with $\gamma<0$: 1 fixed point at $\beta\in\{0.5,0,-0.4,-0.6\}$, $\gamma=-1$; 3, 9, 11 at $\beta=-1,-1,-2$ — multiplicity appears only where the convexity condition fails. Tangent Hessian of $\Phi$ with $q_\sigma\ge10^{-6}$ (S5): min eigenvalue 2.009 / 2.091 / 2.089 / 2.141 for the four dims (bound 2); of $E$: $\ge3.36$. (A first run without the floor on $q$ produced spurious negative values from $1/q$ overflow at $q\sim10^{-300}$; the Hessian is a sum of PSD terms by construction.)

### S3 / S6 — C.1 re-verification, flips, complete 2-cycle census with Lefschetz index sum, period 3/4 census

```python
# canonical instance h=(1.0,0.7,0.5,1.2), dims=(2,2), alphas=(0.5,0.3), gamma=-1; U = basis of 1^perp
# C.1: compare chain-rule D(GoG)|_T with S_e Mr S_b Mr at 900 random interior points, beta in [0.1,1e3]
# flips: track sorted eigenvalues of DG|_T at the fixed point on a beta grid; brentq on each crossing of -1
# census: Newton on GoG - id in log coordinates q = softmax(y), seeds uniform on every face of the simplex (60 per face) + 3000 random; group into orbits;
#         index of a point = sign det(I - D(GoG)|_T); Lefschetz sum = index(fixed point) + sum over orbits of 2*(-1)^{#multipliers>1}
# period 3/4: Newton on G^3 - id, G^4 - id from 400 starts at beta in {2,5,20,40,100,400}, keep minimal-period-3/4 roots
```
Output: C.1 relative error $1.1\times10^{-13}$, min Re eig $-2.7\times10^{-12}$, max $|{\rm Im}|$ $1.8\times10^{-14}$. Flips (eigen-index, β): (0, 0.648020), (1, 1.848777), (2, 2.218503); fixed-point spectrum at β=40: $\{-20.918,-20.060,-19.809\}$. Census table as in flaw 8 (index sum 1 at β=5,10,20,40; −5 at β=100, incomplete). Period-3 / period-4 points: 0 / 0 at every β.

### S4 — depth accounting, recollapse, anomaly numbers, actions, rates

```python
MP=1.2209e28; hbar=6.582e-16   # eV, eV s
for a2 in (1e3,1e4,1e5):
    Hc=MP/np.sqrt(a2); Hr=np.sqrt(180*np.pi/a2)*MP
    for lab,H in (("can",Hc),("repo",Hr)): print(a2,lab,H/hbar*1e-42,H/hbar*1e-40)      # N_inf window
for k,m in (("top",1.73e11),("proton",9.38e8),("electron",5.11e5),("nu",0.05)): print(k,0.5*np.log((MP/100)/m),0.5*np.log(np.sqrt(180*np.pi/1e4)*MP/m))
# closed radiation branch: H^2(k)/H_dS^2 = e^{-2k}(e^{-2k+4N}-1), zero at k=2N
S=lambda NS,NF,NV:(NS+11*NF+62*NV)/2
for lab,(NS,NF,NV) in {"SM":(4,22.5,12),"SM+3nuR":(4,24,12)}.items(): a2=S(NS,NF,NV); print(lab,a2,np.sqrt(180*np.pi/a2),a2/90,a2/180,np.exp(-a2/90))
vol=8*np.pi**2/3; print(-(1/(16*np.pi))*(12-6)*vol, -(1/(16*np.pi))*12*vol, -vol/(120*np.pi**2))   # S^4 actions in MP^2/H^2 units; integrated anomaly /a2
H0=67.4/3.0857e19; yr=3.156e7; print(-(1-0.55)*H0*yr, -2*H0*yr, 10**(19*4.8/(16*np.pi**2)))
```
Output: $H_{\rm repo}/H_{\rm can}=23.78$; $N_{\rm inf}$ at $a_2=10^4$: canonical $[0.19,18.5]$, printed $[4.4,441]$; radiation depths (canonical / printed): top 17.1 / 18.7, proton 19.7 / 21.3, electron 23.5 / 25.0, ν 31.5 / 33.1; closed-branch $H/H_{\rm dS}$ at $k=2N_{\rm inf}$: 0; SM $a_2=497.75$, $H/M_P=1.066$, $a_2/90=5.53$, $e^{-a_2/90}=4.0\times10^{-3}$; $I_E(S^4,\Lambda)=-\pi M_P^2/H^2$, $I_{\rm EH}(S^4,\text{no }\Lambda)=-2\pi M_P^2/H^2$, $\int\langle T\rangle\sqrt g=-a_2/45$; $\dot m/m=-3.10\times10^{-11}$ vs $-1.38\times10^{-10}\ {\rm yr^{-1}}$; RG factor 3.78.
