# Module 1 Prompt Notebook: Context Management

These prompts support context-health assessment, state transfer, persistence decisions, conversation cleanup, usage planning, and recovery from drift.

Use only fictional, synthetic, public, or authorized information. Remove secrets and unnecessary sensitive data before creating summaries or persistent state.

## 1. Context-health audit

### Use when

A conversation is long, repetitive, or beginning to lose earlier instructions.

```text
Audit this conversation for context health.

Conversation or summary:
[PASTE CONTENT]

Evaluate:
- objective clarity;
- instruction consistency;
- repeated or duplicated context;
- stale assumptions;
- conflicting decisions;
- irrelevant side topics;
- missing early-session requirements;
- source-version confusion;
- unresolved questions that appear falsely resolved;
- tool output that no longer matters;
- information that should be persisted elsewhere; and
- indicators of context degradation.

Return:
1. context-health rating;
2. evidence for the rating;
3. items to retain;
4. items to remove;
5. items to verify;
6. items to persist;
7. recommendation: continue, checkpoint, summarize, or restart; and
8. a safe next prompt.
```

## 2. Restart, summarize, or persist decision

### Use when

You need to select the correct response to context pressure.

```text
Decide whether this workflow should:
- continue in the current conversation;
- create a checkpoint;
- summarize and restart;
- restart without carrying most prior context;
- persist selected information; or
- use a combination.

Current state:
[DESCRIBE STATE]

Evaluate:
- whether the task has changed;
- whether the current thread is still coherent;
- whether earlier instructions are being lost;
- amount of irrelevant or conflicting context;
- whether important state is already recorded elsewhere;
- sensitivity and retention requirements;
- current usage budget;
- auditability;
- cost of reconstructing state; and
- consequence of an incomplete handoff.

Return a decision, rationale, transition steps, and validation checks.
```

## 3. State-capsule handoff

### Use when

Work must continue in a fresh conversation.

```text
Create a state capsule for continuing this work in a new conversation.

Preserve:
- objective;
- scope and exclusions;
- accepted decisions and rationale;
- authoritative sources, versions, and dates;
- definitions and terminology;
- requirements and negative constraints;
- completed work;
- current work product and location;
- open questions;
- unresolved evidence;
- assumptions and uncertainties;
- rejected approaches;
- owners and next actions;
- validation status; and
- required human approval.

Separate:
1. confirmed facts;
2. accepted decisions;
3. assumptions;
4. unresolved questions; and
5. temporary details.

Do not introduce new conclusions.
Flag any detail that cannot be compressed safely.
End with a ready-to-paste kickoff prompt for the next conversation.
```

## 4. Handoff-summary validator

### Use when

A summary will become the starting point for another session.

```text
Validate this handoff summary against the source material.

Source material:
[PASTE OR DESCRIBE SOURCE]

Handoff summary:
[PASTE SUMMARY]

Check for:
- omitted decisions;
- omitted negative constraints;
- altered meaning;
- incorrect source versions or dates;
- assumptions presented as facts;
- open questions presented as resolved;
- lost ownership or deadlines;
- sensitive information that should be removed;
- untrusted instructions that became durable; and
- details that require direct quotation rather than compression.

Return:
1. validation result;
2. discrepancies;
3. severity;
4. corrected summary; and
5. reviewer sign-off checklist.
```

## 5. Persistence placement classifier

### Use when

You need to decide what should survive the current conversation.

```text
Classify each item into the narrowest appropriate location:
- Project standing instructions;
- Project knowledge;
- account-level Memory;
- Project-scoped Memory or summary;
- Skill;
- current conversation only;
- external authoritative system;
- decision log;
- generated artifact; or
- do not retain.

Items:
[PASTE ITEMS]

For each item, evaluate:
- purpose;
- recurrence;
- stability;
- scope;
- authority;
- sensitivity;
- expected lifetime;
- owner;
- refresh cadence;
- deletion trigger; and
- risk if stale or leaked.

Flag anything being persisted merely for convenience rather than a valid lifecycle need.
```

## 6. Conversation-hygiene cleanup

### Use when

A thread contains too many topics or too much duplicated material.

```text
Create a cleanup plan for this conversation.

Current contents:
[DESCRIBE OR PASTE CONTENT]

Identify:
- duplicated instructions;
- duplicated documents;
- obsolete drafts;
- stale assumptions;
- unrelated subtopics;
- completed branches of work;
- tool results no longer needed;
- sensitive material that should not remain active;
- decisions that need formal recording; and
- tasks that deserve separate conversations.

Return:
1. material to retain in active context;
2. material to summarize;
3. material to persist elsewhere;
4. material to archive or remove;
5. proposed conversation split; and
6. a clean kickoff prompt for each new thread.
```

