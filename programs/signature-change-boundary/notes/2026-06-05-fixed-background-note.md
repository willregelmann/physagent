# Emergent Lorentzian Signature from a Degenerate Boundary
**A fixed-background consistency note**

---

### Status and scope

This note records a single, limited result. On a *fixed* background whose metric changes signature across a degenerate hypersurface $\Sigma$, three descriptions are mutually consistent and non-singular: the bulk geometry, the geodesic structure, and a free scalar field. The surface $\Sigma$ is traversed with a definite, *asymmetric* character that depends on the causal type of what is crossing.

This is a consistency statement at the **test-field level on a prescribed background**. It is not a dynamical theory, it makes no empirical prediction, and it does not establish that the picture survives once the field is allowed to source the geometry. The explicit limits are collected in §9 and should be read as part of the result, not as boilerplate. The intended use is as a precise, checkable starting point: a set of structural features other approaches to signature change can be compared against.

Throughout, "consistent" means *free of the divergences one would naively expect at a degenerate metric*, and *mutually compatible across the geometric, kinematic, and field-theoretic descriptions*. It does **not** mean "physically realized" or "dynamically selected."

---

## 1. Setup

Work on a four-manifold $\mathcal{M}$ with coordinates $x^\mu = (x^0, x^1, x^2, x^3)$. Fix a prescribed metric

$$ds^2 = \lambda(x^0)\,(dx^0)^2 + (dx^1)^2 + (dx^2)^2 + (dx^3)^2,$$

with $\lambda$ a real function that passes through zero, smooth away from its zero. The three regions are:

- $\lambda < 0$: **Lorentzian** — $x^0$ is timelike, signature $(-,+,+,+)$.
- $\lambda > 0$: **Euclidean** — all four directions spacelike, signature $(+,+,+,+)$.
- $\lambda = 0$: the **degenerate surface** $\Sigma$, where $\det g = \lambda \to 0$ and $g^{-1}$ is undefined.

Near $\Sigma$ take

$$\lambda(x^0) \simeq -c\,\mathrm{sgn}(x^0)\,|x^0|^n, \qquad c>0,\; n>0,$$

so that $\lambda<0$ (Lorentzian) for $x^0>0$, $\lambda>0$ (Euclidean) for $x^0<0$, and $\Sigma$ is at $x^0=0$ — a genuine two-sided signature change for every $n>0$. (An earlier draft wrote $\lambda \simeq -c\,(x^0)^n$, which changes sign only for odd $n$; for even $n$ that form is negative on both sides of $\Sigma$, a degenerate tangency between two Lorentzian regions rather than a signature change. The $\mathrm{sgn}$ form fixes this parity defect; for $n=1$ the two forms coincide. For non-odd $n$ the $\mathrm{sgn}$ profile is only finitely differentiable at $\Sigma$ itself; every derivation below uses only the one-sided asymptotics on the open regions — with one flagged exception, the junction *matching* at the end of §5, which is inherently a two-sided statement — so nothing is lost.) The exponent $n$ controls the rate at which the signature degenerates ($n=1$ linear, $n=2$ quadratic); the results below hold for all $n>0$ and are established from both sides of $\Sigma$.

Two interpretive points fix the framing.

*Signature is configurational, not temporal.* The change across $\Sigma$ is a fact about the spatial pattern of the metric, not a process occurring in time. There is no "before $\Sigma$" and "after $\Sigma$" — only "here" (Lorentzian) and "there" (Euclidean). This is what keeps the construction from being circular: nothing has to *happen in time* for the timelike direction to *be present* in a region.

*$\lambda$ is prescribed.* We do not derive $\lambda$, nor ask what configuration could source it. That is the backreaction problem, and it is out of scope (§9).

## 2. The apparent obstacle

At $\Sigma$, $\det g \to 0$, so $g^{-1}$ diverges. Every object built from the inverse metric — the connection, the d'Alembertian, every propagator, every kinetic term — is formally singular there. If nothing built from $g^{-1}$ remains finite across $\Sigma$, the construction is incoherent and there is nothing to formalize.

The content of this note is that, on the fixed background, this divergence is systematically controlled. The reason (§8) is a single structural fact: every factor of $g^{00} = 1/\lambda$ that appears in a covariant object is escorted by a volume factor $\sqrt{|g|} = \sqrt{|\lambda|}$ from the measure, and the pairing softens the divergence to something integrable or regular-singular rather than catastrophic.

## 3. The geometry is flat on each side **(Rigorous, given fixed background)**

