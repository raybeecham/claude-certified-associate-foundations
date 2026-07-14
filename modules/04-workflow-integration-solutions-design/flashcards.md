# Flashcards: Workflow Integration & Solutions Design

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** When is an explicit workflow preferable to an agent?

<details>
<summary>Back</summary>

When the sequence is known and can use deterministic transitions and bounded model calls.

</details>

## Card 2

**Front:** What tasks should usually be deterministic?

<details>
<summary>Back</summary>

Arithmetic, validation, authorization, business rules, state transitions, and irreversible side effects.

</details>

## Card 3

**Front:** What tasks commonly fit Claude?

<details>
<summary>Back</summary>

Language analysis, extraction, classification, synthesis, drafting, and bounded planning.

</details>

## Card 4

**Front:** What makes human review meaningful?

<details>
<summary>Back</summary>

A qualified reviewer sees the evidence and uncertainty and can reject, modify, or escalate before the action.

</details>

## Card 5

**Front:** What is a tool contract?

<details>
<summary>Back</summary>

A definition of purpose, selection rules, authorization, schema, side effects, errors, retries, and audit.

</details>

## Card 6

**Front:** What is idempotency?

<details>
<summary>Back</summary>

The property that repeating an operation does not create unintended duplicate effects.

</details>

## Card 7

**Front:** Why check status after a tool timeout?

<details>
<summary>Back</summary>

The original side effect may have succeeded, so a blind retry could duplicate it.

</details>

## Card 8

**Front:** Where should long-running workflow state live?

<details>
<summary>Back</summary>

In a durable external state store with validated transitions.

</details>

## Card 9

**Front:** What is a safe fallback for failed grounded retrieval?

<details>
<summary>Back</summary>

Fail safely, ask for evidence, or escalate, rather than silently produce an ungrounded answer.

</details>

## Card 10

**Front:** Why instrument stages separately?

<details>
<summary>Back</summary>

To identify quality, latency, cost, tool, and failure behavior at the responsible component.

</details>

## Card 11

**Front:** What should an architecture decision record contain?

<details>
<summary>Back</summary>

Requirements, options, chosen pattern, responsibility split, controls, risks, and revisit triggers.

</details>

## Card 12

**Front:** What is the simplest-architecture principle?

<details>
<summary>Back</summary>

Use no more autonomy and infrastructure than the measurable requirements demand.

</details>
