# Lesson 7A: Module 2 Quiz — Prompting Foundations

## Overview

This quiz checks whether you can apply the complete Module 2 framework to short professional scenarios.

The goal is not to select the longest prompt, the strongest model, or the most elaborate workflow by default. The goal is to identify the intervention that most directly addresses the observed failure.

The five assessed capabilities are:

1. component-based task specification;
2. sequential decomposition;
3. diagnostic iteration;
4. task-strategy calibration; and
5. deterministic verification.

> Strong prompting decisions are targeted: repair the actual defect, preserve what already works, and use the appropriate execution layer.

## Course quiz result

The learner completed the preparation-course quiz with:

```text
Full marks — 5/5
```

The result demonstrates complete coverage of the course quiz objectives:

- identifying missing context and output requirements;
- decomposing multi-stage evaluations;
- revising only the components that failed;
- preserving latitude during brainstorming; and
- routing arithmetic to code execution.

The proprietary course questions are not reproduced here. The assessment below uses original scenarios that test the same skills.

## How to reason through scenario questions

Use this sequence before choosing an answer:

```text
Observe the symptom
      ↓
Identify the task type
      ↓
Locate the dominant defect
      ↓
Choose the smallest effective intervention
      ↓
Reject unrelated complexity
      ↓
Check whether validation or tools are required
```

### Common distractor patterns

Certification questions often include plausible but weak interventions:

- switching models before fixing an under-specified task;
- asking the model to try harder;
- increasing output length without defining usefulness;
- retrying the same prompt repeatedly;
- recommending before criteria are established;
- manually repairing output while leaving a reusable workflow broken;
- trusting arithmetic produced through prose; and
- applying final-selection filters during the first brainstorming pass.

These choices may change the output, but they do not correct the dominant design problem.

---

# Original five-question quiz

Answer all five questions before opening the answer key.

Target score: **5/5 for mastery** or **4/5 for provisional readiness**.

## Question 1 — Component specification

A program lead asks:

```text
Write an update about the new dashboard.
```

The response is polished but generic. It does not explain who the dashboard is for, the operational problem it solves, or where the update will be published.

Which single intervention is strongest?

- **A.** Ask for a more compelling and creative answer.
- **B.** Add the audience, communication channel, key operational benefit, and required output shape.
- **C.** Use a stronger model with the same instruction.
- **D.** Generate five versions and select the most detailed one.

## Question 2 — Decomposition

A sourcing team must compare four service providers against an approved requirements package and recommend one for a pilot.

Which workflow is most reliable?

- **A.** Ask for scores, trade-offs, and a recommendation in one uninterrupted response.
- **B.** Ask for a recommendation first, then request supporting reasons.
- **C.** Derive and approve criteria, score each provider against the same criteria, analyze material trade-offs, then produce the recommendation.
- **D.** Evaluate each provider in a separate context without sharing an approved scorecard.

## Question 3 — Diagnostic iteration

A status brief is factually accurate and uses the required sections. However, it is 900 words when the executive audience needs approximately 250 words, and the prose is more formal than requested.

What is the most efficient next step?

- **A.** Rewrite every component of the prompt.
- **B.** Preserve the facts and structure, revise the length and tone constraints, and compare the new output with the prior version.
- **C.** Switch models and regenerate without changing the task specification.
- **D.** Abandon the prompt and shorten this one document manually.

## Question 4 — Strategy by task type

A design team wants a broad pool of possible names for an internal analytics tool before conducting legal, brand, and feasibility screening.

How should the first prompt be calibrated?

- **A.** Apply the final legal, length, brand, and scoring rubric before generating ideas.
- **B.** Request one safest name so the team avoids reviewing weak concepts.
- **C.** Define the naming goal and hard prohibited boundaries, request substantial volume and variation, and defer ranking and most filters.
- **D.** Prescribe one creative direction and require all names to follow it.

## Question 5 — Verified computation

A prompt asks Claude to summarize quarterly transaction activity and calculate the median transaction value. The narrative appears reasonable, but the median conflicts with the spreadsheet total.

What is the strongest repair?

