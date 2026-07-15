# Context Management Patterns

## Purpose

These patterns help preserve coherence, traceability, and security across long conversations and multi-session work.

The durable principle is:

> Keep active context small, authoritative, and sufficient for the next action.

## Pattern summary

| Pattern | Use when | Primary principle |
|---|---|---|
| Context Budget | A session contains many files, turns, tools, or instructions | Curate active context |
| Clean Task Boundary | A new phase or task begins | Restart deliberately |
| State Capsule | Work must move to a new conversation | Summarize operational state |
| Persist by Lifecycle | Information should survive the current thread | Store it in the correct layer |
| Thin Active Context | A Project or agent contains too much material | Retrieve only what is needed |
| Context-Drift Detection | Earlier requirements are being lost | Diagnose and intervene |
| Source and Decision Ledger | Long work needs compact traceability | Externalize authoritative state |
| Usage-Aware Segmentation | A large task may exhaust rolling or weekly limits | Plan work in stages |
| Summary Validation | A compressed handoff becomes durable | Review before trust |
| Secure Context Boundary | Untrusted or sensitive content may persist | Preserve authority and scope |

---

## Pattern 1: Context Budget

### Problem

A conversation accumulates messages, files, tools, results, and instructions until recall, focus, latency, or usage efficiency degrades.

### Design

Inventory everything consuming context:

- standing instructions;
- conversation turns;
- uploaded files;
- retrieved knowledge;
- tool definitions;
- tool results;
- examples;
- current drafts; and
- output requirements.

Classify each item as:

- required now;
- retrieve on demand;
- summarize;
- persist elsewhere;
- remove as stale;
- remove as duplicate;
- remove as irrelevant; or
- remove as unauthorized.

### Control

Preserve:

- authoritative instructions;
- current evidence;
- accepted decisions;
- safety constraints;
- output contracts; and
- required review gates.

### Decision rule

> A context window is a working set, not an archive.

---

## Pattern 2: Clean Task Boundary

### Problem

A single conversation is used for multiple phases or unrelated tasks, causing instruction drift and mixed state.

### Design

Start a new conversation when:

- a new phase begins;
- the task changes materially;
- source scope changes;
- corrections accumulate;
- the thread becomes hard to audit;
- context degradation appears; or
- a fresh session improves focus.

Before restarting:

1. capture accepted decisions;
2. record sources and versions;
3. save deliverables;
4. list open questions;
5. persist durable state; and
6. create a validated handoff.

### Decision rule

> Restart at meaningful work boundaries, not only when the product forces you to.

---

## Pattern 3: State Capsule

### Problem

A new conversation must continue work without carrying the full transcript.

### Design

Create a compact state artifact containing:

- objective;
- scope;
- decisions;
- source ledger;
- constraints;
- terminology;
- completed work;
- work in progress;
- assumptions;
- open questions;
- risks;
- next actions; and
- review requirements.

Separate facts, decisions, assumptions, and unresolved questions.

### Control

Validate the capsule against the original conversation before it becomes the next session's starting point.

### Decision rule

> Transfer state, not transcript volume.

---

## Pattern 4: Persist by Lifecycle

### Problem

Users either lose important state when a chat ends or persist too much information in the wrong place.

### Design

Map information by purpose:

| Information | Home |
|---|---|
| Durable workstream behavior | Project instructions |
| Reusable evidence | Project knowledge |
| General preference | Memory |
| Reusable method | Skill |
| Current task detail | Current conversation |
| Traceable decision | Decision log or record |
| Operational truth | External authoritative system |

### Control

Every persistent item should have:

- scope;
- owner;
- source;
- last-confirmed date;
- refresh cadence; and
- deletion trigger.

### Decision rule

> Persistence should follow lifecycle and authority, not convenience.

---

## Pattern 5: Thin Active Context

### Problem

A Project or agent loads every available document and tool into every turn.

### Design

Use retrieval and task decomposition so that only relevant material enters active context.

- Keep Project instructions concise.
- Curate Project knowledge.
- Retrieve sources by task.
- Disable unused tools and connectors.
- Clear obsolete tool results.
- Split research, analysis, drafting, and validation into separate threads.

### Control

Require source labels and version dates so retrieved material remains interpretable.

### Decision rule

> Load what the next decision needs, not everything the workstream owns.

---

## Pattern 6: Context-Drift Detection

### Problem

Claude stops following earlier instructions or contradicts accepted state.

### Signals

