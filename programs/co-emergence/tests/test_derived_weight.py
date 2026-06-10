"""Tests for the derived-weight toy model (issue #81).

Verifies the claims of the 2026-06-10 exploration
`2026-06-10-derived-weight-from-signature.md`:

1. Mode-level dichotomy: the elliptic (Euclidean) branch is positive and
   cannot cancel; every hyperbolic (Lorentzian) polarization admits exact
   destructive cancellation.
2. The derived weight with complex polarization reproduces the stipulated
   weight exp((-1 + i theta) R) exactly at eps = 1/(1+theta), c = 1+theta,
   fixed points included.
3. Pure Euclidean (eps = 1) recovers the Riemannian Boltzmann model.
4. Pure Lorentzian (eps = 0) gives a unimodular weight: uniform fixed-point
   magnitudes, exact phase locking phi_sigma = c R_sigma, nonzero imaginary
   coherences, entirely phase-generated entanglement — and phase-stripping
   recovers the uniform product state, NOT the Riemannian fixed point.
5. The real polarization (selected by a real signature-change crossing)
   yields a real fixed point with sign-indefinite weights: cancellation
   without complex structure.
6. The two complex polarizations (continuation directions) give conjugate
   fixed points with equal entropy (informs #88).
"""

import numpy as np
import pytest

from .toy_model import CoEmergenceModel
from .derived_weight import (
    DerivedWeightModel,
    elliptic_mode,
    entanglement_entropy,
    hyperbolic_mode_complex,
    hyperbolic_mode_real,
)

DIMS = (2, 2)
ALPHAS = [0.5, 0.3]
BETA = 0.4
H_PAPER = np.array([1.0, 0.7, 0.5, 1.2])  # the paper's N=4 external field


def _h_generic(seed=2026, n=4):
    return np.random.RandomState(seed).uniform(0.5, 1.5, size=n)


def _fixed_point(model, seed=42, n_starts=20):
    np.random.seed(seed)
    fps = model.find_fixed_points(n_starts=n_starts)
    assert len(fps) > 0, "no fixed point found"
    return fps[0]


class TestModeDichotomy:
    """Lemma 1 and Lemma 2 of the exploration, at the mode level."""

    def test_elliptic_branch_positive_no_cancellation(self):
        s = np.linspace(0.0, 50.0, 1000)
        w = elliptic_mode(s)
        assert np.all(w > 0)
        # No cancellation: superpositions of weights add moduli exactly.
        assert abs(w[10] + w[500]) == pytest.approx(abs(w[10]) + abs(w[500]))

    def test_hyperbolic_cancellation_every_polarization(self):
        # Any solution with phi(0) = 1 is cos(s) + a*sin(s); at s = pi it
        # equals -1 regardless of the (complex) polarization a.
        rng = np.random.RandomState(7)
        for _ in range(20):
            a = rng.randn() + 1j * rng.randn()
            phi = lambda s: np.cos(s) + a * np.sin(s)
            assert abs(phi(0.0) + phi(np.pi)) < 1e-12
        # The two canonical polarizations included.
        assert abs(hyperbolic_mode_complex(0) + hyperbolic_mode_complex(np.pi)) < 1e-12
        assert abs(hyperbolic_mode_real(0) + hyperbolic_mode_real(np.pi)) < 1e-12

    def test_real_polarization_is_equal_weight_superposition(self):
        # cos s - sin s = a e^{is} + b e^{-is} with |a| = |b| = 1/sqrt(2):
        # the real crossing selects no complex line.
        s = np.linspace(0, 10, 200)
        a, b = (1 + 1j) / 2, (1 - 1j) / 2
        recon = a * np.exp(1j * s) + b * np.exp(-1j * s)
        assert np.allclose(recon, hyperbolic_mode_real(s), atol=1e-12)
        assert abs(abs(a) - abs(b)) < 1e-15


class TestDerivedEqualsStipulated:
    """The stipulated gamma = -1 + i theta is the mixed-signature member
    eps = 1/(1+theta), c = 1+theta of the derived family."""

    @pytest.mark.parametrize("theta", [0.5, 1.0, 2.0])
    def test_weights_identical(self, theta):
        c, eps = 1.0 + theta, 1.0 / (1.0 + theta)
        derived = DerivedWeightModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, c=c, eps=eps
        )
        stipulated = CoEmergenceModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, gamma=-1.0 + 1j * theta
        )
        rng = np.random.RandomState(0)
        for _ in range(5):
            psi = rng.randn(4) + 1j * rng.randn(4)
            psi /= np.linalg.norm(psi)
            assert np.allclose(derived.weights(psi), stipulated.weights(psi), atol=1e-13)

    def test_fixed_points_identical(self):
        theta = 1.0
        derived = DerivedWeightModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA,
            c=1.0 + theta, eps=1.0 / (1.0 + theta),
        )
        stipulated = CoEmergenceModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, gamma=-1.0 + 1j * theta
        )
        fp_d = _fixed_point(derived)
        fp_s = _fixed_point(stipulated)
        assert CoEmergenceModel.rho_distance(fp_d, fp_s) < 1e-8


class TestPureEuclidean:
    """eps = 1, c = 1: the derived weight is the Riemannian Boltzmann weight."""

    def test_recovers_riemannian_model(self):
        derived = DerivedWeightModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, c=1.0, eps=1.0
        )
        riem = CoEmergenceModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, gamma=-1.0 + 0j
        )
        psi = np.ones(4, dtype=complex) / 2.0
        w = derived.weights(psi)
        assert np.allclose(w.imag, 0.0, atol=1e-14)
        assert np.all(w.real > 0)
        assert np.allclose(w, riem.weights(psi), atol=1e-13)
        fp = _fixed_point(derived)
        rho = CoEmergenceModel.partial_trace(fp, DIMS, (0,))
        assert abs(rho[0, 1].imag) < 1e-10  # classical correlations only


