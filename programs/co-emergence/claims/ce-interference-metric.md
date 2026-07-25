---
id: ce-interference-metric
program: co-emergence
tier: rigorous
status: live
statement: >
  Re(rho) = (rho + rho^T)/2 is a density matrix; S(Re rho) >= S(rho); and
  supp(rho) is contained in supp(Re rho), so the interference metric
  I_S(rho) = S(rho || Re rho) = S(Re rho) - S(rho) is finite for every state.
object:
  name: I_S
  space: density matrices on C^d
hypotheses:
  - rho is Hermitian
  - rho is positive semidefinite
  - x in C^d
internal_steps:
  - step: "x^dag (rho + rho^T) x = x^dag rho x + x^dag rho^T x, both summands nonnegative"
    hypotheses: [rho is positive semidefinite, x in C^d]
    note: >
      Repaired 2026-07-24. This step previously read
      x^dag (rho + rho^T) x = 2 Re(x^dag rho x), which is false for Hermitian
      non-real rho and held only for real x — a narrower hypothesis than the
      claim's, which is why lint L4 fired on it. The repair carries no narrowed
      hypothesis: rho^T is positive semidefinite because it is isospectral to
      rho, as already used in part (a), so both summands are nonnegative for
      every x in C^d and a vanishing sum forces each to vanish.
cites:
  - key: xue_imaginarity
    role: load-bearing
    supports: >
      The closed form min over real states of S(rho || sigma) = S(Re rho) - S(rho),
      introduced as the relative entropy of imaginarity.
    verified: {at: 2026-07-24, by: none}
falsifier: >
  A density matrix whose support escapes the support of its real part.
consequence: >
  The interference metric is well defined on all states, and is the quantity
  used to separate quantum from classical contributions.
novelty:
  status: prior-art
  searched: 2026-07-24
  found: [xue_imaginarity, hickey_gour]
tex: {file: programs/co-emergence/index.tex, label: eq:interference_metric}
provenance: {born: 2026-06-11, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: demote
  finding: >
    Parts (a) and (b) correct. Part (c)'s proof asserts
    x^dag (rho + rho^T) x = 2 Re(x^dag rho x), which is false for Hermitian
    non-real rho. Counterexample independently reproduced: rho = [[1, i], [-i, 1]]
    (Hermitian, PSD, eigenvalues 0 and 2) with x = (1, i) gives 4 on the left and
    0 on the right. The gap propagates into part (b)'s equality clause. The
    conclusion is true and two repairs are available. Separately: this quantity
    is the relative entropy of imaginarity (Xue et al. 2021), uncited.
---

**Open defect.** Two independent repairs, either sufficient:

1. rho^T is PSD by part (a), so `x^dag rho^T x >= 0` and `x^dag rho x >= 0` are
   both non-negative; the hypothesis forces the sum to zero, hence each term
   individually. No appeal to the false identity.
2. Restrict to real vectors v, where `v^T (Re rho) v = <v|rho|v>` holds
   *exactly*. Almost certainly the argument originally intended, generalised to
   complex x without rechecking.

The same flawed step appears verbatim in
`explorations/2026-06-10-interference-metric.md` (~line 107): the error
propagated exploration -> paper.

`tests/interference_metric.py` validates the *conclusion* numerically
(~1e-16 agreement over 200 random states) without ever executing the flawed
step. Numerical validation of a true conclusion cannot certify its proof.

**Prior art unverified at source.** Xue, Guo, Ye & Li, *Quantum Information
Processing* 20, 383 (2021) is paywalled with no arXiv preprint; the
identification rests on later papers citing it as the origin of this closed
form. Under this repository's citation discipline that requires source-level
verification before entering the .tex — hence `verified.by: none`.
