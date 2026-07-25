# Lesson 7B: Module 2 Key Takeaways

## Overview

Module 2 moves prompting away from clever wording and toward disciplined task specification.

The durable workflow is:

```text
Understand the work
      ↓
Specify the task
      ↓
Choose the right strategy
      ↓
Execute in inspectable stages
      ↓
Evaluate the output
      ↓
Repair the smallest responsible component
```

> Prompting is not the search for a magic sentence. It is the design of a clear, testable instruction for one stage of an AI-enabled workflow.

The preparation course closes this module with five ideas. This public lesson preserves those objectives using original explanations and engineering extensions.

---

# Takeaway 1: Structure drives quality, not cleverness

A professional prompt is built from functional components.

The course component stack is:

```text
Role
  + Context
  + Task
  + Constraints
  + Output format
```

The repository expands that stack when the task requires more precision:

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

## What this means

A prompt does not improve because it sounds sophisticated. It improves because every instruction resolves a real ambiguity or protects a required result.

Compare:

```text
Act as a world-class strategist and create an outstanding analysis.
```

with:

```text
Using only the supplied requirements and proposals, compare the three options against cost, implementation time, operational risk, and support coverage. Mark a criterion unknown when the evidence is insufficient. Return a four-row scorecard followed by the two most important trade-offs.
```

The second prompt is stronger because it defines the evidence, criteria, ambiguity behavior, and output—not because it uses more impressive language.

## Engineering rule

> Every prompt component should either reduce uncertainty, constrain validity, guide execution, or make the result easier to evaluate.

Decorative instructions that accomplish none of those purposes should be removed.

## Quick check

Before sending an important prompt, ask:

1. What should the model do?
2. What does it need to know?
3. What evidence may it use?
4. What boundaries matter?
5. What should the result look like?
6. What should happen when information is missing?
7. How will I know the output is acceptable?

---

# Takeaway 2: Context is the component people most often omit

The model cannot see facts, expectations, or organizational knowledge that exist only in the user's head.

```text
What the author knows
      ≠
What the model has been told
```

A prompt such as:

```text
Write an update about the project.
```

leaves the model to infer:

- which project;
- the current state;
- the audience;
- the purpose;
- the decision or action needed;
- the relevant risks;
- the tone; and
- the delivery channel.

Generic output is therefore often a **context failure**, not evidence that the model is incapable.

## Context includes

- relevant background;
- audience and expertise;
- communication purpose;
- prior decisions;
- current state;
- authorized source material;
- definitions and terminology;
- organizational constraints; and
- downstream use.

## Context does not mean “include everything”

Excess context can obscure the task, introduce stale assumptions, or consume the working context window.

Use the **minimum sufficient context**:

```text
Enough information to perform the task correctly
-
irrelevant history
-
stale material
-
duplicated instructions
```

## Engineering rule

> Add the information the model cannot safely infer, not every fact available to you.

## Diagnostic signal

When an output is polished but generic, ask first:

```text
What did I know that the model did not?
```

---

# Takeaway 3: Decompose complex work into ordered, checkable stages

Many apparently simple requests contain several different tasks.

```text
Evaluate the options and recommend one.
```

may actually require:

```text
Derive criteria
      ↓
Validate criteria
      ↓
Extract evidence
      ↓
Score options
      ↓
Analyze trade-offs
      ↓
Recommend
```

Each stage should produce an inspectable result that the next stage can consume.

## The stage contract

For every stage, define:

```text
Input
  ↓
Process
  ↓
Output
  ↓
Validation
```

## Sequence high-stakes foundations first

When several deliverables depend on the same interpretation, establish and validate the shared foundation before allowing parallel drafting.

```text
Source material
      ↓
Extract shared facts
      ↓
Validate
      ↓
Fan out into independent deliverables
      ↓
Fan in for consistency review
```

This prevents one misunderstanding from propagating across several outputs.

## Engineering rule

> Validate upstream assumptions before scaling downstream production.

