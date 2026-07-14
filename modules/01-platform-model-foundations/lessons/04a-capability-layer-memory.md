# Lesson 4A: Capability Layer, Memory

## Overview

Memory supports continuity across sessions by retaining selected work-relevant facts, preferences, and recurring context. It reduces repetitive setup, but it should not be treated as an unlimited archive, an authoritative record, or a replacement for a Project knowledge base.

The useful mental model is:

```text
Memory
   |
   +-- Carries relevant continuity forward
   +-- Reduces repeated re-entry
   +-- Remains subject to correction and deletion
   +-- Must be reviewed for freshness and scope
```

> [!IMPORTANT]
> Memory is valuable only when it remains accurate, appropriately scoped, and authorized. Stale or misplaced memory can create persistent errors across future sessions.

## Learning objectives

After completing this lesson, you should be able to:

- explain what Memory is intended to retain;
- distinguish Memory from Project instructions, Project knowledge, chat history, and formal records;
- identify strong and weak candidates for Memory;
- design a recurring Memory-curation process;
- explain how Project-scoped boundaries reduce cross-workstream leakage;
- decide when Incognito mode is appropriate;
- explain why Incognito mode does not override organizational retention policy;
- evaluate memory imports before making them persistent; and
- identify privacy, staleness, and memory-poisoning risks.

## What Memory is for

Memory answers:

> Which recurring facts or preferences would be useful in future sessions without requiring the user to re-enter them each time?

Appropriate candidates may include:

- recurring role context;
- stable communication preferences;
- preferred output structures;
- names or roles of frequent collaborators, when appropriate and authorized;
- long-lived working constraints;
- recurring terminology preferences;
- stable goals that span multiple conversations; and
- accessibility or formatting preferences.

### Example

A user frequently requests technical briefings with:

- a concise executive summary;
- detailed technical analysis after the summary;
- explicit assumptions;
- no unsupported claims; and
- a short list of next actions.

Those are recurring working preferences and may be useful Memory candidates.

## What Memory is not

Memory should not become the default home for every piece of information Claude encounters.

Do not treat Memory as:

- a source of record;
- a controlled policy repository;
- a document-management system;
- a replacement for Project knowledge;
- a substitute for version control;
- a secrets store;
- a repository for temporary case details;
- proof that a fact remains current; or
- a place for data that the user is not authorized to persist.

### Key distinction

```text
Continuity is not authority.
```

A remembered preference may help shape an answer. A remembered regulation, deadline, balance, organizational role, or technical configuration should still be verified against the current authoritative source when correctness matters.

## Memory versus adjacent concepts

| Concept | Primary purpose | Appropriate content | Main risk |
|---|---|---|---|
| Memory | Cross-session continuity | Stable preferences and recurring facts | Staleness or overreach |
| Project instructions | Durable rules for one workstream | Role, scope, source rules, output requirements | Conflicting or outdated instructions |
| Project knowledge | Curated reusable evidence | Approved documents and references | Stale, conflicting, or unauthorized files |
| Chat history | Record of prior conversations | Past exchanges and decisions | Assuming history is automatically active context |
| Current conversation | Task-specific working context | Today's request, current inputs, temporary facts | Context overload |
| Formal record system | Authoritative organizational state | Approved records, tickets, policies, databases | Access and governance failures |

### Decision rule

> Put information in the narrowest layer that matches its purpose, lifecycle, and authority.

## Strong Memory candidates

A strong candidate is:

1. likely to recur;
2. stable enough to remain useful;
3. not better managed in a Project or formal record;
4. safe and authorized to retain;
5. easy for the user to review and correct; and
6. useful across more than one conversation.

### Candidate test

Score each statement from 0 to 2:

| Question | 0 | 1 | 2 |
|---|---:|---:|---:|
| Will this recur? | No | Maybe | Yes |
| Is it stable? | Changes often | Changes occasionally | Rarely changes |
| Is Memory the right system? | Better elsewhere | Unclear | Yes |
| Is retention appropriate? | No | Needs review | Yes |
| Would future sessions benefit? | Little | Somewhat | Clearly |

A high score supports Memory. A low score suggests using the current conversation, a Project, or an external record instead.

## Weak Memory candidates

Avoid or closely review:

