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
something derived — and on reading an ensemble-averaged fading of coherence
as genuine decoherence, which is an open interpretational question. A further
idea — that rigid crystals would decay Gaussian while soft materials would
drift back toward exponential — is a conjecture: the mechanism has not been
worked out, and it is not yet known whether any realistic laboratory object
is soft enough to show the difference. Nothing here has been tested by any
experiment.

## Results

1. **(Sketch)** The decoherence timescale is tau_coh = (4sqrt(2)/5) hbar/E_Delta ~ 1.13 tau_DP, determined by the same gravitational self-energy as the Diosi-Penrose prediction.
2. **(Sketch)** The temporal profile is Gaussian, not exponential -- a consequence of the noise kernel for stationary matter being time-independent in the Newtonian limit. Both results rest on the Einstein-Langevin framework's Gaussian-noise assumption (made explicit as Assumption 1 in the paper, not derived) and on an unresolved ensemble-dephasing caveat (Remark 2 in the paper).
3. **(Conjecture)** The profile is material-dependent: rigid crystalline bodies give Gaussian decoherence, while bodies whose acoustic modes approach the gravitational coherence frequency would transition toward exponential. The crossover mechanism is asserted, not derived, and whether any experimentally realistic platform reaches the crossover regime is open.

## Relationship to other programs

This paper's predictions are understood within the self-consistency hierarchy as Level 2 (metric) phenomena: the Einstein-Langevin equation is the stochastic extension of the semiclassical Einstein equation whose fixed-point structure is studied in `fixed-point-existence` (exact in the Starobinsky case, Rigorous; perturbative Banach argument at Sketch level since its 2026-06 demotion; Schauder existence conditional). The decoherence prediction here does not depend on those existence results.

## Build

```bash
pdflatex index.tex
```
