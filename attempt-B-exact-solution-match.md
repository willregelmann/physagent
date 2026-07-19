# Attempt B: Direct case-matching against FPE's exact solutions

**Question:** Does GGD's "stationary matter" noise-kernel approximation sit safely inside a regime where FPE's M3 obstruction doesn't apply, or would restoring genuine retardation reintroduce the same causal-kernel difficulty?

**Technique:** direct case-matching of GGD's background against FPE's stated exact/existing theorems.

## Findings (as originally submitted)

**Summary verdict:** GGD's background is genuinely the class FPE explicitly excludes (Minkowski/asymptotically flat), not a degenerate limit of any FLRW-based result FPE has proven — but this does not endanger GGD's prediction, because GGD's actual calculation never invokes the self-consistency/existence question FPE answers in the first place.

### 1. GGD's background is genuinely flat/asymptotically flat, not an FLRW limit

`index.tex` L194-197: Newtonian/weak-field limit, no scale factor/Hubble rate/cosmological fluid. Source is a localized rigid body, spatially inhomogeneous by construction — incompatible with the FLRW ansatz independent of H's value, not an H→0 limit. FPE's MPS technique reaches non-compact FLRW by exploiting homogeneity; GGD's setup removes homogeneity by definition.

### 2. FPE's machinery explicitly, repeatedly excludes this class

`index.tex` L85, L766-771: "does not cover Minkowski space or asymptotically flat backgrounds." The 2026-07-17 hyperboloidal exploration independently reconfirmed non-containment. Conclusion (Rigorous, by direct citation): GGD's background is not covered, and not reachable by any limit, of any existence result FPE currently has.

### 3. But GGD doesn't need that machinery

FPE's machinery answers whether the fully coupled, nonlinear semiclassical map has a fixed point, with M3 obstructing the uniform bound needed across a neighborhood of trial geometries. GGD's classical background is linear Poisson theory with self-gravity negligible (Gm/Rc²~10⁻³⁵); its noise kernel is a variance of a non-relativistic mass distribution, labeled (Rigorous), no Hadamard renormalization step; its stochastic fluctuation is a linear SPDE. No fixed point, no ball of metrics, no uniform bound needed anywhere. Both papers' companion-paper notes describe two different existence questions at genuinely different difficulty levels.

### 4. Retardation restoration

Would add ordinary flat-space, linear, classical retarded-potential corrections — not a uniform bound over trial geometries. M3's difficulty needs a Lorentzian, causal-past-supported Green operator of the *renormalized* effective action in a contraction-mapping proof; GGD's retardation never needs that. (Sketch — the general fluctuation-dissipation relationship between the noise and response kernels in Hu-Verdaguer's program is asserted from the framework's structure, not independently re-derived this session.)

### 5. Axiom check

GGD's lab-frame Newtonian limit looks like what Axioms 1-2 forbid at the fundamental level, but both GGD and FPE self-identify as Level-2 phenomenology, where a preferred foliation is treated as an accepted, disclosed cost (same cost FPE's own MPS-based repair pays openly). (Sketch — co-emergence doesn't explicitly rule on GGD's specific construction.)

### Honest gaps

Did not verify from a primary Hu-Verdaguer source that the noise kernel and the M3-relevant response kernel are formally the symmetric/antisymmetric halves of one bi-tensor. If GGD extended to relativistic/field-theoretic matter, the non-relativistic escape route would no longer apply.

---
*Status after attack + steelman: the CATEGORICAL claim ("structurally exempt, different kind of object") does NOT survive — the fluctuation-dissipation assertion in §4, checked directly, turned out to cut the other way (N and K ARE the symmetric/antisymmetric projections of one object); the axiom-check in §5 was found to invert the valence of its own cited sources; and GGD's own Assumption (iv) was shown to be an admitted, untruncated-in-principle self-consistency loop, contradicting "no fixed-point loop anywhere." A different, narrower claim survives: GGD is the leading-order (zeroth-iterate) term of the SAME self-consistency map FPE studies, Sketch-level safe by order-of-magnitude estimate, not by theorem. See `steelman-B.md` and the synthesis document.*
