# CE-3: Do distinct smooth structures yield distinct Einstein–Hilbert actions?

**Date:** 2026-06-19
**Type:** Research exploration (differential geometry / 4-manifold topology)
**Issue:** #29 (CE-3)
**Outcome:** Partial positive result. The worst case — a topological invariant
forcing the action uniform — is **rigorously excluded**. A strong, rigorous,
*Riemannian* precedent (LeBrun, via Seiberg–Witten theory) shows scale-fixed
scalar-curvature functionals genuinely distinguish smooth structures on
homeomorphic, non-diffeomorphic compact 4-manifolds. Transferring this to the
framework's actual setting — *non-compact* (exotic $\mathbb{R}^4$) and
*Lorentzian* metrics — is open and is the residual gap.

---

## The question (from the toy model)

The N=4 toy model (`2026-03-04-toy-model.md`) showed that the co-emergence
mechanism is non-trivial **only when the external field $h_{rc}$ is non-uniform**
across smooth structures: with $h = (1,1,1,1)$ and $\beta = 0$, the fixed point
is the trivial uniform product state with no coherences, for any signature
$\theta$. In the full theory, $h_{rc}$ is intended to be the Einstein–Hilbert
action $S_{\mathrm{EH}}[g^*_\sigma]$ of the self-consistent metric on smooth
structure $\sigma$. So the mechanism's non-triviality is hostage to a purely
mathematical question:

> For a 4-manifold $\mathcal{M}$ admitting distinct smooth structures
> $\sigma_1, \sigma_2 \in \mathrm{Sm}(\mathcal{M})$, is
> $S_{\mathrm{EH}}[g^*_{\sigma_1}] \neq S_{\mathrm{EH}}[g^*_{\sigma_2}]$,
> or is the action forced equal by some topological invariant?

The issue frames two branches: **(1)** distinct structures generically support
distinct actions (a derived structural prediction — good for the framework), or
**(2)** the action is pinned by a topological invariant shared across smooth
structures, in which case $\mu^*$ is uniform on $\mathrm{Sm}(\mathcal{M})$ and
the framework produces only classical statistics (fatal).

Here $S_{\mathrm{EH}}[g] = \int_{\mathcal{M}} s_g \, d\mu_g$ is the
(matter-free) total scalar curvature, $s_g$ the scalar curvature, $d\mu_g$ the
metric volume form.

---

## Part I — Branch (2) is rigorously excluded: $S_{\mathrm{EH}}$ is not a topological invariant

**Claim 1 (Rigorous).** *The total scalar curvature $S_{\mathrm{EH}}[g]$ is
neither a topological nor a smooth invariant. No topological invariant can force
it to take equal values across smooth structures.*

Two independent reasons:

**(a) Scale dependence.** Under a constant rescaling $g \mapsto \lambda^2 g$
($\lambda > 0$) in dimension $n$, the scalar curvature transforms as
$s \mapsto \lambda^{-2} s$ and the volume form as
$d\mu \mapsto \lambda^{n} d\mu$, so
$$
S_{\mathrm{EH}}[\lambda^2 g] = \lambda^{\,n-2}\, S_{\mathrm{EH}}[g]
\;\xrightarrow{\;n=4\;}\; \lambda^2\, S_{\mathrm{EH}}[g].
$$
The value can be sent to $0$ or $\pm\infty$ by rescaling a single fixed metric.
A topological invariant is a number attached to $\mathcal{M}$ alone; a quantity
that a metric rescaling moves continuously through all of $\mathbb{R}_{\geq 0}$
(or $\mathbb{R}$, when $s$ changes sign) cannot be one.

**(b) The topological curvature integrals are $\chi$ and $\tau$, and
$S_{\mathrm{EH}}$ is independent of both.** The only diffeomorphism-invariant
integrals of the curvature of a closed 4-manifold that *are* topological are the
two classical ones:
$$
\chi(\mathcal{M}) = \frac{1}{8\pi^2}\int_{\mathcal{M}}
\Big(|W|^2 - \tfrac12 |\mathring{\mathrm{Ric}}|^2 + \tfrac{1}{24}s^2\Big)\,d\mu
\quad\text{(Gauss–Bonnet–Chern),}
$$
$$
\tau(\mathcal{M}) = \frac{1}{12\pi^2}\int_{\mathcal{M}}
\big(|W^+|^2 - |W^-|^2\big)\,d\mu
\quad\text{(Hirzebruch signature theorem).}
$$
Both are *homeomorphism* invariants (Freedman): they are blind to smooth
structure. The linear-in-curvature functional $\int s\,d\mu$ does not appear in
either combination and is algebraically independent of them — it weights $s$ to
the first power, while $\chi,\tau$ see only quadratic curvature scalars. There
is no representation of $\int s\,d\mu$ as a function of $\chi$ and $\tau$.

