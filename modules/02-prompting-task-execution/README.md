# Module 2: Prompting & Task Execution

## Why this domain matters

Prompt quality begins with task definition. Clear instructions, examples, data boundaries, uncertainty behavior, and output contracts reduce ambiguity and make results easier to evaluate and integrate.

## Learning objectives

By the end of this module, you should be able to:

- define success criteria before iterating on wording;
- convert a vague request into a testable task contract;
- use direct instructions, examples, delimiters, roles, and output schemas appropriately;
- distinguish instructions from untrusted content;
- decompose multi-stage tasks;
- design safer tool descriptions and parameter schemas;
- specify missing-data and uncertainty behavior; and
- recognize when a failure belongs to evaluation, data, model selection, or workflow design instead of prompt engineering.

## Files

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

Look for the smallest prompt or task-design improvement that directly addresses the observed ambiguity. “Add more detail” is not enough. The best answer names the missing contract element, example, boundary, schema, or validation behavior.

## Completion criteria

- [ ] I can write a task contract with objective, evidence, constraints, output, and success criteria.
- [ ] I can explain when examples are more useful than additional prose.
- [ ] I can separate untrusted data from authoritative instructions.
- [ ] I can specify safe tool-use behavior.
- [ ] I completed the prompt clinic and scored at least 80% on the quiz.

## Official reading

- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
