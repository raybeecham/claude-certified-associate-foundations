# Module 2: Prompting & Task Execution

Official Exam Domain 1 · **14% of the exam blueprint**

## Why this domain matters

Prompt quality begins with task definition. Clear instructions, evidence boundaries, constraints, uncertainty behavior, and output contracts reduce ambiguity and make results easier to execute, evaluate, and integrate.

> **Module thesis:** Prompts are not magic. Prompts are specifications.

Module 1 established that an AI task is an engineering design problem before it is a prompting problem. Module 2 focuses on the task specification inside that system.

```text
Business problem
      ↓
Workflow design
      ↓
Task specification
      ↓
Prompt
      ↓
Candidate output
      ↓
Evaluation and revision
```

## Course-aligned lesson map

Each lesson expands the preparation-course concepts with original explanations, generic examples, prompt notebooks, exercises, knowledge checks, flashcards, and reusable engineering patterns.

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] 02. Anatomy of an Effective Prompt
  - [x] [Component Stack](lessons/02a-component-stack.md)
  - [x] [Worked Build](lessons/02b-worked-build.md)
- [x] 03. Task Decomposition
  - [x] [Decomposition](lessons/03a-decomposition.md)
  - [x] [Parallel Case](lessons/03b-parallel-case.md)
- [x] [04. Iterating to Improve Output](lessons/04-iterating-to-improve-output.md)
- [x] 05. Adapting Strategy by Task Type
  - [x] [Strategy](lessons/05a-strategy-by-task-type.md)
  - [x] [Checkpoint](lessons/05b-strategy-checkpoint.md)
- [ ] 06. Exercise: Repair the Prompt
- [ ] 07. Module 2 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 08. Module Complete

## Learning objectives

By the end of this module, you should be able to:

- create effective prompts using a repeatable component structure;
- define success criteria before iterating on wording;
- convert a vague request into a testable task contract;
- apply sequential and parallel decomposition;
- validate shared foundations before downstream work begins;
- iterate diagnostically by repairing the component that failed;
- preserve working content and test for regressions;
- recognize when iteration has converged;
- adapt the control-latitude balance to analysis, research, drafting, and brainstorming;
- decompose hybrid tasks that combine several task modes;
- identify the dominant prompt weakness rather than listing every possible flaw;
- make one targeted repair while preserving working elements;
- distinguish under-specification from over-specification;
- distinguish instructions from untrusted content; and
- recognize when a failure belongs outside prompt engineering.

## Four durable capabilities

### 1. Component-based prompting

```text
Objective
  + context
  + evidence
  + constraints
  + process
  + output contract
  + uncertainty behavior
  + success criteria
```

### 2. Task decomposition

Break overloaded work into inspectable stages.

```text
Input → Process → Output → Validation
```

Use sequential stages when outputs depend on prior results. Use a shared-foundation parallel pattern when several independent outputs consume the same approved evidence.

```text
Shared source
    ↓
Extract
    ↓
Validate
    ↓
Fan out into parallel tasks
    ↓
Fan in for consistency review
```

### 3. Diagnostic iteration

Identify the failed quality dimension and revise the smallest responsible component rather than merely asking for a better answer.

```text
Observe → Diagnose → Modify → Validate → Decide
```

Change one significant variable at a time when practical, preserve validated content, check for regression, and stop when the next iteration costs more than the value it is likely to produce.

### 4. Task-strategy adaptation

The component stack remains stable, but the control-latitude balance changes with the task.

| Task type | Tighten | Loosen |
|---|---|---|
| Analysis | Criteria, standards, evidence, scope, ambiguity handling | Phrasing |
| Research | Question, sources, time boundary, citations, verification | Search path and synthesis approach |
| Drafting | Audience, purpose, facts, tone, length, format | Word choice and sentence construction |
| Brainstorming | Goal, hard guardrails, volume, diversity dimensions | Direction, novelty, and combinations |

Use this rule:

> Tighten what determines validity. Loosen what benefits from variation.

Hybrid tasks should usually be decomposed:

```text
Research → Validate → Analyze → Brainstorm → Evaluate → Draft → Review
```

### Prompt calibration

Prompt quality can fail in both directions.

```text
Under-specified → Minimum sufficient specification → Over-specified
```

- Under-specified prompts force unsafe or unhelpful inference.
- Calibrated prompts protect validity while preserving useful latitude.
- Over-specified prompts suppress variation, create stiffness, or force premature convergence.

For diagnosis:

```text
Predict the failure
      ↓
Identify the dominant weakness
      ↓
Make one targeted repair
      ↓
Preserve working elements
```

## Current lesson resources

### Lessons

