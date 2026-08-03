# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — teaching, quiz, and takeaways are complete. Module Complete remains open. Module 4's final completion checkpoint also remains open.

## Module thesis

> Configure recurring behavior, knowledge, procedures, continuity, and access once; benefit across repeated conversations; then maintain the environment so it remains accurate, authorized, scoped, testable, and owned.

```text
Using Claude
      ↓
Current prompt and individual judgment

Operating Claude
      ↓
Configured baseline
+ governed knowledge
+ reusable procedures
+ scoped continuity and access
+ precise persistent instructions
+ human and technical controls
+ lifecycle maintenance
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Configuring Projects](lessons/02-configuring-projects.md)
- [x] [03. Connectors & Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)
- [x] [04. System-Level Instructions That Stick](lessons/04-system-level-instructions-that-stick.md)
- [x] [05. Maintaining Configurations](lessons/05-maintaining-configurations.md)
- [x] 06. Module 5 Quiz
  - [x] [Quiz — Full marks, 5/5](lessons/06a-module-5-quiz.md)
  - [x] [Key Takeaways](lessons/06b-key-takeaways.md)
- [ ] 07. Module Complete

---

# Completion record

```text
Module 5 teaching sections: Complete
Module 5 quiz:              Full marks — 5 of 5
Key takeaways:              Complete
Module complete:            Open
```

---

# Five durable takeaways

## 1. Configuration is leverage

A configured environment reduces repeated setup and turns individual prompting habits into visible, reusable team expectations.

```text
Set up once
      ↓
Use repeatedly
      ↓
Review and maintain
      ↓
Continue to trust
```

Configuration improves consistency and inspectability, but it does not guarantee factual accuracy or replace qualified review.

## 2. Match each need to the right mechanism

| Need | Primary home |
|---|---|
| Immediate task | Current request |
| Project behavior | Project instructions |
| Project facts and references | Project knowledge |
| Reusable procedure | Skill |
| Selected continuity | Project-scoped Memory |
| External source access | Connector |
| Exact rule or authorization | Deterministic control |
| Approved durable state | System of record |

```text
Behavior → instructions
Facts → knowledge
Procedure → Skill
Continuity → Memory
Access → connector
Authority → deterministic and human controls
```

Give each responsibility one authoritative home, then pair mechanisms when one business need contains several responsibility types.

```text
Scoped continuity
      ≠
Authoritative record
      ≠
Permission boundary
```

## 3. Know each connector's boundary

```text
Connector available
      ≠
Source accessible
      ≠
Source authoritative
      ≠
Action supported
      ≠
Action approved
```

Maintain a connector capability contract with identity, source scope, read and draft tools, write or external-action tools, unsupported actions, approval boundaries, owner, review date, and revocation path.

```text
Retrieve
  ↓
Read
  ↓
Analyze
  ↓
Draft
  ↓
Human review
  ↓
Approval
  ↓
Controlled execution, if supported
```

A stronger model does not expand connector permissions or unsupported capabilities.

## 4. Write instructions precisely

A durable instruction defines:

| Element | Question |
|---|---|
| Trigger | When does the rule apply? |
| Required behavior | What should Claude do? |
| Evidence boundary | What may it rely on? |
| Failure behavior | What happens when the requirement cannot be met? |
| Observable output | How can a reviewer verify it? |

```text
Vague:
Write clear and professional notes.

Precise:
Record each decision as a separate bullet.
List every action as owner — due date — status.
Label missing owners `owner TBD`.
Put unresolved questions in a final section.
```

Apply the two-reader test: two competent readers should interpret a material instruction the same way.

```text
Instruction written
      ≠
Instruction precise
      ≠
Instruction technically enforced
```

High-stakes guardrails still require permissions, deterministic checks, controlled tools, human review, and approval gates.

## 5. Maintain configurations or quality decays

```text
Configured baseline
      ↓
Process, source, permission, and personnel change
      ↓
Silent configuration drift
      ↓
Output quality degradation
```

Use recurring and event-triggered reviews. A monthly review is a practical baseline for active Projects, adjusted for change rate and consequence.

Review:

- instructions for outdated terminology, process, format, evidence rules, and reviewers;
- knowledge for authority, freshness, duplicates, supersession, scope, and ownership;
- Skills for owner, distribution, version, trigger behavior, dependencies, tests, and rollback;
- connectors for identity, permissions, tools, business need, offboarding, and revocation; and
- Memory for accuracy, relevance, and proper authority placement.

```text
No visible error
      ≠
