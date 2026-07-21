# Pattern: Task Specification Before Prompting

## Problem

A user begins by drafting prompt wording before defining the outcome, evidence, constraints, output, or success criteria. The resulting prompt is vague, overloaded, or difficult to evaluate.

## Context

Use this pattern for business, research, drafting, analysis, planning, extraction, classification, and technical tasks where the intended result matters beyond casual conversation.

## Forces

- Users often know the desired outcome but have not externalized the requirements.
- Models infer unstated details probabilistically.
- More prompt text can introduce conflicts and noise.
- Some failures originate outside the prompt layer.
- A useful output must be both executable and evaluable.

## Solution

Define the task specification before optimizing the final prompt.

```text
Intent
  ↓
Objective
  ↓
Audience and decision
  ↓
Authorized evidence
  ↓
Constraints and boundaries
  ↓
Required process
  ↓
Output contract
  ↓
Uncertainty behavior
  ↓
Success criteria
  ↓
Prompt wording
```

Use minimum sufficient clarity: include every requirement that materially affects execution, safety, or evaluation, and remove everything else.

## Diagnostic rule

When the result is weak, identify the failed layer before rewriting.

```text
Instruction unclear?       → repair the prompt
Evidence unavailable?      → repair retrieval or inputs
Calculation unreliable?    → use deterministic computation
Thread degraded?           → repair context
Capability insufficient?   → reconsider model or tools
Quality unknown?           → repair evaluation
Authority unclear?         → repair governance
```

## Consequences

### Benefits

- Reduces ambiguity.
- Produces outputs that are easier to evaluate.
- Makes iteration targeted rather than speculative.
- Separates prompt design from architecture and governance.
- Improves reuse across models and platforms.

### Costs

- Requires more up-front thinking.
- Can be excessive for trivial, low-consequence tasks.
- Depends on users knowing or discovering their actual requirements.

## Anti-patterns

- Start with a decorative expert persona.
- Add length without adding functional requirements.
- Ask the model to infer the audience and decision.
- Rewrite the entire prompt after every weak result.
- Use prompt wording to compensate for missing evidence or authorization.
- Treat a fluent answer as proof that the task was specified correctly.

## Example

### Before

```text
Analyze the feedback and tell me what to do.
```

### After

```text
Analyze the supplied feedback excerpts to help the product owner select one onboarding issue for further investigation.

Use only the supplied excerpts. Group them into no more than five themes. For each theme, provide the supporting excerpt count, two representative quotations, likely user impact, and one unresolved question.

Rank themes by evidence strength and potential impact. Do not invent percentages or root causes. State when the available evidence is insufficient to distinguish two themes.
```

## Related patterns

- Grounded analysis
- Structured extraction
- Context checkpoint and restart
- Deterministic computation boundary
- Human review gate

## Exam relevance

This pattern supports Official Domain 1: Prompting and Task Execution. In scenario questions, prefer the smallest specific task-contract repair over generic instructions to add more detail.