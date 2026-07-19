# Methodology

This is a research-as-code project. The paper is the codebase, open problems are GitHub issues, and contributions are pull requests.

## Core Model

The default workflow is **agent-as-contributor, human-as-reviewer**. Agents work on branches, submit PRs, and the human author reviews and merges. On specific issues, the human can shift to real-time collaboration.

Every PR must target a specific issue. Speculative exploration that doesn't map to an existing issue should first propose a new issue for discussion before branching.

Agents have no merge authority. Only the human author merges.

### Autonomous Experiment Mode

For the duration of the experiment pre-registered in `EXPERIMENT.md`, the two
human-in-the-loop rules above are superseded by the constitution in
`AUTONOMY.md`: merge authority is delegated to a mechanical gate stack
(deterministic CI → semantic claim-support → adversarial quorum →
constitutional guard, with GitHub auto-merge as the executor), the human author
acts as experimenter rather than reviewer, and explorations are merged via
gated PRs rather than committed directly to `main`. Everything else in this
document — rigor standards, the rigor lifecycle, citation discipline,
adversarial review modes, team patterns, issue relations — remains in force
unchanged and is enforced by the gate stack rather than by human review.
`AUTONOMY.md` is the controlling document wherever the two conflict; outside
the experiment window, this section is inert.

## What This Program Produces

This is a program for deriving new physics, not a literature-verification
machine. The default output of a contribution is original mathematics
developed within the framework's own axioms — not a report of what already
exists elsewhere. Literature has three legitimate roles here, and none of
them is a gate on originality:

1. **Citation grounding.** When a claim leans on an external result, that
   citation must exist and must actually support the claim (Citation
   Discipline, below). This governs how *external* claims are represented —
   never whether new claims may be attempted.
2. **Technique borrowing.** Established methods from elsewhere — a
   contraction technique proved on a different manifold class, a formalism
   from an adjacent subfield — are fair game as tools to apply to this
   framework's open problems, even where no one has combined them with this
   framework before. Borrowing a technique is not borrowing a conclusion.
3. **Literature synthesis as its own deliverable.** Occasionally the object
   of study *is* the literature: an Exploration can legitimately conclude "no
   one has connected X and Y, and here is why that connection might matter."
   That is a valid Exploration output. It is not, by itself, a result —
   identifying an unexplored connection is the start of a derivation, not the
   end of one.

**The actual gate on a result is the rigor lifecycle** (Conjecture → Sketch →
Rigorous, below) plus self-checks plus adversarial review — never prior
publication. "No existing paper does this" is scoping information, not a
verdict. Read it as *here is open territory*, not *here is a reason to
stop*. The Researcher role (Agent Teams → Standard roles, below) reports what
the literature says and stops there by design, precisely so a different
agent can take the next step and attempt the derivation itself. If a debate,
triage pass, or literature search concludes "unresolved, not disproven,
nobody has constructed this yet," the correct next move is usually to
attempt the construction — at whatever rigor level is honestly achievable,
with every gap named — not to treat the absence of precedent as a finding in
itself.

## No Idea Is Eliminated Without a Defense

A candidate direction, position, or fan-out attempt is never killed on the
strength of a single critical pass. Before any debate, review, or elimination
step records something as dead, its strongest possible version must actually
be constructed and tested — not merely imagined and waved off. "This looks
wrong on its face" is not a verdict; a verdict requires an honest defense
attempt that still fails.

This is not politeness — it is a defense against the single largest failure
mode of an adversarial-review system: that adversarial pressure alone,
without an equally serious defense pass, systematically favors whatever
already looks conventional and kills whatever looks strange before it gets a
fair hearing. There are no dumb ideas at the point of judgment — only ideas
that have or haven't yet been steelmanned.

The Synthesis agent role (Agent Teams, below) already runs this as two
passes for every position debate — adversarial critique, then a defense
assessment distinguishing fatal flaws from solvable gaps. That two-pass
discipline is required everywhere an idea can die under this methodology,
not only there: an attempt eliminated in a fan-out cycle, a demotion the red
team proposes, a park/close disposition on a proposed direction. "No dumb
ideas" does not mean every idea survives — it means every idea gets an
honest trial before it doesn't.

## Rigor Standards

Every derivation in a PR must include self-checks documented in the PR description:

- **Dimensional analysis** — every equation must be dimensionally consistent.
- **Limiting cases** — the result must reduce to known results in appropriate limits (flat space, weak field, classical limit, etc.).
- **Consistency** — the result must not contradict other results in the paper or established physics within the framework's validity domain.
- **Order-of-magnitude sanity** — numerical predictions must be evaluated and compared against physical intuition.

