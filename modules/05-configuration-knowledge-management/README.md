# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — Module 5 is the active module. Module 4's final completion checkpoint remains open.

## Module thesis

> Set up the right context, instructions, procedures, and access once; benefit across repeated conversations; then maintain the configuration so it remains accurate, authorized, scoped, and owned.

```text
Using Claude
      ↓
Current prompt and individual judgment

Operating Claude
      ↓
Configured baseline
+ governed knowledge
+ reusable procedures
+ scoped access
+ human controls
+ lifecycle maintenance
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [ ] 02. Configuring Projects
- [ ] 03. Connectors & Uploaded Knowledge
- [ ] 04. System-Level Instructions That Stick
- [ ] 05. Maintaining Configurations
- [ ] 06. Module 5 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 07. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Module 4 to Module 5 bridge

Module 4 assigned workflow responsibilities to models, code, tools, storage, and humans.

Module 5 asks how the model-facing environment should be configured and maintained so those assignments remain repeatable.

```text
Approved workflow responsibility
      ↓
Configured instructions and knowledge
      ↓
Scoped access and reusable procedures
      ↓
Source authority, freshness, and conflict handling
      ↓
Testing and maintenance
      ↓
Reliable configured workspace
```

The transition question is:

> What should Claude consistently know and do in this workspace, where should that behavior live, and how will the configuration remain trustworthy over time?

---

# Foundation 1: Using versus operating Claude

## Personal use

A person supplies the context, prompt, sources, format, and review decisions for the current conversation.

## Operating model

A team maintains an approved starting environment containing:

- bounded purpose;
- intended users;
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

## Team capability

Configuration turns individual prompting habits and unstated expertise into visible, reusable expectations.

```text
Individual knowledge and prompting habits
      ↓
Explicit instructions, sources, procedures, and controls
      ↓
More consistent team capability
```

Consistency does not require identical wording. It requires consistent source boundaries, requirements, output contracts, uncertainty behavior, and review obligations.

---

# Foundation 2: Configuration layers

| Layer | Primary role |
|---|---|
| Current request | Immediate task and current constraints |
| Project instructions | Durable behavior for one bounded workspace |
| Project knowledge | Workspace-specific evidence and background |
| Skill or reusable procedure | Repeatable method, checklist, template, script, or resource |
| Connector | Controlled access to an external system |
| Uploaded file | Explicit source supplied for current work or workspace |
| Scoped memory | Selective continuity where supported and appropriate |
| Deterministic control | Authorization, validation, routing, and exact rules outside prompt text |

```text
Immediate task              → current request
Workspace behavior          → Project instructions
Workspace evidence          → Project knowledge
Reusable procedure          → Skill
External system access      → connector
Explicit source             → uploaded file
Selective continuity        → scoped memory
Authorization or exact rule → deterministic control
```

Configuration layers are not interchangeable.

Common errors include:

- placing temporary details into permanent instructions;
- placing reusable procedures only in one Project;
- treating connector access as source authority;
- storing secrets in instructions or knowledge;
- using memory as a system of record;
- encoding authorization only in natural language; and
- adding every available document instead of the minimum relevant set.

```text
Available context
      ≠
Appropriate configuration
```

---

# Foundation 3: The configured baseline

A bounded configuration should define:

- purpose;
- users;
- approved use cases;
- prohibited uses;
- instructions;
- knowledge categories;
- source authority order;
- connector scope;
- output contract;
- uncertainty behavior;
- review and approval gates;
- data-handling constraints;
- owner;
- version;
- review cadence;
- rollback path; and
- retirement conditions.

The baseline should answer:

```text
What is this workspace for?
Who may use it?
What may Claude know?
What should Claude do consistently?
What must remain human or deterministic?
Which sources control?
Who reviews the result?
Who maintains the configuration?
```

A Project should not become an unbounded container for every document and task in a department.

---

# Foundation 4: Knowledge governance

## Source register

Every maintained source should have visible metadata.

| Field | Purpose |
|---|---|
| Source ID | Stable reference |
| Title and location | Discoverability |
| Source type | Policy, procedure, data, reference, template, example |
| Authority | Controlling, advisory, draft, historical, superseded |
| Owner | Responsible person or function |
| Effective date | Applicability start |
| Review or expiration date | Freshness control |
| Scope | Users, regions, systems, decisions, or cases covered |
| Sensitivity | Access and handling requirement |
| Conflicts | Known disagreements |
| Replacement | Controlling successor when superseded |

```text
Available source
      ≠
Authorized source
      ≠
Controlling source
      ≠
Current source
```

## Conflict handling

When sources disagree:

1. identify the exact conflict;
2. compare authority, scope, effective date, and version;
3. determine whether one source supersedes another;
4. preserve the unresolved conflict when authority is unclear;
5. obtain resolution from the authorized owner; and
6. update the register and affected configuration.

---

# Foundation 5: Connectors, files, access, and secrets

Connector or file availability does not establish that every retrieved item should affect the answer.

Define:

- permitted systems;
- identity and permissions;
- authoritative source types;
- date and version limits;
- minimum evidence;
- conflict behavior;
- sensitive-field handling;
- retention rules;
- read-only versus state-changing access; and
- required human approval.

```text
More connected data
      ≠
