# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — Module 5 is the active module. Module 4's final completion checkpoint remains open.

## Module thesis

> Set up the right context, instructions, procedures, continuity, and access once; benefit across repeated conversations; then maintain the configuration so it remains accurate, authorized, scoped, and owned.

```text
Using Claude
      ↓
Current prompt and individual judgment

Operating Claude
      ↓
Configured baseline
+ governed knowledge
+ reusable procedures
+ scoped continuity
+ scoped connector access
+ human controls
+ lifecycle maintenance
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Configuring Projects](lessons/02-configuring-projects.md)
- [x] [03. Connectors & Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)
- [ ] 04. System-Level Instructions That Stick
- [ ] 05. Maintaining Configurations
- [ ] 06. Module 5 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 07. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Using versus operating Claude

A person using Claude supplies the prompt, context, sources, format, and review decisions for the current conversation.

A team operating Claude maintains a bounded, approved environment with:

- standing instructions;
- approved knowledge;
- reusable procedures;
- scoped connectors;
- selected continuity;
- output contracts;
- review and approval gates;
- testing;
- ownership; and
- maintenance cadence.

```text
Good prompt today
      ≠
Reliable configured baseline tomorrow
```

---

# Foundation 2: Configuring Projects

## Four primary mechanisms

| Mechanism | Primary role |
|---|---|
| Project instructions | Workspace behavior |
| Project knowledge | Workspace facts and references |
| Skills | Reusable procedures |
| Project-scoped Memory | Selected continuity |

```text
Behavior   → Project instructions
Facts      → Project knowledge
Procedure  → Skill
Continuity → Project-scoped Memory
```

## Pairing rule

One business need may require several mechanisms because it contains different responsibilities.

```text
Instruction:
Always cite material factual claims.

Knowledge:
Approved sources Claude should cite.
```

```text
Skill:
Status-report procedure.

Knowledge:
Current plan, brand guide, and references.

Memory:
Reviewed preferences and prior Project decisions.
```

Give each responsibility one authoritative home, then pair mechanisms without duplicating authority.

## Memory boundary

```text
Scoped continuity
      ≠
Authorization boundary
      ≠
Confidentiality control
      ≠
System of record
```

Material decisions remain subordinate to approved records, permissions, and human authority.

---

# Foundation 3: Connectors and uploaded knowledge

Connectors provide authorized access to external systems. Uploaded files provide explicit source material for a chat or Project.

Neither mechanism establishes that every accessible item is authoritative, current, in scope, or actionable.

```text
Connected or uploaded
      ≠
Permitted for every task
      ≠
Authoritative
      ≠
Current
      ≠
Authorized for external action
```

## Connector purpose and access

Before enabling a connector, define:

- business purpose;
- intended users;
- connected identity;
- permitted systems, folders, mailboxes, tenants, or repositories;
- read capabilities;
- draft capabilities;
- write or external-action capabilities;
- prohibited or unsupported actions;
- data sensitivity;
- approval boundaries;
- owner;
- review date; and
- revocation conditions.

Use the smallest connector and permission scope that supports the approved workflow.

```text
Connect everything by default
      ≠
Useful knowledge management
```

## Capability register

| Field | Meaning |
|---|---|
| Connector | Exact integration and version |
| Identity | Whose permissions are used |
| Source scope | Accessible systems and records |
| Read tools | Search and retrieval capabilities |
| Draft tools | Proposed-output capabilities |
| Write tools | Create, update, send, publish, or delete capabilities |
| Unsupported actions | Known boundaries |
| Approval boundary | Human confirmation before consequence |
| Error modes | Setup, authentication, permission, scope, timeout, capability |
| Owner and review date | Maintenance responsibility |

Capabilities differ by connector, product surface, administrator settings, and permission configuration.

```text
Mail connector
      ≠
Universal mail capability
```

A connector may search and read, create drafts, or support write tools only when specifically documented and enabled.

## Stage separation

```text
Search or retrieve
      ↓
Read evidence
      ↓
Analyze
      ↓
Draft proposed output
      ↓
Human review and approval
      ↓
Controlled execution, if supported
```

A connector that can draft but not send has reached its designed boundary rather than failed.

## Boundary-aware troubleshooting

Classify failures before escalation:

1. connector not installed or enabled;
2. wrong or expired authentication;
3. insufficient permission;
4. source outside configured scope;
5. connector not loaded for the conversation;
6. unsupported action;
7. missing, renamed, or stale source;
8. external-system failure; or
9. probable product defect.

```text
Unexpected result
      ≠
Product bug
```

The supplied course reports two field-observed cautions:

- an apparently obvious connector-addition path may not be the organization's approved installation path; and
- capability-boundary failures may be mislabeled and routed to the wrong support function.

Treat these as operational cautions, not universal documented behavior. Confirm approved paths and current capabilities with the relevant administrator and official documentation.

---

# Uploaded-knowledge governance

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
- refresh type;
- conflicts;
- replacement; and
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

## Duplicates and supersession

A knowledge base containing several unlabeled versions of the same policy invites obsolete citations and blended requirements.

```text
New source approved
      ↓