On the Lorentzian side ($\lambda<0$) define $u = \int_0^{x^0}\sqrt{-\lambda(s)}\,ds$. Then $du^2 = -\lambda\,(dx^0)^2$, and the line element becomes

$$ds^2 = -\,du^2 + (dx^1)^2 + (dx^2)^2 + (dx^3)^2,$$

i.e. flat Minkowski space. The same substitution with $\sqrt{\lambda}$ on the Euclidean side gives flat $\mathbb{R}^4$. Direct computation agrees: the only nonzero Christoffel symbol is $\Gamma^0_{00} = \lambda'/2\lambda$, and the Riemann tensor it produces vanishes identically.

**The Euclidean side, explicitly.** For $x^0<0$, $\lambda = c\,|x^0|^n > 0$. Define $v = \int_{x^0}^{0}\sqrt{\lambda(s)}\,ds$, the Euclidean distance from $\Sigma$. Then $dv^2 = \lambda\,(dx^0)^2$ and

$$ds^2 = dv^2 + (dx^1)^2 + (dx^2)^2 + (dx^3)^2,$$

flat $\mathbb{R}^4$; the map $v(x^0)$ is a diffeomorphism on the open Euclidean region and degenerates only at $\Sigma$. The Christoffel computation is uniform across the two sides: with $\lambda = -c\,\mathrm{sgn}(x^0)\,|x^0|^n$ one has $\lambda' = -c\,n\,|x^0|^{n-1}$ for all $x^0\neq 0$, so

