---
id: ggd-material-crossover
program: gaussian-gravitational-decoherence
tier: conjecture
status: live
statement: >
  A finite phonon correlation time tau_c ~ 1/omega_phonon enters the noise
  kernel, so the coherence exponent crosses over from C_V(0) t^2 (Gaussian) at
  t << tau_c to 2 C_V(0) tau_c t (linear/exponential) at t >> tau_c, making the
  decoherence profile material-dependent.
object:
  name: coherence exponent under exponentially-correlated noise
  space: the Einstein-Langevin model with finite correlation time
hypotheses:
  - exponentially-correlated noise, C_V(tau) = C_V(0) exp(-|tau|/tau_c)
  - the identification tau_c ~ 1/omega_phonon
falsifier: >
  A measured decoherence profile whose shape does not track the predicted
  branch for the platform's omega_phonon/omega_g ratio.
consequence: >
  Determines which platforms should show Gaussian versus exponential profiles,
  and therefore whether Result 2's Gaussian prediction is safe on current
  hardware.
novelty:
  status: independent-rederivation
  searched: 2026-07-25
  found: []
  note: >
    SPLIT.
    THE CROSSOVER FORMULA IS PRIOR ART and textbook - and the paper cites
    nothing for it, which is a citation gap in merged content. Canonical chain:
    P. W. Anderson, J. Phys. Soc. Jpn. 9, 316 (1954); R. Kubo, J. Phys. Soc.
    Jpn. 9, 935 (1954); and R. Kubo, "A Stochastic Theory of Line Shape", Adv.
    Chem. Phys. 15, 101 (1969), which gives the exact relaxation function
    Phi(t) = exp[-Delta^2 tau_c^2 (exp(-t/tau_c) - 1 + t/tau_c)] - quadratic
    exponent at short t, linear at long t, precisely the printed case structure.
    For the decay rather than lineshape framing: Klauder and Anderson, Phys. Rev.
    125, 912 (1962). The mathematics was verified at full text through an
    independent modern rederivation (cond-mat/0401519 eq. 7) since the 1950s
    originals are not fetchable.
    THE m_star THRESHOLD IS NOVEL. Nothing found equates the lowest acoustic
    phonon frequency to the gravitational coherence frequency, uses the shared
    1/R scaling to cancel the radius, and obtains a single size-independent
    critical mass. Closest prior work, and an honest neighbour: Diosi,
    arXiv:1404.6644 (2014), asks the structurally similar question - do internal
    acoustic modes matter for DP decoherence - but yields a critical WAVELENGTH
    from a fixed nuclear-oscillator frequency, with no sound-speed dependence and
    no E_Delta construction. Adjacent question, different construction.
    Also checked and rejected as a coincidence: sqrt(hbar c_s / G), a Planck mass
    with sound speed substituted for c, does appear in the analog-gravity
    literature (arXiv:1907.02902) in a physically unconnected context. A
    dimensional match, not prior art.
  territory: >
    The field's standard review (Bassi, Grossardt and Ulbricht, arXiv:1706.05677)
    was full-text-checked for phonon, rigid-body and internal-structure content
    and has NONE. Adjacent work exists (Diosi 2014, Quach 2017, Aguiar and Matsas
    2025) but the specific construction does not.
  citations_owed:
    - >
      Kubo, Adv. Chem. Phys. 15, 101 (1969) as primary for the crossover, with
      Anderson (1954) and Kubo (1954) as the foundational pair. These predate
      arXiv and Crossref, so check resolution against tools/verify_citations.py
      before they enter the bibliography - this repository has already been
      bitten in both directions, by a resolving citation that was wrong (geroch)
      and a correct one that would not resolve.
    - >
      Diosi arXiv:1404.6644 as an explicit "related but distinct" reference near
      the m_star discussion.
