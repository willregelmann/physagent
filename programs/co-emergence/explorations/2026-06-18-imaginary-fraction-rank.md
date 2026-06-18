# Imaginary fraction of the Lorentzian fixed point: not rank, but N, spread, and alignment

**Date:** 2026-06-18
**Program:** co-emergence
**Issue:** #33 (CE-2)
**Status:** Complete — positive (exact reduction) and corrective (the "rank dependence" is a confound)
**Script:** `tests/imaginary_fraction.py`; tests `tests/test_imaginary_fraction.py`

## Summary

The mixed-dimensions exploration (2026-03-05) reported that the imaginary
fraction of the global fixed-point wavefunction `psi*` "increases with subsystem
rank," rising from `im_frac ≈ 0.26` at rank 2 to `≈ 0.34` at rank 6. Issue #33
asked for the mechanism. The answer is that **rank is not the variable.** Three
findings:

1. **Exact reduction (Rigorous).** `im_frac` is a deterministic functional of
   the Born magnitude spectrum `{p_sigma} = {|psi*_sigma|^2}` and the Lorentzian
   angle `theta` — it carries no information beyond them. The closed form
   reproduces the directly computed `im_frac` to machine precision (`~10^-16`).

2. **The "rank dependence" is a confound (Rigorous, numerical).** At fixed total
   dimension `N`, `im_frac` is independent of the subsystem rank `min(d_1, d_2)`.
   The earlier table varied rank and `N` together; the trend it attributed to
   rank is a dependence on `N`.

3. **Two alignment conventions were conflated (Rigorous).** The `~0.25` figure
   (scaling study) and the `~0.34` figure (mixed-dimensions) come from two
   *different* global-phase-alignment conventions applied to the same fixed
   points, not from two rank regimes. The paper's "`~25%` rising to `~34%`
   depending on subsystem rank" mixes both confounds and is corrected here.

The large-`N` value and the `theta`-dependence both follow analytically, and the
fixed point is shown to sit far *below* a Haar-random baseline.

## The exact reduction

At any fixed point the weight is `w_sigma = exp(gamma R_sigma)` with
`gamma = -1 + i theta` and `R_sigma` real, so

```
|psi*_sigma| = e^{-R_sigma} / Z     (phase-independent),
arg psi*_sigma = theta R_sigma = -theta log|psi*_sigma|   (mod global phase).
```

The magnitude equation closes on `|psi|^2` alone, so the Lorentzian and
Riemannian fixed points share the same magnitudes (this is why phase-stripping
exactly recovers the Riemannian state, and why the Riemannian `im_frac` is
exactly 0). Writing `p_sigma = |psi*_sigma|^2` and aligning the global phase so
that a reference component `r` is real and positive,

```
im_frac^2 = sum_sigma p_sigma sin^2( (theta/2) log(p_r / p_sigma) ).        (*)
```

This is exact (Rigorous): it is just the definition `||Im psi||^2 / ||psi||^2`
evaluated on `psi*_sigma = sqrt(p_sigma) exp(-i theta/2 · log(p_sigma/p_r))`.
It explains item-by-item why `im_frac` vanishes for `theta = 0` and why it is a
pure phase effect. Numerically (`tests/imaginary_fraction.py`, block 1):

```
dims=(2,2)        : direct=0.218452  formula=0.218452
dims=(2,5)        : direct=0.340517  formula=0.340517
dims=(6,6)        : direct=0.345267  formula=0.345267
dims=(2,2,2,2)    : direct=0.343043  formula=0.343043
--> max |direct - formula| = 1.1e-16
```

### Alignment convention enters through `p_r`

The reference `p_r` in (*) is fixed by the alignment convention:

- **Max-magnitude alignment** (`tests/mixed_dimensions.py`): `r = argmax p`, so
  `p_r = p_max`. This is the convention behind the `~0.34` numbers.
- **Optimal (minimal imaginary-norm) alignment** (the d_env scaling study): the
  global phase is the principal axis of `sum_sigma psi_sigma^2`. This gives a
  systematically smaller value and is the convention behind the `~0.25` numbers.

Reproducing the scaling study's `im_frac` table on its own configurations
(`d_sub = 16`, `d_env ∈ {4, 8, 16}`):

| dims | N | max-align | opt-align | scaling study (md) |
|------|---|-----------|-----------|--------------------|
| (16,4) | 64 | 0.367 | 0.225 | 0.234 |
| (16,8) | 128 | 0.384 | 0.244 | 0.246 |
| (16,16) | 256 | 0.390 | 0.248 | 0.250 |

The optimal-alignment column matches the scaling-study table; the
max-alignment column matches the mixed-dimensions table. They are the same
fixed points under two conventions — the `0.25` vs `0.34` gap is the
convention, not the physics.

## Rank independence at fixed N

Holding `N` fixed and varying the subsystem rank `min(d_1, d_2)` leaves
`im_frac` unchanged (max alignment, `theta = 1`, 20 seeds):

| N | dims | min-dim | im_frac |
|---|------|---------|---------|
| 16 | (2,8) | 2 | 0.335 ± 0.044 |
| 16 | (4,4) | 4 | 0.338 ± 0.042 |
| 16 | (2,2,2,2) | 2 | 0.334 ± 0.040 |
| 36 | (6,6) | 6 | 0.364 ± 0.033 |
| 36 | (4,9) | 4 | 0.364 ± 0.031 |
| 36 | (2,2,3,3) | 2 | 0.362 ± 0.030 |
| 64 | (8,8) | 8 | 0.376 ± 0.023 |
| 64 | (16,4) | 4 | 0.378 ± 0.024 |
| 64 | (2,2,2,2,2,2) | 2 | 0.382 ± 0.029 |

