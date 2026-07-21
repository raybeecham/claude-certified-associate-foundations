# Lesson 4: Iterating Prompts to Improve Output

## Overview

A first draft rarely lands perfectly. The professional skill is not rewriting the entire prompt whenever the output disappoints. It is observing the output, diagnosing the failure, changing the smallest responsible component, and checking whether the revision actually helped.

> Never rewrite a prompt before you understand why it failed.

Iteration is a controlled feedback loop:

```text
Task specification
      ↓
Candidate output
      ↓
Observe
      ↓
Diagnose
      ↓
Modify one component
      ↓
Validate
      ↓
Continue, accept, edit, escalate, or stop
```

## Output deficiencies are diagnostic signals

A weak output often points back to a specific defect in the task specification.

| Output symptom | Likely cause | Targeted fix |
|---|---|---|
| Generic or off-base | Context is thin | Add the background, audience, decision purpose, or source material the model could not infer |
| Answers the wrong question | Task verb or scope is ambiguous | Sharpen the primary instruction and define the object of the task |
| Wrong length, tone, or shape | Constraint or output contract is missing | Add the missing boundary or format requirement |
| Misses one section | One required element is underspecified | Revise only that section or output requirement |
| Unsupported claims | Evidence boundary is weak | Provide authoritative evidence and prohibit unsupported invention |
| Inconsistent sections | Too many competing objectives | Decompose the work or establish a shared foundation |
| Incorrect arithmetic | Wrong execution layer | Use Code Execution or another deterministic method |
| Repeats earlier mistakes | Context has degraded or stale state persists | Summarize, restart, or reconstruct clean context |
| Cannot complete the task | Missing data, permissions, or tool access | Fix the system condition rather than the wording |

The objective is failure localization, not prompt decoration.

## The one-change rule

Change one significant variable at a time whenever practical.

If role, context, task, constraints, and format are all rewritten together, the result may improve, but you will not know which change mattered. That makes the workflow harder to learn from, reproduce, and maintain.

```text
Observe one failure
      ↓
Select one likely cause
      ↓
Change one responsible component
      ↓
Compare against the prior output
```

The rule is not absolute. A severely underspecified prompt may need several foundational components at once. After the first repair, however, subsequent iterations should become targeted.

## A live diagnose-and-fix cycle

### Round 1

**Prompt**

```text
Write a follow-up email to the client about the delayed deliverable.
```

**Likely output**

A generic, slightly defensive email that does not explain the cause, provide a revised date, or establish the intended tone.

**Diagnosis**

- context is missing;
- the new delivery date is missing;
- the tone constraint is missing; and
- the output contract does not request a subject line.

This prompt is sufficiently underspecified that the first repair should add the essential task contract.

### Round 2

**Revised prompt**

```text
Write a follow-up email about a two-day delay on an analytics deliverable.

Context:
The delay was caused by a data-quality issue that has now been corrected. The revised delivery date is Thursday.

Constraints:
Use an accountable, calm tone without over-apologizing. Keep the message under 120 words.
```

**Likely output**

A concise note containing the cause, revised date, and accountable close.

**Diagnosis**

The body is usable. The remaining defect is narrow: no subject line.

### Round 3

**Targeted revision**

```text
Keep the body unchanged. Add a subject line that signals resolution and the revised delivery date rather than emphasizing the delay.
```

**Result**

The revision changes only the missing component while preserving the body that already works.

## Preserve what works

A useful draft is working state. Do not discard it casually.

When most of the output is correct:

1. identify the defective section;
2. state what must remain unchanged;
3. specify the narrow revision;
4. compare the revision against the prior version; and
5. verify that the repair did not damage working content.

Example:

```text
Keep the recommendation and evidence table unchanged. Rewrite only the risk section so that each risk includes likelihood, impact, mitigation, and owner.
```

This is more controlled than asking for a complete rewrite.

## Compare revisions, do not rely on impression

For each round, compare against explicit criteria.