## Decompose when the request

- contains several primary verbs;
- combines research, analysis, ideation, or drafting;
- needs intermediate approval;
- includes consequential calculations;
- creates several deliverables from one evidence set;
- contains tool calls or side effects; or
- would be difficult to debug as one opaque prompt.

Do not decompose merely to make a workflow look sophisticated. A single bounded task with one acceptance test may be better handled in one prompt.

---

# Takeaway 4: Iterate on the component that failed

A disappointing output is diagnostic evidence.

```text
Output symptom
      ↓
Likely component defect
      ↓
Targeted change
      ↓
Comparison
```

## Common mappings

| Output symptom | Likely defect | Targeted repair |
|---|---|---|
| Generic or off-base | Thin context | Add the missing background, audience, purpose, or evidence |
| Answers the wrong question | Ambiguous task | Sharpen the primary verb and object |
| Wrong length or tone | Missing constraint | Add or repair the length, tone, or style boundary |
| Useful content, unusable shape | Weak output contract | Define sections, fields, schema, or ordering |
| Unsupported claims | Weak evidence boundary | Name authorized sources and missing-evidence behavior |
| Shallow multi-part response | Missing decomposition | Separate dependent stages |
| Incorrect arithmetic | Wrong execution layer | Use code or another deterministic method |
| Repeated stale assumptions | Context degradation | Summarize, restart, or rebuild clean state |

## The one-change rule

When practical, change one significant variable at a time.

```text
Observe
  ↓
Diagnose
  ↓
Modify
  ↓
Validate
  ↓
Decide
```

This preserves working content and makes the cause of improvement easier to understand.

## Know when to stop

Iteration has converged when:

- the output meets acceptance criteria;
- remaining changes are cosmetic;
- another prompt round is unlikely to outperform a quick manual edit;
- improvement has become marginal; or
- the failure belongs to evidence, tools, permissions, model selection, or workflow design rather than wording.

## Engineering rule

> Do not optimize blindly. Localize the failure, make the smallest effective change, and stop when the next iteration costs more than it is likely to return.

---

# Takeaway 5: Match strategy to task type

The component stack remains useful across tasks, but the balance between control and latitude changes.

| Task type | Tighten | Leave flexible |
|---|---|---|
| Analysis | Criteria, standards, evidence, scope, ambiguity behavior | Phrasing |
| Research | Question, time boundary, sources, citations, verification | Search path and synthesis approach |
| Drafting | Audience, purpose, facts, tone, length, format | Word choice and sentence construction |
| Brainstorming | Goal, hard guardrails, requested range | Direction, novelty, and combinations |

## Analysis

Analysis needs repeatable judgment.

```text
Criteria + evidence + standard + ambiguity handling
```

Too much latitude produces unsupported opinion.

## Research

Research needs scope and source discipline.

```text
Question + currency boundary + source hierarchy + citations + verification
```

Recent or changing questions require current retrieval rather than training memory alone.

## Drafting

Drafting needs a communication contract.

```text
Audience + purpose + approved facts + tone + format
```

Over-prescribing sentence-level wording can make the result stiff.

## Brainstorming

Brainstorming needs protected divergence.

```text
Generate range
      ↓
Group
      ↓
Evaluate
      ↓
Converge
```

Applying final-selection filters during the first pass suppresses useful variety.

## Engineering rule

> Tighten what determines validity. Loosen what benefits from variation.

---

# The five takeaways as one system

These are not isolated prompt tips. Together they form a workflow discipline.

```text
1. Build from functional components
              ↓
2. Supply the context the model cannot infer
              ↓
3. Decompose dependent work into checkable stages
              ↓
4. Diagnose and repair the failed component
              ↓
5. Calibrate control and latitude to the task type
```

A compact decision sequence is:

```text
What is the task?
      ↓
What context and evidence are required?
      ↓
Does the work need decomposition?
      ↓
Where must the model conform?
      ↓
Where may it explore?
      ↓
How will the output be validated?
      ↓
What is the smallest repair if it fails?
```

