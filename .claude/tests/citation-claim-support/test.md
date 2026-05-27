---
name: citation-claim-support
tools: ["WebFetch", "WebSearch"]
assertions:
  - "starobinsky: the cited Starobinsky 1980 paper supports that the trace anomaly of conformal/quantum fields on an FRW background admits an exact de Sitter solution of the semiclassical Einstein equation (a self-consistent inflationary fixed point)"
  - "parker_simon: the cited Parker-Simon paper supports the use of order reduction to recast the higher-derivative semiclassical Einstein equation as a second-order (order-reduced) equation"
  - "meda_pinamonti_siemssen: the cited Meda-Pinamonti-Siemssen paper supports existence/uniqueness (a contraction-type argument) for solutions of the semiclassical Einstein equation on cosmological/FLRW spacetimes"
  - "meda_pinamonti_stability: the cited Meda-Pinamonti 'Linear stability' paper supports that, for a massive quantum field, linear perturbations of the semiclassical solution decay polynomially in time"
  - "oppenheim: the cited Oppenheim paper supports the position that classical gravity coupled to quantum matter (a postquantum / semiclassical-as-fundamental theory) is a serious candidate rather than only an approximation"
---

Semantic claim-support check for the load-bearing citations in
`programs/fixed-point-existence/index.tex`. The deterministic `verify-citations`
CI gate already confirms these references *exist*; this test checks the harder,
non-mechanical question METHODOLOGY.md assigns to human/agent review: does each
cited source actually *support the specific claim* it is attached to?

This is a **semantic smoke test**, not a proof check. Judge each assertion only
on whether the cited work's own abstract/results back the claim the paper makes
with it — not on whether the physics is ultimately correct.

For each assertion (keyed by its `\bibitem` key):

1. Read `programs/fixed-point-existence/index.tex` and locate where the key is
   `\cite`d, to confirm the exact claim the paper attributes to it. The
   bibliography entry (author, title, journal, year) is in the
   `thebibliography` block near the end of the file.
2. Use `WebSearch` to find the cited work by its author, title, and year, then
   `WebFetch` its abstract page (arXiv, the journal/DOI page, or an
   authoritative index) to read what it actually claims.
3. Judge PASS only if the source's own stated results support the specific claim
   the paper makes. If the source is about a clearly different result, or you
   cannot locate an authoritative description of it, judge FAIL with the reason.
   Quote the supporting sentence from the source as evidence.

Be strict: a source that is merely *topically related* but does not state the
specific claim is a FAIL. Cite the title/venue you actually located as evidence,
so a reader can tell you found the right paper and not a namesake.
