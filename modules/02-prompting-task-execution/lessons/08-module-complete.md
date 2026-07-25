# Lesson 8: Module 2 Complete

## Completion status

Module 2 is complete.

```text
3 of 3 preparation-course checkpoints passed
```

The completed checkpoints are:

1. **Strategy checkpoint:** all answers correct;
2. **Repair the Prompt exercise:** all three stages correct; and
3. **Module 2 quiz:** full marks, 5/5.

This completion record confirms coverage of the preparation-course objectives for Prompting and Task Execution.

> Structured prompting improves consistency by turning an implicit request into a clear, testable task specification.

## What you can now do

After completing this module, you can:

- build a prompt from Role, Context, Task, Constraints, and Output Format;
- use a role only when a defined perspective improves the work;
- provide the context and evidence Claude cannot safely infer;
- replace vague instructions with a specific action, object, and decision purpose;
- define boundaries, uncertainty behavior, and output contracts;
- decompose complex work into ordered, checkable stages;
- validate shared foundations before parallel work begins;
- diagnose output deficiencies and repair the smallest responsible component;
- stop iterating when the output is usable and further changes have marginal value;
- tighten or loosen constraints according to the task type;
- preserve creative latitude during brainstorming and apply filters later;
- route exact arithmetic, counting, sorting, and validation to code or another deterministic method; and
- recognize when a failure belongs to evidence, tools, context, model selection, permissions, governance, or workflow design instead of the prompt.

## The complete Module 2 method

```text
Understand the business need
          ↓
Choose the dominant task type
          ↓
Supply context and authorized evidence
          ↓
Build the component stack
          ↓
Decompose dependent work
          ↓
Execute with the correct model and tools
          ↓
Evaluate the result
          ↓
Repair the smallest responsible component
          ↓
Stop, edit, escalate, or continue
```

The prompt is one instruction inside that larger system. It is not the entire workflow.

## The component stack

The course-aligned foundation is:

```text
Role
  + Context
  + Task
  + Constraints
  + Output Format
```

For higher-precision professional work, the repository expands the specification:

```text
Business objective
      ↓
Role or operating frame
      ↓
Context and audience
      ↓
Authorized evidence
      ↓
Task
      ↓
Required process
      ↓
Constraints
      ↓
Output contract
      ↓
Uncertainty behavior
      ↓
Success criteria
```

Every component should carry weight that the output depends on. Decorative wording should not be confused with functional specification.

## The five durable rules

### 1. Structure drives quality, not cleverness

A sophisticated-sounding prompt can still be unusable. Define the work, evidence, boundaries, output, and success conditions.

### 2. Context is commonly omitted

When an output is polished but generic, ask:

```text
What did I know that the model did not?
```

Supply the minimum sufficient context rather than every available detail.

### 3. Decompose complex work

For each stage, define:

```text
Input → Process → Output → Validation
```

Validate high-stakes foundations before downstream or parallel production.

### 4. Iterate diagnostically

```text
Observe → Diagnose → Modify → Validate → Decide
```

Preserve what already works. Change one significant variable at a time when practical.

### 5. Match strategy to task type

| Task type | Tighten | Leave flexible |
|---|---|---|
| Analysis | Criteria, evidence, standards, scope, ambiguity behavior | Phrasing |
| Research | Question, currency, sources, citations, verification | Search path and synthesis approach |
| Drafting | Audience, purpose, facts, tone, length, format | Word choice and sentence construction |
| Brainstorming | Goal, hard guardrails, requested range | Direction, novelty, and combinations |

Use the calibration rule:

> Tighten what determines validity. Loosen what benefits from variation.

## Course completion message and engineering boundary

The preparation-course completion message emphasizes that mastering prompt structure produces more consistent, high-quality results.

For professional systems, that should not be interpreted as a guarantee that Claude will produce exactly the right answer every time. A strong prompt can reduce ambiguity, but it cannot independently guarantee:

- factual correctness;
- complete evidence;
- reliable arithmetic;
- current information;
- consistent behavior across all inputs;
- safe permissions;
- policy compliance;
- appropriate human judgment; or
- release readiness.

That boundary explains why **Output Evaluation** follows Prompting in the Associate path.

```text
Prompting specifies intended behavior
                ↓
Evaluation measures observed behavior
                ↓
Human review determines whether release is acceptable
```

## Associate path position