Identify replaced source
      ↓
Remove or label superseded version
      ↓
Update source register
      ↓
Run regression questions
      ↓
Record effective date and owner
```

Historical sources may remain when history is part of the use case, but their status must be explicit.

## Synced and static sources

| Refresh type | Maintenance approach |
|---|---|
| Synced source | Monitor upstream ownership, access, and material changes |
| Static upload | Replace manually when the controlling source changes |
| Connector retrieval | Validate permissions, scope, and currency at use time |
| Historical archive | Prevent accidental treatment as current authority |

```text
Connected or synced
      ≠
Reviewed and approved
```

---

# Connector and knowledge register

| ID | Source or connector | Capability | Authority | Scope | Refresh | Owner | Review | Action boundary |
|---|---|---|---|---|---|---|---|---|
| C-001 | Approved mail connector | Search, read, draft | Evidence source | Named mailbox | Live | Workspace owner | Quarterly | No send |
| K-001 | Current policy | Read | Controlling | Defined use case | Static | Policy owner | On change | Reference only |
| K-002 | Prior policy | Read | Superseded | Historical | Archive | Policy owner | Annual | Never current guidance |

This register prevents connector names and file availability from becoming implicit assumptions.

---

# Worked policy-brief example

A fictional compliance team prepares weekly policy-change briefs.

## Connectors

- read-only access to an approved repository;
- email search for messages from the policy owner;
- no authority to send, publish, or modify source records.

## Uploaded knowledge

- current briefing template;
- approved terminology guide;
- current review checklist;
- superseded policies removed or explicitly labeled historical.

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
- offboarding and revocation.

---

# Common failure modes

| Failure | Repair |
|---|---|
| Connector availability treated as authority | Classify source ownership, version, and scope |
| Capability assumed from connector name | Maintain a tool-level capability contract |
| Everything connected by default | Apply least privilege and enable only relevant tools |
| Static upload treated as live | Record refresh type and replacement trigger |
| Duplicate versions retained without status | Remove, archive, or label superseded copies |
| Unsupported action reported as a bug | Check setup, authentication, permission, scope, loading, and capability first |
| Draft directly triggers external consequence | Add qualified review and approval before execution |

---

# Integrated configuration protocol

```text
1. Define the bounded purpose and users
2. Classify behavior, facts, procedures, continuity, access, exact controls, and state
3. Place each concern in the correct configuration mechanism
4. Select the minimum required connectors and source scope
5. Record connector identity, capabilities, and unsupported actions
6. Establish source authority, freshness, scope, sensitivity, and conflict rules
7. Curate uploaded knowledge and remove or label superseded versions
8. Separate retrieve, draft, approve, and execute
9. Test successful, denied, stale, conflicting, and unsupported cases
10. Version and approve the configuration
11. Monitor sources, permissions, capabilities, and operational dependency
12. Update, revoke, roll back, or retire when conditions change
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Configuring Projects](lessons/02-configuring-projects.md)
- [Connectors and Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)
- [Connectors and Uploaded Knowledge prompts](../../prompts/module-05/03-connectors-uploaded-knowledge-prompts.md)

## Engineering patterns

- [Project Configuration Slot Selection Pattern](../../patterns/project-configuration-slot-selection-pattern.md)
- [Connector and Knowledge Boundary Pattern](../../patterns/connector-and-knowledge-boundary-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

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

# Completion criteria

- [x] I completed the Module 5 introduction.
- [x] I completed Configuring Projects.
- [x] I completed Connectors and Uploaded Knowledge.
- [ ] I can distinguish behavior, facts, procedures, continuity, access, exact controls, and state.
- [ ] I can apply the Project configuration pairing rule.
- [ ] I can distinguish connector access from source authority.
- [ ] I can create a connector capability contract.
- [ ] I can separate retrieve, draft, approve, and execute stages.
- [ ] I can classify connector failures before escalation.
- [ ] I can curate uploaded knowledge and remove or label superseded sources.
- [ ] I can distinguish synced sources from static snapshots.
- [ ] I can apply least privilege and define revocation.
- [ ] I can keep credentials and secrets outside prompts and repositories.
- [ ] I can design durable instructions with clear scope and precedence.
- [ ] I can test, version, roll back, and retire configurations.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential emails, private Drive content, connector identifiers, credentials, internal policies, private knowledge sources, proprietary instructions, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Source note

The Connectors and Uploaded Knowledge course material was supplied on August 3, 2026. Product capabilities and interfaces can change. Current official documentation and organizational policy control if they conflict with course or repository material.
