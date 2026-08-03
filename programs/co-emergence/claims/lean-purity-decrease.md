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
  last_built: {at: 2026-08-03, by: ci, result: pass}
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
novelty:
  status: novel
  searched: 2026-07-24
  found: []
  note: >
    Novel as a formalized artifact. The checker read the Lean proof term
    line by line: it is built from general Mathlib API (Finset.sum_nonneg,
    norm_sum_le, Complex.norm_exp_ofReal_mul_I) plus a per-term triangle
    inequality, and invokes NO purity- or dephasing-specific Mathlib lemma
    -- so this is not re-proving something already available. Mathematically
    the underlying principle, that phase-randomizing and unital channels do
    not increase purity, is textbook; the rank-general entrywise-phase
    Gram-matrix formulation was not found stated this way.
provenance: {born: 2026-07-05, born_by: worker}
---

Part (a) of the entropy excess, formalized in full: purity decrease for all
ranks, via Fact 3 and the entrywise modulus bound.

**`last_built` is absent until CI writes it.** When this node was created there
was no job running `lake build` at all: the `#print axioms` audit recorded in the
paper's `rem:lean_entropy_excess` was a prose assertion about a machine check no
machine had re-run since it was written.

`lean.yml` now exists, builds against a pinned toolchain, asserts no `sorry`, and
verifies the axiom set against declarations generated from this graph. Its
scheduled run writes the result back here via `claim_graph.py record-build`, so
this field records something a machine actually did rather than something a
human asserted. Until that run lands, L10 fires on this node - correctly.

`bridge.reviewed` is likewise null: the formal-to-informal correspondence has
never been adversarially reviewed as such.