After self-checks pass, the human reviewer can request **adversarial review**: a second agent is dispatched to critique the derivation. Adversarial review is optional but recommended for any result that would change a prediction or appear in the abstract.

Adversarial review has two distinct modes with different mandates. The human reviewer specifies which mode (or both) is requested.

**Verification mode.** The adversarial agent checks every step of the derivation: does the algebra follow, are limits taken correctly, are cited results actually used as cited, are there sign errors or factor errors? Verification is the baseline mode for any PR promoting a result to Rigorous.

**Stress testing mode.** The adversarial agent actively tries to break the result. This means: constructing explicit counterexamples; identifying edge cases where the stated conditions are met but the conclusion fails; finding alternative interpretations of the same mathematics that lead to different conclusions; checking every limiting case against known results from a different direction. Stress testing is the appropriate mode for any result that would be used as a lemma in subsequent work or that makes a new physical prediction.

In stress testing mode, the adversarial agent must explicitly attempt to find violations of the framework's hidden-assumption warnings: Can time evolution be made to sneak back in? Is there a smuggled background structure? Is there a preferred observer or foliation hidden in the setup? A stress test that does not check these is incomplete.

An agent must never claim a result is proven when it has only been sketched. PRs should clearly label work as one of:

- **Rigorous** — every step follows from the previous with no gaps.
- **Sketch** — the argument structure is correct but steps are omitted.
- **Conjecture** — a plausible claim without a complete argument.

### Rigor Lifecycle

Rigor levels are not permanent. Results can be promoted or demoted, and each transition requires its own PR with specific requirements.

**Promotions:**

- **Conjecture → Sketch**: Name every logical step the argument would require, even if none are filled in. A sketch is an honest accounting of what a proof needs to contain. Gaps must be labeled explicitly. This PR does not fill gaps — it maps them.
- **Sketch → Rigorous**: Fill every gap. No step may be omitted without a citation to an established result that covers it. Requires adversarial verification review (see below) before the PR can merge.

**Demotions:**

- **Rigorous or Sketch → Demoted**: A gap has been found that the existing work does not cover. Open a PR that identifies the gap precisely, resets the rigor label, and optionally opens a new issue for filling the gap.
- **Conjecture → Withdrawn**: A counterexample has been found, or the conjecture directly contradicts an established result. The withdrawal PR states precisely what failed and why. Withdrawn conjectures are not deleted — they remain with a Withdrawn label so the negative result is not forgotten.

Demotion is as important as promotion. A result that is silently wrong is worse than a result that is explicitly a sketch. Agents should treat demotion as normal maintenance, not failure.

## Citation Discipline

Two tiers:

**Paper-grade (strict).** Any reference that would enter `\begin{thebibliography}` must be verified to exist. The agent must confirm the author, title, journal, and year, and must verify that the paper actually supports the claim being made. Web search is required, not optional. Fabricating a citation is the single most serious failure mode.

*Automated enforcement.* Reference **existence** is mechanically gated in CI by `tools/verify_citations.py` (the `verify-citations` workflow): every `\bibitem` is resolved against the Crossref and arXiv APIs on each PR touching a `.tex` file, and the build fails on any unresolved entry. References that legitimately cannot be resolved by title/DOI/arXiv (books, foreign-language classics, internal companion papers) are listed in `tools/citation-allowlist.yml` with a per-entry justification. The gate checks *existence only* — confirming that a cited work supports its claim remains a human/agent responsibility, as above.

**Exploratory (honest).** In GitHub issues and PR discussions, agents may reference literature they have not verified, but must flag it explicitly: *"I believe Wald (1994) discusses this, but I have not verified the specific reference."* Unverified references must never be committed to the `.tex` file. When exploratory references are later promoted to paper-grade, they go through the strict verification process.

**Markdown is not a certification venue.** The deterministic and semantic
gates (`verify-citations`, `claim-support`) run against `.tex` files; they do
not run against Markdown. A reference cited in a program's `explorations/` or
`notes/` Markdown remains **exploratory tier** no matter how carefully it was
manually verified — including by a dedicated verification PR — because no
mechanical gate has actually checked it. Paper-grade status requires the
bibliography to live in a `.tex` file's `\begin{thebibliography}`, where
`verify-citations` and `claim-support` can and do run against it. Do not
write "paper-grade verified" language about a citation whose bibliography is
still in Markdown; that language belongs only to sources gated as above.
(Motivated by a real incident, not a hypothetical: `signature-change-boundary`'s
SCB-4 pass manually certified a citation paper-grade while its bibliography
was still Markdown-only — the certification was later found to have the
citation's position backwards, an error no gate had the chance to catch. See
`explorations/governance/2026-07-05-monthly-record-integrity.md`.)