- **A.** Ask Claude to calculate the median several more times and use the most common answer.
- **B.** Add instructions to use code execution for parsing and calculation, expose the calculation method, and validate the computed value against the input rows.
- **C.** Trust the narrative because the calculation is only one part of the response.
- **D.** Remove all quantitative analysis from the workflow.

---

<details>
<summary>Answer key and rationales</summary>

## Question 1 answer: B

The observed symptom is generic communication caused by missing context and output specification.

The targeted repair adds:

- the audience;
- the publication channel;
- the feature's decision-relevant benefit; and
- the required communication shape.

### Why the other answers are weaker

- **A:** Creativity does not supply the missing facts or audience.
- **C:** A stronger model still has to infer the same missing information.
- **D:** Repeated sampling may produce variation, but not reliable relevance.

### Component diagnosis

```text
Generic output
      ↓
Missing context and output contract
      ↓
Add audience, purpose, benefit, channel, and shape
```

## Question 2 answer: C

The work contains dependent stages with different success criteria.

A reliable workflow is:

```text
Requirements
      ↓
Approved criteria and weights
      ↓
Consistent provider scoring
      ↓
Trade-off analysis
      ↓
Recommendation
```

Each intermediate output can be inspected before downstream work continues.

### Why the other answers are weaker

- **A:** A single pass hides criteria formation and weakens auditability.
- **B:** Recommending first encourages post-hoc justification.
- **D:** Isolated evaluations may use inconsistent assumptions and standards.

### Workflow diagnosis

```text
Several dependent reasoning tasks
      ↓
Sequential decomposition
      ↓
Validate each intermediate result
```

## Question 3 answer: B

Most of the output already passes. The failed dimensions are length and tone.

The strongest revision preserves:

- approved facts;
- correct structure;
- audience purpose; and
- any sections that already meet the requirement.

It changes only the responsible constraints and then tests for improvement and regression.

### Why the other answers are weaker

- **A:** Rewriting everything discards working components and obscures causality.
- **C:** Model switching does not repair the missing or ineffective boundaries.
- **D:** Manual editing may solve the one document but leaves the reusable prompt defective.

### Iteration diagnosis

```text
Accurate content + wrong length and tone
      ↓
Constraint failure
      ↓
Targeted revision
      ↓
Compare and stop when usable
```

## Question 4 answer: C

Brainstorming requires protected divergence before convergence.

The first stage should establish:

- the goal;
- hard safety, legal, or prohibited boundaries;
- requested volume; and
- dimensions of variation.

Detailed filtering, scoring, and selection belong in a later stage.

### Why the other answers are weaker

- **A:** Final-stage criteria applied too early suppress useful range.
- **B:** A single answer eliminates the desired exploration.
- **D:** One prescribed direction creates premature convergence.

### Strategy diagnosis

```text
Need range
      ↓
Loosen creative direction
      ↓
Retain only hard guardrails
      ↓
Generate broadly
      ↓
Filter later
```

## Question 5 answer: B

A suspect calculation is a deterministic verification problem.

The model can explain the trend, but the calculation should be executed and checked through code.

A sound workflow should define:

- the input rows and fields;
- treatment of missing or malformed values;
- the exact median definition;
- the code-based calculation;
- an inspectable result; and
- an independent validation check.

### Why the other answers are weaker

- **A:** Repeated probabilistic answers do not become a verified computation.
- **C:** A plausible narrative does not validate the number.
- **D:** The calculation is useful and should be repaired, not removed.

### Execution-layer diagnosis

```text
Narrative synthesis → model
Exact calculation   → code
Result validation   → deterministic check
Final interpretation → model and human review as appropriate
```

</details>

---

## Scoring and remediation

| Score | Interpretation | Next action |
|---:|---|---|
| 5/5 | Mastery | Continue to Module 2 takeaways |
| 4/5 | Strong readiness | Review the missed concept and retry one equivalent scenario |
| 3/5 | Partial readiness | Revisit the relevant lesson and complete a targeted drill |
| 0–2/5 | Foundation gap | Review the component stack, decomposition, iteration, strategy, and tool-routing lessons before retrying |

Do not remediate by memorizing option letters. Explain:

