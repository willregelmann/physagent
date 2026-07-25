---
id: ce-feigenbaum-cascade
program: co-emergence
tier: speculation
status: dead
statement: >
  Past F_toy's first flip bifurcation the iteration undergoes a period-doubling
  cascade converging at the Feigenbaum ratio 4.6692, terminating in a chaotic
  positive-Lyapunov regime.
object: {name: F_toy, space: the probability simplex}
hypotheses:
  - gamma fixed, h fixed, beta swept past the first flip
  - A symmetric
falsifier: >
  Track the bifurcation points and compute successive ratios; no convergence
  near 4.6692 falsifies.
consequence: >
  A chaotic regime would mean self-consistency selects no configuration at all
  at strong coupling.
provenance: {born: 2026-07-25, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-25
  cause: >
    No cascade exists. Beta swept from 0.6 to 200,000 - five orders of magnitude
    - plus ~390 multistart trials: the period is always exactly 1 or exactly 2,
    never 4, never 8, never aperiodic. The attracting orbit's spectral radius
    DECREASES with beta (0.97 near onset to ~0.037 by beta ~ 50, flat to 2e5),
    so there is no structural room for a period-4 bifurcation anywhere in range.
    An independent Benettin computation found the maximal Lyapunov exponent
    negative everywhere tested, flatly contradicting the chaotic-regime claim.
  attack_corrected_the_brief: >
    The dispatching brief argued the 1-D unimodal reduction Feigenbaum requires
    probably fails here, citing the beta=40 spectrum {0, -41.9, -40.1, -39.6} as
    three eigenvalues near -1. The attack found that spectrum belongs to the
    REPELLING fixed point, not the attracting cycle - a conflation. The flip at
    beta = 0.648020 is a clean single-eigenvalue crossing, so the reduction does
    hold. The brief's sharpest axis was wrong and the attack said so.
  defense_attempted: yes
  defense_findings: >
    Generality extended to 9 further instances up to N = 16 with ~1400 more
    trials: zero exceptions at any N. The defense then explained the cap, which
    neither the speculation nor the attack could - see
    [[ce-second-iterate-real-spectrum]]. There was never a structural reason to
    expect Feigenbaum universality, because the algebraic protection that keeps
    the first doubling clean provably does not recur at the second.
---

The most productive death of either cycle. Its investigation produced
[[ce-second-iterate-real-spectrum]] and three corrections to
[[ce-riem-classical-unique]].
