# Signature Change at a Degenerate Boundary

**Status:** Early note / musings

## In plain English

Spacetime has a built-in difference between time and space (its "signature").
Some approaches to quantum cosmology imagine regions where that distinction
switches off — geometry with no time direction at all — which raises the
question: is the border between a timeless region and a normal one a tear, a
wall, or something traversable? This program studies the simplest such border
on a fixed, hand-prescribed background and finds it surprisingly tame:
geometry, particle paths, and waves all either cross it or terminate on it in
a finite, controlled way, with a precise asymmetry — paths through time end
at the boundary, paths through space cross unharmed. (One step in that
picture is only sketched, not proven: a spatial path crosses the border as a
*route*, but whether a freely-falling path continues through it still obeying
the free-fall rule is deferred to the literature rather than derived here.) A follow-up note adds a
prescribed *expanding* universe on the time side and finds the particle-path
and wave behaviour just as tame — but the geometry itself now stays smooth at
the border only if the expansion slows to a halt right at it; otherwise the
border becomes a genuine curvature spike. These are early notes,
not a paper; the core calculations are rigorous for the fixed background,
while a few steps — the crossing rule above, the interpretive "crossing
structure" section, and a claimed single unifying mechanism — are sketches,
and nothing here claims such borders actually occur in
nature — only that they are not mathematically catastrophic.

A fixed background whose metric changes signature across a degenerate hypersurface $\Sigma$ supports a Lorentzian region adjacent to a Euclidean one, and the crossing of $\Sigma$ by worldlines and fields is benign rather than singular. This program asks a narrow, foundational question: **can a fixed Euclidean background produce a Lorentzian region, and can worldlines cross the boundary between them?**

## Scope

This is deliberately a **fixed-background, test-field** investigation.

- The signature-changing metric $\lambda(x^0)$ is **prescribed**, not derived. There is no dynamics for $\lambda$ and no backreaction.
- The content is a *consistency* result: the bulk geometry, the geodesic structure, and a free scalar field are mutually compatible and non-singular across $\Sigma$, and the surface is traversed with a definite, causal-type-dependent asymmetry.
- **Self-consistency is explicitly out of scope here.** It is meant to be layered on top of this result later, not built into it. A future agent should not merge this into the co-emergence program or attach the SCE fixed-point machinery to it — the point of keeping it separate is that the kinematic/field-theoretic crossing picture stands on its own and is *upstream* of any self-consistency argument.

"Consistent" throughout means *free of the divergences a degenerate metric naively produces* and *mutually compatible across the geometric, kinematic, and field-theoretic descriptions*. It does **not** mean physically realized or dynamically selected.

## Current contents

- `notes/2026-06-05-fixed-background-note.md` — the seed note. Establishes, on the background $ds^2 = \lambda(x^0)(dx^0)^2 + d\vec x^2$ with $\lambda$ passing through zero:
  - the bulk is flat on each side; $\Sigma$ is a coordinate-degenerate boundary, not a curvature singularity;
  - timelike geodesics reach $\Sigma$ at finite proper time but have no timelike continuation; spacelike *curves* cross with character intact (the crossing asymmetry); continuation *as a geodesic* through $\Sigma$ is Sketch (every crossing geodesic arrives with degenerating coordinate velocity; extendability is Kossowski–Kriele [7] territory, not derived in the note — reset in the July 2026 red-team audit);
  - a free scalar's temporal equation has a regular singular point at $\Sigma$, Bessel-reducible with $\nu = \tfrac12$, so all modes are bounded and the canonical momentum has finite one-sided limits — making the Dray–Manogue–Tucker no-surface-layer junction condition imposable and uniquely solvable (not "automatic", and disputed in the literature by Hayward's stronger vanishing-momentum condition);
  - the stress-energy scalar invariants are bounded;
  - all of the above are, at **(Sketch)** unification level, faces of one mechanism: every $g^{00}=1/\lambda$ is escorted by $\sqrt{|g|}=\sqrt{|\lambda|}$ (§8; each individual bullet is Rigorous given §§3–6);
  - the analysis is two-sided: the profile $\lambda \simeq -c\,\mathrm{sgn}(x^0)\,|x^0|^n$ gives a genuine signature change for every $n>0$, and each of §§3–6 is established from both the Lorentzian ($x^0>0$) and the Euclidean ($x^0<0$) sides.

