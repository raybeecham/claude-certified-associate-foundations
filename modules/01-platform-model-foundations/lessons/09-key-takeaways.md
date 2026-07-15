# Lesson 9: Module 1 Key Takeaways

## Overview

Module 1 establishes the operating framework for professional work with Claude. Before writing the prompt, decide:

1. where the work should happen;
2. which capabilities the task requires;
3. which model tier is the best fit;
4. how context will remain coherent; and
5. how the output will be reviewed.

The module can be compressed into five durable principles.

> [!IMPORTANT]
> These principles are more useful than memorizing a temporary model name, plan limit, or interface detail. Product behavior changes. The decision logic should remain stable.

## Takeaway 1: Select the entry point before writing the prompt

The entry point determines where the work lives and how the result will be used.

| Work pattern | Starting entry point | Primary reason |
|---|---|---|
| One-off question, quick draft, or exploration | Chat | Minimal setup |
| Recurring work with stable background | Project | Persistent instructions and curated knowledge |
| Editable deliverable with a document lifecycle | Artifact | Separate work product for revision and handoff |
| Current multi-source investigation | Research | Search, follow-up investigation, and synthesis |

### Decision rule

```text
One-off and conversational?          -> Chat
Recurring with stable context?       -> Project
Recipient will open or edit output?  -> Artifact
Current multi-source investigation?  -> Research
```

These entry points can be combined. A recurring market analysis may live in a Project, use Research for current evidence, and produce an Artifact for the final briefing.

### Common mistake

A useful result does not prove that the workflow used the right entry point. Re-entering the same background every week is a workflow-design problem even when the output is good.

### Exam signal

Look for words such as:

- one-time;
- weekly, monthly, or recurring;
- same background;
- same template;
- editable report;
- current, recent, or last 90 days; and
- multiple external sources.

## Takeaway 2: Separate the four capability problems

The capability layer separates context, procedure, computation, and continuity.

| Capability | Responsibility | Core question |
|---|---|---|
| Project | Persistent workstream context | What should Claude know and honor in this workstream? |
| Skill | Reusable procedure | How should this recurring task be performed? |
| Code Execution | Executed calculation, transformation, chart, or file operation | What should be run rather than generated as prose? |
| Memory | Appropriate cross-session continuity | Which recurring preferences or facts should carry forward? |

### High-value distinctions

```text
Project instructions = durable behavior
Project knowledge    = curated reusable evidence
Current task input   = facts and files for this cycle
Skill                = repeatable ordered procedure
Code Execution       = executed computation or transformation
Memory               = cross-session continuity
External record      = authoritative operational truth
Human review         = accountable final judgment
```

### Standing instructions versus knowledge

Standing instructions tell Claude **how to behave**. Knowledge tells Claude **what to know or analyze**.

Example:

- “Flag clauses that depart from the approved position” is a standing instruction.
- The approved contract playbook is Project knowledge.
- The current contract is cycle-specific source material.
- The clause-review sequence is a Skill.
- A variable-rate exposure calculation belongs in Code Execution.

### Skills and review

A Skill can stabilize procedure, structure, and terminology. It cannot guarantee identical wording, factual accuracy, or complete issue detection. Review remains part of the workflow.

### Code Execution and verification

Executed code proves that a method ran. It does not prove that the inputs, assumptions, formula, units, or interpretation were correct.

```text
Correct inputs
      +
Correct method
      +
Successful execution
      +
Validated output
      =
Usable result
```

### Memory and authority

Memory provides continuity, not proof. Consequential facts must still be checked against the current source of truth.

## Takeaway 3: Match the model tier to the task

The certification uses the Haiku, Sonnet, and Opus framework.

| Task profile | Starting tier | Trade-off |
|---|---|---|
| Structured, routine, high-volume work | Haiku | Maximizes speed and efficiency when the task is clear |
| Most professional drafting, synthesis, and analysis | Sonnet | Balances quality, speed, and usage |
| Complex, ambiguous, nuanced, or high-consequence reasoning | Opus | Raises the quality ceiling at higher latency or usage cost |

### Certification shortcut

```text
Haiku  = structured volume
Sonnet = balanced professional default
Opus   = ambiguity and quality-sensitive reasoning
```

### Production rule

> Use the fastest and least costly model that passes the validated quality threshold.

