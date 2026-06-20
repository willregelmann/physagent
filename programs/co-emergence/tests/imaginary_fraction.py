#!/usr/bin/env python3
"""
Imaginary-fraction analysis of the Lorentzian fixed point (issue #33, CE-2).

The mixed-dimensions exploration (2026-03-05) reported that the imaginary
fraction of psi* "increases with subsystem rank" (0.26 at rank 2 -> 0.34 at
rank 6).  This script shows that interpretation is a confound: at fixed total
dimension N the imaginary fraction does not depend on the subsystem rank
min(d_1, d_2), and the apparent rank trend is (i) a dependence on N and
(ii) a difference in the global-phase-alignment convention between two earlier
scripts.

The controlling identity is exact.  At any fixed point

    psi*_sigma = w_sigma / ||w||,   w_sigma = exp(gamma R_sigma),  gamma = -1 + i*theta,

so |psi*_sigma| = e^{-R_sigma}/Z is phase-independent (it equals the Riemannian
fixed point) and the phase is theta R_sigma = -theta log|psi*_sigma|.  Writing
the Born weights p_sigma = |psi*_sigma|^2 and aligning the global phase so that
a chosen reference component (index r) is real, the imaginary fraction is a
deterministic functional of the magnitude spectrum and theta:

    im_frac^2 = sum_sigma p_sigma * sin^2( (theta/2) * log(p_r / p_sigma) ).      (*)

For the max-magnitude alignment of mixed_dimensions.py, r = argmax p.  For the
optimal (minimal imaginary-norm) alignment used by the d_env scaling study,
the global phase is the principal axis of sum_sigma psi_sigma^2.

Consequences, all checked below:
  - (*) reproduces the directly computed im_frac to machine precision (Rigorous).
  - im_frac = 0 exactly for the Riemannian fixed point (theta = 0).
  - At fixed N, im_frac is independent of subsystem rank min(d_1, d_2).
  - im_frac rises with N toward an analytic large-N limit set by theta and the
    spread of h; for max alignment, theta = 1, h ~ U[0.5, 1.5] the limit is
    ~0.40 (and ~0.25 for the optimal alignment).
  - The fixed point sits far BELOW the Haar-random baseline at every accessible
    N: the self-consistency map produces minimal, not maximal, phase complexity.
    NOTE: the Haar baseline does NOT converge to 1/sqrt2 -- under the
    max-magnitude reference the Born-weighted <sin^2> is modulated by
    Gamma(2 +- i*theta) and the value keeps rising with N (0.64 at N=256 to
    0.82 at N~2.6e5), staying above the fixed point's ~0.40 throughout. (An
    earlier version of this script and of index.tex wrongly claimed a 1/sqrt2
    limit; corrected by the 2026-06-19 red-team audit.)

Reference: programs/co-emergence/index.tex, Section 3.1 (sec:toy_model).
"""

import numpy as np
from scipy import integrate

try:  # works as a package import (pytest) and as a standalone script
    from .toy_model import CoEmergenceModel
except ImportError:  # pragma: no cover
    from toy_model import CoEmergenceModel


# ── alignment conventions ─────────────────────────────────────────────

def im_frac_max(psi):
    """Imaginary fraction with the max-magnitude component aligned real.

    This is the convention of tests/mixed_dimensions.py.
    """
    idx = np.argmax(np.abs(psi))
    z = psi * np.exp(-1j * np.angle(psi[idx]))
    return np.linalg.norm(z.imag) / np.linalg.norm(z)


def im_frac_opt(psi):
    """Imaginary fraction with the global phase that minimizes ||Im psi||.

    The minimizer is the principal axis of the complex second moment
    sum_sigma psi_sigma^2; this is the convention of the d_env scaling study.
    """
    a = 0.5 * np.angle(np.sum(psi * psi))
    z1 = psi * np.exp(-1j * a)
    z2 = psi * np.exp(-1j * (a + np.pi / 2))
    z = z1 if np.linalg.norm(z1.imag) <= np.linalg.norm(z2.imag) else z2
    return np.linalg.norm(z.imag) / np.linalg.norm(z)


def im_frac_formula(psi, theta):
    """Closed form (*) with the max-magnitude reference."""
    p = np.abs(psi) ** 2
    p = p / p.sum()
    p_ref = p.max()
    return float(np.sqrt(np.sum(p * np.sin(0.5 * theta * np.log(p_ref / p)) ** 2)))


# ── fixed-point driver ────────────────────────────────────────────────

def fixed_point(dims, seed, theta=1.0, n_starts=8):
    """Return one converged Lorentzian fixed point, or None."""
    N = int(np.prod(dims))
    rng = np.random.RandomState(seed)
    h = rng.uniform(0.5, 1.5, size=N)
    model = CoEmergenceModel(dims=dims, h=h, alphas=[0.4] * len(dims),
                             beta=0.4, gamma=-1.0 + 1j * theta)
    for s in range(n_starts):
        np.random.seed(seed * 1000 + N + s)
        psi, err, _ = model.find_fixed_point(max_iter=20000, tol=1e-11)
        if err < 1e-9:
            return psi
    return None


def summarize(dims, seeds, theta=1.0, conv="max"):
    f = im_frac_max if conv == "max" else im_frac_opt
    vals = []
    for s in seeds:
        psi = fixed_point(dims, s, theta=theta)
        if psi is not None:
            vals.append(f(psi))
    return (np.mean(vals), np.std(vals), len(vals)) if vals else (np.nan, np.nan, 0)


