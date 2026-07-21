# Lesson 2B: A Worked Build

## Overview

A weak prompt often fails without producing anything obviously false. It may return fluent, plausible prose that is simply too generic, too broad, or too poorly shaped to use.

> A response can be factually harmless and still be operationally unusable.

This lesson builds one prompt in stages so that each improvement can be traced to a specific task-specification component.

## Starting point: everything left implicit

```text
Write a summary of our quarterly operations.
```

| Component | Present? | Consequence |
|---|---:|---|
| Role | No | No clear professional perspective or depth |
| Context | No | No audience, situation, or decision purpose |
| Task | Partly | “Summarize” is clear, but the subject is underspecified |
| Constraints | No | No scope, priority, length, or exclusions |
| Output format | No | No usable structure for the recipient |

A model may return polished prose about throughput, staffing, cost, quality, and delivery. Nothing in the prompt tells it which of those dimensions matters. The likely result is not necessarily wrong. It is generic because the request did not define relevance.

## Build the prompt one component at a time

The goal is a one-page operations update for a regional director. The source is an attached Q3 dataset. The director cares about throughput and cost, and only material deviations should be highlighted.

### Stage 1: Clarify the task

```text
Summarize the attached Q3 operations data.
```

**Improved:** the period, source, and action are clearer.

**Still missing:** audience, priority rule, length boundary, and output shape.

### Stage 2: Add context and audience

```text
I am preparing an update for our regional director, who cares about throughput and cost rather than process detail. Summarize the attached Q3 operations data.
```

**Improved:** the model can prioritize information for a specific reader and suppress irrelevant process detail.

**Still missing:** a measurable definition of importance and a response structure.

### Stage 3: Add a useful role

```text
Act as an operations analyst. I am preparing an update for our regional director, who cares about throughput and cost rather than process detail. Summarize the attached Q3 operations data.
```

**Improved:** the requested perspective and vocabulary are explicit.

> A role is optional. It should clarify perspective, not decorate the prompt. “World-class expert” adds little unless a defined professional lens changes the task.

### Stage 4: Add constraints

```text
Act as an operations analyst. I am preparing an update for our regional director, who cares about throughput and cost rather than process detail. Summarize the attached Q3 operations data, covering only metrics that moved more than 10% against target. Exclude routine process commentary.
```

**Improved:** relevance is measurable, scope is narrower, and non-material changes are excluded.

The phrase “only metrics that moved more than 10% against target” does more work than “focus on the most important results.”

### Stage 5: Add the output contract

```text
Act as an operations analyst.

Context:
I am preparing a one-page update for our regional director, who cares about throughput and cost rather than process detail.

Task:
Summarize the attached Q3 operations data.

Constraints:
- Cover only the three metrics that moved more than 10% against target.
- Exclude routine process commentary.
- Do not introduce facts that are not present in the attached data.

Output:
- One short headline.
- Three bullet points.
- One sentence per bullet.
- Include the metric, direction and size of variance, and operational significance supported by the data.
- If fewer than three metrics meet the threshold, report only those that qualify and state that no additional metrics met it.
```

This is no longer merely a request for prose. It is a bounded task contract.

## Why the final version is stronger

| Quality dimension | Weak prompt | Built prompt |
|---|---|---|
| Audience fit | Unspecified | Regional director |
| Relevance | Model guesses | Quantified threshold |
| Scope | Broad | Material throughput and cost deviations |
| Grounding | Implicit | Attached data only |
| Structure | Model chooses | Headline plus three one-sentence bullets |
| Missing-data behavior | Undefined | Report only qualifying metrics |
| Editing burden | High | Low |
| Evaluation | Subjective | Checkable against explicit requirements |

The model did not become more capable between versions. The task became more observable and less ambiguous.

## Official five-component annotation

```text
Act as an operations analyst.
└─ Role

I am preparing a one-page update for our regional director,
who cares about throughput and cost rather than process detail.
└─ Context and audience

Summarize the attached Q3 operations data.
└─ Task

Cover only the three metrics that moved more than 10% against target.
Exclude routine process commentary.
Do not introduce facts not present in the data.
└─ Constraints

Return one short headline followed by three one-sentence bullets.
└─ Output format
```

For certification questions, recognize:

1. Role
2. Context
3. Task
4. Constraints
5. Output format

## Engineering annotation

| Engineering element | Implementation |
|---|---|
| Business objective | Prepare a usable leadership update |
| Audience | Regional director |
| Role | Operations analyst |
| Context | Q3 operations; throughput and cost matter |
| Evidence | Attached Q3 data |
| Task | Summarize |
| Selection rule | More than 10% against target |
| Constraints | Three metrics maximum; exclude routine detail; no unsupported facts |
| Output contract | Headline plus three one-sentence bullets |
| Uncertainty behavior | Report fewer than three when fewer qualify |
| Success criteria | Correct metrics, correct variances, concise executive relevance |

