/-
Copyright (c) 2026 Will Regelmann, Claude (Anthropic). All rights reserved.
Released under the project's terms; see the repository root.

# Phase-induced purity decrease and entropy excess (co-emergence, Lemma `lem:entropy_excess`)

Machine-checked formalization of the load-bearing inequalities of the
phase-induced entropy-excess lemma in `programs/co-emergence/index.tex`
(§ "Phase-induced entropy excess"). Tracks issue #45 (milestone CE-5);
encodes the **corrected** statement of issue #76 (inequalities, with the
equality case only in its trivial separable direction — NOT the retracted
"all entries equal" `iff`).

The fixed point carries magnitudes `m i j ≥ 0` and phases locked to them,
`φ = θ·log m`. With the row index `i` summed and `j,k` the Gram indices,
the reduced density (Gram) matrix is

  ρ(θ)_{jk} = ∑_i m_{ij} m_{ik} · exp(i θ (log m_{ik} − log m_{ij})).

Here the phase `L i j` plays the role of `log m_{ij}`; it is left abstract,
so the purity result holds for the locked phases of the fixed point and, more
generally, for any real phase profile.

Results:
* `purity_decrease` — **Lemma (a), all ranks.** Tr(ρ(θ)²) ≤ Tr(ρ(0)²).
* `trace_rho_sq`    — certifies the formalized purity ∑_{jk}|ρ_{jk}|² IS Tr(ρ²)
                      (uses Hermiticity `rho_hermitian`).
* `rank2_entropy_excess` / `rank2_entropy_excess_of_sv` — **Lemma (b), rank 2.**
  S(θ) ≥ S(0), with Fact 2 (top singular value decreases, Perron–Frobenius)
  supplied as an explicit hypothesis — the single unproven dependency.

The general-rank von Neumann excess is known FALSE (paper Remark
`rem:vn_general_rank`) and is deliberately not formalized.
-/
import Mathlib

namespace CoEmergence

open Finset Complex Real

/-! ## Part (a): purity decrease, all ranks -/

variable {I J : Type*} [Fintype I]
variable (m : I → J → ℝ) (L : I → J → ℝ) (θ : ℝ)

/-- Real phase of term `i` in Gram entry `(j,k)`: `θ (L_{ik} − L_{ij})`
    (with `L = log m` this is `θ (log m_{ik} − log m_{ij})`). -/
def phase (i : I) (j k : J) : ℝ := θ * (L i k - L i j)

/-- Gram (reduced density) matrix entry
    `ρ(θ)_{jk} = ∑_i m_{ij} m_{ik} · exp(i · phase)`. -/
noncomputable def rho (j k : J) : ℂ :=
  ∑ i, (m i j * m i k : ℂ) * Complex.exp ((phase L θ i j k : ℂ) * Complex.I)

/-- The `θ = 0` Gram entry, as a real number: `ρ(0)_{jk} = ∑_i m_{ij} m_{ik} ≥ 0`. -/
def g (j k : J) : ℝ := ∑ i, m i j * m i k

lemma rho_zero (j k : J) : rho m L 0 j k = (g m j k : ℂ) := by
  simp only [rho, g, phase, zero_mul, Complex.ofReal_zero]
  push_cast; simp

lemma g_nonneg (hm : ∀ i j, 0 ≤ m i j) (j k : J) : 0 ≤ g m j k :=
  Finset.sum_nonneg fun i _ => mul_nonneg (hm i j) (hm i k)

/-- **Fact 3 (entrywise Gram contraction).** `|ρ(θ)_{jk}| ≤ ρ(0)_{jk}` for `m ≥ 0`,
    by the triangle inequality (each term has modulus `m_{ij} m_{ik}`). -/
lemma norm_rho_le (hm : ∀ i j, 0 ≤ m i j) (j k : J) :
    ‖rho m L θ j k‖ ≤ g m j k := by
  calc ‖rho m L θ j k‖
      ≤ ∑ i, ‖(m i j * m i k : ℂ) * Complex.exp ((phase L θ i j k : ℂ) * Complex.I)‖ :=
        norm_sum_le _ _
    _ = ∑ i, m i j * m i k := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, ← Complex.ofReal_mul,
          Complex.norm_real, Real.norm_of_nonneg (mul_nonneg (hm i j) (hm i k))]
    _ = g m j k := rfl

/-- `ρ(θ)` is Hermitian: `ρ(θ)_{kj} = conj ρ(θ)_{jk}`. -/
lemma rho_hermitian (j k : J) : rho m L θ k j = (starRingEnd ℂ) (rho m L θ j k) := by
  simp only [rho, map_sum, map_mul, ← Complex.exp_conj, Complex.conj_ofReal, Complex.conj_I]
  refine Finset.sum_congr rfl fun i _ => ?_
  have hph : (↑(phase L θ i k j) : ℂ) * Complex.I = ↑(phase L θ i j k) * -Complex.I := by
    rw [phase, phase]; push_cast; ring
  rw [hph]; ring

variable [Fintype J]

/-- Rényi-2 purity `Tr(ρ(θ)²) = ∑_{jk} |ρ(θ)_{jk}|²`. -/
noncomputable def purity : ℝ := ∑ j, ∑ k, ‖rho m L θ j k‖ ^ 2

