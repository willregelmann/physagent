---
id: ce-nohilbert
program: co-emergence
tier: rigorous
status: live
statement: >
  Any formulation of quantum gravity taking a Hilbert space with inner product
  as a fundamental input violates the timeless axiom, because the inner product
  requires either a preferred spatial hypersurface or a preferred time parameter.
hypotheses:
  - an arbitrary quantum gravity formulation taking a Hilbert space as fundamental
internal_steps:
  - step: the Fock-space inner product is a functional integral over a Cauchy surface
    hypotheses: [the standard QFT Fock-space construction]
  - step: unitary evolution presupposes a time parameter
    hypotheses: [evolution given explicitly by U(t2, t1)]
falsifier: >
  A Hilbert-space construction with a genuine inner product obtained by
  covariant, non-foliation-dependent means.
consequence: >
  The framework must not take a Hilbert space as input; local Hilbert structure
  has to co-emerge instead.
novelty:
  status: novel
  searched: 2026-07-24
  found: []
  note: >
    Self-contained argument, nothing to misattribute. But the checker
    independently sharpened the known gap: the AQFT/GNS counterexample class
    is NOT flat-space-limited as the audit supposed -- Hadamard states
    (Radzikowski 1996) and the Sorkin-Johnston vacuum (Afshordi, Aslanbeigi
    & Sorkin, JHEP 08 (2012) 137) both work on generic curved backgrounds.
    Grep confirms none of AQFT, GNS, Hadamard-state, Sorkin or Johnston
    appears anywhere in the paper. The real hedge is narrower and still
    open: all of that literature presupposes a FIXED background causal
    structure, which Axiom 2 forbids, so whether it survives when the metric
    is dynamical is genuinely unresolved.
tex: {file: programs/co-emergence/index.tex, label: ax:nohilbert}
provenance: {born: 2026-03-03, born_by: human}
audit:
  reviewed: 2026-07-24
  verdict: demote
  finding: >
    Universally quantified over "any formulation" but argued only for the
    canonical/Fock construction and explicit unitary evolution. Algebraic QFT
    builds the observable algebra covariantly and obtains a Hilbert space via
    GNS, with states selected by covariant conditions (Hadamard microlocal,
    Sorkin-Johnston from the causal Green's function). None of AQFT, GNS,
    Hadamard, or Sorkin-Johnston appears anywhere in the paper. No circularity
    found: the argument does not assume its conclusion.
---

Control-arm result (predates the autonomous experiment). The audit rated this
DEMOTE at medium confidence, hedged on the grounds that the counterexample
lives in QFT-on-a-fixed-background and may not survive in the no-background
regime the paper actually targets — state selection without a background is
itself open. Either narrow the quantifier to what is argued, or address the
algebraic route explicitly.
