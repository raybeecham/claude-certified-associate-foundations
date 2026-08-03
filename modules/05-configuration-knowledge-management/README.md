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
+ scoped access
+ human controls
+ lifecycle maintenance
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Configuring Projects](lessons/02-configuring-projects.md)
- [ ] 03. Connectors & Uploaded Knowledge
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

A team operating Claude maintains an approved starting environment containing:

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

Configuration turns individual habits and unstated expertise into visible, reusable expectations.

---

# Foundation 2: Configuring Projects

A Project runs smoothly when recurring needs are placed in the correct mechanism.

## Four primary mechanisms

| Mechanism | Primary role | Typical contents |
|---|---|---|
| Project instructions | Workspace behavior | Tone, format defaults, citation rules, uncertainty behavior, review reminders |
| Project knowledge | Workspace facts and references | Policies, brand guides, statements of work, approved reports, reference files |
| Skills | Reusable procedures | Report formatters, checklists, analysis workflows, document-generation methods |
| Project-scoped Memory | Selected continuity | Prior decisions, stakeholder preferences, unresolved questions, recurring terminology |

```text
Behavior   → Project instructions
Facts      → Project knowledge
Procedure  → Skill
Continuity → Project-scoped Memory
```

The mechanisms are related but not interchangeable.

## Instructions

Project instructions should contain durable behavioral rules such as:

- use a formal register;
- cite supplied sources for material factual claims;
- label uncertainty instead of guessing;
- use the approved output structure; and
- escalate conflicting evidence.

Do not use instructions as a warehouse for all factual details or as the only home for a complex reusable procedure.

## Knowledge

Project knowledge should contain relevant, permitted, maintained source material.

For important sources, record:

- authority;
- owner;
- scope;
- effective date;
- review date;
- sensitivity;
- conflicts; and
- replacement when superseded.

```text
Knowledge uploaded
      ≠
Knowledge current
      ≠
Knowledge controlling
```

## Skills

Skills carry task-specific procedures, instructions, scripts, and resources that can activate when relevant across Claude.

Use a Skill when the method:

- recurs;
- should remain consistent;
- can be defined independently from one Project's private facts;
- has clear inputs and outputs;
- benefits from examples, templates, or scripts; and
- can be tested and versioned.

```text
One Project's background → Project knowledge
Reusable method          → Skill
```

## Project-scoped Memory

Where available and appropriate, Project memory can preserve continuity from prior work within that Project.

Use it selectively for:

- settled stakeholder names;
- standing preferences;
- prior conversational decisions;
- recurring terminology; and
- unresolved follow-up context.

Material items should still be verified against authoritative records.

```text
Stable approved reference → Project knowledge
Evolving Project history  → Project-scoped Memory
```

```text
Scoped continuity
      ≠
Authorization boundary
      ≠
Confidentiality control
      ≠
System of record
```

Project separation helps scope continuity, but it does not replace identity, permissions, disclosure review, or data-handling controls.

---

# The pairing rule

Many needs require more than one mechanism because they contain different responsibilities.

## Citation example

```text
Project instruction:
Always cite the source document for material factual claims.

Project knowledge:
The approved source documents Claude is expected to cite.
```

## Status-report example

```text
Skill:
Standard report procedure and required sections.

Project knowledge:
Brand guide, current plan, approved reference documents.

Project instructions:
Tone, citation, uncertainty, and review requirements.

Project-scoped Memory:
Settled stakeholder preferences and prior Project decisions.
```

> Give each responsibility one authoritative home, then pair mechanisms when a business need contains different responsibility types.

---

# Worked account-workspace example

A fictional consulting team creates one bounded Project for a client account.

## Project instructions

- formal register;
- source citations for material claims;
- no unsupported gap filling;
- unresolved questions and conflicts labeled;
- approved weekly-update format.

## Project knowledge

- current statement of work;
- current brand guide;
- approved delivery plan;
- last three approved status reports;
- maintained glossary.

## Skill

An account-independent status-report Skill defines:

1. required inputs;
2. standard sections;
3. issue and risk formatting;
4. decisions and actions;
5. quality checks; and
6. output validation.

The procedure is reusable while each Project supplies its own knowledge.

## Project-scoped Memory

Eligible continuity may include:

- accepted stakeholder naming;
- approved abbreviations;
- prior conversational decisions; and
- unresolved follow-up items.

## Sharing and permissions

A shared Project should have explicit membership, visibility, source permissions, ownership, review expectations, offboarding, and disclosure controls.

---

# Common configuration mistakes

