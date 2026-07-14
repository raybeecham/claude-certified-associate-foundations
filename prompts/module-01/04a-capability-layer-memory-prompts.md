# Module 1 Prompt Notebook: Memory

These prompts support Memory selection, curation, scoping, Incognito decisions, import review, and persistent-state security. Replace bracketed fields with task-specific information and verify current product behavior and organizational policy before use.

## 1. Memory candidate classifier

### Use when

You are deciding where recurring information should live.

```text
Classify each item below as:
- account-level Memory;
- Project-scoped Memory;
- Project standing instructions;
- Project knowledge;
- current conversation input;
- external authoritative record;
- Incognito-only context; or
- do not retain.

Items:
[PASTE ITEMS]

For each item, evaluate:
- recurrence;
- stability;
- authority;
- sensitivity;
- scope;
- expected lifetime;
- user benefit;
- risk if stale;
- risk if exposed; and
- required review cadence.

Return a table with classification, rationale, and action.
```

## 2. Memory curation audit

### Use when

Stored memories need periodic review.

```text
Audit the following Memory inventory.

Inventory:
[PASTE INVENTORY]

Classify each entry as:
- retain;
- update;
- narrow;
- merge;
- move to Project instructions;
- move to Project knowledge;
- verify against an authoritative source;
- delete;
- delete and initiate exposure review; or
- requires policy review.

Evaluate:
- current accuracy;
- last-confirmed date;
- recurrence;
- scope;
- sensitivity;
- source;
- ambiguity;
- conflict with other entries;
- risk if stale; and
- next review date.

Do not assume an entry remains valid because it was previously stored.
```

## 3. Minimal Memory set builder

### Use when

A user has too much candidate context and wants a focused Memory set.

```text
Create the smallest useful Memory set from the information below.

Candidate information:
[PASTE INFORMATION]

Retain only entries that are:
- likely to recur;
- stable;
- useful across sessions;
- safe and authorized to persist;
- not better managed in a Project or formal record; and
- easy for the user to review and correct.

For each retained entry, write:
- concise memory statement;
- scope;
- source;
- last-confirmed date;
- review cadence; and
- deletion trigger.

List excluded items and explain where they belong instead.
```

## 4. Project-scoping review

### Use when

Memory may be leaking assumptions between unrelated workstreams.

```text
Review the following continuity requirements for scope separation.

Workstream A:
[DESCRIPTION]

Workstream B:
[DESCRIPTION]

Candidate memories:
[LIST]

Classify each memory as:
- safe to remain general;
- scoped to Workstream A;
- scoped to Workstream B;
- belongs in Project instructions;
- belongs in Project knowledge;
- temporary input; or
- should not be retained.

Identify:
- terminology conflicts;
- stakeholder confusion risks;
- privacy risks;
- differing approval chains;
- facts that could become stale; and
- controls needed to prevent cross-workstream use.
```

## 5. Memory versus Project boundary review

### Use when

You are unsure whether information belongs in Memory or Project configuration.

```text
Determine whether each item belongs in Memory, Project instructions, Project knowledge, or neither.

Items:
[PASTE ITEMS]

Use these rules:
- Memory supports cross-session continuity.
- Project instructions define durable rules for one workstream.
- Project knowledge contains curated reusable evidence for one workstream.
- Formal records remain external authoritative sources.

Return:
1. classification table;
2. rationale;
3. proposed Memory entries;
4. proposed Project instructions;
5. proposed Project knowledge inventory; and
6. items requiring deletion or external verification.
```

## 6. Incognito decision memo

### Use when

A standalone conversation may need to stay out of ordinary Memory and chat history.

```text
Evaluate whether the following task should use Incognito mode.

Task:
[DESCRIBE TASK]

Assess:
- whether the task belongs in a standalone Chat;
- whether it should influence future Memory;
- whether it should appear in normal chat history;
- data sensitivity;
- authorization to process the information;
- organizational retention requirements;
- approved environment requirements;
- need for an audit trail; and
- alternative workflows.

Return:
- recommendation;
- rationale;
- controls Incognito provides;
- controls Incognito does not provide;
- data-handling prerequisites; and
- safer alternative if Incognito is insufficient.
```

## 7. Imported-memory review

