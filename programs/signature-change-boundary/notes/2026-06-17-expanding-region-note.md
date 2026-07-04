# Expanding Lorentzian Region: Signature Change on a Prescribed FLRW Background
**A fixed-background consistency note (extension of the 2026-06-05 seed note to flat-slice expansion)**

---

### Status and scope

This note extends the seed note (`2026-06-05-fixed-background-note.md`, §§3–6)
from flat spatial slices to a prescribed, spatially flat, **expanding**
background

$$ds^2 = \lambda(x^0)\,(dx^0)^2 + a^2(x^0)\,\big[(dx^1)^2+(dx^2)^2+(dx^3)^2\big],$$

with $a$ a prescribed smooth function, $a(x^0)>0$ **everywhere including $\Sigma$**,
and $\lambda$ the same odd-type signature-change profile fixed by SCB-1,

$$\lambda(x^0)\simeq -c\,\mathrm{sgn}(x^0)\,|x^0|^{n},\qquad c>0,\ n>0,$$

so that $\lambda<0$ (Lorentzian) for $x^0>0$, $\lambda>0$ (Euclidean) for $x^0<0$,
and $\Sigma=\{x^0=0\}$. Both $\lambda$ **and** $a$ are prescribed: no dynamics, no
backreaction, no self-consistency machinery (binding scope guard,
`OBJECTIVES.md`; README scope note). Everything is at the test-field level on a
fixed metric, and "consistent" carries the same restricted meaning as in the
seed note — free of the divergences a degenerate metric naively produces, and
mutually compatible across the geometric, kinematic, and field-theoretic
descriptions — not "physically realized."

The seed note's central finding for flat slices was that all four descriptions
(bulk geometry, geodesics, free scalar, stress–energy) are simultaneously
benign at $\Sigma$ through one mechanism: every $g^{00}=1/\lambda$ is escorted by
$\sqrt{|g|}=\sqrt{|\lambda|}$. The single structural change here is that the
spatial volume now carries its own factor, $\sqrt{|g|}=\sqrt{|\lambda|}\,a^3$, and
the spatial metric $a^2\delta_{ij}$ is no longer constant. The headline result
of this note is that **this splits the seed note's unconditional §3 result into
two regimes**:

- the **test-field crossing structure** (§§4–6 below) is unconditionally robust
  — it needs only $a(0)>0$ — so geodesic asymmetry, Fuchsian field regularity,
  finite canonical momentum (no surface layer), and bounded stress–energy all
  survive verbatim, modified only by explicit factors of $a$;
- the **bulk geometry** (§3 below) is **no longer automatically benign**. The
  expanding bulk is FLRW-curved rather than flat, and $\Sigma$ becomes a genuine
  curvature singularity for generic smooth $a$. It remains a mere
  coordinate-degenerate boundary **only if** the scale factor approaches $\Sigma$
  with a vanishing *proper* expansion rate — a condition the flat-slice case
  satisfied identically and therefore hid.

Rigor labels (project convention) are attached per result. All "Rigorous"
labels in this note mean **Rigorous given the fixed background**, in the SCB-3
sense: every step follows on the prescribed metric, with no claim about
dynamics, backreaction, or physical realization.

---

## 1. Setup and conventions

Coordinates $x^\mu=(x^0,x^i)$, $i=1,2,3$. The nonzero metric components are
$g_{00}=\lambda(x^0)$ and $g_{ij}=a^2(x^0)\,\delta_{ij}$, so

$$\det g = \lambda\,a^{6},\qquad g^{00}=\frac1\lambda,\qquad g^{ij}=\frac{1}{a^2}\delta^{ij},\qquad \sqrt{|g|}=\sqrt{|\lambda|}\,a^{3}.$$

Write $'\equiv d/dx^0$ and define the **coordinate expansion rate**
$H\equiv a'/a$ (a smooth, bounded function near $\Sigma$ because $a$ is smooth and
$a(0)>0$). The Christoffel symbols are those of a warped product with flat
slices:

