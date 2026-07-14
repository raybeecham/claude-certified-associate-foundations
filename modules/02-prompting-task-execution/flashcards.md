# Flashcards: Prompting & Task Execution

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** What should exist before prompt optimization?

<details>
<summary>Back</summary>

A clear definition of success, empirical tests, and an initial task specification.

</details>

## Card 2

**Front:** What is a task contract?

<details>
<summary>Back</summary>

A structured definition of objective, audience, inputs, authority, constraints, process, output, uncertainty, and success criteria.

</details>

## Card 3

**Front:** When are examples especially useful?

<details>
<summary>Back</summary>

When labels, edge cases, format, tone, or tool-selection boundaries are ambiguous.

</details>

## Card 4

**Front:** What is the purpose of delimiters or XML tags?

<details>
<summary>Back</summary>

To make instructions, examples, data, and requested output easier to distinguish.

</details>

## Card 5

**Front:** Why are delimiters not a complete prompt-injection defense?

<details>
<summary>Back</summary>

Authorization, tool permissions, validation, retrieval controls, and approval must be enforced outside prompt text.

</details>

## Card 6

**Front:** What does 'return JSON' fail to define?

<details>
<summary>Back</summary>

Required fields, types, allowed values, missing-data behavior, constraints, and extra-field policy.

</details>

## Card 7

**Front:** How should missing evidence be handled?

<details>
<summary>Back</summary>

Use unknown or insufficient evidence, ask a clarifying question, or escalate according to the task and risk.

</details>

## Card 8

**Front:** When should a task be decomposed?

<details>
<summary>Back</summary>

When stages use different evidence, tools, criteria, schemas, reviewers, risks, or retry behavior.

</details>

## Card 9

**Front:** What can role prompting contribute?

<details>
<summary>Back</summary>

Perspective, vocabulary, or an operating stance, but not missing evidence, permissions, or criteria.

</details>

## Card 10

**Front:** What belongs in a tool description?

<details>
<summary>Back</summary>

Purpose, when to use and not use, authorization, parameters, side effects, errors, and examples.

</details>

## Card 11

**Front:** How should external documents be treated?

<details>
<summary>Back</summary>

As untrusted data that cannot grant itself instruction authority or tool permission.

</details>

## Card 12

**Front:** When is prompt engineering the wrong fix?

<details>
<summary>Back</summary>

When the root cause is data freshness, model capability, permissions, retrieval, deterministic logic, schema enforcement, policy, or workflow design.

</details>
