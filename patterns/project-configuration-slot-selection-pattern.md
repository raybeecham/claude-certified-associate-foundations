# Project Configuration Slot Selection Pattern

## Problem

Recurring needs are placed in the wrong configuration layer, causing duplication, drift, weak reuse, ambiguous authority, or hidden dependencies.

## Decision model

```text
Behavior / Fact / Procedure / Continuity / Access / Exact control / Durable state
      ↓
Choose the smallest correct mechanism
      ↓
Pair mechanisms when responsibilities differ
      ↓
Assign one authoritative home
      ↓
Test, maintain, and retire
```

## Slot-selection table

| Responsibility | Primary mechanism |
|---|---|
| Immediate task | Current request |
| Durable workspace behavior | Project instructions |
| Workspace facts and references | Project knowledge |
| Reusable procedure | Skill |
| Selected prior Project context | Project-scoped Memory |
| External-system access | Connector |
| Explicit current source | Uploaded file |
| Authorization, fixed rule, exact calculation | Deterministic control |
| Approved state and records | System of record |

## Pairing rule

```text
Always cite claims → Project instruction
Approved sources   → Project knowledge
Report procedure   → Skill
Settled preferences → scoped Memory
Release approval   → human or deterministic workflow control
```

Do not force a multi-responsibility business need into one slot.

## Procedure

1. Define the Project purpose, users, approved uses, prohibited uses, data boundary, owner, review cadence, and retirement conditions.
2. Inventory recurring needs.
3. Classify each need as behavior, fact, procedure, continuity, access, exact control, or durable state.
4. Assign the primary mechanism.
5. Identify required pairings.
6. Establish one authoritative home.
7. Add owner, version, effective date, sensitivity, tests, review date, rollback, and retirement metadata.
8. Test instruction behavior, source retrieval, stale knowledge, Skill activation, Memory relevance, access, cross-project contamination, and side effects.

## Controls

- Keep Projects bounded by purpose, users, and sources.
- Keep secrets out of instructions, knowledge, Skills, and Memory.
- Treat Memory as continuity, not authority, durable state, or a security guarantee.
- Treat Project separation as scope, not a replacement for permissions and disclosure controls.
- Keep reusable Skills independent from Project-private facts.
- Place authorization and exact rules outside probabilistic prompt text.
- Review shared Projects for membership, inherited access, and offboarding.

## Common failures

| Failure | Repair |
|---|---|
| Everything becomes an instruction | Separate facts into knowledge and procedures into Skills |
| Memory becomes source of truth | Verify against knowledge or the system of record |
| Skill becomes Project-specific | Keep procedure generic and draw facts from the active Project |
| One Project contains unrelated work | Split by purpose, audience, source, or sensitivity |
| Configuration is duplicated | Select one authoritative home and remove duplicates |

## Compact rule

```text
Behavior → Project instructions
Facts → Project knowledge
Reusable procedure → Skill
Selected continuity → scoped Memory
External access → connector
Exact rule or authorization → deterministic control
Approved state → system of record
```

> Give each responsibility one authoritative home, then pair mechanisms only when the need contains different responsibility types.

## Evidence to retain

- Project charter;
- configuration map;
- instruction version;
- knowledge-source register;
- Skill version;
- access record;
- Memory eligibility rules;
- tests;
- approval;
- change history;
- rollback path;
- next review date.
