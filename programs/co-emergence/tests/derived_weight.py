"""
Derived-weight variant of the co-emergence toy model (issue #81).

Instead of stipulating the self-consistency weight w_sigma = exp(gamma * R_sigma)
with gamma = -1 + i*theta, the weight is *built* from the temporal mode
structure of a free scalar on each signature, following the fixed-background
analysis of programs/signature-change-boundary/notes/2026-06-05-fixed-background-note.md
(section 5): temporal modes are oscillatory (hyperbolic operator) on the
Lorentzian side and exponentially decaying (elliptic operator) on the
Euclidean side, at the same rate constants.

Construction
------------
Each configuration sigma is assigned a temporal extent tau_sigma with
omega * tau_sigma = c * R_sigma (the action identification — a named gap of
the construction, see the 2026-06-10 exploration), of which a fraction eps
is Euclidean and 1 - eps is Lorentzian. The weight is the amplitude of the
canonically selected temporal mode accumulated over that extent:

    w(sigma) = phi_E(eps * tau_sigma) * phi_L((1 - eps) * tau_sigma)

with phi_E the unique bounded (decaying) elliptic branch, and phi_L one of
two polarizations of the hyperbolic solution space:

- 'complex': phi_L(u) = exp(i * omega * u), the Wick-contour / positive-
  frequency polarization. Then w = exp((-eps + i(1-eps)) * c * R), and the
  stipulated weight exp((-1 + i*theta) R) is recovered exactly at
  eps = 1/(1+theta), c = 1+theta.
- 'real': phi_L(u) = cos(omega u) - sin(omega u), the polarization selected
  by matching the Euclidean decaying branch across a *real* signature-change
  boundary (value + canonical momentum continuity). Real and sign-indefinite:
  cancellation without complex phases.

omega is set to 1 internally; only the product omega * tau = c * R enters.
"""

import numpy as np

from .toy_model import CoEmergenceModel


def elliptic_mode(s):
    """Euclidean (elliptic) temporal mode: the unique bounded branch.

    phi_E(v) = exp(-omega v), evaluated at s = omega * v. Real, positive,
    monotone — incapable of cancellation.
    """
    return np.exp(-np.asarray(s, dtype=float))


def hyperbolic_mode_complex(s):
    """Lorentzian mode, complex (Wick-contour / positive-frequency) polarization.

    phi_L(u) = exp(i omega u), evaluated at s = omega * u. Unimodular.
    The conjugate branch exp(-i omega u) is the opposite continuation
    direction (theta -> -theta, an orientation choice).
    """
    return np.exp(1j * np.asarray(s, dtype=float))


def hyperbolic_mode_real(s):
    """Lorentzian mode, real polarization selected by a real crossing of Sigma.

    Matching the Euclidean decaying branch e^{-omega v} across the degenerate
    boundary with value and canonical-momentum continuity gives
    phi_L(u) = cos(omega u) - sin(omega u): real, oscillatory,
    sign-indefinite. Evaluated at s = omega * u.
    """
    s = np.asarray(s, dtype=float)
    return np.cos(s) - np.sin(s)


class DerivedWeightModel(CoEmergenceModel):
    """Toy model whose weight is built from per-configuration mode amplitudes.

    Parameters beyond CoEmergenceModel's: c (action identification
    omega * tau_sigma = c * R_sigma), eps (Euclidean fraction of the temporal
    extent, in [0, 1]), polarization ('complex' or 'real').

    For polarization='complex' the weight equals exp(gamma_eff * R) with
    gamma_eff = (-eps + 1j * (1 - eps)) * c, which is also stored as
    self.gamma so the parent class's machinery stays consistent.
    """

    def __init__(self, dims, h, alphas, beta, c, eps, polarization="complex"):
        if not 0.0 <= eps <= 1.0:
            raise ValueError("eps must be a fraction in [0, 1]")
        if polarization not in ("complex", "real"):
            raise ValueError("polarization must be 'complex' or 'real'")
        gamma_eff = (-eps + 1j * (1.0 - eps)) * c if polarization == "complex" else None
        super().__init__(dims, h, alphas, beta, gamma_eff)
        self.c = c
        self.eps = eps
        self.polarization = polarization

    def weights(self, psi):
        """Weight = mode amplitude over the configuration's temporal extent."""
        R = self.curvature(psi).real
        s = self.c * R  # omega * tau_sigma, with omega = 1
        w_euclidean = elliptic_mode(self.eps * s)
        if self.polarization == "complex":
            w_lorentzian = hyperbolic_mode_complex((1.0 - self.eps) * s)
        else:
            w_lorentzian = hyperbolic_mode_real((1.0 - self.eps) * s)
        return w_euclidean * w_lorentzian


def entanglement_entropy(psi, dims, keep):
    """Von Neumann entropy (nats) of the reduced state of a pure state."""
    rho = CoEmergenceModel.partial_trace(np.asarray(psi), tuple(dims), tuple(keep))
    evals = np.linalg.eigvalsh(rho)
    evals = evals[evals > 1e-15]
    return float(-np.sum(evals * np.log(evals)))
