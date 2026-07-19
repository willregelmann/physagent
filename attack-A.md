# Attack pass on Attempt A

Five findings, verified directly against repo files:

1. **Unexamined corpus inconsistency.** `co-emergence/index.tex` L1371-1375 ("Level 2... its existence is established in the companion paper," stated definitionally) and L1764-1766 ("Level 2 existence is a necessary condition") vs. `fixed-point-existence/index.tex` L52-56 and GGD README L48 ("does not depend on those existence results," never derived). Three mutually-tense assertions, never reconciled.

2. **Direct textual contradiction: FPE has a rigorous route on Minkowski for the M3-relevant kernel bound specifically.** `fixed-point-existence/index.tex` L377-385 (Källén-Lehmann remark, independently verified verbatim): "On Minkowski spacetime, the bound can alternatively be established via the Källén-Lehmann spectral representation... This approach is rigorous on flat backgrounds but does not extend directly to general curved spacetimes." Directly undercuts "FPE's machinery doesn't cover this class period."

3. **Retardation-vs-staticness conflation + inequality error.** GGD's actual math is elliptic throughout (Poisson equation, static Green's function) — never contains a retarded/hyperbolic Green's function. The assigned technique was applied to a hypothetical relativistic completion, not the text as written. Separately: the attempt's sentence "the timescale... separately ≪ τ_coh" has the inequality backwards relative to GGD's own margin (spreading time ≫ τ_coh by ~5×10¹⁴).

4. **Axiom-check precedent not engaged.** The M3 exploration's Position B treats deriving a preferred foliation from background symmetry as illegitimate unless flagged as a new assumption (even Position A names it "A7"). The attempt's "concluded: no" doesn't engage this precedent.

5. **The O(v²/c²)-never-derived admission is more damaging than credited** — given finding 3, the entire comparison against M3 was run against a reconstructed object, not GGD's actual text.

No survive/eliminate verdict rendered (attack pass only).
