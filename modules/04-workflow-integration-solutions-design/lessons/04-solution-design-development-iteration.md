# Lesson 4: Solution Design, Development, and Iteration

## Overview

Claude is most useful in solution design when it participates in a controlled development loop rather than producing one large answer that is treated as final.

```text
Ideate
  ↓
Prototype
  ↓
Gather evidence and feedback
  ↓
Refine
  ↓
Re-test against acceptance criteria
  ↓
Accept, continue, or stop
```

> Claude is a design collaborator, not a vending machine.

The workflow succeeds when each iteration preserves the approved context, makes one bounded change, and produces observable evidence about whether the solution improved.

This lesson develops five capabilities:

1. generating a bounded option set before committing to a design;
2. converting one option into a testable prototype;
3. collecting structured user and validation feedback;
4. refining without losing prior requirements or introducing regressions; and
5. distinguishing a useful prototype from a production-ready solution.

---

# Plain-English explanation

A weak design workflow asks:

```text
Build the whole solution.
```

A stronger workflow asks:

```text
What are the requirements?
What options could satisfy them?
Which option should we prototype?
What should the prototype prove?
What feedback did we observe?
What one change should happen next?
What must be retested?
```

The goal is not to generate more versions. The goal is to reduce uncertainty with each version.

```text
New version
      ≠
Improved solution
```

An iteration counts as progress only when it improves a defined property such as usability, correctness, coverage, speed, accessibility, maintainability, or stakeholder fit.

---

# One analogy: an engineering test flight

Aircraft are not designed by drawing a final plane and immediately putting passengers aboard.

The team:

- evaluates design alternatives;
- builds a prototype;
- tests a bounded set of behaviors;
- records failures;
- changes the design;
- repeats the test; and
- expands the operating envelope only after evidence supports it.

AI-assisted solution design should follow the same logic.

A prototype demonstrates that an idea can work under stated conditions. It does not prove that the solution is safe, secure, maintainable, accessible, scalable, or approved for production.

```text
Prototype works in demo
      ≠
Production readiness
```

---

# The design loop

## Stage 1: Ideate

Generate several meaningfully different solution approaches.

For each option, capture:

- user and problem addressed;
- workflow pattern;
- model contribution;
- deterministic components;
- data and tools required;
- human review and approval;
- value hypothesis;
- major limitations;
- implementation effort; and
- testable risks.

Avoid producing cosmetic variants of one idea.

## Stage 2: Select a prototype hypothesis

Choose one option using explicit criteria.

Example:

```text
Hypothesis:
A lightweight interactive dashboard will reduce weekly metric-review preparation time while preserving human ownership of metric definitions and final reporting.
```

The prototype should answer a small number of questions:

- Can the user complete the core task?
- Are the important values represented correctly?
- Is the interaction understandable?
- Can the team identify the required controls?
- Is the proposed workflow materially better than the current one?

## Stage 3: Build the smallest useful prototype

A prototype should contain only enough functionality to test the highest-risk assumptions.

```text
Minimum useful prototype
      ≠
Minimum amount of thought
```

Define:

- included features;
- excluded features;
- test data;
- intended users;
- acceptance criteria;
- known limitations; and
- conditions under which the result must not be used.

## Stage 4: Gather evidence and feedback

Feedback should be observable and classified.

| Feedback class | Example |
|---|---|
| Requirement failure | Region filter missing |
| Correctness failure | Total does not match source data |
| Usability failure | Users cannot find the date control |
| Accessibility failure | Color alone communicates status |
| Performance failure | Large input causes unacceptable delay |
| Disclosure failure | Sensitive field appears in the view |
| Preference | Stakeholder prefers a different chart type |
| New requirement | Printed report needs a signature area |

Do not treat every comment as equal. Resolve release-blocking issues before preferences.

## Stage 5: Refine through bounded changes

Each refinement cycle should state:

