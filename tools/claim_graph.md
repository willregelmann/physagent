# The claim graph

The repository's research state is a graph of **claims**. Each claim is a
Markdown file with YAML-subset frontmatter under `programs/<name>/claims/`.
The paper stays prose; the graph is authoritative about tier, dependency, and
verification state.

```
python tools/claim_graph.py lint [--warn] [--json]
python tools/claim_graph.py show <id>          # claim + what a demotion would break
python tools/claim_graph.py query --tier rigorous --since 2026-06-09
python tools/claim_graph.py coverage <id>      # mechanical coverage of the closure
python tools/claim_graph.py stats
```

Stdlib only, matching `tools/verify_citations.py` — CI needs no dependency
install.

## Why this exists

Every defect that reached `main` in this project and was caught by the
2026-07-24 independent audit was **relational**, not arithmetic. Not one was a
sign error or a botched integral. They were: a Rigorous claim leaning on a
Sketch one; a contraction proved for a different map on a different space; a
proof step valid only for real vectors asserted for complex ones; citations
never re-examined after the day they landed; a result carried as original that
was published in 2021.

Relational defects are graph conditions. Graph conditions are mechanically
checkable. That is the entire thesis.

**What this cannot do:** make a claim true. It makes *inconsistencies between
claims* visible and cheap to find. A wrong derivation with correct dependencies
passes every lint here. That is what adversarial review is for.

## Lints, and the defect each one comes from

| Lint | Catches | Origin |
|---|---|---|
| **L1** | load-bearing edge to a lower tier | `prop:riem_classical` asserted Rigorous uniqueness on a permanently-Sketch contraction (CE-13) |
| **L2** | cross-object transfer, undeclared or unjustified | the same edge — the companion contraction is about a field-theoretic map on manifolds, not `F` on `C^N` |
| **L3** | dependency needs a hypothesis the dependent never states | *(warn)* generalisation of the same family |
| **L4** | internal step assuming hypotheses narrower than its claim | `prop:interference_metric` asserted `x†(ρ+ρᵀ)x = 2Re(x†ρx)`, true only for real `x`; `prop:nohilbert` argued two constructions and concluded "any" |
| **L5** | tier ≥ conjecture with novelty unchecked | CE-1's interference metric is the relative entropy of imaginarity (Xue et al. 2021), carried as original |
| **L6** | load-bearing citation verified by abstract, expired, or unrecorded | `geroch` and `thm:exotic` misattributions sat green on `main` from March to July — nothing re-examines a citation already merged |
| **L7** | live claim resting on a dead/withdrawn/superseded one | demotion propagation: CE-13 was this sweep, done by hand weeks late |
| **L8** | dependency cycle | `prop:nohilbert` was checked for circularity by hand during the audit |
| **L9** | formal node with `sorry` or non-standard axioms | — |
| **L10** | formal node with no/failing/stale build record | `programs/co-emergence/lean/` is pinned and asserted sorry-free in a LaTeX remark; no CI job has ever re-run it |
| **L11** | formal node discharging an informal claim with an unreviewed bridge | Lean proves a formal statement, the paper an informal one; the correspondence is where errors hide and Lean cannot check it |
| **L12** | toolchain pin drift | *(warn)* |
| **L13** | claim at sketch+ absent from the paper, or a stale `\label` | keeps the prose and the graph from diverging on tier |

`tools/tests/test_claim_graph.py` encodes each of these as a regression fixture
built from the real historical defect. **If the suite stops catching them, the
schema is wrong.** That is the acceptance criterion for the whole design.

## Two lifecycles

**Generative:** `speculation → conjecture`, gated on the conjecture criteria —
falsifiable, novel, consequential, consistent, reachable. Enforced by the
schema: `falsifier`, `consequence` and `novelty` become required at
`conjecture`.

**Verification:** `conjecture → sketch → rigorous`, gated on proof.

A claim resting at `conjecture` forever is a **success**, not a failure. The
demotion machinery does not touch that tier — demoting a conjecture for being
unproven is a category error.

