---
id: ce-signature-crossing-irreversible
program: co-emergence
tier: speculation
status: dead
statement: >
  A self-consistency weight whose configuration crosses a two-sided
  signature-change surface loses its cancellation-capacity structure
  irreversibly - no local operation confined to the elliptic region can restore
  the antiperiodic pattern phi(u + pi/omega) = -phi(u) on re-crossing - in
  contrast to the echo-reversible ensemble suppression in GGD.
hypotheses:
  - fixed background
  - the crossing is configurational, not temporal
  - omega nonzero
falsifier: >
  Construct a transformation T defined entirely within the elliptic region that
  maps elliptic-side data back to a state exhibiting antiperiodic cancellation
  on re-crossing.
consequence: >
  Would have supplied a geometric, non-time-evolved classicalization mechanism.
provenance: {born: 2026-07-24, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-24
  cause: >
    The falsifier is satisfied by T = identity. The junction condition
    (continuity of phi and canonical momentum) is an invertible 2x2 linear map
    between Lorentzian and Euclidean constants, det = -1, so any nonzero
    elliptic data returns nonzero Lorentzian data - and every nonzero hyperbolic
    solution is antiperiodic. Nothing is lost, so nothing needs restoring.
    Verified numerically at ~1e-15 residual over 20,000 trials.
  defense_attempted: yes
  defense_findings: >
    The defense pass corrected the attack: non-invertibility does not require
    nonlinearity or dissipation - a linear projection suffices, and the framework
    uses one (restriction to the bounded elliptic branch). It pursued that route
    and found the round trip on the restricted ray is ALSO exactly the identity,
    forcing B = -A, which is still a nonzero antiperiodic hyperbolic solution.
    It further resolved the reading the attack left open - the round trip
    preserves the specific (A,B), not merely the generic property - so the
    stronger information-preservation reading fails harder than the binary one.
  secondary_cause: >
    Axiom 1. "Crosses", "re-crossing", "restore" are temporal vocabulary, and
    the source note adopts here/there rather than before/after framing precisely
    to exclude that reading. The defense also identified why the analogy misfires
    technically: the geodesic asymmetry in the source is real because
    g_uv x'^u x'^v = -1 has no solution for lambda > 0, a genuine one-way
    obstruction. Nothing analogous exists at the mode level, where both solution
    spaces are present on both sides and matching is linear algebra.
---

Killed on the first adversarial pass and confirmed dead by an independent
defense pass that tried three rescue routes and computed each one. Retained as
a record, per the never-delete rule.

The one true statement in this neighbourhood is already in the record as the
mode-selection compatibility fact, and should not be dressed in decoherence
vocabulary.