**Conclusion of Part I.** Branch (2) — the fatal case — *does not occur*. There
is no topological theorem that forces $S_{\mathrm{EH}}$ uniform across
$\mathrm{Sm}(\mathcal{M})$. The framework clears its lowest bar rigorously.

> **Caveat made explicit.** Claim 1 says the action is *not forced equal*. It
> does not by itself say the actions *are* different — "not a topological
> invariant" is necessary but not sufficient for branch (1). Part II supplies
> the positive content; Part III states where it stops.

---

## Part II — Branch (1), rigorously, in the compact Riemannian case

Because $S_{\mathrm{EH}}$ is scale-dependent (Claim 1a), the sharp question is
not about the *raw* action — which the self-consistent dynamics will scale-fix
anyway — but about a **scale-invariant** distillate of it, where one can ask
cleanly whether smooth structure changes the value. There are two canonical
scale-invariant functionals built from $s$, and Seiberg–Witten theory shows
**both distinguish smooth structures**.

### II.1 The Yamabe invariant

The normalized total scalar curvature (Yamabe functional) is
$$
\mathcal{Q}(g) = \frac{\int_{\mathcal{M}} s_g\,d\mu_g}{\big(\mathrm{Vol}(g)\big)^{(n-2)/n}},
$$
scale-invariant by construction. The **Yamabe invariant** of a smooth compact
manifold is the min–max
$$
\mathcal{Y}(\mathcal{M}) = \sup_{[g]} \ \inf_{g'\in[g]} \mathcal{Q}(g'),
$$
the inner infimum running over a conformal class (the Yamabe constant of $[g]$,
always attained — solution of the Yamabe problem), the outer supremum over
conformal classes. $\mathcal{Y}$ is a **diffeomorphism invariant of the smooth
structure**.

**Claim 2 (Rigorous; LeBrun 1996, 1999).** *The sign and value of
$\mathcal{Y}$ depend on the smooth structure, not merely the homeomorphism
type.* For $\mathcal{M}$ underlying a complex algebraic surface, LeBrun's
theorem ties the sign of $\mathcal{Y}$ to the Kodaira dimension
[LeBrun, *Kodaira dimension and the Yamabe problem*, Comm. Anal. Geom. **7**
(1999) 133–156]:
$$
\mathrm{sign}\,\mathcal{Y}(\mathcal{M}) =
\begin{cases}
+ & \mathrm{Kod} = -\infty,\\
0 & \mathrm{Kod} = 0,1,\\
- & \mathrm{Kod} = 2 \ (\text{general type}).
\end{cases}
$$
For the negative (general-type) case the value is computed exactly:
$\mathcal{Y}(\mathcal{M}) = -4\pi\sqrt{2\,c_1^2(X_{\min})}$, where
$X_{\min}$ is the minimal model. Since homeomorphic 4-manifolds can have
minimal models of different Kodaira dimension or different $c_1^2$ — the
foundational examples are due to the Seiberg–Witten machinery LeBrun deploys —
$\mathcal{Y}$ separates smooth structures that $\chi,\tau$ cannot.

### II.2 The $L^2$ scalar-curvature infimum and the sharp Seiberg–Witten bound

The cleaner object for "how much scalar curvature must any metric carry" is
$$
\mathcal{I}_s(\mathcal{M}) = \inf_{g}\ \int_{\mathcal{M}} s_g^2\, d\mu_g,
$$
also scale-invariant in dimension 4 (Claim 1a with the integrand $s^2$ gives
$\lambda^{-4}\cdot\lambda^4 = \lambda^0$). This infimum is a smooth invariant,
and Seiberg–Witten theory makes it computable from below.

