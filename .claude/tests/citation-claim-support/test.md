---
name: citation-claim-support
tools: ["WebFetch", "WebSearch"]
assertions:
  - "starobinsky: the paper's own text at every \\cite{starobinsky} site is consistent with — and supported by — what the cited Starobinsky 1980 paper establishes: that the trace anomaly of conformal/quantum fields on an FRW background admits an exact de Sitter solution of the semiclassical Einstein equation (a self-consistent inflationary fixed point)"
  - "parker_simon: the paper's own text at every \\cite{parker_simon} site is consistent with — and supported by — what the cited Parker-Simon paper establishes: the use of order reduction to recast the higher-derivative semiclassical Einstein equation as a second-order (order-reduced) equation"
  - "meda_pinamonti_siemssen: the paper's own text at every \\cite{meda_pinamonti_siemssen} site is consistent with — and supported by — what the cited Meda-Pinamonti-Siemssen paper establishes: existence/uniqueness (a contraction-type argument) for solutions of the semiclassical Einstein equation on cosmological/FLRW spacetimes"
  - "meda_pinamonti_stability: the paper's own text at every \\cite{meda_pinamonti_stability} site is consistent with — and supported by — what the cited Meda-Pinamonti 'Linear stability' paper establishes: that, for a massive quantum field, linear perturbations of the semiclassical solution decay polynomially in time"
  - "oppenheim: the paper's own text at every \\cite{oppenheim} site is consistent with — and supported by — what the cited Oppenheim paper establishes: the position that classical gravity coupled to quantum matter (a postquantum / semiclassical-as-fundamental theory) is a serious candidate rather than only an approximation"
---

Semantic claim-support check for the load-bearing citations in
`programs/fixed-point-existence/index.tex`. The deterministic `verify-citations`
CI gate already confirms these references *exist*; this test checks the harder,
non-mechanical question METHODOLOGY.md assigns to human/agent review: does each
cited source actually *support the claim the paper currently attaches to it*?

**The paper is the thing under test, not the assertion list.** Each assertion
has two parts: a `\bibitem` key, and a reference description of what the cited
source actually establishes. The description is ground truth about the SOURCE;
it says nothing about what the paper currently claims — the paper's text may
have drifted or been edited to misattribute. Judging an assertion true because
the description matches the source, without checking the paper's own words, is
the known failure mode of this test (it let a deliberately inverted claim pass
during gate verification on 2026-06-05). Do not repeat it.

This is a **semantic smoke test**, not a proof check. Judge only on whether the
cited work's own abstract/results back the claim the paper makes — not on
whether the physics is ultimately correct.

For each assertion (keyed by its `\bibitem` key):

1. Read `programs/fixed-point-existence/index.tex` and locate EVERY site where
   the key is `\cite`d. Extract, verbatim, the claim the paper's surrounding
   text attributes to the source at each site. Record these extracted claims —
   they are the object being judged.
2. Compare each extracted claim against the assertion's reference description
   of the source. If the paper attributes to the source a materially different
   result — and especially if it attributes the OPPOSITE position (e.g. citing
   a paper that develops a theory as having refuted it) — judge **FAIL**
   immediately, quoting the divergent paper text. Do not proceed to step 3 to
   "rescue" the assertion.
3. Use `WebSearch` to find the cited work by author, title, and year, then
   `WebFetch` its abstract page (arXiv, journal/DOI page, or an authoritative
   index). Judge PASS only if the source's own stated results support the
   extracted paper claims from step 1. Quote the supporting sentence from the
   source as evidence.

Be strict, in both directions: a source that is merely *topically related* but
does not state the paper's specific claim is a FAIL; a paper claim that
diverges from what the source establishes is a FAIL even though the reference
description remains true of the source. Cite the title/venue you actually
located as evidence, so a reader can tell you found the right paper and not a
namesake.
