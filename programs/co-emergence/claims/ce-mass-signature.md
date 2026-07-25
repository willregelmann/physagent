---
id: ce-mass-signature
program: co-emergence
tier: rigorous
status: live
statement: >
  Mass requires Lorentzian signature: on Riemannian signature p.p >= 0 always,
  so the mass shell p_mu p^mu = -m^2 can never hold, and the particle
  classification requires the (-,+,+,+) split.
hypotheses:
  - a curved, dynamical, generically symmetry-free 4-manifold
internal_steps:
  - step: the mass-shell/dispersion-relation argument is local and algebraic
    hypotheses: [local signature at a point]
    justification: >
      Purely pointwise; requires no symmetry group and no global structure.
      Airtight as stated.
  - step: massive particles are irreducible representations of ISO(3,1), classified by mass and spin
    hypotheses: [exact global Poincare symmetry on flat Minkowski space]
cites:
  - key: wigner
    role: load-bearing
    supports: classification of particles by mass and spin
    verified: {at: 2026-07-24, by: full-text, expires: 2027-07-24}
falsifier: >
  A local particle-content argument on a curved symmetry-free manifold that does
  not require the Lorentzian split.
consequence: mass and Lorentzian signature co-emerge rather than being independent
novelty:
  status: prior-art
  searched: 2026-07-24
  found: [wigner]
  note: >
    Sub-claim (ii) appeals directly to Wigner, Ann. Math. 40, 149 (1939),
    verified exact. IMPORTANT distinction: the citation is CORRECTLY
    attributed -- the defect is inferential, applying a flat-space
    exact-global-symmetry result to a curved, generically symmetry-free
    manifold. That is a scope gap, NOT the T2 citation-content-mismatch
    class, and should be kept analytically distinct from geroch/thm:exotic.
    No published curved or symmetry-free analogue of Wigner's theorem was
    found. Separately confirmed: the paper's 'ISO(4) has no analogous
    classification' is overstated -- Mackey induction handles it and SO(4)
    is compact; what is actually absent in Euclidean signature is the causal
    positive-energy interpretation.
tex: {file: programs/co-emergence/index.tex, label: sec:mass_signature}
provenance: {born: 2026-03-03, born_by: human}
audit:
  reviewed: 2026-07-24
  verdict: demote
  finding: >
    Sub-claim (i), the mass-shell argument, is airtight. Sub-claim (ii) appeals
    to Wigner's classification, which is a global exact-Minkowski-symmetry
    result, while the framework's own no-background axiom forbids an assumed
    symmetry group and Level 0 is a curved generically non-symmetric manifold.
    Nothing bridges the two. Secondary, non-load-bearing: "ISO(4) has no
    analogous classification" overstates - ISO(4) UIRs are classifiable via
    Mackey induction; what is absent in Euclidean signature is the causal
    positive-energy particle interpretation, not the classification itself.
---

Control-arm result. The fix is either a local curved-spacetime particle-content
argument replacing the flat-space Wigner appeal, or an explicit restriction of
this subsection to the flat/asymptotic limit.