Ranks differing by up to a factor of 4 at fixed `N` agree to `< 0.005` —
within the seed spread. Rank has no independent effect; `im_frac` is a function
of the *global* spectrum `{p_sigma}`, and the bipartition used to define
"rank" never enters (*).

## N dependence and the large-N limit

The genuine size variable is the total dimension `N`. With `min(d) = 2` held
fixed (so rank cannot be responsible):

| N | max-align | opt-align |
|---|-----------|-----------|
| 4 | 0.224 | 0.161 |
| 8 | 0.289 | 0.196 |
| 16 | 0.334 | 0.226 |
| 32 | 0.362 | 0.235 |
| 64 | 0.382 | 0.244 |
| 128 | 0.398 | 0.250 |

A fit `im_frac(N) = a − b N^{-c}` gives `a ≈ 0.43`, `c ≈ 0.55` (max alignment).
The limit is analytic. With `R_sigma ≈ h_sigma` (the couplings `alpha, beta`
shift `R` by `O(1/N)` and are numerically negligible, as the scaling study's
parameter sweep already found) and `h ~ U[0.5, 1.5]`, the Born weights are
`p_sigma ∝ e^{-2 h_sigma}` and, for the max alignment, `p_r = p_max ↔ h_min`.
As `N → ∞`, `h_min → 0.5` and

```
im_frac^2 → E_p[ sin^2( theta (h − 0.5) ) ],   p ∝ e^{-2h} on [0.5, 1.5],
```

an `N`-independent integral. For `theta = 1` it evaluates to `im_frac → 0.399`,
matching the `N = 128` numerics. The approach is set by how fast the reference
component `h_min` reaches the floor of the `h`-support
(`E[h_min] = 0.5 + 1/(N+1)`), giving the `~N^{-c}` finite-size correction.

So the rank-2 `(2,2)` value (`≈ 0.22`) is not geometrically special: it is
simply the smallest-`N` point, where the reference component sits far from the
support floor and the weighted phase spread is small.

## theta dependence

`im_frac` is an increasing function of `theta`, zero at `theta = 0`, and linear
in `theta` for small `theta` (from `sin^2 ≈ (theta/2)^2 (·)^2`):

| theta | im_frac (dims=(4,4)) | analytic limit |
|-------|----------------------|----------------|
| 0.00 | 0.000 | 0.000 |
| 0.25 | 0.090 | 0.108 |
| 0.50 | 0.177 | 0.212 |
| 1.00 | 0.338 | 0.399 |
| 2.00 | 0.563 | 0.631 |

(The finite-`N` `(4,4)` values sit below the `N → ∞` limit, as expected.)

## Comparison with the Haar baseline

Issue #33 asked whether the fixed point approaches the Haar value (maximal phase
complexity). It does not. For a Haar-random pure state the Born weights are
`p ~ Dirichlet(1, ..., 1)`; applying (*) (max alignment, `theta = 1`):

| N | Haar im_frac | fixed point |
|---|--------------|-------------|
| 4 | 0.319 | 0.224 |
| 16 | 0.461 | 0.334 |
| 64 | 0.563 | 0.382 |
| 256 | 0.637 | ~0.39 |
| → ∞ | 0.707 (`1/√2`) | 0.399 |

The Haar value diverges in log-spread and averages `sin^2 → 1/2`, giving
`im_frac → 1/√2`. The fixed point saturates near `0.40` instead: the
self-consistency map produces the *minimal* phase structure consistent with the
moderate magnitude heterogeneity set by `h`, far below a generic random state.
This is consistent with the entropy-excess exploration's finding that the
fixed-point phases are narrowly distributed (std `~0.29` rad) and locked to the
magnitudes, rather than random.

## What this changes

For the paper (Section 3.1, `sec:toy_model`, the scaling bullet):

- Replace "`~25%` ... rising to `~34%` for higher-rank subsystems" with the
  accurate statement: `im_frac` is set by `theta`, the spread of `h`, the total
  dimension `N`, and the alignment convention — **not** by subsystem rank. State
  the exact reduction (*) and the large-`N` value (`~0.40` max-align /
  `~0.25` opt-align for `theta = 1`, `h ~ U[0.5,1.5]`).
- The qualitative physics is unchanged and in fact strengthened: the imaginary
  content is exactly the phase footprint, exactly zero for Riemannian, nonzero
  and `O(1)` for Lorentzian at every `N`, and analytically controlled.

For the README key-results table and "In plain English": adjust the
`~25–34% (rank-dependent)` line to "`~25–40%` depending on convention and size;
zero for Riemannian," removing the rank attribution.

## Open follow-ups (not part of CE-2)

- The exact reduction (*) holds for any fixed point of this family; whether an
  analogous closed form survives a continuum smooth-structure moduli space (the
  physical claim) is open and would need the Level-1 measure (CE-9). Noting here
  for the scout — this is a milestone question, not a thread proposal.
- `im_frac` is alignment-convention dependent; if a canonical convention is
  wanted for reporting, the optimal (min-imaginary-norm) one is basis-free and
  is the natural choice. This is a reporting decision, not a result.
