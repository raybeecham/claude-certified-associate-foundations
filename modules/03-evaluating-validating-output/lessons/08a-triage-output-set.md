# Lesson 8A: Exercise — Triage the Output Set

## Completion record

The preparation-course exercise was completed with all four classifications aligned to the revealed model answers.

```text
Result: 4 of 4 classifications correct
```

The demonstrated decisions were:

1. a low-stakes internal draft could proceed after light editing;
2. an internally contradictory total required revision and deterministic recomputation;
3. precise but untraceable statistics required revision and source validation; and
4. a regulatory submission required qualified human review regardless of surface quality.

This public lesson uses original fictional scenarios rather than reproducing proprietary course questions.

---

# Overview

Triage converts evaluation findings into an action.

The reviewer is not merely asking whether an output is good or bad. The reviewer must decide whether it can be used now, repaired within the existing workflow, or transferred to qualified human ownership.

This lesson uses three verdicts:

| Verdict | Meaning |
|---|---|
| **Ready to use** | The output is adequate for the stated low- or proportionate-risk use after any minor editing |
| **Needs revision** | A bounded defect can be corrected, verified, and re-evaluated within the workflow |
| **Needs human override** | Stakes, uncertainty, missing authority, governing obligations, or severe defects require qualified human control |

> Triage is a decision about both the output and the use—not merely how polished the text appears.

---

# Plain-English explanation

Ask two different questions:

```text
How good is the output?
          +
How risky is the intended use?
          ↓
What should happen next?
```

These questions are related, but they are not the same.

A rough internal brainstorm may look messy and still be safe to use as a starting point.

A clean regulatory summary may look excellent and still require expert review before submission.

The beginner shortcut is:

```text
Small, fixable issue + contained use → revise or use with light editing
Missing support or wrong calculation → revise and verify
High consequence or required authority → human override
```

---

# One analogy: emergency triage

In emergency triage, the order of attention is not determined by who looks the most composed or who makes the most noise.

A person with a visible minor injury may need simple treatment. A calm person with a hidden high-risk condition may require immediate specialist attention.

AI-output triage follows a similar principle:

- visible roughness does not always mean high risk;
- polished appearance does not always mean low risk;
- the consequence and required expertise determine the response; and
- the reviewer must identify the correct next action rather than merely describe the symptoms.

```text
Appearance
    ≠
Risk
    ≠
Required review level
```

This is only an analogy. It is not medical guidance.

---

# The two-axis triage model

Evaluate outputs on two axes.

## Axis 1: Output condition

Ask:

- Are the requirements met?
- Are claims supported?
- Are calculations correct?
- Is anything material missing?
- Is the output internally consistent?
- Is the framing fair?
- Is the format usable?

## Axis 2: Use risk

Ask:

- What is the consequence if wrong?
- Can the action be reversed?
- Who will see or rely on it?
- Is the work regulated, contractual, confidential, or professionally governed?
- Is qualified review required by policy?

## Combined matrix

| Output condition | Use risk | Likely verdict |
|---|---|---|
| Adequate | Low | Ready to use |
| Minor presentational weakness | Low | Ready to use with light editing |
| Bounded factual, calculation, citation, or completeness defect | Low or material | Needs revision |
| Strong draft | High or governed | Needs human override or mandatory qualified review |
| Severe unsupported or conflicting output | Any material use | Needs human override, reconstruction, or rejection |

The highest-risk condition controls the minimum review requirement.

---

# Original exercise

Classify each output as:

- Ready to use
- Needs revision
- Needs human override

State the dominant reason and next action.

## Output A: workshop-starter ideas

An AI assistant produces twelve ideas for an internal process-improvement workshop. The list is clearly labeled `rough starting ideas`. Eight ideas are useful, while four are generic or repetitive. No client, public, legal, financial, or regulated use is planned.

### Best verdict

**Ready to use with light editing.**

### Why

- low stakes;
- internal audience;
- explicitly provisional;
- easily reversible; and
- weak entries can be removed without changing the purpose.

### Next action

Trim repetitive ideas and use the remaining list to start the workshop.

---

## Output B: inconsistent resource total

A weekly internal resource summary lists six workstreams with assigned staff counts. The reported total is `128`, but the six line items sum to `121`.

### Best verdict

**Needs revision.**

### Why

The output contains an internal arithmetic contradiction. The correct total cannot be selected by prose confidence or majority guess.

### Next action

- inspect the line items;
- confirm whether any workstream was omitted;
- recompute using code or the authoritative staffing system;
- correct the total; and
- recheck downstream statements that relied on it.

---

## Output C: untraceable market statistics

A market brief includes three precise adoption percentages and a year-over-year growth claim. The document provides no source names, links, publication dates, populations, or methodologies.

### Best verdict

**Needs revision.**

### Why

The figures are precise but unauditable. They may be correct, fabricated, stale, out of scope, or based on incomparable populations.

