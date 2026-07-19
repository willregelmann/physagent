# Cross-Program Connections Not Captured by Any Single Program

**Date:** 2026-07-18
**Role:** Cross-program synthesis, produced in an interactive Claude Code session at the human experimenter's direction (not a governor routine run — see process note). Scope: identify substantive connections between programs that no single program's README/OBJECTIVES/Explorations currently states, because each tracks only its own thread.
**Inputs:** `programs/co-emergence/index.tex` §3 and OBJECTIVES.md (CE-10, CE-11, CE-12); `programs/fixed-point-existence/index.tex` and OBJECTIVES.md (FPE-4/M3); `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md`; `programs/signature-change-boundary/README.md`; `programs/gaussian-gravitational-decoherence/index.tex` and OBJECTIVES.md (GGD-3); `explorations/governance/2026-06-11-cycle-1-direction-debate.md`; `programs/co-emergence/explorations/2026-07-18-twistor-theory-scoping.md`.

---

## Finding 1: a recurring "Lorentzian direction is the obstructed one" pattern, tracked in only one place

The same qualitative asymmetry — the Lorentzian/timelike direction hits an obstruction, termination, or absence of a real solution, while the Riemannian/spacelike direction passes through, closes, or exists cleanly — appears independently in at least four separate technical contexts across this repo:

1. **`co-emergence`'s core result** (`index.tex` §3): self-consistency of the fixed-point map with a Lorentzian geometry forces the wavefunction to develop complex phases; a Riemannian geometry stays purely real/classical. (Rigorous, for the small solvable model.)
2. **`fixed-point-existence`'s M3 obstruction**: already named explicitly in `explorations/governance/2026-06-11-cycle-1-direction-debate.md` (Position B's hidden-assumption check) as "M3 is an elliptic (Riemannian) resolvent silently standing in for the hyperbolic (Lorentzian) problem" — the existence proof's kernel-bound technique works cleanly in the elliptic case but requires a compact Cauchy surface (currently unavailable in general) in the hyperbolic case.
3. **`signature-change-boundary`'s crossing asymmetry** (Rigorous, given the fixed background): timelike geodesics reach the signature-change surface Σ at finite proper time with no timelike continuation; spacelike curves cross with character intact. This is a fully independent, already-proven, concrete geometric instance of the same qualitative split.
4. **Today's twistor-theory scoping exploration** (`co-emergence/explorations/2026-07-18-twistor-theory-scoping.md`): non-trivial self-dual metrics have no real Lorentzian representative at all (verified by direct primary-source fetch); the corresponding Riemannian/split-signature constructions are the ones that exist non-trivially.

**What is and isn't being claimed.** This is not presented as a surprising discovery in the sense of "nobody could have predicted this" — the generic fact that Lorentzian signature gives hyperbolic (causal, finite-propagation-speed) structure while Riemannian signature gives elliptic (boundary-value, no causal structure) structure is textbook mathematical physics, and it is unsurprising that four independent derivations, each rooted in the same signature distinction, would independently rediscover *some* version of this split. What **is** worth naming is that only one of the four (`CE-12`) is a governor-tracked, cross-program milestone, and it is scoped narrowly to a two-way comparison (co-emergence's `rem:signature_blind` vs. fixed-point-existence's M3) that does not currently cite either the SCB crossing-asymmetry result or today's twistor finding as additional data points — even though both are sitting on the record, already labeled, and directly on-topic.

