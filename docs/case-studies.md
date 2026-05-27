# Case Studies: The Methodology Working

The point of [the workflow](agent-workflow.md) is not that agents produce
research — it's that the guardrails catch the failure modes agents are prone
to. These are receipts: concrete moments where adversarial review, honest
negative-result reporting, rigor demotion, or a CI gate did its job. Each is a
real artifact in the git history, not a claim.

---

## 1. Adversarial review downgraded a result (Rigorous → Sketch)

**Artifact:** commit [`04c05fa`](https://github.com/willregelmann/self-consistency/commit/04c05fa) — *"Address adversarial review: downgrade Prop 3, fix Banach language, qualify Hilbert derivation claim."*

A proposition in the co-emergence paper ("Lorentzian conditioning produces
quantum coherences") was labelled **Rigorous**. Adversarial review found that
its genericity condition was unverified for physically natural fields and that
the proof leaned on a fixed-point form only established in the toy model. The
result was demoted **Rigorous → Sketch**, the Banach-vs-Hilbert language was
corrected, and an overclaim that "Hilbert space is derived" was softened to
"not introduced as a separate axiom," with the open question stated explicitly.

*Why it matters:* the single most important competence for agent-driven
research is not over-claiming. Here the process caught and walked back an
overclaim before it could propagate.

## 2. Negative results are recorded, not buried

**Artifacts:**
[`ebd01bb`](https://github.com/willregelmann/self-consistency/commit/ebd01bb) —
*"PW conditioning is not approximately unitary (negative result)"*;
[`b0abc7f`](https://github.com/willregelmann/self-consistency/commit/b0abc7f) —
*"B1 and C1 signature explorations (both negative results)."*

A natural conjecture — that Page–Wootters conditioning yields approximately
unitary time evolution — was investigated and **failed**. Likewise, two
attempts to derive Lorentzian signature from lower-level self-consistency were
negative. All three are committed Explorations, kept as permanent records so
future agents don't re-walk closed paths.

*Why it matters:* a system rewarded for producing positive results will
hallucinate them. This program treats a documented negative result as a
first-class output that narrows the search space.

## 3. Rigor demotion as routine maintenance

The general-rank von Neumann entropy-excess claim was demoted after a
counterexample was found (3×3 density matrices with extreme entries), while the
all-rank **purity-decrease** result and the rank-2 entropy result survived and
remain Rigorous. The paper now states precisely where the result holds and
where it doesn't.

*Why it matters:* rigor labels track the truth as it's currently understood,
and are revised in public rather than quietly left stale.

## 4. The citation gate caught a real mis-citation

**Artifact:** PR [#46](https://github.com/willregelmann/self-consistency/pull/46) (`verify-citations`).

On its *first run*, the automated citation gate flagged an unresolved
reference in the `fixed-point-existence` paper. Investigation showed the
`gottschalk_siemssen` entry had stapled the wrong authors and title onto a
**correct arXiv ID** (2201.10288). That ID is actually Meda & Pinamonti,
*"Linear stability of semiclassical theories of gravity"* (Ann. Henri Poincaré
24, 1211, 2023) — which turned out to be the *correct* source for the cited
claim (massive fields give polynomially decaying perturbations). The citation
was corrected and verified paper-grade: author, title, journal/year, **and**
claim-support.

*Why it matters:* hallucinated and mis-attributed citations are the headline
trust problem for AI-assisted research (in 2025, fabricated citations survived
human peer review at major venues). A mechanical existence gate caught a real
instance here that human reading had missed.
