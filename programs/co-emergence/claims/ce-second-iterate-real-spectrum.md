---
id: ce-second-iterate-real-spectrum
program: co-emergence
tier: sketch
status: live
statement: >
  The Jacobian of the SECOND iterate of the self-consistency map has real
  spectrum at every point of the domain, by the same congruence mechanism as the
  first-iterate result extended one level. Consequently the second iterate can
  also only fold or flip, never undergo Neimark-Sacker. Crucially the mechanism
  does NOT extend to third or higher iterates, which explains why the observed
  period-doubling stops at 2 rather than cascading.
object:
  name: D(G o G)
  definition: "D(G o G)(a) = S(e) M S(b) M, with S(p) = diag(p) - p p^T, b = G(a), e = G(b)"
  space: tangent space of the probability simplex
hypotheses:
  - gamma real
  - the marginal-coupling matrix A symmetric
  - the softmax form induced by the self-consistency weight
depends_on:
  - id: ce-self-consistency-real-spectrum
    role: load-bearing
    transfers: cross-object
    justification: >
      Genuinely a different object - that claim is about DG, the first iterate's
      Jacobian; this is about D(G o G), the second's. The transfer is not the
      result but the MECHANISM: the same congruence by S^(1/2) that makes DG
      similar to a symmetric matrix also works one level up, because the inner
      S-factor sequence is a one-element palindrome at k = 2. That is exactly why
      the claim has content - the mechanism extends to the second iterate and
      provably breaks at the third, where the S-factors would have to commute.
      Declaring this same-object would hide the very step being asserted.
falsifier: >
  A complex eigenvalue pair of D(G o G) at any interior point under the stated
  hypotheses; or an observed period-4 orbit born by any route other than a real
  eigenvalue crossing -1.
consequence: >
  Explains, rather than merely observes, why the period caps at 2. There was
  never a structural reason to expect Feigenbaum universality here: the algebraic
  protection that keeps the first doubling clean provably does not recur at the
  second. Any new period-2 orbit must be born by fold, matching what is observed.
novelty:
  status: unchecked
  note: >
    NOT YET CHECKED. A prior-art pass is owed before this is relied on. The
    parent first-iterate result was found to be classical in part (the
    symmetric-definite generalized eigenvalue problem) and novel only in its
    bifurcation-theoretic packaging; this extension needs the same treatment,
    including the k >= 3 breakdown argument.
provenance: {born: 2026-07-25, born_by: adversary}
derivation: >
  Conjugating by S(e)^(-1/2), well defined because S(e) is positive definite on
  the tangent hyperplane whenever e is interior, which G always guarantees, gives
  Z = S(e)^(1/2) M S(b) M S(e)^(1/2) - a palindrome of self-transpose factors,
  hence manifestly symmetric, hence real spectrum by similarity. Verified three
  independent ways to machine precision (max mismatch 1.03e-12, all imaginary
  parts below 1e-16): the analytic formula, a finite-difference Jacobian, and the
  explicit symmetric conjugation, at random interior points across beta in
  [0.1, 160] and gamma in [-5, -0.5].
  The k >= 3 breakdown: the conjugation produces a symmetric matrix only when the
  inner sequence of S-factors is a palindrome under reversal. That is automatic
  for k = 1 (empty) and k = 2 (one element), but for k >= 3 requires the S(q_i)
  to commute, which they generically do not. Confirmed numerically: real spectrum
  at k = 1, 2 (imaginary parts below 1e-18) and clearly complex at k = 3 to 6
  (imaginary parts up to 3e8 at beta = 40).
gaps:
  - >
    Verified numerically in reduced coordinates; the ambient-coordinate write-up
    for general N is the remaining step - the identical gap the parent claim
    carries.
  - >
    The k >= 3 breakdown rests on "generically" plus a numerical witness rather
    than a proof that non-commutativity of the S-factors holds at generic points.
  - >
    Does not explain WHY the second-iterate spectral radius decays to ~0.037
    rather than merely staying below 1. A Rayleigh-quotient bound was attempted
    and diverges - see the failed-routes record on ce-riem-classical-unique.
empirical_support: >
  Period exactly 1 or 2, never higher, across 10 distinct instances up to N = 16
  and beta up to 2e5, in more than 2200 total solves. Zero exceptions.
---

Produced by the adversarial investigation of [[ce-feigenbaum-cascade]], which
claimed a cascade and was false. The defense pass explicitly declined to promote
this beyond Sketch, noting that promotion is the prover's ladder rather than the
steelman's job.
