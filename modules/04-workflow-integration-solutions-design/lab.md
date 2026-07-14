# Lab: Governed PQC Readiness Workflow

## Scenario

Design a workflow that:

1. accepts approved system evidence;
2. maps cryptographic dependencies;
3. compares them with a target migration policy;
4. drafts remediation actions;
5. creates a draft work item; and
6. routes it to an authorized security architect.

The system must not modify production, approve compliance, or assign legal conclusions.

## Objectives

- Select a workflow pattern.
- Partition model, code, tool, storage, and human responsibilities.
- Define safe tool contracts and side-effect controls.
- Design observability, fallback, and rollback.

## Tasks

### Task 1: Architecture

Create a sequence diagram with:

- user;
- identity provider;
- evidence store;
- retrieval service;
- Claude;
- validation service;
- draft work-item tool;
- workflow database;
- reviewer; and
- audit log.

### Task 2: Responsibility matrix

| Step | Claude | Deterministic code | Tool/service | Human |
|---|---|---|---|---|
| Validate user access | | | | |
| Extract cryptographic assets | | | | |
| Validate identifiers | | | | |
| Apply status thresholds | | | | |
| Draft remediation language | | | | |
| Create work item | | | | |
| Approve priority | | | | |
| Deploy a change | | | | |

### Task 3: State machine

Define states such as:

- received;
- authorized;
- evidence_retrieved;
- analysis_validated;
- draft_created;
- awaiting_review;
- approved_for_planning;
- rejected;
- escalated; and
- failed_safe.

List allowed transitions and the deterministic condition for each.

### Task 4: Tool contract

Define `create_draft_remediation_item`.

Requirements:

- idempotency key;
- system and control identifiers;
- evidence references;
- proposed owner role, not an invented person;
- no production change;
- no automatic approval;
- status lookup before retry; and
- audit event.

### Task 5: Failure table

Cover:

- retrieval outage;
- malformed output;
- unsupported claim;
- duplicate tool request;
- reviewer timeout;
- authorization revocation;
- policy conflict; and
- partial completion.

### Task 6: Observability

Define metrics and logs for each stage while minimizing sensitive content.

## Deliverable

Create `governed-workflow-design.md` with the diagram, state machine, contracts, failure handling, and ADR.

## Acceptance criteria

- [ ] Exact validation and authorization remain deterministic.
- [ ] The draft tool has narrow permissions.
- [ ] Retried writes are idempotent.
- [ ] Durable state is external to the prompt.
- [ ] Human review occurs before consequential action.
- [ ] Failure cannot silently fall back to ungrounded output.
- [ ] Every result is traceable to model, prompt, sources, tools, and approval.

<details>
<summary>Model solution outline</summary>

This is a fixed, governed workflow rather than an unconstrained agent. Claude extracts and drafts within defined schemas. Code authorizes users, validates identifiers and evidence, applies hard policy rules, manages state, and enforces transitions. The tool creates only a draft with an idempotency key. A qualified architect approves planning priority, and production deployment is out of scope.

</details>
