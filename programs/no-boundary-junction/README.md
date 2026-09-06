# Self-Consistency at a No-Boundary Signature-Change Junction

**Status:** Early notes (experimenter-priority program, promoted directly on 2026-09-05; tracking issue #215)

## In plain English

Take the framework's timeless, purely spatial four-dimensional block and read it as the "Euclidean cap" of a no-boundary universe: a smooth, edgeless region with no time direction, out of which ordinary spacetime histories emerge across a border where the time direction switches on. This program asks what the framework's own consistency condition says *at that border* — which surface it is, what it fixes, and what it leaves free. So far the record establishes mostly what the border does not do. It does not by itself produce any energy scale other than the one the framework already had (the curvature of the cap), so it cannot explain on its own why particle masses are so far below that scale; what it would need is a dimensionless coupling fixed at the border, and the record contains no rule that fixes one (established in a structured three-way debate, each line surviving adversarial review only as this negative). The cap the framework's own equations produce is at the Planck scale for realistic matter content and becomes trustworthy only with enormously many fields, an input this program states rather than derives (a rigorous arithmetic fact). How long the emerging universe lingers near the cap before its instability takes over is not a property of the cap either; it is set by a second free number in the framework's gravitational sector (a sketch-level result). The program's first real question was therefore whether the border constrains that second number. It does, but as a ceiling rather than a value: above a threshold the no-boundary state is dominated by a second, smaller cap whose universe collapses almost at once, so a single well-behaved cap requires the second number to be small, and then the emerging universe lingers near the cap for only a handful of doublings (a numerical result within the simplest cosmological setting; whether it survives a different rule for adding up caps is an open question). Everything about deriving quantum mechanics, time, or the arrow of time from the border remains conjecture and is labelled as such.

## Scope

Self-consistency of the semiclassical Einstein equation at a signature-change junction between a no-boundary Euclidean cap (the framework's anomaly-driven de Sitter fixed point, continued to the round S⁴) and the Lorentzian classical branches that emerge from it. The program is:

- **downstream of `signature-change-boundary`**, whose fixed-background results (benign crossing; junction regularity; in the smooth class, vanishing extrinsic curvature) it uses as kinematic input and does not re-derive;
- **downstream of `fixed-point-existence`**, whose exact anomaly-driven fixed point supplies the cap (existence and instability Rigorous by citation; coefficient Sketch, with the convention now reconciled — see `notes/2026-09-05-step0-which-junction.md` §1);
- **upstream of `co-emergence`'s** mass, local-time and local-Hilbert-space questions, to which it hands junction-side results (the reframing's proposals for Osterwalder–Schrader reconstruction across the derived junction, WKB time on the branches, and a causal-order orientation are conjectures here, milestoned as J-4 to J-6).

**Standing assumption of the program (explicit input, not a result):** conformal field content with a₂ ≡ (N_S + 11N_F + 62N_V)/2 ≥ 10⁶, so that the cap is semiclassical (H₀ ≤ 0.1 M̄_P). Results depending on a₂ are stated as functions of a₂ with validity ranges. The alternative junctions — the observed cosmological constant (not a fixed point of anything on record) and a Planckian cap with Standard-Model content (outside semiclassical validity) — were considered and rejected at step 0.

## Current contents

- `notes/2026-09-06-j1-root-uniqueness-bounds-the-boxR-coefficient.md` — J-1: the junction constrains the □R / R² coefficient through root dominance: the sphere is a real junction for every ε, but above ε_c ∈ (0.35, 0.36) a symmetric double bubble is a second real junction with lower Euclidean action whose continuation recollapses; the sphere is the unique dominant root iff ε < ε_c, which caps the root's depth at a few e-folds (Rigorous (numerical) for the caps and actions; Sketch for dominance, which assumes Euclidean weighting).
- `notes/2026-09-05-step0-which-junction.md` — step 0 of #215: the two coefficient conventions reconciled (the recorded 16π discrepancy is 8π × 2; Rigorous arithmetic); the junction is Planckian for Standard-Model content and semiclassical only for a₂ ≳ 1.4 × 10⁶ (Rigorous arithmetic; threshold a convention); the de Sitter depth of the root is N_inf ≈ 3(H₀²/M²) ln(M_P/H₀), set by the free □R / R² coefficient that also defines the scalaron mass M — not by the fixed point (algebra Rigorous, seed estimate Sketch); commitment to the anomaly junction with large field content.
- The explorer synthesis that produced the program, `programs/co-emergence/explorations/2026-09-05-junction-mass-scale.md` (PR #216): the mass test answered "no from (Λ, G) alone" with the residue named (one dimensionless coupling per additional scale); the elimination ledger; and three side results (toy-model fixed-point uniqueness, Rigorous; period cap at 2, Rigorous; smooth-class junction condition, Rigorous given background). Full record on `scratch/explorer/2026-09-05-junction-mass-scale`.

## Key results

| Result | Status | Source |
|---|---|---|
| The no-boundary junction with free matter carries exactly one continuous dimensionless number, ε_J = (H₀/M_P)² = 180π/a₂; every other branch scale is M_P × (function of a coupling); no selection principle for any coupling is on record | Sketch (components Rigorous) | #216 synthesis §3 |
| K_Σ = 0 is forced in both gluings (reality condition; Hayward/Kossowski–Kriele and curvature regularity in the smooth class) | Rigorous, given fixed background and smoothness | #216 synthesis §3, §6c |
| H₀² = 180π/(G a₂) = 2880π² M̄_P²/(N_S + 11N_F + 62N_V); the printed coefficient is standard | Rigorous arithmetic, given the standard anomaly coefficients | step-0 note §1 |
| Standard-Model content gives H₀ ≈ 5.3 M̄_P; semiclassical cap needs a₂ ≳ 1.4 × 10⁶ | Rigorous arithmetic; threshold Sketch | step-0 note §1.3 |
| Linearized instability of the cap's de Sitter branch: (λ + 4)(ελ² + 3ελ − 1) = 0, ε = H₀²/M², one growing mode for one sign of the □R coefficient | Rigorous (flat-slice trace-equation linearization, sympy) | step-0 note §2.2 |
| N_inf ≈ 3(H₀²/M²) ln(M_P/H₀): the root's depth is a function of the free □R coefficient | Sketch | step-0 note §2.3 |
| For the unstable sign ε > 0 and ε > ε_c ∈ (0.35, 0.36), a second reflection-symmetric regular Euclidean cap exists (the symmetric double bubble); for ε ≤ 0.35 and for ε < 0 the sphere is the only real junction | Rigorous (numerical), minisuperspace | J-1 note §2 |
| The double bubble's Euclidean action lies below the sphere's by a finite gap at birth (ΔI ≈ −2.7a) growing as ≈ −4εa; its real continuation recollapses within a Hubble time; the minisuperspace action normalization is exact (Euler–Lagrange ≡ trace equation) and the sphere's analytic action −a(5 + 4ε) is reproduced numerically | Rigorous (numerical); normalization Rigorous | J-1 note §3 |
| Under no-boundary Euclidean weighting the sphere is the unique dominant real root iff 0 < ε < ε_c ≈ 0.355 (M > 1.68 H₀), which caps the root's depth at N_inf ≈ 5–7 e-folds | Sketch (Euclidean weighting assumed; routed to J-6) | J-1 note §4 |
| The junction constrains any *other* coupling, or selects a value rather than a window | Conjecture — open | — |

## Relationship to other programs

- **`signature-change-boundary`** — upstream (`informs`): fixed-background crossing and junction regularity; this program supplies back the smooth-class equivalence of its bounded-expansion-rate condition with K_Σ = 0 (#215 step 2b).
- **`fixed-point-existence`** — upstream (`informs`): the anomaly fixed point; this program supplies back the coefficient-convention reconciliation (#168) and the "large-N, not realistic" correction to `fpe-fixed-point-is-inflationary`.
- **`co-emergence`** — downstream (`informs`): Open Problem 1 (mass), `conj:mass_generation`, and the toy-model side results (#215 step 2a).
- **`gaussian-gravitational-decoherence`** — no relation established.

## Build

Prose only (`notes/`). Port to `index.tex` once J-1 lands; see `AGENTS.md` for the convention.
