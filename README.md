# Self-Consistency as Physical Law

### Research-as-code: running a theoretical-physics program with AI agents as contributors

[![tests](https://github.com/willregelmann/self-consistency/actions/workflows/tests.yml/badge.svg)](https://github.com/willregelmann/self-consistency/actions/workflows/tests.yml)
[![build-papers](https://github.com/willregelmann/self-consistency/actions/workflows/build-papers.yml/badge.svg)](https://github.com/willregelmann/self-consistency/actions/workflows/build-papers.yml)
[![verify-citations](https://github.com/willregelmann/self-consistency/actions/workflows/verify-citations.yml/badge.svg)](https://github.com/willregelmann/self-consistency/actions/workflows/verify-citations.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

**This repository is primarily an experiment in a methodology**: how to run a
rigorous research program with AI agents as contributors and a human as
reviewer. The paper is the source, open problems are GitHub issues, and
contributions — including from AI agents — arrive as pull requests subject to
review, self-checks, adversarial critique, rigor labels, and machine
verification.

Theoretical physics (quantum gravity, via a self-consistency framework) is the
**testbed** — chosen because it is unforgiving: a hard formal domain where
sloppy or hallucinated AI output becomes obvious. The research is real and is
described below, but the artifact worth studying is the *process*.

## What this demonstrates

The agent-engineering machinery is documented in **[`docs/agent-workflow.md`](docs/agent-workflow.md)** — roles, the contribution lifecycle, agent-team debates, custom tooling, and guardrails. Highlights:

- **Agent-as-contributor, human-as-reviewer.** Agents work on branches and open PRs; only the human merges. ([`METHODOLOGY.md`](METHODOLOGY.md))
- **Custom agent tooling** in [`.claude/`](.claude/commands/): `/work-issue`, `/review-pr` (two-pass dialectical review), `/restructure-paper`, plus `TeammateIdle`/`TaskCompleted` quality-gate hooks.
- **Agent-team debates** that develop competing positions in parallel to fight anchoring, then adjudicate by synthesis — recorded as dated Explorations.
- **Verifiable output over attested output.** Three CI gates: tests pass, every paper compiles, and **every citation resolves against Crossref/arXiv** ([`tools/verify_citations.py`](tools/verify_citations.py)).
- **Honest failure.** Rigor labels are demoted when wrong, negative results are recorded, and the citation gate has already caught a real mis-citation. See the **[case studies](docs/case-studies.md)** — the receipts.

## The research (testbed)

We propose that physical law is what self-consistency looks like: the universe
is the fixed point of a constraint requiring that geometry and the quantum
fields it hosts mutually determine each other. Gravity is not an independent
degree of freedom to be quantized but a constraint — the demand that the block
spacetime be self-consistent.

The work is organized into independent **programs**, each a self-contained paper
under `programs/<name>/index.tex` with its own `README.md`:

| Program | What it establishes | Status |
|---------|--------------------|--------|
| [`fixed-point-existence`](programs/fixed-point-existence/) | Self-consistent solutions to the semiclassical Einstein equation exist — exactly (Starobinsky trace anomaly), perturbatively (Banach contraction, $\kappa \sim (m/M_P)^2$), and conditionally (Schauder). The Planck scale emerges as the validity boundary. | Pre-submission draft |
| [`gaussian-gravitational-decoherence`](programs/gaussian-gravitational-decoherence/) | The Einstein–Langevin equation predicts a **Gaussian** (not exponential) decoherence profile, with $\tau_{\text{coh}} \sim 1.13\,\tau_{\text{DP}}$, as a consequence of the semiclassical equation rather than an added postulate. | Pre-submission draft |
| [`co-emergence`](programs/co-emergence/) | Mass, Lorentzian signature, local time, and local Hilbert space co-emerge as the unique cross-level self-consistent configuration, with phase structure (and an entropy excess) confirmed by a finite toy model through N=16. | Draft |

## Building

Each paper compiles independently; the bibliography is self-contained via `\begin{thebibliography}`, so no `bibtex` step is needed:

```bash
pdflatex programs/<program-name>/index.tex
```

The `co-emergence` numerics are backed by a test suite:

```bash
pip install -r requirements.txt
pytest
```

## Falsifiability

- Observation of BMV entanglement at the quantum gravity rate refutes the framework.
- Observation of gravitational decoherence at the Diosi–Penrose rate refutes the framework.
- The sharpest known limitation is black hole evaporation past the Page time, where topology change becomes essential.

## License

Released under [CC0 1.0 Universal](LICENSE) (public domain dedication).

## Authors

- Will Regelmann
- Claude (Anthropic)