- `notes/2026-06-17-expanding-region-note.md` — extends §§3–6 of the seed note to a prescribed flat-slice **expanding** background $ds^2 = \lambda(x^0)(dx^0)^2 + a^2(x^0)\,d\vec x^2$, $a>0$ smooth (SCB-6, #63). Findings (Rigorous given the fixed background, except spacelike geodesic continuation which is Sketch; $a\equiv$const recovers the seed note exactly):
  - **Test-field crossing structure is unconditionally robust** (needs only $a(0)>0$): the geodesic asymmetry survives — spacelike *curves* cross intact (spacelike geodesic continuation is Sketch — reset in the July 2026 red-team audit, matching the seed note; see #146) — with Hubble redshift of peculiar momentum; the scalar's temporal equation stays Fuchsian with the same indicial roots $\{0,1+\tfrac n2\}$ and $k^2\to k^2/a(0)^2$; the canonical momentum stays finite (no surface layer); the stress-energy invariants stay $O(1)$.
  - **Bulk geometry is only conditionally benign:** the expanding bulk is FLRW-curved (not flat), and $\Sigma$ becomes a genuine curvature singularity unless the *proper* expansion rate $\mathcal H = a'/(a\sqrt{|\lambda|})$ stays bounded at $\Sigma$ — sharp leading condition $a' = O(|x^0|^{n/2})$, completed by $a$ being $C^2$ in proper time. The flat-slice case satisfied this identically ($\mathcal H\equiv0$) and so could not see it.
  - The exact $\nu=\tfrac12$ Bessel reducibility is demoted to a **local** statement near $\Sigma$; the global elementary closed form is special to constant $a$.

## Open points (from review)

- **Degeneracy order vs. sign change** — *addressed* (#65). The note now states the profile as $\lambda \simeq -c\,\mathrm{sgn}(x^0)\,|x^0|^n$ (a genuine two-sided signature change for every $n>0$, with the parity defect of the earlier $-c(x^0)^n$ form recorded in §1) and carries the Euclidean-side parallel analysis through §§3–6.
- **No-log strengthening** — *addressed* (#120 / #128). Because $\nu=\tfrac12$ is non-integer for every $n$, there is no logarithmic solution even when the indicial roots $\{0,\,1+\tfrac n2\}$ differ by an integer (even $n$); this is now stated explicitly in §5.
- **Rigor labels** — *addressed* (#120 / #128), then **partially reset** (July 2026 red-team audit). Current state: §3 Rigorous given the fixed background; §4 Rigorous *except* continuation-as-a-geodesic through $\Sigma$, which is Sketch; §5 Rigorous for the mode analysis (with the junction *matching* stated as an imposable two-sided condition, not an automatic one); §6 Rigorous; §7 Sketch; §8 Sketch as a unification claim (its individual bullets Rigorous given §§3–6); §9 none (limitations, not results).
- **Citations** — *addressed* (#135), then **corrected** (July 2026 red-team audit). All seven references [1]–[7] exist with correct bibliographic data, but the SCB-4 content-match for [3] was wrong: the note had attributed the *continuity-of-momentum* no-surface-layer condition jointly to Hayward 1992 and Dray–Manogue–Tucker 1993, whereas Hayward's paper requires the field to be *instantaneously stationary* at the junction ($\pi|_\Sigma = 0$), opposing the Dray–Manogue–Tucker condition (the explicit rebuttal appears in his gr-qc/9303034, 1993). The corrected attribution: Dray–Manogue–Tucker [4] (continuity, the position this note's generic solution realizes), Hayward [3] (stronger vanishing-momentum condition, the opposing side of the dispute), Hellaby–Dray [5] (conservation-law caveat), Kossowski–Kriele 1993/1994 (degenerate-metric geodesics). Cleared for a `thebibliography` on the SCB-5 port *with the corrected attributions*.

## Relationship to other programs

- **`co-emergence`** — *Downstream.* Co-emergence argues signature is selected by cross-level self-consistency; its B1 result shows a single level does not distinguish signatures. This program is the complementary fixed-background statement: a prescribed signature-changing background is kinematically and field-theoretically benign. The self-consistency layer would sit on top of this result (`informs`), but is intentionally not developed here.

## Build

Currently prose only (`notes/`). Port to `index.tex` once the content settles; see `AGENTS.md` for the build convention.
