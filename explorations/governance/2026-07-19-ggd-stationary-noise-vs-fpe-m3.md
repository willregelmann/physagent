# GGD's Stationary Noise Kernel vs. FPE's M3 Obstruction — Explorer Fan-Out Synthesis

**Date:** 2026-07-19
**Role:** Synthesis of a width-3 explorer fan-out cycle (`automation/routines/explorer.md`), run as an interactive-mode dry run of the newly-designed routine (first real test of the two-pass attack/steelman elimination discipline adopted 2026-07-18). Synthesis performed by the interactive lead, following the precedent of prior same-day Explorations.
**Question:** Does `gaussian-gravitational-decoherence` (GGD)'s "stationary matter" noise-kernel approximation sit safely inside a regime where `fixed-point-existence` (FPE)'s M3 obstruction doesn't apply, or would restoring genuine retardation reintroduce the same causal-kernel difficulty? (Sourced from `explorations/governance/2026-07-18-cross-program-connections.md`, Finding 2 — a falsifiable question flagged there as thread-proposal-shaped but never previously worked.)
**Scratch record:** `scratch/explorer/2026-07-19-ggd-stationary-vs-m3-obstruction` (branch, never merged, never deleted per the explorer scratch-tier design) — 3 fan-out attempts, 3 attack passes, 3 steelman passes, in full.

---

## Executive summary

**Verdict: GGD's numerical predictions are safe from M3, but the reason is narrower and less clean than the initial three-way convergence suggested — and the process that surfaced this is itself the main finding worth recording.**

