# Module 5: Configuration & Knowledge Management

Associate Persona · Official Exam Domain 5 · **12% of the exam blueprint**

> **Status:** In progress — Module 5 is the active module. Module 4's final completion checkpoint remains open.

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
+ scoped continuity
+ scoped connector access
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
- [ ] 05. Maintaining Configurations
- [ ] 06. Module 5 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 07. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Using versus operating Claude

A person using Claude supplies the prompt, context, sources, format, and review decisions for the current conversation.

A team operating Claude maintains a bounded, approved environment with instructions, knowledge, procedures, connectors, continuity, output contracts, controls, tests, ownership, and maintenance cadence.

```text
Good prompt today
      ≠
Reliable configured baseline tomorrow
```

---

# Foundation 2: Configuring Projects

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

Give each responsibility one authoritative home, then pair mechanisms when a business need contains different responsibility types.

```text
Scoped continuity
      ≠
Authorization boundary
      ≠
Confidentiality control
      ≠
System of record
```

---

# Foundation 3: Connectors and uploaded knowledge

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

Uploaded knowledge requires ownership, authority, effective and review dates, version, refresh type, conflicts, replacement, sensitivity, and permitted use.

```text
File uploaded
      ≠
File approved
      ≠
File current
      ≠
File controlling
```

Remove, archive, or clearly label duplicate and superseded sources. Distinguish synced sources from static snapshots and historical archives.

---

# Foundation 4: Persistent instructions that stick

Persistent instructions define recurring behavior across Project conversations.

Appropriate uses include:

- verification and citation behavior;
- evidence and source boundaries;
- missing-data and uncertainty behavior;
- tone and terminology;
- output structure;
- review reminders; and
- escalation rules.

```text
Recurring behavioral requirement
      ↓
Precise standing instruction
      ↓
Representative and adversarial tests
      ↓
Consistent Project baseline
```

## Instruction anatomy

| Element | Question |
|---|---|
| Trigger | When does the rule apply? |
| Required behavior | What should Claude do? |
| Evidence boundary | What may it rely on? |
| Failure behavior | What happens when the rule cannot be satisfied? |
| Observable output | How can a reviewer tell it was followed? |

## Vague versus precise

```text
Vague:
Make the reports good and accurate.

Precise:
Lead with a one-sentence headline.
Use Summary, Evidence, Risks, Decisions, and Actions.
Cite the supplied source and location for material factual claims.
State the source or reviewed calculation method for every figure.
Label unsupported figures `unverified`.
List unresolved evidence gaps.
Do not describe a draft as approved.
```

```text
Vague intention
      ≠
Operational behavior
```

## Two-reader test

Ask whether two competent readers would interpret the instruction the same way.

If not, add defined terms, thresholds, named formats, source boundaries, examples, failure behavior, or precedence.

| Weak | Stronger |
|---|---|
| Be concise | Limit the executive summary to five bullets and 150 words |
| Be professional | Use a formal register, no slang, and define acronyms on first use |
| Verify facts | Cite the supplied source and location for every material claim |
| Do not hallucinate | Mark unsupported claims `not supported by supplied sources` |
| Flag risks | List likelihood, impact, owner, and mitigation |

## Mechanism boundary

```text
Behavior → Project instructions
Facts → Project knowledge
Procedure → Skill
Continuity → scoped Memory
Exact rule or authorization → deterministic control
Temporary exception → current request
Secret → approved secret handling
```

## Conflict and precedence

```text
Instruction present
      ≠
Instruction highest authority
      ≠
Instruction technically enforceable
```

When maintained instructions conflict, identify the exact conflict, compare scope and authority, determine supersession, preserve unresolved conflicts, obtain owner resolution, and rerun tests.

## Instructions are not security controls

Persistent instructions cannot independently enforce identity, authorization, data isolation, connector permissions, secret handling, professional approval, external-action restrictions, or exact business rules.

```text
Instruction says `do not send`
      ≠
Send capability technically disabled
```

