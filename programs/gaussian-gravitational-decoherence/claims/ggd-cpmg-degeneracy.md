---
id: ggd-cpmg-degeneracy
program: gaussian-gravitational-decoherence
tier: speculation
status: dead
statement: >
  Because the noise field is exactly static within a realization, an n-pulse
  CPMG sequence recovers coherence no better than a single Hahn echo for any n,
  unlike ordinary 1/f dephasing where higher-order sequences generically win.
hypotheses:
  - the Einstein-Langevin model with the static kernel
  - any balanced pulse sequence
falsifier: any observed n-dependence of the residual
consequence: claimed a discriminant orthogonal to the existing profile test
provenance: {born: 2026-07-25, born_by: generator}
disposition:
  outcome: killed
  date: 2026-07-25
  cause: >
    Vacuous as stated. Under the paper's own static kernel the noise PSD is a
    delta at zero frequency, and the filter-function limit is ZERO for Hahn and
    every CPMG-n alike - not "no better", identically zero for all, by the
    definition of refocusing. Zero decay is the floor, not a target CPMG could
    undercut, so no measurement inside that regime could show CPMG winning.
  defense_attempted: yes
  defense_findings: >
    The defense corrected the attack's exponents - the z^4/(128 n^4) law is an
    artifact of the 1/f IR-cutoff convention, and against a Lorentzian PSD (which
    is what this paper's own crossover formula describes) the law is z/(6 n^2).
    It then answered the reframing quantitatively and negatively. The sensitive
    window is z = t/tau_c ~ O(0.1-10). The phonon candidate gives z ~ 1.3e8,
    eight orders past it; the wavepacket-spreading bound gives z ~ 2e-15, fifteen
    orders short. The two candidates sit on opposite sides, ~23 orders apart, and
    z does not depend on n at all - so no achievable n bridges it. Residual
    signal ~1e-8 against a floor needing ~1e16 shots: short by 13 orders. The
    realizability limit on pulse count never even comes into play.
  what_is_true_and_why: >
    The literal text is true for these platforms, but for a mundane reason
    rather than the intended one. NOT "echo trains structurally cannot beat Hahn
    for static-type noise" - that is false in general, and CPMG demonstrably beats
    Hahn for colored noise with tau_c in range. Rather: both candidate tau_c
    values are so far outside the window that Hahn, CPMG-2 and CPMG-infinity are
    mutually indistinguishable.
  odd_even_asymmetry: >
    A real structural feature the defense derived and correctly scoped: odd n
    gives F ~ x^4/(64 n^4), even n gives x^6/(256 n^4) - an extra factor of x^2
    cancellation odd n does not get. It matters for 1/f-type peaked spectra
    (Table-1-style numbers are implicitly even-n) and washes out against a
    Lorentzian.
---

The stronger positive restatement, already effectively in the paper: a single
Hahn echo is not merely as good as CPMG, it is **exhaustive** - it already
achieves complete refocusing, so nothing remains for any n > 1 protocol to
improve.

**Surfaced but NOT certified, and requiring its own adversarial pass:** a possible
directional inconsistency in the paper's material-dependent-crossover conjecture.
Its crossover formula puts the Gaussian/static branch at t << tau_c and the
exponential branch at t >> tau_c (standard Kubo-Anderson motional narrowing);
with the conjecture's own tau_c ~ 1/omega_phonon that makes t >> tau_c equivalent
to omega_phonon >> omega_g. But the two-material evaluation asserts the opposite -
that omega_phonon >> omega_g is where the static result safely applies. The
defense listed three possibilities (real error, labelling mismatch, its own
misreading) and declined to certify any. It does NOT threaten
[[ggd-single-realization]], whose staticity rests on the wavepacket-spreading
margin rather than the phonon mechanism.
