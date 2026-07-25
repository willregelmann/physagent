# Interference Metric: Separating Quantum Phase Coherence from Classical Redistribution

**Date:** 2026-06-10
**Program:** co-emergence
**Issue:** #32 (milestone CE-1)
**Status:** Complete — positive result, metric defined and validated
**Code:** `tests/interference_metric.py`, `tests/test_interference_metric.py`

## Motivation

The co-emergence thesis turns on a clean dividing line: Lorentzian
self-consistency produces *quantum* interference, Riemannian self-consistency
produces only *classical* statistics. The paper needs a diagnostic that
realizes this line at the density-matrix level.

The diagnostic used in the early N=8/16 toy-model tests compared the
rotated-basis populations of the reduced density matrix `rho` to those of
`diag(rho)`, flagging "destructive interference" when
`p_quantum(k) < p_incoherent(k)` for some outcome `k` in some basis. The
mixed-dimensions exploration (`2026-03-05-mixed-dimensions.md`, §"Interference
metric: needs refinement") found this fires for **both** signatures:

> Both Lorentzian and Riemannian states show "destructive interference" ...
> This occurs because the definition compares full ρ to diag(ρ) — and even
> purely real off-diagonal elements (classical correlations from tracing a pure
> state) redistribute probabilities across rotated bases.

The N=8 test code had already noted the same thing in a comment (lines 212–219
of `test_toy_model_n8.py`): "Actually real off-diagonal elements CAN produce
interference." The open question (mixed-dimensions §"Open questions" #3) was to
find

> a definition that cleanly separates quantum interference (from complex
> phases) from classical probability redistribution (from real correlations).

This exploration supplies one.

## The metric

For a density matrix `rho` (Hermitian, PSD, unit trace), define the
**entrywise real part**

```
Re rho := (rho + conj(rho)) / 2,
```

where `conj` is complex conjugation of each entry. For Hermitian `rho` this is
the **time-reversal-symmetrized state**. The interference metric is the
von Neumann entropy gap

```
I_S(rho) := S(Re rho) - S(rho),       S(X) = -Tr(X log X).
```

A companion non-entropic witness is the Hilbert–Schmidt norm of the imaginary
part, `I_HS(rho) := ||Im rho||_F`.

### Why `Re rho` is the right reference object

Time reversal acts on a density matrix by complex conjugation in a real basis,
`T: rho -> conj(rho)`. The fixed points of `T` are exactly the real states.
`Re rho = (rho + T rho)/2` is the closest `T`-invariant state to `rho` — the
state with all time-reversal-odd (probability-current) content removed. The
imaginary part `Im rho` is precisely the part of the state that sources a
probability current and produces interference fringes; a real density matrix
has none. So `I_S` measures *how much of the state's structure is
interference-capable* relative to its classical (real, `T`-invariant)
shadow. This is the same logic as the relative entropy of coherence in resource
theory, with the incoherent set "diagonal states" replaced by the larger set
"real states" — which is exactly what removes the classical-redistribution
false positive.

## Properties (Rigorous)

Throughout, `rho` is Hermitian PSD with `Tr rho = 1`, and `conj(rho) = rho^T`
because `rho` is Hermitian.

**Proposition 1 (Re rho is a valid density matrix). (Rigorous.)**
`Re rho` is real, symmetric, PSD, and unit-trace.
*Proof.* Real and symmetric: `(Re rho)_{jk} = Re(rho_{jk})` and, by
hermiticity, `Re(rho_{jk}) = Re(conj(rho_{kj})) = Re(rho_{kj})`. Unit trace:
the diagonal of a Hermitian matrix is real, so `(Re rho)_{jj} = rho_{jj}` and
`Tr Re rho = Tr rho = 1`. PSD: `conj(rho) = rho^T` is PSD (same spectrum as
`rho`), and `Re rho = (rho + rho^T)/2` is the average of two PSD matrices,
hence PSD. ∎

**Proposition 2 (`rho` and `conj(rho)` are isospectral). (Rigorous.)**
`conj(rho) = rho^T` has the same eigenvalues as `rho`, so
`S(conj(rho)) = S(rho)`. ∎

**Theorem 3 (Nonnegativity and faithfulness). (Rigorous.)**
`I_S(rho) >= 0`, with equality iff `Im rho = 0`.
*Proof.* By concavity of the von Neumann entropy and Proposition 2,
```
S(Re rho) = S( (rho + conj(rho))/2 )
          >= (1/2) S(rho) + (1/2) S(conj(rho))
          = S(rho),
```
so `I_S(rho) >= 0`. For the equality case, use the relative-entropy identity
(Theorem 4): `I_S(rho) = S(rho || Re rho)`, and the von Neumann relative entropy
vanishes iff its arguments coincide, i.e. `rho = Re rho`, i.e. `Im rho = 0`.
Conversely if `Im rho = 0` then `Re rho = rho` and `I_S = 0`. ∎

**Theorem 4 (Relative-entropy identity). (Rigorous.)**
`I_S(rho) = S(rho || Re rho)`, where `S(a||b) = Tr a(log a - log b)` is the
von Neumann relative entropy. The support condition `supp(rho) ⊆ supp(Re rho)`
holds for **every** density matrix: if `(rho + rho^T)x = 0` then
`x*(rho + rho^T)x = x*rho x + x*rho^T x = 0`, and both summands are nonnegative
(`rho` by hypothesis, `rho^T` because it is isospectral to `rho` and hence also
positive semidefinite), so each vanishes separately; in particular
`x*rho x = 0`, forcing `rho x = 0`. So `null(Re rho) ⊆ null(rho)` universally,
and the relative entropy is finite for all density matrices.

> **Correction, 2026-07-24.** This step previously read
> `x*(rho + rho^T)x = 2 Re(x*rho x)`, which is **false** for Hermitian non-real
> `rho`: with `rho = [[1, i], [-i, 1]]` (Hermitian, PSD, eigenvalues 0 and 2)
> and `x = (1, i)`, the left side is 4 and the right side is 0. The identity
> holds for *real* `x`, which is almost certainly the argument intended before
> the quantifier was generalised to complex `x` without rechecking. The
> conclusion is unaffected — the repair above uses only the positive
> semidefiniteness of `rho^T` already established alongside it. Found by the
> 2026-07-24 independent audit; the same step had propagated from here into
> `index.tex`, and both are now fixed.
*Proof.* Write `rho = Re rho + i Im rho`. The real matrix `Im rho` is
antisymmetric (`Im(rho_{jk}) = Im(conj(rho_{kj})) = -Im(rho_{kj})`), while
`B := log(Re rho)` is real symmetric. For any real antisymmetric `A` and real
symmetric `B`, `Tr(AB) = Tr((AB)^T) = Tr(B^T A^T) = -Tr(BA) = -Tr(AB)`, so
`Tr(AB) = 0`. Hence
```
Tr(rho log Re rho) = Tr(Re rho · B) + i Tr(Im rho · B)
                   = Tr(Re rho · log Re rho) + 0
                   = -S(Re rho).
```
Therefore `S(rho || Re rho) = Tr(rho log rho) - Tr(rho log Re rho)
= -S(rho) + S(Re rho) = I_S(rho)`. ∎

So `I_S` is not merely a heuristic gap: it is the genuine quantum relative
entropy (distinguishability) between the state and its closest real shadow —
a faithful, information-theoretic measure of imaginary coherence.

**Numerical confirmation.** The identity holds to `~1e-16` over random states
(`test_relative_entropy_identity`); nonnegativity holds with no violations over
200 random states (`test_nonnegative_random`); `Re rho` is a valid density
matrix in every trial (`test_real_part_is_valid_density_matrix`).

## Size-robust global version

The reduced-state `I_S(rho_R)` inherits the partial-trace averaging the paper
already documents (§"Phase structure of the fixed point"): for a fixed small
subsystem of a growing pure state, the imaginary off-diagonals are suppressed
by phase cancellation across environment configurations, so `I_S(rho_R)`
*decreases and fluctuates* as `d_env` grows — it measures the **visible**
interference in that subsystem, which is genuinely small for a large bath.

For a **size-robust** signature, apply the same construction to the global pure
state `rho_g = |psi*><psi*|`:

```
I_S^global := S(Re rho_g).
```

(The second term `S(rho_g) = 0` because the global state is pure.) Writing the
global-phase-aligned, normalized state as `psi* = a + i b` with `a, b` real,

```
Re rho_g = a a^T + b b^T,
```

which has rank ≤ 2. Its nonzero spectrum equals that of the 2×2
**real–imaginary Gram matrix**

```
G = [[ a·a, a·b ],
     [ a·b, b·b ]],     trace G = |a|^2 + |b|^2 = 1,
```

so

**Proposition 5 (Closed form). (Rigorous.)**
`I_S^global = -λ_+ log λ_+ - λ_- log λ_-`, where `λ_±` are the eigenvalues of
`G`. In particular `I_S^global = 0` iff `b ∥ a` after phase alignment, i.e. iff
`psi*` is real up to a global phase. *(Proof: direct;
`a a^T + b b^T = [a b] G' [a b]^T`-type reduction gives nonzero spectrum equal
to that of the Gram matrix `G`. Verified to `~1e-16` in
`test_closed_form_matches_random`.)*

This is the entropic refinement of the paper's "imaginary fraction" diagnostic:
where im_frac reports `|b|^2`, `I_S^global` reports the full entropy of the
`(a, b)` Gram spectrum, which also accounts for the overlap `a·b`.

## Numerical validation

All on toy-model fixed points; `theta = 1`, `h ~ U[0.5,1.5]`, seeds as in
`conftest.py`. Full assertions in `test_interference_metric.py` (16 tests, all
passing; full suite 75/75).

| Quantity | Riemannian (θ=0) | Lorentzian (θ=1) |
|---|---|---|
| `I_S(rho_R)`, N=4 | `0.0` (≤1e-12) | `7.6e-4` |
| `I_S(rho_R)`, N=8, all 6 subsystems | `0.0` (≤1e-12) | `> 1e-8` |
| `I_S(rho_R)`, N=16 | `0.0` (≤1e-12) | `> 1e-8` |
| `I_S^global`, N=4..128 | `0.0` (≤1e-12) | `0.075 – 0.24`, no decay |

**θ-scaling (N=8, one subsystem):** monotone in θ and quadratic at small θ
(`I_S ∝ θ²`), mirroring the entropy excess `S(θ)/S(0) ≈ 1 + cθ²`:

| θ | 0.00 | 0.25 | 0.50 | 1.00 | 2.00 |
|---|---|---|---|---|---|
| `I_S(rho_R)` | 0 | 1.57e-3 | 5.91e-3 | 1.93e-2 | 4.35e-2 |

The ratio `I_S(0.5)/I_S(0.25) ≈ 3.76 ≈ 4`, consistent with `θ²` plus subleading
corrections (`test_quadratic_at_small_theta`). `I_HS = ||Im rho||_F` scales
linearly in θ at small θ, as expected for a first-moment witness.

**Size-dependence of the reduced metric.** `I_S(rho_R)` for a fixed one-qubit
subsystem of an N=4..64 chain fluctuates and trends downward with `d_env`
(values from `1e-2` down to `~1e-6` in places), reproducing the documented
`~d_env^{-0.6}` partial-trace averaging. This is the expected behavior, not a
defect: it is exactly why the size-robust diagnostic is `I_S^global` (or the
eigenvalue-level entropy excess), as the paper already argues.

## Self-checks

- **Dimensional analysis.** Entropies and relative entropies are dimensionless
  (nats); `I_S` and `I_S^global` are dimensionless. `I_HS = ||Im rho||_F` is
  dimensionless (density-matrix entries are dimensionless). Consistent.
- **Limiting cases.** θ→0 (Riemannian): `Im rho → 0`, `I_S → 0` identically, at
  every system size and for every subsystem — the exact-zero baseline the old
  metric lacked. Pure real state: `I_S = 0`. Maximal case bounded by
  `S(Re rho) ≤ log d`.
- **Consistency.** `I_S` agrees with the existing robust diagnostics: zero
  exactly where the Riemannian fixed point is real, positive exactly where the
  Lorentzian fixed point carries phases, and its global version tracks the
  imaginary-fraction / entropy-excess story (both phase effects, both stable in
  size). It contradicts none of the paper's results; it *replaces* the
  retracted `p_quantum<p_incoherent` heuristic, whose failure the
  mixed-dimensions exploration recorded.
- **Order-of-magnitude.** At θ=1, `h~U[0.5,1.5]`, `I_S^global ≈ 0.1–0.2` nats,
  the right order for a state with `O(10%)` of its norm in the imaginary part:
  the Gram matrix `G ≈ diag(0.9, 0.1)` has entropy `≈ 0.33` nats, and overlap
  `a·b` reduces it, landing in the observed band.

## Limitations and honest gaps

- **Basis dependence (by design).** "Real part" is defined relative to the
  smooth-structure (computation) basis, in which the Riemannian fixed point is
  real and time reversal is conjugation. This is physically appropriate —
  interference is always relative to a measurement frame — but it means `I_S` is
  not invariant under arbitrary complex unitaries (it *is* invariant under real
  orthogonal changes of basis, which commute with `T`). The metric answers
  "interference relative to the classical/Riemannian frame," which is the
  question the thesis poses. **(Stated, not a defect.)**
- **Support condition (resolved, not a limitation).** Theorem 4 requires
  `supp(rho) ⊆ supp(Re rho)`, but this holds for every density matrix by the
  null-space argument in the proof (see above). The relative-entropy form is
  unconditionally finite; the code's explicit support check is conservative
  but can never fire on a valid density matrix.
- **Not a full resource monotone (Conjecture).** I expect `I_S` to be
  monotone under the free operations of the resource theory of imaginarity
  (real channels), by analogy with the relative entropy of coherence, but I do
  **not** prove monotonicity here and make no such claim. Only the four
  properties above (Propositions 1, 5; Theorems 3, 4) are Rigorous.

## Implications for the paper

1. **Replace the retracted heuristic.** Section 3 should state the metric
   `I_S = S(Re rho) - S(rho)` as the interference diagnostic, with its
   exact-zero-on-Riemannian / positive-on-Lorentzian property (Rigorous), and
   drop any residual reliance on the `p_quantum<p_incoherent` comparison.
2. **Cleaner claim.** The sentence "imaginary coherences absent for Riemannian,
   present for Lorentzian" is now backed by a *faithful* measure that is
   identically zero on real states, not a thresholded population comparison.
3. **Ties the diagnostics together.** `I_S^global` is the entropic version of
   the imaginary fraction and shares its size-robustness; the reduced-state
   `I_S` is the entropic version of the (size-suppressed) reduced imaginary
   coherence. Same construction, two scales.

No new paper-grade citations are introduced. The resource-theory-of-imaginarity
and relative-entropy-of-coherence analogies above are exploratory framing only;
they are not committed to `index.tex` and would require strict verification
before any citation.

## Suggested follow-ups (not done here)

- Prove or refute the resource-monotonicity conjecture (would justify calling
  `I_S` *the* interference measure rather than *a* witness). Candidate new
  issue.
- A short companion to CE-2: does `I_S^global`'s closed form (Gram spectrum)
  explain the rank-dependence of the imaginary fraction?