$$\Gamma^0_{00} \;=\; \frac{\lambda'}{2\lambda} \;=\; \frac{n}{2x^0}$$

on *both* sides — the same simple pole at $\Sigma$, approached from either direction (in the distance-from-$\Sigma$ variable $x=|x^0|$ this reads $+n/2x$ on the Lorentzian side and $-n/2x$ on the Euclidean side) — and it remains the only nonzero symbol. A Riemann tensor built from a single $\Gamma^0_{00}(x^0)$ vanishes identically: every component with a spatial index contains a vanishing Christoffel, and $R^0{}_{000} = 0$ by antisymmetry. So the Euclidean bulk is flat by direct computation as well, its geodesics are straight lines in $(v,\vec x)$, and all curvature invariants are zero on both sides.

**Consequence.** On the fixed background, the bulk on each side of $\Sigma$ is flat; all curvature invariants are zero, and their limits along every curve reaching $\Sigma$ vanish. The surface $\Sigma$ is therefore *not* a curvature singularity in the standard limits-of-invariants sense. It is a degenerate boundary — the edge of a flat region. Two precisions (added in the July 2026 red-team audit, replacing an earlier "the $x^0$ coordinate, but not the geometry, breaks down"): the degeneracy at $\Sigma$ is *invariant*, not a chart artifact — no coordinate change makes $g$ non-degenerate across a signature change — and curvature *at* $\Sigma$ itself is not definable in the standard distributional frameworks (the connection $\Gamma^0_{00} \sim n/2x^0$ is not locally integrable across $\Sigma$, placing the geometry outside the Geroch–Traschen class), though no regularization of this ansatz can concentrate curvature there, since the formal Riemann expression vanishes identically for every $\lambda(x^0)$ by index structure alone. The map $u(x^0)$ is a diffeomorphism on the open Lorentzian region and degenerates only at $\Sigma$ itself.

This already settles, *for this background*, a question that geodesics alone cannot: a geodesic ending at $\Sigma$ at finite parameter is here ending at a boundary of a flat region, not running into diverging curvature.

## 4. Geodesics and the crossing asymmetry **(Rigorous, given fixed background — except continuation *as a geodesic* through $\Sigma$, which is Sketch; see below)**

Parametrize a curve by $x^0$ and write $\vec u = d\vec x/dx^0$ for its coordinate spatial velocity.

**Timelike geodesics reach $\Sigma$ at finite proper time.** Proper time along a timelike curve is

$$\tau = \int \sqrt{-\lambda - |\vec u|^2}\; dx^0, \qquad |\vec u|^2 < -\lambda,$$

the inequality being the requirement to stay inside the light cone. The integrand is bounded above by $\sqrt{-\lambda}$, which tends to $0$ at $\Sigma$. A bounded integrand vanishing at the endpoint, over a finite coordinate interval, gives a finite integral. For the rest curve with $\lambda=-c\,(x^0)^n$,

$$\tau = \sqrt{c}\int_0^{a}(x^0)^{n/2}\,dx^0 = \sqrt{c}\,\frac{2}{\,n+2\,}\,a^{(n+2)/2} < \infty$$

for every $n>0$. The only way to make $\tau$ diverge is $\lambda \to -\infty$ sufficiently fast at $\Sigma$ (e.g. $\lambda \sim -c/(x^0)^2$) — a divergence of the prescribed profile, not anything forced by signature change. (An earlier revision glossed this as "curvature blow-up"; that is false in this metric class, where the geometry is flat for *every* $\lambda(x^0)$ — the $\lambda \sim -c/(x^0)^2$ profile has $\tau = \infty$ with identically vanishing Riemann tensor. Divergent proper time and curvature blow-up are independent.) So a massive worldline *reaches* the boundary; it is not held back by an infinite barrier.

**Timelike geodesics have no timelike continuation.** The normalization $g_{\mu\nu}\dot x^\mu \dot x^\nu = -1$ reads $\lambda(\dot x^0)^2 + |\vec v|^2 = -1$, which requires $\lambda<0$. For $\lambda>0$ the left side is non-negative and the equation has no solution: there is no timelike geodesic in the Euclidean region, because there is no timelike direction there at all.

The honest, neutral statement is therefore: **a timelike geodesic is incomplete at $\Sigma$ at finite proper time.** It reaches $\Sigma$ and cannot be continued as a timelike curve. Two readings — a graceful handoff to the Euclidean region, or a genuine edge — are *not* distinguishable from the geodesic alone. They are distinguished here only by §3: the curvature is bounded (zero), so the incompleteness is that of a flat-region boundary, the mild kind, not a curvature singularity. Whether it stays mild under backreaction is open (§9). The informal phrase "de-particling" is the *benign* gloss; the load-bearing fact is the incompleteness.

**Spacelike curves cross with their character intact.** A spacelike curve has length element $\sqrt{\lambda + |\vec u|^2}\,dx^0$ with $|\vec u|^2 > -\lambda$; near $\Sigma$ the integrand tends to $|\vec u|>0$, so it too reaches $\Sigma$ at finite parameter. But for $\lambda>0$ *every* direction is spacelike, so the curve continues with no change of causal character. Spacelike is the type shared with the Euclidean directions.

**Continuation *as a geodesic* through $\Sigma$ (Sketch).** The crossing statement above is about spacelike *curves*, and its $|\vec u|>0$-at-$\Sigma$ hypothesis fails for every geodesic. The only nonzero Christoffel gives the affine first integral $\dot x^0 = C/\sqrt{|\lambda|}$ (spatial components $\dot x^i = v^i$ constant), so along every $\Sigma$-crossing spacelike geodesic the coordinate spatial velocity obeys $\vec u = \vec v\,\sqrt{|\lambda|}/C \to 0$ at $\Sigma$: every crossing geodesic arrives coordinate-tangent to the exceptional $x^0$-direction. What is Rigorous for geodesics: finite arc length to $\Sigma$ (the integrand is $O(|x^0|^{n/2})$, integrable), constant spacelike character on each open side, and the existence of spacelike-*curve* continuations. What is **not** established here: that the continuation can be made *as a geodesic*, uniquely — the geodesic equation is singular at $\Sigma$ ($\Gamma^0_{00} = n/2x^0$ is not integrable across it), and endpoint-plus-coordinate-direction data at $\Sigma$ do not select the outgoing spatial velocity. Geodesic extendability across a transverse type-change surface is exactly the subject of Kossowski–Kriele [7]; whether their extension results cover this profile, step for step, has not been checked here and is left as an explicit gap. An earlier revision headlined this paragraph "spacelike geodesics cross with their character intact" at Rigorous; that label covered more than the argument shows and was reset in the July 2026 red-team audit.

**From the Euclidean side.** For $x^0<0$ the metric is positive-definite, so every curve is spacelike — there is no timelike sector to discuss. A curve approaching $\Sigma$ from $x^0<0$ has length element $\sqrt{\lambda + |\vec u|^2}\;dx^0$ with $\lambda>0$: the radicand is positive for *every* $\vec u$ (no cone condition exists), and near $\Sigma$ the integrand tends to $|\vec u|$ — or to $0$ via $\sqrt{\lambda}\sim\sqrt{c}\,|x^0|^{n/2}$ if $\vec u \to 0$ — so over a finite coordinate interval the arc length is finite. Euclidean curves also reach $\Sigma$ at finite parameter; nothing on either side is held away from the surface. Crossing into $x^0>0$ with $|\vec u|>0$ at $\Sigma$, the curve satisfies the Lorentzian spacelike condition $|\vec u|^2 > -\lambda$ automatically near $\Sigma$ (the right-hand side tends to $0$), and continues as a spacelike curve: character intact, in either direction of traversal. The one exceptional direction is the $x^0$-axis itself, which is spacelike on the Euclidean side and timelike on the Lorentzian side: as a point set it passes through $\Sigma$, but its causal character flips there. Read from the Lorentzian side this is the rest worldline above (timelike, no timelike continuation); read from the Euclidean side it is the unique spacelike direction that fails to cross *as itself*. The two readings are the same asymmetry.

**The asymmetry.** Both types reach $\Sigma$; they differ in whether they *continue as themselves*. Timelike curves cannot (no timelike continuation exists). Spacelike curves can. This asymmetry is forced by positive-definiteness of the Euclidean region alone; it requires nothing about the field equations.

## 5. A free scalar field across $\Sigma$ **(Rigorous, given fixed background)**

Put a free scalar $\phi$ of mass $m$ on the background. The Laplace–Beltrami operator carries the measure factor $\sqrt{|g|}=\sqrt{|\lambda|}$:

$$\Box\phi = \frac{1}{\sqrt{|\lambda|}}\,\partial_0\!\Big(\frac{\sqrt{|\lambda|}}{\lambda}\,\partial_0\phi\Big) + \nabla^2\phi .$$

For a mode $\phi \propto e^{i\vec k\cdot\vec x}$ near $\Sigma$, with $\lambda=-c\,(x^0)^n$, the temporal equation reduces (after clearing the leading factor) to

$$\phi'' - \frac{n}{2x}\,\phi' + c\,(m^2+k^2)\,x^{n}\,\phi = 0, \qquad x\equiv x^0.$$

This has a **regular singular (Fuchsian-type) point** at $x=0$: a simple pole in the $\phi'$ coefficient, a vanishing coefficient on $\phi$. (For integer $n$ the $\phi$-coefficient $x^n$ is analytic and classical Frobenius theory applies verbatim; for non-integer $n$ it is not analytic at $0$ (only finitely differentiable) and the classical theory does not literally apply — there the load-bearing proof is the *explicit global solutions exhibited below*, verified by direct substitution for symbolic $n>0$, and the indicial exponents are read off from them.) The indicial equation $s(s-1) - \tfrac{n}{2}s = 0$ gives roots

$$s = 0 \qquad\text{and}\qquad s = 1 + \tfrac{n}{2}.$$

Both are $\ge 0$ for $n>0$, so both local solutions are **bounded** at $\Sigma$, with $\phi'\to 0$. The field does not blow up; the divergence of $g^{00}$ is demoted to a regular singular point by the measure factor. (The exceptional mode $m^2+k^2=0$, i.e. $\beta=0$, is not covered by the Bessel basis below — there $\sin(\beta x^\gamma)$ degenerates — but solving $\phi'' - \tfrac{n}{2x}\phi' = 0$ directly gives the basis $\{1,\; x^{1+n/2}\}$: still bounded, still log-free, momentum still finite. All conclusions of this section hold for it.)

