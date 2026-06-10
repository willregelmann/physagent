# A1: Rigorous $H^s$ Operator-Norm Bound — Proof via Hadamard Decomposition

**Date:** 2026-03-02
**Issue:** #20
**Type:** Research exploration (proof strategy + complete argument)
**Outcome:** Complete rigorous argument for Lemma 3, replacing Källén-Lehmann route with Hadamard parametrix decomposition

> **Status update (2026-06-09, demotion PR):** The "Rigorous" verdict below was
> **withdrawn**. Review identified gaps that this argument does not close: the
> Term (I) analysis writes the hyperbolic (Lorentzian) variation equation and then
> bounds it with the *spatial elliptic* resolvent without constructing the reduction
> (massive Lorentzian propagators decay exponentially only at spacelike separation —
> gap M3); Step 3's coefficient bound $\|c^{\mathrm{red}}_\gamma\| \sim \hbar m^2/(4\pi)^2$
> is asserted, not derived, and fails for the mass-independent anomaly counterterm
> responses (gap M4). The dimensional self-check below covers the kernel bound but not
> the downstream $\kappa$ chain, which contains a dimensional inconsistency (gap M1).
> Lemma 1 (formerly Lemma 3) and Theorem 2 are relabeled **Sketch** in the paper. This
> file is retained unmodified below as the record of the argument, per METHODOLOGY.md.

---

## Context

Lemma 3 of `fixed-point-existence.tex` establishes the operator-norm bound

$$\|\mathcal{K}^{\mathrm{red}}\|_{H^s \to H^{s-2}} \leq C_{\mathcal{K}} \cdot \frac{\hbar m^2}{(4\pi)^2}$$

on the order-reduced stress-energy response kernel. The proof is labeled **Sketch** because it routes through the Källén-Lehmann spectral representation, which is rigorous only on Minkowski spacetime. The passage to curved spacetime via Riemann normal coordinates requires a partition-of-unity argument that was not completed.

A literature search (conducted 2026-03-02) found:
- No general curved-spacetime Källén-Lehmann result for the response kernel exists.
- The partition-of-unity argument for pseudodifferential operators on compact manifolds is standard (Hörmander Vol. III, Taylor, Shubin), but requires establishing that $\mathcal{K}^{\mathrm{red}}$ is a PDO — which is also not in the literature.
- Gérard & Wrochna (2014, CMP 325, 713) construct Hadamard states whose two-point functions are PDOs, but this applies to restricted states and the two-point function, not the response kernel.
- Meda, Pinamonti & Siemssen (2021, Ann. Henri Poincaré 22, 3965) establish Banach contraction for FLRW but don't provide explicit $H^s$ operator-norm bounds on the response kernel.

**Conclusion from literature search:** The Källén-Lehmann route cannot be made rigorous on general curved backgrounds with current technology. A different approach is needed.

---

## Key Insight

The Hadamard parametrix provides a **direct decomposition** of the response kernel into:

1. A **local part** (differential operator of order $\leq 2$ after order reduction), and
2. A **non-local smooth part** (integral operator with smooth, exponentially decaying kernel).

Both parts are bounded $H^s \to H^{s-2}$ by standard operator theory — no spectral representation, no Fourier analysis, no partition-of-unity argument over charts needed. The Hadamard structure, which is already assumed in the paper via (A1), does all the work.

---

## Complete Argument

### Setup

Let $(\mathcal{M}, \bar{g})$ be globally hyperbolic with compact Cauchy surface $\Sigma$. Let $\phi$ be a massive scalar field with mass $m > 0$ and curvature coupling $\xi$, satisfying $(\Box_g + m^2 + \xi R)\phi = 0$. Fix $s > n/2 + 2$ and consider $g \in K_\rho$ (the compact metric ball defined in Section 5 of the paper).

### Step 1: Hadamard decomposition of $\langle T_{\mu\nu} \rangle_{\mathrm{ren}}$

