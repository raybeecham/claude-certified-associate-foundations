# Lesson 5B: Strategy Checkpoint — Diagnose the Prompt

## Overview

This checkpoint tests whether you can inspect a prompt, identify its **dominant weakness**, and make the **single change** most likely to improve the result.

The goal is not to rewrite every prompt into a long template. It is to diagnose what is missing, ambiguous, or over-specified.

> Good prompting is a calibration problem. Some prompts need more specification. Others need more latitude.

## Course checkpoint result

The learner completed the preparation-course checkpoint with:

```text
All correct
```

The result demonstrates correct recognition of:

- an ambiguous task;
- missing scope and constraints;
- missing context and audience;
- strategy mismatch caused by over-constraining brainstorming; and
- targeted repair rather than wholesale rewriting.

The course checkpoint wording is not reproduced here. The exercises below are original study material covering the same objectives.

## The dominant-weakness principle

A prompt can have several imperfections, but one usually explains most of the likely failure.

Use this sequence:

```text
Inspect the prompt
      ↓
Predict the likely output problem
      ↓
Identify the dominant component or strategy defect
      ↓
Make one targeted change
      ↓
Preserve everything else that still works
```

The best diagnosis is not always the longest list of missing details. It identifies the defect with the highest explanatory power.

## The calibration continuum

```text
Under-specified                  Calibrated                    Over-specified
|-----------------------------------|-----------------------------------|
Too much inference            Enough control               Useful latitude removed
Generic output                Usable output                Stiff or repetitive output
Unclear task                  Clear objective              Premature convergence
Missing boundaries            Validity protected           Creativity suppressed
```

### Under-specification

The prompt leaves information implicit that Claude cannot infer safely.

Typical signs:

- vague verbs such as `improve`, `review`, or `analyze`;
- no audience or decision purpose;
- no scope boundary;
- no evidence boundary;
- no length, tone, or output shape; and
- no behavior for missing information.

### Over-specification

The prompt controls dimensions that should remain flexible for the task.

Typical signs:

- brainstorming is forced through many filters before ideas exist;
- drafting prescribes sentence-level wording and sounds mechanical;
- analysis is burdened with stylistic constraints unrelated to validity;
- research is told exactly which conclusions to reach; and
- one prompt asks for divergence and convergence simultaneously.

### Calibration rule

> Tighten the dimensions that determine validity. Loosen the dimensions that benefit from variation.

## Component-to-symptom map

| Dominant weakness | Likely symptom | Highest-value repair |
|---|---|---|
| Role | Wrong professional lens, depth, or vocabulary | Add a role only when a defined perspective changes the task |
| Context | Generic, misprioritized, or audience-blind output | Add the background, audience, purpose, or prior decision Claude cannot infer |
| Task | Wrong action or unclear improvement goal | Replace vague language with one explicit primary verb and object |
| Constraints | Wrong scope, length, tone, exclusions, or degree of latitude | Add missing boundaries or remove constraints that suppress useful variation |
| Output format | Content may be useful but difficult to consume | Define the required shape, sections, fields, or structure |
| Evidence boundary | Unsupported claims or invented details | Name authorized sources and missing-evidence behavior |
| Task strategy | Task is controlled in the wrong way | Rebalance control and latitude for analysis, research, drafting, or brainstorming |
| Workflow design | One prompt performs several distinct modes shallowly | Decompose the request into validated stages |

## Original checkpoint

Choose the dominant weakness and propose one targeted change before opening the answer key.

### Prompt 1

```text
Polish this.
```

The request appears beside a draft project email.

Choose one:

- Role
- Context
- Task
- Constraints
- Output format
- Task strategy

**Single change:**

> 

### Prompt 2

```text
Explain everything about third-party technology risk.
```

Choose one:

- Role
- Context
- Task
- Constraints
- Output format
- Task strategy

**Single change:**

> 

### Prompt 3

```text
Create a professional update about the implementation project.
```

