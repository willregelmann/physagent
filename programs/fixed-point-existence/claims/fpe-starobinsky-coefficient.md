---
id: fpe-starobinsky-coefficient
program: fixed-point-existence
tier: sketch
status: live
statement: >
  The explicit fixed-point coefficient is H0^2 = 180 pi / (G |a2|).
hypotheses:
  - FRW/cosmological setting
  - a specific choice of conformal field content and normalization convention
depends_on:
  - id: fpe-starobinsky-existence
    role: load-bearing
    transfers: same-object
falsifier: a consistent field content giving a different coefficient
consequence: fixes the de Sitter scale in terms of the anomaly coefficient
novelty:
  status: prior-art
  searched: 2026-07-24
  found: [starobinsky]
  note: >
    Adjacent, and it SHARPENS the recorded defect rather than resolving it.
    Linde 2025 (arXiv:2509.01675, full text) reproduces what reads as
    Starobinsky's own relation, H0^-2 = k2/(2880 pi^2), with k2 the
    conformal-anomaly coefficient in Starobinsky's notation. Converting
    through this paper's own stated a2 = 2880 pi^2 a does not obviously
    reduce to the printed 180 pi/(G a2): the prefactors differ by a factor
    of 16 pi. Combined with the separately recorded
    dimensional-inconsistency defect, this is now two independent lines of
    evidence that the printed coefficient formula is wrong rather than
    merely under-specified. Adjudicating the convention needs the primary
    text, which remains unreachable.
tex: {file: programs/fixed-point-existence/index.tex, label: sec:starobinsky}
provenance: {born: 2026-06-26, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    The paper's own self-demotion of this coefficient to Sketch is correct and
    was independently validated: Starobinsky parametrizes via a specific field
    content rather than a general a2, and Capper-Duff establishes the anomaly's
    existence without fixing the field-content normalization. The trace-anomaly
    literature carries a genuine scheme-dependent ambiguity which vanishes on
    exact de Sitter - so it does not touch existence, but is exactly the
    normalization freedom that bites the coefficient.
defects:
  - id: dimensional-convention
    found: 2026-07-24
    by: adversary
    severity: correctness
    finding: >
      The formula as printed in programs/fixed-point-existence/index.tex is
      dimensionally inconsistent. With a2 dimensionless - standard usage for a
      central-charge-type coefficient, and how this claim treats it - 180 pi / G
      has SI dimension kg s^2 / m^3, not [time]^-2. It is a natural-units
      (hbar = c = 1) formula, and an independent search of the entire paper found
      NO unit-convention statement anywhere. Two agents derived this
      independently in the same cycle.
    scope: >
      Does not affect the existence claim, which is about de Sitter being a
      solution and is dimension-free. It affects the printed coefficient formula
      only - already Sketch for independent reasons.
    remedy: >
      State the unit convention explicitly at the equation, or restore hbar and c.
      To be applied on any future touch of that section.
---

An instance of the split being drawn in the right place: existence Rigorous,
coefficient Sketch. Issue #133 tracks restoring the coefficient.

**Open correctness defect, found 2026-07-24** — see `defects` above. The
coefficient formula lacks a stated unit convention and is dimensionally
inconsistent as printed. This surfaced while killing a speculation
([[ggd-ds-curvature-correction]]), not through any verification pass over the
paper, and it had been present through a CONFIRMED audit verdict.

See [[fpe-fixed-point-is-inflationary]] for what the coefficient's magnitude
actually implies once the convention is restored.
