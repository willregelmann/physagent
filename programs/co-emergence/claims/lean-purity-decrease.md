---
id: lean-purity-decrease
program: co-emergence
kind: formal
tier: rigorous
status: live
statement: >
  purity_decrease (hm : forall i j, 0 <= m i j) : purity m L theta <= purity m L 0
formal:
  decl: CoEmergence.purity_decrease
  toolchain: leanprover/lean4:v4.31.0
  mathlib: v4.31.0
  axioms: [propext, Classical.choice, Quot.sound]
  sorry_free: true
bridge:
  to: ce-entropy-excess
  claim: >
    Lean's `rho m L theta` is the paper's M(theta)^dag M(theta), and
    `trace_rho_sq` certifies that the formalized quantity sum_jk |rho_jk|^2 is
    indeed Tr(rho^2), using Hermiticity of rho. The bridge from the Lean
    statement to the paper's matrix claim is itself formalized.
  reviewed: null
discharges: [ce-entropy-excess]
falsifier: a counterexample to the formal statement, or a failing build
consequence: part (a) of the entropy excess is mechanically discharged
novelty: {status: unchecked}
provenance: {born: 2026-07-05, born_by: worker}
---

Part (a) of the entropy excess, formalized in full: purity decrease for all
ranks, via Fact 3 and the entrywise modulus bound.

**`last_built` is deliberately absent.** No CI job in this repository runs
`lake build`, and none ever has - `grep -rln 'lean\|lake' .github/workflows/`
returns nothing. The `#print axioms` audit recorded in the paper's
`rem:lean_entropy_excess` is a prose assertion about a machine check that no
machine has re-run since it was written. Lint L10 fires on this node and should
keep firing until the CI job exists. That is the correct state of the record,
not a bookkeeping oversight.

`bridge.reviewed` is likewise null: the formal-to-informal correspondence has
never been adversarially reviewed as such.
