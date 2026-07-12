# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project

**This repository is an autonomous research system running on GitHub.** Seven
scheduled agent routines (worker, reviewer, responder, red-team, scout,
librarian, governor) claim issues, write and adversarially review derivations,
demote results that fail stress-testing, and set direction; merges happen only
through a mechanical gate stack, with the human acting as experimenter rather
than reviewer. The system mapping — Actions as compute, labels as the state
machine, issues/PRs as the database, the gate stack as the policy engine — is
in `docs/ARCHITECTURE.md`.

Its workload is a research program developing a geometric block universe
framework for quantum gravity. Papers are organized into programs (each with
its own directory) and live at varying stages of completion.

## Which mode are you in?

You are operating in one of two modes, and it matters which:

- **As a routine** (dispatched by an `autonomy-*` workflow, authenticated as
  the machine account): your role file in `automation/routines/<role>.md` and
  `AUTONOMY.md` are controlling. You hold the machine account's authority and
  all of its limits — protected paths, quorum rules, the NEVER list.
- **As an interactive assistant** (a Claude Code session the human
  experimenter is driving): you act under their direction and identity. You
  may draft changes to protected paths for their review, but such changes
  merge only through the experimenter's documented amendment procedure, and
  infrastructure changes you co-author belong in the `EXPERIMENT.md` log.
  You still follow METHODOLOGY's rigor and citation discipline — the schema
  does not relax for humans.

## Programs

Each program has its own directory under `programs/` with a `README.md` describing its status, results, and relationship to other programs. Read the relevant README before starting work on a program.

## Repository structure

```
programs/                          — Each program has its own directory
  <program-name>/
    index.tex                      — The paper (early-stage programs may have notes/ only)
    README.md                      — Status, key results, "In plain English" abstract
    OBJECTIVES.md                  — Ordered milestones with done-conditions
    explorations/                  — Research investigations for this program
explorations/governance/           — Cross-program governance explorations
automation/routines/               — Autonomous-mode role definitions (protected path)
docs/                              — ARCHITECTURE.md (the system mapping), workflow docs, historical experiment data
metrics/                           — Autonomous-experiment metrics
scripts/hooks/                     — Quality-gate hooks (protected path)
tools/                             — CI tooling: citation verification (protected path)
METHODOLOGY.md                     — Research-as-code workflow (read before contributing)
AUTONOMY.md                        — Constitution of the autonomous experiment mode
EXPERIMENT.md                      — Pre-registered autonomous experiment design
```

## Build

Each paper compiles independently:

```bash
pdflatex programs/<program-name>/index.tex
```

The bibliography uses `\begin{thebibliography}` (no separate .bib file), so no bibtex step is needed.

## Methodology

Read `METHODOLOGY.md` before contributing. It defines:

- The research-as-code workflow: contributions are PRs against issues, explorations are structured investigations in each program's `explorations/` directory
- Rigor standards and lifecycle: Conjecture → Sketch → Rigorous, with explicit demotion paths
- Citation discipline: paper-grade citations must be verified via web search; exploratory references must be flagged as unverified
- Adversarial review modes: verification (check the math) and stress testing (actively try to break the result)
- Agent team patterns: when to use teams vs. subagents, standard roles, team size guidance

## Conventions

- LaTeX with `amsmath`, `amssymb`, `amsthm` for mathematics
- Custom theorem environments: `theorem`, `axiom`, `proposition`, `lemma`, `conjecture`, `definition`, `remark`
- All results labeled: **(Rigorous)**, **(Sketch)**, or **(Conjecture)**
- Equations labeled `\label{eq:...}`, sections `\label{sec:...}`
- References use `\cite{key}` with keys defined in `thebibliography`
- Accented names use LaTeX commands (e.g., `Di\'osi`, `M\o ller`)
- Date format: Month YYYY
- Authors: Will Regelmann, Claude (Anthropic)
- Each program README maintains an `## In plain English` abstract for
  non-physicist readers: every sentence traceable to a labeled result, no
  claim stated above its rigor label, conjectures called conjectures in plain
  English too. Updated in the same PR as any headline rigor change; the
  governor freshness-sweeps monthly.

## Documentation

Markdown files in this repo (READMEs, explorations, this file) can include
Mermaid diagrams — GitHub renders them natively in-browser, no separate image
export needed.

## Before starting work

1. Read `METHODOLOGY.md` — understand the contribution workflow and rigor requirements.
2. Read the program's `explorations/` directory if working on a topic that has been previously investigated.
3. Read the current state of the paper (`programs/<name>/index.tex`).
4. Check open GitHub issues for the relevant program before opening a new one.
