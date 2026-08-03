# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — all teaching sections are complete. Module 5 quiz, takeaways, and completion remain open. Module 4's final completion checkpoint remains open.

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
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 07. Module Complete

---

# Integrated configuration framework

## 1. Use the correct configuration layer

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

Give each responsibility one authoritative home, then pair mechanisms when one business need contains different responsibility types.

## 2. Govern connectors and uploaded knowledge

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

Every connector needs a capability contract covering identity, source scope, read tools, draft tools, write tools, unsupported actions, approval boundaries, owner, review date, and revocation.

Every maintained source needs owner, authority, scope, effective and review dates, version, refresh type, conflicts, replacement, sensitivity, and permitted use.

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

Remove, archive, or clearly label duplicate and superseded sources. Distinguish synced sources, static uploads, live retrieval, and historical archives.

## 3. Write precise persistent instructions

A durable instruction defines:

| Element | Question |
|---|---|
| Trigger | When does the rule apply? |
| Required behavior | What should Claude do? |
| Evidence boundary | What may it rely on? |
| Failure behavior | What happens when the rule cannot be satisfied? |
| Observable output | How can a reviewer verify it? |

```text
Vague:
Make reports good and accurate.

Precise:
Cite the supplied source and location for material claims.
State the source or reviewed calculation for figures.
Label unsupported figures `unverified`.
List unresolved gaps.
Do not describe a draft as approved.
```

Apply the two-reader test: two competent readers should interpret a material instruction the same way.

```text
Instruction says `do not send`
      ≠
Send capability technically disabled
```

Persistent guidance does not replace identity, authorization, permissions, deterministic controls, professional approval, or external-action restrictions.

## 4. Maintain the configured baseline

Configurations silently drift when processes, sources, procedures, permissions, people, and product behavior change.

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

Review immediately after policy changes, source replacement, Skill changes, permission changes, team turnover, product migration, repeated regressions, incidents, or growth into shared infrastructure.

## 5. Maintain each component differently

### Instructions

Check terminology, process, format, evidence rules, reviewers, conflicts, and observable tests.

### Knowledge

Check authority, effective dates, duplicates, supersession, scope, sensitivity, refresh behavior, and ownership.

### Skills

Track owner, distribution method, version, enabled audience, trigger description, dependencies, tests, and rollback.

- Anthropic-built Skills are maintained by Anthropic.
- Organization-provisioned Skills are maintained by organization owners.
- Directly shared Skills can update automatically for recipients when the owner updates the shared Skill.
- Personally uploaded custom Skills require the owner to edit, replace, or re-upload their own copy.

```text
Slight recurring format drift
      ≠
Prompting problem by default
```

It may be an outdated Skill, changed dependency, trigger issue, or configuration conflict.

### Connectors

Review identity, source scope, enabled tools, permissions, administrator approval, current need, offboarding, failures, and revocation.

### Memory

Review, correct, add, or delete entries. Export approved context before major migration or reset where appropriate. Reset is destructive and should be used only when selective repair is insufficient.

```text
More remembered context
      ≠
Better continuity
```

Memory does not replace instructions, authoritative knowledge, workflow state, or a system of record.

---

# Worked degraded-Project example

A recurring report Project begins producing subtly wrong output.

The review finds:

1. an instruction uses a retired metric name;
2. knowledge contains two template versions;
3. a custom Skill still uses the old section order; and
4. Memory names a stakeholder who has left.

```text
Version and update instruction
      ↓
Remove or archive obsolete template
      ↓
Replace and regression-test Skill
      ↓
Delete stale Memory entry
      ↓
Rerun representative reports
```

The correct fix is maintenance of the reusable baseline, not increasingly elaborate one-time prompts.

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

## Maintenance decision table

| Condition | Action |
|---|---|
| Minor isolated error | Edit and retest |
| Controlling source replaced | Replace and rerun coverage tests |
| Skill procedure changed | Update or re-upload, version, and test |
| Access no longer needed | Disable or revoke |
| Memory entry stale | Correct or delete |
| Memory broadly misleading | Export approved context, then consider reset |
| New version regresses | Roll back |
| Workspace no longer needed | Retire and revoke dependencies |

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Configuring Projects](lessons/02-configuring-projects.md)
- [Connectors and Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)
- [System-Level Instructions That Stick](lessons/04-system-level-instructions-that-stick.md)
- [Maintaining Configurations](lessons/05-maintaining-configurations.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)
- [Connectors and Uploaded Knowledge prompts](../../prompts/module-05/03-connectors-uploaded-knowledge-prompts.md)
- [System-Level Instructions prompts](../../prompts/module-05/04-system-level-instructions-prompts.md)
- [Maintaining Configurations prompts](../../prompts/module-05/05-maintaining-configurations-prompts.md)

## Engineering patterns

- [Project Configuration Slot Selection Pattern](../../patterns/project-configuration-slot-selection-pattern.md)
- [Connector and Knowledge Boundary Pattern](../../patterns/connector-and-knowledge-boundary-pattern.md)
- [Persistent Instruction Precision Pattern](../../patterns/persistent-instruction-precision-pattern.md)
- [Configuration Maintenance Lifecycle Pattern](../../patterns/configuration-maintenance-lifecycle-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Output degrades without prompt change     → inspect configuration drift
Old metric appears in every report         → update standing instruction
Several template versions conflict         → retain one controlling source
Personal Skill uses old procedure          → update or re-upload and retest
Shared Skill owner publishes an update     → recipients receive updated shared version
Former stakeholder persists in Memory      → edit or delete entry
Memory broadly misleads future work        → export, then consider reset
Unused connector remains authorized        → revoke or disable
Change breaks known cases                  → roll back
```

For maintenance scenarios:

1. identify the affected component;
2. determine ownership and distribution model;
3. compare it with current operating reality;
4. inspect source, permission, and version drift;
5. choose the smallest sufficient repair;
6. preserve approved information before destructive actions;
7. rerun regression tests;
8. document approval and release;
9. monitor for recurrence; and
10. set the next review date.

---

# Completion criteria

- [x] I completed all Module 5 teaching sections.
- [ ] I can place behavior, facts, procedures, continuity, access, controls, and state correctly.
- [ ] I can create connector and source capability registers.
- [ ] I can curate uploaded knowledge and manage supersession.
- [ ] I can write precise persistent instructions and apply the two-reader test.
- [ ] I can distinguish instructions from enforceable controls.
- [ ] I can establish recurring and event-triggered maintenance.
- [ ] I can version and test instructions, knowledge, Skills, connectors, and Memory.
- [ ] I can distinguish shared-skill updates from owner-managed personal uploads.
- [ ] I can choose edit, replace, revoke, reset, rollback, or retirement appropriately.
- [ ] I can preserve approved context before destructive changes.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential instructions, connectors, credentials, private knowledge, Skill packages, Memory exports, internal policies, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Source note

The Maintaining Configurations course material was supplied on August 3, 2026. Product behavior can change. Current official Anthropic documentation and organizational policy control if they conflict with course or repository material.