---

# Connection to AI Fluency

The AI Fluency Framework's **Description** competency distinguishes three forms of communication with AI systems:

- **Product description:** what the system should produce;
- **Process description:** how it should approach the work; and
- **Performance description:** how it should behave during the interaction.

Module 2 maps naturally to that framing:

| AI Fluency description type | Module 2 equivalent |
|---|---|
| Product | Task, output contract, audience, success criteria |
| Process | Decomposition, required steps, tool rules, validation |
| Performance | Role, tone, constraints, uncertainty behavior |

This reinforces the repository's broader view that prompting is the specification layer inside a larger human-AI workflow.

---

# Certification recall sheet

```text
Generic output?
→ Check context first.

Wrong action?
→ Repair the task verb.

Complex dependent work?
→ Decompose and validate intermediate results.

Mostly correct output?
→ Change only the failed component.

Brainstorming too narrow?
→ Restore latitude and filter later.

Analysis too opinionated?
→ Add criteria and evidence boundaries.

Research may be stale?
→ Require current grounded sources and verification.

Calculation looks wrong?
→ Route it to code or another deterministic tool.
```

---

# Knowledge check

## Question 1

A prompt is long and polished but still produces an unusable result. What should be checked first?

**Answer:** Whether the prompt's functional components actually define the task, context, evidence, boundaries, output, and success criteria. Length and sophistication do not guarantee specification quality.

## Question 2

Why is context a common source of failure?

**Answer:** Authors often assume the model can see facts, expectations, or prior decisions that exist only in their heads.

## Question 3

What makes a decomposed stage useful?

**Answer:** It has a defined input, process, output, and validation method, and its output can be consumed by the next stage.

## Question 4

What is the best response to an output that is accurate but too long?

**Answer:** Preserve the accurate content and revise the length constraint or output contract rather than rewriting the entire prompt.

## Question 5

Why should brainstorming and analysis use different constraint strategies?

**Answer:** Analysis depends on repeatable criteria and evidence, while early brainstorming depends on range and variation before filtering.

---

# Flashcards

## Flashcard 1

**Q:** What drives professional prompt quality?

**A:** Functional structure and task specification, not clever wording.

## Flashcard 2

**Q:** What is the most commonly omitted prompt component?

**A:** Context—the information that exists in the author's head but was never supplied.

## Flashcard 3

**Q:** What should every decomposed stage define?

**A:** Input, process, output, and validation.

## Flashcard 4

**Q:** What is the core iteration rule?

**A:** Diagnose the output, repair the smallest responsible component, compare, and stop at diminishing returns.

## Flashcard 5

**Q:** What is the task-strategy calibration rule?

**A:** Tighten what determines validity and loosen what benefits from variation.

## Flashcard 6

**Q:** What should happen when a result depends on exact arithmetic or counting?

**A:** Use code or another deterministic method and validate the result.

---

# Source and currency note

The five course takeaways were supplied from the June 2026 preparation material. Product-specific statements in this public lesson were rechecked against official sources on **July 25, 2026**.

Official sources:

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [AI Fluency: Description](https://www.anthropic.com/ai-fluency/description)

Product features, model behavior, interfaces, plan availability, and documentation can change. Recheck current official documentation before publishing implementation-specific claims.

---

# Related material

- [Component Stack](02a-component-stack.md)
- [Task Decomposition](03a-decomposition.md)
- [Parallel Decomposition Case](03b-parallel-case.md)
- [Iterating to Improve Output](04-iterating-to-improve-output.md)
- [Strategy by Task Type](05a-strategy-by-task-type.md)
- [Strategy Checkpoint](05b-strategy-checkpoint.md)
- [Repair the Prompt](06-repair-the-prompt.md)
- [Module 2 Quiz](07a-module-2-quiz.md)
- [Key Takeaways prompt notebook](../../../prompts/module-02/07b-key-takeaways-prompts.md)