**Claim 3 (Rigorous; LeBrun 2001).** *If $\mathcal{M}$ carries a non-trivial
monopole (Seiberg–Witten basic) class $\mathfrak{a}$ with self-dual part
$\mathfrak{a}^+$, then for every Riemannian metric $g$*
$$
\int_{\mathcal{M}} s_g^2 \, d\mu_g \ \geq\ 32\pi^2 (\mathfrak{a}^+)^2,
$$
*and for a minimal complex surface of general type the bound is sharp with
$(\mathfrak{a}^+)^2 = c_1^2$, so $\mathcal{I}_s(\mathcal{M}) = 32\pi^2 c_1^2$*
[LeBrun, *Ricci curvature, minimal volumes, and Seiberg–Witten theory*,
Invent. Math. **145** (2001) 279–316; *Four-manifolds without Einstein
metrics*, Math. Res. Lett. **3** (1996) 133–147]. The right-hand side is a
**Seiberg–Witten** quantity: it changes under operations (e.g. blow-up, which
adds a $\overline{\mathbb{CP}}^2$ and shifts $c_1^2 \to c_1^2 - 1$) that can
preserve the homeomorphism type while changing the diffeomorphism type. Hence
$\mathcal{I}_s$ separates smooth structures.

### II.3 Identification of the geometric data (acceptance criterion)

The issue asks to *identify exactly which geometric data distinguishes the
actions*. The answer from Parts I–II:

- **Not** $\chi$ or $\tau$ (homeomorphism invariants — blind to smooth structure).
- **Yes** the **Seiberg–Witten basic classes** (monopole classes), equivalently
  the smooth-structure-dependent **lower envelope of the scalar-curvature
  distribution**. These control the scale-invariant scalar-curvature functionals
  $\mathcal{Y}$ and $\mathcal{I}_s$, and they are precisely the data that
  homeomorphic but non-diffeomorphic 4-manifolds differ on.

This is exactly the kind of weight the paper already gestures at in
the Level 1 section (`sec:level1`): "Donaldson and Seiberg–Witten theory provide invariants of
smooth structures that can serve as weights in $\mu^*$." Part II makes that
concrete: the SW invariants enter the *action* through the minimal
scalar-curvature functionals, not only as an abstract labeling.

---

## Part III — Where this stops: the residual gap (honest accounting)

The rigorous results of Part II are established in a setting **adjacent to, but
not identical with**, the framework's. Two mismatches, both load-bearing:

**Gap A — Riemannian vs Lorentzian.** $\mathcal{Y}$, $\mathcal{I}_s$, and the
Seiberg–Witten bounds are theorems about **Riemannian** metrics. The
co-emergence self-consistent metric $g^*_\sigma$ is **Lorentzian** (indeed the
whole point of the program is that signature is dynamical). There is no
Seiberg–Witten or Yamabe machinery for Lorentzian metrics: the SW equations use
the positive-definite Weitzenböck/Bochner structure and the ellipticity that
Riemannian signature supplies. A Wick-rotation argument is not automatic — the
self-consistent Lorentzian metric need not have a distinguished Riemannian
section, and the action's imaginary structure ($e^{iS}$, the very source of the
toy model's phases) is signature-dependent.

**Gap B — Compact vs non-compact.** LeBrun's theorems are for **compact**
4-manifolds. The framework's leading Level-0 candidate (CE-8, README Open
Problem 3) is the **non-compact** exotic $\mathbb{R}^4$, which has trivial
$H_2$ and no compact Seiberg–Witten invariants of the standard kind. Whether
exotic $\mathbb{R}^4$'s are distinguished by *any* curvature functional is, to
my knowledge, open. (The relevant smooth invariants there — e.g. Taubes'
periodic-ends / end-summable obstructions, Gompf's "radial families" — are not
phrased as scalar-curvature functionals.) So even the Riemannian half of the
argument does not yet reach the manifold class the framework most wants.

**Status of branch (1) for the actual framework.**

> **Claim 4 (Conjecture).** *For the framework's Level-0 manifold (whichever of
> the CE-8 candidates is selected), distinct smooth structures generically
> support self-consistent Lorentzian metrics with distinct Einstein–Hilbert
> actions $S_{\mathrm{EH}}[g^*_\sigma]$.*

This is a **Conjecture**, supported by: (i) the rigorous exclusion of the fatal
branch (Part I), and (ii) a strong rigorous precedent in the nearest tractable
category (Part II). It is **not** Rigorous, because of Gaps A and B. Labeling it
anything stronger would violate the rigor discipline.

---

## What this means for the toy model and the paper

1. **The toy model's non-uniform $h_{rc}$ is structurally justified, not
   merely a parameter choice — in the compact Riemannian category (Rigorous).**
   The exploration's own caveat #2 ("the external field $h$ is not derived")
   is partially discharged: a scale-fixed action *does* vary across smooth
   structures whenever Seiberg–Witten invariants do. What remains undischarged
   is the transfer to Lorentzian signature and to the non-compact candidate.

