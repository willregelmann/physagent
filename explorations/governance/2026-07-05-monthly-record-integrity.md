# Governance monthly pass 2026-07-05: record integrity over throughput

**Date:** 2026-07-05
**Routine:** governor (monthly full pass — first scheduled run of July; T+26 of 90)
**Model:** claude-opus-4-8 (governor + position agents A–D + synthesis subagent, all claude-opus-4-8)
**Status:** Complete — OBJECTIVES edits, thread-proposal dispositions, and freshness sweep applied in the accompanying governance PR
**Position files:** `2026-07-05-position-A-citation-integrity.md`, `-B-record-rerank.md`, `-C-fpe-anchor.md`, `-D-ggd-frontier.md` (committed alongside per METHODOLOGY.md; losing arguments are part of the record)

## Context

Second monthly governance pass of the experiment (cycle 1 was 2026-06-11). The
reconstruction preamble (routine §0) found, since the last pass:

- **21 merged agent result-PRs** (metrics W24→W27: 5/8/7/7 per week); demotion
  rate ~0.19 (healthy); rigor distribution drifting demotion-heavy (Rigorous
  flat ~5, Sketch 8→12), promotions flat at ~1/week.
- **One active `needs-human` halt:** issue #75 (Red-team log), applied 2026-07-02.
- Three open `thread-proposal` issues: #137 (new), and #104/#110 (promoted to
  CE-11/CE-12 on 2026-06-21, still awaiting scout speccing).
- `agent-ready` queue **empty** at pass time (Sunday); #136 (GGD-1) and #45
  (CE-5) assigned/in-flight; scout refills Monday.

## Tripwire assessment (EXPERIMENT.md T1–T5)

- **T1 (zero demotions after 20 merged result-PRs): not fired.** 21 merged;
  demotion machinery firing steadily — merged demotions #116, #125, #134 and
  correction PR #147 in flight; demotion_rate 0.19.
