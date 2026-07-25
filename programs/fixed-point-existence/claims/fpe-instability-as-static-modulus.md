---
id: fpe-instability-as-static-modulus
program: fixed-point-existence
tier: speculation
status: dead
statement: >
  The linear instability of the exact constant-H de Sitter solution corresponds,
  re-expressed without time evolution, to a continuous one-parameter family of
  nearby physically inequivalent exact fixed points of the same trace-anomaly
  equation - the growing mode integrating to a genuine static modulus.
hypotheses:
  - conformal matter
  - a2 > 0
  - FRW ansatz
falsifier: >
  Solve the full non-linearized fixed-point condition allowing deviations from
  exact de Sitter, treating H as a free static parameter.
consequence: >
  Would have reframed instability as under-determination, requiring a selection
  principle beyond self-consistency.
provenance: {born: 2026-07-24, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-24
  cause: >
    Arithmetic. The constant-H condition reduces to H^2 (G a2 H^2 - 180 pi) = 0,
    whose roots are exactly {0, +H0, -H0}. A nonzero polynomial has a finite zero
    set. No continuous branch exists, for any a2 > 0. Further, f'(H0) is nonzero,
    so the root is simple and transverse and the static Jacobian's kernel is
    zero-dimensional - there is not even an infinitesimal flat direction.
  defense_attempted: yes
  defense_findings: >
    The defense rebuilt the curvature computation from a bare FRW metric rather
    than rechecking, confirming Weyl^2 = 0 identically for any a(t) and
    box-R = -6 H''' - 42 H H'' - 24 H'^2 - 72 H^2 H'. It then supplied the
    decisive argument: the only family genuinely near H0 in the full theory is
    the time-translation orbit H(t - t0) of a trajectory on the saddle's
    unstable manifold - and time translation is exactly the gauge freedom
    Axiom 1 requires to be quotiented out, not promoted to distinct fixed points.
    The family S4 needed would have been pure gauge under the very axiom invoked
    to construct it.
  citation_note: >
    The attack pass quoted Hawking-Hertog-Reall as saying "no continuous family
    of exact de Sitter solutions... only a single instantonic solution". The
    defense fetched the paper, verified the separate quote "unstable both to the
    future and to the past" verbatim on page 4, and could NOT locate that second
    phrase. Treat it as an accurate paraphrase, never as a verbatim quote; cite
    the substance (their eq. 2.19 and the shooting-parameter analysis) instead.
---

Dead, and it produced [[fpe-constant-h-rigidity]] - which argues *for* the
fixed-point program's central thesis, the opposite valence from what this
speculation wanted.

Two tempting non-claims were ruled out in the same pass: the a2-deformation
"family" is a family of fixed points of *different theories*, not a modulus of
one; and the H = 0 root is a degenerate double root, the standard graceful-entry
problem in this model class rather than a new one.
