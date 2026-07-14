# Module 1: Claude Platform & Model Foundations

## Why this domain matters

A strong prompt cannot compensate for selecting the wrong product surface, misunderstanding state, ignoring version changes, or failing to observe how a request ended. This domain establishes the platform mental model used by every later module.

## Learning objectives

By the end of this module, you should be able to:

- distinguish interactive Claude use, API integration, managed agent capabilities, and cloud-hosted access at a requirements level;
- choose model characteristics from quality, latency, cost, context, tool, and risk requirements;
- distinguish context capacity, output limits, knowledge freshness, and application-managed state;
- explain the roles of trusted configuration, user task content, tools, and retrieved knowledge;
- interpret response metadata such as stop reasons and usage;
- plan model and prompt migrations using regression tests; and
- define the minimum observability needed for production use.

## Files

- [notes.md](notes.md): Core concepts and decision patterns
- [lab.md](lab.md): Platform and model selection matrix
- [flashcards.md](flashcards.md): Twelve recall prompts
- [quiz.md](quiz.md): Eight original scenario questions

## Exam lens

Expect scenarios in which several Claude surfaces or model approaches could work. The best answer usually follows from the use case's control, integration, quality, latency, cost, and governance requirements, not from selecting the most powerful option by default.

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