- temporary deadlines;
- current incident details;
- one-time project facts;
- credentials, tokens, or secrets;
- regulated personal data;
- confidential source material;
- facts copied from untrusted content;
- claims that have not been verified;
- information likely to expire soon; and
- preferences that apply to only one workstream.

## Memory curation

Memory is a maintained information set, not a write-once feature.

A memory that was accurate three months ago can become actively misleading after an organizational change, a new role, an updated preference, or a revised constraint.

### Recommended review cycle

For active users, establish a regular review cadence. The course recommends at least monthly review as a practical baseline.

During review:

1. list stored memories;
2. confirm each item is still accurate;
3. correct changed information;
4. delete obsolete entries;
5. remove duplicates;
6. narrow entries that are too broad;
7. relocate workstream-specific facts into the proper Project;
8. identify sensitive content that should not persist; and
9. record the review date when the workflow requires governance evidence.

### Curation states

| State | Meaning | Action |
|---|---|---|
| Current | Accurate and useful | Retain |
| Needs refinement | Useful but too broad or ambiguous | Rewrite |
| Project-specific | Applies to one workstream | Move to Project configuration |
| Temporary | No longer recurring | Delete |
| Unverified | Source or accuracy is uncertain | Verify or remove |
| Sensitive | Persistence is inappropriate | Delete and review exposure |
| Superseded | Replaced by a newer fact or preference | Update |

### Example prompt: Memory audit

```text
Review the following stored Memory entries.

For each entry, classify it as:
- retain;
- update;
- narrow;
- move to a Project;
- verify;
- delete; or
- requires policy review.

Evaluate:
- accuracy;
- recurrence;
- current usefulness;
- sensitivity;
- scope;
- source;
- last-confirmed date; and
- whether an authoritative external record should control instead.

Do not assume an entry remains true merely because it was previously stored.
```

## Project-scoped Memory

Project-scoped Memory helps keep continuity separated by workstream.

The intended boundary is:

```text
Project A Memory  !=  Project B Memory
```

A preference or fact that belongs to one Project should not automatically shape an unrelated Project.

### Why the boundary matters

Separate scopes reduce:

- accidental cross-workstream disclosure;
- terminology contamination;
- conflicting instructions;
- application of the wrong stakeholder context;
- reuse of stale assumptions; and
- inappropriate personalization.

### Design guidance

Use separate Projects when workstreams have materially different:

- source material;
- audiences;
- terminology;
- confidentiality requirements;
- approval chains;
- constraints; or
- retention expectations.

> [!WARNING]
> A Project boundary is not permission to upload unauthorized information. Data classification, workspace policy, and user authorization still apply.

## Memory boundaries and shared facts

Some facts may seem useful everywhere, such as a general writing preference. Others should remain scoped, such as a workstream's stakeholder names, reporting thresholds, or domain-specific terminology.

Use this classification:

| Type of fact | Preferred scope |
|---|---|
| General writing preference | Account-level Memory, when available and appropriate |
| Workstream-specific preference | Project-scoped Memory or Project instructions |
| Stable Project evidence | Project knowledge |
| Current task detail | Current conversation |
| Authoritative operational state | External source of record |

## Incognito mode

Incognito mode is designed for standalone conversations that should not contribute to ordinary Memory or chat-history continuity.

It can be useful for:

- sensitive exploratory discussions;
- temporary brainstorming;
- testing prompts that should not influence later sessions;
- one-time work with inputs that should not appear in normal history; and
- separating an experiment from established preferences.

### Important limitations

Incognito mode should not be interpreted as:

- permission to enter otherwise prohibited data;
- a guarantee of zero backend retention;
- a way to bypass enterprise controls;
- a replacement for an approved secure environment; or
- a control that overrides organizational data-retention policy.

The course describes Incognito as applying to standalone Chats outside Projects. Product behavior can change, so verify current account and workspace behavior before relying on it.

### Incognito decision test

Use Incognito only when all of the following are true:

1. the task belongs in a standalone Chat;
2. it should not inform future Memory;
3. it should not appear in normal chat history;
4. the information is still permitted in the environment; and
5. organizational retention rules have been understood.

## Importing memories from another AI platform

The course identifies memory import as experimental as of June 2026. Availability and supported plans may change, so treat this as a version-specific feature rather than a permanent certification fact.

