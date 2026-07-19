---
name: citation-claim-support
tools: ["WebFetch", "WebSearch"]
assertions:
  - "starobinsky: the paper's own text at every \\cite{starobinsky} site is consistent with — and supported by — what the cited Starobinsky 1980 paper establishes: that the trace anomaly of conformal/quantum fields on an FRW background admits an exact de Sitter solution of the semiclassical Einstein equation (a self-consistent inflationary fixed point)"
  - "parker_simon: the paper's own text at every \\cite{parker_simon} site is consistent with — and supported by — what the cited Parker-Simon paper establishes: the use of order reduction to recast the higher-derivative semiclassical Einstein equation as a second-order (order-reduced) equation"
  - "meda_pinamonti_siemssen: the paper's own text at every \\cite{meda_pinamonti_siemssen} site is consistent with — and supported by — what the cited Meda-Pinamonti-Siemssen paper establishes: existence/uniqueness (a contraction-type argument) for solutions of the semiclassical Einstein equation on cosmological/FLRW spacetimes"
  - "meda_pinamonti_stability: the paper's own text at every \\cite{meda_pinamonti_stability} site is consistent with — and supported by — what the cited Meda-Pinamonti 'Linear stability' paper establishes: that, for a massive quantum field, linear perturbations of the semiclassical solution decay polynomially in time"
  - "oppenheim: the paper's own text at every \\cite{oppenheim} site is consistent with — and supported by — what the cited Oppenheim paper establishes: the position that classical gravity coupled to quantum matter (a postquantum / semiclassical-as-fundamental theory) is a serious candidate rather than only an approximation"
  - "capper_duff: [coefficient-normalization, fixed-point-existence] the paper's own text at every \\cite{capper_duff} site is consistent with — and supported by — what the cited Capper-Duff paper establishes: the existence of the conformal trace anomaly for quantum fields. The paper's text must NOT attribute to Capper-Duff the de-Sitter-evaluated, field-content-summed normalization constant in $\\langle\\hat T^\\mu{}_\\mu\\rangle = -a_2 H_0^4/120\\pi^2$, nor the closed-form coefficient $H_0^2=180\\pi/(G|a_2|)$ itself — the paper's own Rigor-status note (Section~starobinsky) already states these are a later, paper-internal reparametrization/convention, not something Capper-Duff supplies. This assertion exists to gate any FUTURE edit that tries to close that gap by citing Capper-Duff (or a new source) for the numeric coefficient without the source actually deriving it — see the revisit condition recorded in `explorations/governance/2026-07-05-monthly-record-integrity.md`."
  - "fixed_point: [companion-citation, co-emergence] the paper's own text at every \\cite{fixed_point} site in `programs/co-emergence/index.tex` is consistent with what the companion paper `programs/fixed-point-existence/index.tex` actually establishes about the semiclassical Einstein equation's Banach-contraction argument: a perturbative, field-theoretic argument (a map on spacetime metrics/field configurations) that is permanently **Sketch**-level, not Rigorous, given the M3 structural obstruction (the non-local response kernel is a Lorentzian hyperbolic Green operator with causal-past support that resists a compact-Cauchy-surface bound; see `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md`). It does NOT supply a finite-dimensional contraction or uniqueness argument for co-emergence's own toy-model map $F(\\psi)_\\sigma = e^{\\gamma R_\\sigma}/\\|e^{\\gamma R}\\|_2$ on $\\mathbb{C}^N$ — that is a distinct map on a distinct space. A `\\cite{fixed_point}` site in co-emergence that reads as though the companion paper's contraction directly guarantees uniqueness for the $\\mathbb{C}^N$ map is a FAIL, regardless of whether the companion paper's own (correctly-labeled) result is itself fine."
  - "hu_verdaguer: [gaussian-gravitational-decoherence] the paper's own text at every \\cite{hu_verdaguer} site is consistent with — and supported by — what the cited Hu-Verdaguer 'Stochastic gravity' review establishes: the Einstein-Langevin equation as the established stochastic-gravity framework for including the two-point (noise-kernel) fluctuations of quantum stress-energy as a source term alongside the mean semiclassical Einstein equation. This is the single most load-bearing citation in the paper (nearly every derived result routes through it) and has never been claim-support-checked before this assertion."
  - "diosi: [coefficient-normalization, gaussian-gravitational-decoherence] the paper's own text at every \\cite{diosi} site is consistent with — and supported by — what Di\\'osi's paper establishes: a universal decoherence/master-equation model for gravitationally-induced collapse, with a specific decoherence-rate/timescale formula. The paper's comparison coefficient (its stated ratio to $\\tau_{DP}$, e.g. $\\tau_{coh}\\approx 1.13\\,\\tau_{DP}$) must accurately reflect the *functional form* of the timescale Di\\'osi's own paper derives (not merely cite Di\\'osi for the general topic of gravitational decoherence)."
  - "penrose: [coefficient-normalization, gaussian-gravitational-decoherence] the paper's own text at every \\cite{penrose} site is consistent with — and supported by — what the cited Penrose paper establishes: that gravitational self-energy of the difference between two mass distributions sets an intrinsic decoherence/state-reduction timescale (Penrose's gravitationally-induced state-reduction proposal), reached from the ill-definedness of the time-translation Killing vector between superposed spacetimes — a distinct argument from Di\\'osi's, converging on the same order-of-magnitude timescale. The paper's text must not conflate the two derivations' routes to the same number."
  - "melo_dissipative: [junction-camp-membership, gaussian-gravitational-decoherence] the paper's own text at every \\cite{melo_dissipative} site is consistent with — and supported by — what the cited Melo et al. dissipative-DP paper actually claims about the exponential-decay exponent under friction, specifically the paper's own framing of \\S7.x's 'discrimination question' and the exponent-correction claim near lines 638-662 of `programs/gaussian-gravitational-decoherence/index.tex`. This is a contested/nuanced technical claim (an exponent correction under a friction model) of exactly the kind that misattributes easily if only the abstract is checked — verify the specific mechanism, not just the topic."
