---
id: ce-allpairs-witness
program: co-emergence
tier: speculation
status: dead
statement: >
  At fixed magnitude spectrum, I_S is a strictly monotonically increasing
  function of the all-pairs Born-weighted mean of sin^2 of the half-log-ratio
  phase differences - the O(N^2) extension of im_frac's O(N) reference-anchored
  construction.
hypotheses:
  - m_ij > 0 strictly
  - theta in [0, pi]
falsifier: >
  Any theta pair with matching Q but differing I_S rank order, or a derivative
  sign disagreement.
consequence: >
  Would close the practical gap left open by ce-quantumness-not-one-dimensional.
provenance: {born: 2026-07-25, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-25
  cause: >
    A counterexample sharper than the one that killed its O(N) predecessor: Q
    agrees to NINE significant figures while I_S differs by 1041% relative
    (against six figures and 61% last time). And Q's own turning point sits
    essentially on im_frac's, not on I_S's - it inherited exactly the blind spot
    it was built to fix. Ensemble Spearman is statistically indistinguishable
    from im_frac's in the mild regime and markedly worse in the skewed one.
  defense_attempted: yes
  defense_findings: >
    The defense refuted the brief's hypothesis. The brief argued the fix was
    SIGN SENSITIVITY, since Q sees phases only through sin^2 and is blind to the
    sign of the coherences while I_S is not. The defense built the exact
    sign-faithful witness - matching the real part's off-diagonals to 1e-16, and
    catching that the naive all-pairs sum is simply wrong for d1 > 1 because it
    includes index pairs that never appear in the density matrix - and showed it
    STILL fails, qualitatively: at one configuration the witness is strictly
    monotone across the whole interval while I_S is unimodal. Monotone versus
    unimodal is not a numerical near-miss. Across five weight/kernel
    combinations, nothing clears 0.99, and the "obviously correct" variant is the
    WORST in the skewed regime.
---

Killed, and superseded by a better claim - see [[ce-witness-obstruction]], which
explains why im_frac and Q both failed by ONE mechanism rather than as two
independent accidents.

One structural property is worth keeping regardless: Q is alignment-independent,
verified to 1e-16, with no reference component and invariant under global phase
rotation. That is a genuine improvement over im_frac and survives the
monotonicity kill intact.