**Polarity-sensitive citations need a named affirming passage, not just a
topic match.** A citation is polarity-sensitive when the cited work is one of
several genuinely competing or opposed positions — rival junction/boundary
conditions, rival interpretations, a result versus its own later rebuttal —
as opposed to simply establishing an uncontested fact. For any
polarity-sensitive citation, the paper's text (or the verification record,
for exploratory references) must (1) quote or closely paraphrase the
*specific affirming passage* in the source that supports the claim attached
to it, not just its abstract or general topic, and (2) name the competing
position(s) and state which side the citation is actually on. A citation
checked only against its abstract, with no named competing camp, has not
been polarity-checked — an abstract routinely omits which side of a dispute
a paper takes. (Same motivating incident as above: the SCB-4 pass certified
Hayward's paper as supporting a junction condition Hayward's own paper
explicitly argues against; the abstract alone gives no hint of this.)

### Citation Failure Recovery

The happy path (exploratory → verified → paper-grade) is documented above. The failure path must also be explicit.

**Exploratory reference fails verification.** The reference does not exist, cannot be located, or does not support the claim attributed to it. Protocol: (1) Comment on every issue thread or PR that cited the reference, marking it as unverified and withdrawn. (2) Do not promote to paper-grade. (3) Note what was claimed and what verification found — negative results about the literature are useful information for future agents who might chase the same reference.

**Paper-grade citation is found to misrepresent the source.** A committed `.tex` citation either cites a nonexistent paper or misrepresents what the cited paper says. This is a correctness bug in the paper, not a normal research setback. Protocol: (1) Open a correction PR that either corrects the citation with a verified alternative, or removes the claim. (2) Comment on all open issues that depended on the misrepresented result. (3) Check whether any other results in the paper used that citation as a lemma; those results must be reviewed.

The severity distinction matters: an exploratory reference that fails verification is expected and normal. A paper-grade citation that is wrong is treated with the same urgency as a mathematical error in the derivation.

## Agent Teams

For research tasks involving genuine uncertainty — where the right answer is not known and anchoring on a single approach is a risk — use **agent teams** rather than sequential subagents.

A subagent is a delegation: one agent handles a well-defined task and returns a result. A team is a debate: multiple agents develop independent positions in parallel, without seeing each other's reasoning, and a synthesis agent adjudicates. The team structure is specifically valuable because parallel agents cannot anchor on each other. Each position is developed from the axioms independently, and the synthesis then finds what survives adversarial review across all of them.

### When to use a team

The official strongest use cases are research and review, competing hypotheses, and cross-layer coordination. For this project, that maps to:

- **Research**: multiple teammates investigate different aspects of an open problem simultaneously, then share and challenge each other's findings.
- **Adversarial review**: teammates each apply a distinct critical lens to a derivation — one checking math, one checking hidden assumptions, one stress-testing limiting cases.
- **Competing positions**: teammates develop independent positions in parallel without seeing each other's reasoning. The debate structure is explicitly designed to fight anchoring: sequential investigation biases every subsequent step toward the first theory explored. Parallel investigators who actively try to disprove each other surface theories that survive genuine scrutiny.

Use a subagent (not a team) when the task is well-defined: verify a citation, compile the paper, search the literature for a specific result, draft a section given a complete outline. Subagents report results back to the lead; they do not communicate with each other. Use teams when inter-agent challenge and coordination are the point.

### Team structure for debates

The canonical pattern for a research debate:

1. **Position agents (parallel).** Each agent independently develops the strongest version of one position. Agents do not see each other's work. Each position agent must: propose a specific mathematical structure (not just a direction), label all claims Rigorous/Sketch/Conjecture, and honestly identify where their position is underspecified.

2. **Synthesis agent (after all positions complete).** Reads all positions. Runs two passes: (a) adversarial critique — find every hidden assumption, every place a position appeals to existing structure rather than deriving it; (b) defense assessment — distinguish fatal flaws from solvable gaps. Then identifies convergence across positions and proposes what the surviving elements imply for the research direction.