The equation is in fact **Bessel-reducible**. With $\alpha = \tfrac{n+2}{4}$, $\gamma = \tfrac{n+2}{2}$, $\beta = \tfrac{2\sqrt{c(m^2+k^2)}}{n+2}$, the solution is $\phi = x^{\alpha} Z_\nu(\beta x^\gamma)$ with $\nu^2 = \alpha^2/\gamma^2 = \tfrac14$, i.e. $\nu = \tfrac12$ exactly. Half-integer Bessel functions are elementary: trigonometric on the Lorentzian side; the decaying branch on the Euclidean side.

**No logarithmic solutions, for every $n>0$.** The two branches are log-free for *all* $n>0$, including the cases where the indicial gap of the pre-reduction equation is an integer. Logarithms enter the second solution of the Bessel equation only when the order $\nu$ is an integer — the case in which $J_\nu$ and $J_{-\nu}$ become linearly dependent and the independent second solution must be $Y_\nu$, which carries a $\log$. Here $\nu=\tfrac12$ is *not* an integer, so $J_{1/2}(z)\propto z^{-1/2}\sin z$ and $J_{-1/2}(z)\propto z^{-1/2}\cos z$ are linearly independent elementary functions and neither contains a logarithm. This matters for the even-$n$ profiles ($n=2,4,6,\dots$): there the indicial roots of the original ODE, $s=0$ and $s=1+\tfrac n2$, differ by the integer $1+\tfrac n2$, and a naive reading of the Fuchsian (Frobenius) theory might worry that an integer indicial gap *forces* a $\log$ in the smaller-root solution. The Bessel reduction shows it does not. The criterion that controls the appearance of a logarithm is the integrality of the Bessel order $\nu$, not the integrality of the indicial gap of the pre-reduction equation; and $\nu=\alpha/\gamma=\tfrac12$ is fixed independently of $n$. Concretely, the two elementary branches realize the two indicial roots with no log term for any $n$: $x^{\alpha}J_{-1/2}(\beta x^\gamma)\sim x^{\alpha-\nu\gamma}=x^{0}$ recovers the $s=0$ root and $x^{\alpha}J_{1/2}(\beta x^\gamma)\sim x^{\alpha+\nu\gamma}=x^{1+n/2}$ recovers the $s=1+\tfrac n2$ root (using $\nu\gamma=\alpha$). The potential integer-gap obstruction is thus absorbed by the change of variables, which supplies two linearly independent log-free branches for every $n>0$. (For odd $n$ — e.g. $n=1$, gap $\tfrac32$ — the gap is already non-integer and no concern arises; the Bessel argument covers both parities uniformly.)

