# Lesson 1: Module Introduction — Workflow Integration & Solution Design

## Overview

There is a meaningful difference between using Claude as an individual and designing a workflow that uses Claude repeatedly.

```text
Personal productivity use
        ↓
One person prompts, reviews, and adapts as needed

Workflow integration
        ↓
A team runs a repeatable process with defined stages,
responsibilities, controls, and outcomes
```

The value of AI compounds when a useful interaction becomes a reliable workflow. The risk also compounds when the wrong stages are delegated, when human authority is removed, or when a probabilistic model is treated as though it were a deterministic system.

> Workflow value comes from deliberate delegation, not maximum automation.

This lesson introduces the module's anchor competency: **Delegation**.

Delegation asks, for each stage of a workflow:

- Is this step appropriate for AI assistance?
- Must a human retain the work or decision?
- Should the step be collaborative?
- Does an exact rule, calculation, tool, or system of record belong here instead?
- What validation and approval are required before the result moves forward?

---

# Plain-English explanation

Saying `I use Claude` usually means one person chooses when to ask for help and personally interprets the result.

Saying `our workflow uses Claude` means the organization has decided:

- when Claude is used;
- what Claude receives;
- what Claude is expected to produce;
- what Claude is not allowed to decide;
- which systems or tools are involved;
- who checks the work;
- who approves consequential actions;
- what happens when the process fails; and
- how success is measured.

A helpful individual habit does not become a reliable organizational process merely because more people copy the prompt.

```text
Repeated prompting
      ≠
Designed workflow
```

The workflow must make responsibility explicit.

---

# One analogy: adding a new role to an assembly line

Imagine a factory introduces a new automated station.

The question is not simply:

```text
Can this machine perform work?
```

The design team must ask:

- Which task should the station perform?
- What inputs must arrive in what condition?
- Which measurements must be exact?
- Who checks defects?
- What happens if the station stops?
- Can the station create an irreversible problem?
- Which decisions remain with skilled operators?

Claude integration works the same way.

A model may be useful at interpreting, summarizing, classifying, drafting, or proposing options. That does not mean it should approve obligations, authorize payments, alter official records, or make unsupported professional decisions.

> The goal is not to put Claude at every station. The goal is to put the right capability at each station.

---

# Two teams, same process, different delegation

Consider a fictional contract-review workflow.

Both teams use Claude to accelerate review.

## Team A: bounded collaboration

```text
Contract received
      ↓
Claude extracts clauses and drafts proposed redlines
      ↓
Deterministic checks confirm required fields and clause inventory
      ↓
Lawyer reviews evidence, interpretation, and proposed changes
      ↓
Lawyer approves or rejects every final decision
```

### Result

- review effort decreases;
- the lawyer remains the accountable decision-maker;
- Claude performs bounded preparation work;
- evidence and changes remain visible; and
- quality controls stay in the workflow.

## Team B: authority delegated too far

```text
Contract received
      ↓
Claude interprets and classifies clauses
      ↓
Claude approves clauses labeled low risk
      ↓
Only selected clauses receive human review
```

### Failure

A clause is classified incorrectly and creates an obligation that no authorized reviewer examined.

The failure is not merely `Claude made a mistake`.

The workflow assigned final authority to a component that could not own the legal judgment or accountability.

## Core distinction

```text
Useful AI task
      ≠
Safe AI-owned decision
```

The design question is not whether the model can produce an answer. It is whether the workflow should rely on that answer at that stage and under those controls.

---

# Delegation as the anchoring competency

Delegation is the deliberate assignment of work across humans, models, deterministic systems, tools, and storage.

A useful first-pass classification is:

| Delegation mode | Meaning |
|---|---|
| **AI-appropriate** | Claude can perform the step within defined boundaries and validation |
| **Human-retained** | The step requires authority, accountability, professional judgment, or contextual responsibility that must remain human |
| **Collaborative** | Claude assists with preparation, analysis, options, or drafting while a human evaluates and decides |
| **Deterministic or tool-owned** | The step requires an exact rule, calculation, authorization check, external action, or system-of-record operation |

## AI-appropriate examples

- extracting candidate requirements;
- summarizing a verified source package;
- classifying text under a reviewable taxonomy;
- drafting alternatives;
- identifying possible process bottlenecks;
- generating test cases; and
- comparing options against explicit criteria.

## Human-retained examples

- final legal interpretation;
- professional approval;
- decisions affecting rights, employment, benefits, safety, or eligibility;
- acceptance of material risk;
- exception handling where policy is ambiguous;
- approval of public or regulatory communications; and
- accountability for release.

## Deterministic or tool-owned examples

- exact arithmetic;
- authorization checks;
- schema validation;
- duplicate detection;
- fixed routing rules;
- durable state updates;
- sending, filing, deleting, or modifying records; and
- audit logging.

## Collaborative examples

