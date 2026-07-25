---
id: ce-imfrac-exact-reduction
program: co-emergence
tier: rigorous
status: live
statement: >
  The imaginary fraction of the self-consistent fixed point admits an exact
  reduction to the magnitude spectrum: im_frac^2 = sum_sigma p_sigma
  sin^2((theta/2) log(p_r / p_sigma)), under max-magnitude alignment.
object:
  name: im_frac
  space: fixed points of F in C^N
hypotheses:
  - psi* is a fixed point of F
  - gamma = -1 + i theta
  - the reference component r is chosen by maximum magnitude
falsifier: >
  A fixed point where the direct computation and the closed form disagree
  beyond machine precision.
consequence: >
  The imaginary fraction is set by N, the spread of h, and the alignment
  convention - not by subsystem rank, retiring the earlier rank-dependence
  reading.
novelty:
  status: novel
  searched: 2026-07-24
  found: []
  note: >
    Nothing found. The construction depends on this framework's own
    fixed-point form, so an outside paper would have to already be working
    with the same self-consistency map. Adjacent fields checked and ruled
    out: circular statistics / Kuramoto order parameter, whose superficially
    similar sin^2 identities do not carry the reference-alignment convention
    or the fixed-point tie.
tex: {file: programs/co-emergence/index.tex, label: sec:toy_model}
provenance: {born: 2026-06-18, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Re-derived from scratch and matched term for term. Independently verified by
    running the repository suite: 20/20 assertions of machine-precision agreement
    across 6 shapes and 2 seeds, plus 113 co-emergence tests passing. Scope
    checked: the closed form is claimed only for max-magnitude alignment, and the
    "optimal" alignment genuinely uses a different phase convention that the paper
    does not claim the formula covers. No overclaim.
---
