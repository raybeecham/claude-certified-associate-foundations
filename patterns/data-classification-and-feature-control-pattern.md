# Data Classification and Feature-Control Pattern

## Problem

Teams often choose a feature before deciding whether the data is permitted in that environment.

This creates recurring failures:

1. sensitive information is uploaded before classification;
2. Incognito, Memory settings, or sandboxing are mistaken for compliance approval;
3. partial redaction leaves people identifiable; and
4. over-redaction destroys the validity of the task.

## Context

Use this pattern when a workflow involves:

- file uploads;
- code execution;
- Projects and Project knowledge;
- Memory or chat search;
- Incognito chats;
- connectors;
- regulated, personal, confidential, or third-party data;
- data exports or retention; or
- analytics that may permit re-identification.

## Recommended design

```text
Define task and minimum data
      ↓
Classify data
      ↓
Confirm approved environment
      ↓
Minimize, redact, aggregate, or synthesize
      ↓
Select feature and persistence controls
      ↓
Test privacy and task validity
      ↓
Approve, constrain, redesign, defer, or reject
```

## 1. Rapid classification

Use a simple screening model that maps to current organizational policy.

| Tier | Meaning | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or widely cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path is confirmed |

```text
Uncertain tier
      ↓
Treat as more sensitive
      ↓
Seek authorized clarification
```

## 2. Minimum necessary data

For each field, decide whether it is:

- required;
- removable;
- aggregatable;
- pseudonymizable;
- replaceable with synthetic data;
- a secret that must be excluded; or
- too sensitive for the proposed path.

```text
Available
      ≠
Necessary
```

## 3. Redaction validity

A valid privacy transformation must satisfy both:

```text
Reduced identification risk
      +
Preserved task validity
```

Review direct and indirect identifiers, including exact dates, rare attributes, precise locations, small groups, account references, and free text.

If identifiers are essential, move the task to an approved environment or stop. Do not label a dataset anonymous merely because names were removed.

## 4. Processing authorization

Before selecting a persistence feature, establish:

- active account and organization;
- approved product and entry point;
- permitted data classes;
- contractual, regulatory, and third-party restrictions;
- data owner approval;
- required privacy, legal, security, or records review; and
- incident and escalation paths.

```text
Processing allowed?
      ↓
Then decide retention and persistence.
```

## 5. Feature controls

### Code execution

Sandboxing can isolate execution, but does not establish that the data may be processed. Minimize files, remove secrets, review network behavior, validate outputs, and handle artifacts according to policy.

### Memory

Use Memory only for approved continuity. Do not treat it as an authoritative record, permission boundary, or suitable location for sensitive material merely because it is convenient.

### Incognito

Use Incognito to exclude an approved conversation from ordinary chat history and Memory. On organizational accounts, retention and export rules may still apply.

```text
Incognito
      ≠
No retention
      ≠
Permission to process Red data
```

### Connectors and sharing

Apply least privilege, source scope, role controls, retention, and revocation. Access to data does not mean permission to process it for every purpose.

## 6. Decision outcomes

| Outcome | Meaning |
|---|---|
| Approve | Data and environment are permitted; controls are sufficient |
| Constrain | Reduce data, persistence, access, or scope |
| Redesign | Use synthetic data, local approved processing, or a different workflow |
| Defer | Policy, contract, plan, or owner approval is unresolved |
| Reject | No responsible approved path exists |

## Controls

- data owner and classification;
- minimum-necessary field list;
- approved environment record;
- redaction and re-identification test;
- feature-control map;
- retention and deletion rules;
- least privilege;
- human review;
- approval evidence;
- incident and escalation path; and
- review date.

## Failure modes

### Incognito-as-compliance

**Failure:** The user assumes history and Memory exclusion authorizes regulated data.

**Repair:** Confirm processing approval before choosing persistence controls.

### Sandbox-as-authorization

**Failure:** A sandbox is treated as proof the data is allowed.

**Repair:** Classify data and verify the approved environment first.

### Partial redaction

**Failure:** Direct names are removed but indirect identifiers remain.

**Repair:** Test combinations, free text, small groups, and linkage risk.

### Invalid redaction

**Failure:** Privacy transformation removes information required for valid analysis.

**Repair:** Use an approved path or redesign the task.

### Plan-label assumptions

**Failure:** Users rely on remembered plan behavior rather than current organization settings.

**Repair:** Verify account, feature enablement, retention, export, and administrator controls.

## Compact decision rule

> Classify before entry, confirm that processing is allowed, minimize what the task does not need, use redaction only when privacy improves without invalidating the work, and treat Incognito, Memory, and sandboxing as bounded controls rather than permission to process sensitive data.

## Review checklist

- What is the exact task?
- Who owns the data?
- What is the current classification?
- Which fields are necessary?
- Are direct or indirect identifiers present?
- Does redaction preserve validity?
- Is this account and environment approved?
- What history, Memory, export, retention, and deletion rules apply?
- Are connector and execution permissions minimal?
- Who approved the decision?
- What happens if the classification or feature behavior changes?
