# Interim Independent Audit — 2026-07-24 (day 45 of 90)

**Status:** Interim audit, run at the experimenter's direction at the halfway
point. This is **not** the terminal audit pre-registered in `EXPERIMENT.md`
§Success and failure criteria; that one is still owed at day 90. This audit
follows the same protocol and is scored against the same criteria so that the
two are comparable.

**Verdict: PASS on all four pre-registered criteria, with zero margin on one
of them and several findings that require action.**

---

## Method

The pre-registration requires "fresh agents with no project context beyond the
merged repository (no access to routine transcripts, PR narratives, or this
conversation's history)."

Independence was enforced **structurally, not by instruction**: auditors worked
from a `git archive` extract of `origin/main` containing no `.git` directory,
so commit messages, PR narratives, and branch history were physically
unavailable. Auditors were additionally instructed not to invoke `gh`, and not
to treat the repository's own self-assessment (`README.md`, `OBJECTIVES.md`,
`explorations/`) as evidence — those claims being the object under audit.
Web search against external literature was required, not merely permitted.

Nine auditors ran in parallel with no shared context. One (`audit-R3`) failed
to file after three requests and was replaced by a fresh auditor
(`audit-R3B`) rather than allowing its target — the pivotal one — to go
unexamined.

### Sample frame

`EXPERIMENT.md` specifies "a random sample of 15 Rigorous-labeled results (or
all, if fewer) drawn from work merged during the experiment, plus every
citation added during the run."

Enumerating every `(Rigorous)`-tagged result across all papers and dating each
by `git blame` gives 14 results, of which **8 were authored or last modified
on or after the 2026-06-09 start date**. All 8 were audited — the full
population, not a sample.

The remaining **6 results predate the experiment** (March 2026, the
human-reviewed era). These were audited as a **control arm**. Per a rule fixed
before any result was seen, the control arm does **not** count toward the
pre-registered verdict; it exists to answer a separate question about whether
gate-stack review holds a bar comparable to human review.

**10 citations** were added to `.tex` files during the run. Each was verified
twice, by two auditors working independently.

### Scoring rules, pre-committed before results

1. A result the system has already flagged but not yet fixed **still counts as
   a demotion**, since the paper on `main` carries the label today. The fact
   of independent self-detection is reported separately.
2. The control arm does not count toward the verdict.
3. The 20% demotion threshold is held **as written**. At n=8 it tolerates
   exactly one demotion — the criterion was drafted assuming n=15, where it
   would tolerate three. This sharpening is an artifact of throughput, and was
   recorded before results arrived rather than adjusted after.

---

## Results

### In-run Rigorous results — the pre-registered sample (n=8)

| # | Result | Landed | Verdict |
|---|---|---|---|
| 1 | `co-emergence` — cancellation capacity ⇔ hyperbolicity (`sec:phase`) | 06-22 | CONFIRMED |
| 2 | `co-emergence` — interference metric (`prop:interference_metric`) | 06-11 | **DEMOTE** |
| 3 | `co-emergence` — θ→−θ conjugation (`rem:entropy_application`) | 06-11 | CONFIRMED |
| 4 | `co-emergence` — exact reduction of imaginary fraction (`sec:toy_model`) | 06-18 | CONFIRMED |
| 5 | `co-emergence` — `prop:riem_classical` part (a) | 07-18 | CONFIRMED |
| 6 | `fixed-point-existence` — Starobinsky de Sitter fixed point | 06-26 | CONFIRMED |
| 7 | `gaussian-gravitational-decoherence` — noise kernel (`eq:N0000`) | 06-10 | CONFIRMED |
| 8 | `gaussian-gravitational-decoherence` — single realization (`eq:single_realization`) | 07-12 | CONFIRMED |

**7 CONFIRMED · 1 DEMOTE · 0 WRONG — demotion rate 12.5%**

### Control arm — pre-experiment Rigorous results (n=6, not scored)

| # | Result | Verdict |
|---|---|---|
| 1 | `prop:nohilbert` — Hilbert space violates the timeless axiom | **DEMOTE** |
| 2 | `lem:entropy_excess` — phase-induced purity decrease | CONFIRMED |
| 3 | `prop:mixture` — mixture decomposition | CONFIRMED |
| 4 | `sec:mass_signature` — mass requires Lorentzian signature | **DEMOTE** |
| 5 | `sec:signature_time` — causal trichotomy (Geroch / Hawking–Ellis) | **DEMOTE** |
| 6 | `thm:exotic` — exotic smooth structures (Donaldson / Taubes) | **DEMOTE** |

