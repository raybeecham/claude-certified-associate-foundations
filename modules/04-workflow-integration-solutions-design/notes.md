# Notes: Workflow Integration & Solutions Design

## 1. Choose the simplest interaction pattern

Start with the lowest-complexity pattern that satisfies the requirements.

| Pattern | Best fit | Key limitation |
|---|---|---|
| Interactive chat | Human-led exploration and drafting | Limited repeatability and integration |
| Fixed workflow | Known sequence with defined handoffs | Less adaptive to novel paths |
| API-backed application | Controlled experience, data, validation, and integration | Application must manage state and operations |
| Bounded agent | Dynamic task planning and tool selection | More complex governance, observability, and failure handling |
| Managed long-running capability | Extended work with platform-managed execution | Requires careful fit assessment, access controls, and monitoring |

Do not use an agent merely because the task has several steps. A known sequence is usually safer and easier to test as an explicit workflow.

## 2. Partition responsibilities deliberately

A reliable design assigns each responsibility to the component best suited to it.

### Claude

Good candidates:

- summarization;
- classification under defined criteria;
- synthesis across sources;
- extraction from semi-structured content;
- drafting;
- natural-language explanation;
- proposing alternatives; and
- planning within a bounded task.

### Deterministic code

Good candidates:

- exact arithmetic;
- schema validation;
- access control;
- business rules;
- date and identifier validation;
- deduplication;
- threshold enforcement;
- state transitions;
- idempotency;
- cryptographic operations; and
- audit event creation.

### Tools and services

Good candidates:

- retrieving approved records;
- querying authoritative systems;
- performing an allowed action;
- writing to a controlled destination;
- calculating through a trusted service; and
- obtaining current external data.

### Humans

Good candidates:

- high-impact decisions;
- ambiguous source conflicts;
- policy exceptions;
- irreversible release approvals;
- legal, clinical, financial, or employment judgment;
- incident response authority; and
- final accountability.

A human review step is meaningful only when the reviewer has the expertise, evidence, time, and authority to reject or modify the result.

## 3. Design the workflow around trust boundaries

Map:

- users and identities;
- trusted instructions;
- untrusted content;
- data stores;
- tools;
- external services;
- model calls;
- human reviewers;
- side effects; and
- logs.

For every boundary, ask:

1. What enters?
2. Who authorized it?
3. How is it validated?
4. What data classification applies?
5. What may leave?
6. What is logged?
7. What happens on failure?

## 4. Tool contracts

A tool should expose one clear capability through a narrow contract.

### Contract elements

- name;
- purpose;
- when to use;
- when not to use;
- authorization requirement;
- input schema;
- output schema;
- side effects;
- error cases;
- timeout behavior;
- retry safety;
- idempotency support; and
- audit requirements.

### Weak design

```text
Tool: manage_system
Description: Performs system operations.
```

This is ambiguous and overly broad.

### Stronger design

```text
Tool: create_draft_change_request
Use only after a validated control gap has been confirmed.
Creates a non-executable draft. It does not approve or deploy changes.
Requires system_id, control_id, evidence_refs, proposed_owner_role,
and requested_review_date.
```

The surrounding application validates every argument and independently enforces authorization.

## 5. Side effects and idempotency

Retries are normal in distributed systems. An operation that sends a message, creates a ticket, changes a record, or transfers value can create duplicates if blindly repeated.

Use:

- idempotency keys;
- operation status checks;
- unique business identifiers;
- transactional boundaries;
- deduplication;
- at-least-once versus exactly-once assumptions; and
- explicit retry rules.

Read-only operations may be safe to retry. Side-effecting operations require stronger controls.

## 6. State and resumability

Long-running work must survive process restarts, user pauses, rate limits, and reviewer delays.

Persist:

- workflow identifier;
- current state;
- completed steps;
- validated intermediate artifacts;
- source and prompt versions;
- pending approvals;
- tool call status;
- retry count;
- expiration; and
- final outcome.

Do not rely on the model context as the sole durable state store. Validate state transitions deterministically.

## 7. Human approval gates

Place approval **before** the consequential action.

Examples:

- before publishing an incident statement;
- before sending a legal notice;
- before modifying production access;
- before submitting a high-impact eligibility decision;
- before executing a change plan; and
- before disclosing sensitive information.

Provide reviewers with:

- the proposed action;
- supporting evidence;
- uncertainty and conflicts;
- policy checks;
- known limitations;
- change history; and
- approve, reject, modify, and escalate options.

A reviewer who only sees the final prose cannot validate the evidence chain.

## 8. Failure handling

Define expected behavior for each failure class.

| Failure | Example response |
|---|---|
| Transient service error | Bounded retry with backoff and jitter |
| Invalid model output | Reject, repair under strict controls, or rerun |
| Unauthorized request | Deny and log |
| Tool timeout | Check status before retrying |
| Missing evidence | Ask for input or escalate |
| Source conflict | Surface conflict and route according to authority |
| Refusal | Respect boundary, classify, and provide allowed fallback |
| Human timeout | Escalate or expire safely |
| Partial workflow completion | Resume from validated checkpoint |
| Critical validation failure | Stop and contain |

Fallbacks should not silently reduce safety. For example, skipping citations because retrieval failed is not a valid fallback for a grounded task.

## 9. Observability

Capture stage-level metrics rather than a single end-to-end number.

Recommended stages:

- authentication;
- input validation;
- retrieval;
- model request;
- tool selection;
- tool execution;
- output validation;
- human review; and
- final side effect.

Record:

- request and workflow IDs;
- versioned prompts and schemas;
- source set;
- tool arguments and outcomes, with redaction;
- stop reason;
- latency and token use;
- retries;
- validation failures;
- approval decision; and
- disposition.

This enables troubleshooting, audit, and cost analysis.

## 10. Architectural decision record

For important solutions, write a short ADR.

```text
Decision:
Use case:
Requirements:
Options considered:
Chosen pattern:
Responsibility split:
Trust boundaries:
Human controls:
Failure handling:
Observability:
Residual risks:
Revisit trigger:
```

## 11. Common design mistakes

| Mistake | Better approach |
|---|---|
| Model performs exact authorization | Enforce authorization in code |
| Agent has broad generic tools | Narrow, purpose-specific tools |
| Retry all failures | Classify and retry only safe transient failures |
| Human approves after execution | Gate before the side effect |
| Workflow state exists only in prompt | Persist validated state externally |
| One end-to-end latency metric | Profile every stage |
| Hidden fallback to ungrounded answer | Fail safely or escalate |
| Complex agent for fixed sequence | Use explicit workflow |

## 12. Review questions

1. What evidence supports choosing an agent instead of a fixed workflow?
2. Which tasks should remain deterministic?
3. How do idempotency and retries interact?
4. What makes a human approval gate meaningful?
5. Which workflow fields must be versioned for reproducibility?