- [Module 2 Introduction](lessons/01-module-introduction.md)
- [Component Stack](lessons/02a-component-stack.md)
- [A Worked Build](lessons/02b-worked-build.md)
- [Task Decomposition](lessons/03a-decomposition.md)
- [Parallel Decomposition Case](lessons/03b-parallel-case.md)
- [Iterating to Improve Output](lessons/04-iterating-to-improve-output.md)
- [Strategy by Task Type](lessons/05a-strategy-by-task-type.md)
- [Strategy Checkpoint](lessons/05b-strategy-checkpoint.md)

### Prompt notebooks

- [Module 2 Introduction prompts](../../prompts/module-02/01-module-introduction-prompts.md)
- [Component Stack prompts](../../prompts/module-02/02a-component-stack-prompts.md)
- [Worked Build prompts](../../prompts/module-02/02b-worked-build-prompts.md)
- [Task Decomposition prompts](../../prompts/module-02/03a-decomposition-prompts.md)
- [Parallel Case prompts](../../prompts/module-02/03b-parallel-case-prompts.md)
- [Iteration prompts](../../prompts/module-02/04-iterating-to-improve-output-prompts.md)
- [Task Strategy prompts](../../prompts/module-02/05a-strategy-by-task-type-prompts.md)
- [Strategy Checkpoint prompts](../../prompts/module-02/05b-strategy-checkpoint-prompts.md)

### Engineering patterns

- [Task Specification Before Prompting](../../patterns/task-specification-before-prompting.md)
- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Task Strategy Fit Pattern](../../patterns/task-strategy-fit-pattern.md)
- [Prompt Calibration Pattern](../../patterns/prompt-calibration-pattern.md)

### Existing module files

- [notes.md](notes.md): Domain study notes
- [lab.md](lab.md): Prompt clinic and applied exercise
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Original scenario questions

## Task-strategy exam shortcut

```text
Analysis      → criteria and standards
Research      → scope, sources, currency, citations
Drafting      → audience, tone, purpose, format
Brainstorming → goal, guardrails, volume, range
```

Do not choose the prompt with the most constraints automatically. Choose the prompt that constrains validity while preserving useful variation.

## Checkpoint diagnosis shortcut

```text
Vague improvement verb       → Task
Broad, uncontrolled topic    → Constraints
No reader, purpose, or use   → Context
Useful content, wrong shape  → Output format
Prematurely filtered ideas   → Strategy mismatch or over-constraint
```

A strong checkpoint answer names:

1. the dominant weakness;
2. the likely output symptom;
3. one targeted repair; and
4. what should remain unchanged.

## Exam lens

Look for the smallest prompt or task-design improvement that directly addresses the observed ambiguity. “Add more detail” is rarely sufficient.

Choose sequential decomposition when later work depends on an intermediate result. Choose parallel decomposition only after the shared evidence or interpretation is validated and the branches no longer depend on one another.

For iteration questions, diagnose the symptom before revising. Preserve content that already passes, change the smallest responsible component, compare the new output against explicit criteria, and stop when further prompting offers only marginal value.

For task-strategy questions, identify the dominant task type, then ask where control is necessary and where latitude improves the result. Research also requires a source and currency decision; brainstorming normally requires divergence before convergence.

For checkpoint questions, identify the dominant weakness rather than every possible weakness. Calibration can require adding a missing component or removing a constraint that damages the task.

Also recognize when prompt revision is not the right intervention. Missing evidence, unsuitable models, degraded context, unreliable calculations, absent validation, and unclear authority require changes elsewhere in the system.

## Completion criteria

- [ ] I can explain why a prompt is a task specification rather than a magic phrase.
- [ ] I can apply Role, Context, Task, Constraints, and Output Format.
- [ ] I can define Input, Process, Output, and Validation for every workflow stage.
- [ ] I can distinguish sequential dependencies from parallel work.
- [ ] I can design a shared-foundation fan-out/fan-in workflow.
- [ ] I can prevent one upstream error from propagating into multiple deliverables.
- [ ] I can diagnose which prompt component failed before revising.
- [ ] I can apply the one-change rule and preserve working content.
- [ ] I can test an iteration for both improvement and regression.
- [ ] I can distinguish prompt failures from system failures.
- [ ] I can recognize diminishing returns and stop iterating.
- [ ] I can distinguish analysis, research, drafting, and brainstorming strategy.
- [ ] I can identify what to tighten and what to loosen for each task type.
- [ ] I can separate divergence from convergence during brainstorming.
- [ ] I can specify source, citation, currency, and verification requirements for research.
- [ ] I can decompose a hybrid task into task-appropriate stages.
- [x] I completed the preparation-course strategy checkpoint with all answers correct.
- [ ] I can distinguish under-specified, calibrated, and over-specified prompts.
- [ ] I can identify one dominant weakness and one targeted repair.
- [ ] I completed the prompt clinic and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Official reading

Product behavior and prompting recommendations change. Verify current guidance before relying on implementation-specific details.

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)
- [Claude features and capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)
