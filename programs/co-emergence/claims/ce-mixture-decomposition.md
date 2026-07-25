---
id: ce-mixture-decomposition
program: co-emergence
tier: rigorous
status: live
statement: >
  Mixture decomposition: sum over clock values c of p(c) rho_{S|c} equals the
  partial trace of |psi><psi| over the clock factor.
object:
  name: rho_S
  space: density matrices on the system factor of C^N
hypotheses:
  - a fixed factorization Sigma = C x S
  - psi in C^N arbitrary
falsifier: a state and partition where the two sides differ
consequence: >
  Conditioning on a clock reproduces the reduced state; the Page-Wootters
  construction is consistent with the partial trace.
novelty:
  status: independent-rederivation
  searched: 2026-07-24
  found: []
  note: >
    Not attributable to any specific paper: this is the direct algebraic
    content of the partial trace as an expectation over projective outcomes,
    one line by matrix elements, which is exactly what the paper's proof
    does. Used routinely and silently throughout the Page-Wootters
    literature as a known fact, never presented as a result needing
    attribution. No citation given and none needed.
tex: {file: programs/co-emergence/index.tex, label: eq:cond_dm}
provenance: {born: 2026-03-05, born_by: human}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    The standard unraveling-of-a-partial-trace identity, re-derived termwise and
    correct for any psi and any partition. Minor caveat, not demotion-worthy: if
    p(c) = 0 for some c then rho_{S|c} is formally 0/0; the identity still holds
    by the universal convention that such terms contribute the zero matrix, but a
    fully pedantic statement would say so.
---