```text
Observed problem
      ↓
Likely cause
      ↓
Requested change
      ↓
Expected improvement
      ↓
Regression checks
```

Change one coherent feature set at a time when practical. Large mixed revisions make it difficult to identify what improved or regressed.

## Stage 6: Re-test and decide

After every change:

- rerun affected acceptance tests;
- check preserved requirements;
- inspect calculations and data handling;
- compare against the previous version;
- record new limitations;
- decide continue, accept, redesign, or stop.

---

# Stable design context

Iteration fails when each round starts from a different understanding of the problem.

A stable design context should preserve:

- approved requirements;
- user personas and use cases;
- source and data definitions;
- prior decisions and rationale;
- acceptance criteria;
- design constraints;
- known risks;
- version history;
- unresolved questions; and
- current prototype state.

Projects can support this continuity by holding project knowledge, project instructions, and related conversations. Current official Claude documentation describes Projects as self-contained workspaces with project knowledge and instructions. Product behavior and availability can change.

```text
Stable context
      +
Versioned decisions
      +
Bounded change requests
      =
Cumulative iteration
```

Without stable context:

- previous constraints disappear;
- resolved decisions reopen;
- terminology drifts;
- requirements regress;
- one-off drafts accumulate; and
- the team cannot explain why the current design exists.

---

# Worked example: an internal metrics dashboard artifact

## Scenario

A fictional business analytics team maintains five operational metrics and needs a small internal interface for review meetings.

The goal is not to commission a production application immediately. The team first wants to test whether an interactive dashboard improves review speed and usability.

## Design contract

```text
Users: internal analysts and team leads
Data: approved synthetic metric dataset
Core purpose: view five metrics and inspect monthly changes
Human ownership: metric definitions and reporting decisions
Prototype type: interactive web artifact
Not authorized for: production reporting or sensitive data
```

## Cycle 1: Build the core view

Request:

```text
Create a simple interactive dashboard artifact using the supplied synthetic data.
Show the five approved metrics, one visual per metric, the reporting period,
and the data-source note. Do not invent missing values.
```

### What this cycle tests

- whether the five metrics can be represented;
- whether the labels are understandable;
- whether the source data is mapped correctly; and
- whether users can navigate the basic view.

### Acceptance checks

- all five metrics appear;
- metric names and units match the approved definitions;
- values match the source dataset;
- missing data is explicit; and
- no unapproved metric appears.

## Cycle 2: Add region filtering and totals

Observed feedback:

- users need to view one region at a time;
- totals must update with the filter; and
- the current design does not make the active filter obvious.

Change request:

```text
Add a region filter.
Recompute the summary totals from the filtered records rather than using static values.
Show the active region clearly and include an All Regions option.
Preserve the five metric definitions and existing source note.
```

### Regression checks

- unfiltered totals still reconcile;
- each region includes only its records;
- filters do not change metric definitions;
- empty regions display a clear no-data state; and
- charts and summary values use the same filtered dataset.

## Cycle 3: Improve change signals and printing

Observed feedback:

- month-over-month change is hard to scan;
- the dashboard must print cleanly for a meeting packet; and
- color-only meaning would create an accessibility problem.

Change request:

```text
Add month-over-month change indicators.
Use color plus an arrow and text label so meaning does not depend on color alone.
Apply the approved direction-of-improvement rule for each metric.
Create a print layout with readable labels, source note, reporting period,
and page breaks that do not split metric cards.
```

### Important correction to a simplistic color rule

`Green for increase` is not universally correct. For some metrics, such as defects or wait time, a decrease may represent improvement.

The workflow therefore requires a maintained metadata field:

| Metric | Improvement direction |
|---|---|
| Customer satisfaction | Higher |
| Completion rate | Higher |
| Average wait time | Lower |
| Defect rate | Lower |
| Open backlog | Lower, subject to context |

The artifact should apply the approved rule rather than infer it.