### Next action

- locate authoritative sources;
- verify that each source supports the full claim;
- add checkable citations;
- preserve scope and date; and
- remove or qualify any figure that cannot be supported.

---

## Output D: agency-submission summary

An AI assistant drafts a summary for submission to an environmental oversight agency. Several points have been spot-checked and appear accurate. The document is clear, complete-looking, and professionally formatted.

### Best verdict

**Needs human override.**

### Why

- regulatory audience;
- potentially lasting official record;
- high consequence if incomplete or misstated;
- governing requirements may apply; and
- spot-checking is not complete qualified review.

The draft may be useful input, but it cannot become the submission solely because it looks clean.

### Next action

Require an authorized subject-matter and compliance reviewer to inspect the controlling evidence, filing requirements, calculations, disclosures, and final approved version before submission.

---

# What the exercise tests

## 1. Appearance is not risk

The roughest-looking output may have the lowest consequence.

The cleanest-looking output may require the strongest gate.

## 2. A defect does not always require escalation

A bounded arithmetic or citation defect may be repaired and verified within the workflow.

Human override is reserved for cases where consequence, authority, evidence, policy, or professional judgment requires it.

## 3. High stakes can override good apparent quality

A well-written regulated or external deliverable still requires the mandated reviewer.

```text
High-quality draft
      ≠
Authorized final output
```

## 4. The reason should identify the controlling issue

Weak reason:

```text
It seems risky.
```

Stronger reason:

```text
The output is intended for a regulator, creates an official and difficult-to-reverse record, and therefore requires qualified review under the Diligence thresholds.
```

## 5. Triage must specify the next action

A verdict without an action is incomplete.

```text
Ready to use        → proceed for the stated use
Needs revision      → repair, verify, and re-evaluate
Needs human override → transfer substantive control to a qualified reviewer
```

---

# Practical example: an executive dashboard note

## Generated note

```text
Customer escalations declined 22% this month, demonstrating that the new routing process has resolved the underlying support issue.
```

## Review findings

- The dashboard shows a 22% month-over-month decline.
- The reporting period contains two fewer business days.
- A major customer's tickets were temporarily routed through another queue.
- The data does not establish that the new process caused the decline.
- The note is intended for an executive operating review.

## Triage

**Needs revision.**

The metric may be accurate, but the causal claim exceeds the evidence and relevant conditions are omitted.

## Repair

```text
Customer escalations declined 22% month over month. The period contained two fewer business days, and one major customer's tickets were temporarily routed through another queue. Additional observation is needed before attributing the decline to the new routing process.
```

## Why this is not automatically human override

The note supports an internal operating discussion and its defects are bounded and correctable. A qualified executive or operational review may still be appropriate, but the scenario does not necessarily require transfer to a regulated specialist.

If the same claim were used in a public earnings statement or contractual performance report, the review requirement would rise.

---

# The triage protocol

```text
1. Define the intended use
          ↓
2. Assess output condition
          ↓
3. Apply the Discernment references
          ↓
4. Apply the Diligence thresholds
          ↓
5. Identify the dominant defect or gate
          ↓
6. Choose the verdict
          ↓
7. State the next action
          ↓
8. Record unresolved uncertainty and reviewer ownership
```

## Step 1: Define use

Record:

- audience;
- decision or action;
- draft versus final status;
- reversibility;
- governing obligations; and
- consequence if wrong.

## Step 2: Assess condition

Check:

- requirements;
- sources;
- professional standards;
- accuracy;
- completeness;
- consistency;
- bias;
- audience fit; and
- output format.

## Step 3: Identify the controlling issue

Examples:

```text
Generic internal ideas          → low-stakes quality issue
Numbers do not reconcile        → calculation defect
Precise statistics lack sources → grounding defect
Regulatory submission           → mandatory human-review gate
```

## Step 4: Choose and document the verdict

Use one sentence:

```text
[VERDICT] because [CONTROLLING REASON]; next, [REQUIRED ACTION].
```

---

# Mapping the three verdicts to the wider module

| Exercise verdict | Wider Module 3 actions |
|---|---|
| Ready to use | Release for the stated use, possibly after light editing |
| Needs revision | Edit and/or verify, then re-evaluate |
| Needs human override | Escalate, reconstruct, or reject until qualified ownership is established |

The five-action model is more granular, but the three exercise verdicts are easier for rapid daily classification.

---

# Common anti-patterns

## Anti-pattern 1: Messy means unsafe

**Failure:** A rough internal draft is escalated solely because it is unpolished.

**Repair:** Separate presentation quality from consequence and intended use.

## Anti-pattern 2: Polished means ready

**Failure:** A regulated or external draft bypasses mandatory review.

**Repair:** Apply Diligence thresholds before judging surface quality.

## Anti-pattern 3: Every error triggers human override