Pair consequential rules with least privilege, deterministic validation, tool restrictions, human review, approval gates, logging, and systems of record.

## Test model

Use:

- positive tests;
- missing-evidence tests;
- source-conflict tests;
- bypass attempts;
- format exceptions;
- unrelated-task tests;
- draft-versus-approved tests; and
- regression tests after change.

---

# Integrated configuration protocol

```text
1. Define bounded purpose, users, and prohibited uses
2. Classify behavior, facts, procedures, continuity, access, exact controls, and state
3. Place each concern in the correct mechanism
4. Select minimum connector and source scope
5. Record connector identity, capabilities, and unsupported actions
6. Establish source authority, freshness, sensitivity, and conflict rules
7. Curate uploads and remove or label superseded versions
8. Write persistent instructions with trigger, evidence, failure, and observable behavior
9. Apply the two-reader test and document precedence
10. Pair consequential instructions with enforceable controls
11. Test successful, denied, stale, conflicting, bypass, and unsupported cases
12. Version, approve, monitor, update, revoke, roll back, or retire
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Configuring Projects](lessons/02-configuring-projects.md)
- [Connectors and Uploaded Knowledge](lessons/03-connectors-uploaded-knowledge.md)
- [System-Level Instructions That Stick](lessons/04-system-level-instructions-that-stick.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)
- [Connectors and Uploaded Knowledge prompts](../../prompts/module-05/03-connectors-uploaded-knowledge-prompts.md)
- [System-Level Instructions prompts](../../prompts/module-05/04-system-level-instructions-prompts.md)

## Engineering patterns

- [Project Configuration Slot Selection Pattern](../../patterns/project-configuration-slot-selection-pattern.md)
- [Connector and Knowledge Boundary Pattern](../../patterns/connector-and-knowledge-boundary-pattern.md)
- [Persistent Instruction Precision Pattern](../../patterns/persistent-instruction-precision-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Always cite supplied sources          → persistent Project instruction
Current policy text                   → Project knowledge
Standard multi-step report method     → Skill
Be professional                       → too vague; define observable behavior
Unsupported claim                     → label unknown or unverified
Two maintained instructions conflict  → resolve authority and version
Instruction says no external action   → still require technical controls
Instruction changed                   → rerun regression tests
```

For persistent-instruction scenarios:

1. identify whether the need is durable behavior;
2. keep facts and procedures in their appropriate mechanisms;
3. define trigger, evidence boundary, failure behavior, and observable output;
4. apply the two-reader test;
5. specify uncertainty and escalation behavior;
6. document precedence and conflict handling;
7. pair high-stakes rules with enforceable controls;
8. test normal and adversarial cases;
9. version and approve changes; and
10. maintain the instruction set as workflows evolve.

---

# Completion criteria

- [x] I completed the Module 5 introduction.
- [x] I completed Configuring Projects.
- [x] I completed Connectors and Uploaded Knowledge.
- [x] I completed System-Level Instructions That Stick.
- [ ] I can distinguish behavior, facts, procedures, continuity, access, exact controls, and state.
- [ ] I can apply the Project configuration pairing rule.
- [ ] I can distinguish connector access from source authority.
- [ ] I can create a connector capability contract.
- [ ] I can curate uploaded knowledge and manage supersession.
- [ ] I can identify durable behavior that belongs in persistent instructions.
- [ ] I can convert vague instructions into observable rules.
- [ ] I can apply the two-reader test.
- [ ] I can define evidence, uncertainty, and failure behavior.
- [ ] I can distinguish instructions from technical enforcement.
- [ ] I can test and version persistent instructions.
- [ ] I can maintain, roll back, and retire configurations.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential instructions, connector identifiers, credentials, private knowledge sources, proprietary procedures, client data, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Source note

The System-Level Instructions course material was supplied on August 3, 2026. Product capabilities and interfaces can change. Current official documentation and organizational policy control if they conflict with course or repository material.