| Dimension | Round 1 | Round 2 | Round 3 |
|---|---:|---:|---:|
| Includes cause | No | Yes | Yes |
| Includes revised date | No | Yes | Yes |
| Appropriate tone | Weak | Yes | Yes |
| Under 120 words | Unknown | Yes | Yes |
| Subject line | No | No | Yes |
| Manual editing required | High | Low | Minimal |

A revision is successful when it improves the failed dimension without degrading important dimensions that already passed.

## When not to iterate the prompt

Prompt revision is not always the correct intervention.

| Failure | Correct intervention |
|---|---|
| Source document is missing | Obtain the source |
| Evidence is stale | Refresh the evidence |
| Calculation is unreliable | Use deterministic execution and verify inputs |
| Model is unsuitable | Test a more appropriate model or route exceptions |
| Conversation has drifted | Restart with a validated state capsule |
| Tool lacks permission | Correct authorization or remove the action |
| Output requires legal or domain authority | Escalate to a qualified reviewer |
| Success criteria were never defined | Define evaluation before further iteration |

> Change the prompt when the failure is instructional. Change the system when the failure is architectural.

## Knowing when to stop

Iteration has converged when another round is unlikely to create enough value to justify its cost.

```text
Large improvement
      ↓
Moderate improvement
      ↓
Small improvement
      ↓
Marginal change
      ↓
Stop
```

Stop when one of these conditions is met:

- the acceptance criteria pass;
- remaining edits are faster manually;
- the next change is stylistic rather than substantive;
- repeated runs vary without improving;
- the failure belongs outside the prompt;
- additional work requires human judgment; or
- time, cost, or risk exceeds the expected benefit.

> Optimize until the expected value of the next iteration is lower than its cost.

## Diagnostic iteration record

For consequential or recurring workflows, record each meaningful iteration.

| Field | Entry |
|---|---|
| Prompt version | |
| Output version | |
| Observed symptom | |
| Suspected cause | |
| Component changed | |
| Elements preserved | |
| Evaluation criteria | |
| Result | Improved / unchanged / degraded |
| Next decision | Continue / accept / edit / escalate / stop |

This creates traceability and prevents cycling through the same failed revisions.

## Exam lens

The best answer usually identifies the smallest change that directly addresses the observed symptom.

Look for pairings such as:

- generic output → add missing context;
- wrong action → sharpen the task;
- wrong length or tone → add constraints;
- wrong structure → define the output format;
- one weak section → revise only that section;
- mostly correct output → preserve working content;
- diminishing returns → stop and perform a quick manual edit.

Avoid answers that rewrite everything without diagnosis or rely on the model to rate its own quality.

## Knowledge check

### 1. A report is accurate and well structured, but the executive summary is too technical. What is the best next step?

Revise only the executive summary with an audience and tone constraint while preserving the validated report body.

### 2. A revised prompt improves tone but removes two required facts. Did the iteration succeed?

No. It improved one dimension while degrading completeness. Restore the required facts and evaluate both tone and completeness.

### 3. A prompt produces incorrect totals despite several wording changes. What should change?

Move the arithmetic into a deterministic execution layer and validate the inputs and method.

## Flashcards

**Q:** What is the first step after receiving a disappointing output?  
**A:** Observe and classify the specific deficiency before revising anything.

**Q:** What is the one-change rule?  
**A:** Change one significant responsible component at a time whenever practical.

**Q:** Why preserve working text?  
**A:** It reduces regression risk and makes the effect of the revision easier to evaluate.

**Q:** When has iteration converged?  
**A:** When acceptance criteria pass or further prompting produces only marginal value.

**Q:** When should the system change instead of the prompt?  
**A:** When the failure involves evidence, computation, model fit, context, tools, authority, or validation.

## Applied exercise

Use this output symptom:

> The draft policy memo is well written but contains no source references, combines facts with assumptions, and recommends action despite two unresolved questions.

Complete the following:

1. classify each symptom;
2. identify the responsible prompt or system component;
3. propose the smallest revision for each defect;
4. state what should remain unchanged;
5. define acceptance criteria for the next round; and
6. decide whether human review is required before release.

## Key takeaway

> Do not optimize blindly. Diagnose first, change the smallest responsible component, compare the result, and stop when the output is fit for use.