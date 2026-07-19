# Attempt A: Stationary/frequency-domain Green's-function reduction

**Question:** Does GGD's "stationary matter" noise-kernel approximation sit safely inside a regime where FPE's M3 obstruction doesn't apply, or would restoring genuine retardation reintroduce the same causal-kernel difficulty?

**Technique:** stationary scattering / frequency-domain reduction of retarded Green's functions.

## Findings (as originally submitted)

**Technique used:** stationary scattering / frequency-domain reduction of retarded Green's functions (Fourier transform in time of a time-translation-invariant hyperbolic problem into a family of frequency-indexed elliptic resolvent problems). This is a genuine, standard technique (Titchmarsh's theorem — causality of a retarded Green's function is equivalent to analyticity of its temporal Fourier transform in the upper-half frequency plane, giving outgoing-wave Helmholtz resolvents `(∇² + (ω/c)² + i0^+)^{-1}` at each real ω; standard in quasinormal-mode analysis and stationary scattering theory). Flagged: general physics/math knowledge, not verified against a specific citation in this session.

### 1. Does GGD's actual setup qualify for the reduction?

GGD's text (`index.tex` L259–275) states the stationary approximation as a within-window claim (spreading time ≈6×10¹² s vs τ_coh ≈13 ms, margin ~5×10¹⁴). A strict frequency-domain reduction requires eternal stationarity; GGD's actual process is transient (prepared, held, measured). The technique degrades gracefully into the correct one: the near-zone/quasi-static expansion of a retarded potential, licensed whenever the light-crossing time across the source is short compared to the source's own timescale of change. Conclusion (Sketch): GGD's static approximation is well-justified as the leading term of a near-zone expansion, not as exact eternal stationarity. GGD's repeated bare "O(v²/c²)" assertion is consistent with this but not derived anywhere — a genuine gap in the paper, independent of the FPE question.

### 2. Does the reduction sidestep M3, or relocate it?

FPE's K(x,y) = δ⟨T̂(x)⟩/δg(y) is a response/susceptibility kernel entering a self-consistency fixed-point map, needing a uniform bound over a compact family of backgrounds — M3 is that its causal-past support defeats the needed spacelike-decay bound. GGD's N₀₀₀₀ is a prescribed two-point correlator of a fixed quantum state, entering linearly as a noise source with backreaction explicitly neglected (Assumption iv) — no fixed-point iteration anywhere. Restoring retardation reinstates the ordinary causal Green's function (unavoidable, general fact) but not M3's *specific* obstruction: no self-consistency loop, wrong background class (FPE's machinery explicitly excludes Minkowski/asymptotically-flat, L85/L769-770), and no spectral-gap-on-Σ object in GGD at all.

### 3. Axiom check

Treating GGD's setup as "stationary enough" doesn't smuggle a new preferred-frame assumption — the Newtonian-limit scaffolding already presupposes an asymptotically flat background with a preferred rest frame; exploiting Minkowski's exact global timelike Killing vector draws on that already-adopted structure, not an additional layer.

### 4. Verdict

GGD's static-kernel approximation is safe against M3 — because it is the wrong genus of problem for M3 to bind on (no fixed point, no compact-Σ, wrong background class), not because FPE's existing machinery affirmatively covers it.

### Underspecified

Did not derive the O(v²/c²) claim explicitly. If GGD ever generalizes to a genuinely self-consistent, iterated, curved-background version, that hypothetical would confront something much closer to M3.

---
*Status after attack + steelman: core claim (genus mismatch, no fixed-point loop for M3 to obstruct) SURVIVES, narrowed. The specific retardation/frequency-domain technique was WITHDRAWN (checked against a reconstructed relativistic completion of GGD not present in the actual elliptic text; contained a real inequality-direction error). See `steelman-A.md` for the corrected surviving claim, and the synthesis document for how this reconciles with Attempt B's steelman.*