$$\Gamma^0_{00}=\frac{\lambda'}{2\lambda},\qquad
\Gamma^0_{ij}=-\frac{a a'}{\lambda}\,\delta_{ij},\qquad
\Gamma^i_{0j}=\frac{a'}{a}\,\delta^i_j=H\,\delta^i_j,$$

all others zero (the metric is spatially homogeneous with flat slices, so every
purely spatial derivative vanishes). Setting $a\equiv$ const returns
$\Gamma^0_{00}=\lambda'/2\lambda$ as the *only* nonzero symbol, recovering the
seed note's §3 connection.

The cleanest organizing device, used throughout, is the **proper variable**.
On the Lorentzian side ($x^0>0$, $\lambda<0$) set

$$u=\int_0^{x^0}\!\sqrt{-\lambda(s)}\,ds=\frac{2\sqrt c}{\,n+2\,}\,(x^0)^{(n+2)/2},$$

so $du=\sqrt{-\lambda}\,dx^0$ and the line element becomes flat-slice FLRW in
proper (cosmic) time,

$$ds^2=-\,du^2+a^2(u)\,d\vec x^2 .$$

On the Euclidean side ($x^0<0$, $\lambda>0$) the analogous distance
$v=\int_{x^0}^{0}\sqrt\lambda\,ds$ gives the Riemannian warped product
$ds^2=dv^2+a^2(v)\,d\vec x^2$. In both cases $\Sigma$ sits at proper parameter
$0$, reached from $x^0$ at the finite value above. The map $u(x^0)$ is a
diffeomorphism on the open Lorentzian region and degenerates only at $\Sigma$,
where $du/dx^0=\sqrt{-\lambda}\to0$ — exactly as in the seed note. The new
content is entirely in how $a$ behaves through this degenerate change of
variable.

---

## 2. Bulk geometry — the expanding bulk is FLRW-curved, and $\Sigma$ is a curvature singularity unless the proper expansion rate vanishes

**Claim (Rigorous, given the fixed background).** For $a$ not constant the bulk
on each side of $\Sigma$ is curved flat-slice FLRW, not flat. The curvature
invariants are finite rational functions of the **proper** expansion rate and
its proper-time derivative,

$$\mathcal H\equiv\frac{1}{a}\frac{da}{du}=\frac{a'}{a\,\sqrt{-\lambda}}\quad(\text{Lorentzian}),
\qquad \mathcal H_E\equiv\frac{a'}{a\,\sqrt{\lambda}}\quad(\text{Euclidean}),$$

and they remain bounded at $\Sigma$ **iff** these proper rates (and their proper
derivatives) stay bounded there. For generic smooth $a$ with $a'(0)\neq0$ they
diverge, so $\Sigma$ is a genuine curvature singularity. The sharp leading
condition for boundedness is

$$\boxed{\;a'(x^0)=O\!\big(|x^0|^{\,n/2}\big)\ \text{as } x^0\to0\;}$$

(equivalently $\mathcal H$ bounded), completed by the second-order requirement
that $a$ extend to a $C^2$ function of the proper variable $u$ at $u=0$.

**Derivation.** In the proper-time gauge $ds^2=-du^2+a^2(u)d\vec x^2$ the
geometry is standard spatially flat FLRW. With dots denoting $d/du$, the
nonvanishing curvature is built from $\mathcal H=\dot a/a$ alone; e.g. the Ricci
scalar and Kretschmann invariant are

$$R=6\Big(\frac{\ddot a}{a}+\frac{\dot a^2}{a^2}\Big)
=6\big(\dot{\mathcal H}+2\mathcal H^2\big),\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=12\Big(\frac{\ddot a^2}{a^2}+\frac{\dot a^4}{a^4}\Big),$$

with $R_{\mu\nu}R^{\mu\nu}$ a similar quadratic in $\ddot a/a$ and $\dot a^2/a^2$.
(These are the textbook flat-FLRW expressions; the spatial slices are flat, so
*all* curvature is the extrinsic curvature of the slicing, a function of
$\mathcal H,\dot{\mathcal H}$ only.) Thus the bulk is flat **iff** $\mathcal H\equiv0$
**iff** $a\equiv$ const — recovering §3 of the seed note as the limiting case,
and confirming that the flat-slice analysis was the measure-zero situation in
which the bulk is flat for free.

The behavior at $\Sigma$ is governed by the degenerate change of variable. With
$a'(0)=A_1$ and $\sqrt{-\lambda}=\sqrt c\,(x^0)^{n/2}$,

$$\mathcal H=\frac{a'}{a\sqrt{-\lambda}}
\;\sim\;\frac{A_1}{a(0)\sqrt c}\,(x^0)^{-n/2}\xrightarrow[x^0\to0]{}\infty
\quad(A_1\neq0),$$

so $\dot a^2/a^2=\mathcal H^2\sim(x^0)^{-n}$ and $R,\,R_{\mu\nu}R^{\mu\nu},\,
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ all diverge: **$\Sigma$ is a curvature
singularity for any $a$ with $a'(0)\neq0$.** This is the qualitative break from
the flat-slice note, where the bulk was flat and $\Sigma$ was merely a
coordinate-degenerate edge of a flat region.

Boundedness of $\mathcal H$ at $\Sigma$ requires $a'/\sqrt{-\lambda}=O(1)$, i.e.
$a'(x^0)=O(|x^0|^{n/2})$ — the boxed condition. In particular $a'(0)=0$ is
*necessary* but, for $n>2$, not sufficient: if $a'(0)=0$ then
$a'\sim a''(0)\,x^0$ and $\mathcal H\sim (x^0)^{1-n/2}$, bounded only for $n\le2$.
The clean invariant statement is therefore the second-order one:

> $\Sigma$ remains a coordinate-degenerate boundary (bounded curvature
> invariants) **iff** the scale factor, written as a function of the proper
> variable $u$, extends to a $C^2$ function at $u=0$ with $a(0)>0$ — i.e.
> $\dot a(0)$ and $\ddot a(0)$ finite. In the coordinate $x^0$ this reads
> $a'=O(|x^0|^{n/2})$ (first order, for $\mathcal H$) together with the matching
> second-order condition (for $\dot{\mathcal H}$, equivalently $\ddot a$).

The same statement holds on the Euclidean side with $\mathcal H_E=a'/(a\sqrt\lambda)$:
the singularity structure is sign-symmetric in $x^0$, so the condition is
**two-sided**, exactly as the seed note's §§3,5 results were carried through from
both sides of $\Sigma$.

**Status.** This is a clean *conditional / partial-negative* result and a fully
acceptable outcome under the issue's acceptance criteria: relative to the
flat-slice case, the §3 "bulk flat, $\Sigma$ benign" statement is **demoted to
conditional** — benign only when the proper expansion rate is regular at $\Sigma$,
and a genuine curvature singularity otherwise. Rigorous (given the fixed
background).

**Remark (consistency with the framework's only exact expanding solution).**
The issue's motivation notes that the framework's one exact self-consistent
Level-2 solution is the Starobinsky/de Sitter fixed point (an expanding
spacetime). De Sitter has $a(u)\propto e^{Hu}$ with *constant* proper
$\mathcal H=H_0$ — the regular case of the boxed condition, $\mathcal H$ bounded at
every $u$. So the obstruction found here does not conflict with the existence of
that solution; it says that an expanding Lorentzian region can adjoin $\Sigma$
without a curvature singularity precisely when its proper expansion rate stays
finite *down to $\Sigma$*, which de Sitter (away from $\Sigma$) and any profile
obeying the boxed condition do. Establishing whether a self-consistent profile
actually obeys it is the backreaction question and is out of scope here.

---

## 3. Geodesics and the crossing asymmetry — survives for $a(0)>0$ **(Rigorous, given fixed background — except continuation *as a geodesic* through $\Sigma$, which is Sketch; see below)**

**Claim (Rigorous, given the fixed background — except continuation *as a geodesic*, which is Sketch).** The crossing asymmetry of §4 of
the seed note survives intact whenever $a(0)>0$. Timelike geodesics reach $\Sigma$
at finite proper time; they have no timelike continuation into the Euclidean
region; spacelike curves cross with character intact (spacelike geodesic continuation is Sketch — see below). The scale factor adds
Hubble redshift of the peculiar momentum but changes none of these conclusions.

**Timelike geodesics reach $\Sigma$ at finite proper time.** In the proper-time
gauge the metric is independent of $x^i$, so the comoving momenta are conserved:
$a^2\dot x^i=p^i=$ const (dot $=d/d\tau$, $\tau$ proper time). The timelike
normalization $-\dot u^2+a^2|\dot{\vec x}|^2=-1$ gives

$$\frac{du}{d\tau}=\sqrt{1+\frac{|\vec p|^2}{a^2}}\ \ge 1 .$$

Because $a(0)>0$, the right-hand side is finite at $\Sigma$, and
$\Delta\tau=\int du\,\big(1+|\vec p|^2/a^2\big)^{-1/2}\le\Delta u<\infty$: the
worldline reaches $\Sigma$ ($u=0$) at finite proper time. Parametrizing instead
by $x^0$, proper time is
$\tau=\int\sqrt{-\lambda-a^2|\vec u|^2}\,dx^0$ with the (now $a$-weighted) cone
condition $|\vec u|^2<-\lambda/a^2$, $\vec u=d\vec x/dx^0$; the integrand is
bounded by $\sqrt{-\lambda}\to0$ over a finite interval, so $\tau<\infty$ — the
same convergence as the seed note, with $a(0)>0$ merely rescaling the cone. As
before, the *only* way to make $\tau$ diverge is $\lambda\to-\infty$ sufficiently
fast — a divergence of the prescribed profile, not anything forced by signature
change. (The "(curvature blow-up)" parenthetical in an earlier draft is false:
if $a\equiv$ const the geometry is flat for every $\lambda(x^0)$,
as the seed note's §4 correction records — $\tau$ can diverge without any
curvature blow-up.)

The new physical content is **Hubble redshift**: the peculiar velocity
$v_{\rm phys}^2=a^2|\dot{\vec x}|^2/\dot u^2=(|\vec p|^2/a^2)/(1+|\vec p|^2/a^2)$
carries $a^2|\dot{\vec x}|^2=|\vec p|^2/a^2$, so peculiar momentum redshifts as
$a^{-1}$ and $v_{\rm phys}\to0$ in an expanding phase — the standard FLRW
friction. This rescales velocities but does not affect whether $\Sigma$ is
reached in finite proper time.

**No timelike continuation.** In the Euclidean region $\lambda>0$ and the metric
$\lambda(dx^0)^2+a^2 d\vec x^2$ is positive-definite for any $a>0$: there is no
timelike direction at all. The normalization $\lambda(\dot x^0)^2+a^2|\dot{\vec x}|^2=-1$
has no solution. This conclusion is **independent of $a$** — it follows from
positive-definiteness alone, exactly as in the seed note.

**Spacelike curves cross intact.** For $\lambda>0$ every direction is
spacelike; the spatial metric $a^2\delta_{ij}$ is non-degenerate at $\Sigma$
because $a(0)>0$, so a spacelike curve crossing $\Sigma$ continues with its
causal character unchanged. The lone exceptional direction is the $x^0$-axis,
spacelike on the Euclidean side and timelike on the Lorentzian side: it passes
through $\Sigma$ as a point set but flips character there. The asymmetry —
**both types reach $\Sigma$; only spacelike continues as itself** — is forced by
positive-definiteness of the Euclidean region, and is untouched by the
expansion.

**Continuation *as a geodesic* through $\Sigma$ (Sketch).** The crossing statement above is about spacelike *curves*, and its $|\vec u|>0$-at-$\Sigma$ hypothesis fails for every geodesic in the expanding background. The conserved comoving momenta give $a^2\dot x^i=p^i={}$const, and the affine normalization then yields $\dot x^0=C/\sqrt{|\lambda|}$, so the coordinate spatial velocity obeys $\vec u=(\vec p/a^2)\sqrt{|\lambda|}/C\to 0$ at $\Sigma$ (since $a(0)>0$ is finite): every crossing geodesic arrives coordinate-tangent to the exceptional $x^0$-direction, exactly as in the seed note's §4. The $|\vec u|>0$ hypothesis fails, and the argument for geodesic crossing does not close. What is Rigorous: finite arc length to $\Sigma$, constant spacelike character on each open side, and the existence of spacelike-*curve* continuations through $\Sigma$. What is Sketch: that the continuation can be made *as a geodesic* through $\Sigma$, uniquely — the geodesic equation is singular at $\Sigma$ and this question is deferred to #146.

**Status.** Rigorous (given the fixed background) for: timelike geodesics reach $\Sigma$ at finite proper time; no timelike continuation exists; spacelike curves cross with character intact. Sketch: spacelike geodesic continuation through $\Sigma$. Setting $a\equiv$ const removes the redshift and reproduces the demoted §4 of the seed note verbatim.

---

## 4. Free scalar field across $\Sigma$ — Fuchsian structure survives, exact $\nu=\tfrac12$ Bessel form is special to constant $a$

Put a free scalar $\phi$ of mass $m$ on the background. With
$\sqrt{|g|}=\sqrt{|\lambda|}\,a^3$, $g^{00}=1/\lambda$, $g^{ij}=a^{-2}\delta^{ij}$,
the Klein–Gordon operator $(\Box-m^2)\phi=0$ reads

$$\frac{1}{\sqrt{|\lambda|}\,a^3}\,\partial_0\!\Big(\frac{\sqrt{|\lambda|}\,a^3}{\lambda}\,\partial_0\phi\Big)
+\frac{1}{a^2}\nabla^2\phi-m^2\phi=0 .$$

For a spatial mode $\phi=e^{i\vec k\cdot\vec x}\chi(x^0)$ on the Lorentzian side
($\lambda=-c\,x^n$, $x\equiv x^0>0$), the spatial Laplacian contributes
$-k^2/a^2$, and clearing the temporal prefactor (computed exactly as in the seed
note, now with the extra $a^3$ inside the derivative) gives

$$\boxed{\;\chi''+\Big(3H-\frac{n}{2x}\Big)\chi'+c\,x^{n}\Big(m^2+\frac{k^2}{a^2}\Big)\chi=0,\qquad H=\frac{a'}{a}.\;}$$

Against the seed note's $\chi''-\frac{n}{2x}\chi'+c(m^2+k^2)x^n\chi=0$ there are
exactly two changes, both anticipated in the issue:

1. a **Hubble friction** term $+3H\chi'$ (the factor $3$ is the three expanding
   spatial dimensions, $\partial_0\log a^3$);
2. the wavenumber is **redshifted**, $k^2\to k^2/a^2$.

**The singular point at $\Sigma$ is still Fuchsian, with the same indicial
roots (Rigorous, given the fixed background).** The coefficient of $\chi'$ is
$3H-\frac{n}{2x}$. Since $a$ is smooth with $a(0)>0$, $H=a'/a$ is **analytic**
(bounded) at $x=0$; the *only* singular part is the simple pole $-\frac{n}{2x}$,
with the same residue as in the seed note. The coefficient of $\chi$,
$c\,x^n(m^2+k^2/a^2)$, vanishes analytically at $x=0$ (again $a(0)>0$). Hence
$x=0$ is a regular singular point and the indicial equation is unchanged,

$$s(s-1)-\tfrac{n}{2}s=0\ \Longrightarrow\ s=0\ \text{ or }\ s=1+\tfrac n2 .$$

Both roots are $\ge0$, so both local solutions are bounded at $\Sigma$ with
$\chi'\to0$ — the field does not blow up. The redshift sends $k^2\to k^2/a(0)^2$
in every leading coefficient, **exactly the modification the issue predicted**;
the Hubble term $3H$ is a regular perturbation that shifts higher Frobenius
coefficients but never enters the indicial equation.

**The exact $\nu=\tfrac12$ Bessel reducibility is local-only.** In the seed note
the *entire* equation was Bessel-reducible with $\nu=\tfrac12$ exactly, giving
elementary global solutions ($\sin/\cos$ on the Lorentzian side,
$e^{-\beta x^\gamma}/\sinh$ on the Euclidean side). That is a **special feature of
constant $a$** and does **not** survive for general smooth $a$: the $3H(x^0)\chi'$
term and the $x$-dependence of $k^2/a^2$ make the coefficients non-power-law, so
the equation is no longer of Bessel type globally. What survives is precisely
the issue's "locally yes / globally no":

- **Locally (yes).** Freezing the analytic coefficients at $\Sigma$
  ($H\to H(0)$, $a\to a(0)$) returns the Bessel equation
  $\chi''-\frac{n}{2x}\chi'+c\,(m^2+k^2/a(0)^2)\,x^n\chi=0$, with the exact
  $\nu=\tfrac12$ reduction $\chi=x^\alpha Z_{1/2}(\beta x^\gamma)$,
  $\alpha=\tfrac{n+2}{4}$, $\gamma=\tfrac{n+2}{2}$,
  $\beta=\tfrac{2}{n+2}\sqrt{c\,(m^2+k^2/a(0)^2)}$. The true solution agrees with
  this $\nu=\tfrac12$ form **to leading order** near $\Sigma$ (the $3H(0)\chi'$
  correction is subleading once the regular series begins; see below).
- **Globally (no).** Away from $\Sigma$ the elementary closed forms are replaced
  by the mode functions of a scalar on flat-slice FLRW — solutions of a
  variable-coefficient ODE that admit elementary/Hankel closed forms only for
  special $a$ (e.g. power-law or de Sitter $a$). For generic prescribed $a$ the
  global solution has no elementary expression; the seed note's
  trig/exponential global mode space is therefore a constant-$a$ artifact, not a
  general feature.

**No logarithm.** Because $\nu=\tfrac12$ controls the *local* exponents and the
indicial roots $\{0,1+\tfrac n2\}$ are the same as the seed note's, the SCB-2
no-log observation carries over locally: the second solution near $\Sigma$ does
not acquire a logarithm from the leading (frozen) operator. (Whether subleading
non-Bessel terms can generate a log at higher order for resonant integer
$1+\tfrac n2$ is a presentation question for the eventual §5/SCB-2 port, not a
boundedness question — both exponents are $\ge0$ regardless.)

**Status.** Rigorous (given the fixed background) for: the boxed temporal
equation, the Fuchsian classification, the indicial roots $\{0,1+\tfrac n2\}$,
boundedness of both modes, and the $k^2\to k^2/a(0)^2$ redshift. The downgrade of
the *global* elementary $\nu=\tfrac12$ closed form to a *local* statement is an
explicit, honest demotion relative to the flat-slice note, with the obstruction
named (non-power-law coefficients from $3H$ and $k^2/a^2$). Setting $a\equiv$
const removes $3H$ and the redshift and returns the seed note's global Bessel
solution exactly.

---

## 5. Canonical momentum and stress–energy — no surface layer, bounded invariants, for all smooth $a>0$

**No-surface-layer / matching condition (Rigorous, given the fixed background).**
The canonical momentum conjugate to $\phi$ is

$$\pi=\sqrt{|g|}\,g^{00}\,\partial_0\phi=\sqrt{|\lambda|}\,a^3\cdot\frac1\lambda\,\chi'
=-\frac{a^3}{\sqrt c}\,x^{-n/2}\,\chi'\quad(\text{Lorentzian}).$$

The two Frobenius branches give, near $\Sigma$:

- $s=1+\tfrac n2$ branch: $\chi\sim x^{1+n/2}$, $\chi'\sim x^{n/2}$, so
  $\pi\sim x^{-n/2}\,a^3\,x^{n/2}\to a(0)^3\times(\text{finite const})$;
- $s=0$ branch: the regular series is
  $\chi=1+a_{n+2}\,x^{n+2}+\cdots$ with $a_1=a_2=\cdots=a_{n+1}=0$
  (the simple-pole friction term forces $a_1=0$, and the analytic $3H$ piece —
  whose contribution $3H\chi'$ is then itself higher order — never reintroduces
  a low-order coefficient; the first source is the $c\,x^n\chi$ term at order
  $x^n$). Hence $\chi'=O(x^{n+1})$ and $\pi\sim x^{-n/2}\,a^3\,x^{n+1}=O(x^{n/2+1})\to0$.

In both cases $\pi$ approaches a **finite constant** (times $a(0)^3$) at $\Sigma$:
the no-surface-layer condition holds automatically, **for every smooth $a>0$,
with no condition on $a'(0)$** — in pointed contrast to the curvature condition
of §2. The reason is that the Hubble friction $3H$ is *regular*, so it perturbs
the Fuchsian momentum balance only at subleading order; the leading
$x^{-n/2}\!\cdot x^{n/2}$ escort of the seed note's §5 is untouched. The Euclidean
side is identical with $\partial_0=-d/dx$ and the modified-Bessel branches; $\pi$
is finite from both sides, so the matching is two-sided.

**Stress–energy is bounded (Rigorous, given the fixed background).** With
$X\equiv g^{\alpha\beta}\partial_\alpha\phi\,\partial_\beta\phi$ and the regular
solutions ($\chi'=O(x^{n/2})$ at worst),

$$X=g^{00}(\partial_0\phi)^2+g^{ij}\partial_i\phi\,\partial_j\phi
\sim x^{-n}\cdot x^{n}+\frac{k^2}{a^2}\chi^2=O(1),$$

the spatial term finite because $a(0)>0$. The curvature-sourcing invariant is a
function of $X,V$ alone,

$$T_{\mu\nu}T^{\mu\nu}=X^2+2VX+4V^2=O(1),$$

so it is bounded at $\Sigma$, on both sides (the Euclidean kinetic term is
non-negative, $g^{00}=+x^{-n}/c$, and again $X=O(1)$). The seed note's two
caveats persist verbatim: individual *raised* components still diverge —
$T^{00}=(g^{00})^2T_{00}\sim x^{-n}$, and now also $a$-weighted spatial
components — even though the scalar contractions stay finite; and this is a test
field on a fixed background, showing the benign geometry is *compatible* with
finite test stress–energy, not that the coupled system has a benign solution.

**An honest tension worth flagging (not a contradiction).** The *test-field*
stress–energy is bounded at $\Sigma$ for all smooth $a>0$, yet by §2 the
*background's own* Einstein tensor diverges there whenever $a'(0)\neq0$. These
do not conflict — the first is a probe field, the second is the prescribed
geometry — but they make precise where a future self-consistency layer would
have to do work: closing the loop ($\phi$ sourcing $g$) would demand a matter
sector able to support the divergent curvature of §2, which the bounded
test-field $T_{\mu\nu}$ here does *not* by itself supply. This is the
backreaction question (seed note §9.2), explicitly out of scope.

**Status.** Rigorous (given the fixed background); identical conclusions to the
seed note's §§5–6 for the canonical momentum and stress–energy, now carrying
explicit $a$ factors and requiring only $a(0)>0$. Setting $a\equiv$ const
reproduces §§5–6 exactly.

---

## 6. Summary and the one mechanism, revisited

On flat slices the seed note's §8 read all four benign facts as one escorting:
every $g^{00}=1/\lambda$ paired with $\sqrt{|g|}=\sqrt{|\lambda|}$. The expansion
adds a spatial volume factor $a^3$ and a non-constant spatial metric $a^2$, and
the result is a clean split:

| Description | Flat slices ($a\equiv$ const) | Prescribed expanding $a(x^0)>0$ |
|---|---|---|
| **Bulk geometry** (§2) | flat; $\Sigma$ a coordinate-degenerate boundary, **unconditionally** | FLRW-curved; $\Sigma$ a **curvature singularity unless** $\mathcal H=a'/(a\sqrt{|\lambda|})$ stays bounded, i.e. $a'=O(|x^0|^{n/2})$ + $C^2$-in-$u$ |
| **Geodesic asymmetry** (§3) | timelike reach $\Sigma$/no continuation; spacelike curves cross intact (spacelike geodesic continuation: Sketch) | **survives** for $a(0)>0$; adds Hubble redshift of peculiar momentum |
| **Scalar field** (§4) | Fuchsian, roots $\{0,1+\tfrac n2\}$; exact $\nu=\tfrac12$ Bessel **globally** | Fuchsian, **same roots**, $k^2\to k^2/a(0)^2$; exact $\nu=\tfrac12$ form **local-only** (global elementary closed form lost) |
| **Momentum / stress–energy** (§5) | $\pi\to$ const (no surface layer); $T_{\mu\nu}T^{\mu\nu}=O(1)$ | **survives** for all smooth $a>0$; $\pi\to a(0)^3\times$ const; invariants $O(1)$ |

The escorting mechanism still operates for the test field: $\sqrt{|g|}\,g^{00}\sim
a^3\,x^{-n/2}$ clears the temporal operator to a Fuchsian point, the field
equation forces $\chi'\sim x^{n/2}$ to compensate $g^{00}\sim x^{-n}$, and the
momentum and stress–energy stay finite — the $a^3$ rides along as a bounded
escort because $a(0)>0$. What the escort cannot fix is the **bulk curvature**:
the seed note's §3 "flat on each side" was the one place the conclusion did not
come from the $1/\lambda$–$\sqrt{|\lambda|}$ pairing but from the slices being
flat *and unwarped*. Warping the slices ($a$ non-constant) reintroduces genuine
curvature, and the degenerate change of variable to proper time amplifies it
into a singularity at $\Sigma$ unless the proper expansion rate is regular there.

**The headline.** Adjoining an *expanding* Lorentzian region to a
signature-change boundary is kinematically and field-theoretically as benign as
the static case (§§3–5), but it is **geometrically benign only conditionally**
(§2): the boundary stays non-singular precisely when the scale factor reaches
$\Sigma$ with a finite proper expansion rate. The flat-slice seed note satisfied
this for free ($\mathcal H\equiv0$) and so could not see the condition; it is the
characteristic new feature of the expanding extension.

---

## 7. What this does not claim

All seed-note disclaimers (§9 there) carry over unchanged, plus two specific to
this note:

1. **No dynamics or backreaction.** Both $\lambda$ and $a$ are prescribed. The
   curvature singularity of §2 (when $a'(0)\neq0$) is a statement about a
   *prescribed* geometry; whether a self-consistent profile avoids it (by
   obeying the boxed regularity condition) is the backreaction question and is
   out of scope (binding SCB scope guard).
2. **The §2 condition is a fixed-background curvature statement, not a
   selection principle.** That de Sitter (constant proper $\mathcal H$) sits in
   the regular class is suggestive but is not a claim that the framework
   *selects* such profiles. No empirical prediction is made.
3. **A single, special family.** Flat spatial slices; $\lambda$ and $a$ functions
   of $x^0$ only. Spatially structured slices, spatial dependence in $a$, and
   anisotropy remain uncovered (as in the seed note's §9.5).

## Relation to existing work

The flat-slice lineage of the seed note (Ellis and collaborators; the
*competing* junction conditions of Dray–Manogue–Tucker — momentum continuity —
and Hayward — momentum vanishing, the two sides of a published dispute; see
the seed note's corrected Relation-to-existing-work section; Kossowski–Kriele
degenerate geodesics) applies here as well; these references were
**paper-grade verified** under SCB-4 (#135), with the Hayward attribution
corrected in the July 2026 red-team audit, and are recorded as formal entries
in the seed note's References section. The
expanding case additionally touches **signature-change cosmology** and the
**no-boundary** literature (Halliwell–Hartle-type integration-contour analyses
for an expanding no-boundary region are the natural comparison for the §2
condition and the §4 evanescent-tail/contour ambiguity inherited from the seed
note's §7,§9.4). **These references are exploratory and unverified here and are
deliberately not committed as paper-grade citations**; SCB-4 is the milestone
that will verify or replace the exploratory list before any port to `index.tex`.
What this note isolates is structural and self-contained: the split between an
unconditionally benign test-field crossing and a *conditionally* benign bulk
geometry, with the sharp regularity condition on the proper expansion rate.
