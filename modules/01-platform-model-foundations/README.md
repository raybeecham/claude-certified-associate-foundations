# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding state, ignoring version changes, or failing to observe how a request ended. This domain establishes the platform mental model used by every later module.

## Course-aligned lesson map

We are building this module section by section from the certification preparation course. Each completed lesson expands the course concepts with original explanations, practical examples, prompts, knowledge checks, and engineering perspectives.

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [ ] 02. How Claude Behaves
- [ ] 03. Core Entry Points
  - [ ] Entry Points
  - [ ] Worked Example
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
- differentiate Haiku, Sonnet, and Opus by capability characteristics and task fit;
- match model selection to quality, speed, cost, and volume requirements;
- manage context limitations and continuity features across sessions;
- distinguish context capacity, output limits, knowledge freshness, and application-managed state;
- explain the roles of trusted configuration, user task content, tools, and retrieved knowledge;
- interpret response metadata such as stop reasons and usage;
- plan model and prompt migrations using regression tests; and
- define the minimum observability needed for production use.

## Files

- [lessons/](lessons/): Course-aligned lessons built section by section
- [notes.md](notes.md): Broader platform engineering concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Twelve baseline recall prompts
- [quiz.md](quiz.md): Eight original scenario questions
- [Module 1 prompt library](../../prompts/module-01/01-workflow-foundation-prompts.md): Reusable prompts introduced in the lessons

## Exam lens

Expect scenarios in which several Claude surfaces or model approaches could work. The best answer usually follows from the use case's control, integration, quality, latency, cost, and governance requirements, not from selecting the most powerful option by default.

Use this four-question checklist throughout the module:

1. Am I using the correct entry point?
2. Am I activating the capabilities the task actually needs?
3. Does the model fit the quality, speed, cost, and volume requirements?
4. Is context being managed deliberately?

## Completion criteria

- [ ] I can explain application state without claiming the model “remembers” by itself.
- [ ] I can separate context, output, and knowledge freshness.
- [ ] I can justify a model selection with measurable criteria.
- [ ] I can explain why model updates require regression testing.
- [ ] I completed the lab and scored at least 80% on the quiz.

## Official reading

- [Intro to Claude](https://platform.claude.com/docs/en/intro)
- [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
