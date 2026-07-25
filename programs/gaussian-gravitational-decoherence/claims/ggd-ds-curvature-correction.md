---
id: ggd-ds-curvature-correction
program: gaussian-gravitational-decoherence
tier: speculation
status: dead
statement: >
  On the framework's own trace-anomaly de Sitter fixed point, the GGD noise
  kernel acquires a leading curvature correction
  N_dS = N_flat * [1 + kappa (H0 L / c)^2 + O((H0 L/c)^4)] for branch separation
  L, with kappa a fixed O(1) coefficient set by the departure of the de Sitter
  retarded Green function from flat 1/r.
hypotheses:
  - the hypotheses of ggd-noise-kernel
  - embedding in the exact de Sitter fixed point of fpe-starobinsky-existence
falsifier: >
  Compute the linearized stress-tensor two-point function on exact de Sitter to
  leading order and check whether kappa vanishes.
consequence: >
  Would have tied a cosmological parameter fixed by the framework's own anomaly
  coefficient to a laboratory decoherence observable.
provenance: {born: 2026-07-24, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-24
  cause: >
    Category error. N_0000 = (c^4/4) dRho(x) dRho(x') is a pointwise product of
    local densities with no propagator and no integral in it; the Green function
    enters only downstream in U(x) and E_Delta. There is nothing in the kernel
    for a Green-function correction to modify.
  defense_attempted: yes
  defense_findings: >
    The defense relocated the claim onto the downstream objects where the Green
    function does live, and computed it. The leading correction is EXACTLY ZERO
    at Newtonian order, for a structural reason neither pass anticipated: the
    Lambda-sourced term in the modified Poisson equation is a uniform background
    independent of rho, present even at rho = 0, so it is identical regardless
    of dRho's configuration and cancels identically in any dRho-linear
    functional. The matter-sourced Green function is unmodified. Verified two
    independent ways - from the exact Schwarzschild-de Sitter metric function,
    and from the standard Newtonian-cosmology-with-Lambda treatment.
  secondary_cause: >
    Independently fatal on timescale. Combining the Planck-adjacent H0 with the
    paper's own Rigorous-by-citation instability, a quasi-de Sitter stage at
    that curvature lasts ~1e-42 to 1e-40 s - 39 to 45 orders of magnitude
    shorter than the fastest platform in GGD's own table. The background does not
    survive long enough to host an apparatus even in principle.
  attack_correction: >
    The defense also corrected the attack: graviton-propagator gauge ambiguity
    is a quantized-graviton issue, and this calculation is classical throughout.
    Right bottom line, wrong mechanism.
---

Dead, but it produced two things that outlive it: the dimensional-convention
defect recorded on [[fpe-starobinsky-coefficient]], and the scope claim
[[fpe-fixed-point-is-inflationary]].

Worth recording the trap that caused it: H0 is exactly the symbol conventionally
used for the present-day Hubble constant, and this speculation silently used the
observed value where the framework's own is ~60 orders of magnitude larger.