tex: {file: programs/gaussian-gravitational-decoherence/index.tex, label: eq:crossover}
provenance: {born: 2026-07-25, born_by: adversary}
defects:
  - id: directional-inversion
    found: 2026-07-25
    by: adversary
    severity: correctness
    status: RESOLVED 2026-07-25 - direction withdrawn, see resolution
    finding: >
      The formula is correct; its directional interpretation is inverted
      everywhere it is applied. Independently re-derived twice by sympy:
      I(t) = 2 C_V(0) tau_c [tau_c + (t - tau_c) exp(t/tau_c)] exp(-t/tau_c),
      giving Gaussian at t << tau_c and linear at t >> tau_c - which matches the
      printed formula and standard Kubo-Anderson motional narrowing. With
      tau_c ~ 1/omega_phonon and any external timescale t, omega_phonon >> omega_g
      means t >> tau_c, i.e. the LINEAR branch. The paper asserts the opposite.
    timescale_independent_form: >
      The inversion does not depend on which t is chosen. Take omega_phonon to
      infinity - the literal rigid-body limit - at any fixed finite external time
      (tau_DP, tau_coh, or total run time, none of which depend on omega_phonon).
      Then tau_c goes to zero and t/tau_c diverges unconditionally. The inversion
      is structural to the tau_c ~ 1/omega_phonon identification itself.
    paper_contradicts_itself: >
      Decisive and needing no external literature. The section on static noise
      (~lines 296-310), two pages BEFORE this conjecture, states that finite or
      short tau_c gives exponential decay and tau_c -> infinity gives Gaussian.
      The material-dependent transition section (~681-707), applying the
      IDENTICAL formula with tau_c ~ 1/omega_phonon substituted, asserts that
      high omega_phonon - which by its own identification means SHORT tau_c -
      gives Gaussian. The same paper gives opposite limiting behaviour for the
      same formula.
    root_cause: >
      "Rigid" was read as a synonym for "static" in the colloquial sense - a
      stiff lattice barely moves. But the formal object built for it,
      tau_c ~ 1/omega_phonon, makes rigid bodies SHORT-tau_c, which is the
      mathematical opposite of static (tau_c -> infinity) in the framework the
      paper sets up two pages earlier.
    locations: >
      Six, not five: the transition-section intro (~684-690); the platform table
      caption (~502-503); the "Restriction of Conjecture 1" paragraph (~772-780);
      the abstract (~47-54); README.md, both the plain-English paragraph and
      Results item 3; and - found by the defense pass - this conjecture's OWN
      qualitative sentence (~705-706), which says lower-rigidity bodies drift
      from Gaussian toward exponential. Lower rigidity means longer tau_c, hence
      MORE static under the conjecture's own math.
    defense_attempted: yes
    strongest_defense: >
      Amplitude suppression rather than time-averaging. For a quantum harmonic
      oscillator <x^2> -> hbar/(2 m omega_phonon), so a stiffer body's internal
      modes genuinely have SMALLER fluctuation amplitude, not merely faster
      fluctuation. If the phonon contribution were a small additive term riding
      on Result 2's dominant static rigid-body term, a stiff body's total profile
      could remain Gaussian even with the phonon sub-term in its own linear
      regime - and that would dissolve the Result 2 tension by construction.
      This is physically real and is the best case available. It is also
      TEXTUALLY ABSENT: the crossover-threshold and two-material derivations are
      pure frequency-ratio comparisons with no amplitude or variance factor
      anywhere, m_* carries no zero-point-fluctuation term, and nobody has
      computed the phonon-to-static amplitude ratio for real diamond. Reading it
      in requires supplying a derivation that does not exist.
    scope:
      formula_eq_692_703: survives unchanged - the algebra is correct
      qualitative_sentence_705_706: inverted; withdraw or flip
      accessibility_verdict_716_788: inverted throughout; a demotion, not a copy-edit
      abstract_and_readme: restate the inverted claim; must change with the above
      m_star_eq_740: untouched - it is the locus where the frequencies cross, symmetric in direction
    consequence_if_taken_literally: >
      Corrected, this conjecture predicts EXPONENTIAL decoherence for the same
      BMV microdiamond that Result 2 predicts GAUSSIAN decoherence for - a direct
      conjecture-versus-result conflict about one body, where the paper currently
      claims no discriminating prediction and consistency with Result 2.
    resolution: >
      Experimenter decision, 2026-07-25: tau_c ~ 1/omega_phonon was a PLACEHOLDER
      pending the paper's own admitted open phonon-spectrum problem, not a literal
      identification. The direction is therefore WITHDRAWN rather than flipped -
      flipping would assert a physical claim the formula alone does not support,
      given that a different candidate mechanism (amplitude suppression) would
      give the opposite direction and neither is derived.
      Applied: the formula and m_* are kept unchanged; the directional sentence in
      the conjecture is withdrawn; the accessibility verdict is retracted as
      overreach beyond what is derived; the abstract, both README locations, the
      table caption and the Limitations paragraph state the direction as
      undetermined rather than asserting either branch. A withdrawal note in the
      paper records what was claimed, why it was wrong, and why it was not simply
      flipped.
    also_unresolved: >
      Whether tau_c for the phonon channel is the oscillation period
      ~1/omega_phonon, as written, or damping-limited ~Q/omega_phonon. Good
      crystal resonators reach Q ~ 1e6 to 1e10, which would move t/tau_c by six
      to ten orders of magnitude and could change the verdict on its own.
not_affected:
  - >
    ggd-single-realization. Its staticity rests on the wavepacket-spreading
    margin (~5e14), which uses only m, d, hbar and tau_coh; omega_phonon never
    appears in that derivation and first occurs in the paper well after it.
    Verified independently by both passes.
---

**Open correctness defect in merged content, reaching the abstract and the
README.** Found not by a verification pass over the paper but as a byproduct of
adversarially investigating an unrelated speculation
([[ggd-cpmg-degeneracy]]), which is the fourth time in two generative cycles
that a defect in standing content has surfaced this way.

The attack and defense passes agree on the finding and reached it by independent
routes; the defense additionally caught a transcription slip in the attack's own
formula (a factor of tau_c where tau_c^2 belongs, dimensionally short by one
power of time), which does not affect the limits.

**Resolved 2026-07-25.** The direction is withdrawn, not flipped. The formula,
the frequency-crossing threshold and `m_*` are untouched; the accessibility
verdict is retracted as overreach. A withdrawal note in the paper records what
was claimed, why it was wrong, and why flipping it would have been a second
unsupported assertion rather than a fix.

Still open, and now stated as such in the paper: whether `tau_c` for the phonon
channel is the oscillation period as written or damping-limited `~Q/omega_phonon`
(six to ten orders of magnitude apart for good crystal resonators), and whether
the intended mechanism was amplitude suppression rather than time-averaging.
Either would fix the direction; neither is derived.