- **T2 (fabricated / claim-misrepresenting citation in merged content): FIRED
  2026-07-02 — correctly handled by the red team; recorded here, not papered
  over.** The red-team audit found reference **[3] Hayward 1992** in the merged
  signature-change-boundary Markdown note cited as *supporting* the
  continuity-of-momentum (no-surface-layer) condition, when Hayward in fact
  requires *vanishing* junction momentum and explicitly **rebutted** the
  Dray–Manogue–Tucker condition the note adopts (gr-qc/9303034: "how the
  approach of Dray et al. can be corrected"). The note satisfies DMT and
  *violates* Hayward — the source was cited for the position it argued against.
  `needs-human` applied to #75; correction PR **#147** (`agent-pr`+`demotion`)
  opened per METHODOLOGY citation-failure recovery and armed for auto-merge
  behind the gate stack; #147 also resets SCB §4 geodesic-continuation and §8
  unification Rigorous→Sketch. **Governor actions:** do **not** remove
  `needs-human` (experimenter-only; NEVER rule 7); the SCB research thread stays
  halted (only #147 proceeds); record the SCB-4 milestone as certification-void
  (below). The **experimenter** owns clearing #75.
- **T3 (quorum accept rate > 95% over trailing 20 verdicts): cannot be
  mechanically evaluated — instrumentation gap; not evidently fired.** The
  accept/revise/reject rate (health metric #6) is **not surfaced** in
  `metrics/*.json`. Corroborating evidence that the quorum is not rubber-
  stamping: revise verdicts (#101; #89 ran four revise rounds), a reject (#77),
  and four merged demotion PRs in-window. Flagged as a proposal to the
  experimenter (C5) to surface metric #6 so T3 becomes checkable.
- **T4 (>50% merged volume outside milestones, trailing 4 weeks): not fired.**
  Merged work maps to CE/FPE/GGD/SCB milestones or is governance/demotion
  maintenance tied to them; drift is low.
- **T5 (two consecutive metrics runs fail / no data): not fired.** W24–W27 all
  present and non-empty (last 2026-06-29); next run (W28) due ~Monday.

## The debate

Four position agents developed independent cases (no shared view), adjudicated
by a synthesis subagent (METHODOLOGY team pattern). Direction questions:

- **A — citation-integrity is the cycle's top risk:** the two attribution-
  polarity misses (#134 Starobinsky coefficient; #147/T2 Hayward) are one
  structural blind spot; harden verification, freeze citation-content-heavy
  Rigorous promotions.
- **B — the record is stale and only the governor can fix it:** re-rank the
  month-old cross-program ordering (5/9 top slots Done/void), record-correct
  the void SCB-4 certification.
- **C — FPE is the load-bearing, most-damaged spine:** prioritize FPE-5/FPE-7
  repair and audit co-emergence's anchor language for post-demotion overclaims.
- **D — GGD is the only falsifiable-frontier program:** protect and harden the
  one experiment-killable prediction (but GGD-2 is already Done — the "phantom
  #1" is a bookkeeping desync).

### What the debate established (and the governor independently verified)

1. **Bookkeeping desync is real, governor-exclusive, and cheap.** **GGD-2's
   done-condition is met** — issue #102 was closed by PR #105 (merged
   2026-06-15); §5 carries the discriminant (0.22 fractional-coherence
   difference, 3σ, ~8000 shots, BMV+MAQRO) — yet the OBJECTIVES row still reads
   "Open." Five of the nine top slots in the 2026-06-11 cross-program ordering
   are Done/void (GGD-2, FPE-4 Outcome B, SCB-2/3, SCB-6, FPE-1; CE-4 further
   down). SCB-4's row reads "Open" but its README/PR-#138 certification is T2-void.

2. **The integrity of *merged content* — not throughput — is the current
   primary risk, in three registers of the same defect ("the record says more
   than the rigor supports"):**
   - *Citation polarity* (A): the T2/#134 class. The mechanism is a **verified
     gate-coverage hole** — `claim-support` (`semantic-review.yml:43`) runs only
     on diffs touching `programs/*.tex` or `.claude/tests/`, so the **Markdown
     SCB note was never semantically gated**; the test suite reads only
     `programs/fixed-point-existence/index.tex` and its `starobinsky` assertion
     covers *existence*, not the coefficient; co-emergence/GGD/SCB have **no**
     claim-support suite. Both misses landed exactly in these holes.
   - *Internal anchor consistency* (C): FPE demotions left overclaim residues in
     co-emergence. **Two now verified by the governor against
     `programs/co-emergence/index.tex`:**
     - **L980–983 (`prop:riem_classical`) — CONFIRMED defect, a demotion
       candidate.** The uniqueness step reads "the Banach contraction
       (Section~\ref{sec:level2}) guarantees a unique fixed point in ℂ^N." But
       Section level2 contains **no** finite-dimensional contraction for the
       $N$-site map $F(\psi)_\sigma = e^{\gamma R_\sigma}/\|e^{\gamma R}\|_2$; it
       relays the companion paper's **field-theoretic** SCE contraction, which
       is permanently **Sketch** under the M3 structural obstruction and is about
       a *different map*. A Rigorous proof step's uniqueness thus rests on a
       Sketch anchor about a different object. ($F$ is not manifestly a
       contraction on $\mathbb{C}^N$ for general real $\gamma$, so this is not a
       one-line citation swap.)
     - **L1706 — CONFIRMED residue.** "The Banach contraction result ($\kappa\ll1$
       for sub-Planckian curvatures; Sketch)" restates the **withdrawn** (M2)
       curvature-dependent Planck-boundary claim; FPE's corrected single-scale
       $\kappa\sim(m/M_P)^2$ is $R$-independent. Low severity, real internal-
       consistency defect.
     - *Not a defect:* L106–113's "signature-blind" line is adequately hedged
       (Sketch label; existence rests on the two exact fixed points). **Do not
       over-correct it.**
   - *Void certification* (B): SCB-4's "paper-grade verified" citation status is
     the T2 case — a dedicated verification pass (#138) certified the wrong
     polarity.

3. **The one falsifiable-frontier program (GGD) should be protected and
   hardened, not just extended** (D): its Result 2 (Gaussian profile) rests on
   the framework's built-in Gaussian-noise Assumption 1; an independent
   linearized-gravity noise kernel (arXiv:2606.04099, informs #107) offers a
   cross-check. D's own sharpest concession: **Remark 2** (ensemble dephasing ≠
   single-system decoherence) may leave the predicted *observable undefined* —
   a foundational gap sharper than more discriminability arithmetic.

4. **The machinery is largely self-healing** (B, conceded by A): the red team
   caught T2, #147 is armed, the scout refills Monday. This **bounds** the
   governor's mandate to high-value record-correction and routing — **not** a
   research freeze.

### What did not survive adjudication

- **A's broad promotion freeze** — over-reacts to n=2 and trades a verified-cheap
  risk against a real *Inconclusive*-outcome risk (throttled throughput). The
  hardening proposals survive; the blanket freeze does not. The **one** narrow
  hold that is justified is #137 specifically (its failed task-class and the
  blind gate coincide on the *same* coefficient).
- **C's "FPE-above-GGD" ranking** — an unsupported judgment ("most damaged" is
  not a metric; "M6/M7 repairable" was inherited from the README, not verified).
  C's *audit* recommendation survives on verified evidence; its ranking does not.
- **D's literal "GGD-2 first"** — GGD-2 is already Done. The residual cross-check
  and Remark 2 survive as the real GGD content.

## Decisions

### Enacted this cycle (this governance PR: OBJECTIVES + this exploration + freshness)

- **GGD OBJECTIVES:** GGD-2 → **Done** (PR #105, 2026-06-15). New milestone
  **GGD-3** (independent noise-kernel cross-check vs arXiv:2606.04099 / #107),
  with the *kernel-comparability precondition* written into the done-condition
  (agreement/disagreement is signal only under matched setup).
- **All four OBJECTIVES:** replace the stale 2026-06-11 cross-program ordering
  (see the new ordering below); mark Done rows with merging-PR refs (FPE-4
  Outcome B / #109, SCB-2/3 / #128, SCB-6 / #113, FPE-1 / #101, CE-4 / #131 —
  several already carried in status prose but not in the ordering).
- **SCB OBJECTIVES:** **SCB-4 record-correction (annotation, not re-open —** the
  row already reads "Open"): #138's content certification is **void** (T2);
  #147 in flight; SCB thread **halted** under `needs-human` (#75); §4/§8 reset
  to Sketch by #147.
- **co-emergence OBJECTIVES:** new milestone **CE-13** (anchor-language audit
  against post-demotion FPE rigor) — priority item is the **L980 demotion
  candidate** (`prop:riem_classical`), plus the L1706 residue fix and a sweep of
  every `\cite{fixed_point}` / "Banach contraction" / "guarantees" /
  "signature-blind" / "sub-Planckian" site; L106–113 explicitly out of scope
  (already hedged). CE-11/CE-12 **retain** `thread-proposal` per routine §2
  ("leave the label in place… the scout will spec it against the new
  milestone") — governor does not re-adjudicate promoted proposals; flagged for
  Monday scout as ~2 weeks overdue for speccing.
- **Freshness sweep:** co-emergence, fixed-point-existence, and GGD "In plain
  English" abstracts checked against current results — **current, no edit
  needed** (the L980/L1706 defects live in `index.tex`, not the READMEs; FPE's
  README already reflects the M3/Planck-withdrawal state; the Starobinsky
  *coefficient* demotion does not touch the READMEs, which state only
  existence/instability). **SCB README freshness DEFERRED** — its "paper-grade
  verified" citation line and "paths through space cross unharmed" plain-English
  are falsified by the pending #147 correction, but the SCB thread is under a
  `needs-human` halt and editing SCB program files would race #147; the
  responder/#147 owns that correction. Deferral recorded here so it is not
  papered over; the next monthly sweep re-checks it post-#147.

### New cross-program priority ordering (open milestones)

Repair-of-merged-content honesty and the falsifiable frontier rank above new CE
results; in-flight items stay where they are.

1. **GGD-1** (#136, in-flight — falsifiable frontier)
2. **CE-13** (anchor-language audit; contains the confirmed L980 demotion — a
   silently-wrong Rigorous step is worse than an honest Sketch, METHODOLOGY)
3. **FPE-5** (top *live* FPE repair — Schauder M6/M7; hardening the cited anchor)
4. **FPE-7** (well-definedness M8/M9; shares the M3 root)
5. **GGD-3** (noise-kernel cross-check; needs #107)
6. **CE-10 follow-ons** (cheap framing honesty)
7. **CE-11, CE-12** (promoted; scout to spec Monday)
8. **FPE-6** (Planck-boundary retirement note)
9. **FPE-2** (assumption A3)
10. **CE-5** (#45, in-flight; Lean covariate)
11. **CE-6 … CE-9** (unissued extensions)

Halted/blocked, unranked: the **SCB thread** (`needs-human` #75 — only #147
proceeds); **FPE-3** (blocked by FPE-4); **SCB-5** (experimenter-gated,
`.github/` touch); **SCB-4** (certification void, halted).

### Routed this cycle (no protected-path edit)

- **#137 → PARK** (thread-proposal disposition). Its done-condition — locate a
  paper-grade source and promote the Starobinsky coefficient
  $H_0^2=180\pi/(G|a_2|)$ Sketch→Rigorous — is the *exact* failed task-class of
  #134, on the *same* coefficient, through a `claim-support` gate verified blind
  to coefficient content (the `starobinsky` assertion covers existence only).
  Promoting it now manufactures the T2/#134 failure mode. **Not closed** (the
  direction is legitimate; the coefficient at Sketch is a fully honest interim
  state — no urgency). **Revisit condition:** promote once a claim-support
  *coefficient-normalization* assertion for that de Sitter coefficient exists on
  `programs/fixed-point-existence/index.tex` (hardening proposal C1) **and** a
  paper-grade source supplying the closed form has been located.
- **L980 → red-team / worker demotion** via CE-13: supply an independent
  finite-dimensional uniqueness/contraction lemma for $F$ on $\mathbb{C}^N$, or
  demote `prop:riem_classical` to Sketch. Highest-value single research finding
  of the debate, and it is **verified**, not conjectured.
- **Remark 2 (GGD observable-definition gap) → `thread-proposal`** (governor's
  one proposal this run) for future adjudication — underspecified and possibly
  entangled with a foundational interpretational choice, so **not** promoted
  this cycle (governor must not promote anything needing a new postulate).

### Proposed to the experimenter (protected paths — NOT enactable by any agent; @-mention in the PR)

These target `.claude/`, `.github/`, `tools/`, `METHODOLOGY.md`. The governor may
only *propose*; the experimenter enacts (gate-workflow files have **no** agent
path — the machine PAT lacks the `workflow` scope). Motivated by the verified
coverage holes:

- **C1.** Extend `.claude/tests/citation-claim-support/` to every program's
  `index.tex` (co-emergence, GGD, SCB have none) and add two assertion classes
  the misses exploited: **coefficient-normalization** (closed-form coefficients,
  not just existence) and **junction-camp-membership** (Hayward vanishing-
  momentum vs Dray–Manogue–Tucker). Highest-leverage single fix; also the
  precondition for un-parking #137.
- **C2.** Close the Markdown hole: run `claim-support`/existence verification on
  Markdown notes carrying paper-grade bibliographies, **or** a METHODOLOGY rule
  barring paper-grade certification in Markdown (bibs must live where the gates
  run). The Hayward miss was invisible because the note was Markdown.
- **C3.** METHODOLOGY rule: polarity-sensitive claims (junction conditions, camp
  membership, closed-form coefficients) must cite the **specific affirming
  passage** and **name competing camps** — giving reviewer and `claim-support` a
  polarity anchor. #138 certified Hayward on abstracts, which have none.
- **C4.** De-correlate models: consider flipping `MODEL_WORKER` (a documented,
  no-PR experimenter knob) so the terminal audit and quorum do not share the
  abstract-level blind spot that false-certified Hayward through *both* quorum
  and dedicated verification.
- **C5.** Instrumentation: surface the T3 quorum accept/revise/reject rate
  (health metric #6) in `metrics/*.json` so T3 is mechanically checkable.

### Left to the Monday scout

Spec and open the `agent-ready` issues for CE-13 (incl. the L980 demotion),
GGD-3, CE-11, CE-12; refill the queue generally. **Flag:** the empty queue is a
benign weekend artifact (#136/#45 in-flight; Monday refill), **but** the
`agent_ready` trend 4→4→3→1→0 is a real leading indicator that the easy-to-spec
frontier is thinning and the remaining milestones are harder to spec. Not a
tripwire; noted for direction.

### Version tag: none this cycle

The METHODOLOGY tag bar requires "no known internal contradictions." This cycle
carries an **active `needs-human` halt (T2, #75)**, an **unmerged correction
(#147)**, and a **freshly confirmed Rigorous-label defect (L980)**. Tagging would
assert a clean state that does not currently exist. Deferred to a pass where #147
has merged, L980 is dispositioned, and #75 is cleared. When in doubt, don't.

---

*Position files A–D are committed alongside this synthesis. The synthesis
subagent independently re-verified the L980 site before recommending its
demotion; the governor re-verified L980 and L1706 against
`programs/co-emergence/index.tex` before recording them here.*

routine: governor · model: claude-opus-4-8
