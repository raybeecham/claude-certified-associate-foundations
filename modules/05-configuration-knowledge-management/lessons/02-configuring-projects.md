# Lesson 2: Configuring Claude Projects

## Overview

A Project works well when each recurring need is placed in the correct configuration mechanism.

```text
Behavior   → Project instructions
Facts      → Project knowledge
Procedure  → Skill
Continuity → Project-scoped Memory
```

The configuration skill is choosing the smallest correct slot, then pairing slots when one business need contains different responsibility types.

---

# Plain-English explanation

A weekly status-report workflow may need:

| Need | Mechanism |
|---|---|
| Formal tone and citation rule | Project instructions |
| Current statement of work and brand guide | Project knowledge |
| Standard report procedure | Skill |
| Settled stakeholder preferences | Project-scoped Memory, when appropriate |

Putting everything into one large instruction block makes the Project harder to test, reuse, update, and govern.

---

# Analogy: a professional kitchen

```text
House rules → instructions
Pantry      → knowledge
Recipe      → Skill
Shift notes → scoped continuity
```

A recipe does not belong in the pantry, and yesterday's shift notes do not replace an official ingredient label.

---

# Project instructions

Use Project instructions for durable workspace behavior:

- tone and register;
- output structure;
- citation expectations;
- uncertainty behavior;
- source boundaries;
- terminology;
- review reminders; and
- escalation behavior.

Example:

```text
Use a formal register.
Cite supplied source locations for material factual claims.
Label missing or conflicting evidence rather than guessing.
Use the approved weekly-update structure.
```

```text
Behavior rule       → Project instructions
Reference fact      → Project knowledge
Repeatable workflow → Skill
```

---

# Project knowledge

Use Project knowledge for workspace-specific source material:

- policies;
- statements of work;
- brand guides;
- approved templates;
- product references;
- datasets;
- approved reports; and
- glossaries.

For important sources, record owner, authority, scope, effective date, review date, sensitivity, conflicts, and replacement.

```text
Knowledge uploaded
      ≠
Knowledge current
      ≠
Knowledge controlling
```

---

# Skills

Skills package reusable procedures, instructions, scripts, and resources for specialized tasks.

Use a Skill when the method:

- recurs;
- should remain consistent;
- is reusable beyond one Project;
- has clear inputs and outputs;
- benefits from examples, templates, or scripts; and
- can be versioned and tested.

```text
One Project's background → Project knowledge
Reusable method          → Skill
```

Skills can activate when relevant across Claude rather than being confined to one Project.

---

# Project-scoped Memory

Where available and appropriate, Project Memory can preserve selected continuity from prior Project work:

- stakeholder names;
- standing preferences;
- prior conversational decisions;
- unresolved questions; and
- recurring terminology.

```text
Stable approved reference → Project knowledge
Evolving Project history  → Project-scoped Memory
```

Memory should not replace authoritative documents, Project instructions, workflow state, a system of record, access control, authorization, or professional approval.

Current Claude guidance describes each Project's memory as separate from non-project chats. Treat this as a continuity boundary—not as a complete security or disclosure guarantee.

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

# The pairing rule

Many needs require more than one mechanism.

## Citation example

```text
Instruction:
Always cite the source document for material factual claims.

Knowledge:
The approved source documents Claude should use.
```

## Status-report example

```text
Skill:
Procedure and standard report structure.

Knowledge:
Brand guide, current plan, approved references.

Project instructions:
Tone, citation, uncertainty, and review expectations.

Memory:
Settled preferences and prior Project decisions.
```

> Give each responsibility one authoritative home, then pair mechanisms when a need contains different responsibility types.

---

# Worked example: a fictional client workspace

## Instructions

- use a formal register;
- cite material factual claims;
- do not fill evidence gaps with assumptions;
- label unresolved questions and conflicts;
- follow the approved weekly-update format.

## Knowledge

- current statement of work;
- brand guide;
- approved delivery plan;
- last three approved reports;
- maintained glossary.

## Skill

A reusable status-report Skill defines required inputs, standard sections, risk formatting, decisions, action items, quality checks, and output validation.

## Memory

Eligible continuity may include accepted naming, abbreviations, prior conversational decisions, and unresolved follow-ups. Material items are checked against authoritative records.

## Sharing

A shared Project should have explicit membership, visibility, source permissions, ownership, review expectations, offboarding, and disclosure controls.

One-Project-per-client can support separation, but it does not replace identity, permission, records, or data-handling controls.

---

# Common mistakes

| Mistake | Repair |
|---|---|
| Procedure buried in instructions | Move the reusable method to a Skill |
| Behavior rule stored only in knowledge | Put behavior in Project instructions |
| Stable fact stored only in Memory | Move authority to knowledge or a system of record |
| Project used as a dumping ground | Bound it by purpose, users, sources, and sensitivity |
| Same rule duplicated across layers | Select one authoritative home |
| Memory described as a security guarantee | Add permissions and disclosure controls |

---

# Project configuration protocol

```text
1. Define purpose, users, and prohibited uses
2. Inventory recurring needs
3. Classify each as behavior, fact, procedure, continuity, access, exact control, or durable state
4. Place it in the smallest correct mechanism
5. Identify required pairings
6. Establish source authority, freshness, scope, and sensitivity
7. Define sharing, access, and review boundaries
8. Test representative and adversarial scenarios
9. Record version, owner, and approval
10. Review, update, roll back, or retire on cadence
```

## Configuration map

| Need | Type | Mechanism | Owner | Test |
|---|---|---|---|---|
| Cite material claims | Behavior | Project instructions | Project owner | Claim-to-source test |
| Current policy | Fact | Project knowledge | Policy owner | Version and scope check |
| Standard report | Procedure | Skill | Process owner | Golden-output cases |
| Settled preference | Continuity | Project Memory | Project owner | Accuracy and relevance review |

---

# Exam lens

```text
Always cite sources                 → Project instruction
Current policy document             → Project knowledge
Repeatable report procedure         → Skill
Prior Project decision              → scoped Memory, verified if material
Rule plus supporting facts          → pair instructions with knowledge
Procedure buried in instructions    → move to Skill
Stable fact stored only in Memory   → move to knowledge
Unrelated clients in one Project    → separate bounded workspaces
Memory described as security        → add permissions and data controls
```

---

# Short recap

```text
1. Instructions govern Project behavior.
2. Knowledge provides Project facts and references.
3. Skills carry reusable procedures.
4. Project Memory preserves selected continuity.
5. Memory is not an authoritative record or security control.
6. Many needs require paired mechanisms.
7. Give each responsibility one authoritative home.
8. Keep Projects bounded.
9. Test sharing, retrieval, drift, and conflict.
10. Maintain configurations over time.
```

## Educational-use notice

This is an unofficial educational resource. Product availability and behavior can change. Verify current official Anthropic documentation before relying on implementation-specific behavior.