### Use when

Memory candidates have been exported from another AI platform.

```text
Review this imported memory set before persistence.

Imported entries:
[PASTE OR ATTACH ENTRIES]

For each entry, check for:
- staleness;
- duplicates;
- unsupported inference;
- platform-specific instructions;
- secrets or credentials;
- sensitive personal or organizational data;
- Project-specific details;
- facts requiring current verification;
- ambiguous wording; and
- conflicts with existing Memory.

Classify each entry as:
- safe to retain;
- rewrite and retain;
- move to a Project;
- verify first;
- delete; or
- escalate for policy review.

Then produce a minimal approved import set and a post-import validation checklist.
```

## 8. Memory freshness review

### Use when

A consequential answer appears to rely on a remembered fact.

```text
Review the following remembered facts for freshness before using them.

Facts:
[PASTE FACTS]

For each fact, identify:
- source;
- last-confirmed date;
- expected rate of change;
- consequence if wrong;
- authoritative source to verify;
- whether it should remain in Memory; and
- corrected statement, if verified.

Do not use Memory alone as evidence for a consequential claim.
```

## 9. Memory-poisoning risk assessment

### Use when

A workflow may convert external content into persistent Memory.

```text
Assess the risk that untrusted content could create or alter persistent Memory.

Workflow:
[DESCRIBE WORKFLOW]

External sources:
[LIST SOURCES]

Evaluate:
- which content is untrusted;
- how memory candidates are proposed;
- whether user confirmation is explicit;
- source provenance;
- scope assignment;
- authority confusion;
- malicious instruction risk;
- persistence and rollback;
- logging and alerting; and
- review ownership.

Return:
1. threat scenarios;
2. likelihood and impact;
3. required controls;
4. safe candidate-memory workflow;
5. rollback and cleanup procedure; and
6. residual risk.
```

## 10. Memory entry rewrite

### Use when

An existing entry is too broad or ambiguous.

```text
Rewrite the following Memory entry so it is narrow, testable, and appropriately scoped.

Current entry:
[ENTRY]

Clarify:
- subject;
- scope;
- conditions where it applies;
- conditions where it does not apply;
- source;
- last-confirmed date;
- expected expiration or review date; and
- whether it is a preference, fact, or constraint.

Avoid wording that could silently apply to unrelated workstreams.
```

## 11. Memory deletion and remediation plan

### Use when

A stale, sensitive, or incorrect memory has been discovered.

```text
Create a remediation plan for the following Memory issue.

Issue:
[DESCRIBE ISSUE]

Assess:
- incorrect or sensitive entries;
- scope of possible influence;
- conversations or outputs that may have been affected;
- authoritative correction;
- deletion steps;
- replacement entry, if needed;
- notification or escalation requirements;
- audit evidence; and
- prevention controls.

Return immediate actions, follow-up actions, owner, and completion criteria.
```

## 12. Monthly Memory review checklist

### Use when

Establishing a recurring curation process.

```text
Create a monthly Memory review checklist for an active professional user.

Include:
- inventory review;
- accuracy confirmation;
- duplicate removal;
- scope review;
- Project-boundary review;
- sensitive-data review;
- stale-fact verification;
- imported-memory review;
- memory-poisoning indicators;
- deletion and correction actions;
- next-review scheduling; and
- evidence to retain for governance.

Keep the process practical enough to complete in 15 minutes unless an issue is found.
```

## Suggested study exercise

1. Use prompt 1 to classify ten synthetic facts.
2. Use prompt 2 to audit the resulting Memory set.
3. Use prompt 6 on a sensitive standalone scenario.
4. Use prompt 7 on a fictional import file.
5. Use prompt 9 to threat-model an email-to-Memory workflow.

## Related material

- [Memory lesson](../../modules/01-platform-model-foundations/lessons/04a-capability-layer-memory.md)
- [Capability Layer lesson](../../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)
- [Capability patterns](../../patterns/capability-patterns.md)
- [Capability Layer prompt notebook](04-capability-layer-skills-code-execution-prompts.md)

## Version-awareness note

Memory features, plan eligibility, Project scoping, Incognito behavior, import support, and administration can change. Verify current official Anthropic documentation and organization policy before relying on these templates.