### Safe import principle

> Import candidates, not unquestioned truth.

An imported memory set may contain:

- stale preferences;
- duplicate entries;
- platform-specific instructions;
- unsupported assumptions;
- sensitive information;
- content that belongs in a Project;
- facts that were inferred incorrectly; or
- old context that should be deleted.

### Import workflow

1. Export or collect the candidate memories through an approved method.
2. Review every entry before persistence.
3. Remove secrets and unauthorized data.
4. Classify general versus Project-specific information.
5. Verify facts that may have changed.
6. Rewrite ambiguous entries.
7. Import only the minimal useful set.
8. Recheck the resulting Memory after import.
9. Delete the transfer file when policy requires it.

If automated import is unavailable, the course describes manual entry through Memory settings as the fallback. Do not place general memory candidates into a Project knowledge base merely because import is unavailable. The storage location should follow the information's purpose, not feature convenience.

## Memory security and integrity

Persistent continuity expands the impact of incorrect or malicious information.

### Key risks

| Risk | Example | Control |
|---|---|---|
| Stale memory | Old role or preference continues shaping outputs | Scheduled review and last-confirmed date |
| Scope leakage | Workstream-specific fact appears elsewhere | Project scoping and separation |
| Overcollection | Too much personal or operational detail is retained | Data minimization |
| Memory poisoning | Untrusted content becomes a durable instruction or fact | Require user confirmation and source review |
| Authority confusion | Remembered statement overrides current evidence | Source hierarchy and verification |
| Sensitive persistence | Confidential detail remains longer than intended | Retention policy and deletion |
| Ambiguous entry | Broad memory affects unrelated tasks | Narrow wording and explicit scope |

### Memory-poisoning control

Do not automatically convert content from emails, websites, uploaded documents, tool results, or other untrusted sources into persistent Memory.

A safer workflow is:

```text
Untrusted content
      |
      v
Candidate fact or preference
      |
      v
Source and scope review
      |
      v
Explicit user confirmation
      |
      v
Store, narrow, or reject
```

## Memory and human control

Users should be able to:

- inspect what is stored;
- understand why it is useful;
- correct inaccurate entries;
- delete unwanted entries;
- narrow overly broad scope;
- separate workstreams; and
- choose when continuity should not apply.

A workflow that depends on hidden or unreviewable persistent state is difficult to govern.

## Common mistakes

### Storing everything

More Memory is not automatically better. Excess information increases staleness, conflict, and privacy risk.

### Treating Memory as a database

Memory supports continuity. It does not provide the controls, schemas, approvals, and audit guarantees of a formal system of record.

### Mixing unrelated workstreams

Separate Projects and scopes when terminology, people, evidence, or constraints differ.

### Forgetting to review

Unreviewed Memory can preserve facts long after they stop being true.

### Using Incognito as a policy bypass

Incognito changes product continuity behavior. It does not authorize prohibited data or override organizational policy.

### Importing without curation

Imported memories should be screened, minimized, and classified before persistence.

## Worked examples

### Example 1: General preference

A user consistently wants:

- headings;
- concise executive summaries;
- detailed technical rationale; and
- explicit next steps.

**Best fit:** Memory, if enabled and appropriate.

### Example 2: Workstream terminology

A recurring initiative uses a specific glossary and reporting threshold.

**Best fit:** Project instructions or Project knowledge, not general Memory.

### Example 3: Current incident detail

A temporary incident bridge number and live status are needed today.

**Best fit:** Current conversation or authorized incident system, not Memory.

### Example 4: Sensitive exploration

A user wants to explore a permitted but sensitive topic without adding it to normal history or Memory.

**Best fit:** Incognito mode, after confirming organizational retention and data-handling requirements.

### Example 5: Imported preference set

A user transfers preferences from another assistant.

**Best fit:** Review each item, delete stale or sensitive entries, separate Project-specific context, and retain only confirmed general preferences.

## Hands-on lab

### Objective

Design and audit a safe Memory set.

### Part 1: Classification

Classify each item as Memory, Project instructions, Project knowledge, current conversation, external record, or delete:

1. Preferred answer structure.
2. A current access token.
3. A workstream's approved glossary.
4. A temporary deadline next Friday.
5. A stable accessibility preference.
6. A policy document.
7. A collaborator's role that changed last month.
8. A confidential attachment from a one-time task.

