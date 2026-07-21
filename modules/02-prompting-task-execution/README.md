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
- [ ] 04. Iterating to Improve Output
- [ ] 05. Adapting Strategy by Task Type
  - [ ] Strategy
  - [ ] Checkpoint
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
- adapt prompting strategy to analysis, research, drafting, brainstorming, extraction, classification, and planning;
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

### 4. Task-strategy adaptation

Different task types require different evidence, structure, constraints, and evaluation methods.

## Current lesson resources

### Lessons

- [Module 2 Introduction](lessons/01-module-introduction.md)
- [Component Stack](lessons/02a-component-stack.md)
- [A Worked Build](lessons/02b-worked-build.md)
- [Task Decomposition](lessons/03a-decomposition.md)
- [Parallel Decomposition Case](lessons/03b-parallel-case.md)

### Prompt notebooks

- [Module 2 Introduction prompts](../../prompts/module-02/01-module-introduction-prompts.md)
- [Component Stack prompts](../../prompts/module-02/02a-component-stack-prompts.md)
- [Worked Build prompts](../../prompts/module-02/02b-worked-build-prompts.md)
- [Task Decomposition prompts](../../prompts/module-02/03a-decomposition-prompts.md)
- [Parallel Case prompts](../../prompts/module-02/03b-parallel-case-prompts.md)

### Engineering patterns

- [Task Specification Before Prompting](../../patterns/task-specification-before-prompting.md)

### Existing module files

- [notes.md](notes.md): Domain study notes
- [lab.md](lab.md): Prompt clinic and applied exercise
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Original scenario questions

## Exam lens

Look for the smallest prompt or task-design improvement that directly addresses the observed ambiguity. “Add more detail” is rarely sufficient.

Choose sequential decomposition when later work depends on an intermediate result. Choose parallel decomposition only after the shared evidence or interpretation is validated and the branches no longer depend on one another.

Also recognize when prompt revision is not the right intervention. Missing evidence, unsuitable models, degraded context, unreliable calculations, absent validation, and unclear authority require changes elsewhere in the system.

## Completion criteria

- [ ] I can explain why a prompt is a task specification rather than a magic phrase.
- [ ] I can apply Role, Context, Task, Constraints, and Output Format.
- [ ] I can define Input, Process, Output, and Validation for every workflow stage.
- [ ] I can distinguish sequential dependencies from parallel work.
- [ ] I can design a shared-foundation fan-out/fan-in workflow.
- [ ] I can prevent one upstream error from propagating into multiple deliverables.
- [ ] I can diagnose which prompt component failed before revising.
- [ ] I can adapt strategy to the task type.
- [ ] I completed the prompt clinic and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Official reading

Product behavior and prompting recommendations change. Verify current guidance before relying on implementation-specific details.

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
