# Lesson 2A: Component Stack

## Overview

A professional prompt is easier to design and repair when it is treated as a set of functional components rather than one block of improvised prose.

> The official five-component stack is Role, Context, Task, Constraints, and Output Format.

Not every request needs all five. The purpose of the stack is not to make prompts longer. It is to make missing information visible before the request is sent.

## The official five components

| Component | What it controls | Typical failure when missing |
|---|---|---|
| Role | Perspective, vocabulary, depth, and assumptions | Generic or misaligned professional framing |
| Context | Audience, situation, prior decisions, source material, and purpose | Generic output or invented assumptions |
| Task | The primary action Claude should perform | Wrong operation or ambiguous scope |
| Constraints | Boundaries such as length, tone, inclusions, exclusions, and prohibited behavior | Output that is unusable without substantial editing |
| Output format | The shape and interface of the result | Correct ideas in the wrong form |

## 1. Role

A role specifies the perspective required for the task.

```text
Act as an operations analyst reviewing quarterly performance.
```

A useful role changes how the task should be interpreted. Decorative roles such as “world-class expert” usually add little.

**Decision rule:** Include a role only when a defined professional lens, vocabulary, or standard materially changes the result.

## 2. Context

Context is everything Claude must know that cannot be inferred safely.

This may include:

- audience;
- situation;
- prior decisions;
- definitions;
- business rules;
- source material;
- scope;
- assumptions; and
- exclusions.

```text
The audience is a regional director who cares about throughput and cost, not process detail.
```

Context is often the most important missing component because people naturally assume that information in their own head is already shared.

## 3. Task

The task states the action using a clear primary verb.

Common verbs include:

- summarize;
- compare;
- extract;
- classify;
- draft;
- evaluate;
- identify;
- rank; and
- recommend.

```text
Compare the three options against the approved evaluation criteria.
```

Different verbs imply different success conditions. “Summarize” and “evaluate” are not interchangeable.

## 4. Constraints

Constraints keep the result inside usable boundaries.

Examples include:

- maximum length;
- tone;
- required inclusions;
- exclusions;
- allowed evidence;
- prohibited assumptions;
- privacy restrictions;
- time horizon; and
- safety boundaries.

```text
Cover only metrics that moved more than 10% against target. Exclude routine process commentary.
```

Prefer measurable constraints over vague preferences.

## 5. Output format

Output format defines the shape of the deliverable.

Examples include:

- table;
- bullet list;
- executive summary;
- email;
- memo;
- JSON;
- CSV;
- presentation outline; and
- requirements document.

```text
Return one headline followed by three one-sentence bullets.
```

The downstream consumer should determine the format.

## The engineering extension

The five-component stack is the certification foundation. Higher-consequence work often needs additional task-specification elements:

| Engineering component | Question answered |
|---|---|
| Business objective | Why is this task being performed? |
| Evidence boundary | What information may the model rely on? |
| Process | What stages or method should be followed? |
| Uncertainty behavior | What should happen when information is missing or conflicting? |
| Success criteria | How will the result be judged? |
| Review | Who verifies or approves consequential output? |

```text
Business objective
      ↓
Role + Context + Task + Constraints + Output
      ↓
Evidence + Process + Uncertainty + Success Criteria
      ↓
Candidate output
      ↓
Evaluation and human review
```

## Minimum sufficient specification

A prompt should contain the smallest set of components needed to remove material ambiguity.

| Task | Likely minimum |
|---|---|
| Simple factual question | Task |
| Quick rewrite | Task + constraint |
| Executive draft | Context + task + constraints + output |
| Professional analysis | Context + task + evidence + constraints + output + success criteria |
| Consequential recommendation | Full task specification plus validation and accountable review |

## Diagnostic checklist

When an output disappoints, ask:

1. Was the professional perspective wrong? Check the role.
2. Was the answer generic or based on assumptions? Check context.
3. Did Claude perform the wrong operation? Check the task verb.
4. Was the result too long, broad, or off-tone? Check constraints.
5. Was the content useful but difficult to use? Check output format.
6. Were claims unsupported? Check the evidence boundary.
7. Did the model guess when it should have stopped? Check uncertainty behavior.
8. Are we unable to say whether the result passed? Define success criteria.

## Knowledge check

### Question 1
A draft is accurate but far too detailed for an executive audience. Which component most directly needs revision?

**Answer:** Constraints, especially audience-appropriate length and level of detail.

### Question 2
Claude summarizes a document when the user wanted competing options ranked. Which component failed?

**Answer:** Task. The primary action was ambiguous or incorrect.

### Question 3
A response uses plausible but unsupported background assumptions. Which component is most likely missing?

**Answer:** Context, and possibly an explicit evidence boundary.

## Flashcards

**Q:** What are the official five prompt components?  
**A:** Role, Context, Task, Constraints, and Output Format.

**Q:** Which component is most commonly omitted?  
**A:** Context.

**Q:** Is a role required in every prompt?  
**A:** No. Use it only when a professional perspective materially changes the task.

**Q:** Why specify output format?  
**A:** To make the result usable by its downstream consumer without another formatting pass.

**Q:** What is the purpose of the stack?  
**A:** To expose missing task information and make prompt diagnosis repeatable.