## What the example proves

The team can create and refine a working prototype by describing changes instead of writing code directly.

It does **not** prove:

- the artifact is secure for sensitive data;
- the calculations are correct without testing;
- the solution supports enterprise scale;
- the interface meets every accessibility requirement;
- the artifact has durable production storage;
- sharing permissions are appropriate; or
- the organization has approved deployment.

Current Claude guidance notes that artifact sharing or publishing can expose the artifact and, in some contexts, attached files or conversation materials. Review current product documentation and organizational data policy before sharing.

---

# Prototype versus production

| Prototype question | Production question |
|---|---|
| Can users complete the core task? | Can authorized users complete it reliably at required scale? |
| Does the concept communicate value? | Are value, cost, controls, and ownership operationally sustainable? |
| Do sample values render? | Are data lineage, reconciliation, privacy, and retention controlled? |
| Does the interaction work? | Are accessibility, security, monitoring, and support requirements met? |
| Can the team revise quickly? | Are versions, releases, rollback, and change control governed? |

A prototype can be accepted for learning while rejected for production deployment.

---

# Feedback and decision log

Maintain a design log:

| Cycle | Observation | Classification | Decision | Change | Acceptance test | Result |
|---|---|---|---|---|---|---|
| 1 | Region view absent | Requirement | Add | Region filter | Totals reconcile by region | Pass/Fail |
| 2 | Color-only signal | Accessibility | Revise | Add text and arrows | Meaning visible in grayscale | Pass/Fail |

Also record rejected feedback and why. Otherwise the same request may return in later cycles without context.

---

# Iteration stopping rules

Continue when:

- material acceptance criteria are still unmet;
- the next change is bounded and testable;
- evidence suggests the change will improve the solution;
- the prototype remains the appropriate vehicle; and
- review capacity is available.

Stop or escalate when:

- the prototype meets its learning objective;
- changes become cosmetic with no measurable value;
- requirements conflict;
- evidence or authority is missing;
- architecture, security, accessibility, or data issues exceed the prototype scope;
- the solution needs production engineering; or
- the team cannot define what success means.

```text
More iteration
      ≠
More progress
```

---

# Design and iteration protocol

```text
1. Establish the approved design context
2. Generate meaningfully different options
3. Select one option using explicit criteria
4. Define prototype hypothesis and scope
5. Build the smallest useful prototype
6. Test against requirements and high-risk assumptions
7. Classify feedback
8. Make bounded changes
9. Run regression and acceptance checks
10. Record decisions and limitations
11. Accept, continue, redesign, escalate, or stop
```

---

# Common anti-patterns

## One-shot final solution

**Failure:** A large initial draft is treated as complete.

**Repair:** Create a bounded prototype and evidence-driven iteration plan.

## Unstable context

**Failure:** Each round reinterprets users, requirements, or terminology.

**Repair:** Maintain Project knowledge, instructions, requirement baseline, and decision log.

## Feedback without classification

**Failure:** Preferences displace correctness or release-blocking issues.

**Repair:** Classify requirement, correctness, usability, accessibility, performance, disclosure, and preference feedback.

## Revision without regression testing

**Failure:** A new filter fixes one request but breaks totals or existing behavior.

**Repair:** Define affected and preserved acceptance tests before changing the prototype.

## Feature accumulation

**Failure:** Every suggestion becomes a feature.

**Repair:** Require connection to user outcome, requirement, evidence, and priority.

## Prototype treated as production

**Failure:** A successful demo bypasses security, data, accessibility, operational, and approval review.

**Repair:** Use a production-readiness gate separate from prototype acceptance.

## Model-owned design authority

**Failure:** Claude chooses requirements, trade-offs, and final acceptance without accountable owners.

**Repair:** Retain human product, domain, risk, and approval ownership.

---

# Exam reasoning pattern

