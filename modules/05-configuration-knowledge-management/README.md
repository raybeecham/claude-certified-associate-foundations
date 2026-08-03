# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** Roadmap staged — Module 4's final completion checkpoint remains open. No Module 5 lesson is marked complete yet.

## Why this domain matters

A useful Claude interaction can depend heavily on configuration that the user no longer sees in the immediate prompt.

Projects, uploaded knowledge, connectors, reusable instructions, and maintained procedures can make work more consistent. They can also become hidden operational dependencies when their ownership, authority, scope, freshness, access, and maintenance rules are unclear.

```text
Business or workflow need
        ↓
Configuration boundary
        ↓
Project instructions and knowledge
        ↓
Connectors and uploaded sources
        ↓
Reusable instructions and procedures
        ↓
Maintenance, testing, and change control
        ↓
Reliable configured workspace
```

> **Module thesis:** Configuration should make correct behavior easier to repeat without hiding stale knowledge, conflicting instructions, excessive access, or unowned dependencies.

---

# Course-aligned roadmap

- [ ] 01. Module Introduction
- [ ] 02. Configuring Projects
- [ ] 03. Connectors & Uploaded Knowledge
- [ ] 04. System-Level Instructions That Stick
- [ ] 05. Maintaining Configurations
- [ ] 06. Module 5 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 07. Module Complete

No course lesson file is marked complete until the corresponding preparation-course material is supplied and converted into original public-safe study content.

## Learning progression

```text
Understand configuration as part of the workflow
              ↓
Configure a Project around a bounded purpose
              ↓
Select connectors and uploaded knowledge deliberately
              ↓
Design durable instructions with clear scope and precedence
              ↓
Test, maintain, version, and retire configurations
              ↓
Demonstrate configuration judgment under quiz conditions
```

---

# Module 4 to Module 5 bridge

Module 4 mapped who or what should perform each workflow responsibility.

```text
Workflow stage
      ↓
Model / deterministic / tool / storage / human owner
      ↓
Validation, review, approval, and recovery
```

Module 5 asks how the model-facing configuration and knowledge environment should be established and maintained.

```text
Approved workflow responsibility
      ↓
Configured instructions and knowledge
      ↓
Scoped access and retrieval
      ↓
Source authority, freshness, and conflict handling
      ↓
Testing and lifecycle maintenance
```

The transition question is:

> What should Claude consistently know and do in this workspace, where should that behavior live, and how will the configuration remain trustworthy over time?

---

# Durable engineering foundation

The repository already contains extended configuration and knowledge-management material. It will be mapped to the supplied course sections as they arrive.

## Configuration layers

A reliable design separates several different concerns:

| Layer | Purpose |
|---|---|
| User request | The immediate task and current constraints |
| Project instructions | Durable behavior for one bounded workspace |
| Project knowledge | Project-specific source material and background |
| Skill or reusable procedure | Repeatable method, template, checklist, script, or resource package |
| Connector | Controlled access to an external system or repository |
| Uploaded file | Explicit source supplied for the current work or workspace |
| Memory or continuity feature | Selective cross-conversation continuity where supported and appropriate |
| Deterministic control | Rules, authorization, validation, routing, and exact calculations outside prompt text |

```text
Immediate task                    → current request
Workspace-specific behavior       → Project instructions
Workspace-specific evidence       → Project knowledge
Reusable procedure                → Skill
External system access            → connector
Exact rule or authorization       → deterministic control
```

Configuration layers should not be treated as interchangeable.

## Project configuration

A Project should have a bounded purpose and an explicit operating contract.

Define:

- project objective;
- intended users;
- approved use cases;
- prohibited uses;
- standing instructions;
- knowledge sources;
- source authority order;
- expected output formats;
- uncertainty behavior;
- review and approval requirements;
- data-handling constraints;
- owner;
- review date; and
- retirement conditions.

A Project should not become an unbounded container for every document and task in a department.

## Knowledge-source register

Every maintained source should have visible governance metadata.

| Field | Purpose |
|---|---|
| Source ID | Stable reference |
| Title and location | Discoverability |
| Source type | Policy, procedure, reference, data, example, template |
| Authority | Controlling, advisory, historical, draft, superseded |
| Owner | Person or function responsible for the source |
| Effective date | When it became applicable |
| Review or expiration date | Freshness control |
| Scope | Users, regions, systems, decisions, or cases covered |
| Sensitivity | Access and handling requirement |
| Conflicts | Known disagreements with other sources |
| Replacement | New controlling source when superseded |

```text
Available source
      ≠
Authorized source
      ≠
Controlling source
      ≠
Current source
```

## Connectors and uploaded knowledge

Connector or file availability does not establish that every retrieved item should influence the answer.

A retrieval design should define:

- which systems are permitted;
- which identities and permissions apply;
- which source types are authoritative;
- what date or version limits apply;
- what minimum evidence is required;
- how conflicts are surfaced;
- how sensitive fields are handled;
- what results may be retained;
- what actions are read-only versus state-changing; and
- what human approval is required.

Use the smallest relevant and permitted source set.

```text
More connected data
      ≠
Better context
```

## Instruction design and precedence

Durable instructions should be:

- specific enough to guide behavior;
- narrow enough to avoid unrelated interference;
- consistent with higher-authority policy and platform controls;
- explicit about source boundaries and uncertainty;
- testable through representative scenarios;
- versioned and owned; and
- separated from secrets or sensitive credentials.

Potential instruction conflicts should be visible rather than silently reconciled.

```text
Instruction present
      ≠
Instruction appropriate
      ≠
Instruction consistently enforceable
```

Prompts and instructions cannot replace identity, authorization, data isolation, professional authority, or external approval controls.

## Configuration maintenance

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
Review sources and behavior
  ↓
Update, rollback, or retire
```

Maintain:

- configuration version;
- change owner;
- reason for change;
- affected workflows;
- source additions and removals;
- instruction changes;
- test cases and results;
- reviewer and approval;
- rollout date;
- rollback path;
- known limitations; and
- next review date.

## Conflict and freshness handling

When sources disagree:

1. identify the exact conflicting claims;
2. compare authority, scope, effective date, and version;
3. determine whether one source supersedes another;
4. preserve unresolved conflict when authority is unclear;
5. ask the authorized owner to resolve it; and
6. record the resolution and affected configuration.

When a source is stale or outside scope, exclude it or label the limitation explicitly.

## Access and secret boundaries

Apply least privilege to connectors and knowledge access.

- Grant only the systems, folders, records, and actions required.
- Keep credentials and secrets out of prompts, instructions, repositories, and uploaded knowledge.
- Separate read access from write or external-action authority.
- Review inherited access and shared-workspace exposure.
- Define offboarding and revocation behavior.
- Retain audit evidence where required.

## Caching and reusable context

Caching can reduce repeated processing for stable reusable prefixes, but it does not solve:

- source staleness;
- excessive access;
- instruction conflict;
- incorrect business rules;
- sensitive-data handling;
- invalid assumptions; or
- missing human approval.

Use caching only when the content is sufficiently stable, reusable, permitted, and appropriately invalidated.

---

# Learning objectives

By the end of this module, you should be able to:

- explain why configuration is part of workflow design rather than a convenience layer;
- configure a Project around a bounded purpose and use case;
- distinguish Project instructions, Project knowledge, Skills, connectors, uploaded files, and deterministic controls;
- define a governed source register;
- select authoritative, current, relevant, and permitted knowledge;
- apply least privilege to connectors and retrieval;
- separate read access from write or external-action authority;
- design durable instructions with clear scope and conflict behavior;
- recognize that instructions cannot enforce identity, authorization, or professional approval;
- test configuration behavior with representative and adversarial scenarios;
- resolve or surface source conflicts;
- detect stale, superseded, or out-of-scope knowledge;
- version, approve, monitor, update, rollback, and retire configurations;
- keep secrets and credentials out of prompts and knowledge stores; and
- use caching only for appropriate stable context.

---

# Existing module resources

The repository already contains extended practice material that remains available while the course-aligned lessons are developed.

- [notes.md](notes.md): Configuration, source governance, access, and maintenance concepts
- [lab.md](lab.md): Applied configuration and knowledge-management exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

Course-aligned lessons and Module 5 prompt notebooks will be added as each supplied section is completed.

---

# Exam lens

Configuration scenarios often test whether the learner places content in the correct layer and maintains appropriate authority and access boundaries.

```text
One bounded workspace needs stable behavior → Project instructions
Workspace needs approved source material     → Project knowledge
Procedure should work across contexts        → Skill
Current external information is needed       → connector or retrieval path
Exact authorization or fixed rule            → deterministic control
Source is stale or conflicting               → surface, resolve, or exclude
More files are available                     → still select minimum relevant evidence
Secret appears in instructions                → remove and use approved secret handling
```

For scenario questions:

1. identify the workspace purpose and user;
2. distinguish instruction, knowledge, procedure, access, and authority;
3. select the smallest relevant configuration layer;
4. establish source authority, scope, and freshness;
5. apply least privilege;
6. keep secrets outside prompt and knowledge content;
7. define conflict and uncertainty behavior;
8. test representative and adversarial cases;
9. version and approve material changes; and
10. define monitoring, rollback, and retirement.

---

# Completion criteria

- [ ] I completed the Module 5 introduction.
- [ ] I can configure a Project around a bounded purpose.
- [ ] I can distinguish Project instructions, Project knowledge, Skills, connectors, and uploaded files.
- [ ] I can build and maintain a source register.
- [ ] I can select authoritative, current, relevant, and permitted evidence.
- [ ] I can resolve or surface conflicting sources.
- [ ] I can apply least privilege to knowledge and connector access.
- [ ] I can keep credentials and secrets outside prompts and repositories.
- [ ] I can design durable instructions with clear scope and precedence.
- [ ] I can test and maintain configuration behavior.
- [ ] I can version, approve, roll back, and retire configurations.
- [ ] I can explain when retrieval and caching help and what they do not solve.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential configuration files, connector identifiers, credentials, internal policies, private knowledge sources, proprietary instructions, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Official reading

Product capabilities and recommendations can change. Verify current official documentation before relying on implementation-specific behavior.

- [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Context management](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)
