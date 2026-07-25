---
id: ggd-branch-overlap-kernel
program: gaussian-gravitational-decoherence
tier: speculation
status: dead
statement: >
  Relaxing the orthogonal-branches hypothesis to overlap epsilon, the equal-time
  noise kernel acquires a multiplicative suppression (1 - |epsilon|^2), so
  decoherence is governed by branch distinguishability rather than by the density
  difference alone.
hypotheses:
  - non-relativistic stress-energy operator, definite branch CM positions
  - general complex epsilon
falsifier: recompute without assuming orthogonality; a non-scalar result falsifies
consequence: claimed continuous suppression under partial which-path erasure
provenance: {born: 2026-07-25, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-25
  cause: >
    Four independent failures, of which the first is structural. (1) The
    hypotheses are internally inconsistent: "definite CM position" means an exact
    position eigenstate, for which the overlap is a delta function and is
    identically zero - reaching epsilon = 0.3 requires a wavepacket width
    comparable to the body's own size, not a perturbation. (2) A third Gaussian
    centred at the branch midpoint enters the connected correlator, with no
    counterpart in the density difference, so no scalar prefactor can absorb it.
    (3) The result depends on arg(epsilon), not |epsilon|^2 - at a relative phase
    of pi/2 the entire correction vanishes for ANY overlap magnitude. (4) The
    numerical ratio changes sign, which a factor in [0,1] can never do. Verified
    three independent ways to machine precision; the epsilon = 0 limit reduces
    exactly to the paper's kernel.
  defense_attempted: yes
  defense_findings: >
    The defense tested the one reading neither pass had tried - overlap in an
    internal or pointer degree of freedom, with the CM sector held exactly
    orthogonal, which is the paper's existing hypothesis unrelaxed. That reading
    is internally consistent, and symbolically it gives N_epsilon - N_0000 = 0
    IDENTICALLY for any epsilon: the stress-energy cross terms carry the CM
    factor and never see the internal overlap. So the consistent version confirms
    the kinematic reading rather than rescuing the dynamical one.
    It also deflated the midpoint term: it is the ordinary interference term in
    |alpha phi_1 + beta phi_2|^2, textbook, and double-exponentially suppressed
    at realistic separations.
  wrong_object: >
    The real insight. Branch overlap is KINEMATIC - it reduces the achievable
    initial coherence, present even with gravity switched off - not a rescaling
    of the noise kernel that sets the decay rate. See the hardening note below.
---

**What survives is a hardening note, deliberately NOT a claim node.** The defense
was explicit that a true-but-inert scoping statement should not enter the graph:

State-preparation branch overlap is provably orthogonal to the paper's profile
discriminant. That discriminant is a ratio normalised by the initial coherence,
so any common prefactor cancels identically - and this is physical rather than
algebraic coincidence, since the same apparatus produces both hypothetical curves
being compared. Its only observable trace is an increased shot budget through
reduced fringe contrast.

The functional form is also settled against the speculation: the
Englert-Greenberger-Yasin relation gives visibility LINEAR in overlap, not
quadratic-complement. Verified through a secondary rendering after the primary
PDF extraction failed - the same failure mode already logged on
[[ggd-noise-kernel]] - so it is exploratory tier and would need source
verification before entering a bibliography.
