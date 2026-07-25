---
id: ce-signature-time
program: co-emergence
tier: rigorous
status: live
statement: >
  The causal trichotomy (timelike/spacelike/null) and proper time along
  worldlines give local time without a global foliation; general relativity
  prohibits a universal time.
hypotheses:
  - a Lorentzian manifold
cites:
  - key: geroch
    role: load-bearing
    supports: >
      Global hyperbolicity implies a topological splitting M = R x Sigma.
    verified: {at: 2026-07-24, by: none}
  - key: hawking_ellis
    role: load-bearing
    supports: standard causal structure and proper time
    verified: {at: 2026-07-24, by: full-text, expires: 2027-07-24}
falsifier: a globally hyperbolic spacetime admitting no such splitting
consequence: local worldline time suffices; no preferred slicing is introduced
novelty:
  status: prior-art
  searched: 2026-07-24
  found: [geroch, hawking_ellis]
  note: >
    Independently reproduced the recorded defect exactly, including volume,
    pages and year, and supplied the replacement: Geroch, 'Domain of
    Dependence', J. Math. Phys. 11, 437-449 (1970). CORRECTED 2026-07-24 --
    the bibitem now points at the right paper. Hawking-Ellis verified
    correct and genuinely supports the physical content.
tex: {file: programs/co-emergence/index.tex, label: sec:signature_time}
provenance: {born: 2026-03-03, born_by: human}
audit:
  reviewed: 2026-07-24
  verdict: demote
  finding: >
    The physical content is standard and genuinely supported by Hawking & Ellis.
    But \cite{geroch} resolves to Geroch, "Spinor structure of space-times in
    general relativity. I", J. Math. Phys. 9, 1739 (1968) - a paper about spinor
    structures and Stiefel-Whitney classes, unrelated to this content. The
    theorem actually required is Geroch, "Domain of Dependence", J. Math. Phys.
    11, 437 (1970), which is cited nowhere in the document. High confidence: a
    checkable title/abstract mismatch, not a judgment call. No hidden-foliation
    problem otherwise.
---

**T2-class defect in merged content.** A real paper, correctly titled and dated,
attached to a claim it does not establish - the class that passes an
existence-only citation check by construction. Predates the experiment
(March 2026) and has been green on every CI run since.

`verified.by` is recorded as `none` because the citation *was* checked and
*failed*; there is no schema state for "verified and refuted", which is itself
a finding about the schema.