class TestPureLorentzian:
    """eps = 0: unimodular weight. Phase locking survives; damping does not."""

    @pytest.fixture(scope="class")
    def model(self):
        return DerivedWeightModel(
            dims=DIMS, h=_h_generic(), alphas=ALPHAS, beta=BETA, c=1.0, eps=0.0
        )

    @pytest.fixture(scope="class")
    def fp(self, model):
        return _fixed_point(model)

    def test_weight_unimodular(self, model, fp):
        assert np.allclose(np.abs(model.weights(fp)), 1.0, atol=1e-13)

    def test_fixed_point_converges(self, model, fp):
        assert CoEmergenceModel.rho_distance(model.F_map(fp), fp) < 1e-10

    def test_uniform_magnitudes(self, fp):
        assert np.allclose(np.abs(fp), 0.5, atol=1e-10)

    def test_exact_phase_locking(self, model, fp):
        # phi_sigma - phi_0 = c (R_sigma - R_0) mod 2pi
        R = model.curvature(fp).real
        rel_phase = np.angle(fp / fp[0])
        expected = model.c * (R - R[0])
        diff = np.mod(rel_phase - expected + np.pi, 2 * np.pi) - np.pi
        assert np.allclose(diff, 0.0, atol=1e-10)

    def test_imaginary_coherence_nonzero(self, fp):
        rho = CoEmergenceModel.partial_trace(fp, DIMS, (0,))
        assert abs(rho[0, 1].imag) > 1e-3

    def test_entanglement_entirely_phase_generated(self, fp):
        # The Lorentzian state is entangled...
        S_lor = entanglement_entropy(fp, DIMS, (0,))
        assert S_lor > 1e-3
        # ...while its phase-stripped counterpart (uniform magnitudes) is the
        # rank-one product state with zero entropy.
        stripped = np.abs(fp).astype(complex)
        stripped /= np.linalg.norm(stripped)
        assert entanglement_entropy(stripped, DIMS, (0,)) < 1e-10

    def test_phase_stripping_does_not_recover_euclidean_fixed_point(self, fp):
        # Unlike the stipulated model, magnitudes differ across signatures:
        # stripping phases yields the uniform state, not the Boltzmann state.
        euclidean = DerivedWeightModel(
            dims=DIMS, h=_h_generic(), alphas=ALPHAS, beta=BETA, c=1.0, eps=1.0
        )
        fp_e = _fixed_point(euclidean)
        stripped = np.abs(fp).astype(complex)
        stripped /= np.linalg.norm(stripped)
        assert CoEmergenceModel.rho_distance(stripped, fp_e) > 1e-2


class TestRealPolarization:
    """The real-crossing polarization: cancellation without complexness."""

    def test_fixed_point_real_no_coherences(self):
        model = DerivedWeightModel(
            dims=DIMS, h=_h_generic(), alphas=ALPHAS, beta=BETA,
            c=1.0, eps=0.0, polarization="real",
        )
        fp = _fixed_point(model)
        # Weights are real, so the fixed point is real up to a global phase.
        fp_aligned = fp * np.exp(-1j * np.angle(fp[np.argmax(np.abs(fp))]))
        assert np.allclose(fp_aligned.imag, 0.0, atol=1e-8)
        rho = CoEmergenceModel.partial_trace(fp, DIMS, (0,))
        assert abs(rho[0, 1].imag) < 1e-8

    def test_weights_sign_indefinite(self):
        # With an extent scale placing c*R across a zero of cos - sin, the
        # real-polarization weights take both signs: real cancellation.
        h = np.array([0.5, 0.6, 1.4, 1.5])
        model = DerivedWeightModel(
            dims=DIMS, h=h, alphas=ALPHAS, beta=BETA,
            c=0.6, eps=0.0, polarization="real",
        )
        psi = np.ones(4, dtype=complex) / 2.0
        w = model.weights(psi).real
        assert np.any(w > 0) and np.any(w < 0)


class TestConjugation:
    """The two continuation directions give conjugate fixed points with the
    same entropy: the sign of theta is an orientation choice (informs #88)."""

    def test_conjugate_fixed_points_equal_entropy(self):
        theta = 1.0
        plus = CoEmergenceModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, gamma=-1.0 + 1j * theta
        )
        minus = CoEmergenceModel(
            dims=DIMS, h=H_PAPER, alphas=ALPHAS, beta=BETA, gamma=-1.0 - 1j * theta
        )
        fp_p = _fixed_point(plus)
        fp_m = _fixed_point(minus)
        assert CoEmergenceModel.rho_distance(np.conj(fp_p), fp_m) < 1e-8
        S_p = entanglement_entropy(fp_p, DIMS, (0,))
        S_m = entanglement_entropy(fp_m, DIMS, (0,))
        assert S_p == pytest.approx(S_m, abs=1e-9)
        rho_p = CoEmergenceModel.partial_trace(fp_p, DIMS, (0,))
        rho_m = CoEmergenceModel.partial_trace(fp_m, DIMS, (0,))
        assert rho_p[0, 1].imag == pytest.approx(-rho_m[0, 1].imag, abs=1e-9)
