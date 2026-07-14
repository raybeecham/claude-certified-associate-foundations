# Capability Patterns

## Purpose

These patterns help choose and combine Claude capability layers without mixing context, procedure, computation, and continuity into one undifferentiated prompt.

## Pattern summary

| Pattern | Use when | Primary capability |
|---|---|---|
| Persistent Workstream Context | Background and sources recur | Project |
| Reusable Procedure | The same task procedure repeats | Skill |
| Executed Computation | Numbers, transformations, charts, or files must be produced programmatically | Code Execution |
| Cross-Session Continuity | Relevant preferences or facts should carry forward | Memory |
| Minimal Capability | The task is one-off and simple | None or the minimum needed |
| Layered Analytical Workflow | A recurring workflow needs context, procedure, and computation | Combination |
| Trust Before Enablement | A Skill or capability receives access to data or tools | Review and least privilege |
| Validate the Method | Code ran, but the result is consequential | Independent validation |

---

## Pattern 1: Persistent Workstream Context

### Problem

Users repeatedly paste the same background, source material, terminology, and standing requirements into new conversations.

### Context

Use this pattern when:

- the task recurs;
- background remains substantially stable;
- the same sources are reused;
- terminology must remain consistent; or
- multiple conversations belong to one workstream.

### Design

Create a Project containing:

- curated, authorized knowledge;
- standing instructions;
- source hierarchy;
- terminology;
- output and review rules; and
- focused conversations for separate tasks.

### Do not place here

- temporary facts;
- unapproved data;
- current task details that change every run;
- stale or superseded sources; or
- the entire history of unrelated conversations.

### Decision rule

> Repeated stable background belongs in a Project, not in the opening paragraph of every new Chat.

---

## Pattern 2: Reusable Procedure

### Problem

A task is performed repeatedly, but the procedure drifts between runs or must be re-explained each time.

### Context

Use this pattern when:

- the same task type recurs;
- steps should occur in a defined order;
- required sections or schemas must remain consistent;
- missing-data behavior must be standardized; or
- review and escalation rules should apply every time.

### Design

Define a Skill with:

- clear trigger;
- required inputs;
- precondition checks;
- ordered steps;
- source restrictions;
- output contract;
- deterministic checks;
- prohibited actions; and
- human review.

### Control

Define a variance contract:

- what must remain invariant;
- what may vary;
- what must come from current inputs;
- what requires deterministic validation; and
- what requires human approval.

### Decision rule

> Stable procedure belongs in a Skill. Stable workstream knowledge belongs in a Project.

---

## Pattern 3: Executed Computation

### Problem

A workflow asks a generative model to produce calculations, transformed data, charts, or structured files using language generation alone.

### Context

Use this pattern when:

- a number will be used or reported;
- data must be cleaned, normalized, joined, or deduplicated;
- statistics or projections are needed;
- a chart must be generated from data;
- a real file must be produced; or
- the operation should be reproducible and auditable.

### Design

Use Code Execution to:

1. inspect inputs;
2. define assumptions, units, and method;
3. execute the operation;
4. preserve transformation logs;
5. reconcile before and after results;
6. report warnings and exceptions; and
7. generate and validate the output.

### Control

Successful execution is not sufficient. Validate:

- input completeness;
- authorization;
- formula and method;
- units;
- missing-value treatment;
- logic;
- output interpretation; and
- acceptance criteria.

### Decision rule

> If the result can be computed and correctness matters, execute it. Then validate the method and output.

---

## Pattern 4: Cross-Session Continuity

### Problem

A user repeatedly re-enters stable preferences or relevant personal working context across sessions.

### Context

Use Memory where current product behavior, workspace settings, and data policy permit it.

Appropriate candidates may include:

- stable communication preferences;
- recurring formatting preferences;
- relevant ongoing interests; or
- continuity that does not require a formal authoritative record.

### Do not use Memory as

- a controlled document repository;
- a source of record;
- a replacement for Project knowledge;
- a secrets store;
- a place for highly sensitive temporary data; or
- proof that a fact remains current.

### Decision rule

> Use Memory for relevant continuity, not for authoritative knowledge management.

---

## Pattern 5: Minimal Capability

### Problem

A workflow becomes over-engineered because every available feature is added by default.

