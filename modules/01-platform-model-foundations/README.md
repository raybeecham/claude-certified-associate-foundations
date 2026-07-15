# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding model behavior, using stale evidence, mixing capability responsibilities, selecting an underpowered or unnecessarily expensive model, or failing to manage context. This domain establishes the platform mental model used by every later module.

Four decisions set the quality ceiling for a Claude workflow:

1. entry point;
2. capability layer;
3. model selection; and
4. context management.

Before making those decisions, the learner must also understand Claude's probabilistic behavior and the review controls that behavior requires.

## Course-aligned lesson map

We are building this module section by section from the certification preparation course. Each completed lesson expands the course concepts with original explanations, generic professional examples, reusable prompts, labs, knowledge checks, flashcards, and engineering perspectives.

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
- [ ] 06. Context Management
- [ ] 07. Exercise
- [ ] 08. Quiz
- [ ] 09. Key Takeaways
- [ ] 10. Module Complete

## Learning objectives

By the end of this module, you should be able to:

- select the appropriate Claude entry point and feature set for a professional task;
- explain why generative outputs vary and why fluent confidence is not evidence of accuracy;
- choose among Chat, Projects, Artifacts, and Research;
- identify when recurring work has outgrown an ordinary Chat;
- separate persistent context, reusable procedure, executed computation, and cross-session continuity;
- decide when Projects, Skills, Code Execution, and Memory add value;
- distinguish Project standing instructions from Project knowledge;
- distinguish reusable Project knowledge from current-cycle source material;
- explain why Skills reduce variance without eliminating review;
- perform a basic trust and permission review for a Skill;
- explain why successful code execution does not automatically validate inputs or methodology;
- identify strong and weak Memory candidates;
- distinguish Memory from Project configuration and authoritative records;
- curate Memory for freshness, accuracy, scope, and sensitivity;
- explain Project-scoped Memory and Incognito boundaries;
- recognize memory-poisoning and persistent-state integrity risks;
- redesign recurring high-consequence workflows using capability layers;
- preserve verification and human accountability while reducing repeated effort;
- map workflow components to standing instructions, knowledge, Skills, Code Execution, current inputs, and human review;
- differentiate Haiku, Sonnet, and Opus by task fit;
- match model selection to capability, speed, cost, usage, and volume requirements;
- identify the minimum model that passes representative evaluations;
- design model escalation and routing patterns;
- explain why a stronger model does not replace grounding, computation, or review; and
- manage context limitations and continuity across sessions.

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

### Engineering patterns

- [Capability patterns](../../patterns/capability-patterns.md): Project context, Skill procedures, Code Execution, Memory, least privilege, and computational validation
- [Memory patterns](../../patterns/memory-patterns.md): Curation, scope separation, Incognito, import review, memory-poisoning defense, and remediation
- [Model-selection patterns](../../patterns/model-selection-patterns.md): Tier selection, minimum-qualified-model evaluation, routing, migration, and version control

### Baseline module material

- [notes.md](notes.md): Broader platform engineering concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Baseline recall prompts
- [quiz.md](quiz.md): Original scenario questions

## Capability Layer completion summary

Use this placement model:

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

A stronger model does not replace:

- authoritative sources;
- Code Execution for calculations;
- structured-output validation;
- privacy and authorization controls;
- human review; or
- accountable final decisions.

### Current product note

The certification uses the Haiku, Sonnet, and Opus frame. As of July 14, 2026, current Anthropic documentation also lists Claude Fable 5 as a widely released tier above the current Opus tier. Treat that as a dated product note, not an exam memorization target.

## Exam lens

Expect scenarios in which several Claude surfaces, capabilities, or model approaches could technically work. The best answer usually follows from the use case's recurrence, persistence, procedure, computation, continuity, output, evidence, quality, latency, cost, volume, and governance requirements, not from selecting the most advanced option by default.

Use this diagnostic checklist:

1. How is Claude likely to behave on this task?
2. Am I using the correct entry point?
3. What durable behavior belongs in Project standing instructions?
4. What reusable evidence belongs in Project knowledge?
5. What source material applies only to the current cycle?
6. What reusable procedure belongs in a Skill?
7. What calculation, transformation, chart, or file should use Code Execution?
8. What continuity, if any, belongs in Memory?
9. Which facts remain controlled by an authoritative external system?
10. Which decisions remain consequential, uncertain, or accountable to a human reviewer?
11. Is the task structured, balanced, or highly complex and ambiguous?
12. Does the selected model fit the quality, speed, cost, and volume requirements?
13. Has the model passed representative evaluation cases?
14. Is context being managed deliberately?

For model selection, ask:

1. What is the minimum acceptable quality?
2. Which severe failures matter most?
3. What request volume and latency are expected?
4. What cost or usage budget applies?
5. Can routine cases use a lower tier?
6. Which conditions should trigger escalation?
7. What controls remain outside the model?
8. Which exact model version and settings are being used?

## Completion criteria

- [ ] I can explain why repeated runs can differ without assuming one is automatically wrong.
- [ ] I can separate confident language from factual evidence.
- [ ] I can choose among Chat, Projects, Artifacts, and Research.
- [ ] I can identify a recurring setup tax and estimate a Project's value.
- [ ] I can distinguish standing instructions from Project knowledge.
- [ ] I can distinguish Project knowledge from current-cycle source material.
- [ ] I can distinguish Project context from a Skill procedure.
- [ ] I can define invariants and allowed variation for a Skill.
- [ ] I can identify provenance, permission, and data-access questions before enabling a Skill.
- [ ] I can explain when Code Execution should replace language-only calculation.
- [ ] I can explain why executed code can still produce an invalid result.
- [ ] I can distinguish Memory from Project instructions, Project knowledge, chat history, and a source of record.
- [ ] I can perform a Memory-curation review and describe a control against memory poisoning.
- [ ] I can map a recurring workflow to Project, Skill, Code Execution, Memory, current inputs, and human review.
- [ ] I can explain why verification remains after a capability-layer redesign.
- [ ] I can classify every item in the Capability Layer checkpoint and explain the placement.
- [ ] I can distinguish Haiku, Sonnet, and Opus by task fit.
- [ ] I can explain why Sonnet is the normal certification starting point for professional knowledge work.
- [ ] I can identify cases that justify Haiku or Opus.
- [ ] I can define an evaluation for selecting the minimum qualified model.
- [ ] I can design escalation from Haiku to Sonnet or Opus using observable checks.
- [ ] I can explain why a stronger model does not guarantee accuracy.
- [ ] I completed the module lab and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples in this repository are fictional, generic, synthetic, or based on public information. Do not contribute client names, nonpublic agency details, proprietary work products, confidential data, credentials, or facts that could identify a real engagement.

## Official reading

Product capabilities, model versions, and plan availability can change. Use official sources as the current authority.

- [Claude Help Center](https://support.claude.com/en/)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
- [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)

## Version-awareness note

Model names, versions, model-picker defaults, comparative capability, pricing, effort settings, plan availability, automatic switching, Memory behavior, Project scoping, Skill administration, Code Execution availability, workspace administration, and retention can change. Treat current official documentation, the actual product surface, and organization policy as authoritative.