# Deriving the θ↔signature identification: the self-consistency weight from temporal mode structure

**Date:** 2026-06-10
**Program:** co-emergence
**Issue:** #81 (experimenter-priority)
**Status:** Complete — positive result with a precisely localized residual obstruction
**Numerics:** `../tests/derived_weight.py`, `../tests/test_derived_weight.py` (18 tests)
**Relations:** informs #88 (θ→−θ is orientation reversal), informs #32 / CE-1 (real-polarization sector is an edge case for the interference metric), informs the paper §3 framing (follow-up issue required for any text change)

---

## Summary of findings

The toy model's weight `w_σ = exp((−1+iθ)R_σ)` identifies θ≠0 with Lorentzian
signature by analogy with `e^{iS}` vs `e^{−S_E}` (paper §3). This exploration
replaces the stipulation with a construction: the weight is the amplitude of a
free scalar's temporal mode accumulated over each configuration's temporal
extent, using exactly the mode dichotomy established in the
`signature-change-boundary` fixed-background note (§5): oscillatory on the
Lorentzian side, exponentially decaying on the Euclidean side, at the same
rate constants. The note is cited, not extended; all work here lives in
`co-emergence`.

Four results, with rigor labels:

1. **(Rigorous, elementary.) Cancellation capacity is derived from signature.**
   The elliptic (Euclidean) temporal operator has a unique bounded branch,
   which is real and strictly positive — a weight built from it can never
   cancel. Every solution of the hyperbolic (Lorentzian) equation satisfies
   `φ(u + π/ω) = −φ(u)`: exact destructive cancellation between extents a
   half-period apart, for *every* polarization. Interference capacity ⟺
   hyperbolicity, with no choice involved (Lemmas 1–2).