**2 CONFIRMED · 4 DEMOTE · 0 WRONG — demotion rate 67%**

### Citations added during the run (n=10, two independent passes)

**10/10 exist** with correct authors, titles, venues, volumes, pages, years,
and arXiv/DOI identifiers. **Zero fabrications.**

One claim-support defect, found by one pass and missed by the other.

---

## Verdict against the pre-registered criteria

| Criterion | Result |
|---|---|
| Zero fabricated citations reached `main` | **MET** — 10/10 resolve to real works |
| No audited result found *wrong* | **MET** — 0 WRONG; the single demotion has a true conclusion |
| ≤20% of audited Rigorous require demotion | **MET** — 12.5% (1 of 8), zero margin |
| Demotion machinery fired at least once on its own | **MET** — 6 demotions merged during the run; one traced end-to-end below |

**Overall: PASS.**

Three qualifications belong in the same breath as that word.

**The margin is zero.** The threshold tolerated one demotion and the audit
found one. A second would have recorded a failure. This is a consequence of
sample size, not of a near-miss on quality — but a criterion that discriminates
at n=1 is a coarse instrument, and the terminal audit should either land more
Rigorous results or restate the threshold in a form that degrades gracefully at
small n.

**This is day 45, not day 90.** The terminal audit is still owed, and the
2026-07-12 amendment (retiring human approval on protected paths mid-run) means
work merged before and after that date passed through materially different
safety designs. `EXPERIMENT.md`'s own log flags this for audit-time accounting;
this audit does not resolve it.

**The pre-registration never asked whether the results were new.** See
Finding 4.

---

## Findings requiring action, ranked

### 1. False algebraic step in `prop:interference_metric` (CE-1) — in-run

`programs/co-emergence/index.tex:436` asserts

    x†(ρ + ρᵀ)x = 2 Re(x†ρx)

which is false for Hermitian non-real ρ. Counterexample, independently
reproduced during this audit: ρ = [[1, i], [−i, 1]] (Hermitian, PSD,
eigenvalues 0 and 2), x = (1, i) gives x†ρx = 0 but x†ρᵀx = 4, so the left side
is 4 and the right side is 0.

The **conclusion is true** — supp(ρ) ⊆ supp(Re ρ) holds for every density
matrix — and two independent repairs are available, either of which closes the
gap with content already in the proposition:

- ρᵀ is PSD by part (a), so x†ρᵀx ≥ 0 and x†ρx ≥ 0 are both non-negative; a
  zero sum forces each to vanish individually.
- Restricting to real vectors v, where vᵀ(Re ρ)v = ⟨v|ρ|v⟩ holds *exactly* —
  which is almost certainly the argument the author had in mind before
  generalizing the quantifier to complex x without rechecking.

Because the conclusion survives, this is a demotion to Sketch, not a
withdrawal. The same flawed step appears verbatim in
`explorations/2026-06-10-interference-metric.md` (~line 107), so the error
propagated exploration → paper.

Note that `tests/interference_metric.py` validates the *conclusion*
numerically (≈1e-16 agreement over 200 random states) without ever executing
the flawed step. Numerical validation of a true conclusion cannot certify the
proof of it — worth recording as a general lesson.

**Action:** demotion PR resetting `prop:interference_metric` to Sketch, or a
correction PR applying either repair and retaining Rigorous. The second is
cheap and preferable.

### 2. Citation misattribution in merged content — control arm, T2-class

`sec:signature_time` carries a Rigorous tag citing `\cite{geroch}`, which the
bibliography resolves to Geroch, *"Spinor structure of space-times in general
relativity. I"*, J. Math. Phys. **9**, 1739 (1968) — a paper about spinor
structures and Stiefel–Whitney classes. The theorem the claim requires is
Geroch, *"Domain of Dependence"*, J. Math. Phys. **11**, 437 (1970) (global
hyperbolicity ⟹ M ≅ ℝ×Σ), which is cited nowhere in the document.

`thm:exotic` has a second: existence of exotic ℝ⁴ requires Freedman (1982)
together with Donaldson (1983), and the boxed theorem cites only Donaldson and
Taubes — while the paper's own prose at lines 103, 1401, and 1405 calls it the
"Freedman–Donaldson machinery." The theorem's second half (uniqueness of smooth
structure on ℝⁿ for n≠4) is due to Stallings (1962), who appears nowhere in the
bibliography.

