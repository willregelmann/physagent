---
id: ggd-single-realization
program: gaussian-gravitational-decoherence
tier: rigorous
status: live
statement: >
  With a static noise kernel the field is frozen within a realization, so
  per-realization coherence magnitude is exactly constant; the Gaussian t^2
  suppression appears only after ensemble averaging, and is echo-reversible
  inhomogeneous dephasing (T2*-type), not white-noise decoherence.
hypotheses:
  - the Einstein-Langevin model as stated
  - the static kernel of eq:N0000_static
  - Gaussian noise (Assumption 1)
depends_on:
  - id: ggd-noise-kernel
    role: load-bearing
    transfers: same-object
falsifier: >
  A per-realization coherence decay under a strictly static kernel, or failure of
  the Hahn-echo cancellation.
consequence: >
  The predicted observable is a shot-averaged visibility, and the discriminant
  against Diosi-Penrose is a many-shot quantity - which is what a real
  interferometer measures.
novelty: {status: unchecked}
tex: {file: programs/gaussian-gravitational-decoherence/index.tex, label: eq:single_realization}
provenance: {born: 2026-07-12, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Every algebraic and statistical step recomputed by hand. The paper does NOT
    conflate ensemble-averaged decay with single-system irreversibility - it does
    the opposite, labelling the averaged decay inhomogeneous dephasing,
    distinguishing it from Diosi white-noise T2 decoherence, and showing the Hahn
    echo cancels it exactly while noting an echo cannot cancel white noise. The
    T2*/T2 distinction was cross-checked against external literature. The 0.22
    fractional-coherence discriminant was independently recomputed: 0.216 at
    t/tau_DP = 0.474, against the paper's ~0.22 at ~0.48. No mismatch between the
    claimed and derived observable.
  exposition_gap: >
    The step "static kernel implies the field is frozen per realization" is
    asserted, not derived. Independently verified correct (the increment has zero
    variance, so the process is almost surely constant), but the paper should
    show it - roughly half a paragraph.
---

The newest in-run Rigorous result, merged 2026-07-12 via PR #151, and it audits
clean. The auditor was given a deliberately leading prompt suggesting this class
of result usually conflates the two notions; it found the opposite and showed
its work.
