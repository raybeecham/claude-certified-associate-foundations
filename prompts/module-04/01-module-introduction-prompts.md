# Module 4 Notebook: Workflow Integration Introduction

Use these prompts to distinguish personal AI use from repeatable workflow integration and to begin delegation analysis without exposing confidential operating details.

---

## 1. Personal use versus workflow assessment

```text
Assess whether this example is:
- a personal productivity habit;
- an informal team practice; or
- a designed workflow.

Example:
[DESCRIPTION]

Evaluate:
- trigger;
- inputs;
- repeatability;
- stage ownership;
- validation;
- approval;
- state;
- failure handling;
- versioning; and
- business measurement.

Identify what must be added before the process can be treated as a reliable team workflow.
```

---

## 2. Business-outcome-first review

```text
Before proposing any AI integration, define the real workflow objective.

Use case:
[DESCRIPTION]

Return:
1. business outcome;
2. user or stakeholder need;
3. current process;
4. pain points;
5. success criteria;
6. consequence of error;
7. frequency and volume;
8. governing constraints; and
9. reasons Claude may or may not add value.

Do not begin with `where can we automate?`
```

---

## 3. Workflow-stage inventory

```text
Map the current workflow into stages.

For each stage, record:
- stage name;
- trigger;
- owner;
- input;
- work performed;
- output;
- decision or side effect;
- system of record;
- consequence if wrong;
- current validation;
- exception path; and
- candidate delegation mode.

Candidate delegation modes:
- AI-appropriate;
- human-retained;
- collaborative;
- deterministic;
- tool-owned; or
- storage-owned.
```

---

## 4. Delegation first-pass classifier

```text
Classify each workflow stage using the following modes:

AI-appropriate:
Probabilistic interpretation, classification, synthesis, or drafting under reviewable criteria.

Human-retained:
Authority, accountability, professional judgment, exception handling, or consequential approval.

Collaborative:
Claude prepares or analyzes while a human evaluates and decides.

Deterministic:
Exact calculations, fixed rules, authorization checks, schemas, routing, or validation.

Tool-owned:
Controlled retrieval, external action, or system interaction.

Storage-owned:
Durable state, authoritative records, logs, checkpoints, and version history.

For every classification, explain the controlling reason and required validation.
```

---

## 5. Task versus authority review

```text
Review this proposed delegation and separate the task from the authority behind it.

Proposal:
[DESCRIPTION]

Identify:
- what Claude may prepare;
- what Claude may recommend;
- what decision the workflow would make;
- who has legal, policy, professional, or organizational authority;
- what action or side effect follows;
- what validation must occur; and
- who remains accountable.

Flag any case where task assistance has silently become decision authority.
```

---

## 6. Collaborative workflow designer

```text
Design a collaborative workflow in which Claude assists but does not own consequential decisions.

Use case:
[DESCRIPTION]

Return:
1. Claude preparation steps;
2. deterministic checks;
3. human review points;
4. approval authority;
5. tool execution boundary;
6. durable state and evidence record;
7. exception and escalation path; and
8. release criteria.
```

---

## 7. Over-delegation detector

```text
Inspect this workflow for over-delegation.

Workflow:
[DESCRIPTION]

Flag stages where Claude is expected to:
- authorize;
- approve;
- accept material risk;
- perform exact calculations without deterministic checks;
- execute irreversible actions without approval;
- interpret governing rules without qualified review;
- store authoritative state only in conversation; or
- decide exceptions without policy ownership.

Recommend the smallest responsible redesign for each issue.
```

---

## 8. Personal-prompt production-readiness review

```text
A skilled user has a prompt that works well in personal use.

Prompt and use:
[DESCRIPTION]

Identify the unstated assumptions that must become explicit before a team can rely on it:
- authorized inputs;
- source hierarchy;
- task contract;
- acceptance criteria;
- stage ownership;
- validation;
- versioning;
- state;
- exceptions;
- failure recovery;
- approval; and
- monitoring.

Return a production-readiness gap list rather than merely rewriting the prompt.
```

---

## 9. Team A versus Team B comparison

```text
Compare two workflow designs that use the same AI capability.

Team A:
[WORKFLOW]

Team B:
[WORKFLOW]

Compare:
- delegated tasks;
- retained authority;
- validation;
- human review;
- side effects;
- state;
- exception handling;
- accountability; and
- likely failure modes.

Explain why the safer design is safer without assuming that less automation is always better.
```

---

## 10. Failure-path design

```text
Add failure handling to this proposed workflow.

Workflow:
[DESCRIPTION]

For each stage, define:
- detectable failure;
- timeout;
- retry rule;
- idempotency requirement;
- fallback;
- escalation owner;
- rollback or compensation;
- evidence retained; and
- condition that blocks continuation.
```

---

## 11. Workflow-value measurement

```text
Define success measures for this AI-assisted workflow.

Use case:
[DESCRIPTION]

Separate:
- activity metrics;
- stage quality metrics;
- operational metrics;
- risk metrics;
- human-review metrics; and
- business-outcome metrics.

Reject metrics that prove only usage volume, such as prompt count or generated pages, unless they support a defined business outcome.
```

---

## 12. Minimum-complexity architecture review

```text
Choose the least complex workflow pattern that satisfies the requirement.

Use case:
[DESCRIPTION]

Compare:
- interactive chat;
- fixed workflow;
- API-backed application; and
- bounded agent.

Evaluate repeatability, latency, state, tools, autonomy, exception rate, side effects, validation, and approval.

Recommend the simplest qualified pattern and explain why the more complex alternatives are unnecessary or risky.
```

---

## 13. Workflow introduction oral drill

Answer each in two or three sentences:

1. What is the difference between personal Claude use and workflow integration?
2. What is Delegation?
3. What is the difference between task delegation and decision delegation?
4. When is collaborative delegation preferable?
5. Which responsibilities usually belong outside the model?
6. Why is copying a successful personal prompt into production risky?
7. Why should workflow design begin with the business outcome?
8. What should a reliable workflow measure?

---

# Compact Module 4 introduction card

```text
BUSINESS OUTCOME
[WHAT MUST IMPROVE]

CURRENT WORKFLOW
[STAGES, OWNERS, INPUTS, OUTPUTS]

DELEGATION
[AI / HUMAN / COLLABORATIVE / DETERMINISTIC / TOOL / STORAGE]

AUTHORITY
[WHO MAY DECIDE OR APPROVE]

VALIDATION
[WHAT MUST BE CHECKED]

SIDE EFFECTS
[WHAT CHANGES OUTSIDE THE MODEL]

STATE
[WHERE DURABLE RECORDS LIVE]

FAILURE PATH
[RETRY / FALLBACK / ESCALATION / ROLLBACK]

MEASUREMENT
[QUALITY / TIME / RISK / BUSINESS OUTCOME]
```
