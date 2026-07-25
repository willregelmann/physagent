---
id: ce-quantumness-not-one-dimensional
program: co-emergence
tier: sketch
status: live
statement: >
  The imaginary fraction and the interference metric are genuinely independent
  order parameters once phase spread is O(1). im_frac is an O(N) quantity - a
  Born-weighted first moment of phase against a single reference component -
  while I_S is sensitive to the full O(N^2) Gram matrix of pairwise Born-weighted
  coherences. They coincide only at leading order in theta, where I_S is
  proportional to im_frac squared.
object:
  name: (im_frac, I_S)
  space: the one-parameter family rho_theta at fixed magnitude spectrum
hypotheses:
  - m_ij > 0 strictly
  - max-magnitude alignment convention
depends_on:
  - id: ce-imfrac-exact-reduction
    role: load-bearing
    transfers: cross-object
    justification: >
      That claim establishes the closed form for im_frac on fixed points of F in
      C^N; this claim evaluates im_frac on the M(theta) family at fixed magnitude
      spectrum, which is a different object. The transfer was checked, not
      assumed: im_frac's closed form is purely kinematic and does NOT require
      psi to be a self-consistent fixed point - it is an identity for any vector
      of the form psi_sigma proportional to m_sigma exp(i theta log m_sigma).
      Verified numerically to 1e-16 across ~30 configurations.
  - id: ce-interference-metric
    role: load-bearing
    transfers: cross-object
    justification: >
      That claim establishes I_S on general density matrices on C^d; here it is
      evaluated on rho_theta specifically. The transfer holds because
      vec(M(theta)) is a bipartite pure state whose partial trace is exactly
      rho_theta = M(theta)^dag M(theta) - verified numerically against the
      repository's own partial_trace implementation. So both quantities are
      honestly computable on one common family, which is what makes comparing
      them meaningful at all.
falsifier: >
  A demonstration that I_S is a function of im_frac alone at fixed magnitude
  spectrum, or a rank-order violation below theta* (none found in 120 trials).
consequence: >
  "How quantum" a configuration is is not a scalar beyond the small-theta
  regime. Any argument treating the two witnesses as interchangeable is invalid
  in the regime the toy model actually operates in.
novelty: {status: unchecked}
provenance: {born: 2026-07-24, born_by: adversary}
derivation: >
  Explicit witness at fixed magnitude spectrum: two theta values where im_frac
  agrees to 6 significant figures, the all-pairs Born-weighted mean of sin^2
  differs by 17%, and I_S differs by 61% - amplified beyond the underlying 17%
  because entropy is concave in the spectrum. Two phase patterns can agree on
  every reference-relative angle while disagreeing on the non-reference pairwise
  angles, and im_frac is blind to those by construction. Consistent with the
  repository's own small-theta facts: I_S goes as theta^2 while im_frac goes as
  theta.
restricted_positive_result: >
  Below theta* = min(first turning point of im_frac, first turning point of I_S),
  Spearman rank correlation is 1.000000 in all 120 of 120 configurations tested.
  This is true but of limited practical use: I_S can turn first, so im_frac's
  closed form is not a sufficient certificate of being inside the safe zone, and
  determining theta* requires the expensive computation the proxy existed to
  avoid.
gaps:
  - >
    The O(N) versus O(N^2) characterization rests on one explicit witness plus a
    120-configuration ensemble, not a proof.
  - >
    Large-N asymptotics unresolved: turning-point rates fall from 60% at N=4 to
    15% at N=25, but whether that limits to zero or saturates is unknown.
---

Produced by killing [[ce-imfrac-determines-interference]].

Open question this raises, worth a future speculation: is the all-pairs
Born-weighted mean of sin^2 the natural O(N^2) extension of im_frac, and does it
track I_S where im_frac does not? It has a closed form candidate and was not
pursued.
