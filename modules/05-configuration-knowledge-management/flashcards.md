# Flashcards: Configuration & Knowledge Management

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** What is a knowledge-source register?

<details>
<summary>Back</summary>

A governed inventory of source owner, authority, version, date, classification, scope, refresh, and provenance.

</details>

## Card 2

**Front:** What determines which conflicting source governs?

<details>
<summary>Back</summary>

Documented authority, scope, effective version, and organizational precedence.

</details>

## Card 3

**Front:** Why is retrieval an authorization decision?

<details>
<summary>Back</summary>

Only permitted sources should reach the model context for the current user and task.

</details>

## Card 4

**Front:** What is the goal of retrieval?

<details>
<summary>Back</summary>

The smallest relevant, permitted, authoritative, current evidence set.

</details>

## Card 5

**Front:** Why is more context not always better?

<details>
<summary>Back</summary>

It can add noise, conflict, stale content, cost, latency, access risk, and prompt injection.

</details>

## Card 6

**Front:** How should unresolved source conflict be handled?

<details>
<summary>Back</summary>

Surface it with citations and route according to the documented authority process.

</details>

## Card 7

**Front:** What does freshness require beyond a file timestamp?

<details>
<summary>Back</summary>

Content version, effective date, owner, review date, supersession, and update process.

</details>

## Card 8

**Front:** What is a strong prompt-caching candidate?

<details>
<summary>Back</summary>

A stable, permitted, reused prefix such as system instructions, tool definitions, or reference content.

</details>

## Card 9

**Front:** What can invalidate a cached prefix?

<details>
<summary>Back</summary>

Changes in content, ordering, tools, system instructions, breakpoints, or applicable expiration.

</details>

## Card 10

**Front:** Where should secrets be stored?

<details>
<summary>Back</summary>

In an approved secret manager, never in prompts, source files, examples, logs, or outputs.

</details>

## Card 11

**Front:** Why must access control occur before retrieval?

<details>
<summary>Back</summary>

Post-generation filtering is too late because unauthorized data already entered model context.

</details>

## Card 12

**Front:** Why version configuration and source sets?

<details>
<summary>Back</summary>

To reproduce outputs, test changes, resolve incidents, and roll back.

</details>
