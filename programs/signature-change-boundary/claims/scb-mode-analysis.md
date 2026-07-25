---
id: scb-mode-analysis
program: signature-change-boundary
tier: rigorous
status: live
statement: >
  On a fixed background whose metric changes signature across a degenerate
  surface, the nu = 1/2 Bessel reduction puts the mode equation into elementary
  trigonometric (hyperbolic side) or exponential (elliptic side) form near the
  surface, with no logarithmic solutions for any n.
object:
  name: mode_ode
  space: solutions of the field equation near a degenerate surface
hypotheses:
  - fixed background
  - metric degenerate on the crossing surface
  - test-field approximation
falsifier: a mode admitting a logarithmic solution at nu = 1/2
consequence: >
  Fields cross the signature-change boundary in a finite, controlled way, with a
  causal-type asymmetry - timelike paths terminate, spacelike paths cross intact.
novelty: {status: unchecked}
provenance: {born: 2026-06-23, born_by: worker}
notes: >
  This program is at notes stage - there is no index.tex, so the L13 tex-sync
  lint has nothing to check against. Section 4's geodesic-continuation gap and
  sections 7-8 were reset to Sketch by correction PR #147; section 5, the mode
  analysis relied on here, was left intact at Rigorous.
---

Load-bearing for [[ce-cancellation-capacity]] across a program boundary. That
edge is declared `cross-object` with a written justification, which is the
correct treatment: the ODE reduction is proved here about mode solutions, and
used there about the self-consistency weight.
