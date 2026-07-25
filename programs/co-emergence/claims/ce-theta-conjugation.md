---
id: ce-theta-conjugation
program: co-emergence
tier: rigorous
status: live
statement: >
  Replacing theta by -theta conjugates M entrywise and hence conjugates rho,
  leaving the singular values and all derived entropies unchanged; the sign of
  theta is a harmless orientation convention.
object:
  name: rho_theta
  space: positive matrices under entrywise phase
hypotheses:
  - m_ij > 0 strictly
depends_on:
  - id: ce-entropy-excess
    role: load-bearing
    transfers: same-object
falsifier: a configuration whose spectrum differs between theta and -theta
consequence: orientation of the phase carries no physical content
novelty:
  status: prior-art
  searched: 2026-07-24
  found: []
  note: >
    Standard linear algebra, not a paper-gradable target: a complex matrix
    and its entrywise conjugate have identical singular values (Horn &
    Johnson, Matrix Analysis, 2nd ed., CUP 2013, SVD chapter). The checker
    re-derived it independently. The claim is already honest about being 'a
    harmless orientation convention'. NOTE this is prior-art in the WEAK
    sense -- textbook mathematics, not a research result rediscovered. That
    is a different situation from CE-1 and warrants a citation, not a
    correction.
tex: {file: programs/co-emergence/index.tex, label: rem:entropy_application}
provenance: {born: 2026-06-11, born_by: worker}
audit:
  reviewed: 2026-07-24
  verdict: confirmed
  finding: >
    Verified two independent ways (termwise on the rho formula, and via the
    dagger algebra). "A matrix and its entrywise conjugate have the same
    singular values" confirmed standard. Minor, outside the tagged claim: the
    adjacent numeric aside quotes S_Lor/S_Riem as 1.69 at one site and 1.68 at
    another for the same setup; re-running the toy model gives a seed- and
    N-dependent spread (~1.66 at N=16 to ~1.80 at N=4). Both quoted values sit
    inside that spread, but "stable across all system sizes tested" is stronger
    than a quick reproduction supports at small N.
---

Note the object here is shared with [[ce-entropy-excess]]: same matrix family,
same space. The `same-object` edge is correct.
