# Module 2: Prompting & Task Execution

Official Exam Domain 1 · **14% of the exam blueprint**

## Why this domain matters

Prompt quality begins with task definition. Clear instructions, evidence boundaries, constraints, uncertainty behavior, and output contracts reduce ambiguity and make results easier to execute, evaluate, and integrate.

> **Module thesis:** Prompts are not magic. Prompts are specifications.

Module 1 established that an AI task is an engineering design problem before it is a prompting problem. Module 2 now focuses on the task specification inside that system.

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
- [ ] 02. Anatomy of an Effective Prompt
  - [ ] Component Stack
  - [ ] Worked Build
- [ ] 03. Task Decomposition
  - [ ] Decomposition
  - [ ] Parallel Case
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

- create effective prompts for business and technical tasks using a repeatable component structure;
- define success criteria before iterating on wording;
- convert a vague request into a testable task contract;
- apply task decomposition to complex, multi-part requests;
- iterate diagnostically by repairing the component that failed;
- adapt prompting strategy to analysis, research, drafting, brainstorming, extraction, classification, and planning;
- use examples, delimiters, output schemas, and uncertainty behavior appropriately;
- distinguish instructions from untrusted content; and
- recognize when a failure belongs to evidence, model selection, context, evaluation, governance, or workflow design instead of prompt engineering.

## Four durable capabilities

### 1. Component-based prompting

Build prompts from functional components rather than improvised prose.

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

Break overloaded work into stages, sequence dependencies, run independent work in parallel where appropriate, and integrate the results.

### 3. Diagnostic iteration

Do not merely ask for a better answer. Identify the failed quality dimension and revise the smallest responsible component.

### 4. Task-strategy adaptation

Analysis, research, drafting, brainstorming, extraction, classification, and planning require different evidence, structure, constraints, and evaluation methods.

## Current lesson resources

### Lessons

- [Module 2 Introduction](lessons/01-module-introduction.md)

### Prompt notebooks

- [Module 2 Introduction prompts](../../prompts/module-02/01-module-introduction-prompts.md)

### Engineering patterns

- [Task Specification Before Prompting](../../patterns/task-specification-before-prompting.md)

### Existing module files

- [notes.md](notes.md): Domain study notes
- [lab.md](lab.md): Prompt clinic and applied exercise
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Original scenario questions

## Exam lens

Look for the smallest prompt or task-design improvement that directly addresses the observed ambiguity.

“Add more detail” is rarely sufficient. The best answer names the missing component, such as:

- audience;
- objective;
- evidence boundary;
- constraint;
- decomposition step;
- output contract;
- example;
- uncertainty behavior; or
- evaluation criterion.

Also recognize when prompt revision is not the right intervention. Missing evidence, unsuitable models, degraded context, unreliable calculations, absent validation, and unclear authority require changes elsewhere in the system.

## Completion criteria

- [ ] I can explain why a prompt is a task specification rather than a magic phrase.
- [ ] I can write a task contract with objective, evidence, constraints, output, and success criteria.
- [ ] I can explain when examples are more useful than additional prose.
- [ ] I can separate untrusted data from authoritative instructions.
- [ ] I can decompose sequential and parallel work.
- [ ] I can diagnose which prompt component failed before revising.
- [ ] I can adapt strategy to the task type.
- [ ] I can specify safe tool-use and missing-data behavior.
- [ ] I completed the prompt clinic and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute client names, confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Official reading

Product behavior and prompting recommendations change. Verify current guidance before relying on implementation-specific details.

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)