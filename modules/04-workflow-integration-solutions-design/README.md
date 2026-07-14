# Module 4: Workflow Integration & Solutions Design

## Why this domain matters

Production quality comes from the surrounding system as much as the model. A sound design assigns each responsibility to the component best suited for it and makes side effects, state, retries, approvals, and failures explicit.

## Learning objectives

By the end of this module, you should be able to:

- choose among interactive chat, fixed workflow, API-backed application, and bounded agent patterns;
- partition model, deterministic, tool, storage, and human responsibilities;
- design precise tool contracts;
- place validation and human approval at the right boundaries;
- handle retries, idempotency, timeouts, fallback, and rollback;
- persist long-running state outside the prompt;
- instrument stage-level outcomes; and
- prefer the simplest architecture that satisfies the requirements.

## Files

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

Scenarios often tempt you to make the model responsible for exact rules or irreversible actions. Prefer deterministic components for authorization, calculations, validation, and side effects. Keep model autonomy bounded by tool permissions and approval gates.

## Completion criteria

- [ ] I can create a component responsibility matrix.
- [ ] I can identify where idempotency is required.
- [ ] I can place a meaningful human approval gate.
- [ ] I can describe stage-level observability and fallback.
- [ ] I completed the workflow lab and scored at least 80% on the quiz.

## Official reading

- [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
