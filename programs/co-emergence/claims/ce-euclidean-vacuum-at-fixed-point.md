---
id: ce-euclidean-vacuum-at-fixed-point
program: co-emergence
tier: conjecture
status: live
statement: >
  At the exact Starobinsky de Sitter fixed point, the state the paper's own map
  text already specifies - the de Sitter-invariant Euclidean/Bunch-Davies vacuum,
  selected by symmetry plus Euclidean regularity rather than by Sorkin-Johnston -
  is a positive-semidefinite, Hadamard, CCR-satisfying two-point function whose
  defining inner product is provably Cauchy-surface-independent, and is therefore
  not covered by the three grounds prop:nohilbert actually argues.
hypotheses:
  - conformal matter with a2 > 0
  - the exact constant-H de Sitter fixed point
falsifier: >
  Either (i) show that Euclidean-regularity / analytic-continuation selection is
  itself structure the timelessness or no-background axiom forbids - genuinely
  open, not resolved by the pass that produced this; or (ii) show the construction
  is moot regardless, because the exact solution's provable instability means it
  is never the physically operative background.
consequence: >
  If it held, a covariant foliation-free two-point-function construction exists
  at one isolated point in solution space. Far narrower than "the obstruction
  does not bite at self-consistency loci" in general.
gate:
  status: blocked
  by: >
    Falsifier (ii) is INDEPENDENTLY FATAL as a physical claim and is unaffected by
    how (i) resolves. Even a total win on the state-construction question leaves
    this a statement about an idealised, never-realised fixed point - the exact
    eternal solution is unstable, with a quasi-de Sitter lifetime of order
    1e-42 to 1e-40 s.
novelty:
  status: novel
  searched: 2026-07-25
  found: []
  note: >
    Nothing found combines a no-fundamental-Hilbert-space objection with a
    self-consistent-fixed-point state construction. The Bunch-Davies vacuum
    itself is of course standard and not in question; the claim is about what
    constructing it AT a fixed point does to the background-dependence
    objection.
  pinamonti_siemssen_resolved: >
    The strongest candidate prior art, open through two prior passes, is now
    settled at full text - and the answer is a third structure neither pass
    anticipated. Their construction is NEITHER naively sequential NOR a joint
    two-variable Banach fixed point. A functional is fixed once, associating to
    every candidate trial metric a canonically determined state; the contraction
    then runs on a SINGLE variable. So "simultaneously" in their abstract means
    "one equation rather than alternating solves", not "joint product space over
    (state, metric) as independent unknowns".
    Decisively, that state is an ADIABATIC STATE OF ORDER ZERO, explicitly not
    Hadamard or Bunch-Davies, because Hadamard states cannot be defined on the
    non-smooth C1 trial metrics appearing as intermediate iterates.
  extension_structurally_excluded: >
    And the extension question is answered negatively for a reason stronger than
    "nobody has done it". Their renormalization constants are chosen
    SPECIFICALLY to cancel the higher-derivative anomaly term - the very term
    that drives the Starobinsky fixed point. Their existence theorem is proved in
    a regime that renormalizes away the mechanism this claim runs on. Their own
    de Sitter chapter is a different calculation: perturbative fluctuations on a
    Newtonianly-perturbed background, not a self-consistency argument, and not at
    the anomaly-exact point.
  unreached: >
    One adjacent lead was not reached: a Phys. Rev. D paper on fully
    self-consistent semiclassical gravity (also PhilSci-Archive 25780), paywalled
    with the archive mirror unreachable. At snippet level it reads as a
    dynamical, collapse-model self-consistency condition rather than a static
    eternal fixed point, and is not framed around the no-Hilbert-space question.
    Recorded as CHECKED AT SNIPPET LEVEL ONLY, not as clear.
  bibliographic_note: >
    arXiv:1503.01826 resolves to Siemssen's PhD thesis, not a standalone
    two-author preprint. The repository's `pinamonti_siemssen` key correctly
    cites the journal article, Commun. Math. Phys. 334, 171 (2015).
provenance: {born: 2026-07-25, born_by: adversary}
supersedes: ce-sj-at-fixed-point
promotion:
  from: speculation
  to: conjecture
  date: 2026-07-25
  gate: >
    All five conjecture criteria met. Falsifiable: two named routes, (i) showing
    Euclidean-regularity selection is itself forbidden structure, (ii) the
    instability. Novel: checked at source, see above. Consequential: it would
    narrow prop:nohilbert's obstruction to off-fixed-point formulations.
    Consistent: no contradiction with a live claim. Reachable: the first step is
    an axiom-level check on whether analytic continuation counts as background
    structure.
  caveat_carried_forward: >
    The instability gate is NOT resolved by promotion and is not a novelty
    question. Falsifier (ii) remains independently fatal to this as a claim about
    physically realised backgrounds - the exact fixed point has a lifetime of
    order 1e-42 s. Promotion records that this is a well-formed conjecture worth
    holding, not that it describes anything realised.
  provenance_note: >
    Worth stating precisely for the experiment's record: this conjecture was not
    produced by the generator. The generator proposed a Sorkin-Johnston version
    which was killed outright; the DEFENSE pass constructed this reframing while
    arguing against that death. The generative tier produced it, through its
    adversarial half rather than its generative half.
---

The reframing that survived [[ce-sj-at-fixed-point]]'s death. The vehicle was the
problem, not the thesis: the paper does not use Sorkin-Johnston at all - its map
text says de Sitter symmetry selects the conformal vacuum, obtained by conformal
transformation, which never runs the SJ eigenvalue problem on an unbounded
manifold and has none of its divergence pathology.

Why it plausibly evades prop:nohilbert's actual three grounds, read from the
proposition rather than from a summary: the Klein-Gordon inner product it is
built from is provably independent of the Cauchy surface for solutions, which is
the direct opposite of ground (1)'s stated mechanism; a GNS construction does not
itself invoke a unitary evolution operator, addressing ground (2); and no
measurement basis is chosen, addressing ground (3). **Recorded as the producing
pass's own logic check against the paper's text, explicitly not paper-grade.**

Better question this surfaced, grounded in citations this program already
verified paper-grade: has the Pinamonti-Siemssen joint (state, metric) Banach
construction - which solves simultaneously for the quantum state and the Hubble
function - been or can it be extended from the perturbative regime to the exact,
non-perturbative Starobinsky point, using the Euclidean vacuum as ansatz? Flagged
honestly as abstract-level only; whether "simultaneous" means non-sequential
per-step or only at the final fixed point was not established.
