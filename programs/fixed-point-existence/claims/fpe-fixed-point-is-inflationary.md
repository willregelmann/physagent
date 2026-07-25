---
id: fpe-fixed-point-is-inflationary
program: fixed-point-existence
tier: sketch
status: live
statement: >
  The trace-anomaly de Sitter fixed point sits at Planck-adjacent curvature for
  any physically realistic matter content, and is therefore an inflationary /
  early-universe result - not a model of the observed cosmological constant.
  Matching the observed Hubble rate would require a2 of order 1e124.
hypotheses:
  - conformal matter with a2 > 0 of realistic magnitude, a2 ~ 1e3 to 1e5
  - FRW / de Sitter setting
depends_on:
  - id: fpe-starobinsky-existence
    role: load-bearing
    transfers: same-object
  - id: fpe-starobinsky-coefficient
    role: load-bearing
    transfers: same-object
falsifier: >
  A physically motivated field content yielding a2 within a few orders of
  magnitude of 1e124 - i.e. closing roughly 120 orders from standard
  normalizations.
consequence: >
  The claim graph must record that this H0 and the observed cosmological H0 are
  different objects. Any downstream claim reading the fixed point as the
  present-day accelerating universe inherits a ~60-order-of-magnitude error.
novelty: {status: unchecked}
provenance: {born: 2026-07-24, born_by: adversary}
derivation: >
  Restoring hbar and c gives H0 ~ sqrt(180 pi / a2) * (M_Pl c^2 / hbar), i.e.
  roughly 1e40 to 1e43 per second for a2 in [1e3, 1e5]. Solving instead for the
  a2 that reproduces the observed H0 of about 2.2e-18 per second gives
  a2 ~ 4.0e124. Two agents derived the same figure independently. This
  reproduces the standard result that trace-anomaly-driven de Sitter is a
  near-Planckian phenomenon, H ~ M_Pl / sqrt(N).
notational_trap: >
  H0 is exactly the symbol conventionally used for the present-day Hubble
  constant. A speculation in this cycle silently substituted the observed value
  and produced an estimate 60 orders of magnitude off. The paper's text gestures
  at the inflationary application, but never states the converse.
---

Produced while killing [[ggd-ds-curvature-correction]].

A consequence worth recording separately: combined with the paper's own
Rigorous-by-citation instability, a quasi-de Sitter stage at this curvature
lasts of order 1e-42 to 1e-40 seconds - roughly 40 orders of magnitude shorter
than any laboratory timescale in the GGD program.
