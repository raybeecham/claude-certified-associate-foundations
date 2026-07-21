# Lesson 1: Module 2 Introduction

## Overview

Two prompts can describe the same general request and still produce very different results.

```text
Write something about the quarterly results.
```

and

```text
Draft a 250-word update for department leaders. Focus on revenue growth, customer retention, and delivery performance. Use a concise executive tone, open with the main result, include three bullets, and end with one decision needed from leadership.
```

The model did not become more capable between those prompts. The second request reduced ambiguity.

This module treats prompting as a learnable communication discipline. The central skill is not clever wording. It is translating intent into a sufficiently precise task specification.

> **Core principle:** Prompts are not magic. Prompts are specifications.

## What prompting really is

A prompt is the interface between human intent and model behavior.

The user usually begins with an internal goal:

```text
I need an executive update.
```

The model cannot directly observe the unstated audience, evidence, tone, constraints, or definition of success behind that goal. Prompting makes those hidden requirements explicit.

```text
Human intent
     ↓
Task description
     ↓
Model interpretation
     ↓
Candidate output
     ↓
Evaluation and revision
```

A strong prompt narrows the gap between what the user means and what the model can infer.

## Description as an AI fluency competency

The preparation material names this competency **Description**: telling the model precisely what you want.

Description includes more than naming the topic. It may require specifying:

- the objective;
- the audience;
- the relevant context;
- the evidence or source material;
- the boundaries of the task;
- the required process;
- the output format;
- the desired length and tone;
- uncertainty or missing-data behavior; and
- the standard by which the result will be judged.

A vague prompt delegates these decisions to the model. A structured prompt keeps the important decisions with the user.

## The engineering interpretation

From an AI Systems Engineering perspective, a prompt is one component of a larger system.

```text
Business problem
      ↓
Workflow design
      ↓
Task specification
      ↓
Prompt
      ↓
Model output
      ↓
Validation
      ↓
Human decision
```

This distinction matters because not every failure is a prompt failure.

| Observed problem | Likely layer |
|---|---|
| The request is vague | Prompt or task specification |
| The source material is missing | Evidence or retrieval |
| The calculation is unreliable | Deterministic computation |
| The model lacks required capability | Model selection |
| The conversation has become confused | Context management |
| The output cannot be trusted | Evaluation and validation |
| The action exceeds authority | Governance or human approval |

Prompting should improve the task description. It should not be used to hide architectural problems.

## What this module teaches

The module develops four connected capabilities.

### 1. Build prompts from repeatable components

Effective prompts are assembled from functional parts rather than improvised as a single paragraph.

```text
Objective
  + context
  + inputs
  + constraints
  + output contract
  = clearer task specification
```

Later lessons will define the component stack and show how each component changes model behavior.

### 2. Decompose complex work

Some tasks contain multiple reasoning stages, outputs, dependencies, or audiences. Asking for everything at once can create omissions and contradictions.

```text
Complex request
      ↓
Identify stages
      ↓
Sequence dependencies
      ↓
Run independent work in parallel where appropriate
      ↓
Integrate and review
```

Decomposition turns one overloaded request into a manageable workflow.

### 3. Iterate diagnostically

Iteration should not mean repeatedly asking for a better answer.

Weak iteration:

```text
Make it better.
```

Diagnostic iteration:

```text
The analysis identifies the right issues, but it does not distinguish evidence from assumptions. Revise it so every major claim is labeled as sourced fact, inference, or unresolved question.
```

The goal is to identify the failed component and repair that component.

### 4. Adapt strategy to the task type

Different tasks require different prompting strategies.

| Task type | Primary need |
|---|---|
| Analysis | criteria, evidence, comparison, reasoning boundaries |
| Research | source quality, freshness, scope, citation, uncertainty |
| Drafting | audience, purpose, voice, structure, length |
| Brainstorming | diversity, quantity, constraints, selection criteria |
| Extraction | source boundaries, fields, schema, missing-value behavior |
| Classification | label definitions, examples, ambiguity handling |
| Planning | objective, dependencies, resources, milestones, risks |

A strategy that helps one task may weaken another. Highly constrained brainstorming can reduce useful variety, while unconstrained extraction can reduce consistency.

## The module's central loop

The full discipline can be expressed as one loop:

```text
Describe
   ↓
Decompose
   ↓
Generate
   ↓
Evaluate
   ↓
Diagnose
   ↓
Revise the failed component
```

This is more reliable than trying to discover a perfect prompt on the first attempt.

## Prompt quality is not prompt length

A longer prompt is not automatically better.

Additional text is useful only when it reduces meaningful ambiguity or introduces a necessary control.