## Node schema

Required always: `id` (immutable, must match filename), `program`, `tier`,
`status`, `statement`. Required at `conjecture` and above: `falsifier`,
`consequence`, `novelty`.

The three fields doing most of the work, none of which existed before:

- **`object`** — `name`, `definition`, `space`. Two claims about different
  objects cannot silently support each other (L2).
- **`hypotheses`** — enumerated, so a dependency requiring something its
  dependent never states is visible (L3).
- **`internal_steps`** — steps invoking *narrower* hypotheses than the claim,
  each needing a written `justification` to be used at full generality (L4).

Formal (Lean) nodes carry `kind: formal`, a `formal:` block (`decl`,
`toolchain`, `mathlib`, `axioms`, `sorry_free`, `last_built`), a `bridge:` to
the informal claim, and `discharges:`.

## Mechanical coverage

```
coverage(C) = |{load-bearing nodes in C's closure discharged by a valid formal node}|
              ---------------------------------------------------------------------
                                  |closure(C) ∪ {C}|
```

Deliberately **not** "does this claim have a Lean file" — that is satisfied by a
formalization which assumes everything interesting. Assumed hypotheses are
edges, and edges are counted.

The worked example is the entropy-excess pair. Part (a) is formalized in full.
Part (b) is machine-checked only at its scalar step, with three structural links
supplied as hypotheses and not re-derived in Lean. Both are legitimately
Rigorous; they are 100% and 0% mechanically covered, and the graph says so
without anyone having to write a careful paragraph and hope readers notice.

Today both read 0%, because no CI job runs `lake build` and a formal node with
no build record discharges nothing.

## Migration state

Extracted 2026-07-24 from the audited results plus their dependencies:
**20 claims** — 17 rigorous, 3 sketch, 0 conjecture, 0 speculation, 2 formal.

The tier distribution is the diagnosis restated: this corpus has no generative
tier at all.

### The novelty boundary is temporary and is meant to be deleted

`NOVELTY_ENFORCED_FROM = 2026-07-24`. No claim predating the graph had ever
been prior-art checked, so enforcing L5 retroactively would fail 19 of 20 nodes
at once and teach everyone to ignore the linter. Claims born on or after that
date must carry a novelty check; older ones warn.

**Standing instruction from the experimenter (2026-07-24): remove this constant
and run the novelty check over the grandfathered claims.** The end state is no
boundary — L5 errors on every claim at conjecture or above, unconditionally.

The path there is enumerated, not aspirational:

```bash
python tools/claim_graph.py stats | jq -r '.novelty_backlog[]'
```

Each entry needs a prior-art search at source, and its `novelty:` block filled
in with `status`, `searched`, and `found`. When `novelty_backlog_remaining`
reaches 0, delete `NOVELTY_ENFORCED_FROM` and the grandfathering branch in
`lint_L5_novelty`, and the gate becomes unconditional.

This is not housekeeping. CE-1's interference metric was the relative entropy of
imaginarity (Xue et al. 2021), carried as an original contribution and caught
only because an independent audit happened to look. Every unswept node is
another chance at exactly that. The backlog exists to be burned down, not to
make the boundary comfortable.

**Not yet extracted:** 43 labelled sites exist across the papers; 20 are
represented. The remainder are largely Sketch-tier sub-results not touched by
the audit.

## Not yet wired

`.github/workflows/` is outside what agents or this session author — it needs
the experimenter's admin-merge path. Two jobs are wanted:

1. **`claim-graph`** — `python tools/claim_graph.py lint`, on any PR touching
   `programs/*/claims/**` or `programs/*/index.tex`.
2. **`lean`** — `lake exe cache get && lake build`, plus a `#print axioms`
   assertion, writing the result back to each formal node's `last_built`.
   Without cache retrieval a Mathlib build will dominate CI runtime.

Until (2) exists, L10 fires on every formal node and mechanical coverage reads
zero. That is the correct state of the record.