| Course module | Focus | Status | Repository path |
|---|---|---|---|
| M1 | Product & Model Selection | Complete | [Module 1](../../01-platform-model-foundations/) |
| M2 | Prompting | **Complete — you are here** | [Module 2](../) |
| M3 | Output Evaluation | **Up next** | [Module 3](../../03-evaluating-validating-output/) |
| M4 | Workflow Integration | Later | [Module 4](../../04-workflow-integration-solutions-design/) |
| M5 | Configuration | Later | [Module 5](../../05-configuration-knowledge-management/) |
| M6 | Governance | Later | [Module 6](../../06-governance-risk-responsible-use/) |
| M7 | Troubleshooting | Later | [Module 7](../../07-troubleshooting-optimization/) |
| M8 | Course Summary & Next Steps | Final course synthesis | [Master cheat sheet](../../../docs/master-cheat-sheet.md) and [practice exams](../../../practice-exams/) |

The preparation course describes the next modules as follows:

- **M3 — Output Evaluation:** validate output and identify when human review is non-negotiable;
- **M4 — Workflow Integration:** map workflows against delegation criteria and redesign them safely;
- **M5 — Configuration:** configure and maintain Projects, instructions, and knowledge;
- **M6 — Governance:** apply use-case, data, policy, and ethics judgment responsibly;
- **M7 — Troubleshooting:** diagnose underperformance and optimize workflows; and
- **M8 — Course Summary & Next Steps:** review the path, prepare for the exam, and recognize escalation boundaries.

## Why Module 3 is next

Module 2 answered:

```text
How should the task be specified?
```

Module 3 asks:

```text
How do we know the output is good enough?
```

A well-structured prompt is the beginning of evaluation, because it gives the workflow explicit acceptance criteria. Module 3 extends that work into:

- measurable success criteria;
- representative test sets;
- normal, edge, missing, conflicting, and adversarial cases;
- code-based, human, and model-assisted graders;
- claim-to-source support;
- consistency and regression testing;
- release-blocking failure analysis; and
- mandatory human review for consequential decisions.

Continue with [Module 3: Evaluating & Validating Claude's Output](../../03-evaluating-validating-output/).

## Review module

Use this sequence for a focused review:

1. [Component Stack](02a-component-stack.md)
2. [Worked Build](02b-worked-build.md)
3. [Task Decomposition](03a-decomposition.md)
4. [Parallel Decomposition Case](03b-parallel-case.md)
5. [Iterating to Improve Output](04-iterating-to-improve-output.md)
6. [Strategy by Task Type](05a-strategy-by-task-type.md)
7. [Strategy Checkpoint](05b-strategy-checkpoint.md)
8. [Repair the Prompt](06-repair-the-prompt.md)
9. [Module 2 Quiz](07a-module-2-quiz.md)
10. [Key Takeaways](07b-key-takeaways.md)

For rapid review, use the [Module 2 completion and transition prompts](../../../prompts/module-02/08-module-complete-prompts.md).

## Start over

Restart from the [Module 2 Introduction](01-module-introduction.md) when:

- the component stack cannot be recalled without notes;
- context, constraints, and output format are still being confused;
- decomposition choices feel arbitrary;
- prompt iterations replace working content unnecessarily;
- analysis and brainstorming receive the same constraint strategy;
- deterministic calculations are still being assigned to prose generation; or
- quiz answers are being memorized without understanding why the distractors fail.

## Transfer test

Before moving on, apply the entire module to one new professional scenario.

1. State the business objective.
2. Identify the dominant task type.
3. Define the authorized evidence.
4. Build the minimum sufficient prompt.
5. Decide whether decomposition is required.
6. Identify any deterministic operations.
7. Define the output contract and success criteria.
8. Predict two likely failure modes.
9. State the smallest repair for each failure.
10. Identify what a qualified human must still review.

The transfer test matters more than reproducing the course wording from memory.

## Completion record

- [x] Strategy checkpoint passed with all answers correct.
- [x] Repair the Prompt exercise completed with all stages correct.
- [x] Module 2 quiz completed with full marks, 5/5.
- [x] Five key takeaways reviewed.
- [x] Preparation-course Module 2 completed.
- [ ] Optional repository prompt clinic completed.
- [ ] Optional extended eight-question quiz scored at 80% or better.
- [ ] New-workflow transfer test completed without relying on notes.

## Public-repository note

This page records the learner's supplied completion status and summarizes the course path using original public-safe language. It does not reproduce proprietary exam questions or hidden course assessment content.