## 7. Long-session architecture plan

### Use when

A task is too large for one reliable conversation.

```text
Design a multi-session context plan for this work.

Work objective:
[OBJECTIVE]

Sources and files:
[SOURCES]

Expected deliverables:
[DELIVERABLES]

Constraints:
[CONSTRAINTS]

Divide the work into focused sessions.
For each session, define:
- purpose;
- required context;
- information explicitly excluded;
- model and tools;
- expected output;
- checkpoint artifact;
- decisions to record;
- validation;
- handoff to the next session; and
- stop condition.

Prefer clean task boundaries over one indefinitely extended thread.
```

## 8. Context-budget reducer

### Use when

A prompt, Project, or agent request contains too much material.

```text
Reduce this context to the smallest authoritative set required for the task.

Task:
[TASK]

Current context inventory:
[INVENTORY]

For each item, classify:
- required now;
- retrieve only if needed;
- summarize;
- move to durable storage;
- remove as duplicate;
- remove as stale;
- remove as irrelevant;
- remove as unauthorized; or
- requires owner review.

Preserve:
- authoritative instructions;
- current sources;
- accepted decisions;
- required examples;
- output contract; and
- safety and review controls.

Return the reduced context package and explain every removal.
```

## 9. Source and decision ledger builder

### Use when

Long work needs compact, traceable state.

```text
Create two artifacts from this material:

1. Source ledger with:
- source name;
- authority;
- owner;
- version or date;
- scope;
- status;
- conflicts;
- citation or location; and
- refresh trigger.

2. Decision ledger with:
- decision;
- rationale;
- supporting evidence;
- assumptions;
- owner;
- decision date;
- validation status;
- dissent or alternatives; and
- revisit trigger.

Material:
[PASTE MATERIAL]

Do not infer approval where none is documented.
```

## 10. Usage-aware work plan

### Use when

A large task may exceed rolling or weekly usage limits.

```text
Create a usage-aware execution plan.

Task:
[TASK]

Current plan and available usage information:
[DETAILS]

Candidate models and tools:
[OPTIONS]

Optimize for:
- required quality;
- session and weekly usage headroom;
- context efficiency;
- latency;
- review effort; and
- completion before deadlines.

Recommend:
1. task segmentation;
2. minimum qualified model by stage;
3. tools to enable or disable;
4. files to place in Project knowledge;
5. questions to batch;
6. checkpoints and handoffs;
7. when to monitor Settings > Usage;
8. fallback if a limit is reached; and
9. conditions that justify usage credits or a plan change.

Do not assume current limit values are permanent.
```

## 11. Memory and context curation review

### Use when

Memory, Project knowledge, and current conversation context may be overlapping.

```text
Review the following information inventory.

Memory:
[MEMORY]

Project instructions:
[INSTRUCTIONS]

Project knowledge:
[KNOWLEDGE]

Current conversation context:
[CURRENT CONTEXT]

Identify:
- duplication;
- scope conflicts;
- stale entries;
- temporary details stored persistently;
- authoritative facts stored only in Memory;
- instructions hidden inside source documents;
- untrusted content promoted to durable state; and
- missing refresh or deletion rules.

Return a corrected placement map and maintenance plan.
```

## 12. Context-drift recovery

### Use when

Claude repeatedly forgets or contradicts prior decisions.

```text
Recover this workflow from context drift.

Original objective and requirements:
[ORIGINAL STATE]

Observed drift:
[EXAMPLES]

Current artifacts and sources:
[ARTIFACTS]

Perform:
1. root-cause assessment;
2. identify decisions still valid;
3. identify stale or conflicting context;
4. reconstruct the authoritative state;
5. create a corrected state capsule;
6. propose a clean new-conversation kickoff;
7. recommend Project or Memory updates; and
8. define tests confirming the recovery worked.

Do not assume context length is the only possible cause.
```

## Suggested study exercise

Use prompts 1, 2, 3, 5, and 10 on a fictional month-long project. Compare the resulting architecture with the lesson's restart, summarize, and persist model.

## Related material

- [Context Management lesson](../../modules/01-platform-model-foundations/lessons/06-context-management.md)
- [Memory prompts](04a-capability-layer-memory-prompts.md)
- [Choosing Models prompts](05-choosing-models-prompts.md)
- [Context Management patterns](../../patterns/context-management-patterns.md)

## Version-awareness note

Context-window sizes, automatic summarization, Code Execution requirements, Project caching and retrieval, chat search, Memory, effort controls, rolling usage windows, weekly pools, usage credits, and Enterprise billing can change. Verify current official Anthropic documentation and product settings.