**Failure:** Routine bounded defects are over-escalated.

**Repair:** Revise and verify when the problem is correctable within the workflow.

## Anti-pattern 4: Re-prompting a wrong calculation

**Failure:** The model produces another plausible total without deterministic computation.

**Repair:** Recompute using code or the authoritative system.

## Anti-pattern 5: Adding citation-shaped text

**Failure:** A source name is generated without actual verification.

**Repair:** Locate, open, and inspect authoritative support.

## Anti-pattern 6: Spot-checking replaces full review

**Failure:** A consequential filing is approved because a few claims were correct.

**Repair:** Apply the complete review standard and required approval gate.

## Anti-pattern 7: Verdict without action

**Failure:** The reviewer labels the output but does not define what happens next.

**Repair:** Add the repair, verification, escalation, or release step.

---

# Exam reasoning pattern

For output-triage scenarios:

1. identify intended use and audience;
2. assess whether the output has a bounded defect;
3. apply requirements, source material, and professional standards;
4. separate accuracy from completeness;
5. identify hallucination, inconsistency, bias, or grounding failures;
6. assess stakes, reversibility, audience, and regulatory exposure;
7. recognize mandatory human-review categories;
8. do not confuse polish with safety or roughness with danger;
9. choose ready to use, needs revision, or needs human override; and
10. state the required next action.

```text
Low-risk provisional draft       → ready with proportionate editing
Internal contradiction           → revise and recompute
Untraceable precise claims       → revise and validate sources
Regulatory or consequential use  → qualified human override
```

---

# Knowledge check

## Question 1

Why can a rough brainstorm be ready to use?

**Answer:** Because it is low stakes, internal, reversible, and clearly provisional; weak entries can be removed without requiring specialist control.

## Question 2

Why does a conflicting total normally receive `needs revision`?

**Answer:** The defect is bounded and can be resolved through authoritative inputs and deterministic recomputation.

## Question 3

Why are precise unsourced statistics not ready to use?

**Answer:** Precision creates an appearance of authority, but the claims remain unverified until their sources, scope, date, and support are checked.

## Question 4

Why does a clean regulatory draft require human override?

**Answer:** The intended use is high stakes, governed, and difficult to reverse. Mandatory qualified review applies independently of appearance.

## Question 5

What are the two triage axes?

**Answer:** Output condition and use risk.

## Question 6

Does `needs human override` mean a quick approval click?

**Answer:** No. It means a qualified person must take substantive control of the evidence, analysis, compliance, and final release decision.

## Question 7

What should every verdict include?

**Answer:** The controlling reason and the required next action.

---

# Flashcards

## Flashcard 1

**Q:** What are the three triage verdicts?

**A:** Ready to use, needs revision, and needs human override.

## Flashcard 2

**Q:** What two axes drive triage?

**A:** Output condition and intended-use risk.

## Flashcard 3

**Q:** What verdict fits a bounded calculation defect?

**A:** Needs revision, followed by deterministic recomputation and re-evaluation.

## Flashcard 4

**Q:** What verdict fits a governed external filing?

**A:** Needs human override, even when the draft appears accurate and polished.

## Flashcard 5

**Q:** Why is appearance an unreliable triage signal?

**A:** Surface quality does not reveal evidence strength, consequences, authority, or governing obligations.

## Flashcard 6

**Q:** When is light editing enough?

**A:** When the use is low stakes, internal, reversible, and the weaknesses are minor and nonmaterial.

## Flashcard 7

**Q:** What follows `needs revision`?

**A:** Targeted repair, verification, and a new triage decision.

## Flashcard 8

**Q:** What follows `needs human override`?

**A:** Qualified human ownership, required validation, and an authorized release decision.

---

# Short recap

```text
1. Judge both the output and the intended use.
2. Do not confuse roughness with risk.
3. Do not confuse polish with release readiness.
4. Use ready to use for adequate, low-risk outputs.
5. Use needs revision for bounded, correctable defects.
6. Use needs human override for consequential, governed, uncertain, or authority-dependent work.
7. Recompute conflicting numbers deterministically.
8. Verify precise claims against auditable sources.
9. State the reason and next action.
10. Treat the highest-risk condition as controlling.
```

> Appearance and risk are different axes. Triage the use, not just the prose.

## Related material

- [Choosing Output Formats](07-choosing-output-formats.md)
- [Diligence: When Human Review Is Non-Negotiable](05-diligence-human-review.md)
- [Discernment: Accuracy and Completeness](02-discernment-accuracy-completeness.md)
- [Module 3 overview](../README.md)
- [Triage Output Set prompt notebook](../../../prompts/module-03/08a-triage-output-set-prompts.md)
- [Three-Reference Discernment Pattern](../../../patterns/three-reference-discernment-pattern.md)
- [Human Review Gate Pattern](../../../patterns/human-review-gate-pattern.md)