```text
Need several approaches          → ideate bounded alternatives
Need to test one idea            → build smallest useful prototype
Feedback received                → classify and prioritize
Change requested                 → define expected effect and regression tests
Repeated iterations drift        → stabilize Project context and decisions
Prototype looks successful       → still apply production-readiness gate
Cosmetic rounds with no gain     → stop or escalate
```

For scenario questions:

1. confirm the requirement baseline;
2. generate options before committing;
3. define what the prototype must prove;
4. keep scope bounded;
5. gather observable feedback;
6. distinguish defects from preferences;
7. refine with controlled change requests;
8. rerun affected and preserved tests;
9. retain human authority over requirements and acceptance; and
10. distinguish prototype success from deployment approval.

---

# Knowledge check

## Question 1

Why is an iteration loop stronger than a one-shot request?

**Answer:** It exposes assumptions through a testable prototype, gathers evidence, and lets the team correct bounded defects while preserving approved requirements.

## Question 2

Why use a Project for recurring design work?

**Answer:** It can preserve project-specific knowledge and instructions across related chats, helping maintain stable requirements, terminology, and prior decisions.

## Question 3

Does a working artifact prove production readiness?

**Answer:** No. Security, data handling, accessibility, scale, monitoring, support, version control, and approval remain separate concerns.

## Question 4

What makes feedback actionable?

**Answer:** It identifies an observed problem, its class and impact, the requested change, expected result, and the acceptance or regression test.

## Question 5

When should iteration stop?

**Answer:** When the learning objective is met, changes no longer produce measurable value, or unresolved architecture, authority, evidence, or production concerns require escalation.

---

# Flashcards

## Flashcard 1

**Q:** What is the core iteration loop?

**A:** Ideate, prototype, gather feedback, refine, and re-test.

## Flashcard 2

**Q:** What should a prototype prove?

**A:** A bounded set of high-risk assumptions and core user tasks.

## Flashcard 3

**Q:** What is stable design context?

**A:** Approved requirements, constraints, users, data definitions, decisions, tests, risks, and version history preserved across iterations.

## Flashcard 4

**Q:** Why classify feedback?

**A:** To prioritize correctness and requirement failures over preferences and avoid uncontrolled feature accumulation.

## Flashcard 5

**Q:** What is regression testing?

**A:** Rechecking previously working requirements after a change to confirm they remain intact.

## Flashcard 6

**Q:** What is the prototype-production distinction?

**A:** A prototype tests an idea; production requires operational, security, data, accessibility, scale, support, and governance controls.

---

# Short recap

```text
1. Treat Claude as a design collaborator.
2. Generate alternatives before selecting a design.
3. Build the smallest prototype that tests the risky assumptions.
4. Preserve context and decisions across rounds.
5. Gather observable, classified feedback.
6. Make bounded changes with expected outcomes.
7. Run acceptance and regression tests.
8. Record decisions, rejected feedback, and limitations.
9. Stop when learning is complete or progress plateaus.
10. Never confuse a working prototype with production approval.
```

> A solution emerges when each iteration reduces uncertainty and preserves what the team has already learned.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute product, software, security, accessibility, legal, or operational advice.

## Source and currency note

The preparation-course material was supplied on August 3, 2026. Product-specific statements were checked against official Claude Help Center information on Projects and artifact sharing on August 3, 2026. Current documentation, terms, policies, capability settings, and organizational rules control when they differ.

Official references:

- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Publish and share artifacts](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)

## Related material

- [Research, Planning, and Process Optimization](03-research-planning-process-optimization.md)
- [Analyzing Requirements and Use Cases](02-analyzing-requirements-use-cases.md)
- [Module 4 overview](../README.md)
- [Solution Design and Iteration prompts](../../../prompts/module-04/04-solution-design-development-iteration-prompts.md)
- [Evidence-Driven Prototype Iteration Pattern](../../../patterns/evidence-driven-prototype-iteration-pattern.md)
