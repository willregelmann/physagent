---
description: "Adversarial review of a physics paper PR"
arguments:
  - name: pr_number
    description: "PR number to review (optional — defaults to current branch's PR)"
    required: false
---

You are orchestrating a two-pass dialectical review of a pull request for one of the project's physics papers (under `programs/`). The first pass finds problems (adversarial critic). The second pass challenges those findings (steelman defender). The calibrated verdict table is the deliverable — not either pass alone.

## Step 1: Resolve the PR

$ARGUMENTS is the optional PR number argument.

- If `$ARGUMENTS` is a number, use that as the PR number.
- If `$ARGUMENTS` is empty, run `gh pr view --json number` to get the PR for the current branch. If no PR exists, tell the user and stop.

## Step 2: Gather context

Once you have the PR number, gather all context using tools. Run these in parallel:

1. **PR metadata**: Run `gh pr view <number> --json title,body,baseRefName,headRefName,number` via Bash
2. **PR diff**: Run `gh pr diff <number>` via Bash
3. **Full paper**: Read the file `gravity-as-constraint.tex`
4. **Methodology**: Read the file `METHODOLOGY.md`

## Step 3: Adversarial Critic (Pass 1)

Use the Task tool with `subagent_type: "general-purpose"` to dispatch a fresh adversarial critic agent. Pass it the following prompt, with the placeholders filled in from the context you gathered:

---

BEGIN CRITIC AGENT PROMPT (fill in placeholders before dispatching):

You are an adversarial critic reviewing a physics paper PR. Your job is to find problems, not praise strengths. Be thorough and specific.
You have NO prior context — evaluate everything from scratch.

# PR Under Review

**Title:** {PR_TITLE}
**PR #{PR_NUMBER}**

## Author's PR Description (contains self-checks)

{PR_BODY}

## Diff (changes to review)

{PR_DIFF}

## Full Paper (for consistency checking)

{FULL_PAPER_CONTENT}

## Project Methodology

{METHODOLOGY_CONTENT}

---

# Your Review Process

You MUST complete Phase 1 entirely before starting Phase 2. Number each finding sequentially (1, 2, 3...).

## Phase 1: Mathematical Review

Do NOT use WebSearch or WebFetch during this phase. Form your own mathematical judgment first.

### Layer 1: Verify Author Self-Checks

The PR description above contains the author's self-check section. For each claim:

- **Dimensional analysis** — independently verify dimensional consistency of every new or modified equation
- **Limiting cases** — independently verify each claimed limiting case actually follows from the math
- **Consistency** — check new results against existing equations in the full paper
- **Order-of-magnitude sanity** — redo numerical estimates from scratch using fundamental constants

For each self-check item, give a verdict: **confirmed**, **error found** (with explanation), or **cannot verify** (with explanation of what's missing).

### Layer 2: Derivation Correctness

Step through every mathematical derivation in the diff:

- Does each step follow logically from the previous?
- Are there sign errors, dropped factors, or wrong identities?
- Are approximations justified and explicitly stated?
- Are there gaps between steps that aren't acknowledged as sketches?

### Layer 3: Scope and Framing

- Is each result correctly labeled as rigorous/sketch/conjecture?
- Do the claims in the PR description accurately reflect what the math shows? (No overclaiming?)
- Are any new assumptions beyond the paper's axioms (Section 2) explicitly flagged?
- Does the contribution stay within the scope of the linked issue?

Categorize all findings as:
- **Critical** — mathematical error, wrong result, result that changes a prediction
- **Important** — unjustified step, misleading rigor label, overclaimed result, unflagged assumption
- **Minor** — notation inconsistency, missing clarification, style issue

## Phase 2: Citation Verification

NOW you may use WebSearch and WebFetch.

Identify every new or modified `\bibitem` in the diff. For each one:

1. **Existence check** — search the web to confirm the paper exists with the claimed author(s), title, journal, and year
2. **Relevance check** — read the abstract or key results of the cited paper and verify it actually supports the specific claim being made in the tex file

Skip citations that already existed in the paper and were not modified by this PR.

Verdict per citation: **verified**, **exists but doesn't support claim**, **not found**, or **details incorrect** (specify what's wrong).

## Output Format

Structure your review EXACTLY as follows:

### Self-Check Verification
| Check | Author's Claim | Verdict | Notes |
|-------|---------------|---------|-------|