### Part 2: Curation

Create a sample Memory inventory with:

- entry;
- scope;
- source;
- last-confirmed date;
- sensitivity;
- review date; and
- action.

### Part 3: Boundary design

Design separate scopes for two fictional workstreams with different terminology and audiences. Explain which facts remain global and which must stay Project-scoped.

### Part 4: Incognito decision

Write a short decision memo explaining whether a sensitive standalone exploration should use Incognito and which organizational controls still apply.

### Part 5: Import review

Review a synthetic set of imported memories and identify:

- duplicates;
- stale facts;
- secrets;
- Project-specific details;
- unsupported assumptions; and
- entries safe to retain.

## Knowledge check

1. What is Memory primarily intended to provide?
2. Why can stale Memory be worse than no Memory?
3. When should a fact belong in Project knowledge instead of Memory?
4. Does Incognito mode override organizational retention policy?
5. Why should imported memories be treated as candidates rather than trusted facts?
6. What is the risk of automatically storing content from untrusted sources?
7. What review cadence does the course recommend as a baseline for active users?
8. Why is a formal source of record still needed for consequential facts?

## Answer guide

1. Appropriate cross-session continuity.
2. It can repeatedly inject incorrect context into future work.
3. When the fact is stable evidence for one defined workstream and should be curated as a source.
4. No.
5. They may be stale, duplicated, sensitive, incorrectly inferred, or scoped to another platform or workstream.
6. Persistent memory poisoning or unauthorized persistence.
7. At least monthly.
8. Memory does not provide the authority, versioning, and governance of a controlled record.

## Flashcards

**Q:** What problem does Memory solve?  
**A:** Re-entering appropriate recurring facts and preferences across sessions.

**Q:** Is Memory an authoritative source?  
**A:** No. It supports continuity and should be verified against authoritative sources when correctness matters.

**Q:** What is the core Memory-curation rule?  
**A:** Review, correct, narrow, move, or delete entries as their accuracy and scope change.

**Q:** What belongs in Project knowledge rather than general Memory?  
**A:** Curated, reusable evidence and references for a specific workstream.

**Q:** What does Project-scoped Memory protect against?  
**A:** Inappropriate cross-workstream continuity and context leakage.

**Q:** What does Incognito mode change?  
**A:** It keeps a standalone session out of ordinary Memory and chat-history continuity, subject to current product behavior.

**Q:** What does Incognito mode not change?  
**A:** Authorization requirements, organizational retention, or data-handling policy.

**Q:** Why should imported memories be reviewed?  
**A:** They may contain stale, sensitive, duplicated, unsupported, or wrongly scoped information.

**Q:** What is memory poisoning?  
**A:** Untrusted or malicious content becoming durable state that influences later sessions.

**Q:** What is the best Memory design principle?  
**A:** Retain the smallest accurate set that creates useful continuity.

## Certification lens

For scenario questions, distinguish among:

- general cross-session continuity;
- one-workstream context;
- reusable evidence;
- temporary task input;
- formal authoritative state; and
- sessions that should not contribute to continuity.

The best answer usually places information in the narrowest appropriate layer and preserves user control.

## Key takeaways

- Memory carries selected continuity across sessions.
- Memory must be actively curated because stale facts can repeatedly distort future work.
- Project-scoped Memory helps separate unrelated workstreams.
- Incognito mode changes Memory and history behavior but does not override organizational retention or authorization.
- Imported memories require review, minimization, verification, and scope classification.
- Memory is not a source of record, Project knowledge base, or secrets store.
- Persistent state increases the importance of data minimization, user control, and protection against memory poisoning.

## Related material

- [Capability Layer, Skills and Code Execution](04-capability-layer-skills-code-execution.md)
- [Capability patterns](../../../patterns/capability-patterns.md)
- [Memory prompt notebook](../../../prompts/module-01/04a-capability-layer-memory-prompts.md)
- [Core Entry Points](03-core-entry-points.md)

## Version-awareness note

This lesson reflects the certification course material supplied for June 2026. Memory availability, plan support, Project scoping, Incognito behavior, import workflows, and workspace administration can change. Verify current behavior in official Anthropic documentation and organization settings before operational use.