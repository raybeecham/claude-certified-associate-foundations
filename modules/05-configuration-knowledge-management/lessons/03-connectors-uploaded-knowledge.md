# Lesson 3: Connectors and Uploaded Knowledge

## Overview

Connectors and uploaded files extend what Claude can use, but access alone does not establish authority, freshness, completeness, or permission to act.

```text
Connector or uploaded source
      ↓
Authorized access
      ↓
Known capability boundary
      ↓
Source authority and freshness
      ↓
Task-specific retrieval
      ↓
Human review and controlled action
```

This lesson develops four capabilities:

1. connecting external sources deliberately;
2. documenting what each connector can and cannot do;
3. separating access from source authority and action authority; and
4. maintaining uploaded knowledge as a curated source set.

> A connector is an access path. It is not a blanket trust decision or an unlimited permission grant.

---

# Plain-English explanation

A connector lets Claude reach an external system that the user or organization has authorized.

Examples may include:

- searching email;
- finding a document in cloud storage;
- reading a calendar;
- retrieving repository files;
- creating a draft; or
- invoking a narrowly defined external tool.

The exact capability depends on the connector, product surface, plan, administrator settings, identity, permission scope, and enabled tools.

```text
Connected
      ≠
Permitted for every task
      ≠
Authoritative
      ≠
Able to perform every action
```

Uploaded knowledge has a different operating model. It is explicitly added to a chat or Project, but it still requires ownership, version control, deduplication, and retirement.

---

# One analogy: a building access badge

A badge may open several doors, but it does not make every room relevant to the current job.

The badge also does not tell you:

- which records are controlling;
- whether a document is current;
- whether you may modify anything;
- whether another person must approve an action; or
- whether the access should still exist next month.

Connectors work similarly.

```text
Access badge → connector authorization
Room contents → retrieved source
Operating procedure → workflow instructions
Approval to change something → separate authority
```

---

# Connecting external sources deliberately

Before enabling a connector, define:

- business purpose;
- intended users;
- permitted systems and accounts;
- read capabilities;
- write or external-action capabilities;
- data sensitivity;
- authoritative source types;
- expected query patterns;
- retention and logging requirements;
- approval requirements;
- owner;
- review date; and
- revocation conditions.

Use the smallest connector and permission set that supports the approved use case.

```text
Connect everything by default
      ≠
Useful knowledge management
```

On managed plans, organization administrators may need to enable or authorize connectors before individuals authenticate. Approved installation and authorization paths should be confirmed with the organization's administrator.

---

# Connector capability contracts

Every connector should have a visible capability contract.

| Field | Question answered |
|---|---|
| Connector | Which integration is involved? |
| Identity | Whose permissions are used? |
| Sources | Which systems, folders, mailboxes, or records are accessible? |
| Read tools | What can Claude search or retrieve? |
| Write tools | What can Claude create, modify, send, or delete? |
| Unsupported actions | What must not be expected? |
| Approval boundary | Which actions require human confirmation? |
| Error modes | How do permission, scope, timeout, and unsupported-action failures appear? |
| Owner | Who maintains the integration? |
| Review date | When are access and capabilities revalidated? |

## Capability examples

Current official guidance describes Google Workspace connector capabilities such as searching and reading Gmail, creating Gmail drafts, working with Google Calendar, and retrieving or saving Drive content. Gmail draft creation does not mean Claude can send the email.

Other connectors may have different action models. Some Microsoft 365 deployments, for example, can enable write tools after additional administrator consent.

Therefore:

```text
Mail connector
      ≠
Universal mail capability
```

Do not infer capability from the system name. Inspect the exact connector, tool set, permission configuration, and current documentation.

---

# Read, draft, approve, and execute are separate stages

A workflow should expose each consequential transition.

```text
Search source
      ↓
Read evidence
      ↓
Draft proposed action
      ↓
Human review and approval
      ↓
Controlled execution, when supported
```

For example:

