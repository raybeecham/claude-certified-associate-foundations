# Module 1 Prompt Notebook: Core Entry Points

These prompts help select and configure Chat, Projects, Artifacts, and Research. Replace bracketed fields with task-specific information and verify current feature availability in the official Claude Help Center.

## 1. Entry-point selector

### Use when

You are deciding where a new task or workstream should begin.

```text
Act as an AI workflow architect.

Task:
[DESCRIBE THE TASK]

Evaluate whether the best starting point is:
- Chat;
- Project;
- Artifact;
- Research; or
- a combination.

Consider:
- whether the task is one-off or recurring;
- stability of background context;
- repeated source-file use;
- consistency of the output format;
- current-information requirements;
- investigation depth;
- intended recipient;
- collaboration needs;
- data sensitivity;
- review requirements; and
- setup cost.

Return:
1. recommended entry point;
2. optional supporting entry points;
3. rationale;
4. setup checklist;
5. risks and controls; and
6. conditions that would change the recommendation.
```

## 2. Project-readiness assessment

### Use when

A Chat may have become a recurring workstream.

```text
Evaluate whether the workflow below should become a Claude Project.

Workflow:
[DESCRIBE WORKFLOW]

Score each condition from 0 to 2:
- recurrence;
- stability of background context;
- reuse of the same documents;
- consistency of output format;
- need for shared terminology;
- need for collaboration;
- cost of repeated setup; and
- need for traceable continuity.

Then provide:
- total score;
- recommendation: remain in Chat, create a Project, or redesign first;
- standing instructions that belong in the Project;
- knowledge that belongs in the Project;
- information that should remain task-specific;
- data that should not be uploaded; and
- a maintenance cadence.
```

## 3. Standing-instructions builder

### Use when

You need durable Project guidance without mixing in temporary task details.

```text
Draft standing instructions for this Project.

Project purpose:
[PURPOSE]

Users:
[USERS]

Authoritative sources:
[SOURCES]

Required outputs:
[OUTPUTS]

Create concise standing instructions covering:
1. role and purpose;
2. scope and exclusions;
3. source authority;
4. approved terminology;
5. analysis procedure;
6. required output structure;
7. citation behavior;
8. missing-evidence behavior;
9. prohibited assumptions;
10. privacy and data-handling constraints;
11. review and escalation rules; and
12. version-control expectations.

After the draft, list any details that are too temporary or task-specific to persist as standing instructions.
```

## 4. Project knowledge-base curator

### Use when

You need to decide what belongs in a Project's reusable knowledge.

```text
Review the proposed Project knowledge inventory below.

Inventory:
[LIST DOCUMENTS, FILES, OR SOURCES]

For each item, classify it as:
- include as authoritative knowledge;
- include as labeled reference;
- include only for one conversation;
- replace with a newer version;
- exclude as irrelevant;
- exclude as duplicate;
- exclude as unauthorized or sensitive; or
- requires owner review.

Return a table with:
- item;
- classification;
- authority;
- version or date;
- sensitivity;
- expected use;
- conflict risk;
- refresh cadence; and
- action.

Then propose a minimal, curated knowledge-base structure.
```

## 5. Conversation decomposition planner

### Use when

A Project contains several distinct tasks that should not be mixed into one long thread.

```text
Decompose this recurring workstream into focused Project conversations.

Workstream:
[DESCRIBE WORKSTREAM]

For each proposed conversation, define:
- purpose;
- required Project knowledge;
- task-specific inputs;
- expected output;
- decisions that must be recorded for other threads;
- handoff artifact or checkpoint; and
- completion criteria.

Avoid assuming that one conversation automatically knows the full content of another conversation.
```

## 6. Artifact design brief

### Use when

The requested result should become a separate deliverable.

```text
Design an Artifact for the following deliverable.

Deliverable:
[DESCRIBE DELIVERABLE]

Audience:
[AUDIENCE]

Purpose:
[PURPOSE]

Define:
- artifact type;
- required sections;
- information hierarchy;
- editable components;
- tables, diagrams, or code blocks needed;
- source and citation requirements;
- accessibility requirements;
- review workflow;
- acceptance criteria; and
- export or handoff considerations.

Then produce a concise prompt for creating the Artifact.
```

