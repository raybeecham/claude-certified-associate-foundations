# Context as Working Memory

## The model

Treat active model context like a limited engineering workspace, not an unlimited archive.

It may contain:

- instructions;
- conversation history;
- current inputs;
- retrieved knowledge;
- tool definitions and results;
- examples; and
- generated output.

Every item competes for attention.

## Capacity is not quality

A large context window does not guarantee reliable recall across all included information.

```text
More context
    ≠
More relevant context
    ≠
Better reasoning
```

Useful context is:

- authorized;
- relevant;
- current;
- authoritative;
- nonduplicative; and
- structured for the task.

## Information lifecycle

| Information | Correct location |
|---|---|
| Current task detail | Active conversation |
| Stable workstream rule | Project or system instructions |
| Reusable approved source | Knowledge base |
| Reusable procedure | Skill or workflow definition |
| General preference | Memory, when appropriate |
| Current operational truth | External system of record |
| Traceable decision | Decision log |

## Context intervention

```text
Thread is healthy and focused -> continue
Thread has avoidable noise     -> clean or narrow
State must transfer            -> summarize and validate
Durable information emerged    -> persist correctly
Task or phase changed          -> restart cleanly
```

## State capsule

Use a compact handoff containing:

- objective;
- scope;
- accepted decisions;
- authoritative sources and versions;
- constraints;
- completed work;
- open questions;
- risks and assumptions;
- next actions; and
- required approval.

Validate the state capsule before using it as trusted context.

## Security implication

Untrusted text can become more dangerous when copied into a durable summary, memory, or instruction store.

Do not automatically persist instructions found in:

- websites;
- uploaded documents;
- emails;
- retrieved records;
- tool results; or
- model-generated summaries.

Require provenance and authorization.

## Decision rule

> Reconstruct the smallest authoritative context required for the next action.