This last fact is the field-theoretic form of the geodesic asymmetry. **The operator changes type across $\Sigma$**: hyperbolic for $\lambda<0$, elliptic for $\lambda>0$. A mode that is *oscillatory* (a propagating wave) on the Lorentzian side continues to an *evanescent* (exponentially decaying) profile on the Euclidean side, while the spatial dependence, being spacelike on both sides, stays oscillatory throughout.

**The Euclidean side, explicitly.** The reduction above used the Lorentzian-side form $\lambda = -c\,x^n$ with $x \equiv x^0 > 0$. For $x^0<0$ set $x \equiv -x^0 > 0$ (the coordinate distance from $\Sigma$), so $\lambda = c\,x^n > 0$. Carrying the same mode through the temporal operator — the two sign flips from $\partial_0 = -d/dx$ cancel in the second-order term, while $g^{00} = 1/\lambda$ has changed sign — gives

$$\phi'' - \frac{n}{2x}\,\phi' - c\,(m^2+k^2)\,x^{n}\,\phi = 0.$$

Written in the distance-from-$\Sigma$ variable, the friction term is identical to the Lorentzian side; the only change is the sign of the non-derivative term, which is the operator's type change (hyperbolic $\to$ elliptic) made explicit. The singular point at $x=0$ is still **Fuchsian** — the sign flip sits on the analytic, vanishing coefficient and does not enter the indicial equation — so the indicial roots are again $s=0$ and $s=1+\tfrac n2$, both $\ge 0$: all modes are bounded at $\Sigma$ from the Euclidean side too. The Bessel reduction goes through with the *same* $\alpha=\tfrac{n+2}{4}$, $\gamma=\tfrac{n+2}{2}$, $\beta=\tfrac{2\sqrt{c(m^2+k^2)}}{n+2}$, with ordinary Bessel functions replaced by modified ones, and again $\nu = \tfrac12$ exactly. Since $\alpha = \gamma/2$, the global solutions are elementary:

$$\phi \propto \sinh(\beta x^\gamma) \quad (s=1+\tfrac n2), \qquad \phi \propto e^{-\beta x^{\gamma}} \quad (s=0),$$

the $I_{1/2}$ and $K_{1/2}$ branches; the same rewriting on the Lorentzian side gives $\sin(\beta x^\gamma)$ and $\cos(\beta x^\gamma)$ — oscillation and evanescence *at the same rate constants* $\beta,\gamma$. Quantitatively, the Euclidean distance from $\Sigma$ is $\sigma_E(x) = \int_0^x\sqrt{\lambda}\,ds = \tfrac{2\sqrt c}{n+2}\,x^{(n+2)/2}$, so the decay exponent is $\beta x^\gamma = \sqrt{m^2+k^2}\;\sigma_E$ — for the $k=0$ mode, exactly $m\,\sigma_E$, the worldline/propagator-tail exponent of §7. Equivalently: in the flat coordinates of §3, $\beta x^\gamma = \sqrt{m^2+k^2}\,u$ on the Lorentzian side and $\sqrt{m^2+k^2}\,v$ on the Euclidean side, and the solution spaces on the two sides are exactly the flat-space mode spaces — spanned by $\cos/\sin(\sqrt{m^2+k^2}\,u)$ and by $e^{\mp\sqrt{m^2+k^2}\,v}$ respectively — pulled back through the degenerate coordinate change — §3's flatness and §5's Fuchsian structure are the same fact, as §8 asserts.

