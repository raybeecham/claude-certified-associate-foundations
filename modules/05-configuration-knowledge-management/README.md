# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — teaching and quiz are complete. Takeaways and Module Complete remain open. Module 4's final completion checkpoint remains open.

## Module thesis

> Set up the right context, instructions, procedures, continuity, and access once; benefit across repeated conversations; then maintain the configuration so it remains accurate, authorized, scoped, testable, and owned.

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
- [ ] 06. Module 5 Quiz
  - [x] [Quiz — Full marks, 5/5](lessons/06a-module-5-quiz.md)
  - [ ] Takeaways
- [ ] 07. Module Complete

---

# Completion record

```text
Module 5 teaching sections: Complete
Module 5 quiz:              Full marks — 5 of 5
Key takeaways:              Open
Module complete:            Open
```

---

# Integrated configuration framework

## 1. Put each need in the correct layer

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

Give each responsibility one authoritative home, then pair mechanisms when one need contains several responsibility types.

## 2. Bound Projects and continuity deliberately

Use a separate bounded Project when workstreams materially differ in purpose, users, sources, permissions, disclosure boundaries, or continuity.

```text
Scoped continuity
      ≠
Authorization boundary
      ≠
Confidentiality control
      ≠
System of record
```

Project separation supports contextual scope. It does not replace identity, permissions, disclosure review, or authoritative records.

## 3. Govern connectors and uploaded knowledge

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

Every connector needs a capability contract covering:

- connected identity;
- source scope;
- read and retrieval tools;
- draft capabilities;
- write or external-action capabilities;
- unsupported actions;
- approval boundaries;
- owner;
- review date; and
- revocation.

```text
Retrieve
  ↓
Read
  ↓
Analyze
  ↓
Draft
  ↓
Human review and approval
  ↓
Controlled execution, if supported
```

Every maintained source needs owner, authority, scope, effective and review dates, version, refresh type, conflicts, replacement, sensitivity, and permitted use.

Remove, archive, or label duplicate and superseded sources. Distinguish synced sources, static uploads, live retrieval, and historical archives.

## 4. Write persistent instructions that are observable

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
List each action as owner — due date — status.
Label missing owners `owner TBD`.
Put unresolved questions in a final section.
```

Apply the two-reader test: two competent readers should interpret a material instruction the same way.

```text
Instruction says `do not send`
      ≠
Send capability technically disabled
```

Persistent guidance does not replace identity, authorization, permissions, deterministic controls, professional approval, or external-action restrictions.

## 5. Maintain the configured baseline

```text
Configured baseline
      ↓
Repeated use and environmental change
      ↓
Configuration drift
      ↓
Scheduled review, repair, rollback, or retirement
```

Use recurring and event-triggered reviews.

| Change profile | Example cadence |
|---|---|
| High-change or high-consequence | Weekly or event-triggered |
| Active recurring Project | Monthly |
| Stable reference workspace | Quarterly |
| Archived workspace | Annual review or retirement |

Review instructions, knowledge, Skills, connectors, Memory, owners, permissions, tests, rollback, and retirement conditions.

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

## Quiz reasoning sequence

```text
Identify the configuration concern
      ↓
Select the correct layer or component
      ↓
Check authority, scope, precision, and capability
      ↓
Identify what remains uncontrolled or stale
      ↓
Choose the smallest responsible repair
      ↓
Reject stronger-model and one-time-prompt distractors
```

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

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)
- [Connectors and Uploaded Knowledge prompts](../../prompts/module-05/03-connectors-uploaded-knowledge-prompts.md)
- [System-Level Instructions prompts](../../prompts/module-05/04-system-level-instructions-prompts.md)
- [Maintaining Configurations prompts](../../prompts/module-05/05-maintaining-configurations-prompts.md)
- [Module 5 quiz and remediation prompts](../../prompts/module-05/06a-module-5-quiz-prompts.md)

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
Multi-step procedure                    → Skill
Workspace-specific behavior             → Project instructions
Stable reference                         → Project knowledge
Evolving continuity                      → scoped Memory
Distinct sensitive workstream            → separate bounded Project
Connector cannot perform requested action → respect capability contract
Vague instruction                        → define observable behavior
Output drifts without prompt change       → inspect stale configuration
```

For Module 5 scenarios:

1. identify the configuration concern;
2. select the smallest correct layer;
3. separate access from authority;
4. respect connector and action boundaries;
5. make persistent behavior precise and testable;
6. keep sensitive workstreams bounded;
7. maintain authoritative sources and procedures;
8. detect quiet drift across all components;
9. pair natural-language guidance with enforceable controls; and
10. choose the smallest sufficient repair.

---

# Completion criteria

- [x] I completed all Module 5 teaching sections.
- [x] I completed the Module 5 quiz with full marks, 5/5.
- [ ] I completed the Module 5 takeaways.
- [ ] I can place behavior, facts, procedures, continuity, access, controls, and state correctly.
- [ ] I can separate sensitive workstreams and define Project boundaries.
- [ ] I can create connector and source capability registers.
- [ ] I can curate uploaded knowledge and manage supersession.
- [ ] I can write precise persistent instructions and apply the two-reader test.
- [ ] I can distinguish instructions from enforceable controls.
- [ ] I can establish recurring and event-triggered maintenance.
- [ ] I can version and test instructions, knowledge, Skills, connectors, and Memory.
- [ ] I can choose edit, replace, revoke, reset, rollback, or retirement appropriately.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential instructions, connectors, credentials, private knowledge, Skill packages, Memory exports, internal policies, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, financial, or operational advice.