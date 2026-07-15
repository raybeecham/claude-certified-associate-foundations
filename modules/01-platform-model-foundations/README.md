# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding model behavior, mixing capability responsibilities, choosing an unsuitable model, or allowing context to become bloated and unreliable.

Four decisions set the quality ceiling for a Claude workflow:

1. entry point;
2. capability layer;
3. model selection; and
4. context management.

This module builds the framework for making those decisions together.

## Course-aligned lesson map

Each completed lesson expands the preparation-course concepts with original explanations, generic professional examples, reusable prompts, labs, knowledge checks, flashcards, and engineering patterns.

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
- [x] [07. Platform Selection Exercise](lessons/07-platform-selection-exercise.md)
- [x] [08. Module 1 Quiz Review](lessons/08-module-1-quiz.md)
- [ ] 09. Key Takeaways
- [ ] 10. Module Complete

## Learning objectives

By the end of this module, you should be able to:

- explain why generative responses vary and why fluent confidence is not evidence of accuracy;
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
- redesign recurring workflows while preserving human accountability;
- differentiate Haiku, Sonnet, and Opus by task fit;
- select the minimum model that passes representative evaluations;
- design model escalation and routing patterns;
- distinguish context-length limits from usage limits;
- recognize context degradation;
- choose among restart, summarize, and persist;
- create and validate a state-capsule handoff;
- combine entry-point, capability, model, and context decisions for one scenario;
- defend a configuration using an explicit benefit-versus-cost trade-off; and
- explain why each quiz distractor is weaker than the best answer.

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
- [Platform Selection Exercise](lessons/07-platform-selection-exercise.md)
- [Module 1 Quiz Review](lessons/08-module-1-quiz.md)

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
- [Platform Selection Exercise prompts](../../prompts/module-01/07-platform-selection-exercise-prompts.md)
- [Quiz and remediation prompts](../../prompts/module-01/08-module-1-quiz-prompts.md)

### Engineering patterns

- [Capability patterns](../../patterns/capability-patterns.md): Project context, Skill procedures, Code Execution, Memory, least privilege, and computational validation
- [Memory patterns](../../patterns/memory-patterns.md): Curation, scope separation, Incognito, import review, memory-poisoning defense, and remediation
- [Model-selection patterns](../../patterns/model-selection-patterns.md): Tier selection, minimum-qualified-model evaluation, routing, migration, and version control
- [Context-management patterns](../../patterns/context-management-patterns.md): Context budgeting, clean restarts, state capsules, persistence, usage planning, and secure handoffs

### Baseline module material

- [notes.md](notes.md): Broader platform engineering concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Eight additional original engineering-oriented scenario questions

## Capability Layer summary

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

> Standing instructions define how Claude behaves. Knowledge defines what Claude knows or analyzes.

## Choosing Models summary

| Task profile | Certification starting tier |
|---|---|
| Structured, routine, high-volume work | Haiku |
| Most professional drafting, synthesis, and analysis | Sonnet |
| Complex, ambiguous, nuanced, or quality-sensitive work | Opus |

Production rule:

> Use the fastest and least costly model that passes the validated quality threshold.

A stronger model does not replace authoritative sources, Code Execution, schema validation, privacy controls, or human review.

## Context Management summary

Context is a finite working budget. When a session loses coherence:

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

> Reconstruct the smallest authoritative context required for the next action.

```text
Context limit = depth of one conversation
Usage limit   = quantity of Claude use over time
```

## Integrated platform-selection summary

For every scenario, decide in this order:

1. **Entry point:** Chat, Project, Artifact, Research, or a combination.
2. **Capability layer:** Project, Skill, Code Execution, Memory, or none.
3. **Model tier:** Haiku, Sonnet, or Opus based on structure, ambiguity, volume, and consequence.
4. **Context strategy:** current thread, Project instructions, Project knowledge, Memory, state capsule, or authoritative record.
5. **Controls:** deterministic validation, source checks, escalation, and human review.

Exercise mapping:

```text
Recent competitor research       -> Research, Sonnet
Recurring fixed-format notes     -> Project + Skill, Sonnet
Ambiguous board analysis         -> Project knowledge + Artifact, Opus
Survey response-rate calculation -> Code Execution, Haiku or Sonnet
Monthly variance analysis        -> Project + Skill + Code Execution, Sonnet
One-off vendor response          -> Chat + Artifact, Sonnet
```

The strongest model justification names the task signal, the benefit gained, and the cost accepted.

## Quiz completion summary

The learner scored **5/5** on the preparation-course Module 1 quiz.

The questions confirmed correct reasoning across:

- recurring Project workflows;
- stable knowledge and standing instructions;
- Code Execution for trustworthy calculations;
- Haiku for clear high-volume classification;
- context recovery through summarize and restart; and
- Project-scoped separation of unrelated workstreams.

The repository adds a separate ten-question original drill. Target at least **80 percent**, then explain every distractor before considering the objective complete.

## Exam lens

Expect scenarios where several configurations could technically work. Select the answer that best matches:

- recurrence;
- persistence;
- current-information requirements;
- reusable procedure;
- computation;
- deliverable format;
- ambiguity;
- consequence;
- quality;
- latency;
- cost or usage;
- context health; and
- governance.

Use this diagnostic checklist:

1. Is the work one-off, recurring, deliverable-oriented, or research-intensive?
2. What should persist as instructions or knowledge?
3. What applies only to the current cycle?
4. What procedure repeats?
5. What must be executed rather than generated?
6. What continuity belongs in Memory?
7. What remains controlled by an authoritative system?
8. What model is the minimum qualified tier?
9. What context should remain active, transfer, or be persisted?
10. Which decisions require accountable human review?

## Completion criteria

- [ ] I can explain why repeated outputs may differ.
- [ ] I can separate confident language from evidence.
- [ ] I can choose among Chat, Projects, Artifacts, and Research.
- [ ] I can identify a recurring setup tax.
- [ ] I can distinguish instructions, knowledge, current input, Skills, Code Execution, Memory, and formal records.
- [ ] I can perform a basic Skill trust review.
- [ ] I can explain why executed code still requires method validation.
- [ ] I can curate Memory and defend against memory poisoning.
- [ ] I can map a recurring workflow across capability layers.
- [ ] I can distinguish Haiku, Sonnet, and Opus by task fit.
- [ ] I can design a minimum-qualified-model evaluation.
- [ ] I can distinguish context-length limits from usage limits.
- [ ] I can choose among restart, summarize, and persist.
- [ ] I can create and validate a state capsule.
- [ ] I matched all six Platform Selection scenarios and explained the signals.
- [x] I scored 5/5 on the preparation-course Module 1 quiz.
- [ ] I scored at least 80 percent on the repository's ten-question Module 1 quiz.
- [ ] I can explain why every quiz distractor is weaker than the correct answer.

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

## Version-awareness note

Model names, versions, defaults, pricing, effort settings, context-window sizes, automatic context management, Code Execution dependencies, Project retrieval, Memory, chat search, rolling usage windows, weekly pools, workspace administration, Enterprise billing, and retention can change. Treat current official documentation, product settings, and organization policy as authoritative.