Choose one:

- Role
- Context
- Task
- Constraints
- Output format
- Task strategy

**Single change:**

> 

### Prompt 4

```text
Generate product names. Every name must be one word, exactly six letters, begin with one of three approved letters, avoid fifteen prohibited terms, express reliability and speed, sound technical but warm, and fit the final naming rubric. Generate and rank the five best options.
```

Choose one:

- Role
- Context
- Task
- Constraints
- Output format
- Task strategy

**Single change:**

> 

<details>
<summary>Answer key and rationales</summary>

## Prompt 1 answer: Task

`Polish` does not define the dimension of improvement.

The strongest repair is to name the intended action, for example:

```text
Rewrite the email so the request is explicit, the tone is concise and constructive, and the final message is under 140 words.
```

This preserves the existing draft while defining what improvement means.

## Prompt 2 answer: Constraints

The topic is too broad to produce a decision-useful answer.

The strongest repair is to define scope, audience, purpose, and length, for example:

```text
For a procurement manager evaluating a software provider, summarize the five most material third-party technology risks that should be assessed before contract award. Limit the response to a one-page checklist and distinguish evidence to request from questions to ask.
```

The primary defect is uncontrolled scope.

## Prompt 3 answer: Context

`Professional` does not identify the reader, purpose, decision, current status, or important facts.

The strongest repair is to provide the audience and use, for example:

```text
Draft a weekly update for the steering committee. The purpose is to explain current status, one schedule risk, the mitigation underway, and the decision needed by Friday.
```

An output format may also help, but context is the dominant missing component.

## Prompt 4 answer: Task strategy and constraint calibration

The request tries to brainstorm and evaluate simultaneously while imposing most final-stage filters before useful range exists.

The strongest repair is to separate divergence from convergence:

```text
Round 1: Generate 30 varied one-word product-name concepts associated with reliability and speed. Do not rank or filter them yet. Avoid only the prohibited terms.

Round 2: Group the ideas, apply the length and brand criteria, then rank the strongest candidates.
```

The problem is not simply that constraints exist. It is that final-selection constraints are applied too early for a brainstorming task.

</details>

## Why the fourth case is different

The first three prompts are under-specified. The fourth is over-specified.

```text
Prompt 1 → too little task precision
Prompt 2 → too little scope control
Prompt 3 → too little context
Prompt 4 → too much early control for brainstorming
```

This distinction matters because `add more detail` is not a universal repair.

A competent prompter can add missing control. A strong prompter can also remove control that harms the task.

## The single-change discipline

When diagnosing a prompt, state the repair as one specific intervention.

Weak diagnosis:

> Make the prompt better and add more detail.

Strong diagnosis:

> Replace `polish` with `rewrite the email so the request is explicit and the tone is concise and constructive`.

A strong answer contains:

1. the dominant weakness;
2. the predicted output symptom;
3. one targeted change; and
4. a reason the change fits the task type.

## Close calls

### Context versus constraints

Use **context** when Claude lacks the situation, audience, purpose, or prior decision.

Use **constraints** when the task is understood but the boundaries are missing.

```text
Who is this for and why?      → Context
How broad, long, formal, or bounded? → Constraints
```

### Task versus output format

Use **task** when Claude does not know what action to perform.

Use **output format** when the action is clear but the returned shape is not.

```text
What should Claude do?        → Task
What should the result look like? → Output format
```

### Constraints versus task strategy

Use **constraints** when a necessary boundary is absent or malformed.

Use **task strategy** when the overall balance of control and latitude is wrong for the task.

A brainstorming request with one unnecessary word limit may have a constraint defect. A request that forces generation, evaluation, filtering, and ranking in the first pass has a broader strategy defect.

## Exam reasoning pattern

For scenario questions:

1. identify the task type;
2. predict what the current prompt will produce;
3. identify the dominant weakness;
4. choose the smallest repair that addresses it;
5. reject options that add unrelated complexity; and
6. check whether the prompt is under-specified or over-specified.

