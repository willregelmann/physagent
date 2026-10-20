---
id: ggd-cpmg-odd-even-colored-asymmetry
program: gaussian-gravitational-decoherence
tier: speculation
status: live
statement: >
  Against a genuinely colored (non-static, non-delta-PSD) gravitational noise
  spectrum with a finite correlation time - unlike the exactly-static kernel
  that made ggd-cpmg-degeneracy vacuous - CPMG-n coherence recovery shows a
  measurable odd/even asymmetry in the pulse count n: odd-n filter functions
  retain a residual x^2 factor (F ~ x^4 / (64 n^4)) that even-n sequences
  algebraically cancel (F ~ x^6 / (256 n^4)), so two CPMG sequences with
  matched total duration and pulse spacing but n and n+1 pulses would show
  measurably different coherence-recovery magnitudes, providing a diagnostic
  of the noise spectrum's shape that does not require resolving which
  mechanism sets its correlation time.
object:
  name: filter-function overlap integral for a CPMG-n sequence against a colored noise power spectral density
  space: single-qubit (or matter-wave interferometer) coherence under the Einstein-Langevin Gaussian-noise model already adopted by this program
hypotheses:
  - the noise kernel has some genuinely finite correlation time tau_c (i.e. is not the exactly-static single-realization kernel of ggd-single-realization)
  - CPMG pulse sequences with n and n+1 pulses at matched total duration T and matched inter-pulse spacing T/n vs T/(n+1)
  - the power spectral density is colored (not white, not an exact Lorentzian where the asymmetry may wash out - see falsifier)
depends_on:
  - id: ggd-cpmg-degeneracy
    role: context
    transfers: same-object
    justification: >
      Same object (CPMG filter functions against this program's noise
      kernel), explicitly a different regime. The dead claim's own defense
      pass derived the odd/even structural finding used here (odd n gives
      F ~ x^4/(64 n^4), even n gives x^6/(256 n^4)) but only evaluated it
      against the exactly-static kernel, where the PSD is a delta function
      at zero frequency and every sequence (odd or even, any n) gives
      identically zero filter response - the degeneracy that killed the
      claim. This speculation asks whether the same structural asymmetry
      survives once the kernel is genuinely colored, a regime the dead claim
      never reached.
falsifier: >
  Compute the filter-function overlap integral for a specific colored PSD
  (the Lorentzian crossover form entering ggd-material-crossover, or a
  generic 1/f^alpha form) at matched n and n+1. If the ratio
  F_odd(n) / F_even(n) tends to 1 as the spectral content moves away from the
  IR-cutoff-dominated regime where the dead claim's law was derived - i.e.
  the odd/even structural difference is subleading to the overall n^-4 decay
  common to both parities for realistic tau_c - the diagnostic is falsified
  as practically useless, independent of whether the asymmetry exists in
  principle.
consequence: >
  If the asymmetry survives at a computable magnitude, it gives an
  experimentally accessible pulse-count-parity diagnostic for the shape of
  the gravitational noise spectrum that is orthogonal to, and available
  before, the open GGD-1 material-crossover question - it needs only that
  some finite tau_c exists, not which phonon (or other) mechanism sets it.
  If it washes out, that sharpens ggd-cpmg-degeneracy's negative result: the
  odd/even structure found there would then be an artifact of the IR-cutoff
  convention specifically, not a generic feature of pulse-sequence filtering
  against colored gravitational noise.
provenance: {born: 2026-08-03, born_by: generator}
---

Mined directly from [[ggd-cpmg-degeneracy]]'s tombstone: its defense pass
derived the odd/even structural finding as a correction to the attacking
pass's exponents, in service of showing the degeneracy claim was vacuous under
a static kernel - but the structural finding itself was never evaluated
against any colored spectrum, only flagged as mattering "for 1/f-type peaked
spectra" and washing out "against a Lorentzian" in the one comparison made.
That comparison was for a single fixed n, not the n-vs-(n+1) asymmetry
proposed here.

Axiom check: this stays entirely within the program's existing
Einstein-Langevin / Gaussian-noise Assumption 1 and the Diosi-Penrose-style
kernel already adopted; it introduces no new background structure, preferred
frame, or foliation. It is conditional on the currently open question of
whether tau_c is finite at all (GGD-1, halted under needs-human) but is
explicitly agnostic to which mechanism sets tau_c - phonon, amplitude
suppression, or otherwise - unlike that milestone, which turns on identifying
the mechanism. This claim would still need that some finite-tau_c regime
exists to have any content; if GGD-1 resolves toward "no accessible platform
reaches the crossover," this speculation would be moot for realistic
platforms even if its filter-function mathematics is correct in principle.