```text
Claude prepares
      ↓
Human evaluates
      ↓
Tool or deterministic component executes
      ↓
Human or organization remains accountable
```

This is often the strongest pattern for consequential work.

---

# The difference between task delegation and decision delegation

Teams often confuse delegating a task with delegating the authority behind it.

## Task delegation

Claude may:

- extract provisions;
- summarize evidence;
- draft a recommendation;
- identify inconsistencies; or
- propose a plan.

## Decision delegation

A workflow may then use the output to:

- approve a clause;
- deny a request;
- publish a statement;
- authorize spending;
- alter a production system; or
- file an official record.

These are different levels of responsibility.

```text
Generate recommendation
      ≠
Authorize action
```

The farther a workflow moves from reversible preparation toward consequential action, the stronger the deterministic controls, validation, human review, and approval requirements become.

---

# Personal use versus organizational workflow

| Dimension | Personal Claude use | Team workflow using Claude |
|---|---|---|
| Trigger | Individual decides when to ask | Defined event, stage, or request |
| Inputs | Selected informally | Authorized and curated input contract |
| Prompt | Adapted conversationally | Versioned task or workflow specification |
| State | Often held in conversation | Persisted in a durable system |
| Output | Read by the user | Passed to people, systems, or later stages |
| Validation | User judgment | Defined checks and acceptance criteria |
| Approval | Usually the same person | Assigned reviewer and approver roles |
| Failure handling | User retries manually | Timeout, retry, escalation, fallback, or rollback |
| Accountability | Individual | Named role or organization |
| Measurement | Subjective usefulness | Stage-level and business outcomes |

The shift to workflow integration requires the informal decisions made by one skilled user to become explicit enough for a team and system to repeat safely.

---

# The module learning objectives

By the end of Module 4, the learner should be able to:

1. apply Claude to analyze requirements and use cases;
2. leverage Claude for research, planning, and process optimization;
3. use Claude to support solution design, development, and iteration;
4. integrate Claude into existing workflows to augment or redesign them; and
5. communicate Claude's value and limitations accurately to stakeholders.

These outcomes follow one progression:

```text
Understand the real requirement
      ↓
Map the current workflow
      ↓
Identify appropriate delegation opportunities
      ↓
Design the future workflow and controls
      ↓
Test and iterate
      ↓
Communicate value, limitations, and ownership
```

---

# The deal in this module

This module does not treat automation as the default objective.

The objective is to improve the workflow while preserving the responsibilities that must remain human, deterministic, controlled, or externally authorized.

The module will ask:

- What business problem is being solved?
- What does the current workflow actually do?
- Which stages contain repetitive language work?
- Which stages require exact rules or calculations?
- Which stages create side effects?
- Which decisions require human authority?
- Where should state be stored?
- What evidence establishes success?
- How should failure and exception paths work?
- How should value and limitations be explained?

A strong workflow may use Claude in one narrow stage, several collaborative stages, or not at all in parts where the model adds no reliable value.

---

# A delegation-first workflow review

Use this introductory review sequence:

```text
1. Define the business outcome
          ↓
2. Map the current stages and owners
          ↓
3. Identify decisions, calculations, actions, and state
          ↓
4. Mark each stage AI-appropriate, human-retained,
   collaborative, deterministic, or tool-owned
          ↓
5. Add validation and approval boundaries
          ↓
6. Define failure, fallback, and escalation behavior
          ↓
7. Measure workflow and business outcomes
```

## Stage inventory template

| Stage | Current owner | Input | Work performed | Output | Consequence if wrong | Candidate delegation |
|---|---|---|---|---|---|---|
| Stage name | Role/system | Source | Activity | Result | Low/material/high | AI / Human / Collaborative / Deterministic / Tool |

The stage inventory does not decide the final architecture. It makes the work visible enough to reason about.

---

# Common failure modes introduced by this lesson

## Automate-first thinking

**Failure:** The team begins with `Where can we add Claude?` rather than the business requirement.

**Repair:** Define the outcome, current process, and acceptance criteria first.

## Delegating authority with the task

**Failure:** Because Claude drafts or classifies an item, the workflow also lets it approve the item.

**Repair:** Separate preparation from authorization.

## Copying a personal prompt into production

**Failure:** A skilled user's unstated context and judgment are missing when others run the prompt.

**Repair:** Make inputs, criteria, validation, state, ownership, and exceptions explicit.

## Treating every step as AI-appropriate

**Failure:** Exact calculations, fixed policy rules, authorization, and irreversible actions are assigned to the model.

**Repair:** Use deterministic logic, controlled tools, systems of record, and human approval.

## Measuring activity rather than value

**Failure:** Success is defined as number of prompts, generated pages, or adoption rate.

**Repair:** Measure cycle time, quality, error rate, review effort, escalation, and the business outcome.

## Ignoring failure paths

**Failure:** The workflow describes the happy path only.