Better context
```

Apply least privilege:

- grant only required systems, folders, records, and actions;
- separate read access from write or external-action authority;
- review inherited access and shared-workspace exposure;
- define revocation and offboarding; and
- retain audit evidence where required.

Keep credentials and secrets out of prompts, instructions, repositories, uploaded knowledge, and source files.

---

# Foundation 6: Scoped memory and continuity

Continuity can reduce repeated explanation but should remain selective.

Ask:

- Is the information stable?
- Is retention appropriate?
- Is scope clear?
- Is it useful across future work?
- Can the user inspect and correct it?
- Would staleness create a material error?
- Does an authoritative system belong elsewhere?

Memory does not replace:

- Project knowledge;
- source provenance;
- a system of record;
- workflow state;
- authorization;
- access control; or
- professional approval.

```text
Helpful continuity
      ≠
Authoritative record
```

---

# Foundation 7: Maintenance lifecycle

Configuration is a lifecycle, not a one-time setup.

```text
Design
  ↓
Test
  ↓
Approve
  ↓
Release
  ↓
Monitor
  ↓
Review instructions, sources, access, and behavior
  ↓
Update, roll back, or retire
```

Maintain:

- owner;
- purpose;
- users;
- version;
- effective date;
- source and instruction inventory;
- connector and access inventory;
- known limitations;
- test suite and results;
- last and next review date;
- rollback path; and
- retirement conditions.

```text
Configuration created
      ≠
Configuration governed
```

## Common decay modes

- stale standing instruction;
- superseded knowledge;
- outdated Skill or template;
- excessive connector access;
- unrelated files accumulating in a Project;
- missing source owner;
- unstaffed review gate;
- unsupported operational dependency; and
- ceremonial maintenance with no recorded result.

---

# Practical operating example

A fictional team creates recurring policy briefings.

## Weak model

Each analyst uses a blank chat, chooses different sources, applies different cutoff dates, and remembers different review steps.

## Configured model

The team maintains:

- a bounded briefing Project;
- approved source categories and authority order;
- standing instructions for cutoff date, citation, uncertainty, and format;
- a reusable briefing procedure;
- read-only connector access to approved repositories;
- a review gate before distribution;
- a source register; and
- a monthly configuration review.

```text
Configured baseline
      +
Current task inputs
      +
Human review
      ↓
More consistent recurring output
```

Configuration does not guarantee factual accuracy. It makes the expected process more repeatable, inspectable, and maintainable.

---

# Operating principles

1. **Configure stable recurring requirements, not every temporary preference.**
2. **Keep evidence and procedure distinct.**
3. **Make hidden dependencies visible.**
4. **Apply least privilege.**
5. **Keep secrets outside prompt content.**
6. **Treat maintenance as planned work.**
7. **Version and test material changes.**
8. **Roll back or retire configurations that no longer serve their purpose.**

---

# Integrated configuration protocol

```text
1. Define the bounded purpose and users
2. Identify recurring behavior, evidence, procedures, and access
3. Place each concern in the correct configuration layer
4. Establish source authority, freshness, and conflict rules
5. Apply least privilege and separate read from action authority
6. Define uncertainty, output, review, and approval behavior
7. Test representative and adversarial cases
8. Approve and version the configuration
9. Monitor behavior, sources, access, and operational dependency
10. Review on cadence and after material events
11. Update, roll back, or retire
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)

## Existing extended practice

- [notes.md](notes.md): Configuration, source governance, access, and maintenance concepts
- [lab.md](lab.md): Applied configuration and knowledge-management exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

---

# Exam lens

```text
One bounded workspace needs stable behavior → Project instructions
Workspace needs approved evidence           → Project knowledge
Procedure should work across contexts        → Skill
Current external information is needed       → connector or retrieval
Exact authorization or fixed rule            → deterministic control
Source is stale or conflicting               → surface, resolve, or exclude
More files are available                     → still select minimum relevant evidence
Secret appears in instructions                → remove and use approved secret handling
Configuration has no owner or review date     → not governed
Memory is treated as official record          → move authority to system of record
```

For introductory scenarios:

1. distinguish using from operating Claude;
2. identify the bounded workspace purpose;
3. place instructions, evidence, procedures, access, continuity, and authority correctly;
4. establish source authority and freshness;
5. apply least privilege;
6. keep secrets outside prompts and knowledge;
7. define review and approval gates;
8. test representative behavior;
9. assign ownership and maintenance cadence; and
10. define rollback and retirement.

---

# Completion criteria

- [x] I completed the Module 5 introduction.
- [ ] I can explain the difference between using and operating Claude.
- [ ] I can explain how configuration creates leverage and team consistency.
- [ ] I can configure a Project around a bounded purpose.
- [ ] I can distinguish Project instructions, Project knowledge, Skills, connectors, uploaded files, memory, and deterministic controls.
- [ ] I can build and maintain a source register.
- [ ] I can select authoritative, current, relevant, and permitted evidence.
- [ ] I can resolve or surface conflicting sources.
- [ ] I can apply least privilege to connector and knowledge access.
- [ ] I can keep credentials and secrets outside prompts and repositories.
- [ ] I can design durable instructions with clear scope and precedence.
- [ ] I can test and maintain configuration behavior.
- [ ] I can version, approve, roll back, and retire configurations.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential configuration files, connector identifiers, credentials, internal policies, private knowledge sources, proprietary instructions, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Source note

The Module 5 introduction was supplied on August 3, 2026. Product capabilities, terms, policies, and documentation can change. Current official documentation controls if it conflicts with course or repository material.