**Concrete, low-cost recommendation:** declare an explicit `informs` relation (per METHODOLOGY's Issue Relations discipline) from `signature-change-boundary`'s crossing-asymmetry result to CE-12, and from today's twistor-scoping exploration to CE-12. Neither requires new research — CE-12's own done-condition ("attempting the Riemannian-signature kernel bound directly... checking whether it closes at Rigorous with no M3-analogue") could be informed by SCB's already-rigorous statement of what the Lorentzian/Riemannian split looks like in a simpler, fully solved toy geometry, and by the twistor exploration's independent confirmation that the same split recurs in a third, unrelated formalism. This does not resolve CE-12's H1/H2 question, but it means CE-12 would draw on three independent data points instead of one when it is eventually worked.

**Why this wasn't already connected:** `signature-change-boundary` has been halted under `needs-human` (#75) since 2026-07-02 for an unrelated citation-integrity reason (the Hayward misattribution), and its scope guard ("do not attach self-consistency machinery... do not merge into co-emergence") appears to have discouraged treating its results as *evidence* for another program's question, as distinct from *building on* it — those are different things, and only the latter is actually barred. (Note: #75 was cleared by the experimenter earlier in this session, so this recommendation is immediately actionable, not blocked.)

---

## Finding 2: `gaussian-gravitational-decoherence` and `fixed-point-existence` may be answering the same question from opposite ends, unlinked

`GGD`'s Gaussian-decoherence result rests on a noise kernel evaluated in an explicit approximation (`index.tex` L261–269): stationary superposition, Newtonian limit, and — stated directly — "retardation corrections are $\mathcal{O}(v^2/c^2)$ and negligible." This is precisely the regime where the full causal (retarded, non-local-in-time) structure of the underlying stress-tensor two-point function is approximated away by hand.

`FPE`'s M3 obstruction is a finding about exactly that causal structure in the un-approximated case: the response kernel is a Lorentzian hyperbolic Green operator with causal-past support, and this is diagnosed as the structural reason a compact-Cauchy-surface bound fails for general (non-stationary, non-FLRW) backgrounds.

These are not the same calculation, but they are plausibly the same underlying object (the retarded stress-energy two-point function sourcing back-reaction) viewed from opposite directions: GGD's phenomenological, weak-field, stationary-matter approximation, and FPE's rigorous, general-existence-proof attempt. **GGD-3** (the program's own milestone for hardening the noise-kernel result) is scoped to cross-check against an *external* independent linearized-gravity calculation (arXiv:2606.04099); nothing in either program's OBJECTIVES currently poses the *internal* cross-program question: does GGD's stationary/retardation-neglected approximation sit safely inside a regime where M3's obstruction doesn't bite (plausible — a genuinely stationary source is close to the FLRW/de-Sitter case where the existing existence machinery *does* work), or would restoring retardation reintroduce the same causal-kernel difficulty M3 already names?

**Recommendation:** this is well-posed and falsifiable enough to be thread-proposal material (per AUTONOMY.md's thread-proposal channel), not a finished result. A falsifiable first step: state precisely what "stationary matter" (GGD's Assumption) requires of the background metric, and check whether that condition is a special case of (or implies) the compact-Cauchy-surface / FLRW-homogeneous-slicing condition FPE's existing exact solutions already rely on. If yes, GGD's Result 2 gets a firmer foundation than "assumed Gaussian noise" (Assumption 1) currently gives it, *and* the cross-check should be added as a documented dependency of GGD-3 rather than left to the external-paper comparison alone. If no — if stationary-matter falls genuinely outside what M3-compatible techniques currently reach — that is itself worth stating plainly rather than leaving implicit, since it would mean GGD's headline prediction rests on an approximation whose validity relative to the rest of the framework's own existence machinery has never been checked.

---

## Recommendation

Neither finding produces new mathematics by itself (per METHODOLOGY, this Exploration establishes direction, not results). Concrete next actions, for the experimenter's disposition:

1. **Finding 1** — low-cost, immediately actionable: add the two `informs` relations to CE-12's issue thread (SCB crossing-asymmetry; today's twistor-scoping exploration). No new issue required.
2. **Finding 2** — thread-proposal-shaped: could be filed as a `thread-proposal` issue (falsifiable first step stated above), for the governor's normal weekly adjudication (promote into GGD-3's scope / an FPE-informs-GGD milestone, park, or close).

This exploration takes no GitHub action itself; both recommendations are presented for the experimenter to authorize.

---

**Process note (interactive-mode disclosure):** Produced in a human-directed interactive Claude Code session, following the same synthesis pattern as `2026-07-17-null-infinity-boundary-clock.md` and `2026-07-18-twistor-theory-scoping.md`. No GitHub claim, comment, issue, or PR was made by any agent in producing this file. Per METHODOLOGY.md, Explorations are committed directly by the human author.

routine: interactive · model: claude-sonnet-5 (human-directed, 2026-07-18)
