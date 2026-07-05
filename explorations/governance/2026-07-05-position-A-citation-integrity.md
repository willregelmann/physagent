# Position A: The attribution-polarity citation leak is the cycle's top governance priority

**Author:** position agent A (governor monthly debate, 2026-07-05) · **Model:** claude-opus-4-8
**Disposition in synthesis:** hardening proposals + the #137 park **adopted**; the broad promotion-freeze **rejected** (over-reacts to n=2).

## Thesis

Two independent red-team findings in the current audit window (#134 Starobinsky
coefficient, 2026-06-25; #147/T2 Hayward [3], 2026-07-02) are the same failure:
**a real, existence-verified citation attached to a claim whose topic it matches
but whose position/coverage it does not** — Starobinsky/Capper–Duff do not supply
the closed-form coefficient; Hayward *rebuts* the Dray–Manogue–Tucker condition
the note satisfies. No pre-merge gate layer reads a source's argumentative
direction, and the semantic tier meant to catch content-mismatch has coverage
holes exactly where both misses landed. Because the terminal audit re-verifies
*every citation added during the run* and a misrepresenting-citation-in-merged-
content is a pre-committed experiment-failure condition, closing this leak
dominates every other governance action this cycle.

## Mechanism (grounded in the gate config)

- **`claim-support` (`semantic-review.yml`) does not cover where the misses
  live.** Its changes filter fires only on `programs/*.tex` or `.claude/tests/`;
  the SCB note is **Markdown**, so claim-support never ran on the Hayward
  citation (existence gating `verify_citations.py` is likewise `.tex`-only). The
  test suite covers **only** `programs/fixed-point-existence/index.tex` and five
  assertions; co-emergence/GGD/SCB have **no** suite. The `starobinsky`
  assertion is scoped to *existence*, not the coefficient; `capper_duff` has no
  assertion — the coefficient misattribution sat in an unasserted blind spot.
- **The failure mode is already known and specifically hardened against** (the
  2026-06-05 Phase-D "inverted claim" false negative) — yet both live misses
  recurred **outside** the hardened assertion's reach.
- **Quorum shares the blind spot** (same-model worker/reviewer post-2026-06-13;
  diff-grounded review reads the source at the same abstract level the worker
  did) and **a dedicated verification pass (#138) certified the wrong polarity**
  from abstracts. Only the red team caught either — post-merge, 3-day cadence.

## Recommendations

**Governor-authority (this cycle):** PARK #137 (its done-condition is the exact
failed task-class on the same coefficient through a blind gate); do not promote
citation-content-heavy Rigorous milestones until hardening lands; write this
exploration; gate SCB-5 on #147 + an SCB claim-support suite; signal a red-team
citation-content polarity sweep; reinforce (never remove) #75 `needs-human`.

**Protected-path proposals (experimenter only):** extend claim-support to every
`index.tex` + add coefficient-normalization and junction-camp assertions; run
claim-support on Markdown notes with paper-grade bibs (or bar such certification
in Markdown); METHODOLOGY rule requiring polarity-sensitive claims to cite the
specific affirming passage and name competing camps; recommend flipping
`MODEL_WORKER` to de-correlate the quorum.

## Honest self-assessment

n=2 is a pattern-of-two, not a measured rate; the base rate of polarity-
sensitive vs benign citations is uncharacterized. "Evading the gate stack" is
partly by-design — content-match was never mechanically gated (red team +
terminal audit own it), and the red team **caught both**, which EXPERIMENT.md
counts as success. The fix may be a bounded "grow the assertion list," not a
research freeze; polarity hardening risks false positives that throttle
throughput toward *Inconclusive*. The line holds only on **stakes asymmetry**: a
misrepresenting citation surviving to the terminal audit is irreversible and
whole-experiment-fatal, while the mitigation is cheap and reversible.

*(Full agent output preserved in the debate record; condensed here for the
committed artifact.)*

routine: governor · model: claude-opus-4-8
