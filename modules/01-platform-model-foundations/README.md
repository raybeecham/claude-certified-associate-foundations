# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding model behavior, using stale evidence, mixing capability responsibilities, selecting an underpowered or unnecessarily expensive model, or allowing context to become bloated and unreliable.

Four decisions set the quality ceiling for a Claude workflow:

1. entry point;
2. capability layer;
3. model selection; and
4. context management.

Before making those decisions, the learner must understand Claude's probabilistic behavior and the review controls that behavior requires.

## Course-aligned lesson map

We are building this module section by section from the certification preparation course. Each completed lesson expands the course concepts with original explanations, generic professional examples, reusable prompts, labs, knowledge checks, flashcards, and engineering patterns.

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. How Claude Behaves](lessons/02-how-claude-behaves.md)
- [x] 03. Core Entry Points
  - [x] [Entry Points](lessons/03-core-entry-points.md)
  - [x] [Worked Example](lessons/03a-core-entry-points-worked-example.md)
- [x] 04. Capability Layer
  - [x] [Skills and Code Execution](lessons/04-capability-layer-skills-code-execution.md)
  - [x] [Memory](lessons/04a-capability-layer-memory.md)
  - [x] [Scenario](lessons/04b-capability-layer-scenario.md)
  - [x] [Checkpoint](lessons/04c-capability-layer-checkpoint.md)
- [x] [05. Choosing Models](lessons/05-choosing-models.md)
- [x] [06. Context Management](lessons/06-context-management.md)
- [ ] 07. Exercise
- [ ] 08. Quiz
- [ ] 09. Key Takeaways
- [ ] 10. Module Complete

## Learning objectives

By the end of this module, you should be able to:

- explain why generative outputs vary and why fluent confidence is not evidence of accuracy;
- choose among Chat, Projects, Artifacts, and Research;
- identify when recurring work has outgrown an ordinary Chat;
- distinguish Project standing instructions from Project knowledge;
- distinguish reusable Project knowledge from current-cycle source material;
- separate persistent context, reusable procedure, executed computation, and cross-session continuity;
- decide when Projects, Skills, Code Execution, and Memory add value;
- explain why Skills reduce variance without eliminating review;
- perform a basic trust and permission review for a Skill;
- explain why executed code can still produce an invalid result;
- curate Memory for freshness, scope, accuracy, and sensitivity;
- recognize memory-poisoning and persistent-state integrity risks;
- redesign recurring workflows using capability layers while preserving human accountability;
- differentiate Haiku, Sonnet, and Opus by task fit;
- select the minimum model that passes representative evaluations;
- design model escalation and routing patterns;
- distinguish context-length limits from usage limits;
- recognize context degradation;
- choose among restart, summarize, and persist;
- create and validate a state-capsule handoff;
- plan long work across clean session boundaries; and
- reconstruct the smallest authoritative context required for the next action.

## Current lesson resources

### Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [How Claude Behaves](lessons/02-how-claude-behaves.md)
- [Core Entry Points](lessons/03-core-entry-points.md)
- [Core Entry Points worked example](lessons/03a-core-entry-points-worked-example.md)
- [Capability Layer, Skills and Code Execution](lessons/04-capability-layer-skills-code-execution.md)
- [Capability Layer, Memory](lessons/04a-capability-layer-memory.md)
- [Capability Layer scenario](lessons/04b-capability-layer-scenario.md)
- [Capability Layer checkpoint](lessons/04c-capability-layer-checkpoint.md)
- [Choosing Models](lessons/05-choosing-models.md)
- [Context Management](lessons/06-context-management.md)

### Module 1 prompt notebooks

- [Workflow foundation prompts](../../prompts/module-01/01-workflow-foundation-prompts.md)
- [How Claude Behaves prompts](../../prompts/module-01/02-how-claude-behaves-prompts.md)
- [Core Entry Points prompts](../../prompts/module-01/03-core-entry-points-prompts.md)
- [Core Entry Points worked-example prompts](../../prompts/module-01/03a-core-entry-points-worked-example-prompts.md)
- [Capability Layer prompts](../../prompts/module-01/04-capability-layer-skills-code-execution-prompts.md)
- [Memory prompts](../../prompts/module-01/04a-capability-layer-memory-prompts.md)
- [Capability Layer scenario prompts](../../prompts/module-01/04b-capability-layer-scenario-prompts.md)
- [Capability Layer checkpoint prompts](../../prompts/module-01/04c-capability-layer-checkpoint-prompts.md)
- [Choosing Models prompts](../../prompts/module-01/05-choosing-models-prompts.md)
- [Context Management prompts](../../prompts/module-01/06-context-management-prompts.md)

### Engineering patterns

- [Capability patterns](../../patterns/capability-patterns.md): Project context, Skill procedures, Code Execution, Memory, least privilege, and computational validation
- [Memory patterns](../../patterns/memory-patterns.md): Curation, scope separation, Incognito, import review, memory-poisoning defense, and remediation
- [Model-selection patterns](../../patterns/model-selection-patterns.md): Tier selection, minimum-qualified-model evaluation, routing, migration, and version control
- [Context-management patterns](../../patterns/context-management-patterns.md): Context budgeting, clean restarts, state capsules, persistence, usage planning, and secure handoffs

