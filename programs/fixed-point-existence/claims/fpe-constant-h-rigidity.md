---
id: fpe-constant-h-rigidity
program: fixed-point-existence
tier: sketch
status: live
statement: >
  For fixed conformal matter content, the self-consistency condition on
  constant-H geometries has the isolated solution set {0, +H0, -H0}, with the
  nonzero roots simple and transverse. There is zero continuous freedom: given
  a2, the cosmological geometry is determined with no free parameters.
object:
  name: constant_H_fixed_point_set
  definition: "zero set of f(H) = H^2 (G a2 H^2 - 180 pi) / (15 pi)"
  space: constant-H FRW geometries
hypotheses:
  - conformal matter
  - a2 > 0
  - FRW ansatz
  - constant H
depends_on:
  - id: fpe-starobinsky-existence
    role: load-bearing
    transfers: same-object
falsifier: >
  An FRW conformal-matter model whose constant-H self-consistency equation has a
  non-isolated or degenerate nonzero root - i.e. a genuine modulus.
consequence: >
  Self-consistency here is *predictive*, not merely satisfiable. This is a
  substantive statement in favour of the fixed-point program's central thesis:
  the constraint pins the geometry rather than leaving a family of equally
  admissible universes.
novelty: {status: unchecked}
provenance: {born: 2026-07-24, born_by: adversary}
derivation: >
  Reducing the trace-anomaly relation on exact constant-H FRW gives a polynomial
  in H with roots {0, +H0, -H0}, H0^2 = 180 pi / (G a2). A nonzero polynomial has
  a finite zero set. f'(H0) is nonzero, so the nonzero roots are simple and the
  static Jacobian's kernel is zero-dimensional. Derived independently by two
  agents, both from the paper's own equations rather than from each other.
gaps:
  - >
    H = 0 is a degenerate (double) root, trivially self-consistent since both
    sides vanish at R = 0. The rigidity statement applies to the nonzero roots;
    flat space being equally self-consistent is the standard graceful-entry
    problem in this model class and is not addressed here.
  - >
    Verification-mode review only is needed for promotion - this is arithmetic
    on top of an existing Rigorous existence result, not new physics.
---

Produced by the adversarial investigation of
[[fpe-instability-as-static-modulus]], which claimed the opposite and was false.

The H = 0 root plausibly bears on co-emergence's mass-generation conjecture,
which requires nonzero curvature: if flat space is equally self-consistent, the
question of why curvature is selected is live. Recorded as a pointer, not
pursued here.