- missing required sections;
- forgotten constraints;
- repeated corrections;
- reopened decisions;
- wrong source version;
- focus only on the latest turn;
- assumptions becoming facts; or
- unrelated context influencing the answer.

### Design

1. test whether the problem is context, prompting, retrieval, tools, or model capability;
2. identify the last known-good state;
3. reconstruct authoritative decisions and sources;
4. create a state capsule;
5. restart if the thread is no longer reliable; and
6. verify recovery with representative tasks.

### Decision rule

> Diagnose drift before upgrading the model or extending the same thread.

---

## Pattern 7: Source and Decision Ledger

### Problem

Sources and decisions are buried across hundreds of conversational turns.

### Design

Maintain two compact artifacts.

**Source ledger:** authority, version, date, scope, status, conflicts, and location.

**Decision ledger:** decision, rationale, evidence, owner, date, assumptions, validation, and revisit trigger.

### Control

Do not infer approval. Record who accepted each consequential decision.

### Decision rule

> Externalize what must remain traceable.

---

## Pattern 8: Usage-Aware Segmentation

### Problem

A long task risks exhausting a rolling session or weekly usage budget before completion.

### Design

- Inspect current usage.
- Define task stages.
- Use the minimum qualified model per stage.
- Batch related questions.
- Store reused files in a Project.
- Disable unnecessary high-effort settings and tools.
- Produce an artifact and handoff at every stage.
- Reserve higher-tier usage for difficult exceptions.

### Control

Define a fallback for an interrupted session:

- saved artifact;
- state capsule;
- next-session prompt;
- unresolved-task list; and
- owner.

### Decision rule

> Plan the work so a usage reset delays execution, not understanding.

---

## Pattern 9: Summary Validation

### Problem

A generated summary is trusted even though it may omit or distort important state.

### Design

Validate for:

- missing constraints;
- altered decisions;
- wrong source versions;
- facts and assumptions mixed together;
- unresolved questions marked complete;
- missing ownership;
- sensitive data; and
- untrusted instructions promoted to durable state.

### Control

Require human approval for consequential handoffs.

### Decision rule

> Compression is a transformation, so validate it like any other transformation.

---

## Pattern 10: Secure Context Boundary

### Problem

Untrusted, unauthorized, or workstream-specific content becomes durable or leaks into another context.

### Design

- Separate unrelated Projects and conversations.
- Treat documents and tool results as evidence, not higher-priority instructions.
- Require authorization before persistence.
- Exclude secrets and unnecessary sensitive fields.
- Label source provenance.
- Prevent automatic promotion into Memory, Skills, instructions, or summaries.
- Apply retention and deletion policy.

### Decision rule

> Context continuity must not override authority, confidentiality, or scope.

---

## Context anti-patterns

### Infinite thread

One conversation is extended indefinitely because automatic summarization exists.

### Transcript as database

Accepted decisions and current facts exist only in chat history.

### Summary without review

A compressed handoff becomes the new source of truth without validation.

### Persist everything

Temporary, sensitive, or stale content accumulates in Memory or Project knowledge.

### Tool overload

Every connector remains active, consuming context and widening permissions.

### Mixed workstreams

Unrelated tasks and confidential contexts share one conversation.

### Bigger model as context fix

A higher-capability model is selected instead of cleaning stale or conflicting context.

### Usage planning by hope

A long session begins without checking budgets, staging work, or saving interim state.

## Context-management checklist

1. What is the exact next action?
2. Which context is required for it?
3. Which source is authoritative?
4. What can be retrieved later?
5. What can be removed now?
6. Has context drift appeared?
7. Is this a clean restart boundary?
8. What state must transfer?
9. Where should durable information persist?
10. Has the summary been validated?
11. Is sensitive data minimized and authorized?
12. What rolling or weekly usage budget remains?
13. What artifact exists if the session ends now?
14. Who owns the next decision and review?

## Related material

- [Context Management lesson](../modules/01-platform-model-foundations/lessons/06-context-management.md)
- [Context Management prompt notebook](../prompts/module-01/06-context-management-prompts.md)
- [Memory patterns](memory-patterns.md)
- [Model-selection patterns](model-selection-patterns.md)

## Version-awareness note

Context-window sizes, automatic context management, compaction, context editing, Project retrieval, tool behavior, Memory, rolling usage windows, weekly usage pools, usage credits, and Enterprise billing can change. Verify current official Anthropic documentation and product settings.