### Baseline module material

- [notes.md](notes.md): Broader platform engineering concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Original scenario questions

## Capability Layer completion summary

| Responsibility | Correct home |
|---|---|
| Stable workstream behavior | Project standing instructions |
| Curated reusable evidence | Project knowledge |
| Current-cycle files or facts | Current conversation or task source input |
| Repeatable ordered procedure | Skill |
| Calculation, transformation, chart, or real file | Code Execution |
| Appropriate cross-session continuity | Memory |
| Authoritative operational state | External source of record |
| Consequential final judgment | Qualified human review |

The highest-value distinction is:

> Standing instructions define how Claude behaves. Knowledge defines what Claude knows or analyzes.

## Choosing Models summary

Use the certification heuristic:

| Task profile | Starting tier |
|---|---|
| Structured, routine, high-volume work | Haiku |
| Most professional drafting, synthesis, and analysis | Sonnet |
| Complex, ambiguous, nuanced, or quality-sensitive work | Opus |

Then apply the production rule:

> Use the fastest and least costly model that passes the validated quality threshold.

A stronger model does not replace authoritative sources, Code Execution, schema validation, privacy controls, or human review.

## Context Management summary

Context is a finite working budget. When a session loses coherence, use:

```text
Restart   = begin a clean conversation
Summarize = transfer validated operational state
Persist   = move durable information into the correct long-lived layer
```

Use this placement model:

| State | Correct location |
|---|---|
| Current task detail | Current conversation |
| Durable workstream rule | Project instructions |
| Reused approved source | Project knowledge |
| General recurring preference | Memory, when appropriate |
| Reusable procedure | Skill |
| Traceable decision | Decision log or formal record |
| Current operational truth | Authoritative external system |

The highest-value context rule is:

> Reconstruct the smallest authoritative context required for the next action.

### Context limit versus usage limit

```text
Context limit = depth of one conversation
Usage limit   = quantity of Claude use over time
```

As of July 14, 2026, Anthropic's Help Center describes automatic summarization for paid Claude chats when Code Execution is enabled, plus rolling five-hour and weekly usage tracking for paid plans. Treat all plan-specific values and product behavior as dated and verify them in the current Help Center and **Settings > Usage**.

## Exam lens

Expect scenario questions where multiple features or models could technically work. Select the answer that best matches recurrence, persistence, procedure, computation, continuity, evidence, ambiguity, quality, latency, cost, volume, context health, and governance requirements.

Use this diagnostic checklist:

1. How is Claude likely to behave on this task?
2. What is the correct entry point?
3. What durable behavior belongs in Project instructions?
4. What reusable evidence belongs in Project knowledge?
5. What source material applies only to the current task?
6. What repeatable procedure belongs in a Skill?
7. What must be calculated or generated with Code Execution?
8. What continuity belongs in Memory?
9. Which facts remain controlled by an authoritative system?
10. Which decisions require accountable human review?
11. Is the task structured, balanced, or highly ambiguous?
12. What is the minimum qualified model?
13. Is the active context focused and authoritative?
14. Has context degradation appeared?
15. Should the workflow continue, checkpoint, summarize, restart, or persist?
16. What usage and session budget remains?

## Completion criteria

- [ ] I can explain why repeated outputs may differ.
- [ ] I can separate confident language from evidence.
- [ ] I can choose among Chat, Projects, Artifacts, and Research.
- [ ] I can identify a recurring setup tax.
- [ ] I can distinguish instructions, knowledge, current inputs, Skills, Code Execution, Memory, and formal records.
- [ ] I can perform a basic Skill trust review.
- [ ] I can explain why executed code still requires method validation.
- [ ] I can curate Memory and defend against memory poisoning.
- [ ] I can map a recurring workflow across capability layers.
- [ ] I can distinguish Haiku, Sonnet, and Opus by task fit.
- [ ] I can design a minimum-qualified-model evaluation.
- [ ] I can explain why a stronger model does not guarantee accuracy.
- [ ] I can distinguish context-length limits from usage limits.
- [ ] I can recognize signs of context degradation.
- [ ] I can choose among restart, summarize, and persist.
- [ ] I can create and validate a state capsule.
- [ ] I can classify information into active context, Project, Memory, Skill, or an authoritative record.
- [ ] I can create a usage-aware multi-session work plan.
- [ ] I completed the module exercise and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples in this repository are fictional, generic, synthetic, or based on public information. Do not contribute client names, nonpublic agency details, proprietary work products, confidential data, credentials, or facts that could identify a real engagement.

## Official reading

Product capabilities, model versions, context sizes, and plan limits change. Use official sources as the current authority.

- [Claude Help Center](https://support.claude.com/en/)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- [Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)

## Version-awareness note

Model names, versions, defaults, pricing, effort settings, context-window sizes, automatic context management, Code Execution dependencies, Project retrieval, Memory, chat search, rolling usage windows, weekly pools, usage credits, workspace administration, Enterprise billing, and retention can change. Treat current official documentation, product settings, and organization policy as authoritative.