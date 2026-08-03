# Module 5 Introduction Prompts

These exercises reinforce the shift from using Claude in isolated conversations to operating a maintained configuration and knowledge environment.

Use fictional, generic, synthetic, public, or explicitly authorized scenarios.

---

## 1. Using versus operating

```text
Compare these two situations:

A. One analyst opens a blank chat, uploads files, and rewrites the same instructions each week.
B. A team uses a maintained workspace with approved knowledge, standing instructions, a reusable procedure, and a named review gate.

Explain:
- which is personal use;
- which is an operating model;
- what dependencies are explicit in B;
- what risks still remain; and
- what evidence would show B is working.
```

---

## 2. Configuration-layer sorter

```text
Classify each item into the most appropriate layer:
- current request;
- Project instructions;
- Project knowledge;
- Skill or reusable procedure;
- connector;
- uploaded file;
- scoped memory;
- deterministic control.

Items:
1. "Use the executive briefing format for this workspace."
2. Today's reporting cutoff date.
3. The approved policy manual.
4. A repeatable evidence-extraction checklist.
5. Read-only access to an approved document repository.
6. A spreadsheet supplied for this analysis.
7. A stable user preference that is appropriate to retain.
8. Authorization to release a payment.

For each choice, explain why adjacent layers are weaker.
```

---

## 3. Bounded Project charter

```text
Design a Project configuration for this fictional recurring workflow:
[DESCRIBE WORKFLOW]

Return:
- purpose;
- intended users;
- approved use cases;
- prohibited uses;
- Project instructions;
- Project knowledge categories;
- source authority order;
- output contract;
- uncertainty behavior;
- human-review gates;
- data-handling constraints;
- owner;
- review cadence;
- rollback approach; and
- retirement conditions.

Do not create an unbounded department-wide workspace.
```

---

## 4. Team-consistency diagnosis

```text
A team receives inconsistent answers from the same source package.

Diagnose whether the cause is most likely:
- inconsistent current prompts;
- missing Project instructions;
- conflicting knowledge;
- stale sources;
- uncontrolled Skills;
- connector scope;
- missing review criteria; or
- model variability.

Ask for the minimum evidence needed to localize the cause before proposing changes.
```

---

## 5. Configured-baseline audit

```text
Audit this configuration:
[PASTE SANITIZED CONFIGURATION DESCRIPTION]

Check:
- purpose and scope;
- users and access;
- instruction ownership;
- knowledge authority and freshness;
- source conflicts;
- procedure ownership;
- connector permissions;
- memory appropriateness;
- review and approval gates;
- tests;
- review cadence;
- rollback; and
- retirement.

Return:
1. ready controls;
2. missing controls;
3. hidden dependencies;
4. release blockers; and
5. next responsible action.
```

---

## 6. Maintenance-cadence builder

```text
Create a maintenance plan for a configured workspace used for:
[WORKFLOW]

Include:
- weekly operational checks;
- monthly source and instruction review;
- quarterly access and purpose review;
- event-triggered review conditions;
- owner for each check;
- evidence retained;
- remediation deadlines;
- rollback triggers; and
- retirement triggers.
```

---

## 7. Stale-source investigation

```text
A configured workspace cites an old policy after a new version was published.

Build a root-cause investigation covering:
- source-register failure;
- authority metadata;
- supersession handling;
- retrieval behavior;
- cached or copied content;
- instruction conflicts;
- testing gaps;
- owner and review cadence; and
- affected outputs.

Conclude with contain, correct, verify, communicate, and prevent actions.
```

---

## 8. Instruction-drift review

```text
Review these standing instructions against the current process description:

Instructions:
[PASTE SANITIZED INSTRUCTIONS]

Current process:
[PASTE SANITIZED PROCESS]

Identify:
- obsolete instructions;
- missing instructions;
- conflicts;
- overly broad rules;
- temporary facts that should move to the current request;
- exact controls that should move outside prompt text; and
- tests needed before release.
```

---

## 9. Memory-scope decision

```text
For each item below, decide whether it belongs in:
- scoped memory;
- Project knowledge;
- current request;
- system of record; or
- nowhere in Claude.

Evaluate:
- stability;
- sensitivity;
- future usefulness;
- authority;
- correction mechanism;
- staleness risk; and
- retention appropriateness.

Items:
[LIST ITEMS]
```

---

## 10. Configuration-risk register

```text
Create a risk register for a configured AI workspace.

Include at least:
- stale knowledge;
- instruction conflict;
- excessive connector access;
- unowned Skill;
- memory drift;
- source-authority ambiguity;
- missing review gate;
- secret exposure;
- configuration sprawl;
- failed rollback; and
- unsupported operational dependency.

For each, provide likelihood, impact, indicator, preventive control, detective control, owner, and response.
```

---

## 11. Secret-boundary test

```text
Inspect this proposed configuration plan for secrets or credentials that are being placed in prompts, instructions, files, repositories, or knowledge sources:
[PASTE SANITIZED PLAN]

Return:
- prohibited secret placements;
- appropriate secret-handling boundary;
- least-privilege access changes;
- read-versus-write separation;
- revocation and offboarding requirements; and
- audit evidence.
```

---

## 12. Same question, two users

```text
Design a test to determine whether two authorized users receive consistently governed results from the same configured workspace.

Control for:
- identical task inputs;
- instruction scope;
- source availability;
- access differences;
- model variability;
- output contract;
- uncertainty behavior;
- review criteria; and
- acceptable variation.

Do not require identical wording when semantic and control consistency is sufficient.
```

---

## 13. Configuration change record

```text
Draft a configuration change record for:
[CHANGE]

Include:
- change ID;
- owner;
- reason;
- affected workflows;
- changed instructions;
- changed sources;
- changed access;
- risk assessment;
- tests and results;
- approver;
- rollout date;
- rollback trigger and procedure;
- known limitations; and
- next review date.
```

---

## 14. Configuration versus stronger prompting

```text
A team proposes solving recurring inconsistency by writing a longer prompt each week.

Compare:
1. longer one-time prompt;
2. Project instructions;
3. Project knowledge;
4. Skill;
5. deterministic control; and
6. maintenance process.

Recommend the minimum appropriate combination and explain why prompt length alone is insufficient.
```

---

## 15. Oral certification drill

Explain aloud in 90 seconds:

```text
- the difference between using and operating Claude;
- why configuration creates leverage;
- how configuration turns individual skill into team capability;
- why configuration layers are not interchangeable;
- why maintenance is part of configuration;
- one stale-knowledge failure;
- one excessive-access failure; and
- one boundary that prompts cannot enforce.
```

Then critique the answer for missing ownership, source, access, testing, or lifecycle considerations.

---

# Compact study card

```text
USING CLAUDE
Current prompt + current context + individual judgment

OPERATING CLAUDE
Bounded purpose
+ maintained instructions
+ governed knowledge
+ reusable procedures
+ scoped access
+ human gates
+ tests
+ owner and review cadence

CONFIGURATION LAYERS
Current request → immediate task
Project instructions → workspace behavior
Project knowledge → workspace evidence
Skill → reusable procedure
Connector → external access
Uploaded file → explicit source
Memory → selective continuity
Deterministic system → authority and exact control

LIFECYCLE
Design → Test → Approve → Release → Monitor → Review → Update/Roll back/Retire

RULE
Set up once, benefit repeatedly, and maintain it so it stays true.
```
