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
novelty:
  status: independent-rederivation
  searched: 2026-07-24
  found: []
  note: >
    SPLIT VERDICT. The general principle is established prior art and MUST
    be cited: distinct resource monotones routinely order states differently
    (Baumgratz, Cramer & Plenio, PRL 113, 140401 (2014)), and more sharply,
    arXiv:2212.02473 proves no finite complete set of monotones exists for
    any resource theory with free pure states, naming imaginarity
    explicitly. That subsumes the qualitative form of this claim. The
    specific technical content -- the O(N) reference-relative first moment
    versus the O(N^2) pairwise-coherence Gram structure, the explicit
    witness, the theta-versus-theta^2 scaling, and the restricted result
    below theta* -- was not found anywhere and is a genuine contribution
    layered on an expected phenomenon. Caveat: one candidate paper
    (arXiv:2506.09799) would not extract and is unverified rather than
    checked-clean.
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
restricted_positive_result:
  status: RETRACTED as evidence, 2026-07-25
  claim_as_recorded: >
    Below theta* = min(first turning point of im_frac, first turning point of
    I_S), Spearman rank correlation is 1.000000 in all 120 of 120 configurations
    tested.
  correction: >
    This was recorded as "true but of limited practical use". It is worse than
    impractical - it is CONTENT-FREE AS EVIDENCE, and was presented here as a
    positive result. theta* is DEFINED as the minimum of the two turning points,
    so both series are individually monotone on [0, theta*] by construction, and
    any two individually monotone functions of a shared variable have Spearman
    exactly +/-1 whether or not they are related at all. It would hold equally for
    two entirely unrelated monotone curves. Nobody should treat theta*-restriction
    as validating a witness choice.
  found_by: >
    The adversarial defense pass on ce-allpairs-witness, scoping beyond its own
    assignment.
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
