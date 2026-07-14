# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding state, ignoring model behavior, using stale evidence, or failing to manage context. This domain establishes the platform mental model used by every later module.

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
- [ ] 04. Capability Layer
  - [ ] Skills and Code Execution
  - [ ] Memory
  - [ ] Scenario
  - [ ] Checkpoint
- [ ] 05. Choosing Models
- [ ] 06. Context Management
- [ ] 07. Exercise
- [ ] 08. Quiz
- [ ] 09. Key Takeaways
- [ ] 10. Module Complete

## Learning objectives

By the end of this module, you should be able to:

- select the appropriate Claude entry point and feature set for a professional task;
- explain why generative outputs vary and why fluency is not evidence of accuracy;
- differentiate Haiku, Sonnet, and Opus by capability characteristics and task fit;
- match model selection to quality, speed, cost, and volume requirements;
- manage context limitations and continuity features across sessions;
- distinguish context capacity, output limits, knowledge freshness, and application-managed state;
- explain the roles of trusted configuration, user task content, tools, and retrieved knowledge;
- interpret response metadata such as stop reasons and usage;
- plan model and prompt migrations using regression tests; and
- define the minimum observability needed for production use.

## Current lesson resources

### Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [How Claude Behaves](lessons/02-how-claude-behaves.md)
- [Core Entry Points](lessons/03-core-entry-points.md)
- [Core Entry Points worked example](lessons/03a-core-entry-points-worked-example.md)

### Module 1 prompt notebooks

- [Workflow foundation prompts](../../prompts/module-01/01-workflow-foundation-prompts.md)
- [How Claude Behaves prompts](../../prompts/module-01/02-how-claude-behaves-prompts.md)
- [Core Entry Points prompts](../../prompts/module-01/03-core-entry-points-prompts.md)
- [Core Entry Points worked-example prompts](../../prompts/module-01/03a-core-entry-points-worked-example-prompts.md)

### Baseline module material

- [notes.md](notes.md): Broader platform engineering concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Twelve baseline recall prompts
- [quiz.md](quiz.md): Eight original scenario questions

## Exam lens

Expect scenarios in which several Claude surfaces, features, or model approaches could technically work. The best answer usually follows from the use case's recurrence, persistence, output, source, quality, latency, cost, and governance requirements, not from selecting the most advanced option by default.

Use this diagnostic checklist throughout the module:

1. How is Claude likely to behave on this task?
2. Am I using the correct entry point?
3. Am I activating only the capabilities the task actually needs?
4. Does the model fit the quality, speed, cost, and volume requirements?
5. Is context being managed deliberately?
6. What validation and human review does the consequence require?

For repeated work, also ask:

1. Does the task recur?
2. Is the background context substantially stable?
3. Is the output format consistent?

If two or more are true, a Project is usually worth considering.

## Completion criteria

- [ ] I can explain why repeated runs can differ without assuming that one is automatically wrong.
- [ ] I can separate confident language from factual evidence.
- [ ] I can choose among Chat, Projects, Artifacts, and Research for a scenario.
- [ ] I can explain why Project conversations share configuration but not complete thread context.
- [ ] I can identify a recurring setup tax and estimate a Project's break-even point.
- [ ] I can separate durable Project instructions, reusable knowledge, and session-specific input.
- [ ] I can explain application state without claiming the model "remembers" by itself.
- [ ] I can separate context, output, and knowledge freshness.
- [ ] I can justify a model selection with measurable criteria.
- [ ] I can explain why model updates require regression testing.
- [ ] I completed the lab and scored at least 80% on the quiz.

## Public-repository scenario policy

Examples in this repository are fictional, generic, or based on public information. Do not contribute client names, nonpublic agency details, proprietary work products, confidential data, or facts that could identify a real engagement.

## Official reading

Product capabilities and plan availability can change. Use official sources as the current authority.

- [Claude Help Center](https://support.claude.com/en/)
- [Intro to Claude](https://platform.claude.com/docs/en/intro)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)
- [Artifacts are now generally available](https://www.anthropic.com/news/artifacts)
- [Claude takes research to new places](https://www.anthropic.com/news/research)
- [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
- [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