The official five components remain the exam-facing model. The engineering elements make the task easier to validate and integrate into a real workflow.

## Why “same model, same data” matters

```text
Same model
+ same evidence
+ clearer specification
= higher probability of usable output
```

This does not mean prompts solve every failure. A clearer prompt cannot compensate for missing or inaccurate data, inaccessible attachments, unsuitable models, incorrect calculations, degraded context, unauthorized data use, absent validation, or unclear decision authority.

Ask:

> Did the model misunderstand the task, or was the system unable to support it?

## Minimum sufficient specification

### Low-consequence request

```text
Summarize this note in three bullets for a project manager.
```

This may be sufficient because the task, audience, and output are simple.

### Professional deliverable

A leadership update usually needs all five official components plus explicit evidence and uncertainty behavior.

### Consequential or automated workflow

Also define source hierarchy, validation, tool permissions, escalation, human approval, and monitoring.

The objective is not maximum prompt length. It is minimum sufficient clarity.

## Diagnostic reading of common failures

| Output problem | Likely gap | Better repair |
|---|---|---|
| Generic prose | Context | Add audience, purpose, and relevant background |
| Wrong operation | Task | Replace vague verbs with one primary action |
| Too long | Constraint | Add a measurable length boundary |
| Wrong tone | Context or constraint | Name the reader and tone requirement |
| Data dump | Constraint or selection rule | Define what qualifies as material |
| Wrong shape | Output format | Specify the interface contract |
| Unsupported claims | Evidence boundary | Restrict claims to approved sources |
| Invented completion | Uncertainty behavior | State what to do when evidence is missing |

## Thirty-second preflight

```text
Role        — Is a professional perspective actually useful?
Context     — What can the model not infer safely?
Task        — Is there one clear primary action?
Constraints — What makes the result usable?
Output      — What exact shape should come back?
Evidence    — What may the model rely on?
Failure     — What should happen when information is missing?
```

Thirty seconds of relevant, testable specification can remove several rounds of revision.

## Applied exercise

Start with:

```text
Write an update about customer support.
```

Build it in five passes:

1. Add one unambiguous task verb.
2. Add audience and decision context.
3. Add only a role that changes the required perspective.
4. Add measurable constraints and an evidence boundary.
5. Add an output contract and missing-data behavior.

After each pass, record what ambiguity was removed, what failure became less likely, what remains ambiguous, and whether the added text is necessary.

## Knowledge check

### Question 1

A prompt asks Claude to “summarize the report for leadership.” The result is too detailed and focuses on methodology. Which repair is most direct?

A. Add a more prestigious role
B. Specify the leadership audience, decision purpose, and exclusions
C. Ask Claude to try harder
D. Use a longer response

**Answer: B.** The failure is contextual and constraint-related.

### Question 2

Why is “cover only metrics more than 10% against target” stronger than “focus on important metrics”?

A. It sounds more technical
B. It guarantees accuracy
C. It defines a testable selection rule
D. It removes the need for source data

**Answer: C.** A measurable threshold reduces ambiguity and supports validation.

### Question 3

Only two metrics exceed the threshold. What prevents the model from inventing a third?

A. Role
B. Tone
C. Missing-data behavior
D. A longer context window

**Answer: C.** The prompt explicitly tells the model to report fewer than three when fewer qualify.

## Flashcards

**Front:** Why can a plausible response still be unusable?  
**Back:** Plausibility does not ensure audience fit, relevance, scope, format, or decision usefulness.

**Front:** Why build a prompt in stages?  
**Back:** It makes each quality improvement traceable to a specific component.

**Front:** What does a quantified selection rule provide?  
**Back:** A shared, testable definition of relevance.

**Front:** Is role always required?  
**Back:** No. Use it only when perspective changes vocabulary, assumptions, depth, or method.

**Front:** What is minimum sufficient specification?  
**Back:** The smallest set of explicit details that removes material ambiguity and makes the output usable and testable.

## Exam lens

When a scenario contrasts a vague prompt with a structured one, identify the component responsible for the improvement:

- missing audience or background → **Context**;
- wrong action → **Task**;
- excessive length or scope → **Constraints**;
- unusable structure → **Output format**;
- inappropriate perspective or depth → **Role**, when genuinely relevant.

Prefer the smallest direct repair over adding every possible instruction.

## Key takeaway

> The model did not get smarter. The task became clearer.

A professional prompt makes important decisions explicit before generation begins. The result is easier to produce, review, and use.