A model decision should be tested on representative cases. Measure factual accuracy, edge-case performance, severe failure rate, structured-output validity, tool reliability, latency, usage, cost, and human revision burden.

### Routing pattern

```text
Routine case -> Haiku
      |
      +-- passes checks -> accept
      |
      +-- ambiguous or failed -> Sonnet
                                  |
                                  +-- complex or high-risk -> Opus
                                                            |
                                                            -> human review
```

Use observable signals for escalation, such as missing fields, schema failure, conflicting evidence, failed validators, or a high-risk category. Do not rely only on a model's self-reported confidence.

### What a stronger model cannot fix

A higher tier does not replace:

- current authoritative evidence;
- Code Execution for calculations;
- access and privacy controls;
- Project knowledge maintenance;
- schema validation;
- context hygiene; or
- qualified human review.

## Takeaway 4: Treat context as a budget

Every conversation has a finite working context. Messages, files, tools, retrieved sources, instructions, and generated output all consume that budget.

The practical objective is not to fill the window. It is to maintain the smallest relevant and authoritative context needed for the next action.

### Signs of context degradation

Intervene when Claude:

- loses an early constraint;
- contradicts an accepted decision;
- focuses only on the most recent exchange;
- reopens resolved questions;
- uses a stale source version;
- forgets owners or open actions; or
- requires repeated correction of the same requirement.

Similar symptoms can also come from a bad prompt, stale knowledge, a tool failure, or an underpowered model. Diagnose before acting.

### The three responses

```text
Restart   = begin a clean conversation
Summarize = transfer validated operational state
Persist   = move durable information into the correct long-lived layer
```

A reliable transition often follows this sequence:

1. Create a state-capsule summary.
2. Validate it against the conversation and source material.
3. Persist only the durable items.
4. Start a clean conversation with the approved handoff.

### State-capsule contents

A useful handoff includes:

- objective and scope;
- accepted decisions;
- authoritative sources and versions;
- requirements and constraints;
- definitions;
- completed work;
- work in progress;
- open questions;
- risks and assumptions;
- rejected approaches;
- next actions; and
- required approvals.

### Context limit versus usage limit

```text
Context limit = depth of one conversation
Usage limit   = quantity of Claude use over time
```

Hitting a usage threshold does not prove that any conversation has degraded. Hitting a context or length limit does not necessarily mean the broader usage allowance is exhausted.

## Takeaway 5: Variation is inherent, so review is structural

Claude generates outputs probabilistically. The same prompt can produce different wording, organization, or examples on different runs.

Configuration can reduce variation by controlling:

- required sections;
- procedure order;
- source restrictions;
- terminology;
- missing-data behavior;
- output schema; and
- review steps.

It cannot eliminate variation in prose or guarantee correctness.

### Review model

```text
Task and approved context
          |
          v
Claude candidate output
          |
          v
Deterministic validation
          |
          v
Evidence and source review
          |
          v
Qualified human review when required
          |
          v
Accept, revise, escalate, or reject
```

### Why this matters for later modules

Module 1 teaches how to configure the workflow. Module 3 will teach how to evaluate and validate the output. The two frameworks are complementary:

```text
Module 1 = choose the environment and operating design
Module 3 = determine whether the result is fit for use
```

## Integrated decision framework

Use this sequence for any professional scenario.

### Step 1: Identify the work pattern

- Is the task one-off or recurring?
- Does it require a deliverable?
- Does it require current external evidence?

### Step 2: Separate responsibilities

- What context persists?
- What procedure repeats?
- What must be computed?
- What continuity is useful?
- What remains authoritative outside Claude?

### Step 3: Select the model

- How structured or ambiguous is the task?
- What is the consequence of failure?
- What volume, latency, and usage constraints apply?
- What is the minimum quality threshold?

### Step 4: Plan context

- What belongs in the current conversation?
- What belongs in Project instructions or knowledge?
- What should be summarized, persisted, or discarded?
- When should the work restart in a clean thread?

### Step 5: Preserve controls

- What requires deterministic validation?
- What evidence must be verified?
- What conditions trigger escalation?
- Who owns the final decision?

## One-page exam matrix