```text
Analysis      → protect criteria and evidence
Research      → protect scope and sources
Drafting      → protect audience and communication shape
Brainstorming → protect range before filtering
```

## Knowledge check

### Question 1

A user says, `Review this plan`, and receives a broad summary instead of a risk assessment. What is the best first repair?

- A. Add an expert role only.
- B. Replace `review` with an explicit instruction to identify risks against named criteria.
- C. Ask for more words.
- D. Change the output into a poem.

**Answer:** B. The task is ambiguous.

### Question 2

A research prompt produces a long but unfocused overview. The question and current-source requirement are already clear, but no geography, time period, or industry is defined. What is missing?

**Answer:** Constraints and scope boundaries.

### Question 3

A draft is accurate and correctly formatted but sounds unnatural because every sentence pattern was prescribed. What is the best repair?

**Answer:** Preserve the factual and structural constraints while loosening sentence-level phrasing.

### Question 4

A brainstorming prompt returns five nearly identical ideas after requiring each idea to satisfy twelve final-selection criteria. What is the dominant problem?

**Answer:** Strategy mismatch caused by premature convergence and over-constraint.

### Question 5

Why should only one dominant change be proposed in a checkpoint diagnosis?

**Answer:** It tests whether the observed failure can be localized and repaired without discarding working parts of the prompt.

## Flashcards

### Flashcard 1

**Q:** What is the objective of prompt diagnosis?

**A:** Identify the dominant weakness and make the smallest targeted repair.

### Flashcard 2

**Q:** What does a vague verb such as `improve` usually indicate?

**A:** An ambiguous task.

### Flashcard 3

**Q:** What usually causes an answer to be broad and unfocused?

**A:** Missing scope or constraints.

### Flashcard 4

**Q:** What usually causes a draft to ignore the reader's priorities?

**A:** Missing context and audience.

### Flashcard 5

**Q:** Can a prompt fail because it has too many constraints?

**A:** Yes. Over-specification can suppress useful latitude, especially during brainstorming.

### Flashcard 6

**Q:** What is the brainstorming calibration rule?

**A:** Diverge first, then apply evaluation and filtering criteria.

## Applied diagnostic drill

For each prompt below, write:

1. dominant task type;
2. likely output symptom;
3. dominant component or strategy weakness;
4. one targeted repair; and
5. what should remain unchanged.

### A

```text
Analyze the attached report.
```

### B

```text
Draft an announcement for everyone.
```

### C

```text
Research recent developments and tell me what they mean.
```

### D

```text
Brainstorm ten ideas, but reject anything that is not immediately feasible, inexpensive, approved by every stakeholder, and ready to launch this month.
```

### E

```text
Extract the five fields listed below into valid JSON.
```

Prompt E may already be sufficiently specified if the source, field definitions, missing-data behavior, and schema are supplied. Diagnosis should not invent a defect merely because the prompt is short.

## Certification lens

The checkpoint reinforces four exam habits:

- identify the missing or mishandled component rather than saying `be more specific`;
- prefer one targeted repair over a complete rewrite;
- recognize task-strategy mismatch, not only missing details; and
- calibrate in both directions by adding necessary control or restoring useful latitude.

## Think like an AI systems engineer

Prompt quality is not proportional to prompt length.

```text
Too little specification → uncontrolled inference
Enough specification     → usable task contract
Too much specification   → unnecessary rigidity
```

The target is the **minimum sufficient specification** for the task, risk, evidence, and downstream use.

## Related material

- [Strategy by Task Type](05a-strategy-by-task-type.md)
- [Iterating to Improve Output](04-iterating-to-improve-output.md)
- [Component Stack](02a-component-stack.md)
- [Checkpoint prompt notebook](../../../prompts/module-02/05b-strategy-checkpoint-prompts.md)
- [Prompt Calibration Pattern](../../../patterns/prompt-calibration-pattern.md)