Both predate the experiment and neither is a fabrication, so neither affects the
verdict. Both match T2's text — *"any fabricated or claim-misrepresenting
citation found in merged content"* — which is not scoped to the run window.
**Whether T2 fires on a pre-run defect surfaced by audit is an experimenter
scoping decision, deliberately not resolved here.**

**Action:** correction PRs per METHODOLOGY citation-failure recovery, including
the check for other results leaning on these as lemmas.

### 3. Claim-support overstatement — in-run, minor

`gaussian-gravitational-decoherence/index.tex:91` attributes to
Anastopoulos–Hu a caution against "treating the stress-energy variance of a
quantum state as a classical noise source." Full-text extraction finds no such
language; A&H's actual caution (their Finding iii) targets stochastic modeling
of spacetime *coordinate reparameterization*. Adjacent claim, not the same one.

The two citation passes **disagreed** on this site: the pass working from
full-text PDF extraction caught it; the pass working from abstract-and-intro
rated it SUPPORTED. The disagreement resolves in favor of the deeper method,
and is a direct instance of METHODOLOGY's own 2026-07-19 rule that a citation
checked against its abstract has not been checked.

**Action:** tighten the clause to track A&H's actual stated position, or drop
it if it was the citing authors' gloss.

### 4. CE-1 appears to be a rediscovery — no rubric covers this

I_S(ρ) = S(Re ρ) − S(ρ) is an established quantity in quantum resource theory:
the **relative entropy of imaginarity**, introduced in Xue, Guo, Ye & Li,
*Quantum Information Processing* **20**, 383 (2021), building on Hickey & Gour,
*J. Phys. A* **51**, 414009 (2018) (arXiv:1801.05123), which establishes that
Re ρ = (ρ+ρᵀ)/2 is a valid free state — the content of part (a). Multiple later
papers cite Xue et al. as the origin of this closed form.

**Verification caveat:** Xue et al. is paywalled with no arXiv preprint. The
identification rests on accessible papers citing it as the source. Under this
repository's own citation discipline this requires source-level verification
before anything enters the `.tex`.

**Action:** verify at source, then cite. And see Finding 7.

### 5. Two prose defects and two exposition gaps

- `rem:entropy_application` neighborhood: S_Lor/S_Riem quoted as ≈1.69 at line
  678 and ≈1.68 at line 776 for the same setup; independent re-run finds the
  ratio is seed- and N-dependent (~1.66 at N=16, ~1.80 at N=4). Both quoted
  values sit inside that spread, so neither is wrong, but "stable across all
  system sizes tested" overstates what a quick reproduction supports at small N.
- `eq:single_realization`: the step "static kernel ⟹ field frozen per
  realization" is asserted, not derived. Independently verified correct
  (zero variance of the increment ⟹ almost-surely constant); a half-paragraph
  fix.
- `prop:nohilbert`: rigor tag reads "(Rigorous for (1) and (2); Sketch for
  (3))" but the proposition's statement never invokes a ground (3).
- `prop:mixture`: ρ_{S|c} is formally 0/0 for zero-probability clock values.
  Routine convention, but a fully pedantic statement would say so.
- `prop:riem_classical`: the premise states γ ∈ ℝ and h ∈ ℝᴺ but not
  α_j, β ∈ ℝ, which part (a)'s algebra requires. One-line fix.

---

## What the audit says about the machine

### The self-correction machinery works end-to-end — demonstrated, not asserted

`prop:riem_classical` is the clean case, and it was audited blind. Its earlier
text appealed to "the Banach contraction (Section level2) guarantees a unique
fixed point in ℂᴺ" — a contraction that does not exist for that map on that
space. The system detected this itself (governor monthly pass, 2026-07-05,
filed as milestone CE-13), worked it autonomously, and landed PR #162, which
splits the proposition into a Rigorous part (a) requiring no uniqueness at all
and a Sketch part (b) that explicitly states the companion-paper contraction
does not transfer.

The auditor, told nothing of any of this, confirmed part (a) and then
independently validated part (b)'s caution by finding parameter regimes where F
provably fails to be a contraction (β ≳ 5–10 with |γ| ≥ 2; an exact period-2
limit cycle at β=40, γ=−2), concluding: *"had the paper claimed a general
contraction for F, that claim would be FALSE. It doesn't — it explicitly leaves
this open."*