(One row per self-check item from the PR description)

### Findings

Number each finding sequentially. For each: severity (Critical/Important/Minor), specific equation/line reference, what's wrong, why it matters.

1. **[Critical/Important/Minor]** ...
2. **[Critical/Important/Minor]** ...

(If no findings: "No issues found.")

### Scope & Framing
- **Rigor labels:** accurate / inaccurate (with specifics)
- **Claims vs. math:** match / overclaimed (with specifics)
- **New assumptions:** none / flagged / unflagged (with specifics)
- **Issue scope:** matches / exceeds (with specifics)

### Citation Verification
| Citation | Exists | Supports Claim | Notes |
|----------|--------|---------------|-------|

(One row per new/modified citation. If no new citations, state "No new or modified citations in this PR.")

END CRITIC AGENT PROMPT

---

Save the critic's full response. If the critic found NO findings (no issues at all), skip Step 4 and go directly to Step 5 with a clean verdict.

## Step 4: Steelman Defender (Pass 2)

Use the Task tool with `subagent_type: "general-purpose"` to dispatch a SECOND fresh agent as a steelman defender. This agent must be independent — it evaluates the artifact on its own merits, not anchored to the critic's reasoning.

Pass it the following prompt, with placeholders filled in:

---

BEGIN DEFENDER AGENT PROMPT (fill in placeholders before dispatching):

You are a steelman defender. An adversarial critic has reviewed a physics paper PR and found issues. Your job is to push back where the critic is wrong or overstating problems. Defend the artifact where it deserves defense. Agree briefly with valid criticisms and move on — spend your effort on points where the review is genuinely wrong.

# PR Under Review

**Title:** {PR_TITLE}
**PR #{PR_NUMBER}**

## Author's PR Description

{PR_BODY}

## Diff (changes to review)

{PR_DIFF}

## Full Paper (for consistency checking)

{FULL_PAPER_CONTENT}

## Project Methodology

{METHODOLOGY_CONTENT}

---

# Adversarial Critic's Review

{CRITIC_REVIEW}

---

# Your Task

For EACH numbered finding from the critic, give a verdict:

- **Valid** — The critic is right. This needs fixing.
- **Overstated** — There's a real concern but the severity is exaggerated or the fix is simpler than implied.
- **Wrong** — The critic is incorrect. The original is fine. Explain why.

Also review the self-check verification table. If the critic marked any self-check as "error found" or "cannot verify", evaluate whether that verdict is correct.

You may use WebSearch and WebFetch if needed to verify claims.

## Output Format

For each numbered finding:

**Finding N: [brief description]**
- Critic's severity: [Critical/Important/Minor]
- Verdict: [Valid/Overstated/Wrong]
- Reasoning: [specific justification — reference equations, line numbers, physics arguments]

If you disagree with any self-check verdict, note it separately.

END DEFENDER AGENT PROMPT

---

## Step 5: Synthesize the Verdict Table

Combine the critic's findings and the defender's verdicts into the final calibrated review. This is the deliverable.

Structure the output EXACTLY as follows:

```
## PR Review: {PR_TITLE}

### Self-Check Verification
(Include the critic's self-check table, with any corrections from the defender noted)

### Verdict Table
| # | Finding | Critic | Defender | Verdict | Action |
|---|---------|--------|----------|---------|--------|
| 1 | [description] | Critical | Valid | **Fix** | [what to do] |
| 2 | [description] | Important | Overstated | **Note** | [why less severe] |
| 3 | [description] | Minor | Wrong | **Dismiss** | [why original is correct] |

### Citation Verification
(Include the critic's citation table)

### Assessment
**Recommendation:** Accept / Revise / Reject
**Summary:** (2-3 sentences)
**Verdict counts:** N Valid | N Overstated | N Wrong
**Items requiring action:** (list only Valid and Overstated findings)
```

Map verdicts to actions:
- Valid → **Fix** (describe what to fix)
- Overstated → **Note** (describe the real concern at correct severity)
- Wrong → **Dismiss** (explain why)

## Step 6: Offer to post

After printing the synthesized review, ask the user:

"Post this review as a comment on PR #<number>?"

Use AskUserQuestion with two options:
- **Yes** — Post as PR comment
- **No** — Keep local only

If yes, post via: `gh pr comment <number> --body "<review text>"`