```text
Search relevant messages      → connector read capability
Draft a response              → draft capability or model output
Approve wording and recipient → human-retained
Send message                  → separate write tool, if enabled and authorized
```

A connector that can draft but not send has not failed when it stops at the draft boundary. The workflow expectation was incorrect.

---

# Boundary-aware troubleshooting

When a connector does not produce the expected result, classify the failure before escalating.

| Failure class | Diagnostic question |
|---|---|
| Not installed or enabled | Is the connector available to this user and organization? |
| Authentication | Is the correct account connected and authorized? |
| Permission | Does that identity have access to the requested item? |
| Scope | Is the source outside the configured folder, mailbox, repository, or tenant? |
| Capability | Does the connector support the requested action? |
| Tool loading | Is the connector enabled for this conversation? |
| Source problem | Is the item missing, stale, renamed, or inaccessible? |
| Product defect | Does supported behavior fail despite correct setup and permissions? |

```text
Unexpected result
      ≠
Product bug
```

## Operational cautions from the supplied course material

The course reports two field-observed pitfalls:

1. an apparently obvious connector-addition path may lead users toward a public directory rather than an organization's vetted connector set; and
2. a capability-boundary failure may be mislabeled as a product defect and routed to the wrong support team.

Treat these as operational cautions, not universal documented behavior. Confirm approved installation paths and connector capabilities with current documentation and the relevant administrator.

---

# Uploaded knowledge

Files can be attached to individual chats or added to Project knowledge for reuse across Project conversations.

Uploaded knowledge should be curated like a maintained shared repository.

For every material file, record:

- source ID;
- title;
- owner;
- authority;
- effective date;
- review or expiration date;
- scope;
- sensitivity;
- version;
- replacement;
- conflicts; and
- permitted use.

```text
File uploaded
      ≠
File approved
      ≠
File current
      ≠
File controlling
```

---

# Duplicate and superseded knowledge

A Project containing three versions of the same policy creates ambiguity.

Potential outcomes include:

- citation of an obsolete rule;
- blended requirements from incompatible versions;
- inconsistent answers across chats;
- unnecessary retrieval noise; and
- hidden disagreement between sources.

Use a supersession process:

```text
New source approved
      ↓
Identify replaced source
      ↓
Remove or clearly label superseded version
      ↓
Update source register
      ↓
Run regression questions
      ↓
Record effective date and owner
```

Historical sources may be retained when the use case requires history, but their status must be explicit.

---

# Synced versus static sources

Not all Project knowledge refreshes the same way.

Current official guidance states that Google Docs added from Drive can remain synchronized with the latest Drive version. Other uploaded files may be static snapshots that require manual replacement.

The source register should identify refresh behavior:

| Refresh type | Maintenance implication |
|---|---|
| Synced source | Monitor upstream ownership, access, and material changes |
| Static upload | Replace manually when the controlling source changes |
| Connector retrieval | Validate permissions, query scope, and source currency at use time |
| Historical archive | Prevent accidental treatment as current authority |

```text
Connected or synced
      ≠
Reviewed and approved
```

---

# Connector and knowledge register

| ID | Source or connector | Access/capability | Authority | Scope | Refresh | Owner | Review date | Action boundary |
|---|---|---|---|---|---|---|---|---|
| C-001 | Approved mail connector | Search, read, draft | Evidence source | Named mailbox | Live | Workspace owner | Quarterly | No send |
| K-001 | Current policy | Read | Controlling | Domestic travel | Static upload | Policy owner | On change | Reference only |
| K-002 | Prior policy | Read | Superseded | Historical comparison | Archive | Policy owner | Annual | Never current guidance |

This register prevents connector names and file availability from becoming implicit assumptions.

---

# Worked example: recurring policy brief

A fictional compliance team prepares weekly policy-change briefs.

## Connectors

- read-only access to an approved document repository;
- email search for messages from the policy owner;
- no authority to send, publish, or modify the source repository.