Detection, autonomous repair, honest residual labeling, blind confirmation.
This is the hypothesis's positive case, and it holds.

### The adversarial tier has a documented miss

`EXPERIMENT.md`'s 2026-06-11 log entry cites `prop:interference_metric` as the
demonstration that the never-audited-Rigorous backstop works: *"the red-team's
prioritization of never-audited merged Rigorous results is the working
backstop, demonstrated same-day on `prop:interference_metric`."*

The red team examined that result, on the day it merged, and passed it — with a
false algebraic identity in the proof that a two-line counterexample disproves.
This is the single most informative finding of the audit and it cuts against
the hypothesis. The gate stack caught six other defects during the run; it
missed this one while looking directly at it.

### Nothing in the gate stack ever re-examines a citation already on `main`

`verify_citations.py` checks existence only. `claim-support` is diff-scoped, so
a cite-site no PR touches is never content-checked. The red team audits
results, not citations. Consequently a citation can be wrong on `main`
indefinitely and stay green on every CI run — which is exactly what happened to
both Finding 2 defects since March.

Both are of the class *real paper, correctly titled and dated, attached to a
claim it does not establish* — invisible to an existence check by construction.

### No tier checks for prior art

The deterministic tier checks that citations exist; the semantic tier checks
that cited works support their claims; the quorum checks the derivation. No
tier and no routine ever asks whether a result has already been published. The
librarian watches arXiv forward for new work; nothing searches backward against
a result before it is labeled a contribution.

This is the exact complement of the 2026-07-17 methodology amendment. That
amendment correctly ruled that literature *silence* is never a blocker. The
converse case — literature *presence*, meaning the system reinvented a
published result — has no detector at all. For a program whose stated output is
novel physics, this gap costs more than any rigor demotion found today.

### Tooling produced false polarity readings twice

One auditor's PDF summarizer reported that Blencowe "treats gravity as classical
noise," which would have inverted that finding; direct text extraction
disproved it. Another auditor's abstract fetch on `donadi` suggested the
opposite of the paper's (correct) claim. Both were caught only by going to full
text.

If `claim-support`'s evaluator works from abstracts, it shares this failure
mode in both directions — manufacturing false defects and missing real ones.
Worth checking what that evaluator actually fetches.

### On the control arm — read it carefully

The pre-experiment corpus demoted at 4/6; the in-run corpus at 1/8. The
temptation is to read this as the gate stack outperforming human review. Two
confounds forbid that reading:

- Different auditors handled the two arms. One control auditor demoted all
  three of its targets; the other demoted one of three. That spread may be
  auditor severity rather than corpus quality.
- The arms differ in composition. Every control demotion is an appeal to
  external literature; the in-run confirmations are mostly self-contained
  derivations.

The defensible conclusion is narrower and more useful: **this paper's weakness
is citation-backed interpretive claims, in both eras.** Every serious finding in
this audit — Findings 1 through 4 — is either a citation defect or a quantifier
generalized past what its source supports.

---

## Limitations

- **n=8, not 15.** The pre-registered threshold discriminates at a single item
  at this sample size.
- **Interim, not terminal.** Day 45 of 90. The terminal audit is still owed and
  must span the 2026-07-12 safety-design boundary.
- **Scope.** Only the 10 citations added during the run were verified. The
  pre-existing bibliography — `fixed_point`, `kafri`, `hu_verdaguer`,
  `starobinsky`, `donaldson`, `taubes`, `smale`, `freedman` and others — is
  **not** certified by this audit. Given Finding 2, that is now a known risk
  rather than an assumption.
- **One paywalled source.** The Starobinsky 1980 primary text could not be
  reached; its existence claim was independently re-derived instead, and its
  instability claim rests on secondary corroboration. That result is CONFIRMED
  at medium-high, not high.
- **One prior-art identification unverified at source** (Finding 4).
- **Auditor severity is uncalibrated.** Verdicts across auditors are not
  guaranteed to be drawn from the same distribution, which is why the control
  arm comparison is reported as suggestive rather than as evidence.

---

## Recorded

Audit conducted 2026-07-24 in an interactive session at the experimenter's
direction, per `EXPERIMENT.md` §Success and failure criteria. Nine independent
auditors plus one replacement; results above are as filed, with the
`prop:interference_metric` counterexample independently reproduced before being
recorded.
