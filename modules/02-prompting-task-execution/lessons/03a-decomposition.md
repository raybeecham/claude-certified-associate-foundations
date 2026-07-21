# Lesson 3A: Task Decomposition for Complex Requests

## Overview

Some requests are too large to specify well as a single instruction. When one prompt contains several distinct objectives, the model must decide how to divide attention, invent intermediate structure, and compress multiple kinds of reasoning into one pass.

> Never ask an AI system to solve four different problems in one prompt when you can solve one problem well four times.

Task decomposition converts a complex request into a sequence of discrete, inspectable stages.

## From business goal to prompts

```text
Business goal
      ↓
Workflow
      ↓
Stages
      ↓
Task specifications
      ↓
Prompts
      ↓
Intermediate outputs
      ↓
Evaluation
```

The prompt is not the workflow. It is the instruction used to execute one stage of the workflow.

## The overloaded request

```text
Evaluate these three vendors and tell me which to pick.
```

This sentence hides at least four different tasks:

1. derive evaluation criteria;
2. score each vendor;
3. identify the most important trade-offs; and
4. produce a recommendation.

If these are performed in one pass, the criteria may be invented silently, weights may be inconsistent, scoring may be shallow, and the recommendation may be difficult to audit.

## The decomposed workflow

```text
Requirements
     ↓
Stage 1: Derive criteria
     ↓
Stage 2: Score vendors
     ↓
Stage 3: Analyze trade-offs
     ↓
Stage 4: Recommend
```

### Stage 1: Derive criteria

**Task:** From the approved requirements, derive the evaluation criteria and proposed weights.

**Output:** A criteria table with definitions, weights, and source references.

**Validation:** Confirm that the criteria are complete, non-duplicative, traceable to requirements, and total 100%.

### Stage 2: Score vendors

**Task:** Score each vendor against the approved criteria using only the supplied materials.

**Output:** A scorecard with evidence and unknowns for every score.

**Validation:** Check scoring consistency, evidence traceability, arithmetic, and missing information.

### Stage 3: Analyze trade-offs

**Task:** Identify where the vendors differ most and explain the consequence of each trade-off.

**Output:** A comparison of cost, capability, risk, implementation burden, and uncertainty.

**Validation:** Confirm that each trade-off follows from the scorecard rather than introducing new unsupported claims.

### Stage 4: Recommend

**Task:** Recommend an option and tie the reasoning to the approved weights, evidence, trade-offs, and unresolved risks.

**Output:** A decision brief with recommendation, rationale, conditions, and dissenting considerations.

**Validation:** Confirm that the recommendation follows from the prior stages and that a qualified human retains final decision authority.

## Why decomposition works

### 1. It reduces hidden ambiguity

Each stage has one primary objective rather than several competing verbs.

### 2. It separates reasoning modes

Deriving criteria, scoring evidence, comparing trade-offs, and recommending are different cognitive operations with different success criteria.

### 3. It creates checkable intermediate outputs

If the criteria are wrong, they can be corrected before any scoring occurs.

### 4. It improves auditability

A reviewer can trace the recommendation back through trade-offs, scores, criteria, and source requirements.

### 5. It localizes failure

A weak final answer does not require rebuilding the entire workflow. The failed stage can be repaired and downstream stages rerun.

## The pipeline rule

Every stage should define:

```text
Input
  ↓
Process
  ↓
Output
  ↓
Validation
```

A stage is well designed when another stage can consume its output without guessing what it means.

| Stage field | Question |
|---|---|
| Input | What authoritative material or prior output enters this stage? |
| Process | What single operation is performed? |
| Output | What artifact or structured result is produced? |
| Validation | How do we know the stage succeeded? |
| Owner | Who reviews, approves, or resolves exceptions? |

## When to decompose

Decomposition is usually warranted when the request:

- contains multiple primary verbs;
- uses outputs from one task as inputs to another;
- requires different reasoning styles;
- has intermediate decisions that should be reviewed;
- mixes generative analysis with deterministic calculation;
- includes independent subtasks;
- has a high consequence of error; or
- would be difficult to audit if performed in one pass.

## Do not over-decompose

Decomposition adds coordination cost. A simple rewrite or extraction task does not need a multi-stage workflow.

Use the smallest number of stages that creates meaningful separation, validation, or parallelism.

> Decompose at changes in objective, evidence, method, owner, or validation—not at every sentence.

## One conversation or several?

Keep stages in the same conversation when they build directly on validated prior results and the context remains coherent.

Use a new conversation or clean execution context when:

- the next stage is genuinely independent;
- early context is no longer needed;
- the thread has become degraded or contradictory;
- the stage requires a different trusted source set;
- permissions or data boundaries differ; or
- an independently generated result reduces anchoring bias.

When moving to a new context, transfer only the validated state required for the next stage.

## Sequential versus parallel work

Sequential stages have dependencies:

```text
Criteria → Scores → Trade-offs → Recommendation
```

Independent analyses may run in parallel:

```text
                 ┌→ Cost analysis ─────┐
Requirements ────┼→ Risk analysis ─────┼→ Integrated decision
                 └→ Capability analysis ┘
```

The next lesson examines parallel decomposition in detail.

## Decomposition worksheet

For a complex request, complete this table before writing prompts:

| Stage | Objective | Input | Output | Validation | Depends on | Owner |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

Then ask:

- Which stages are sequential?
- Which are independent?
- Where should a human approve before continuing?
- Which outputs require deterministic checks?
- What must be transferred between contexts?
- What happens if a stage fails?

## Common failure modes

| Failure | Cause | Repair |
|---|---|---|
| Final recommendation cannot be explained | Intermediate reasoning was hidden | Require explicit stage outputs |
| Errors propagate through the workflow | No stage-level validation | Add gates before downstream execution |
| Later stages reinterpret earlier work | Output contracts are vague | Define schemas and accepted terminology |
| Workflow becomes unnecessarily slow | Over-decomposition | Merge stages with the same objective and validation |
| Independent analyses influence each other | Shared context causes anchoring | Run them separately, then integrate |
| Correct prose contains wrong totals | Calculation left to generation | Use deterministic computation and validate |

## Exam lens

Choose decomposition when a scenario contains multiple dependent tasks and the best answer creates ordered, checkable stages.

The strongest exam answer usually:

1. identifies the hidden subtasks;
2. orders them by dependency;
3. validates intermediate output; and
4. ties the final result to those validated stages.

“Make the prompt longer” is weaker than decomposing a genuinely multi-stage request.

## Knowledge check

### Question 1
Why should criteria be approved before vendors are scored?

**Answer:** Because every downstream score and recommendation depends on the criteria. Validating them first prevents systematic error from propagating.

### Question 2
A request asks Claude to extract facts, calculate totals, and draft a recommendation. What is the best design?

**Answer:** Separate extraction, deterministic calculation, and recommendation into stages with validation between them.

### Question 3
When should sequential stages remain in one conversation?

**Answer:** When each stage depends on the prior validated result and the context remains coherent and appropriately scoped.

## Flashcards

**Q:** What is task decomposition?  
**A:** Splitting a complex request into discrete, ordered, checkable stages.

**Q:** What are the four fields in the pipeline rule?  
**A:** Input, Process, Output, and Validation.

**Q:** What is the main benefit of intermediate outputs?  
**A:** They make errors visible and repairable before those errors propagate.

**Q:** When should stages use separate conversations?  
**A:** When they are independent, require different context or permissions, or the current context has degraded.

**Q:** What is the danger of over-decomposition?  
**A:** Added coordination, latency, context transfer, and maintenance without meaningful quality gain.
