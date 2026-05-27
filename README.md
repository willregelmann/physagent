# Self-Consistency as Physical Law

[![tests](https://github.com/willregelmann/self-consistency/actions/workflows/tests.yml/badge.svg)](https://github.com/willregelmann/self-consistency/actions/workflows/tests.yml)
[![build-papers](https://github.com/willregelmann/self-consistency/actions/workflows/build-papers.yml/badge.svg)](https://github.com/willregelmann/self-consistency/actions/workflows/build-papers.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

This is an experiment in **research-as-code**: treating a theoretical physics project the way software teams treat a codebase. The papers are the source, open problems are GitHub issues, and contributions — including from AI agents — arrive as pull requests subject to review. The goal is to explore what happens when research is conducted with version control, structured review, and human–agent collaboration from the start.

---

We propose that physical law is what self-consistency looks like: the universe is the fixed point of a constraint requiring that geometry and the quantum fields it hosts mutually determine each other. Gravity is not an independent degree of freedom to be quantized but a constraint — the demand that the block spacetime be self-consistent.

## Programs

The work is organized into independent **programs**, each a self-contained paper under `programs/<name>/index.tex` with its own `README.md` describing status and results.

| Program | What it establishes | Status |
|---------|--------------------|--------|
| [`fixed-point-existence`](programs/fixed-point-existence/) | Self-consistent solutions to the semiclassical Einstein equation exist — exactly (Starobinsky trace anomaly), perturbatively (Banach contraction, $\kappa \sim (m/M_P)^2$), and conditionally (Schauder). The Planck scale emerges as the validity boundary. | Pre-submission draft |
| [`gaussian-gravitational-decoherence`](programs/gaussian-gravitational-decoherence/) | The Einstein–Langevin equation predicts a **Gaussian** (not exponential) decoherence profile, with $\tau_{\text{coh}} \sim 1.13\,\tau_{\text{DP}}$, as a consequence of the semiclassical equation rather than an added postulate. | Pre-submission draft |
| [`co-emergence`](programs/co-emergence/) | Mass, Lorentzian signature, local time, and local Hilbert space co-emerge as the unique cross-level self-consistent configuration. The Lorentzian self-consistency map produces phase structure (and an entropy excess) absent in the Riemannian case, confirmed by a finite toy model through N=16. | Draft |

## Building

Each paper compiles independently:

```bash
pdflatex programs/<program-name>/index.tex
```

The bibliography is self-contained via `\begin{thebibliography}`, so no `bibtex` step is needed.

## Numerical results

The `co-emergence` program is backed by a numerical toy model and scaling studies in `programs/co-emergence/tests/`:

```bash
pip install numpy scipy
pytest programs/co-emergence/tests/
```

## Falsifiability

- Observation of BMV entanglement at the quantum gravity rate refutes the framework.
- Observation of gravitational decoherence at the Diosi–Penrose rate refutes the framework.
- The sharpest known limitation is black hole evaporation past the Page time, where topology change becomes essential.

## Methodology

This project is developed collaboratively between a human author and AI agents. Agents claim GitHub issues, work on branches, and submit PRs for human review. All derivations must pass self-checks (dimensional analysis, limiting cases, consistency, order-of-magnitude sanity) before submission, and adversarial review by a second agent can be requested. Citations in the papers must be verified to exist; exploratory references in discussions must be flagged as unverified. See [`METHODOLOGY.md`](METHODOLOGY.md) for the full workflow and [`AGENTS.md`](AGENTS.md) for repository conventions.

## License

Released under [CC0 1.0 Universal](LICENSE) (public domain dedication).

## Authors

- Will Regelmann
- Claude (Anthropic)
