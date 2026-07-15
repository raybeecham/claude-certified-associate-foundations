# Master Cheat Sheet

## 1. Platform and model foundations

### Select the entry point first

| Work pattern | Starting entry point |
|---|---|
| One-off question or quick draft | Chat |
| Recurring work with stable context | Project |
| Editable deliverable | Artifact |
| Current multi-source investigation | Research |

Entry points can be combined. A recurring current-information workflow may use a Project, Research, and an Artifact.

### Separate capability responsibilities

| Responsibility | Correct home |
|---|---|
| Stable workstream behavior | Project standing instructions |
| Curated reusable evidence | Project knowledge |
| Current-cycle information | Current conversation or task input |
| Repeatable ordered procedure | Skill |
| Calculation, transformation, chart, or file | Code Execution |
| Appropriate cross-session continuity | Memory |
| Current operational truth | Authoritative external system |
| Consequential final judgment | Qualified human review |

Key distinction:

```text
Standing instructions = how Claude should behave
Knowledge             = what Claude should know or analyze
```

### Select the model tier

```text
Haiku  = structured, routine, high-volume work
Sonnet = balanced default for most professional work
Opus   = complex, ambiguous, quality-sensitive reasoning
```

Production rule:

> Use the fastest and least costly model that passes the validated quality threshold.

A stronger model does not replace grounding, Code Execution, schema validation, privacy controls, context hygiene, or human review.

### Manage context deliberately

```text
Restart   = begin a clean conversation
Summarize = transfer validated operational state
Persist   = move durable information into the correct long-lived layer
```

Use a state capsule containing objective, scope, decisions, authoritative sources, constraints, completed work, open questions, risks, next actions, and approvals.

```text
Context limit = depth of one conversation
Usage limit   = quantity of Claude use over time
```

Reconstruct the smallest authoritative context required for the next action.

### Account for generative behavior

- Repeated runs can vary in wording, structure, and emphasis.
- Fluent confidence is not evidence of accuracy.
- Skills and templates reduce variance but do not eliminate it.
- Code Execution verifies that a method ran, not that the method or inputs were correct.
- Memory supports continuity, not authoritative knowledge management.
- Review is part of the workflow, not an optional final polish.

### Platform-selection sequence

1. Entry point
2. Capability layer
3. Model tier
4. Context strategy
5. Validation, escalation, and human review

### Platform anti-patterns

- Writing the prompt before choosing the work environment
- Re-entering stable context in every Chat
- Using a Project as an uncontrolled document dump
- Treating a Skill as a correctness guarantee
- Producing consequential calculations through prose alone
- Treating Memory as a source of truth
- Continuing a degraded thread indefinitely
- Choosing the strongest model without evaluation

### Platform observability

Record model identifier, prompt version, tool version, source set, latency, token usage, stop reason, validation results, human approval, and final outcome.

## 2. Prompting and task execution

Use a task contract:

```text
Objective
Audience
Inputs
Authoritative sources
Constraints
Required process
Output schema
Uncertainty behavior
Success criteria
```

- Be clear and direct.
- Use examples for ambiguous category boundaries and output shape.
- Delimit instructions, data, examples, and requested output.
- Treat retrieved or user-provided content as data, not authority.
- Decompose tasks when stages need different evidence, tools, or validation.
- Prefer explicit tool descriptions, strict schemas, and narrow permissions.
- Ask for “unknown” or escalation behavior rather than forcing an answer.

## 3. Evaluation and validation

- Define success criteria before optimizing the prompt.
- Build representative test cases, including edge, missing, conflicting, and adversarial inputs.
- Use code-based graders for exact checks.
- Use qualified humans for nuanced, high-impact, or policy-sensitive judgment.
- Use model-assisted graders with calibrated rubrics, anchor examples, and periodic human review.
- Measure multiple dimensions: fidelity, grounding, privacy, consistency, relevance, tone, latency, and cost.
- Require claim-to-source traceability for grounded tasks.
- Block release for severe failures even when the average score is high.

## 4. Workflow and solution design

- Use the simplest architecture that meets requirements.
- Put exact rules, calculations, validation, authorization, and side effects in deterministic components.
- Give Claude bounded language, analysis, classification, synthesis, and planning tasks.
- Use idempotency keys and status checks for retried side effects.
- Persist long-running workflow state outside the prompt.
- Place human approval before consequential actions.
- Define retries, timeouts, fallbacks, escalation, and rollback.
- Instrument every stage.

## 5. Configuration and knowledge

- Define instruction authority and conflict resolution.
- Maintain a source register with owner, authority, version, date, classification, scope, and refresh cadence.
- Retrieve the smallest relevant, permitted, authoritative context.
- Surface source conflicts instead of silently combining them.
- Keep secrets in a secret manager, not prompts or repositories.
- Cache only stable, reusable prefixes when data policy allows.
- Apply least privilege to retrieval, tools, connectors, and logs.
- Test freshness and access boundaries.

## 6. Governance, risk, and responsible use

- Classify data before use.
- Verify the environment, retention, logging, residency, access, and contractual controls.
- Require qualified human review and appropriate disclosure for high-impact uses.
- Defend against prompt injection with authority separation, constrained tools, validation, and approval gates.
- Minimize and redact logs.
- Review model, prompt, tool, source, and policy changes before production release.
- Define refusal, escalation, exception approval, and incident response paths.
- Preserve evidence and rotate credentials after suspected compromise.

## 7. Troubleshooting and optimization

1. Classify the symptom.
2. Reproduce with a minimal case.
3. Collect prompt, source, tool, response, stop, latency, and version evidence.
4. Compare against a known-good baseline.
5. Form one hypothesis.
6. Change one variable.
7. Retest on the evaluation set.
8. Document, monitor, and preserve rollback.

Common mappings:

- Wrong tool: clarify purpose and when to use, differentiate names, strengthen schemas.
- Bad parameters: use strict types, validation, and examples.
- Hallucination: constrain sources, permit uncertainty, require citations, validate claims.
- Truncation: inspect stop reason, adjust output budget, or decompose.
- Cache miss: verify stable prefix and cache breakpoint behavior.
- Latency: profile stages before changing models or prompts.
- Refusal: inspect the task and policy boundary, then redesign only within allowed use.