| Scenario signal | Best starting response |
|---|---|
| Quick one-off request | Chat |
| Recurring stable workstream | Project |
| Editable work product | Artifact |
| Recent multi-source investigation | Research |
| Repeated task procedure | Skill |
| Real calculation, data transformation, chart, or file | Code Execution |
| Appropriate cross-session preference | Memory |
| Structured high-volume work | Haiku |
| Most professional knowledge work | Sonnet |
| Ambiguous high-stakes synthesis | Opus |
| Long thread loses early state | Summarize, persist, restart |
| Separate confidential workstreams | Separate Projects and scoped continuity |
| Current operational fact | Authoritative external system |
| Consequential judgment | Qualified human review |

## Anti-patterns

### Prompt-first design

Writing the prompt before deciding where the work should live creates repeated setup and poor persistence.

### Maximum capability by default

Adding every feature and choosing the strongest model increases cost, context, permissions, and failure modes without proving better results.

### Project as dumping ground

Uploading every available file increases staleness, conflict, and retrieval noise.

### Skill as guarantee

A repeatable procedure is not proof of accuracy.

### Calculator by prose

Consequential numeric results should be executed and validated.

### Memory as source of truth

Remembered context is not an authoritative, versioned record.

### Endless conversation

Continuing a degraded thread is usually less reliable than validating state and restarting cleanly.

### Fluent output as evidence

Professional tone does not prove factual accuracy.

## Ten flashcards

### 1

**Q:** What should be selected before writing the prompt?

**A:** The entry point.

### 2

**Q:** When has a workflow probably outgrown Chat?

**A:** When the task recurs and the same background, sources, or output format must be reconstructed.

### 3

**Q:** What is the difference between Project instructions and Project knowledge?

**A:** Instructions define durable behavior. Knowledge supplies reusable evidence.

### 4

**Q:** What does a Skill define?

**A:** A repeatable procedure for a task type.

### 5

**Q:** When should Code Execution be used?

**A:** When a calculation, transformation, chart, or real file must be executed accurately and reproducibly.

### 6

**Q:** What is Memory for?

**A:** Appropriate cross-session continuity, not authoritative knowledge management.

### 7

**Q:** What is the normal certification starting tier for professional work?

**A:** Sonnet.

### 8

**Q:** What is the model-selection production rule?

**A:** Choose the fastest and least costly model that passes the validated quality threshold.

### 9

**Q:** What are the three context interventions?

**A:** Restart, summarize, and persist.

### 10

**Q:** Why does review remain necessary after adding Skills and configuration?

**A:** Because generative variation and factual error are not eliminated by configuration.

## Teach-back test

Explain the following without notes:

1. Why a weekly report may need both a Project and a Skill.
2. Why Code Execution can still produce an invalid business result.
3. Why Haiku may be better than Opus for a high-volume classification task.
4. Why Memory should not contain current operational truth.
5. Why a stronger model does not repair a degraded context window.
6. How to move a long-running task into a new conversation safely.
7. Why an editable report may need an Artifact even when the analysis occurs in a Project.
8. Why a 5/5 quiz result is not enough unless the distractors can be explained.

## Current product verification, dated July 14, 2026

The preparation course is based on a June 2026 product snapshot. Current official documentation should control product-specific claims.

Verified current points include:

- Paid Claude chats can automatically summarize earlier messages near the context limit when Code Execution is enabled.
- Projects use retrieval to load relevant content rather than placing every Project file into active context at once.
- Usage limits and conversation-length limits are separate resources.
- Current model names, context sizes, latency descriptions, pricing, and plan availability have evolved beyond the certification's simplified Haiku, Sonnet, and Opus frame.
- Chat search and Memory behavior depend on account, Project, and product settings.

Do not memorize current token counts, pricing, default models, or plan allowances as permanent certification facts.

## Official sources

- [Claude Help Center](https://support.claude.com/en/)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)

## Related material

- [Module Introduction](01-module-introduction.md)
- [How Claude Behaves](02-how-claude-behaves.md)
- [Core Entry Points](03-core-entry-points.md)
- [Capability Layer](04-capability-layer-skills-code-execution.md)
- [Choosing Models](05-choosing-models.md)
- [Context Management](06-context-management.md)
- [Platform Selection Exercise](07-platform-selection-exercise.md)
- [Module 1 Quiz Review](08-module-1-quiz.md)
- [Key Takeaways review prompts](../../../prompts/module-01/09-key-takeaways-prompts.md)
