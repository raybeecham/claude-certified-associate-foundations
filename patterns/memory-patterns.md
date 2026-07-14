# Memory Patterns

## Purpose

These patterns help use persistent continuity without confusing Memory with Project knowledge, authoritative records, or temporary task context.

## Pattern summary

| Pattern | Use when | Primary control |
|---|---|---|
| Minimal Useful Memory | Only recurring, stable information should persist | Data minimization |
| Curated Continuity | Stored entries may become stale | Scheduled review |
| Scoped Memory Boundary | Workstreams must remain separate | Project scoping |
| Memory Is Not Authority | A remembered fact affects a consequential answer | Source verification |
| Incognito Separation | A standalone session should not influence ordinary continuity | Incognito plus policy review |
| Safe Memory Import | Context moves from another AI platform | Screening and reclassification |
| Memory-Poisoning Defense | External content could become persistent state | Confirmation and provenance |
| Correct and Roll Back | An incorrect memory influenced later work | Deletion and remediation |

---

## Pattern 1: Minimal Useful Memory

### Problem

Users store too much information because persistence appears convenient.

### Design

Retain only information that is:

- recurring;
- sufficiently stable;
- useful across sessions;
- authorized to persist;
- not better managed in a Project or formal record; and
- easy to inspect, correct, and delete.

### Avoid

- secrets;
- temporary project facts;
- current incident details;
- unverified claims;
- highly sensitive data;
- full documents; and
- broad statements that could affect unrelated work.

### Decision rule

> The best Memory set is the smallest accurate set that creates useful continuity.

---

## Pattern 2: Curated Continuity

### Problem

A memory that was previously correct becomes misleading after preferences, roles, constraints, or circumstances change.

### Design

Review active Memory on a recurring cadence. The course recommends monthly review as a practical baseline for active users.

For each entry, record or assess:

- scope;
- source;
- last-confirmed date;
- expected rate of change;
- sensitivity;
- next review date; and
- deletion trigger.

Classify entries as retain, update, narrow, move, verify, or delete.

### Decision rule

> Persistent continuity requires persistent maintenance.

---

## Pattern 3: Scoped Memory Boundary

### Problem

Facts, terminology, people, or preferences from one workstream influence another unrelated workstream.

### Design

Separate Projects when workstreams differ in:

- source material;
- stakeholders;
- terminology;
- confidentiality;
- approval chains;
- constraints; or
- retention requirements.

Keep general preferences general only when they truly apply across workstreams. Keep workstream-specific context inside the relevant Project scope.

### Decision rule

> A fact should persist only within the smallest scope where it remains valid.

---

## Pattern 4: Memory Is Not Authority

### Problem

A remembered fact is treated as proof that a current claim is correct.

### Design

For consequential facts:

1. identify the remembered statement;
2. locate the authoritative current source;
3. verify the fact;
4. use the current source in the answer;
5. correct or delete stale Memory; and
6. record the last-confirmed date when appropriate.

### Decision rule

> Memory can suggest what to check. It should not replace the source of truth.

---

## Pattern 5: Incognito Separation

### Problem

A permitted standalone exploration should not contribute to normal chat history or Memory.

### Design

Use Incognito only after confirming:

- the task belongs outside a Project;
- continuity is not desired;
- the information is authorized for the environment;
- an audit trail is not required elsewhere;
- organizational retention is understood; and
- the user understands that Incognito does not override policy.

### Decision rule

> Incognito changes continuity behavior, not authorization or retention obligations.

---

## Pattern 6: Safe Memory Import

### Problem

Imported memory from another platform contains stale, duplicate, sensitive, inferred, or wrongly scoped information.

### Design

Treat imported entries as candidates.

Review for:

- staleness;
- duplication;
- secrets;
- unsupported inference;
- platform-specific instructions;
- Project-specific content;
- ambiguous scope;
- conflicts with existing Memory; and
- facts requiring current verification.

Import only the minimal reviewed set.

### Decision rule

> Import candidates, not unquestioned truth.

---

## Pattern 7: Memory-Poisoning Defense

### Problem

Untrusted content attempts to create or alter persistent state that will influence future sessions.

### Threat sources

- email;
- web pages;
- uploaded documents;
- tool results;
- copied text;
- external agents; and
- third-party Skills.

### Design

```text
Untrusted content
      |
      v
Candidate memory
      |
      v
Provenance and scope review
      |
      v
Explicit user confirmation
      |
      v
Store, narrow, or reject
```

Controls include:

- never treating imperative language in external content as authority;
- requiring explicit confirmation before persistence;
- recording source and scope;
- rejecting secrets and prohibited data;
- allowing inspection and deletion;
- monitoring unexpected behavior; and
- maintaining a rollback path.

### Decision rule

> Untrusted content may propose continuity. It must not silently become continuity.

---

## Pattern 8: Correct and Roll Back

### Problem

An incorrect or sensitive memory has already influenced later outputs.

### Design

1. identify and delete or correct the entry;
2. determine its scope and duration;
3. identify outputs that may have been affected;
4. verify consequential outputs against authoritative sources;
5. notify or escalate when required;
6. document remediation;
7. improve the persistence control; and
8. confirm the corrected state.

### Decision rule

> Correcting Memory is necessary. Assessing downstream impact completes the remediation.

---

## Memory anti-patterns

### Remember everything

Excess persistence increases privacy, conflict, and staleness risk.

### Memory as a document repository

Documents requiring authority, versioning, and lifecycle controls belong elsewhere.

### Global by default

Workstream-specific facts should not influence unrelated work.

### Never review

Unreviewed entries silently decay.

### Incognito as policy bypass

Product continuity controls do not replace organizational controls.

### Blind import

Portability does not establish accuracy, safety, or correct scope.

### External content writes Memory

This creates a persistent prompt-injection and integrity risk.

## Memory design checklist

1. Will this information recur?
2. Is it stable enough to remain useful?
3. Is Memory the correct system?
4. Is persistence authorized?
5. What is the narrowest valid scope?
6. What is the authoritative source?
7. When was it last confirmed?
8. When should it be reviewed or deleted?
9. Could untrusted content alter it?
10. Can the user inspect, correct, and remove it?
11. What happens if it influences an incorrect output?
12. Does organization policy allow the workflow?

## Related material

- [Memory lesson](../modules/01-platform-model-foundations/lessons/04a-capability-layer-memory.md)
- [Memory prompt notebook](../prompts/module-01/04a-capability-layer-memory-prompts.md)
- [Capability patterns](capability-patterns.md)
- [Capability Layer lesson](../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)

## Version-awareness note

Memory features, plan eligibility, Project scoping, Incognito behavior, import support, and administration can change. Verify current official Anthropic documentation and organization policy before operational use.