2. **No paper text should be promoted on this yet.** The honest, citable
   statement is the *negative* one (Part I, Rigorous): the EH action is not a
   topological invariant, so the framework is not forced into classical
   statistics. The *positive* transfer (Claim 4) is a Conjecture and belongs in
   the open-problems discussion, cross-referenced to CE-8, not in a headline.

3. **A genuine new prediction, correctly leveled.** *If* the framework's
   manifold is a compact 4-manifold admitting both Lorentzian metrics
   ($\chi = 0$) and varying Seiberg–Witten data, the spread of $\mu^*$ is
   controlled by the spread of the minimal scalar-curvature functional across
   $\mathrm{Sm}(\mathcal{M})$ — a quantitative, falsifiable handle. But the
   $\chi = 0$ requirement (C1 exploration) and the SW-nontriviality requirement
   are in tension (SW invariants are richest on $\chi > 0$ surfaces of general
   type), which is itself the substance of CE-8.

---

## Self-checks

- **Dimensional analysis.** $[s] = L^{-2}$, $[d\mu] = L^{4}$, so
  $[\int s\,d\mu] = L^{2}$ — consistent with the $\lambda^2$ scaling derived in
  Claim 1a. $[\int s^2 d\mu] = L^{0}$ (dimensionless), consistent with $\mathcal{I}_s$
  being scale-invariant and equal to a pure number times $c_1^2$ (Claim 3).
- **Limiting cases.** $\chi,\tau$ recovered as the only topological curvature
  integrals (standard). The linear functional $\int s\,d\mu$ correctly *fails*
  to be topological — matches the well-known fact that total scalar curvature is
  unbounded above and (without topological constraint) below on any fixed
  manifold (Kazdan–Warner-type flexibility).
- **Consistency.** Compatible with the C1 result (intersection form does not fix
  signature; $\chi = 0$ obstruction) — indeed Part III Gap B and the closing
  tension reproduce the same compact/$\chi=0$ pressure C1 found, now from the
  curvature-functional side. No contradiction with any merged result; this
  exploration introduces no postulate beyond the existing axioms (it analyzes a
  consequence, the action $h_{rc}$, already posited).
- **Order-of-magnitude / sanity.** The sharp value $\mathcal{I}_s = 32\pi^2
  c_1^2$ is an integer ($c_1^2 \in \mathbb{Z}$) times $32\pi^2 \approx 315.8$;
  blow-up shifts it by exactly one unit of $32\pi^2$ — a discrete, smooth-structure
  -indexed ladder, which is the qualitative behavior the framework needs from
  $h_{rc}$ (distinguishable, not accidentally degenerate).

## Citations (verified paper-grade, Crossref/arXiv, 2026-06-19)

- C. LeBrun, *Four-manifolds without Einstein metrics*, Mathematical Research
  Letters **3** (1996) 133–147.
- C. LeBrun, *Kodaira dimension and the Yamabe problem*, Communications in
  Analysis and Geometry **7** (1999) 133–156. (arXiv:dg-ga/9702012)
- C. LeBrun, *Ricci curvature, minimal volumes, and Seiberg–Witten theory*,
  Inventiones Mathematicae **145** (2001) 279–316. (arXiv:math/0003068,
  DOI:10.1007/s002220100148)

These enter only this exploration (`.md`), not `index.tex`; if any is later
promoted into the paper it re-enters the strict verification path. The existence
and topical match of all three were confirmed by web search on 2026-06-19. The
specific constant $32\pi^2$ and the sharp $c_1^2$ identification are from the
2001 Inventiones paper; the Kodaira-dimension sign rule is from the 1999 paper.

## Relations

- **informs #27** — discharges (in the compact Riemannian category) part of the
  toy model's caveat that $h_{rc}$ is an underived parameter choice.
- **informs CE-8 / README Open Problem 3** — the residual gap (Part III) is a
  Level-0 manifold-class question: which 4-manifold simultaneously admits
  Lorentzian metrics *and* smooth-structure-varying Seiberg–Witten data.
- **informs CE-9 / README Open Problem 4** — identifies SW basic classes (via
  $\mathcal{Y}, \mathcal{I}_s$) as candidate weights for the measure on
  $\mathrm{Sm}(\mathcal{M})$.
- **builds on** the C1 exploration (`2026-03-02-C1-signature-bridge.md`): same
  $\chi = 0$ / SW-richness tension, approached from curvature functionals.

routine: worker · model: claude-opus-4-8
