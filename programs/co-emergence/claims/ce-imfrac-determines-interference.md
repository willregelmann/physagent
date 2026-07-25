---
id: ce-imfrac-determines-interference
program: co-emergence
tier: speculation
status: dead
statement: >
  At fixed magnitude spectrum, the interference metric I_S is a strictly
  monotonically increasing function of the imaginary fraction - the two
  quantumness order parameters carry no independent information.
hypotheses:
  - m_ij > 0 strictly
  - max-magnitude alignment convention
  - theta in [0, pi]
falsifier: >
  Scan theta at fixed magnitudes; find derivative-sign disagreement, or two
  theta values with equal im_frac and distinct I_S.
consequence: >
  Would have licensed replacing the diagonalization-based I_S with the
  closed-form im_frac wherever quantumness is tracked.
provenance: {born: 2026-07-24, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-24
  cause: >
    Two independent counterexample mechanisms, both computed against the
    repository's own code. The two quantities have interior turning points at
    different theta, giving pairs where im_frac agrees to 6 significant figures
    while I_S differs by 61% relative. And the failure appears at dims (2,2) with
    magnitudes matching the paper's own h ~ U[0.5,1.5] - which is precisely the
    rank case where ce-entropy-excess part (b) is rigorously proven.
  defense_attempted: yes
  defense_findings: >
    The defense swept 120 configurations and found no skew threshold: im_frac's
    own turning-point onset jumps from 0/12 at a spread ratio of ~1.6x to 9/12 at
    ~2.7x, and the paper's own spread (~3-5x) sits just past that onset. Blanket
    rank correlation is unreliable (mean Spearman 0.893, minimum -0.138). One
    restricted claim does survive - below theta* = min of the two turning points,
    Spearman is 1.000000 in all 120/120 configurations - but the defense then
    dismantled its own rescue: I_S can turn before im_frac, so im_frac's closed
    form is not a sufficient certificate of being inside the safe zone, and
    determining theta* requires exactly the expensive computation the claim
    existed to avoid. It also checked interference_hs on its own initiative and
    found it marginally worse, not better.
---

Killed as stated, but the negative result was characterized rather than merely
reported, and is now recorded as [[ce-quantumness-not-one-dimensional]].

A new question fell out of the analysis and is worth a future speculation: is
the all-pairs Born-weighted mean of sin^2 the natural O(N^2) extension of
im_frac, and does it track I_S where im_frac does not?