/-- Certifies that `purity` is genuinely the trace of `ρ²`:
    `∑_{jk} ρ_{jk} ρ_{kj} = ∑_{jk} |ρ_{jk}|²` (using Hermiticity). The left side
    is `Tr(ρ²) = ∑_j (ρ²)_{jj}`. -/
lemma trace_rho_sq :
    (∑ j, ∑ k, rho m L θ j k * rho m L θ k j) = ((purity m L θ : ℝ) : ℂ) := by
  simp only [purity]
  push_cast
  refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun k _ => ?_
  rw [show rho m L θ k j = (starRingEnd ℂ) (rho m L θ j k) from rho_hermitian m L θ j k,
    Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.ofReal_pow]

/-- **Lemma (a), all ranks.** The purity decreases under the phase map:
    `Tr(ρ(θ)²) ≤ Tr(ρ(0)²)` for every `θ`, whenever `m ≥ 0`. -/
theorem purity_decrease (hm : ∀ i j, 0 ≤ m i j) : purity m L θ ≤ purity m L 0 := by
  simp only [purity]
  refine Finset.sum_le_sum fun j _ => Finset.sum_le_sum fun k _ => ?_
  have h0 : ‖rho m L 0 j k‖ = g m j k := by
    rw [rho_zero, Complex.norm_real, Real.norm_of_nonneg (g_nonneg m hm j k)]
  rw [h0]
  gcongr
  exact norm_rho_le m L θ hm j k

/-! ## Part (b): von Neumann entropy excess, rank 2 -/

/-- Rank-2 von Neumann entropy as a function of the top squared singular value `p`
    (eigenvalues `p`, `1 - p`): `S = -p log p - (1-p) log(1-p)`. -/
noncomputable def Srank2 (p : ℝ) : ℝ := negMulLog p + negMulLog (1 - p)

lemma Srank2_eq_binEntropy (p : ℝ) : Srank2 p = Real.binEntropy p :=
  (Real.binEntropy_eq_negMulLog_add_negMulLog_one_sub p).symm

/-- The larger of two squared singular values summing to 1 is `≥ 1/2`. -/
lemma half_le_top {a b : ℝ} (hab : b ≤ a) (hsum : a + b = 1) : 1 / 2 ≤ a := by
  nlinarith

/-- **Lemma (b), rank 2 (top-eigenvalue form).** With `pθ = σ₁(θ)²`, `p0 = σ₁²` and
    `½ ≤ pθ ≤ p0 ≤ 1`, the von Neumann entropy increases: `S(θ) ≥ S(0)`. The middle
    hypothesis `pθ ≤ p0` is **Fact 2** (Perron–Frobenius: the top singular value
    decreases), the single dependency left unproven here. -/
theorem rank2_entropy_excess {p0 pθ : ℝ}
    (hhalf : 1 / 2 ≤ pθ) (hfact2 : pθ ≤ p0) (hle1 : p0 ≤ 1) :
    Srank2 p0 ≤ Srank2 pθ := by
  rw [Srank2_eq_binEntropy, Srank2_eq_binEntropy]
  have hmem_pθ : pθ ∈ Set.Icc (2⁻¹ : ℝ) 1 := ⟨by rw [← one_div]; exact hhalf, le_trans hfact2 hle1⟩
  have hmem_p0 : p0 ∈ Set.Icc (2⁻¹ : ℝ) 1 := ⟨by rw [← one_div]; exact le_trans hhalf hfact2, hle1⟩
  rcases eq_or_lt_of_le hfact2 with h | h
  · rw [h]
  · exact le_of_lt (Real.binEntropy_strictAntiOn hmem_pθ hmem_p0 h)

/-- **Lemma (b), rank 2 (singular-value form).** Self-contained from the two pairs of
    squared singular values. At `θ = 0`: `a0 ≥ b0 ≥ 0`, `a0 + b0 = 1`; at `θ`:
    `aθ ≥ bθ ≥ 0`, `aθ + bθ = 1`. Given **Fact 2** `aθ ≤ a0`, the entropy increases:
    `S(θ) ≥ S(0)`. -/
theorem rank2_entropy_excess_of_sv {a0 b0 aθ bθ : ℝ}
    (hb0 : 0 ≤ b0) (_hab0 : b0 ≤ a0) (hsum0 : a0 + b0 = 1)
    (_hbθ : 0 ≤ bθ) (habθ : bθ ≤ aθ) (hsumθ : aθ + bθ = 1)
    (hfact2 : aθ ≤ a0) :
    Srank2 a0 ≤ Srank2 aθ :=
  rank2_entropy_excess (half_le_top habθ hsumθ) hfact2 (by linarith)

/-- The `Srank2 a` of a top eigenvalue `a` with partner `b = 1 - a` is the entropy of
    the eigenvalue pair `(a, b)`. -/
lemma Srank2_eq_pair {a b : ℝ} (hsum : a + b = 1) :
    Srank2 a = negMulLog a + negMulLog b := by
  rw [Srank2, show (1 : ℝ) - a = b by linarith]

end CoEmergence