Configuration still correct
```

---

# Module 5 quiz result

```text
Full marks — 5 of 5
```

The original public-safe quiz demonstrated command of:

1. choosing Skills for repeatable procedures;
2. separating sensitive workstreams into bounded Projects;
3. respecting connector capability boundaries;
4. converting vague instructions into observable rules; and
5. diagnosing stale instructions and Memory as configuration drift.

## Quiz shortcut

```text
Repeatable multi-step method → Skill
Different sensitive workstream → separate bounded Project
Connector cannot perform action → capability boundary
Vague standing rule → precise observable instruction
Output drifts without prompt change → inspect configuration
```

---

# Integrated configuration review

Before relying on a configured workspace, ask:

```text
1. Is the Project purpose still current?
2. Is every need in the correct mechanism?
3. Are sources authoritative, current, and in scope?
4. Are connector capabilities and permissions explicit?
5. Are standing instructions precise and testable?
6. Are consequential actions protected by real controls?
7. Are Skills, Memory, and access still accurate?
8. Is ownership and the next review date recorded?
```

A failed question identifies the next maintenance or redesign task.

---

# Configuration maintenance protocol

```text
1. Inventory instructions, knowledge, Skills, connectors, and Memory
2. Assign owners, versions, review dates, and tests
3. Review on cadence and after material events
4. Compare configuration with current process, sources, people, and access
5. Classify drift and downstream impact
6. Edit, replace, disable, revoke, reset, roll back, or retire
7. Preserve approved information before destructive changes
8. Rerun representative and adversarial tests
9. Approve, release, and monitor
10. Record the result and next review date
```

---

# Current module resources

## Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Configuring Projects](lessons/02-configuring-projects.md)
- [Connectors and Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)
- [System-Level Instructions That Stick](lessons/04-system-level-instructions-that-stick.md)
- [Maintaining Configurations](lessons/05-maintaining-configurations.md)
- [Module 5 Quiz](lessons/06a-module-5-quiz.md)
- [Module 5 Key Takeaways](lessons/06b-key-takeaways.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)
- [Connectors and Uploaded Knowledge prompts](../../prompts/module-05/03-connectors-uploaded-knowledge-prompts.md)
- [System-Level Instructions prompts](../../prompts/module-05/04-system-level-instructions-prompts.md)
- [Maintaining Configurations prompts](../../prompts/module-05/05-maintaining-configurations-prompts.md)
- [Module 5 quiz and remediation prompts](../../prompts/module-05/06a-module-5-quiz-prompts.md)
- [Module 5 Key Takeaways prompts](../../prompts/module-05/06b-key-takeaways-prompts.md)

## Engineering patterns

- [Project Configuration Slot Selection Pattern](../../patterns/project-configuration-slot-selection-pattern.md)
- [Connector and Knowledge Boundary Pattern](../../patterns/connector-and-knowledge-boundary-pattern.md)
- [Persistent Instruction Precision Pattern](../../patterns/persistent-instruction-precision-pattern.md)
- [Configuration Maintenance Lifecycle Pattern](../../patterns/configuration-maintenance-lifecycle-pattern.md)

## Extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Repeated setup in every chat            → configure a stable baseline
Multi-step reusable procedure           → Skill
Project-specific source material        → Project knowledge
Standing behavior rule                  → Project instruction
Selected prior context                  → scoped Memory
External source or action               → connector with defined capability
Vague instruction                       → make observable and testable
Quiet recurring regression              → inspect configuration drift
Old source or stakeholder persists      → update knowledge or Memory
Connector cannot perform action         → respect the capability boundary
```

For Module 5 scenarios:

1. identify whether the need is behavior, fact, procedure, continuity, access, authority, or state;
2. choose the smallest correct mechanism;
3. preserve one authoritative home;
4. distinguish access from authority;
5. document connector capabilities and unsupported actions;
6. make persistent instructions precise and observable;
7. pair guidance with enforceable controls;
8. inspect configuration before blaming prompting or model tier;
9. maintain on cadence and after material events; and
10. edit, replace, revoke, reset, roll back, or retire according to the defect.

---

# Completion criteria

- [x] I completed all Module 5 teaching sections.
- [x] I completed the Module 5 quiz with full marks, 5/5.
- [x] I completed the Module 5 takeaways.
- [ ] I can place behavior, facts, procedures, continuity, access, controls, and state correctly.
- [ ] I can create connector and source capability registers.
- [ ] I can curate uploaded knowledge and manage supersession.
- [ ] I can write precise persistent instructions and apply the two-reader test.
- [ ] I can distinguish instructions from enforceable controls.
- [ ] I can establish recurring and event-triggered maintenance.
- [ ] I can version and test instructions, knowledge, Skills, connectors, and Memory.
- [ ] I can choose edit, replace, revoke, reset, rollback, or retirement appropriately.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Product-verification note

This module was reviewed against official Anthropic Help Center material available on August 3, 2026. Current documentation describes Projects as self-contained workspaces with knowledge and instructions, Skills as reusable procedures that load when relevant, connectors as permission-bound integrations with connector-specific capabilities, and project memory as a separate continuity space. Product availability and behavior can change, and current official documentation controls.

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential instructions, connectors, credentials, private knowledge, Skill packages, Memory exports, internal policies, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, financial, or operational advice.