Finally, the canonical momentum $\pi = \sqrt{|g|}\,g^{00}\,\partial_0\phi \sim x^{-n/2}\cdot x^{n/2}$ is **finite and approaches a constant** at $\Sigma$. What this delivers, stated precisely: every solution on each open side has *finite* boundary data $(\phi, \pi)$ at $\Sigma$, so the Dray–Manogue–Tucker no-surface-layer matching condition $[\phi] = [\pi] = 0$ can be *imposed without fine-tuning* — and imposing it is well-posed: given the two Lorentzian constants, the two conditions determine the two Euclidean constants uniquely (an invertible $2\times 2$ system). It is a genuine two-sided junction condition selecting a half-dimensional subspace of the two-sided solution space, **not** something the one-sided regularity supplies by itself; an earlier revision said the condition was "reproduced automatically," which overstated this (and is the one place the analysis is inherently two-sided rather than one-sided-asymptotic, qualifying §1's one-sided-only remark). Note also that *which* junction condition is correct is disputed in the literature: the generic solution here has $\pi|_\Sigma \neq 0$, satisfying Dray–Manogue–Tucker [4] but violating Hayward's stronger instantaneous-stationarity condition $\pi|_\Sigma = 0$ [3] (see Relation to existing work).

The momentum is finite from the Euclidean side as well: with $\partial_0 = -d/dx$, $\pi \sim x^{-n/2}\,\phi'(x)$ up to sign, and both Euclidean branches have $\phi' = O(x^{n/2})$ — $\phi' = \beta\gamma\,x^{n/2}\cosh(\beta x^\gamma)$ and $-\beta\gamma\,x^{n/2}\,e^{-\beta x^\gamma}$ respectively, using $\gamma - 1 = \tfrac n2$ — so $\pi$ approaches a finite constant at $\Sigma$ from either side. The finite-boundary-data statement is two-sided, which is what makes the junction condition imposable from both sides.

## 6. Stress–energy is bounded **(Rigorous, given fixed background)**

For the scalar, $T_{\mu\nu} = \partial_\mu\phi\,\partial_\nu\phi - g_{\mu\nu}\mathcal{L}$ with $\mathcal{L} = \tfrac12 X + V$ and $X \equiv g^{\alpha\beta}\partial_\alpha\phi\,\partial_\beta\phi$. The regular solutions give $\phi'\sim x^{n/2}$, hence

$$X = g^{00}(\phi')^2 + |\nabla\phi|^2 \sim x^{-n}\cdot x^{n} + O(1) = O(1).$$

The curvature-sourcing invariant is a function of $X$ and $V$ alone:

$$T_{\mu\nu}T^{\mu\nu} = X^2 + 2VX + 4V^2 = O(1).$$

The same holds from the Euclidean side. The regular solutions there also have $\phi' = O(x^{n/2})$ in the distance variable $x = -x^0$ (§5), and $g^{00} = +\,x^{-n}/c$, so $X = g^{00}(\partial_0\phi)^2 + |\nabla\phi|^2 \sim x^{-n}\cdot x^{n} + O(1) = O(1)$ — now with the kinetic term non-negative, the metric being positive-definite — and the curvature-sourcing invariant is $O(1)$ on both sides of $\Sigma$. The raised-component caveat below applies verbatim on the Euclidean side ($T^{00}\sim x^{-n}$).

Two points, stated honestly. First, individual *raised* components do diverge — e.g. $T^{00} = (g^{00})^2 T_{00}\sim x^{-n}$ — even though the *scalar invariants* stay finite; the protection is on contractions, not components. Second, this is a test field on a fixed background: it shows the benign geometry is *compatible* with finite stress-energy, not that the coupled system has a benign solution.

## 7. The crossing structure **(Sketch)**

Collecting §§3–6, the surface is traversed with a definite, sector-dependent character.

- **Spacelike / off-shell.** Crosses freely. Spacelike curves continue with character intact (spacelike geodesic continuation is Sketch — §4); spacelike field modes propagate through $\Sigma$ unchanged. This is the clean case.

- **Timelike / on-shell.** Does not cross as a real classical worldline — there is no timelike direction beyond $\Sigma$. Its continuation is the *evanescent* branch of §5: the propagator's exponentially decaying tail into the Euclidean region. Quantitatively, the complexified timelike geodesic has imaginary proper length $i\sigma_E$ (with $\sigma_E$ the Euclidean geodesic distance), so the worldline action $S=-m\!\int d\tau$ carries an exponent of magnitude $m\sigma_E$ — exactly the decay exponent of the massive propagator's evanescent tail. The agreement is not a coincidence: it is the Schwinger proper-time / worldline representation, whose saddle over a Euclidean separation is the geodesic of length $\sigma_E$.

So "worldlines crossing $\Sigma$" is true in two distinct senses. Spacelike (virtual, off-shell) lines cross as real, propagating objects. Massive (on-shell) lines "cross" only in the sense that the off-shell propagator's decaying tail penetrates the Euclidean region; the massive particle itself is confined to the Lorentzian phase. This is internally consistent, and it is the picture.

## 8. The one mechanism **(Sketch as a unification claim; each bullet is Rigorous given §§3–6)**

*(Label reset from "Rigorous, given §§3–6" in the July 2026 red-team audit: the three bullets below individually verify, but "every benign fact is the same fact" is an organizing observation, not a theorem — the proper-time bullet contains no $g^{00}$ at all, its mechanism being $\sqrt{-\lambda}\to 0$ directly from the line element — and the escorting statement is checked only on this product background, not for general covariant objects on general degenerate metrics.)*

The recurring mechanism: the metric determinant supplies $\sqrt{|g|}=\sqrt{|\lambda|}$, and the appearances of $g^{00}=1/\lambda$ in the objects computed above are escorted by it:

- in the d'Alembertian, $\sqrt{|g|}\,g^{00}\sim x^{-n/2}$, which clears to a Fuchsian point rather than an essential one;
- in proper time, the line element carries $\sqrt{-\lambda}\to 0$, making the integral converge;
- in the stress–energy, the field equation forces $\phi'\sim x^{n/2}$, exactly compensating $g^{00}\sim x^{-n}$.

Reading geodesic completeness-to-the-boundary, the regular-singular structure of the field equation, finite stress–energy, and (at §7's Sketch level) the continuing worldline saddle as four faces of one escorting is the Sketch-level unification claim of this section's label: it fits three of the four faces exactly (proper time converges by $\sqrt{-\lambda}\to 0$ alone, with no $g^{00}$ to escort). On a prescribed $\lambda$ the degenerate surface is in any case far better behaved than the bare $g^{-1}\to\infty$ suggests — that much is the content of §§3–6, established piecewise.

## 9. What this does not claim

The result is narrow, and the following are deliberately *not* asserted.

1. **No dynamics for $\lambda$.** The background is prescribed. We do not derive $\lambda$, nor exhibit a configuration that sources it. Whether a $\lambda(\phi)$ for a physical order parameter can produce this profile is not addressed.

2. **No backreaction.** Everything is at the test-field level on a fixed metric. The self-consistent problem — a field solving its own equation on the geometry it sources — is open. In particular, bulk consistency on *both* sides is fully compatible with a distributional surface layer (an Israel-type shell) *at* $\Sigma$, which a fixed-background analysis structurally cannot see. We do not claim the self-consistent surface is shell-free. (There is suggestive evidence it can be: the Fuchsian $\phi'\to 0$ makes the Dray–Manogue–Tucker no-layer condition imposable. This is not a proof.)

3. **No predictions.** Nothing here is an empirical prediction. The note is a consistency and structure result only.

4. **The strong crossing is contour-dependent.** Whether the on-shell sector "crosses" via a genuine complex continuation, or instead terminates at a real boundary, is a global choice — a path-integral contour / boundary-condition choice — not fixed by local data at $\Sigma$. This is the same ambiguity the gravitational path integral faces in the no-boundary context, and it is *not* resolved here. The evanescent-tail picture of §7 is the continuation-favoring reading; the terminating reading is equally consistent with the local analysis.

5. **A single, special background.** Flat spatial slices, $\lambda$ a function of one coordinate. Curved slices, $\lambda$ with spatial structure, caustics forming before $\Sigma$, and other genericities are not covered.

6. **No quantization.** Wheeler–DeWitt structure, emergent-time mechanisms, and the relational-time question are out of scope. This note is entirely classical / test-field.

7. **"De-particling" is interpretation.** The neutral fact is timelike geodesic incompleteness at $\Sigma$ with bounded curvature. Calling it a graceful phase boundary is a reading whose validity depends on the open backreaction question.

## Relation to existing work

The construction sits in the lineage of the classical signature-change literature. The cosmological signature-change solutions of Ellis, Sumeruk, Coule and Hellaby [1], and Ellis's covariant treatment [2], established the setting. Junction conditions at the degenerate surface $\Sigma$ were developed in two *mutually incompatible* forms. Dray, Manogue and Tucker [4] require continuity of the field and of the canonical momentum $\sqrt{|g|}\,g^{00}\partial_0\phi$ (finite and generically nonvanishing at $\Sigma$, no distributional shell) — the condition whose imposability §5 here obtains through the finiteness of the one-sided limits. Hayward [3] derived a strictly stronger condition: the spatial metric and the field must be *instantaneously stationary* at the junction (vanishing extrinsic curvature and vanishing momentum, $\pi|_\Sigma = 0$), and he explicitly rejected the Dray–Manogue–Tucker continuity condition as failing the field equations (the explicit rebuttal appears in his gr-qc/9303034). The generic §5 solution has $\pi \to$ a finite *nonzero* constant, so it satisfies the Dray–Manogue–Tucker condition and violates Hayward's; only the dominant ($s=0$ from the Lorentzian side) branch satisfies both. The no-layer reading adopted here is therefore the Dray–Manogue–Tucker position in a genuine published dispute — contested primarily by Hayward [3], with Hellaby and Dray [5] separately showing that standard conservation laws can fail across a classical signature change even on the Dray–Manogue–Tucker reading (cf. §9.2, §9.4). (An earlier revision of this paragraph attributed the continuity-of-momentum condition jointly to [3] and [4]; that misattributed to Hayward the position he argued against, and was corrected in the July 2026 red-team citation re-verification.) The geodesic behaviour at the degenerate surface — completeness to, and transverse extendability across, the type-change hypersurface — is the subject of the degenerate-metric analyses of Kossowski and Kriele [6,7]; note that the extendability-across question is exactly the step §4 leaves at Sketch level.

The techniques used here — geodesic completeness to a degenerate surface, junction data at $\Sigma$, and the treatment of a free scalar field across the signature change — are standard in that body of work, and no novelty is claimed for them. (The Frobenius/Bessel reduction of §5 is a convenience of presentation; the underlying scalar-field-across-$\Sigma$ problem and its no-surface-layer matching are those of [4], reached there by distributional rather than series methods.) What this note isolates is the *combination*: that geometry, geodesics, field, and stress–energy are simultaneously consistent on this background through one mechanism (§8), and the sector-asymmetric crossing picture that results. Whether the present results reproduce or extend the matching and traversability conditions of [3]–[5] is noted where relevant and otherwise left to the original sources.

### References

The following entries were verified (author, title, journal, volume, page, year, and content-match to the technique attributed) per METHODOLOGY §Citation Discipline, paper-grade tier, during the SCB-4 citation-verification pass (issue #135).

[1] G. F. R. Ellis, A. Sumeruk, D. Coule, and C. Hellaby, "Change of signature in classical relativity," *Classical and Quantum Gravity* **9**, 1535 (1992). DOI: 10.1088/0264-9381/9/6/011.

[2] G. F. R. Ellis, "Covariant change of signature in classical relativity," *General Relativity and Gravitation* **24**, 1047 (1992). DOI: 10.1007/BF00756946.

[3] S. A. Hayward, "Signature change in general relativity," *Classical and Quantum Gravity* **9**, 1851 (1992); Erratum, *ibid.* **9**, 2543 (1992). DOI: 10.1088/0264-9381/9/8/007.

[4] T. Dray, C. A. Manogue, and R. W. Tucker, "The scalar field equation in the presence of signature change," *Physical Review D* **48**, 2587 (1993). DOI: 10.1103/PhysRevD.48.2587; arXiv:gr-qc/9303002.

[5] C. Hellaby and T. Dray, "Failure of standard conservation laws at a classical change of signature," *Physical Review D* **49**, 5096 (1994). DOI: 10.1103/PhysRevD.49.5096; arXiv:gr-qc/9404001.

[6] M. Kossowski and M. Kriele, "Smooth and discontinuous signature type change in general relativity," *Classical and Quantum Gravity* **10**, 2363 (1993). DOI: 10.1088/0264-9381/10/11/019.

[7] M. Kossowski and M. Kriele, "Transverse, type-changing, pseudo-Riemannian metrics and the extendability of geodesics," *Proceedings of the Royal Society of London A* **444**, 297 (1994). DOI: 10.1098/rspa.1994.0019.