All three independently-developed attempts (frequency-domain reduction; direct case-matching against FPE's exact solutions; direct retardation-expansion estimate) converged, without seeing each other, on a similar first-pass conclusion: GGD is safe because it is "a different kind of calculation" than FPE's self-consistency loop, with no fixed-point iteration for M3 to obstruct. This convergence looked like strong evidence. **It was not fully correct**, and only one of three attack passes (on Attempt B) happened to dig deeply enough into GGD's own text — specifically its assumption (iv), "backreaction of decoherence on the noise kernel is neglected" — to find that GGD *does* contain a conceptual self-consistency loop, truncated at the first iterate rather than absent. Once that was established, the categorical "structurally exempt" framing failed under honest steelmanning (§4 below), even though the *practical, numerical* safety of GGD's predictions survived.

**This is the headline methodological lesson of the cycle:** three independent methods reaching the same conclusion is evidence, not proof, when all three share an unexamined premise. The fan-out's value here came not from convergence but from one attack pass's willingness to read GGD's own disclosed assumptions as literally as it read FPE's.

**Corrected, narrower verdict that does survive across all three lines of attack:** GGD's noise-kernel calculation is the leading-order (zeroth-iterate) term of the *same* conceptual self-consistency map FPE studies, evaluated once rather than iterated to convergence. Its safety from M3 rests on two facts, not one: (a) *structurally*, the specific object GGD's retardation correction would touch (a well-posedness/Green's-function piece, analogous to FPE's already-established `C_inv`) is not the object M3 obstructs (the matter-response kernel `K^red`); and (b) *practically*, the two terms GGD truncates to reach that leading order (vacuum-fluctuation contribution, ~10⁻⁵⁸; backreaction of decoherence on the noise kernel) are both independently estimated as extravagantly small, but neither is rigorously bounded — both are explicitly flagged in GGD's own text as estimates, not derived bounds. If either were ever promoted to a rigorous bound, that derivation would need to confront a question much closer to FPE's actual existence question, on a background (Minkowski) FPE's own compact-Cauchy-surface requirement does not currently reach — a genuinely open dependency, not a resolved one.

A second, independently valuable outcome: the cycle found two concrete, real citation/attribution defects in the actual paper text (not just in the fan-out attempts' own reasoning), detailed in §5.

---

## 1. What was tried

Three genuinely different techniques, developed blind to each other:

- **Attempt A** — stationary scattering / frequency-domain reduction of retarded Green's functions.
- **Attempt B** — direct case-matching of GGD's background against FPE's stated exact theorems and their explicit exclusions.
- **Attempt C** — direct perturbative estimate of GGD's own retardation expansion, term-by-term against M3's object.

All three, full text, are on the scratch branch. Full attack and steelman passes are also there; only the survivable content and the corrections are carried forward here.

## 2. What survived, and what didn't

**Attempt A** — the specific technique (retardation restored via frequency-domain reduction) was withdrawn: GGD's actual mathematics is elliptic throughout (a Poisson equation, never a retarded/hyperbolic Green's function), so the technique was checked against a reconstructed relativistic completion of GGD, not the text as written; a genuine inequality-direction error was also found and not defensible. The *core claim* survived on simpler, purely structural grounds: GGD's Sections 2–4 contain no map `F: g → g'`, no candidate set `K_ρ`, no contraction estimate, no iteration, verified by direct reading. This was independently reinforced, not weakened, by chasing a citation the attack flagged as contradicting the "FPE excludes Minkowski, period" premise: FPE's own text (`fixed-point-existence/index.tex` L377–385, the Källén–Lehmann remark) states a rigorous alternative route for the *specific* kernel-bound object M3 discusses, on Minkowski — but a full re-read of the surrounding text (Step 6's separate Rellich–Kondrachov compactness requirement; Open Problem #5, independently numbered) shows FPE treats "M3's kernel-bound gap" and "the compact-Σ gap" as two logically independent open problems, and attributes the Minkowski exclusion of the *full theorem* to the latter, not the former. This actually strengthens the genus-mismatch thesis: Minkowski's own symmetry supplies exactly the structure (a Källén–Lehmann spectral gap) that lets the specific hyperbolic-to-elliptic difficulty M3 names be avoided there, consistent with — not contrary to — "this is the wrong genus of problem for M3 to bind on."

**Attempt C** — survived essentially intact, with three precision corrections: (1) the categorical "no tail exists at all" claim overclaimed against real post-Newtonian tail-term physics (hereditary tails are real, first appearing at 1.5PN — still numerically negligible, but the categorical framing was wrong and is walked back to "no tail at the order GGD computes"); (2) a size-based fallback argument in the attempt's own verdict ("even granting relevance, the correction is tiny") was dropped as not load-bearing, once the correct structural argument (GGD's correction is analogous to FPE's already-unproblematic well-posedness piece, never the obstructed response kernel) is used instead — conflating "small" with "boundable-in-principle" was a real category error the steelman pass caught and corrected rather than merely noted; (3) a citation to co-emergence's Axiom 3 was simply wrong (Axiom 3 is exclusively about Hilbert-space emergence, not foliations or time coordinates) and is replaced by GGD's own disclosed Assumption (ii) plus ordinary gauge-choice reasoning.

**Attempt B** — the categorical claim ("GGD is structurally exempt — a different kind of object than FPE's response kernel") **did not survive**, on three independently-confirmed grounds: (1) GGD's noise kernel and FPE's response kernel are, per the Hu-Verdaguer closed-time-path formalism both papers cite, the symmetric and antisymmetric projections of *one* underlying construction (a fluctuation–dissipation relation), not different kinds of object — GGD's calculation simply never computes the antisymmetric/dissipative half; (2) GGD's own assumption (iv), "backreaction of decoherence on the noise kernel is neglected," is exactly a self-consistency loop truncated at the first iterate, contradicting "no fixed-point loop anywhere"; (3) the attempt's axiom-check section inverted the valence of its own cited sources — co-emergence's Level-2 definition *is* the covariant fixed-point condition (the opposite of a preferred-frame license), and every foliation-related passage in FPE's own text treats foliation-dependence as a limitation, never an accepted design cost. A genuinely narrower claim survives instead (§3).

## 3. Reconciling the tension: is there a fixed-point loop, or not?

Attempts A and C's surviving claims ("no fixed-point loop, wrong genus for M3 to bind on") and Attempt B's surviving claim ("GGD *is* the zeroth-iterate of the same loop, just truncated") are not actually contradictory once stated precisely, but they describe the same fact at different depths, and the difference matters:

- **"No iteration is performed"** (A/C's claim, verified directly against GGD's text) is true: there is no `while`-loop, no explicit re-solving of the noise kernel against a decohered state.
- **"No iteration loop exists, even conceptually, for GGD's calculation to be one iterate of"** (the stronger reading A/C's original framing implied) is false: GGD's own assumption (iv) explicitly names a state→noise→state feedback that it neglects, not one that doesn't exist.

The honest, corrected synthesis is B's steelman's framing, which subsumes rather than contradicts A/C's structural point: GGD computes the leading-order (zeroth-iterate) term of the same conceptual self-consistency map FPE studies. The *structural* genus-mismatch argument from A/C (GGD's retardation correction touches an unproblematic well-posedness object, never the obstructed response kernel) remains correct and is why the *retardation* question specifically resolves cleanly. But it does not, by itself, establish that GGD's calculation overall is "a different kind of problem" than FPE's — it establishes that the *one piece GGD's derivation actually needs* (propagating a given source through a fixed background) is safe, while a *different* piece GGD's own text gestures at but doesn't rigorously address (whether the truncated backreaction and vacuum-fluctuation terms are genuinely negligible, not just plausibly so) is exactly where a version of FPE's question would need to be answered if ever tightened.

**Practical consequence:** GGD's stated numerical predictions (`τ_coh`, the Gaussian profile, the 3σ discriminability claim) are not threatened by this — the dropped terms are independently estimated at 10⁻³⁵ and 10⁻⁵⁸, dwarfing any plausible concern. But the *rigor label* on that safety should be read precisely: Sketch-level, by order-of-magnitude estimate, not by theorem — which is, encouragingly, already how GGD's own paper is labeled. Nothing here changes GGD's rigor status. What it changes is confidence in *why* GGD is safe, and it closes off a slightly-too-strong framing ("categorically exempt") that three independent attempts initially reached for.

## 4. Meta-finding: convergence is evidence, not proof, when the shared premise goes unchecked

Worth stating plainly as the most transferable lesson of this cycle. All three attempts, working independently and blind to each other, initially converged on treating GGD's assumption (iv) — "backreaction... neglected" — as settling the question of whether a self-consistency loop exists, rather than as an assumption *about* an existing loop that requires its own justification. This is exactly the kind of shared blind spot that independent generation does not, by itself, guard against; it took one of three *attack* passes choosing to verify the Hu-Verdaguer fluctuation-dissipation structure directly (rather than accepting "GGD's kernel is linear, therefore different in kind" at face value) to surface it. Had that specific check not been run — had all three attack passes been satisfied with the surface-level "no iteration in the text" observation — this cycle would have recorded a false convergence. The two-pass attack/steelman discipline adopted 2026-07-18 (per METHODOLOGY's "No Idea Is Eliminated Without a Defense") is what caught this, but it is worth naming that it was caught by one attack pass's initiative, not by the design guaranteeing it — a future cycle's fan-out width or attack instructions could usefully be tuned to require explicitly checking a target paper's own stated assumption list against the "is there really no loop here" claim, rather than leaving that check to chance.

## 5. Two concrete citation/attribution defects found, independent of the main question

Both found by cross-checking the actual `.tex` text against what the fan-out attempts assumed, not by design:

1. **`gaussian-gravitational-decoherence/index.tex` L855-859** (Discussion) states that existence of self-consistent semiclassical solutions is "treated in a companion paper," gesturing at FPE's Theorem 2 (Banach)/Theorem 3 (Schauder) as if they cover GGD's regime. Both of FPE's results explicitly require a compact Cauchy surface and explicitly exclude Minkowski/asymptotically-flat backgrounds (`fixed-point-existence/index.tex` L766-771) — a background class GGD's own setup is squarely in. The passage over-credits the companion paper; what GGD's derivation actually needs (an ordinary classical Newtonian background, plus a linear retarded wave equation's well-posedness) is independently established by standard post-Newtonian GR, not by FPE's Theorem 2/3.
2. **`co-emergence/index.tex` L1964-1967** attributes GGD's gravitational-decoherence timescale result to `\cite{fixed_point}` (i.e., to FPE) — but FPE's own text mentions "decoherence" exactly once, in its own companion-paper disclaimer, and derives no decoherence timescale anywhere. This looks like a citation to the wrong companion paper for that specific claim.

Neither defect affects any numeric result or rigor label. Both are precision corrections, in the same spirit as (though lower-stakes than) today's earlier `melo_dissipative` correction (PR #172).

## 6. Rigor label summary

| Claim | Label |
|---|---|
| GGD's retardation correction is structurally distinct from FPE's obstructed response kernel `K^red` (analogous instead to FPE's unproblematic well-posedness piece) | Sketch — argument is clean, not independently re-derived to full rigor |
| GGD's calculation is the leading-order/zeroth-iterate term of the same conceptual self-consistency map FPE studies, not a categorically different kind of problem | Sketch — the corrected, surviving framing |
| GGD's numerical predictions are unaffected by any finding in this cycle | Rigorous, given GGD's own already-stated order-of-magnitude bounds on the two truncated terms |
| Källén-Lehmann remark resolves M3's *kernel-bound* object on Minkowski specifically; the *full* existence theorem still doesn't reach Minkowski, for the separate reason of compact-Σ/Rellich-Kondrachov | Rigorous, by direct citation, verified against the primary text this session |
| GGD's Discussion (L855-859) over-credits the companion paper's existence results for its own regime | Rigorous (textual fact, both papers directly compared) |
| co-emergence L1964-1967 cites the wrong companion paper for GGD's decoherence timescale | Rigorous (textual fact) |
| If GGD's truncated backreaction/vacuum terms were ever rigorously bounded rather than estimated, that derivation would need to confront a question much closer to FPE's open existence question on Minkowski | Conjecture — plausible, not derived, and correctly flagged as the one place this cycle leaves genuinely open |

## 7. Recommendation

No demotion of any GGD or FPE result — nothing here changes a rigor label. Three concrete, low-risk follow-ups, presented for the experimenter's disposition (not executed by this synthesis):

1. **Two citation-precision corrections** (§5) — small `.tex` fixes, same class as today's earlier `melo_dissipative` correction (PR #172).
2. **A thread-proposal candidate**, if the experimenter wants to route it through the newly-live `explorer`/governor pipeline rather than adjudicate directly here: *rigorously bound (rather than order-of-magnitude estimate) GGD's two truncated self-consistency terms — vacuum-fluctuation contribution to the noise kernel, and backreaction of decoherence on the noise kernel — and determine whether doing so requires confronting FPE's M3 obstruction on Minkowski.* Falsifiable first step: attempt the vacuum-fluctuation bound first (the more tractable of the two, per GGD's own Remark), since it doesn't obviously require FPE's existence machinery at all (it's a stress-tensor coincidence-limit renormalization question, not a self-consistency question).
3. **Process note for whoever tunes `explorer.md` next**: consider whether the attack-pass instructions should explicitly require checking a target paper's own disclosed assumption list line-by-line against any "no loop/no dependency exists" claim a fan-out attempt makes, given that's exactly what one of three attacks here needed to catch a shared blind spot the other two missed.

---

**Process note (interactive-mode disclosure):** This is the first live run of the `explorer` routine's fan-out/attack/steelman cycle, executed interactively (not via the scheduled `autonomy-explorer.yml` cron) at the experimenter's direction, following the same interactive-dry-run precedent as prior same-day Explorations. No GitHub claim, comment, issue, or PR was made by any fan-out/attack/steelman subagent. This synthesis and the citation corrections it recommends are presented for the experimenter's review before any further GitHub action.

routine: interactive (explorer dry run) · model: claude-sonnet-5 (fan-out/attack/steelman subagents + interactive-session synthesis, human-directed, 2026-07-19)