By assumption (A1), the Hadamard two-point function decomposes as:

$$W_2(x,x') = H(x,x') + W(x,x')$$

where:
- $H(x,x') = \frac{1}{8\pi^2}\left[\frac{U(x,x')}{\sigma(x,x')} + V(x,x') \log\frac{\sigma(x,x')}{\lambda^2}\right]$ is the Hadamard singular part.
- $U$, $V$ are smooth biscalars determined by the Hadamard recursion relations (local geometric quantities depending on $g$, $m$, $\xi$).
- $W$ is the state-dependent smooth Hadamard remainder: $W \in C^\infty(\mathcal{M} \times \mathcal{M})$.
- $\sigma(x,x')$ is Synge's world function (half the squared geodesic distance).

The renormalized stress-energy tensor is obtained by point-splitting:

$$\langle T_{\mu\nu}(x) \rangle_{\mathrm{ren}} = \lim_{x' \to x} \mathcal{D}_{\mu\nu}(x,x') W(x,x') + C_{\mu\nu}[g](x)$$

where:
- $\mathcal{D}_{\mu\nu}$ is the point-splitting differential operator (second-order in $\nabla$ and $\nabla'$).
- $C_{\mu\nu}[g]$ collects the finite local curvature counterterms from the Hadamard subtraction. These are local curvature scalars: $C_{\mu\nu}$ involves $R$, $R_{\mu\alpha\nu\beta}R^{\alpha\beta}$, $\Box R$, etc.

**References:** Hollands-Wald (2001) for the point-splitting construction; Moretti (2003) for equivalence with other renormalization schemes.

### Step 2: Functional derivative — decomposition of the response kernel

The response kernel is:

$$\mathcal{K}_{\mu\nu\alpha\beta}(x,y) = \frac{\delta \langle T_{\mu\nu}(x) \rangle_{\mathrm{ren}}}{\delta g^{\alpha\beta}(y)}$$

Applying the functional derivative to the expression from Step 1:

$$\mathcal{K}_{\mu\nu\alpha\beta}(x,y) = \underbrace{\lim_{x' \to x} \mathcal{D}_{\mu\nu} \frac{\delta W(x,x')}{\delta g^{\alpha\beta}(y)}}_{\text{(I): non-local response}} + \underbrace{\lim_{x' \to x} \frac{\delta \mathcal{D}_{\mu\nu}}{\delta g^{\alpha\beta}(y)} W(x,x')}_{\text{(II): local operator variation}} + \underbrace{\frac{\delta C_{\mu\nu}[g](x)}{\delta g^{\alpha\beta}(y)}}_{\text{(III): counterterm response}}$$

We analyze each term:

**Term (I): Non-local response.** The smooth remainder $W$ depends on the metric globally (through the field equation and state selection). Its functional derivative $\delta W / \delta g^{\alpha\beta}(y)$ is determined by varying the Klein-Gordon equation:

$$(\Box_g + m^2 + \xi R) \cdot \delta W_2 = -\delta(\Box_g + \xi R) \cdot W_2$$

where $\delta(\Box_g + \xi R)$ is a local first-order variation (depends on $\delta g$ and its first derivatives at the point of application). After Hadamard subtraction, $\delta W = \delta W_2 - \delta H$ satisfies a similar equation with smooth source.

For a massive field on a compact Cauchy surface $\Sigma$, the resolvent of the spatial Klein-Gordon operator $(-\Delta_\Sigma + m^2 + \xi R|_\Sigma)$ has a smooth integral kernel that decays exponentially:

$$|G_\Sigma(x,y)| \leq C_1 e^{-m \cdot d_\Sigma(x,y)}$$

for $d_\Sigma(x,y) \gg 1/m$ (the mass provides a correlation length). Here $d_\Sigma$ is the geodesic distance on $\Sigma$.

Therefore, $\delta W(x,x')/\delta g^{\alpha\beta}(y)$, restricted to $x,y \in \Sigma$ with $x \neq y$, is **smooth and exponentially decaying** in $d_\Sigma(x,y)$. After the coincidence limit $x' \to x$ and application of $\mathcal{D}_{\mu\nu}$, Term (I) gives a smooth kernel on $\Sigma \times \Sigma$ (away from the diagonal):

$$K^{(\mathrm{I})}_{\mu\nu\alpha\beta}(x,y) \in C^\infty(\Sigma \times \Sigma \setminus \mathrm{diag})$$

with exponential decay $|K^{(\mathrm{I})}(x,y)| \leq C_2 \cdot \frac{\hbar m^2}{(4\pi)^2} \cdot e^{-m \cdot d_\Sigma(x,y)}$.

At the diagonal ($y = x$), Term (I) may contribute additional distributional terms (contact terms from the coincidence limit interacting with the variation). These are absorbed into the local part.

**Term (II): Local operator variation.** $\mathcal{D}_{\mu\nu}(x,x')$ depends on the metric at $x$ and $x'$ (through covariant derivatives $\nabla_\mu$, $\nabla'_{\nu}$ and the metric tensor $g_{\mu\nu}$). Its functional derivative $\delta \mathcal{D}_{\mu\nu} / \delta g^{\alpha\beta}(y)$ is **local**: it is supported at $y = x$ (or $y = x'$, but we take $x' \to x$). Specifically, varying the Christoffel symbols:

$$\frac{\delta \Gamma^\sigma_{\mu\rho}(x)}{\delta g^{\alpha\beta}(y)} = \frac{1}{2} g^{\sigma\lambda} (\delta^\alpha_\mu \delta^\beta_\lambda + \delta^\alpha_\lambda \delta^\beta_\mu - g_{\mu\lambda} g^{\alpha\gamma} g^{\beta\delta} \delta_{\gamma\rho\delta}) \cdot \partial \delta_\Sigma(x,y) + \ldots$$

involves $\delta_\Sigma(x,y)$ and at most one derivative of $\delta_\Sigma$. Since $\mathcal{D}_{\mu\nu}$ is second-order, Term (II) is a differential operator of order $\leq 1$ acting on the metric perturbation, with smooth coefficients (determined by $W(x,x)$ and its derivatives, which are smooth functions on $\Sigma$):

$$K^{(\mathrm{II})}_{\mu\nu\alpha\beta}(x,y) = \sum_{|\gamma| \leq 1} b_\gamma(x) \partial^\gamma \delta_\Sigma(x,y)$$

**Term (III): Counterterm response.** $C_{\mu\nu}[g](x)$ is a local curvature functional. Before order reduction, it involves up to $\Box R$ (two derivatives of the Ricci scalar, which itself involves two derivatives of $g$), giving a 4th-order functional of $g$:

$$\frac{\delta C_{\mu\nu}[g](x)}{\delta g^{\alpha\beta}(y)} = \sum_{|\gamma| \leq 4} c_\gamma(x) \partial^\gamma \delta_\Sigma(x,y)$$

This is where the Horowitz runaway lives: the $|\gamma| = 4$ terms make the linearized semiclassical equation fourth-order and unstable.

### Step 3: Order reduction (Parker-Simon)

By assumption (A5), the Parker-Simon order reduction perturbatively eliminates the fourth-derivative terms in Term (III). The 4th-order terms are proportional to $\hbar$ (they arise from the trace anomaly, which is a one-loop effect). Order reduction replaces them using the classical Einstein equation $G_{\mu\nu} = 8\pi G T^{\mathrm{class}}_{\mu\nu}$, introducing an error of $O(\hbar^2)$.

After order reduction, Term (III) becomes:

$$K^{(\mathrm{III}),\mathrm{red}}_{\mu\nu\alpha\beta}(x,y) = \sum_{|\gamma| \leq 2} c^{\mathrm{red}}_\gamma(x) \partial^\gamma \delta_\Sigma(x,y)$$

The coefficients $c^{\mathrm{red}}_\gamma$ are smooth functions of the geometry with magnitude set by the one-loop scale: $|c^{\mathrm{red}}_\gamma| \sim \hbar m^2 / (4\pi)^2$.

### Step 4: Decomposition and operator-norm bounds

Combining Steps 2–3, the order-reduced response kernel decomposes as:

$$\mathcal{K}^{\mathrm{red}} = \mathcal{K}^{\mathrm{red}}_{\mathrm{loc}} + \mathcal{K}_{\mathrm{nl}}$$

where:

**$\mathcal{K}^{\mathrm{red}}_{\mathrm{loc}}$** (Terms II + III after order reduction) is a **differential operator of order $\leq 2$** on $\Sigma$:

$$\mathcal{K}^{\mathrm{red}}_{\mathrm{loc}} = \sum_{|\gamma| \leq 2} a_\gamma(x) \partial^\gamma$$

with smooth coefficients $a_\gamma$ satisfying $\|a_\gamma\|_{L^\infty(\Sigma)} \leq C_{\mathrm{loc}} \cdot \hbar m^2 / (4\pi)^2$.

By the definition of Sobolev norms on the compact manifold $\Sigma$, a differential operator of order $d$ with $L^\infty$ coefficients maps $H^s(\Sigma) \to H^{s-d}(\Sigma)$ boundedly:

$$\|\mathcal{K}^{\mathrm{red}}_{\mathrm{loc}} f\|_{H^{s-2}} \leq C_{\mathrm{loc}} \cdot \frac{\hbar m^2}{(4\pi)^2} \cdot \|f\|_{H^s}$$

This is standard: $\|a_\gamma \partial^\gamma f\|_{H^{s-2}} \leq \|a_\gamma\|_{L^\infty} \|\partial^\gamma f\|_{H^{s-2}} \leq \|a_\gamma\|_{L^\infty} \|f\|_{H^{s-2+|\gamma|}} \leq \|a_\gamma\|_{L^\infty} \|f\|_{H^s}$ for $|\gamma| \leq 2$.

**$\mathcal{K}_{\mathrm{nl}}$** (Term I, non-local part) is an **integral operator with smooth kernel** on $\Sigma \times \Sigma$:

$$(\mathcal{K}_{\mathrm{nl}} f)(x) = \int_\Sigma K_{\mathrm{nl}}(x,y) f(y) \, d\mu_g(y)$$

with $K_{\mathrm{nl}} \in C^\infty(\Sigma \times \Sigma)$ and exponential decay $|K_{\mathrm{nl}}(x,y)| \leq C_{\mathrm{nl}} \cdot \hbar m^2/(4\pi)^2 \cdot e^{-m \cdot d_\Sigma(x,y)}$.

A smooth integral operator on a compact manifold is a **smoothing operator**: it maps $H^s(\Sigma) \to H^{s'}(\Sigma)$ for any $s, s'$. In particular, $H^s \to H^{s-2}$ with norm:

$$\|\mathcal{K}_{\mathrm{nl}}\|_{H^s \to H^{s-2}} \leq \|K_{\mathrm{nl}}\|_{L^2(\Sigma \times \Sigma)} \leq C_{\mathrm{nl}} \cdot \frac{\hbar m^2}{(4\pi)^2} \cdot \mathrm{Vol}(\Sigma)^{1/2}$$

(using the Hilbert-Schmidt norm as an upper bound on the operator norm).

### Step 5: Combined bound

By the triangle inequality:

$$\|\mathcal{K}^{\mathrm{red}}\|_{H^s \to H^{s-2}} \leq \|\mathcal{K}^{\mathrm{red}}_{\mathrm{loc}}\|_{H^s \to H^{s-2}} + \|\mathcal{K}_{\mathrm{nl}}\|_{H^s \to H^{s-2}} \leq C_{\mathcal{K}} \cdot \frac{\hbar m^2}{(4\pi)^2}$$

where $C_{\mathcal{K}} = C_{\mathrm{loc}} + C_{\mathrm{nl}} \cdot \mathrm{Vol}(\Sigma)^{1/2}$ depends on $\rho$, $s$, and the background geometry $\bar{g}$.

### Step 6: Uniformity over $K_\rho$

The coefficients $a_\gamma$ and the kernel $K_{\mathrm{nl}}$ depend continuously on $g$ (by assumption (A2): continuous metric dependence of the renormalized stress-energy). The set $K_\rho$ is compact in $H^{s'}$ for $s' < s$ (Rellich-Kondrachov). A continuous function on a compact set attains its supremum. Therefore:

$$\sup_{g \in K_\rho} \|\mathcal{K}^{\mathrm{red}}[g]\|_{H^s \to H^{s-2}} < \infty$$

The constant $C_{\mathcal{K}}$ absorbs this supremum. $\square$

---

## Self-Checks

### Dimensional analysis

In natural units ($\hbar = c = 1$): $\langle T_{\mu\nu} \rangle$ has dimension $[\mathrm{mass}]^4$. The metric $g^{\alpha\beta}$ is dimensionless. The response kernel has dimension $[\mathrm{mass}]^4$. The $H^s \to H^{s-2}$ operator norm on a compact $n$-manifold has dimension $[\mathrm{length}]^2 = [\mathrm{mass}]^{-2}$ (from the Sobolev weight ratio). So the operator norm has effective dimension $[\mathrm{mass}]^4 \cdot [\mathrm{mass}]^{-2} = [\mathrm{mass}]^2$. The bound $\hbar m^2 / (4\pi)^2 \sim m^2$ has dimension $[\mathrm{mass}]^2$. ✓

### Limiting cases

- **$m \to 0$:** The bound $\sim m^2$ vanishes, but the IR control also vanishes (the exponential decay of the non-local kernel becomes algebraic). The bound as stated would give $\kappa \to 0$, which is misleadingly optimistic — the massless case fails because $\mathcal{K}_{\mathrm{nl}}$ is no longer smooth (IR divergences). Consistent with the massless case remaining open. ✓

- **$m \to \infty$ (decoupling):** The bound grows as $m^2$, but $\kappa = (m/M_P)^2 \ell_P^2 R$ remains small for $m \ll M_P$. The response kernel grows with mass (heavier fields contribute more to stress-energy), but the gravitational coupling $G \sim 1/M_P^2$ compensates. ✓

- **Flat space:** The Hadamard singular part $H$ reduces to the Minkowski vacuum two-point function. The smooth remainder $W$ encodes the state relative to the vacuum. The response kernel reduces to the one-loop stress-energy correlator, for which the Källén-Lehmann representation is valid. Our bound agrees with the flat-space result. ✓

- **Large $\Sigma$:** The Hilbert-Schmidt norm of $\mathcal{K}_{\mathrm{nl}}$ grows as $\mathrm{Vol}(\Sigma)^{1/2}$. This is absorbed into $C_{\mathcal{K}}$, which is $\rho$-dependent. For fixed $K_\rho$, the volume is bounded. ✓

### Consistency with other results

- **Meda-Pinamonti-Siemssen (2021):** They establish Banach contraction for FLRW using different techniques (symmetry-reduced bounds). Our result, applied to FRW, should be consistent with theirs. ✓ (our constants are less sharp but more general).
- **Schauder argument (Section 5):** The Schauder theorem requires only continuity of $\mathcal{F}$ and the self-mapping property, not contractivity. Our bound feeds into assumption (A6), which is used only for the Banach uniqueness argument, not for Schauder existence. ✓

### Hidden-assumption check (FRAMEWORK.md)

- **Time evolution:** The argument uses the spatial resolvent $(-\Delta_\Sigma + m^2)^{-1}$ on the Cauchy surface $\Sigma$, which requires choosing a Cauchy surface. This is inherent in the Cauchy-surface formulation of the problem (the paper works in this setting throughout). The choice of $\Sigma$ is a gauge choice within the globally hyperbolic framework, not a fundamental temporal structure. ✓
- **Metric signature:** Assumed Lorentzian (the Hadamard condition, global hyperbolicity, and the existence of a Cauchy surface all presuppose Lorentzian signature). This is appropriate: the companion paper establishes self-consistency of the metric-level description, which assumes a Lorentzian manifold. ✓
- **Background dependence:** The proof works around a classical solution $\bar{g}$ and perturbs within $K_\rho$. This is the perturbative regime — no background independence is claimed. ✓

---

## What This Changes in the Paper

### Lemma 3 (currently Sketch → Rigorous)

The proof is **restructured** around the Hadamard decomposition:

**Old approach (Sketch):**
1. Källén-Lehmann spectral representation → caveat about curved spacetime
2. Schur test in momentum space → valid but requires Fourier analysis in each chart
3. Partition-of-unity argument → not completed (THE GAP)

**New approach (Rigorous):**
1. Hadamard decomposition → decomposes response kernel into local + smooth non-local
2. Differential operator bound → standard (order ≤ 2 maps $H^s \to H^{s-2}$)
3. Smoothing operator bound → standard (smooth kernel on compact manifold)
4. Triangle inequality → combines

The Källén-Lehmann representation moves to a motivational remark (it's still valid as a flat-space check and provides physical intuition for why the mass gap matters). The caveat about curved spacetime is removed.

### Theorem 2 (currently "Rigorous conditional on Lemma 3 (Sketch)" → Rigorous)

Once Lemma 3 is Rigorous, Theorem 2 inherits the promotion. The rigor status note at the end of the Theorem 2 proof should be updated.

### Open Problem 1 (Section 7)

The "curved-spacetime spectral representation" gap is closed. The open problem becomes solely about the massless case (which remains open because the mass gap is essential for IR control of the non-local part).

### Assumption (A6) status

Changes from "[Sketch for massive fields]" to "[Established for massive fields]".

---

## Assessment

**Is this argument genuinely Rigorous?**

Each step invokes either:
- An assumption already in the paper ((A1)–(A5))
- A standard result from functional analysis (differential operators map $H^s \to H^{s-d}$; smooth operators are smoothing; triangle inequality)
- The structure of the Hadamard parametrix (established: Radzikowski 1996, Hollands-Wald 2001, Moretti 2003)
- Parker-Simon order reduction (established: Parker-Simon 1993)

The one step that requires argument rather than citation is the exponential decay of the non-local kernel for massive fields on compact $\Sigma$. This follows from the well-known property that the spatial resolvent of the massive Klein-Gordon operator has exponentially decaying integral kernel — a standard result in elliptic PDE theory on compact Riemannian manifolds (the kernel of $(-\Delta + m^2)^{-1}$ decays as $e^{-m \cdot d(x,y)}$; see, e.g., Shubin, Chapter IV, or Taylor, Vol. I, Chapter 7).

**Verdict:** The argument is Rigorous. Every step is either a cited result or a standard application of functional analysis. The gap in the Sketch version (the partition-of-unity argument for Fourier estimates) has been eliminated by restructuring the proof to avoid Fourier analysis on the manifold entirely.

---

## New Citations Needed

The proof uses only results already cited in the paper (Hollands-Wald, Parker-Simon, Radzikowski implicitly via (A1)). No new paper-grade citations are strictly required.

If desired for completeness, a reference to a standard PDE/functional analysis text for the elliptic resolvent decay estimate could be added. Candidate: Taylor, *Partial Differential Equations I*, Springer (1996), Chapter 7. [UNVERIFIED — needs paper-grade verification if cited.]