### Context

Use this pattern for:

- one-off questions;
- quick drafts;
- low-consequence exploration;
- small language-only tasks; or
- work with no need for persistence, procedure, calculation, or continuity.

### Design

Start with a normal Chat and add a capability only when a requirement justifies it.

### Trade-off

Every added layer creates some combination of:

- setup cost;
- maintenance;
- access and permission scope;
- context complexity;
- validation burden;
- governance requirements; and
- failure modes.

### Decision rule

> Capabilities should be requirement-driven, not feature-driven.

---

## Pattern 6: Layered Analytical Workflow

### Problem

A recurring analytical deliverable needs stable background, a consistent method, and correct calculations.

### Design

```text
Current task data
      |
      v
Project: context, sources, standing rules
      |
      v
Skill: ordered analytical procedure
      |
      v
Code Execution: calculations, transformations, charts
      |
      v
Draft deliverable
      |
      v
Evidence checks and human review
```

Memory may be added only for appropriate cross-session preferences or continuity. It is not required merely because the other three layers are used.

### Control matrix

| Layer | Failure mode | Control |
|---|---|---|
| Project | Stale or conflicting knowledge | Source ownership, versioning, refresh review |
| Skill | Procedure drift or unsafe instruction | Source review, variance contract, tests |
| Code Execution | Wrong method executed correctly | Formula review, known-case tests, reconciliation |
| Memory | Inappropriate or stale continuity | User control, minimization, correction, policy |
| Human review | Rubber-stamp approval | Defined rubric, accountable reviewer, escalation |

### Decision rule

> Combine layers by responsibility, then test the handoffs between them.

---

## Pattern 7: Trust Before Enablement

### Problem

A third-party Skill or capability appears useful but may receive access to data, files, connectors, or actions.

### Design

Before enablement, review:

- creator and provenance;
- source transparency;
- permissions;
- data access;
- external communication;
- update path;
- supply-chain risk;
- logging;
- monitoring;
- revocation; and
- organizational approval.

Apply least privilege and test with non-sensitive data before broader use.

### Decision rule

> Capability descriptions are claims. Trust decisions require evidence.

---

## Pattern 8: Validate the Method

### Problem

A calculation or file was generated successfully, so users assume the result is correct.

### Design

Validate four stages:

```text
Input validity
      +
Method validity
      +
Execution success
      +
Output validation
      =
Accepted result
```

Use:

- known-case tests;
- independent spot checks;
- reconciliation;
- unit and range checks;
- exception review;
- code or formula inspection; and
- acceptance criteria.

### Decision rule

> Execution proves that a method ran. Validation determines whether the method and result are fit for use.

---

## Capability anti-patterns

### Everything in one prompt

Mixing stable background, reusable procedure, calculations, and personal preferences into one prompt makes the workflow difficult to maintain and test.

### Project as a dumping ground

Uploading every available document increases conflict, staleness, and context noise.

### Skill as a guarantee

A Skill cannot guarantee factual accuracy or identical prose.

### Calculator by prose

Asking for consequential calculations without execution creates avoidable risk.

### Code as proof

Generated code can be logically wrong even when it runs successfully.

### Memory as source of truth

Continuity is not the same as authoritative, versioned knowledge.

### Maximum capability by default

More capabilities do not automatically produce a better workflow.

## Capability design checklist

1. What stable context recurs?
2. What procedure repeats?
3. What must be executed rather than generated?
4. What continuity is appropriate across sessions?
5. Which data and permissions does each layer require?
6. What can be removed to reduce complexity?
7. How will each layer be versioned and maintained?
8. How will handoffs be validated?
9. Where is human review required?
10. How can the capability be disabled, corrected, or retired?

## Related material

- [Capability Layer lesson](../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)
- [Capability Layer prompt notebook](../prompts/module-01/04-capability-layer-skills-code-execution-prompts.md)
- [Core Entry Points](../modules/01-platform-model-foundations/lessons/03-core-entry-points.md)
- [How Claude Behaves](../modules/01-platform-model-foundations/lessons/02-how-claude-behaves.md)

## Version-awareness note

Product behavior, plan availability, workspace administration, and capability details can change. Treat current official Anthropic documentation and organization policy as authoritative.