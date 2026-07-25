---
id: ce-witness-obstruction
program: co-emergence
tier: sketch
status: live
statement: >
  At fixed magnitude spectrum on the M(theta) family, no scalar witness of the
  form W = sum over pairs of w(p_i, p_j) k(phase difference) - for ANY
  magnitude-only weight w and ANY single fixed univariate kernel k applied
  uniformly - is monotonically related to I_S in general. The obstruction is
  dimensional: I_S = S(Re rho) - S(rho) depends on two independent
  theta-dependent quantities per coherence entry, while any such W collapses to
  one.
object:
  name: single-kernel pairwise witnesses
  space: the one-parameter family rho_theta at fixed magnitude spectrum
hypotheses:
  - m_ij > 0 strictly
  - theta in [0, pi]
  - no alignment convention needed; all variants tested are gauge invariant
depends_on:
  - id: ce-quantumness-not-one-dimensional
    role: load-bearing
    transfers: cross-object
    justification: >
      That claim is about two specific witnesses, im_frac and I_S, and reports
      that they diverge. This is about a CLASS - every single-kernel pairwise
      aggregate - and asserts that all of them must. The generalisation is the
      content, so the edge is a genuine broadening rather than a restatement.
      What transfers is the two-degrees-of-freedom mechanism the parent's own
      O(N) versus O(N^2) analysis identified; what does not transfer is any
      claim about a particular witness.
falsifier: >
  A single-kernel pairwise witness of the stated form that is monotonically
  related to I_S across the mild and skewed ensembles. The sharp instance behind
  the claim: at dims (2,2), mild magnitudes, seed 32, the exact sign-faithful
  witness is strictly monotone across the whole interval while I_S is unimodal
  with an interior maximum.
consequence: >
  Rules out the entire natural family of reweighted or resigned im_frac-style
  aggregates, not merely the two witnesses actually tried, and says what to do
  instead: a genuinely two-parameter witness, not a fourth weighting.
novelty:
  status: unchecked
  note: >
    NOT YET CHECKED. Owed a prior-art pass. The parent claim's own sweep found
    that the general principle - distinct resource monotones need not order
    states alike - is established, with a no-finite-complete-set theorem naming
    imaginarity explicitly. This obstruction is sharper and more specific, but
    the relationship to that theorem needs establishing.
provenance: {born: 2026-07-25, born_by: adversary}
derivation: >
  I_S depends per entry on both the real part of the coherence and its modulus.
  The modulus is provably theta-dependent at min(d, d) = 2 via the entropy-excess
  result: purity is non-increasing, hence the coherence modulus is non-increasing,
  hence S(rho) is non-decreasing - confirmed numerically with zero monotonicity
  violations on every seed checked. A witness built from phase differences alone,
  whatever the kernel, recovers only one of the two.
  Empirically, across five weight and kernel combinations - including the exact
  sign-faithful witness matching the real part's off-diagonals to 1e-16 - nothing
  clears 0.99 in aggregate, and the sign-faithful same-row variant is the worst
  performer in the skewed regime.
gaps:
  - >
    The entropy-excess monotonicity this leans on is proved only at
    min(d, d) = 2; general rank needs separate treatment, and the general-rank
    entropy excess was already retracted once.
  - >
    Genericity is established by one sharp instance plus an ensemble pattern, not
    by showing the mismatch occurs on an open set of magnitude spectra.
---

Supersedes the open question left by [[ce-quantumness-not-one-dimensional]] and
explains [[ce-imfrac-determines-interference]] and [[ce-allpairs-witness]] as one
mechanism rather than two accidents.
