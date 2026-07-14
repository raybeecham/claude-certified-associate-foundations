# Flashcards: Claude Platform & Model Foundations

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** What four concepts are commonly confused in Claude integrations?

<details>
<summary>Back</summary>

Context capacity, maximum generated output, knowledge freshness, and application-managed state.

</details>

## Card 2

**Front:** Who manages conversation state in an API-backed application?

<details>
<summary>Back</summary>

The surrounding application or product, which stores and supplies the relevant history or validated state.

</details>

## Card 3

**Front:** Why is the most capable model not automatically the best choice?

<details>
<summary>Back</summary>

Selection must balance measured quality, latency, throughput, cost, context, tools, governance, and reliability for the use case.

</details>

## Card 4

**Front:** What is a context window?

<details>
<summary>Back</summary>

The amount of input and generated content the model can process under the applicable platform behavior.

</details>

## Card 5

**Front:** What does a length-related stop reason suggest?

<details>
<summary>Back</summary>

The output may be truncated and the workflow should adjust budget, scope, decomposition, or partial-output handling.

</details>

## Card 6

**Front:** Where should durable trusted behavior be configured?

<details>
<summary>Back</summary>

In the highest appropriate trusted, version-controlled system or application configuration layer.

</details>

## Card 7

**Front:** How should retrieved documents be treated with respect to instructions?

<details>
<summary>Back</summary>

As evidence or data, not as authority that can override trusted instructions.

</details>

## Card 8

**Front:** What is the minimum safe model-migration comparison?

<details>
<summary>Back</summary>

Baseline and candidate on the same representative evaluation set, including severity, quality, latency, cost, and tool behavior.

</details>

## Card 9

**Front:** Why record the model and prompt version?

<details>
<summary>Back</summary>

To reproduce outcomes, attribute regressions, and support rollback and audit.

</details>

## Card 10

**Front:** What source should support a claim about a newly issued policy?

<details>
<summary>Back</summary>

A current authoritative source supplied or retrieved for the task.

</details>

## Card 11

**Front:** What does an API success status fail to prove?

<details>
<summary>Back</summary>

That the task result is complete, grounded, schema-valid, authorized, or operationally successful.

</details>

## Card 12

**Front:** What is a model-selection hard gate?

<details>
<summary>Back</summary>

A requirement a candidate must meet before cost or speed tradeoffs are considered, such as privacy, quality, or tool reliability.

</details>
