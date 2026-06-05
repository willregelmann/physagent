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
at the boundary, paths through space cross unharmed. These are early notes,
not a paper; the core calculations are rigorous for the fixed background, one
section is a sketch, and nothing here claims such borders actually occur in
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
  - timelike geodesics reach $\Sigma$ at finite proper time but have no timelike continuation; spacelike geodesics cross with character intact (the crossing asymmetry);
  - a free scalar's temporal equation has a regular singular (Fuchsian) point at $\Sigma$, Bessel-reducible with $\nu = \tfrac12$, so all modes are bounded and the canonical momentum is finite (no surface layer);
  - the stress-energy scalar invariants are bounded;
  - all of the above are faces of one mechanism: every $g^{00}=1/\lambda$ is escorted by $\sqrt{|g|}=\sqrt{|\lambda|}$.

## Open points (from review, not yet addressed in the note)

- **Degeneracy order vs. sign change.** The one-sided "reaches $\Sigma$ / Fuchsian regularity" results hold for all $n>0$ in $\lambda \simeq -c\,(x^0)^n$. The *two-sided* picture (an actual Euclidean region, and continuation across $\Sigma$) requires $\lambda$ to change sign, which $-c(x^0)^n$ provides only for odd integer $n$; for even $n$ the metric is Lorentzian on both sides (a degenerate tangency, not a signature change). Restate the profile as an odd-type function, e.g. $\lambda \simeq -c\,\mathrm{sgn}(x^0)\,|x^0|^n$.
- **No-log strengthening.** Because $\nu=\tfrac12$ is non-integer for every $n$, there is no logarithmic solution even when the indicial roots $\{0,\,1+\tfrac n2\}$ differ by an integer (even $n$). Worth stating explicitly in §5.
- **Rigor labels.** The note does not use the project's Rigorous/Sketch/Conjecture labels. §§3–6 are Rigorous given the fixed background; §7's worldline-saddle / propagator-tail matching is a Sketch.
- **Citations.** The references in "Relation to existing work" (Ellis and collaborators; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) are real and on-topic but **exploratory until verified**, and must not enter a `thebibliography` without strict verification (author/title/journal/year + claim support).

## Relationship to other programs

- **`co-emergence`** — *Downstream.* Co-emergence argues signature is selected by cross-level self-consistency; its B1 result shows a single level does not distinguish signatures. This program is the complementary fixed-background statement: a prescribed signature-changing background is kinematically and field-theoretically benign. The self-consistency layer would sit on top of this result (`informs`), but is intentionally not developed here.

## Build

Currently prose only (`notes/`). Port to `index.tex` once the content settles; see `AGENTS.md` for the build convention.
