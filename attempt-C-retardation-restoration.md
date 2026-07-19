# Attempt C: Direct retardation-expansion estimate

**Question:** Does GGD's "stationary matter" noise-kernel approximation sit safely inside a regime where FPE's M3 obstruction doesn't apply, or would restoring genuine retardation reintroduce the same causal-kernel difficulty?

**Technique:** direct perturbative estimate of GGD's own noise kernel's retardation expansion, compared term-by-term against FPE's M3 object.

## Findings (as originally submitted)

### 1. Local vs. non-local retardation correction

GGD's staticity claim has two pieces: (a) N₀₀₀₀ is time-independent because Δρ is frozen over the relevant window (non-relativistic wavepacket-spreading argument, nothing to do with retardation); (b) retardation proper enters the source-to-field map, eq:poisson_stochastic — exact retarded solution of □h̄₀₀ ∝ ξ₀₀ (massless wave equation on flat Minkowski), Taylor-expanded in retarded time gives the standard near-zone/PN multipole series, every term evaluated at a single instant t (local, not a history-integral). The flat massless retarded Green's function obeys Huygens' principle — sharp light-cone support, no tail. Contrast with M3's object: massive field on general curved background, Huygens' principle fails, support fills the closed causal past. GGD's regime lacks both ingredients (massless propagator, flat background).

### 2. Size, and does it compound the existing gap?

(v/c)² ~ 10⁻⁹ (speed of sound) to 10⁻²⁵ (wavepacket-spreading rate) for the microdiamond — many orders smaller than the O(1) Gaussian-noise gap already capping GGD at Sketch, and much smaller than GGD's own backreaction-negligibility bound (~10⁻³⁵). Parametrically decoupled from the Gaussian-noise gap.

### 3. Preferred-frame check

Defining "leading order in v/c" needs a global time coordinate — but this is the same lab-frame coordinate GGD's derivation already commits to from the start (Newtonian limit, decoherence integral), not a new assumption. Checked against Axioms 1-3: Axiom 2 forbids a preferred foliation at the fundamental level, Axiom 3 licenses derived/effective descriptions — GGD's framing as a non-relativistic effective approximation sits inside that exception.

### Load-bearing structural point

FPE's kernel_bound lemma bounds a functional-derivative/self-consistency operator uniformly over a ball of background metrics, to close a Banach fixed point. GGD's noise kernel is a two-point correlation function of a fixed, prescribed state, entering linearly, backreaction explicitly neglected (assumption iv) — no fixed point, no ball of metrics, no uniform bound needed. The companion-paper link is precisely the boundary: that self-consistency problem is where M3 would bite; GGD declines to enter it.

### One-paragraph verdict

The retardation correction is local/tame, no M3-type difficulty at any relevant order. GGD's staticity rests on non-relativistic wavepacket stationarity (separate from retardation); its retardation claim is a Taylor expansion of a Huygens-clean, flat, massless-wave-equation retarded propagator — a strictly local derivative series, qualitatively different from M3's object. Even granting relevance, the size is vastly smaller than GGD's existing O(1) gap. The lab-frame time-slicing is not new.

### Underspecified

Did not make the multipole-series convergence rigorous for GGD's specific Δρ profiles. The claim that GGD's flat-background choice carries no curvature-tail contamination is argued via the paper's own compactness bound rather than independently derived.

---
*Status after attack + steelman: core claim SURVIVES, narrowed. Corrections required: (1) the categorical "no tail at all" claim overclaimed against real PN tail-term physics (hereditary tails exist, first at 1.5PN, still numerically negligible here) — walked back to "no tail at the order GGD computes"; (2) the size-vs-boundedness fallback in the Verdict was dropped as not load-bearing once the correct structural argument (GGD's correction is analogous to FPE's unproblematic well-posedness piece C_inv, never the obstructed response kernel) is used instead; (3) the Axiom 3 citation was WRONG (Axiom 3 is about Hilbert-space emergence only, not foliations) and needs replacing with GGD's own disclosed Assumption (ii) plus ordinary gauge-choice reasoning. See `steelman-C.md` and the synthesis document.*
