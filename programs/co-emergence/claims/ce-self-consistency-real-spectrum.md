---
id: ce-self-consistency-real-spectrum
program: co-emergence
tier: sketch
status: live
statement: >
  The Jacobian of the self-consistency map has real spectrum at every point of
  its domain, not only at fixed points. Consequently only fold and flip
  bifurcations are structurally possible for this class of maps, and
  Neimark-Sacker (quasi-periodic / invariant-torus) bifurcation is excluded
  outright.
object:
  name: DG
  definition: "DG(q) = J_softmax(z(q)) . M, with J_softmax = diag(p) - p p^T and M = 2 gamma (beta I + A)"
  space: tangent space of the probability simplex
hypotheses:
  - gamma real
  - the marginal-coupling matrix A is symmetric
  - the map has the softmax form induced by the self-consistency weight
falsifier: >
  A complex eigenvalue pair of DG at any point of the domain under the stated
  hypotheses, or an observed quasi-periodic / invariant-torus bifurcation in a
  map of this class.
consequence: >
  Constrains the bifurcation structure of every self-consistency map in this
  family. Non-convergence of the fixed-point iteration can only ever be a fold
  or a period-doubling cascade - never quasi-periodic wandering - so
  iteration-failure diagnostics can be read unambiguously.
novelty:
  status: independent-rederivation
  searched: 2026-07-24
  found: []
  note: >
    SPLIT VERDICT. Part A -- SPD times symmetric is similar to a symmetric
    matrix, hence real spectrum -- is the classical symmetric-definite
    generalized eigenvalue problem, textbook material (Golub & Van Loan,
    Matrix Computations, sec. 8.7; also via congruence in Horn & Johnson).
    No new content; one citation closes it. Part B -- Neimark-Sacker
    structurally excluded for this map class -- was not found stated
    anywhere. Wang (arXiv:2605.15651) analyses this exact Jacobian but never
    discusses bifurcation taxonomy, and explicitly works in a general-W
    setting where the symmetry this claim relies on does not hold. Harris,
    McCallum & Harre, Games and Economic Behavior 157, 535 (2026) do
    bifurcation analysis of logit QRE, but via catastrophe theory on the
    equilibrium correspondence -- a static concept, a different object from
    dynamic stability bifurcations of the iteration map. Caveat recorded
    honestly by the checker: once Part A is granted, 'real spectrum implies
    no NS' is near-immediate by the definition of NS, so Part B's novelty is
    the explicit packaging, not new dynamical-systems mathematics. Also
    caveat: the closest paper was paywalled and only its abstract was read.
provenance: {born: 2026-07-24, born_by: adversary}
derivation: >
  J_softmax is symmetric and positive definite on the tangent hyperplane (its
  kernel is exactly the constant direction). M is symmetric because A is a
  symmetric 0/1 matrix. Hence on the tangent space DG is similar to the
  symmetric matrix J^(1/2) M J^(1/2), which has real spectrum. Verified
  numerically at max |Im(eigenvalue)| = 9.4e-12 across 640 trials spanning
  beta in [0.1, 500] and gamma in [-5, -0.5] at random q.
gaps:
  - >
    The tangent-space argument was verified numerically rather than written out
    formally in the reduced coordinates the scripts use, rather than the ambient
    coordinates where the derivation is clean. Closing this is the one step from
    Sketch to Rigorous.
  - >
    Hypotheses are stated for the N=4 toy instantiation. The general
    N-subsystem case needs stating.
---

Produced by the adversarial investigation of [[ce-toy-fixed-point-multiplicity]],
which was itself false. The core argument is complete and gap-free for the
stated hypotheses; only the coordinate bookkeeping is outstanding.

**Prior art not yet checked.** "Symmetric PSD times symmetric has real spectrum"
is a generic linear-algebra fact and this may be known in the discrete-dynamics
or nonlinear Perron-Frobenius literature. Lint L5 fires on this node until
checked, correctly - see [[ce-quantumness-not-one-dimensional]] for the same
status.
