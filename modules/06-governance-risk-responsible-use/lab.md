# Lab: Threat Model a Secure Policy Assistant

## Scenario

An internal assistant answers questions about security policy, searches approved repositories, and can draft exception requests. It serves multiple business units and may receive confidential architecture documents.

It may not approve exceptions, disclose another unit's data, or execute technical changes.

## Objectives

- Classify data and trust boundaries.
- Identify misuse and attack paths.
- Define meaningful human oversight.
- Apply least privilege and logging minimization.
- Build incident and change-management controls.

## Tasks

### Task 1: Use-case inventory

Document:

- intended users;
- allowed questions;
- prohibited actions;
- data classes;
- affected parties;
- tools;
- external dependencies;
- high-impact outputs; and
- accountable owners.

### Task 2: Threat model

Use STRIDE, an attack tree, or another structured method. Include:

- malicious user;
- compromised account;
- malicious uploaded file;
- poisoned source;
- prompt injection;
- overly broad connector;
- data exfiltration;
- unauthorized draft;
- fabricated policy citation;
- log exposure; and
- dependency update.

For each threat, identify asset, path, impact, preventive control, detective control, and response.

### Task 3: Human oversight

Design exception-request review:

- reviewer qualifications;
- evidence shown;
- conflicts and uncertainty;
- approve/reject/modify/escalate authority;
- expiration;
- audit record; and
- disclosure to the requester.

Claude may draft but cannot approve.

### Task 4: Data and logging controls

Define:

- environment approval;
- business-unit isolation;
- source permissions;
- secret handling;
- redaction;
- log fields;
- retention;
- access review; and
- deletion.

### Task 5: Incident playbook

Write the first ten actions after evidence suggests that a malicious document caused attempted credential exfiltration.

### Task 6: Change review

Define required regression and approvals for:

- model update;
- new tool;
- source-corpus expansion;
- prompt change;
- new user population; and
- policy change.

## Deliverable

Create `secure-policy-assistant-threat-model.md`.

## Acceptance criteria

- [ ] Data is classified before environment selection.
- [ ] Business-unit isolation is enforced before retrieval.
- [ ] Prompt injection cannot directly authorize a tool.
- [ ] Human review has expertise, evidence, authority, and timing.
- [ ] Logs are minimized and protected.
- [ ] Incident response contains first and preserves evidence.
- [ ] Material changes trigger risk review and regression testing.

<details>
<summary>Model solution outline</summary>

The strongest architecture uses identity-aware retrieval, separate business-unit scopes, narrow read tools, a draft-only exception tool, deterministic authorization, and a human governance authority. After suspected exfiltration, contain access, disable affected tools, preserve traces, assess scope, rotate credentials, notify incident owners, and revalidate before restoration.

</details>