**Repair:** Define timeout, retry, fallback, escalation, rollback, and correction ownership.

---

# Exam reasoning pattern

For introductory workflow-integration scenarios:

1. identify the real business objective;
2. distinguish personal productivity from a repeatable team process;
3. map the workflow into stages;
4. separate task assistance from decision authority;
5. identify AI-appropriate, human-retained, collaborative, deterministic, and tool-owned work;
6. preserve human accountability for consequential decisions;
7. place validation before side effects;
8. prefer bounded assistance over uncontrolled automation;
9. measure business outcomes rather than model activity; and
10. choose the simplest workflow that meets the requirement.

```text
One person uses a strong prompt      → productivity habit
Team repeats controlled stages       → workflow integration
Claude drafts, human decides          → collaborative delegation
Claude approves consequential action → over-delegation
Exact fixed rule assigned to model    → move to deterministic logic
No failure path                       → add fallback and escalation
```

---

# Knowledge check

## Question 1

What is the difference between `I use Claude` and `our workflow uses Claude`?

**Answer:** Personal use depends on one person's judgment during a conversation. A workflow defines repeatable triggers, inputs, stages, responsibilities, controls, validation, failure handling, and ownership for a team or system.

## Question 2

What is the module's anchoring competency?

**Answer:** Delegation: deciding which work is AI-appropriate, human-retained, collaborative, deterministic, or tool-owned.

## Question 3

Why was Team B's contract workflow unsafe?

**Answer:** It delegated approval authority along with classification work, allowing an unreviewed model judgment to create a consequential obligation.

## Question 4

Does a step being useful for Claude mean Claude should own the final decision?

**Answer:** No. Claude may prepare evidence, options, classifications, or drafts while a human or deterministic control retains authority.

## Question 5

Which responsibilities generally belong outside the model?

**Answer:** Exact calculations, fixed business rules, authorization, durable state, controlled external actions, and consequential approval.

## Question 6

What makes a personal AI interaction repeatable as a workflow?

**Answer:** Explicit inputs, task contracts, stage ownership, validation, approvals, state, failure behavior, versioning, and measurable outcomes.

## Question 7

What should a team ask before deciding where to use Claude?

**Answer:** What business outcome is required, how the current process works, what each stage requires, and which responsibilities are appropriate to delegate.

---

# Flashcards

## Flashcard 1

**Q:** What turns individual AI use into workflow integration?

**A:** Repeatable stages with explicit inputs, responsibilities, controls, validation, state, failure handling, and ownership.

## Flashcard 2

**Q:** What is Delegation?

**A:** The deliberate assignment of workflow responsibilities across AI, humans, deterministic logic, tools, and storage.

## Flashcard 3

**Q:** What is over-delegation?

**A:** Assigning authority, irreversible action, or accountable judgment to the model merely because it can assist with the underlying task.

## Flashcard 4

**Q:** What is collaborative delegation?

**A:** Claude prepares or analyzes while a human evaluates, decides, and remains accountable.

## Flashcard 5

**Q:** Where should exact rules and calculations usually live?

**A:** In deterministic components or authoritative systems rather than free-form model judgment.

## Flashcard 6

**Q:** What is the first workflow-design question?

**A:** What business outcome and user need must the workflow satisfy?

## Flashcard 7

**Q:** Why is copying a personal prompt into a team process risky?

**A:** The original user's unstated context, judgment, corrections, and exception handling may not be captured.

## Flashcard 8

**Q:** What should workflow success measure?

**A:** Quality, cycle time, review effort, error and escalation rates, reliability, and the business outcome—not prompt volume alone.

---

# Short recap

```text
1. Personal Claude use is not automatically workflow integration.
2. A workflow requires repeatable stages, controls, state, and ownership.
3. Delegation is the module's anchoring competency.
4. Separate task assistance from decision authority.
5. Use Claude for bounded probabilistic work.
6. Use deterministic systems for exact rules and calculations.
7. Use controlled tools for external actions and storage for durable state.
8. Retain qualified human judgment and accountability.
9. Design failure, fallback, and escalation paths.
10. Measure business outcomes rather than automation volume.
```

> Workflow value comes from deciding what to delegate—not from automating everything.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, architecture, security, operational, or other professional advice.

## Source note

This lesson expands the Module 4 introduction supplied on **August 2, 2026**. Product capabilities, terms, policies, and documentation can change. Current official Anthropic terms, policies, and documentation control if they conflict with course or repository material.

## Related material

- [Module 4 overview](../README.md)
- [Module 4 introduction prompt notebook](../../../prompts/module-04/01-module-introduction-prompts.md)
- [Module 3 completion](../../03-evaluating-validating-output/lessons/10-module-complete.md)
- [Workflow Design Canvas](../../../ai-systems-engineering/worksheets/workflow-design-canvas.md)
- [Governance Canvas](../../../ai-systems-engineering/worksheets/governance-canvas.md)