## Uploaded knowledge

- current briefing template;
- approved terminology guide;
- current review checklist;
- no superseded policy copies unless explicitly labeled historical.

## Workflow

```text
Retrieve current sources
      ↓
Check version and effective date
      ↓
Extract material changes
      ↓
Draft briefing
      ↓
Qualified human review
      ↓
Authorized publication outside Claude
```

## Controls

- connector capability register;
- source authority order;
- conflict handling;
- duplicate detection;
- weekly source review;
- quarterly permission review; and
- offboarding and revocation process.

---

# Common failure modes

## 1. Connector availability treated as authority

**Failure:** any retrieved item is accepted as controlling.

**Repair:** classify authority, scope, version, and owner.

## 2. Capability assumed from connector name

**Failure:** the workflow expects send, update, or delete behavior that is not enabled.

**Repair:** maintain a tool-level capability contract.

## 3. Everything connected by default

**Failure:** excessive tool overhead, retrieval noise, and broader access than needed.

**Repair:** apply least privilege and enable only relevant connectors.

## 4. Static upload treated as live

**Failure:** a replaced document remains in Project knowledge.

**Repair:** record refresh type, review date, and replacement process.

## 5. Duplicate versions retained without status

**Failure:** Claude cites an obsolete or conflicting policy.

**Repair:** remove, archive, or explicitly label superseded versions.

## 6. Unsupported action reported as a bug

**Failure:** troubleshooting begins with the wrong team.

**Repair:** check installation, authentication, permissions, scope, capability, and tool loading before classifying a defect.

---

# Connector and uploaded-knowledge protocol

```text
1. Define the business purpose and user
2. Identify the minimum required external sources
3. Confirm the approved installation and authorization path
4. Record identity, permissions, and source scope
5. Enumerate read, draft, write, and unsupported capabilities
6. Establish source authority, freshness, and conflict rules
7. Curate uploaded files and remove or label superseded versions
8. Separate retrieval, drafting, approval, and execution
9. Test successful, denied, missing, stale, conflicting, and unsupported cases
10. Monitor usage, permissions, source changes, and failures
11. Reauthorize, update, disable, or retire when conditions change
```

---

# Exam lens

```text
External source is needed            → connector with approved scope
File should persist across Project   → Project knowledge
Connector can read but not act       → redesign around capability boundary
Several versions of one policy       → identify current authority and remove ambiguity
All connectors enabled by default    → apply least privilege
Unexpected connector failure         → classify setup, auth, permission, scope, capability, or defect
Synced source changed upstream        → verify authority and material change
Static file became outdated           → replace and regression-test
```

For connector and knowledge scenarios:

1. distinguish access from authority;
2. identify the connected identity and permission scope;
3. document exact capabilities and unsupported actions;
4. separate read, draft, approve, and execute;
5. select the minimum relevant connector set;
6. curate files by authority, freshness, scope, and sensitivity;
7. remove or label duplicates and superseded sources;
8. classify failures before escalation;
9. test connector and source boundaries; and
10. assign ownership, review cadence, and revocation.

---

# Short recap

```text
1. Connectors provide authorized access to external systems.
2. Access does not establish source authority.
3. Every connector needs a capability contract.
4. Read, draft, approve, and execute are separate stages.
5. Connector capabilities differ by product and permission configuration.
6. Troubleshoot setup, authentication, permission, scope, and capability before declaring a bug.
7. Uploaded knowledge is a maintained source set, not a file dump.
8. Remove or clearly label superseded and duplicate sources.
9. Distinguish synced sources from static snapshots.
10. Review permissions, sources, and connector behavior on a cadence.
```

## Educational-use notice

This lesson is an unofficial educational resource. Connector capabilities, plans, settings, and interfaces can change. Verify current official documentation and organizational policy before relying on implementation-specific behavior. Examples are fictional and do not constitute security, privacy, records-management, compliance, or operational advice.