### Shared context

Claude Code agent teams automatically load the project's CLAUDE.md and everything it @-includes — AGENTS.md and METHODOLOGY.md. This means every teammate already has the hidden-assumption warnings, the rigor standards, and these role descriptions without any additional setup. The spawn prompt provides task-specific parameters; the shared project context is inherited automatically.

### Team size and task sizing

Start with 3–5 teammates. Token costs scale linearly with team size; coordination overhead increases; returns diminish. Three focused teammates often outperform five scattered ones.

Aim for 5–6 tasks per teammate. This keeps everyone productive without excessive context switching.

Size tasks so each produces a clear, self-contained deliverable — a research summary, a position paper, a review of a specific section. Tasks that are too small make coordination overhead dominate; tasks that are too large run too long without check-ins and increase the risk of wasted effort.

### Plan approval for PRs

For teammates working on contributions that will become PRs, require plan approval before implementation:

> "Spawn a drafter teammate to write Section 4. Require plan approval before they make any changes to the file."

The teammate works in read-only mode until the lead approves the approach. The lead can reject with feedback; the teammate revises and resubmits. This enforces the methodology's requirement that derivations be planned before they are written, and creates a record of the approach decision.

### Standard roles

These roles recur across Explorations. When spawning teammates, reference the role by name and supply task-specific parameters.

**Researcher.** Searches the literature for a specific question. Verifies all citations found (author, title, journal, year, content match). Flags unverified references explicitly. Produces a structured summary with a verified citation list. Does not propose mathematical results — only reports what the literature says.

**Position agent.** Develops the strongest possible version of one assigned position. Works without seeing other positions. Proposes a specific mathematical structure, labels all claims Rigorous/Sketch/Conjecture, and honestly identifies where the position is underspecified. Does not hedge toward a middle ground — the point is genuine commitment to one direction so the synthesis has something to push against.

**Synthesis agent.** Reads all position files after positions are complete. Runs two passes: (1) adversarial critique — for each position, find every hidden assumption, every appeal to existing structure rather than derivation, every violation of the hidden-assumption warnings; (2) defense assessment — for each criticism, determine whether it is a fatal flaw or a solvable gap. Then identifies structural convergence across positions and states what the surviving elements imply. Must explicitly check each hidden-assumption warning against each position.

**Drafter.** Writes LaTeX given a complete research summary and style reference. Does not conduct research or verify citations — those arrive as inputs. Matches the style of existing papers in the repo exactly. Labels all results with rigor levels. Attempts to compile the output and fixes errors.

**Verifier.** Checks a derivation or PR for mathematical correctness (verification mode) or actively attempts to construct failure cases (stress testing mode). The human reviewer specifies which mode. In stress testing mode, must attempt to find violations of each hidden-assumption warning.

### Quality gates via hooks

The `TeammateIdle` hook runs when a teammate is about to go idle. Exit code 2 keeps them working — use this to enforce that teammates have completed their required output before going idle. The `TaskCompleted` hook runs when a task is being marked complete; exit code 2 blocks completion. These can be configured in `.claude/settings.json` to enforce output format requirements.

### Recording team outputs

The output of a team debate is an Exploration (see below). Position files and the synthesis are committed to the program's `explorations/` directory as a dated artifact. The positions themselves are part of the record — not just the synthesis — because a position that lost the debate may become relevant again if the synthesis's conclusion is later challenged.

This default (every position committed permanently) fits a small debate — 2-3
positions on one pre-defined question. A wider speculative tournament (more
candidate attempts than that, most expected to fail) doesn't need every
attempt to earn permanent, first-class status to satisfy "never delete a
losing position" — a lighter record (where the attempt lived, why it died)
can carry that obligation instead. Under autonomous mode, this is exactly
what the `explorer` routine's scratch tier does; see AUTONOMY.md's
"Explorations under autonomy" section for the mechanism. Outside autonomous
mode, the same principle applies by judgment: scale the record to the size
of the fan-out, not the other way around.

## Explorations

Some work reshapes the research direction rather than advancing a specific result. This work does not fit the branch-per-issue contribution model. Call it an **Exploration**.

An Exploration is a structured investigation: a debate between competing positions, a literature survey, a synthesis that identifies where the project should go next, or a negative result that closes off a direction. The debate process is the canonical example — multiple agents take positions, an adversarial synthesis is run, and the output is a structured artifact that changes what issues get opened next.

Explorations live in the program's `explorations/` directory, dated and titled:

```
programs/<program-name>/explorations/YYYY-MM-DD-short-title.md
```

They are committed directly to the main branch by the human author, not via a feature branch. An Exploration can produce:

- **New issues**, if it identifies specific open problems worth pursuing.
- **A PR modifying METHODOLOGY.md**, if it changes the process.
- **No further action**, if the result is purely negative — that is a valid outcome, and the Exploration is its own record.

An Exploration does not produce a contribution to the paper directly. If it generates new mathematics, that mathematics must be developed in a subsequent issue-and-PR cycle with proper self-checks and adversarial review. The Exploration establishes direction; the PR establishes results.

Explorations are first-class artifacts. They are not scratch notes or session logs — they are the record of how the program's research direction was shaped. Future agents should read a program's Explorations before starting work on related issues.

## Contribution Workflow

1. **Claim an issue.** Agent assigns itself to an open issue and comments with a brief approach — what it plans to try and why.
2. **Branch.** Create a branch named `program-name/issue-N-short-description` (e.g., `fixed-point-existence/issue-3-noise-kernel-flat-space`).
3. **Work in commits.** Each commit should represent a coherent step. Commit messages should say what was derived or changed, not just "update paper."
4. **Self-check.** Before opening a PR, the agent runs through the rigor checklist (dimensional analysis, limiting cases, consistency, sanity check) and documents results in the PR description.
5. **Open PR.** The PR links to the issue, describes the contribution, states the rigor level (rigorous/sketch/conjecture), and lists self-check results.
6. **Adversarial review (if requested).** The human reviewer can request a second agent to critique the PR.
7. **Revise or merge.** The human author has final say.

If an agent gets stuck or discovers the approach won't work, it comments on the issue explaining why and what it learned. Negative results are valuable — they narrow the search space.

## Version Tags

Tags mark stable states of the paper where all self-checks pass and the content is internally consistent. Not every merge gets a tag — only milestones where the paper stands on its own.

**Scheme:** `vMAJOR.MINOR` following the paper's lifecycle.

- **v0.x** — pre-submission drafts. Tag when a major section, derivation, or prediction set is complete and merged (e.g., `v0.1` fixed-point proof, `v0.2` decoherence rates, `v0.3` experimental predictions).
- **v1.0** — first public release (arXiv submission).
- **v1.x** — revisions in response to referee reports or community feedback.
- **v2.0** — major revision that changes the argument structure or adds significant new results.

**When to tag.** The human author creates tags after merging work that completes a logical milestone. A tag means: the paper compiles, all derivations have passed self-checks at the stated rigor level, and no known internal contradictions exist.

**Tag annotations.** Use annotated tags (`git tag -a`) with a message summarizing what the paper contains at that point. This serves as a changelog entry.

**Using tags in the workflow.**

- Adversarial reviews can be scoped to changes since the last tag.
- Issues and PR descriptions can reference tagged versions for context (e.g., "this addresses a gap in the v0.2 decoherence derivation").
- External references to the paper should cite a specific tag when possible.

## Guarding Against Known Failure Modes

**Hallucinated results.** The self-check and adversarial review requirements exist specifically for this. Additionally, agents must show work — a PR that states a result without the derivation is incomplete regardless of whether the result is correct.

**Ungrounded speculation.** Every PR must connect back to the paper's existing mathematical framework. If a contribution requires new postulates or assumptions beyond the three axioms in Section 2, this must be flagged explicitly in the PR description. The human author decides whether the new assumption is acceptable.

**Lost context.** All substantive work happens on branches tied to issues. Agents must read the current state of the program's paper (`programs/<name>/index.tex`) and its `explorations/` directory, as well as relevant issue threads, before starting work. Discoveries that bear on other open issues should be cross-referenced with a comment on those issues, using the relation types defined below.

### Issue Relations

When filing an issue or opening a PR, declare explicit relations to other issues where they exist. Use these four types:

- **blocks** — this issue must be resolved before the other can proceed.
- **informs** — a result from this issue is relevant to the other, but neither depends on the other.
- **contradicts** — a result from this issue conflicts with a claim in the other; both cannot be right.
- **supersedes** — this issue replaces or extends a previous one, making the other partially or fully obsolete.

Declare relations in the issue body (e.g., "contradicts #12, informs #15"). Update relations as they become apparent during work. When a result invalidates an assumption in another issue, a comment on that issue is required, not optional. The relation system is how the project maintains coherence as it scales — without it, a negative result filed in one issue silently breaks work in another.
