The Einstein-Langevin equation predicts that gravitational decoherence of a rigid body in spatial superposition follows a Gaussian temporal profile — not the exponential profile of the Diosi-Penrose model — because the noise kernel for stationary matter is time-independent, and this static noise is a direct consequence of the semiclassical Einstein equation rather than an additional postulate about spacetime fluctuations.

# Gaussian Gravitational Decoherence

**Status:** Pre-submission draft

## In plain English

Put a small but massive object in two places at once — a quantum
superposition — and gravity itself may destroy the superposition. Penrose and
Diósi famously estimated how fast; experiments are inching toward testing it.
This paper sharpens the prediction: the superposition should not decay
exponentially (steadily, like radioactivity) but as a Gaussian — slowly at
first, then all at once. The timescale agrees with the Penrose–Diósi estimate
to within about 13%, but the *shape* of the decay differs — something an
experiment could check, distinguishing this account from its rivals. The shape
prediction is a sketch, not a finished proof: it relies on modeling gravity's
noise as "Gaussian noise", which is an assumption of the framework used, not
something derived. A second worry — whether an ensemble-averaged fading of
coherence counts as genuine decoherence — is now settled at the level that
matters for experiment: within any single run the superposition's coherence is
exactly preserved and only its phase shifts, and the predicted fading is exactly
what an ordinary many-shot interferometer measures (each new run creates the
superposition anew, redrawing the noise from the superposition's own mass
distribution rather than from a fixed external field, so each shot is an
independent sample), so the prediction is well-defined. Whether to *call* that
ensemble fading "decoherence" is a question of words, not of what the experiment
sees; and because the fading is in
principle reversible, a spin-echo control run could even tell it apart from a
truly irreversible collapse. A further
idea — that rigid crystals would decay Gaussian while soft materials would
drift back toward exponential — is a conjecture: the mechanism has not been
worked out, and it is not yet known whether any realistic laboratory object
is soft enough to show the difference. Nothing here has been tested by any
experiment.

## Results

1. **(Sketch)** The decoherence timescale is tau_coh = (4sqrt(2)/5) hbar/E_Delta ~ 1.13 tau_DP, determined by the same gravitational self-energy as the Diosi-Penrose prediction.
2. **(Sketch)** The temporal profile is Gaussian, not exponential -- a consequence of the noise kernel for stationary matter being time-independent in the Newtonian limit. Both results rest on the Einstein-Langevin framework's Gaussian-noise assumption (made explicit as Assumption 1 in the paper, not derived); this is now the *only* source of the Sketch ceiling, since the ensemble-dephasing caveat (Remark 2) is resolved at the operational level (paper §4.3): the per-realization coherence magnitude is exactly conserved and the Gaussian suppression is an echo-reversible inhomogeneous-dephasing effect recovered only on averaging, so the predicted quantity is the free-evolution ensemble visibility a many-shot interferometer measures (the identification holds because the framework locates the noise source in the superposition's own mass distribution, so each fresh preparation redraws the noise; a frozen external field is a distinct model the framework does not adopt).
3. **(Conjecture)** The profile is material-dependent: rigid crystalline bodies give Gaussian decoherence, while bodies whose acoustic modes approach the gravitational coherence frequency would transition toward exponential. The crossover mechanism is asserted, not derived, and whether any experimentally realistic platform reaches the crossover regime is open.

## Relationship to other programs

This paper's predictions are understood within the self-consistency hierarchy as Level 2 (metric) phenomena: the Einstein-Langevin equation is the stochastic extension of the semiclassical Einstein equation whose fixed-point structure is studied in `fixed-point-existence` (exact in the Starobinsky case, Rigorous; perturbative Banach argument at Sketch level since its 2026-06 demotion; Schauder existence conditional). The decoherence prediction here does not depend on those existence results.

## Build

```bash
pdflatex index.tex
```
