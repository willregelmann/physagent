---
id: lean-rank2-entropy-excess
program: co-emergence
kind: formal
tier: rigorous
status: live
statement: >
  rank2_entropy_excess : p_theta <= p_0 on [1/2, 1] implies
  Srank2(p_theta) >= Srank2(p_0) - binary-entropy monotonicity.
formal:
  decl: CoEmergence.rank2_entropy_excess
  toolchain: leanprover/lean4:v4.31.0
  mathlib: v4.31.0
  axioms: [propext, Classical.choice, Quot.sound]
  sorry_free: true
bridge:
  to: ce-entropy-excess
  claim: >
    The scalar lemma is connected to the paper's matrix claim by three
    structural links that are SUPPLIED AS HYPOTHESES and not re-derived in Lean:
    (i) the eigenvalue identification, (ii) the entropy connection
    S(rho) = Srank2(sigma_1^2), and (iii) Fact 2, sigma_1(theta) <= sigma_1,
    proved analytically in the paper. The formal content is the scalar step only.
  reviewed: null
discharges: []
falsifier: a counterexample to binary-entropy monotonicity, or a failing build
consequence: >
  Part (b) is machine-checked at the level of its key scalar step - which is not
  the same as part (b) being machine-checked.
novelty:
  status: prior-art
  searched: 2026-07-24
  found: []
  note: >
    CONFIRMED HIT, and the one predicted as cheapest. The proof directly
    calls Real.binEntropy_strictAntiOn : StrictAntiOn binEntropy (Set.Icc 2
    inverse 1), which already exists in Mathlib's
    Mathlib.Analysis.SpecialFunctions.BinaryEntropy -- the exact lemma,
    signature matched against Mathlib's own docs. Mathlib also carries
    binEntropy_strictMonoOn and strictConcave_binEntropy, so its coverage of
    this use case is essentially complete. The mathematically load-bearing
    content is therefore imported, not independently proved; this theorem is
    a thin wrapper adding interval side conditions, the equality case, and
    the paper's variable names. That is worth stating plainly on the node,
    since 'formalized in Lean' reads as stronger than it is here.
provenance: {born: 2026-07-05, born_by: worker}
---

**This node is the reason `mechanical_coverage` counts edges rather than
files.** `discharges` is deliberately empty: the Lean theorem proves a scalar
implication, and the three structural links to the paper's matrix claim are
assumed. A formalization that assumes its way to the conclusion discharges
nothing, however confidently its frontmatter is written.

The paper's own remark states this honestly in prose. Encoding it means the
accounting is computed instead of narrated - part (a) at 100% coverage, part (b)
at 0% until the three links are formalized or given their own nodes.

Recorded for the record: the general-rank entropy excess is **not** formalized
because it is **false**, and was retracted. That retraction came out of an
attempted formalization - the highest-value thing Lean has done in this
repository, and it was a killing, not a verification.

**`last_built` is absent until CI writes it.** `lean.yml`'s scheduled run
populates this field via `claim_graph.py record-build`, so it records a build a
machine performed rather than an assertion a human made. L10 fires until then,
correctly. Note that a passing build would not change this node's accounting
anyway: `discharges` is empty, so its mechanical coverage contribution is zero
whether or not the build is green.
