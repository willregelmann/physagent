---
id: ggd-noise-kernel
program: gaussian-gravitational-decoherence
tier: rigorous
status: live
statement: >
  For an orthogonal two-branch superposition with definite branch centre-of-mass
  positions, the equal-time noise kernel factorizes as
  N_0000(x, x') = (c^4/4) Delta_rho(x) Delta_rho(x').
hypotheses:
  - non-relativistic stress-energy operator T00 = c^2 rho(x - X_CM)
  - orthogonal branches
  - each branch has definite centre-of-mass position
falsifier: a superposition satisfying the hypotheses whose kernel does not factorize
consequence: supplies the noise kernel entering the Einstein-Langevin analysis
novelty: {status: unchecked}
tex: {file: programs/gaussian-gravitational-decoherence/index.tex, label: eq:N0000}
provenance: {born: 2026-06-10, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Re-derived from scratch and reproduced exactly. Dimensional check passes
    (energy density squared). Both load-bearing assumptions are explicitly stated
    at the point of use, not smuggled: the "definite centre-of-mass position"
    idealization - zero intra-branch spread - is exactly what a careful check
    would otherwise flag as hidden, and it is stated. The paper's own hedge is
    accurate: only the equal-time factorization is Rigorous, and the use of this
    kernel as a complete Gaussian-noise specification is explicitly not.
---