1. the observed symptom;
2. the dominant defect;
3. why the correct intervention addresses it; and
4. why the nearest distractor does not.

## Coverage map

| Question | Primary capability | Supporting concepts |
|---:|---|---|
| 1 | Component specification | Context, audience, output contract, model-selection restraint |
| 2 | Decomposition | Shared criteria, intermediate validation, auditability |
| 3 | Diagnostic iteration | One-change rule, preservation, regression testing, convergence |
| 4 | Task-strategy calibration | Brainstorming, latitude, divergence before convergence |
| 5 | Verified computation | Tool routing, code execution, deterministic validation |

## Full-module reasoning pattern

```text
Define the real objective
      ↓
Select the task strategy
      ↓
Specify the required components
      ↓
Decompose dependent work
      ↓
Route exact operations to tools
      ↓
Evaluate the candidate output
      ↓
Diagnose and revise the smallest failed component
      ↓
Stop when the result is usable and validated
```

## Exam traps to reject

### “Use a better model”

Model selection matters, but it is not the first repair for an ambiguous task, missing context, absent criteria, or an undefined output contract.

### “Ask it to try harder”

Effort language does not create evidence, boundaries, or acceptance criteria.

### “Run it several times”

Repeated sampling can provide alternatives, but it does not repair systematic under-specification.

### “Recommend first, explain later”

This reverses the evidence-to-decision sequence and encourages rationalization.

### “Rewrite everything”

Wholesale revision discards working components and makes improvement harder to attribute.

### “Trust the calculation”

Fluent language is not proof of deterministic correctness.

## Knowledge check

### Question 1

Why is a more capable model not the default repair for a generic output?

**Answer:** Because missing context, task definition, constraints, or output requirements remain missing regardless of model capability.

### Question 2

Why should criteria be established before supplier scoring?

**Answer:** Shared criteria make scoring consistent, inspectable, and traceable to the requirements.

### Question 3

What should remain unchanged during a targeted iteration?

**Answer:** Components and content that already meet the acceptance criteria.

### Question 4

What is the first-phase objective of brainstorming?

**Answer:** Generate useful range within hard guardrails, without premature ranking or filtering.

### Question 5

Why is calculating a median through code stronger than asking for repeated prose calculations?

**Answer:** Code produces an inspectable deterministic operation rather than another probabilistic estimate.

## Flashcards

### Flashcard 1

**Q:** What usually causes polished but generic output?

**A:** Missing task-relevant context, audience, purpose, or output requirements.

### Flashcard 2

**Q:** What is the correct sequence for a complex evaluation?

**A:** Derive criteria, validate them, score consistently, analyze trade-offs, then recommend.

### Flashcard 3

**Q:** What is the one-change rule?

**A:** Revise the smallest responsible component while preserving what already works.

### Flashcard 4

**Q:** How should a first-round brainstorming prompt be calibrated?

**A:** Tight goal and hard guardrails, broad latitude in quantity and direction, with filtering deferred.

### Flashcard 5

**Q:** Where should exact arithmetic occur?

**A:** In code or another deterministic execution layer with validation.

## Certification lens

For short scenario questions, prefer the answer that:

- addresses the observed symptom directly;
- changes the smallest responsible part of the design;
- preserves validated work;
- respects the task type;
- introduces intermediate validation when work is dependent; and
- routes deterministic operations away from prose generation.

## Think like an AI systems engineer

The five questions cover more than prompt wording.

```text
Specification
      +
Workflow architecture
      +
Execution-layer selection
      +
Evaluation
      +
Controlled iteration
```

That combination is the foundation of reliable AI task execution.

## Related material

- [Component Stack](02a-component-stack.md)
- [Task Decomposition](03a-decomposition.md)
- [Iterating to Improve Output](04-iterating-to-improve-output.md)
- [Strategy by Task Type](05a-strategy-by-task-type.md)
- [Repair the Prompt](06-repair-the-prompt.md)
- [Extended Module 2 quiz](../quiz.md)
- [Quiz and remediation prompt notebook](../../../prompts/module-02/07a-module-2-quiz-prompts.md)