## 7. Inline response versus Artifact decision

### Use when

You are unsure whether the answer should remain in the conversation.

```text
Determine whether the output below should be delivered inline or as an Artifact.

Requested output:
[OUTPUT]

Evaluate:
- expected length;
- revision cycles;
- whether another person will open or edit it;
- whether it has a document lifecycle;
- need for visual structure;
- need for live code or interactive content;
- permanence; and
- handoff requirements.

Return:
1. recommendation;
2. rationale;
3. proposed format; and
4. a creation prompt.
```

## 8. Web search versus Research decision

### Use when

A task requires current information, but the investigation depth is unclear.

```text
Determine whether this task needs:
- no external search;
- targeted web search in Chat; or
- Research.

Task:
[TASK]

Assess:
- number of questions;
- number and diversity of sources;
- freshness requirement;
- need for follow-up searches;
- expected conflicts among sources;
- required depth;
- time available;
- source-verification burden; and
- deliverable type.

Return:
1. recommended search mode;
2. research questions;
3. preferred primary sources;
4. inclusion and exclusion criteria;
5. date range;
6. verification plan; and
7. stopping criteria.
```

## 9. Research plan

### Use when

The task requires a deep, multi-source investigation.

```text
Create a research plan before collecting evidence.

Research objective:
[OBJECTIVE]

Define:
- primary and secondary research questions;
- decision or deliverable the research must support;
- preferred source hierarchy;
- date range;
- geographic or industry scope;
- inclusion and exclusion criteria;
- comparison dimensions;
- evidence-quality rubric;
- conflict-resolution method;
- citation requirements;
- known limitations; and
- completion criteria.

Do not begin synthesis until the plan is explicit.
```

## 10. Combined-workflow architect

### Use when

A professional task may need Project, Research, and Artifact together.

```text
Design an end-to-end Claude workflow for the task below.

Task:
[TASK]

Decide how to use:
- Chat;
- Project;
- Research;
- Artifact;
- human review; and
- external deterministic validation.

For each stage, specify:
- purpose;
- inputs;
- trusted configuration;
- source strategy;
- output;
- validation;
- responsible reviewer;
- information that carries to the next stage; and
- information that must not persist.

Prefer the least complex workflow that satisfies the requirements.
```

## 11. Entry-point workflow audit

### Use when

An existing Claude workflow feels inefficient or inconsistent.

```text
Audit this Claude workflow.

Current workflow:
[DESCRIBE CURRENT WORKFLOW]

Identify:
- repeated setup that belongs in a Project;
- temporary material incorrectly treated as standing context;
- deliverables trapped in chat that should be Artifacts;
- deep research attempted with isolated lookups;
- simple lookups over-engineered as Research;
- context that is duplicated or stale;
- missing source controls;
- missing review gates; and
- unnecessary feature complexity.

Return a current-state diagram, target-state diagram, migration steps, and success metrics.
```

## 12. Project exit and refresh review

### Use when

A Project may contain stale knowledge or no longer have a coherent purpose.

```text
Review this Project for maintenance, refresh, or retirement.

Project summary:
[SUMMARY]

Knowledge inventory:
[INVENTORY]

Assess:
- whether the purpose is still active;
- document freshness;
- obsolete or superseded sources;
- instruction conflicts;
- unauthorized or unnecessary data;
- conversation sprawl;
- reusable decisions that should be preserved;
- content that should be archived; and
- whether the Project should be split, refreshed, or retired.

Return an action plan with owners and due dates.
```

## Suggested study exercise

Use prompts 1, 2, 8, and 10 on the scenarios in the Core Entry Points lab. Compare the recommendation with the lesson's suggested answer and explain any difference.

## Related material

- [Lesson 3: Core Entry Points](../../modules/01-platform-model-foundations/lessons/03-core-entry-points.md)
- [Module 1 workflow-foundation prompts](01-workflow-foundation-prompts.md)
- [Lesson 2 behavior prompts](02-how-claude-behaves-prompts.md)
- [Task brief template](../task-brief-template.md)
