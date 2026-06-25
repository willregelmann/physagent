# Lean4 formalization — co-emergence

Machine-checked proofs for the **load-bearing inequalities** of the
phase-induced entropy-excess lemma (`lem:entropy_excess`, §"Phase-induced
entropy excess" of `../index.tex`). Tracks issue #45 (milestone **CE-5**) and
encodes the **corrected** statement of issue #76.

## What is proved

All statements live in `CoEmergence/EntropyExcess.lean`, namespace
`CoEmergence`. The Gram (reduced density) matrix is, with row index `i`
summed and `j,k` the Gram indices,

```
ρ(θ)_{jk} = ∑_i m_{ij} m_{ik} · exp(i θ (log m_{ik} − log m_{ij})),
```

where the magnitudes satisfy `m i j ≥ 0` and `L i j` plays the role of
`log m_{ij}` (left abstract — so part (a) holds for the phase-locked fixed
point and, more generally, for any real phase profile).

| Theorem | Paper claim |
|---|---|
| `purity_decrease` | **Lemma (a), all ranks:** `Tr(ρ(θ)²) ≤ Tr(ρ(0)²)` for every `θ`, given `m ≥ 0`. |
| `trace_rho_sq` | Certifies the formalized purity `∑_{jk}\|ρ_{jk}\|²` **is** `Tr(ρ²)` (via `rho_hermitian`, ρ Hermitian). |
| `norm_rho_le` | **Fact 3** (entrywise Gram contraction): `\|ρ(θ)_{jk}\| ≤ ρ(0)_{jk}`. |
| `rank2_entropy_excess`, `rank2_entropy_excess_of_sv` | **Lemma (b), rank 2:** `S(θ) ≥ S(0)`. |

Part (b) reduces the entropy excess to the monotonicity of the binary entropy
(`Real.binEntropy_strictAntiOn` on `[½,1]`) applied to the top squared singular
value `σ₁(θ)² ∈ [½, σ₁²]`.

### The one unproven dependency (explicit, not assumed silently)

Part (b) takes **Fact 2** — the top singular value decreases,
`σ₁(θ) ≤ σ₁` (Perron–Frobenius) — as an *explicit hypothesis*
(`hfact2 : pθ ≤ p0`, resp. `aθ ≤ a0`). It is not proved here; the paper proves
it analytically (Fact 2 in the proof of `lem:entropy_excess`). Formalizing the
Perron–Frobenius step is the documented stretch goal of #45.

### Deliberately out of scope

The **general-rank** von Neumann excess `S(θ) ≥ S(0)` is **known false** (paper
Remark `rem:vn_general_rank`, with an explicit counterexample). It is not
formalized. The equality/strictness characterization at full
necessary-and-sufficient strength (including θ-resonances) is open issue #76;
this artifact formalizes only the inequalities and the trivial separable
equality direction, never the retracted "all entries equal" `iff`.

## Build (the verification artifact)

```bash
elan toolchain install $(cat lean-toolchain)   # leanprover/lean4:v4.31.0
lake exe cache get                             # prebuilt Mathlib oleans (no source compile)
lake build                                     # ⇒ "Build completed successfully"
```

A green `lake build` is the verification artifact. Dependency revisions are
pinned in `lake-manifest.json` (Mathlib `v4.31.0`).

**Axiom audit.** `#print axioms` on `purity_decrease`, `trace_rho_sq`,
`rank2_entropy_excess_of_sv` reports only `[propext, Classical.choice,
Quot.sound]` — the standard Mathlib axioms, **no `sorryAx`**. The proofs
contain no `sorry`, `admit`, or `native_decide`.

## CI status

Wiring `lake build` into the merge-gate stack requires a `.github/workflows/`
file — a **protected path** the machine account's PAT cannot author (it lacks
the `workflow` scope; see `AUTONOMY.md`). The CI job is therefore an
experimenter-approval follow-up; until then the green local build above is the
artifact. The build was reproduced from a clean checkout at the SHA of this
PR's branch.