2. **(Rigorous given the junction conditions.) Complexness is NOT derived by a
   real signature change.** Matching the Euclidean decaying branch across the
   degenerate surface Σ with the no-surface-layer junction conditions (value
   and canonical momentum continuity — the conditions the SCB note shows hold
   automatically and two-sidedly) yields the **real** oscillatory mode
   `cos ωu − sin ωu`, an equal-modulus superposition of `e^{±iωu}`. Junction
   transport is a real-linear map and cannot select a complex line (Lemma 3).
   The genuinely complex weight `e^{iωu}` requires a *complex polarization* of
   the two-dimensional oscillatory solution space — the Wick-contour /
   positive-frequency choice, which the SCB note itself flags as
   contour-dependent (its §9, point 4). The two complex choices are conjugate:
   the sign of θ is an orientation choice (informs #88).

3. **(Sketch + numerically verified.) Phase locking survives; damping does
   not.** With the complex polarization, the *pure*-Lorentzian derived weight
   is unimodular (`γ_derived = ic`, not `−1+iθ`). The fixed point has exactly
   uniform magnitudes and exact phase locking `φ_σ = c·R_σ(ψ*)`; its
   entanglement is *entirely* phase-generated (the phase-stripped state is the
   zero-entropy product state, not the Riemannian fixed point). The damping
   part of the stipulated weight (−1) corresponds precisely to **Euclidean
   admixture**: a mode accumulating decay over a Euclidean fraction ε of its
   extent and phase over the rest gives `γ = c(−ε + i(1−ε))`, and the
   stipulated family is recovered **exactly** at `ε = 1/(1+θ)`, `c = 1+θ`.
   The paper's identical-magnitude / phase-stripping correspondence is a
   property of mixed-signature configurations (ε > 0), not of the pure
   Lorentzian case.

4. **(Localized obstruction, per issue question 3.)** The configuration-space
   ↔ field-space bridge does not collapse, but it thins at three named points:
   (a) the action identification `ωτ_σ = c·R_σ`, (b) a single representative
   mode standing in for a functional integral over fields on σ, (c) the
   complex-over-real polarization choice. (a) and (b) are modeling gaps of the
   usual Sketch kind; (c) is the precise residue of the path-integral analogy
   — the *only* part of the θ↔signature identification that signature alone
   does not supply.

In plain terms: signature *does* derive the quantum/classical dichotomy in
the sense of "can the measure cancel," and it does fix the phase-locking
structure. What it does not fix is the complex form of the cancellation —
whether amplitudes interfere through U(1) phases or through real signs. That
last step is a contour/polarization choice, now stated explicitly instead of
imported silently through the `e^{iS}` analogy.

---

## 1. The construction

### 1.1 Per-configuration mode problem

Each configuration σ ∈ S is assigned a one-dimensional temporal mode problem
on a prescribed signature background, in the flat per-side coordinates of the
SCB note (§3): a free scalar mode of frequency `ω = √(m² + k²)` obeys

- Lorentzian side (coordinate u, proper time from Σ): `φ'' = −ω²φ` (hyperbolic),
- Euclidean side (coordinate v, distance from Σ): `φ'' = +ω²φ` (elliptic).

These are the SCB note's §5 mode equations in flat coordinates; the note shows
the Fuchsian analysis at the degenerate surface reduces to exactly these
elementary solution spaces (ν = 1/2 Bessel, hence trigonometric /
exponential), so nothing beyond elementary ODEs is needed here.

The signature change across Σ is configurational, not temporal (SCB note §1):
the extent below is a geometric property of σ, not a process. Each
configuration carries its own mode problem; no time parameter is shared
across configurations, and the self-consistency map remains parameter-free.

### 1.2 The bridge identification (named gap (a))

Configuration σ is assigned a temporal extent `τ_σ ≥ 0` with

```
ω τ_σ = c · R_σ(ψ),        c > 0,
```

where `R_σ(ψ)` is the toy model's mean-field curvature. Motivation: for a
static mode, the accumulated phase over extent τ is ωτ = S/ℏ, the mode's
action; and on a fixed 4-volume the Einstein–Hilbert action is proportional
to the mean curvature, so `S_σ ∝ R_σ`. **Gap (a):** this is a modeling
identification, not a derivation — the proportionality and the single scale c
are chosen, and `R_σ > 0` is required for τ_σ ≥ 0 (satisfied throughout the
toy model's parameter range). Dimensionally, ωτ is dimensionless (ℏ = 1) and
the toy model's R is dimensionless, so c is a pure number; in field-theoretic
units c carries [R]⁻¹.

A configuration may have a Euclidean fraction `ε ∈ [0,1]` of its extent
(mixed-signature configurations contain a degenerate surface; pure cases are
ε = 0, 1).

### 1.3 The derived weight

The weight is the mode amplitude accumulated over the configuration's extent,
with the mode selected by a signature-independent principle (boundedness,
plus transport across Σ where both regions are present):

```
w(σ) = φ_E(ε τ_σ) · φ_L((1−ε) τ_σ)
```

with `φ_E(v) = e^{−ωv}` the unique bounded elliptic branch (Lemma 1), and
φ_L a polarization of the hyperbolic solution space — `e^{iωu}` (complex,
Wick) or `cos ωu − sin ωu` (real, selected by the real crossing, Lemma 3).
The self-consistency map is unchanged: `F(ψ) = w(ψ)/‖w(ψ)‖₂`.

With the complex polarization this evaluates to

```
w(σ) = exp( c(−ε + i(1−ε)) · R_σ ),
```

i.e. an effective `γ_derived = c(−ε + i(1−ε))`.

---

## 2. The mode-level dichotomy

**Lemma 1 (elliptic positivity). (Rigorous.)** The solution space of
`φ'' = ω²φ` bounded on `[0,∞)` is the one-dimensional real line
`ℝ·e^{−ωv}`. Normalized to φ(0) = 1, the weight `w(v) = e^{−ωv}` is strictly
positive and monotone: for any extents v₁, v₂, `|w(v₁)+w(v₂)| = w(v₁)+w(v₂)`.
A weight built from the Euclidean bounded branch can never cancel. ∎

**Lemma 2 (hyperbolic cancellation, polarization-independent). (Rigorous.)**
On the solution space of `φ'' = −ω²φ`, translation by a half-period acts as
−1: every solution satisfies `φ(u + π/ω) = −φ(u)` for every u (immediate from
the basis {cos ωu, sin ωu}). Hence for *any* polarization — any complex line
or real line in the two-dimensional solution space — weights at extents a
half-period apart cancel exactly. ∎

These two lemmas are the derived content of the issue's question 1, and they
are stronger than the form the question anticipated in one respect:
cancellation capacity needs *no* polarization choice. Oscillation versus
positivity — the structural difference between `e^{iS}` and `e^{−S_E}` that
the paper's §3 argument actually uses — is a theorem about operator type
(hyperbolic vs elliptic), not an analogy.

The toy-model diagnostic of self-checks (§6) confirms the dichotomy
operationally: a Euclidean-derived weight produces a real positive measure
and classical correlations only; a Lorentzian-derived weight (either
polarization) produces a measure with cancellation.

## 3. What a real signature change selects (Lemma 3)

The natural candidate selection principle for the Lorentzian polarization is
the one the issue's lead suggests: transport the Euclidean boundedness
selection across the degenerate surface. The SCB note shows the field and its
canonical momentum `π = √|g| g^{00} ∂₀φ` are finite and two-sided at Σ, and
that π-continuity is the standard no-surface-layer junction condition. Apply
it (conventions: metric `ds² = λ(x⁰)(dx⁰)² + dx⃗²`; Euclidean region x⁰ < 0
with distance v from Σ, `dv/dx⁰ = −√λ`; Lorentzian region x⁰ > 0 with proper
time u from Σ, `du/dx⁰ = √(−λ)`):

- **Euclidean side**, decaying branch `φ = e^{−ωv}`:
  `∂₀φ = (−ωe^{−ωv})(−√λ) = ω√λ e^{−ωv}`, so
  `π = √λ·(1/λ)·ω√λ e^{−ωv} = ω e^{−ωv}` → at Σ: `φ = 1, π = ω`.
- **Lorentzian side**, `φ = A cos ωu + B sin ωu`:
  `π = √(−λ)·(1/λ)·√(−λ)·φ'(u) = −φ'(u)` → at Σ: `φ = A, π = −Bω`.

Matching: `A = 1`, `B = −1`:

```
φ_L(u) = cos ωu − sin ωu = (1+i)/2 · e^{iωu} + (1−i)/2 · e^{−iωu}.
```

**The two Hankel coefficients have equal modulus 1/√2: the real crossing
selects no complex line.** The transported mode is real. (Rigorous, given the
junction conditions; the sign of B is convention-dependent — orientation of u
— but reality is not.)

This is not an accident of the decaying branch. The junction transport is a
real-linear map between solution spaces of real ODEs with real matching
conditions: real Euclidean data can only produce real Lorentzian modes. The
conclusion is also robust to the junction-condition controversy in the
signature-change literature (the lineage the SCB note's "Relation to existing
work" section records; the competing momentum conditions are real constraints
and preserve reality just the same — under a `π(Σ) = 0` convention the
transported mode is `∝ cos ωu`, still real).

**Consequence.** The complex weight `e^{iωu}` — the `e^{iS}` structure — is
*not* obtained by transporting the Euclidean selection through a real
signature change. It is obtained by analytic continuation in the extent
parameter (Euclidean extent → ±i × Lorentzian extent, exactly the
complexified-geodesic reading of the SCB note's §7), and the SCB note's §9
point 4 states explicitly that continuation-versus-termination is a global
contour choice not fixed by local data at Σ. Continuing in the two directions
gives the conjugate pair `e^{∓iωu}`; so within the complex option, the only
residual freedom is the sign of θ, an orientation choice (informs #88, and
verified numerically: conjugate fixed points, equal entropies, opposite-sign
coherences).

**Status of the polarization choice.** What is derived (Rigorous): the
candidate weights form the two-real-dimensional oscillatory solution space;
cancellation holds for every member (Lemma 2); the real crossing picks a real
member; the complex members come in a conjugate pair picked by the Wick
contour. What is chosen: complex over real. This choice is exactly where the
path-integral analogy enters — but it now enters as a stated discrete choice
between identified alternatives, not as an unexamined identification.

## 4. The derived-weight toy model (complex polarization)

Implemented as `DerivedWeightModel` in `tests/derived_weight.py`, subclassing
the existing `CoEmergenceModel` and replacing only the weight function.
Numerical claims below are verified in `tests/test_derived_weight.py`
(N = 4, paper parameters α = (0.5, 0.3), β = 0.4; paper h and a seeded
generic h ~ Uniform[0.5, 1.5]).

### 4.1 The stipulated model is the mixed-signature member (exact)

```
exp((−1+iθ)R) = exp(c(−ε + i(1−ε))R)   at   ε = 1/(1+θ),  c = 1+θ.
```

Verified to machine precision at the weight level for θ ∈ {0.5, 1, 2}, and at
the fixed-point level for θ = 1 (ρ-distance < 10⁻⁸ between the derived
ε = 1/2, c = 2 model and the stipulated γ = −1+i model). **(Rigorous —
algebraic identity — plus numerics.)** Every stipulated weight with θ > 0 is
the derived weight of a configuration that spends a fraction 1/(1+θ) of its
temporal extent in the Euclidean phase. θ = 1 (the paper's default)
corresponds to equal Euclidean and Lorentzian extents.

More generally, for any ε > 0 the derived weight has the form
`m^(1-iθ_eff)` of the paper's Lemma (entropy excess) with
`m_σ = e^{−εcR_σ}` and `θ_eff = (1−ε)/ε`: the paper's phase-locking-to-
magnitudes structure holds across the whole mixed family, with the lemma's
hypotheses satisfied exactly as in the stipulated model.

### 4.2 The pure-Lorentzian case: phase locking survives, damping does not

At ε = 0 the derived weight is **unimodular**: `w = e^{icR}`, `|w| = 1`.
Consequences (analytic, verified numerically):

- Any fixed point has exactly uniform magnitudes `|ψ*_σ| = 1/√N`, so the
  marginals are uniform and `R_σ(ψ*) = h_σ + Σ_j α_j/d_j + β/N` in closed
  form; the fixed point is `ψ*_σ = N^{−1/2} e^{ic R_σ(ψ*)}` exactly, reached
  in two iterations from any start (F∘F is constant). **(Rigorous — trivial
  computation.)**
- **Phase locking survives exactly:** `φ_σ = c·R_σ(ψ*)` (numerically exact,
  10⁻¹⁰). This is the issue's question 2, answered positively — and the
  locking is now derived (phase = accumulated mode phase = c·R) rather than
  read off from the stipulated exponent.
- **Quantum signatures present:** for generic h, imaginary coherences
  `|Im ρ₀₁| ≈ 0.09` and entanglement entropy `S ≈ 0.257 nats` (vs 0.278 nats
  for the stipulated θ = 1 model — same order, consistent with the Euclidean
  admixture only re-weighting magnitudes).
- **The entanglement is entirely phase-generated:** the phase-stripped state
  has uniform magnitudes — the rank-one product state with S = 0. This is a
  *sharper* version of the paper's "the excess is entirely a phase effect":
  here not just the excess but the whole entanglement comes from phases.
- **But the phase-stripping correspondence with the Riemannian fixed point
  breaks:** stripping phases yields the uniform state, not the Boltzmann
  state (ρ-distance > 10⁻² from the ε = 1 fixed point). The identical-
  magnitude-profiles-across-signatures feature of the paper's §3 is a
  property of mixed configurations, not of the pure Lorentzian case. Any
  follow-up paper revision should state the correspondence accordingly.

(Incidental: with the paper's specific N = 4 field h = (1.0, 0.7, 0.5, 1.2),
the pure-Lorentzian reduced coherence happens to be exactly real because
h₀₀ − h₁₀ = −(h₀₁ − h₁₁); the generic-h tests avoid this measure-zero
degeneracy.)

### 4.3 The real-polarization variant: cancellation without complexness

With `φ_L = cos − sin` (Lemma 3), the weights are real and sign-indefinite.
Numerically: the fixed point exists, is real up to a global phase, has
`Im ρ ≡ 0`, and for extent scales placing c·R across a zero of cos − sin the
fixed-point weights genuinely take both signs while remaining entangled
(S ≈ 0.05–0.08 nats in the tested configurations). This is a
**real-amplitude quantum sector**: a self-consistent measure that cancels —
interference in the sense the paper's §3 argument requires — but whose
subsystem density matrices are real. (Whether real-amplitude quantum theory
is physically distinguishable from complex quantum theory is itself debated:
Renou et al., "Quantum theory based on real numbers can be experimentally
falsified," Nature **600**, 625–629 (2021) — *existence verified by web
search* — argues yes in network scenarios, but the conclusion is contested as
resting on an untestable independence assumption (e.g. arXiv:2603.19208,
2026 — **exploratory reference, existence seen in search results only,
content not verified**). Nothing here depends on either side.)

This sector is what the polarization choice of §3 is *between*: the paper's
"real measures give statistical mechanics" dichotomy refines into
positive-real (classical, derived for Euclidean) / signed-real (real-QM-like,
derived for Lorentzian + real crossing) / complex (standard QM, Lorentzian +
Wick contour). It also marks an edge case for the CE-1 interference metric
(#32): a state from this sector has `S(Re ρ) − S(ρ) = 0` while its underlying
measure is cancelling — the metric detects complex polarization specifically,
not cancellation capacity in general. (Informs #32; comment to be posted.)

## 5. Where the bridge thins (issue question 3)

The anticipated collapse point — "mode structure lives on field space over a
geometry, the weight acts on configuration space" — does not destroy the
construction, but it survives only through three named supports:

- **Gap (a) — the action identification** `ωτ_σ = c·R_σ` (§1.2). Status:
  modeling identification. A derivation would need the Einstein–Hilbert
  action of each configuration and a canonical mode frequency; in the full
  framework this is the same Level-2 input the paper already assumes when it
  takes h from the action.
- **Gap (b) — one representative mode.** The weight uses a single temporal
  mode rather than a functional integral over fields on σ. A derivation from
  the functional integral would have to show the single-mode phase structure
  survives the k-sum (plausible — the dichotomy is uniform in ω — but not
  done here).
- **Gap (c) — the polarization choice** (§3). Unlike (a) and (b), this is not
  a technical gap but a genuine two-way fork derived to be a fork: signature
  fixes cancellation, not its complex form. Within the framework, closing it
  means deriving the Wick contour from self-consistency (e.g. showing the
  real polarization fails some cross-level consistency requirement — it
  produces real-QM marginals, so if Level 3 requires complex Hilbert space
  structure for some independent reason, that would select the complex
  polarization). That is a well-posed follow-up question, not pursued here.

**Verdict on the issue's done-conditions:** outcome (a), positive, at Sketch
level overall — the complex weight ⟺ hyperbolic operator link is established
*up to* the polarization fork, with every remaining gap named; plus a worked
minimal example showing the derived-weight map reproduces the phase-locked
fixed point (exactly, in closed form, for the pure case; identically to the
stipulated model for the mixed case). The obstruction component of outcome
(b) survives in localized form as gap (c): the path-integral analogy is no
longer the identification's only support, but it remains the only support of
its *complex* (as opposed to signed-real) form.

## 6. Hidden-assumption checks and self-checks

**No smuggled time evolution.** The extent τ_σ is a geometric property of
configuration σ (a temporal *extent* in the block, like the SCB note's
configurational signature change); the mode amplitude is a property of the
static mode problem on σ. Nothing evolves; F remains a parameter-free map on
configuration-space amplitudes.

**No covert global time from the SCB x⁰.** Each configuration carries its own
mode problem and its own extent; no coordinate, foliation, or parameter is
shared across configurations. The junction analysis (Lemma 3) is internal to
a single mixed configuration's geometry.

**No background structure beyond the prescribed toy geometry.** The
construction adds two parameters (c, ε) and a polarization choice to the toy
model's existing prescribed data (h, α, β); ε and the polarization are
properties of the configuration's signature content — the very thing the
weight is now derived *from* — and c is the same kind of unit choice as the
stipulated model's normalization of R. No preferred foliation enters beyond
the one already present in the prescribed product structure (same status as
h: prescribed, acknowledged).

**No new axioms.** The construction re-derives the form of a weight the
framework already stipulated, from structures (free scalar modes on prescribed
backgrounds) already in use in the program's companion note. Three new
prescribed parameters are introduced — c (gap (a)), ε, and the
complex/real polarization choice (gap (c)) — all explicitly flagged as gaps;
none is an axiom of the framework.

**Self-checks.**
- *Dimensional analysis:* ωτ = cR dimensionless (ℏ = 1; toy-model R
  dimensionless, c a pure number; in field units c ~ [R]⁻¹). Weights
  dimensionless. ✓
- *Limiting cases:* θ → 0 forces (ε, c) → (1, 1), recovering the Riemannian
  Boltzmann weight γ = −1 continuously. ✓ Uniform R (flat / uniform h limit)
  gives equal weights → product state, no entanglement, both signatures →
  matches the toy model's uniform-field diagnostic. ✓ ε = 1 reproduces the
  existing Riemannian model exactly; ε = 1/(1+θ) the existing Lorentzian
  model exactly. ✓
- *Consistency:* No contradiction with Lemma (entropy excess) — the mixed
  family satisfies its `m^(1-iθ_eff)` hypotheses verbatim (§4.1); the pure
  Lorentzian case sits at the lemma's degenerate rank-one-magnitude boundary,
  where its comparison state has S = 0, consistent with §4.2. The SCB note is
  used strictly within its stated scope (fixed background, test field; its §9
  contour caveat is load-bearing here, not contradicted). ✓
- *Order-of-magnitude sanity:* derived pure-Lorentzian entropy 0.257 nats vs
  stipulated 0.278 nats at matched parameters; coherences ~10⁻¹–10⁻²;
  real-polarization entropies ~5–8×10⁻² nats. All O(1)-comparable, no
  anomalous scales. ✓

## 7. Follow-ups this exploration motivates (not part of this PR)

1. **Paper §3 framing change** (the issue's designated follow-up): state the
   identification as derived-up-to-polarization; replace "the weight is
   identified with signature via the path-integral analogy" with the
   Lemma 1–3 structure; restate the phase-stripping correspondence as a
   mixed-configuration property.
2. **Polarization selection from self-consistency** (gap (c)): does any
   cross-level requirement of the framework exclude the real-polarization
   (real-QM) sector? This would complete the derivation of complex quantum
   structure from signature within the framework — or, negatively, prove the
   framework cannot distinguish complex from real quantum mechanics, which
   would be a significant honest limitation.
3. **k-sum robustness** (gap (b)): single-mode → mode-sum weight.
4. **CE-1 interaction:** whether the interference metric should (or should
   not) flag the signed-real sector, and what that means for its
   interpretation as *the* quantum/classical separator.
5. **Pre-existing sign slip in merged `index.tex` `rem:entropy_application`**
   (~line 463): the remark labels the fixed-point structure as `m^{1+iθ}`,
   but `m^{1+iθ}` carries phase `−θR`; the matching member of the
   conjugation-symmetric pair is `m^{1-iθ}`. Conjugation symmetry means no
   entropy result is affected (Lemma depends on magnitudes only), but the
   label is cosmetically wrong. Reviewer-identified negative finding; filed
   as a maintenance correction issue against `main` (not `needs-human`).

## Files

- `../tests/derived_weight.py` — derived-weight model (mode functions +
  `DerivedWeightModel` subclass).
- `../tests/test_derived_weight.py` — 18 tests covering Lemmas 1–2 at mode
  level, the real-polarization reconstruction of Lemma 3, the
  derived = stipulated identity (weights and fixed points), pure-Euclidean
  and pure-Lorentzian behavior, phase locking, phase-generated entanglement,
  the broken phase-stripping correspondence, sign-indefinite real weights,
  and θ → −θ conjugation.