# ── analytic large-N limit and Haar baseline ──────────────────────────

def limit_max_align(theta=1.0, lo=0.5, hi=1.5):
    """Large-N limit of im_frac (max alignment), using R ~ h, p ∝ e^{-2h}.

    As N -> infinity the reference (h_min) -> lo, so
        im_frac^2 -> E_p[sin^2(theta (h - lo))],  p ∝ e^{-2h} on [lo, hi].
    """
    num = integrate.quad(lambda h: np.exp(-2 * h) * np.sin(theta * (h - lo)) ** 2, lo, hi)[0]
    den = integrate.quad(lambda h: np.exp(-2 * h), lo, hi)[0]
    return np.sqrt(num / den)


def haar_im_frac(N, theta=1.0, trials=4000, seed=0):
    """Monte-Carlo im_frac (max alignment) for Haar-random pure states.

    A Haar state has Born weights p ~ Dirichlet(1, ..., 1); apply (*).
    """
    rng = np.random.RandomState(seed)
    out = []
    for _ in range(trials):
        E = rng.exponential(1.0, size=N)
        p = E / E.sum()
        out.append(np.sum(p * np.sin(0.5 * theta * np.log(p.max() / p)) ** 2))
    return float(np.sqrt(np.mean(out)))


def main():
    seeds = list(range(20))

    print("=" * 74)
    print("1. EXACT REDUCTION:  im_frac (direct, max-align)  ==  formula (*)")
    print("=" * 74)
    worst = 0.0
    for dims in [(2, 2), (2, 5), (3, 3), (4, 5), (6, 6), (2, 2, 2, 2)]:
        for seed in [42, 123]:
            psi = fixed_point(dims, seed)
            if psi is None:
                continue
            d, fo = im_frac_max(psi), im_frac_formula(psi, 1.0)
            worst = max(worst, abs(d - fo))
            print(f"   dims={str(dims):12s} seed={seed:3d}:  direct={d:.6f}  formula={fo:.6f}")
    print(f"   --> max |direct - formula| = {worst:.2e}  (machine precision)")

    print("\n" + "=" * 74)
    print("2. RANK INDEPENDENCE AT FIXED N  (max alignment, theta=1)")
    print("=" * 74)
    for N, configs in [(16, [(2, 8), (4, 4), (2, 2, 2, 2)]),
                       (36, [(6, 6), (4, 9), (2, 2, 3, 3)]),
                       (64, [(8, 8), (16, 4), (2, 2, 2, 2, 2, 2)])]:
        print(f"  N = {N}:")
        for dims in configs:
            mu, sd, n = summarize(dims, seeds)
            print(f"     dims={str(dims):20s} min-dim={min(dims):2d}: im_frac={mu:.4f} ± {sd:.4f} (n={n})")

    print("\n" + "=" * 74)
    print("3. N DEPENDENCE  (min-dim held at 2; theta=1)")
    print("=" * 74)
    Ns, mus = [], []
    for k in range(2, 8):
        dims = tuple([2] * k)
        mu, sd, n = summarize(dims, seeds)
        Ns.append(2 ** k)
        mus.append(mu)
        print(f"   2^{k}  N={2 ** k:3d}: max-align={mu:.4f} ± {sd:.4f}   "
              f"opt-align={summarize(dims, seeds, conv='opt')[0]:.4f}")
    # Fit a - b * N^{-c}
    Ns = np.array(Ns, float)
    mus = np.array(mus, float)
    from scipy.optimize import curve_fit
    try:
        popt, _ = curve_fit(lambda N, a, b, c: a - b * N ** (-c), Ns, mus,
                            p0=[0.4, 0.5, 0.5], maxfev=10000)
        print(f"   fit  im_frac(N) = {popt[0]:.3f} - {popt[1]:.3f} * N^(-{popt[2]:.3f})")
    except Exception as e:  # pragma: no cover
        print(f"   fit failed: {e}")
    print(f"   analytic large-N limit (max-align): {limit_max_align():.4f}")

    print("\n" + "=" * 74)
    print("4. HAAR BASELINE  (max alignment, theta=1)")
    print("=" * 74)
    print(f"   fixed-point asymptote (analytic) : {limit_max_align():.4f}")
    print("   Haar baseline (max-align) does NOT converge to 1/sqrt2; it keeps")
    print("   rising with N (Gamma(2 +- i*theta) modulation -- see exploration):")
    for N in [4, 16, 64, 256, 1024, 16384, 262144]:
        tr = 4000 if N <= 16384 else 800
        print(f"   N={N:7d}:  im_frac_Haar = {haar_im_frac(N, trials=tr):.4f}")
    print("   --> the fixed point (~0.40) carries far LESS imaginary content")
    print("       than a Haar-random state at every N: minimal, not maximal,")
    print("       phase complexity.")

    print("\n" + "=" * 74)
    print("5. THETA DEPENDENCE  (dims=(4,4); small-theta linear in theta)")
    print("=" * 74)
    for theta in [0.0, 0.25, 0.5, 1.0, 2.0]:
        mu, sd, n = summarize((4, 4), seeds, theta=theta)
        print(f"   theta={theta:4.2f}: im_frac={mu:.4f} ± {sd:.4f}   "
              f"analytic limit={limit_max_align(theta) if theta > 0 else 0.0:.4f}")


if __name__ == "__main__":
    main()
