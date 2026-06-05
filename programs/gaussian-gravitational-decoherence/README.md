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
to within about 13%, but the *shape* of the decay differs, and it depends on
the material: rigid crystals decay Gaussian, soft materials drift back toward
exponential. Shape and material-dependence are things an experiment can
check, distinguishing this account from its rivals. The prediction is derived
at draft rigor and has not been tested by any experiment.

## Results

1. The decoherence timescale is tau_coh = (4sqrt(2)/5) hbar/E_Delta ~ 1.13 tau_DP, determined by the same gravitational self-energy as the Diosi-Penrose prediction.
2. The temporal profile is Gaussian, not exponential -- a consequence of the noise kernel for stationary matter being time-independent in the Newtonian limit.
3. The profile is material-dependent: rigid crystalline bodies give Gaussian decoherence, while soft or amorphous bodies whose acoustic modes approach the gravitational coherence frequency transition toward exponential.

## Relationship to other programs

This paper's predictions are understood within the self-consistency hierarchy as Level 2 (metric) phenomena: the Einstein-Langevin equation is the stochastic extension of the semiclassical Einstein equation whose fixed-point structure is established in `fixed-point-existence`.

## Build

```bash
pdflatex index.tex
```
