# Flashcards: Troubleshooting & Optimization

Use active recall. Read the front, answer aloud, then open the back.

## Card 1

**Front:** What is the first step in troubleshooting?

<details>
<summary>Back</summary>

Define and classify the symptom before changing the system.

</details>

## Card 2

**Front:** Why reconstruct a known-good baseline?

<details>
<summary>Back</summary>

It provides a controlled comparison for identifying which change caused the regression.

</details>

## Card 3

**Front:** Why change one variable at a time?

<details>
<summary>Back</summary>

To attribute the result and preserve a clear rollback path.

</details>

## Card 4

**Front:** What evidence is needed for a tool-selection failure?

<details>
<summary>Back</summary>

Prompt and model versions, eligible tools, tool descriptions, workflow state, requested call, authorization, and comparable baseline.

</details>

## Card 5

**Front:** How do you reduce wrong-tool selection?

<details>
<summary>Back</summary>

Differentiate names and when-to-use rules, add examples, strengthen schemas, and expose only relevant tools.

</details>

## Card 6

**Front:** How should invented tool fields be handled?

<details>
<summary>Back</summary>

Reject them with a strict schema and application validation rather than silently coercing them.

</details>

## Card 7

**Front:** What should be checked when output ends early?

<details>
<summary>Back</summary>

Stop reason, output budget, context size, client timeout, streaming, tool limits, and task scope.

</details>

## Card 8

**Front:** How should a refusal be investigated?

<details>
<summary>Back</summary>

Check the exact task, current policy, authorization, refusal metadata, and recent system changes without attempting evasion.

</details>

## Card 9

**Front:** What commonly causes prompt-cache misses?

<details>
<summary>Back</summary>

A changed or reordered stable prefix, tool definitions, system content, cache breakpoint, or expiration.

</details>

## Card 10

**Front:** How should latency be optimized?

<details>
<summary>Back</summary>

Profile every stage, identify the bottleneck, and test a targeted change against quality and risk thresholds.

</details>

## Card 11

**Front:** What is the right cost metric?

<details>
<summary>Back</summary>

Total cost per successful task, including retries, tools, infrastructure, correction, and human review.

</details>

## Card 12

**Front:** When is a troubleshooting issue resolved?

<details>
<summary>Back</summary>

After the root cause is fixed, the minimal case and regression set pass, monitoring is in place, and rollback is preserved.

</details>