---

Semantic claim-support check for the load-bearing citations in
`programs/fixed-point-existence/index.tex`, `programs/co-emergence/index.tex`,
and `programs/gaussian-gravitational-decoherence/index.tex`. The deterministic
`verify-citations` CI gate already confirms these references *exist*; this test
checks the harder, non-mechanical question METHODOLOGY.md assigns to
human/agent review: does each cited source actually *support the claim the
paper currently attaches to it*?

**Coverage note (2026-07-18, hardening proposal C1 from the 2026-07-05
governance synthesis).** Until this revision, every assertion here targeted
only `fixed-point-existence`; `co-emergence` and `gaussian-gravitational-decoherence`
had zero claim-support coverage despite the CI trigger (`semantic-review.yml`)
running on a diff to *any* program's `.tex` file. `signature-change-boundary`
still has no `index.tex` (prose-only in `notes/`, per its README) and so
cannot be covered by this file-scoped test until it ports (SCB-5); see
METHODOLOGY.md's Markdown citation-discipline rule for why Markdown-only
citations are not paper-grade regardless.

Each assertion is tagged with the assertion class it belongs to, in a
bracketed annotation immediately **after** the `key:` prefix (never between
the key and its colon — the CI failure-scoping script greps for `key:` to
identify which assertion failed, so the key must be followed immediately by
a colon with nothing in between). The tag is one of the two new classes this
revision adds:
- **[coefficient-normalization]** — the paper attaches a specific closed-form
  numeric or algebraic result to a citation. A source that is topically
  correct but does not itself derive/state that specific closed form is a
  FAIL for this class, even though a looser "existence" assertion on the same
  key might separately PASS.
- **[junction-camp-membership]** — the citation is one of several genuinely
  competing or opposed positions in a real dispute (rival conditions, rival
  interpretations, a result vs. its own rebuttal), not simply an uncontested
  fact. Checking only the abstract is insufficient for this class — abstracts
  routinely omit which side of a dispute a paper is actually on. This is the
  class that would have caught the Hayward/Dray-Manogue-Tucker misattribution
  in `signature-change-boundary` (issue #75, T2, 2026-07-02) had SCB's note
  already been in a gated `.tex` file.
- **[companion-citation]** — the citation is to another program's paper in
  this same repo (e.g. co-emergence citing fixed-point-existence). No
  WebSearch/WebFetch is applicable or needed; verify by reading the cited
  companion `.tex` file directly (see step 3a below).

Assertions not explicitly tagged are the original **existence/general-claim**
class: does the cited external source's own stated results support the
paper's claim at all, independent of any specific coefficient or dispute
membership.

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

1. Determine which program(s)' `index.tex` are in scope for this key from the
   assertion's bracketed tag (e.g. `[gaussian-gravitational-decoherence]`,
   appearing right after the key's colon, means check only that file; an
   untagged key like `starobinsky` is shared by both `fixed-point-existence`
   and `co-emergence` as companion papers and must be checked in **both**).
   Read every in-scope `index.tex` and locate
   EVERY site where the key is `\cite`d. Extract, verbatim, the claim the
   paper's surrounding text attributes to the source at each site. Record
   these extracted claims — they are the object being judged.
2. Compare each extracted claim against the assertion's reference description
   of the source. If the paper attributes to the source a materially different
   result — and especially if it attributes the OPPOSITE position (e.g. citing
   a paper that develops a theory as having refuted it) — judge **FAIL**
   immediately, quoting the divergent paper text. Do not proceed to step 3 to
   "rescue" the assertion.
3. For an ordinary external-literature key: use `WebSearch` to find the cited
   work by author, title, and year, then `WebFetch` its abstract page (arXiv,
   journal/DOI page, or an authoritative index). Judge PASS only if the
   source's own stated results support the extracted paper claims from step 1.
   Quote the supporting sentence from the source as evidence.
3a. For a **[companion-citation]**-tagged key (currently only `fixed_point`):
   skip WebSearch/WebFetch entirely — there is no external source to fetch.
   Instead read the cited companion `.tex` file directly (e.g.
   `programs/fixed-point-existence/index.tex` for the `fixed_point` key) and
   compare its actual proven content, at its own stated rigor label, against
   what the citing paper's text attributes to it. A citing paper that states
   or implies a stronger result than the companion paper's own rigor label
   supports is a FAIL, even if the general topic match is correct.

Be strict, in both directions: a source that is merely *topically related* but
does not state the paper's specific claim is a FAIL; a paper claim that
diverges from what the source establishes is a FAIL even though the reference
description remains true of the source. Cite the title/venue you actually
located as evidence, so a reader can tell you found the right paper and not a
namesake.