| Mistake | Why it fails | Repair |
|---|---|---|
| Procedure buried in instructions | Difficult to reuse, test, and version | Move the procedure to a Skill |
| Behavior rule stored only in knowledge | Source content does not reliably establish operating behavior | Put behavior in Project instructions |
| Stable fact stored only in Memory | Continuity may be stale or informal | Put the authoritative fact in knowledge or a system of record |
| Project used as a dumping ground | Creates retrieval noise, conflicts, and disclosure ambiguity | Bound the Project by purpose, audience, and sources |
| Same rule duplicated across layers | Versions drift | Choose one authoritative home |
| Memory described as a security guarantee | Scope does not replace access or disclosure controls | Add identity, permissions, and governance controls |

---

# Project configuration protocol

```text
1. Define the Project purpose, users, and prohibited uses
2. Inventory recurring needs
3. Classify each need as behavior, fact, procedure, continuity, access, exact control, or durable state
4. Place it in the smallest correct mechanism
5. Identify required pairings
6. Establish source authority, freshness, scope, and sensitivity
7. Define sharing, access, and review boundaries
8. Test representative and adversarial scenarios
9. Record configuration version, owner, and approval
10. Review, update, roll back, or retire on cadence
```

## Configuration map

| Need | Type | Mechanism | Authoritative home | Owner | Test | Review cadence |
|---|---|---|---|---|---|---|
| Cite material claims | Behavior | Project instructions | Instruction set | Project owner | Claim-to-source test | Quarterly |
| Current policy | Fact | Project knowledge | Approved policy | Policy owner | Version and scope check | On change |
| Standard report | Procedure | Skill | Skill package | Process owner | Golden-output cases | On release |
| Settled preference | Continuity | Project memory | Reviewed continuity | Project owner | Accuracy and relevance | Monthly |

---

# Broader configuration foundation

Later lessons will extend this baseline into:

- connector and uploaded-file selection;
- least-privilege retrieval;
- source authority and freshness;
- instruction scope and precedence;
- configuration testing;
- change control;
- rollback and retirement;
- stale and superseded knowledge;
- secret boundaries; and
- appropriate reusable context.

```text
Available source
      ≠
Authorized source
      ≠
Controlling source
      ≠
Current source
```

```text
Configuration created
      ≠
Configuration governed
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Configuring Projects](lessons/02-configuring-projects.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-05/01-module-introduction-prompts.md)
- [Configuring Projects prompts](../../prompts/module-05/02-configuring-projects-prompts.md)

## Engineering pattern

- [Project Configuration Slot Selection Pattern](../../patterns/project-configuration-slot-selection-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Always cite sources                 → Project instruction
Current policy document             → Project knowledge
Repeatable report procedure         → Skill
Prior Project decision              → scoped Memory, verified if material
Same need includes rule and facts   → pair instructions with knowledge
Procedure buried in instructions    → move to Skill
Stable fact stored only in Memory   → move to knowledge
Project contains unrelated clients  → separate bounded workspaces
Memory described as security        → add permissions and data controls
```

For Project-configuration scenarios:

1. identify the need type;
2. choose the smallest correct mechanism;
3. distinguish behavior, facts, procedures, and continuity;
4. pair mechanisms when responsibilities differ;
5. retain one authoritative home for each item;
6. verify source authority and freshness;
7. keep Memory subordinate to authoritative records;
8. define sharing and access controls;
9. test for bleed, drift, conflict, and missing context; and
10. assign ownership and maintenance.

---

# Completion criteria

- [x] I completed the Module 5 introduction.
- [x] I completed Configuring Projects.
- [ ] I can explain the difference between using and operating Claude.
- [ ] I can configure a Project around a bounded purpose.
- [ ] I can distinguish Project instructions, Project knowledge, Skills, and scoped Memory.
- [ ] I can apply the pairing rule when one need spans mechanisms.
- [ ] I can give each configuration responsibility one authoritative home.
- [ ] I can distinguish scoped continuity from authority, durable state, and security controls.
- [ ] I can build and maintain a source register.
- [ ] I can apply least privilege to connector and knowledge access.
- [ ] I can keep credentials and secrets outside prompts and repositories.
- [ ] I can design durable instructions with clear scope and precedence.
- [ ] I can test, version, roll back, and retire configurations.
- [ ] I completed the Module 5 quiz and takeaways.
- [ ] I completed the knowledge lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential client workspaces, private knowledge sources, stakeholder details, connector identifiers, credentials, proprietary instructions, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.

## Source note

The Configuring Projects course material was supplied on August 3, 2026. Product capabilities and terminology can change. Current official Anthropic documentation controls if it conflicts with course or repository material.
