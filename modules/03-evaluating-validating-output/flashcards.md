# Flashcards: Evaluating & Validating Claude's Output

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** What makes a success criterion useful?

<details>
<summary>Back</summary>

It is specific, measurable, achievable, relevant, and tied to a decision.

</details>

## Card 2

**Front:** Why are multidimensional evaluations necessary?

<details>
<summary>Back</summary>

An output can be fluent yet fail grounding, privacy, consistency, latency, cost, or task fidelity.

</details>

## Card 3

**Front:** What cases belong in a representative evaluation set?

<details>
<summary>Back</summary>

Normal, edge, missing, conflicting, stale, malformed, long, unauthorized, and adversarial cases.

</details>

## Card 4

**Front:** When should code-based grading be used?

<details>
<summary>Back</summary>

For exact properties such as labels, identifiers, schema, arithmetic, and thresholds.

</details>

## Card 5

**Front:** When is human grading necessary?

<details>
<summary>Back</summary>

For nuanced, consequential, or expert judgment where accountability and context matter.

</details>

## Card 6

**Front:** What controls a model-assisted grader?

<details>
<summary>Back</summary>

A calibrated rubric, score anchors, independent evidence, human review, and agreement monitoring.

</details>

## Card 7

**Front:** What is citation accuracy?

<details>
<summary>Back</summary>

Whether the cited source actually supports the claim attached to it.

</details>

## Card 8

**Front:** How do you validate grounding at claim level?

<details>
<summary>Back</summary>

Extract claims, map each to evidence, and mark supported, partial, unsupported, or contradicted.

</details>

## Card 9

**Front:** Why repeat the same evaluation case?

<details>
<summary>Back</summary>

To measure variance and consistency when stable behavior is required.

</details>

## Card 10

**Front:** What is a regression test?

<details>
<summary>Back</summary>

A repeated test used to detect degradation after model, prompt, tool, source, or configuration changes.

</details>

## Card 11

**Front:** Why can a higher average score still block release?

<details>
<summary>Back</summary>

A critical failure such as unauthorized disclosure cannot be offset by low-severity improvements.

</details>

## Card 12

**Front:** What is a holdout set?

<details>
<summary>Back</summary>

Evaluation cases reserved from prompt tuning for a less biased final validation.

</details>