A prompt becomes weaker when it contains:

- repeated instructions;
- conflicting requirements;
- irrelevant background;
- excessive role-play;
- hidden priorities;
- undefined terms;
- too many goals in one step; or
- constraints that do not support the intended outcome.

The objective is not maximum detail. It is **minimum sufficient clarity**.

## Before and after example

### Vague request

```text
Analyze our customer feedback.
```

The model must guess:

- which feedback;
- what decision the analysis supports;
- which themes matter;
- how evidence should be presented;
- whether quantitative counts are required;
- what format is expected; and
- how uncertainty should be handled.

### Structured request

```text
Analyze the supplied customer-feedback excerpts to help the product team decide which onboarding issue to investigate first.

Use only the supplied excerpts. Group comments into no more than five themes. For each theme, provide:
- a short label;
- the number of excerpts supporting it;
- two representative quotations;
- the likely customer impact; and
- one unresolved question.

Rank the themes by evidence strength and potential impact. Do not invent percentages or causes. If the evidence is insufficient to rank two themes, state that explicitly.
```

The second prompt specifies purpose, evidence boundaries, process, output structure, and uncertainty behavior. It is easier to execute and easier to evaluate.

## Exam lens

Official Domain 1, **Prompting and Task Execution**, represents 14 percent of the exam blueprint.

Expect scenarios that ask for the best improvement to a vague or underperforming request. The strongest answer usually identifies a specific missing element rather than recommending generic additional detail.

Common exam signals include:

- unclear audience;
- multiple tasks combined without structure;
- output does not match the intended format;
- the user keeps rewriting the entire prompt instead of diagnosing the failure;
- a strategy suited to drafting is applied to research or analysis;
- the model invents information because source boundaries were not defined; and
- the user asks for improvement without explaining what failed.

## Learning objectives

By the end of Module 2, you should be able to:

1. create effective prompts for business and technical tasks using a repeatable component structure;
2. apply task decomposition to complex, multi-part requests;
3. iterate diagnostically by repairing the component that failed; and
4. adapt prompting strategy to analysis, research, drafting, brainstorming, and other task types.

## Knowledge check

### Question 1

A manager asks:

```text
Write a report about the project.
```

Which improvement is most useful first?

A. Add a long expert persona.
B. Specify the report's audience, purpose, evidence, and required structure.
C. Ask the model to be highly intelligent.
D. Increase the requested word count.

**Answer: B.** The request lacks a task contract. A persona or greater length does not define the intended outcome.

### Question 2

A prompt produces accurate content but the result cannot be pasted into the required system. Which component most likely needs revision?

A. Model identity
B. Output contract
C. Topic selection
D. Conversation history

**Answer: B.** The content may be correct while the required format remains unspecified or invalid.

### Question 3

A user says, "Make this better," after receiving a draft. What is the main weakness?

A. The instruction does not identify the failed quality dimension.
B. The prompt is too short to be understood.
C. The model should automatically know the user's preference.
D. All revision requests should begin in a new conversation.

**Answer: A.** Diagnostic iteration identifies what failed and what acceptable improvement looks like.

## Flashcards

**Front:** What is the core purpose of a prompt?

**Back:** To translate human intent into a task specification the model can interpret and execute.

---

**Front:** What is Description in the AI Fluency Framework?

**Back:** The competency of telling the model precisely what you want.

---

**Front:** What is minimum sufficient clarity?

**Back:** Including the smallest set of instructions, context, evidence, constraints, and output requirements needed to reduce meaningful ambiguity.

---

**Front:** What are the four central skills in Module 2?

**Back:** Component-based prompting, task decomposition, diagnostic iteration, and strategy adaptation by task type.

---

**Front:** Why is "make it better" a weak iteration instruction?

**Back:** It does not identify which quality dimension failed or define the desired correction.

## Applied exercise

Choose one vague request you might realistically make, such as:

```text
Summarize this document.
```

Rewrite it by adding:

1. the decision or purpose;
2. the intended audience;
3. the authoritative input;
4. the most important constraints;
5. the required output structure; and
6. uncertainty behavior.

Then remove any sentence that does not materially improve execution or evaluation.

## Teach-back prompt

Explain this lesson to another learner using this sentence as the thesis:

> A prompt is a task specification, not a magic phrase.

Your explanation should distinguish prompt failures from evidence, model, context, evaluation, and governance failures.

## Key takeaway

> Consistent output quality comes from structured communication, not cleverness or luck.

The rest of Module 2 will show how to build that structure, divide complex work, diagnose weak results, and select a strategy that fits the task.