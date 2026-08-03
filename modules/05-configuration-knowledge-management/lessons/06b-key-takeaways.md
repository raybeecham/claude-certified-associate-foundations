# Lesson 6B: Module 5 Key Takeaways

## Overview

Module 5 is about moving from isolated prompting to a maintained operating environment.

```text
Configured baseline
      +
Correct mechanism selection
      +
Bounded connector access
      +
Precise instructions
      +
Lifecycle maintenance
      ↓
Repeatable and trustworthy Claude workspace
```

The five durable takeaways are:

1. configuration is leverage;
2. each need belongs in the correct mechanism;
3. every connector has a capability boundary;
4. persistent instructions must be precise and testable; and
5. configurations require scheduled maintenance.

---

# Plain-English explanation

A strong Project does not depend on one person remembering the perfect prompt every time.

It begins with a configured baseline: approved instructions, maintained knowledge, reusable procedures, scoped continuity, bounded external access, and a review process.

That baseline creates leverage only while it remains accurate.

```text
Set up once
      ↓
Use repeatedly
      ↓
Review and maintain
      ↓
Continue to trust
```

---

# One analogy: maintaining a professional workshop

A workshop becomes productive when tools, instructions, materials, and safety controls have assigned places.

- Operating rules belong on the wall.
- Reference materials belong in the library.
- Repeatable methods belong in procedures.
- Current work notes belong in the job folder.
- Specialized equipment has defined capabilities and limits.
- Everything requires inspection and maintenance.

Putting every item in one drawer may seem convenient, but it creates confusion, drift, and preventable mistakes.

Claude configuration follows the same principle.

---

# Takeaway 1: Configuration is leverage

Configuration separates using Claude from operating Claude.

```text
Using Claude
      ↓
Build the prompt and context for this conversation

Operating Claude
      ↓
Maintain an approved baseline that supports repeated work
```

A configured environment can preserve:

- Project purpose and users;
- standing behavior;
- approved knowledge;
- reusable procedures;
- selected continuity;
- connector access;
- output expectations;
- review gates; and
- maintenance ownership.

The durable rule is:

> Configure stable recurring needs once, then verify that the configuration still matches the current workflow.

Configuration does not guarantee correctness. It reduces repeated setup and makes expectations more visible, consistent, and testable.

---

# Takeaway 2: Match each need to the right mechanism

```text
Behavior   → Project instructions
Facts      → Project knowledge
Procedure  → Skill
Continuity → Project-scoped Memory
Access     → Connector
Authority  → Human and deterministic controls
State      → System of record
```

## Instructions

Use for tone, format defaults, evidence rules, uncertainty behavior, and escalation.

## Knowledge

Use for policies, references, templates, approved reports, datasets, and other Project-specific evidence.

## Skills

Use for repeatable procedures, checklists, scripts, and standardized workflows that should activate when relevant.

## Scoped Memory

Use for selected continuity from prior work, such as reviewed preferences, terminology, decisions, and unresolved context.

```text
Selected continuity
      ≠
Authoritative record
      ≠
Permission boundary
```

Many business needs require paired mechanisms. A citation rule belongs in instructions, while the documents to cite belong in knowledge. A reporting procedure belongs in a Skill, while Project-specific facts remain in knowledge.

> Give each responsibility one authoritative home, then pair mechanisms without duplicating authority.

---

# Takeaway 3: Know every connector's boundary

Connectors extend Claude into external systems, but capabilities vary by connector, plan, administrator settings, connected identity, permission scope, and enabled tools.

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

Maintain a capability contract that records:

- connected identity;
- permitted source scope;
- search and read capabilities;
- draft capabilities;
- create, update, send, publish, or delete capabilities;
- unsupported actions;
- human approval boundaries;
- owner;
- review date; and
- revocation path.

Separate consequential stages:

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

When a connector cannot perform the requested action, first check setup, authentication, permissions, source scope, tool loading, and capability. Do not assume a stronger model changes the connector's permissions.

---

# Takeaway 4: Write instructions precisely

Vague persistent instructions fail quietly because they do not define observable behavior.

```text
Weak:
Be professional and accurate.
```

```text
Stronger:
Use a formal register.
Define acronyms on first use.
Cite the supplied source and location for material factual claims.
Label unsupported figures `unverified`.
List unresolved evidence gaps.
```

A durable instruction should define:

| Element | Question |
|---|---|
| Trigger | When does this apply? |
| Required behavior | What should Claude do? |
| Evidence boundary | What may it rely on? |
| Failure behavior | What happens when the rule cannot be met? |
| Observable output | How can a reviewer verify compliance? |

Apply the two-reader test:

> Would two competent readers interpret the instruction the same way?

```text
Instruction written
      ≠
Instruction precise
      ≠
Instruction technically enforced
```

High-stakes instructions still require permissions, deterministic checks, controlled tools, human review, and approval gates.

---

# Takeaway 5: Maintain configurations or quality decays

Instructions, knowledge, Skills, connectors, and Memory can all become stale.

```text
Configured baseline
      ↓
Process, source, permission, and personnel change
      ↓
Silent configuration drift
      ↓
Output quality degradation
```

Use both recurring and event-triggered reviews.

A monthly review is a useful baseline for active Projects, adjusted for change rate and consequence. Review immediately after major policy, source, procedure, permission, team, product, or workflow changes.

## Component checks

### Instructions

Check terminology, process, output format, evidence rules, reviewers, and conflicts.

### Knowledge

Check authority, freshness, duplicates, supersession, scope, sensitivity, and ownership.

### Skills

Check owner, distribution model, version, dependencies, trigger behavior, tests, and rollback path.

### Connectors

Check identity, permissions, enabled tools, business need, offboarding, and revocation.

### Memory

Review, correct, add, or delete entries. Preserve approved information before destructive reset. Accuracy matters more than volume.

```text
No error message
      ≠
No maintenance problem
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

# Exam lens

```text
Repeated setup in every chat          → configure a stable baseline
Multi-step reusable procedure         → Skill
Project-specific source material      → Project knowledge
Standing behavior rule                → Project instruction
Selected prior context                → scoped Memory
External source or action             → connector with defined capability
Vague instruction                     → make observable and testable
Quiet recurring regression            → inspect configuration drift
Old source or stakeholder persists    → update knowledge or Memory
Connector cannot perform action       → respect the capability boundary
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

# Short recap

```text
1. Configuration creates leverage across repeated conversations.
2. Instructions govern behavior.
3. Knowledge supplies Project-specific facts and references.
4. Skills carry repeatable procedures.
5. Scoped Memory preserves selected continuity.
6. Connectors have explicit capability and permission boundaries.
7. Precise instructions create observable behavior.
8. Natural-language guardrails do not replace technical controls.
9. Configurations silently drift as the environment changes.
10. Scheduled review and component-specific maintenance preserve quality.
```

## Product-verification note

This lesson was reviewed against official Anthropic Help Center material available on August 3, 2026. Current documentation describes Projects as self-contained workspaces with their own knowledge and instructions, Skills as reusable procedures that load when relevant, connectors as permission-bound integrations with connector-specific read and write capabilities, and project memory as a separate continuity space. Product availability and behavior can change, and current official documentation controls.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, privacy, records-management, compliance, legal, or operational advice.