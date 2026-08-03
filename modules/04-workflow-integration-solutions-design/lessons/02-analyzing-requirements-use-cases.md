# Lesson 2: Analyzing Requirements and Use Cases with Claude

## Overview

Most workflows begin with unstructured evidence rather than a clean specification.

Inputs may include:

- long documents;
- email threads;
- meeting notes;
- verbal requests;
- forms;
- policies;
- statements of work;
- evaluation criteria; and
- examples from prior work.

Before a workflow can be designed, these inputs must be converted into requirements that are:

- distinct;
- traceable;
- testable;
- owned;
- prioritized;
- explicit about uncertainty; and
- usable by the people who will build or execute the process.

> Claude is useful for translating unstructured material into a reviewable requirements model. The human team still owns interpretation, clarification, prioritization, and approval.

This lesson develops five capabilities:

1. extracting requirements from messy source material;
2. translating broad business needs into task definitions;
3. preserving traceability to source locations;
4. distinguishing explicit, implied, ambiguous, missing, and conflicting requirements; and
5. pressure-testing the resulting requirement set before solution design begins.

---

# Plain-English explanation

A request such as:

```text
We need better reporting.
```

is a business need, not yet a buildable requirement.

A requirements analysis must answer:

```text
What report?
For which audience?
For which decision?
How often?
Using what data?
With what fields and calculations?
In what format?
By when?
Who owns it?
What makes it acceptable?
```

Claude can help generate and organize these questions, but it should not silently decide the answers.

```text
Messy source material
      ↓
Candidate requirements
      ↓
Traceability and classification
      ↓
Ambiguity and gap review
      ↓
Human clarification and approval
      ↓
Testable requirement baseline
```

---

# One analogy: turning a conversation into construction drawings

Imagine a client tells an architect:

```text
We need a better office.
```

That statement does not tell a construction team what to build.

The architect must determine:

- how many people will use it;
- what rooms are required;
- accessibility obligations;
- security needs;
- power and network requirements;
- budget;
- schedule;
- approval authority; and
- what success means.

Claude can help organize the notes and surface missing questions. It cannot replace the client, engineer, regulator, or authorized decision-maker.

> Requirements analysis turns wishes into drawings that can be reviewed, built, and tested.

---

# Business need versus task definition

A business need explains the desired improvement.

A task definition explains what work must be performed and how completion will be judged.

| Business need | Testable task definition |
|---|---|
| Better reporting | Produce a weekly operational report for regional managers using approved service data, with five required metrics and exception notes, delivered as an editable spreadsheet by 9:00 a.m. each Monday |
| Faster proposal response | Extract every RFP requirement into a traceability table within one business day and assign each open response to an owner |
| Improve customer support | Classify incoming requests using the approved taxonomy, route high-severity cases immediately, and preserve human review for exceptions |
| Reduce review effort | Generate a first-pass evidence inventory while retaining final interpretation and approval with the qualified reviewer |

A complete task definition should usually identify:

```text
Actor
Purpose
Trigger
Inputs
Work
Output
Audience
Frequency or deadline
Constraints
Acceptance criteria
Owner and approver
Failure or escalation behavior
```

---

# Requirements classification

Do not place every extracted statement into one undifferentiated list.

Use controlled classes.

| Class | Meaning | Required action |
|---|---|---|
| **Explicit** | Directly stated in the source | Preserve exact meaning and location |
| **Implied** | Reasonably suggested by another clause, criterion, or dependency | Mark as inference and obtain confirmation |
| **Ambiguous** | Supports more than one material interpretation | Draft a clarification question |
| **Missing** | Needed to make the task buildable or testable but absent from the source | Assign an owner to resolve it |
| **Conflicting** | Two sources or passages cannot both control as written | Identify source authority and escalate |
| **Assumption** | Temporary working premise used to continue analysis | Record owner, risk, and expiration |
| **Constraint** | Limits the solution or method | Link to affected requirements |
| **Acceptance criterion** | Defines observable completion or quality | Make it measurable where possible |

The central safeguard is:

```text
Extracted fact
      ≠
Implied requirement
      ≠
Analyst assumption
```

Every row should make that distinction visible.

---

# Requirements traceability table

A practical output is a structured table rather than a narrative summary.

| ID | Requirement | Class | Source | Location | Status | Existing answer/evidence | Ambiguity or gap | Owner | Acceptance criterion |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | Provide transition approach | Explicit | RFP | §3.2.1 | Open | Partial email response | Duration not specified | Transition lead | Approach addresses all listed phases |
| R-002 | Include staffing assumptions | Implied | Evaluation criterion | §6.4 | Needs confirmation | None | Required depth unclear | Proposal manager | Clarification accepted or assumption approved |

Traceability supports:

- source verification;
- coverage checking;
- assignment;
- change control;
- test design;
- auditability; and
- later workflow mapping.

A short label is useful for navigation, but it must not replace the full requirement text or source location.

---

# Worked example: an RFP response workflow

## Scenario

A fictional proposal team receives:

- a 40-page RFP;
- several amendments;
- evaluation criteria;
- a scattered internal email thread;
- prior approved response material; and
- partial answers from subject-matter experts.

The recurring task is to convert the package into an answerable requirement inventory.

## Initial extraction prompt

```text
Use only the supplied RFP package and internal response thread.

Extract every distinct requirement the client asks the bidder to address.
For each requirement, return:
- requirement ID;
- short label;
- full requirement statement;
- explicit, implied, ambiguous, conflicting, or missing classification;
- controlling source document;
- exact section, page, or clause;
- whether the response thread contains a complete, partial, conflicting, or absent answer;
- the evidence location for any existing answer;
- clarification needed;
- proposed owner; and
- testable completion criterion.

Do not convert an inference into an explicit client requirement.
Use `not found` when the source package does not support a field.
Return a table and a separate list of source conflicts.
```

## Resulting workflow asset

The team receives a requirements register where each row can be:

- verified against the RFP;
- assigned to an owner;
- linked to evidence;
- marked complete or open;
- challenged for ambiguity; and
- used to check proposal coverage.

This is more useful than a prose summary because the team can act on each row independently.

---

# Pressure-testing the extracted requirements

Extraction creates a candidate list. Pressure-testing determines whether the list is safe to use.

Use a second pass with a different objective:

```text
Review the extracted requirement register against the full source package.

Identify:
- requirements that support more than one interpretation;
- subordinate clauses that add conditions or exceptions;
- evaluation criteria that imply response obligations;
- requirements that were split incorrectly or combined too broadly;
- duplicate requirements stated in different places;
- conflicts among the base document, amendments, and internal answers;
- missing actors, deadlines, formats, data sources, owners, or acceptance criteria;
- assumptions presented as source facts; and
- requirements whose completion cannot yet be tested.

For each issue, state the affected requirement ID, evidence location, risk, and recommended clarification or correction.
```

## Why the second pass matters

A first extraction may fail by:

- overlooking a requirement buried in a subordinate clause;
- treating an evaluation criterion as descriptive rather than consequential;
- combining separate obligations into one row;
- overlooking an amendment that supersedes the base document;
- interpreting an example as a mandatory requirement;
- accepting an internal answer that does not address the client question; or
- inventing a missing detail to make the table look complete.

Pressure-testing applies Module 3 Discernment earlier in the workflow.

```text
Requirement extracted
      ↓
Check source support
      ↓
Check completeness and interpretation
      ↓
Clarify or approve
```

---

# Requirement quality test

A strong requirement should satisfy the following where applicable.

| Property | Question |
|---|---|
| Necessary | Does it support the business objective or controlling source? |
| Traceable | Can the reviewer find its source and location? |
| Clear | Would two qualified readers interpret it similarly? |
| Atomic | Does the row contain one independently trackable obligation? |
| Feasible | Can the workflow or team reasonably satisfy it? |
| Testable | Can completion be observed or measured? |
| Bounded | Are scope, conditions, and exclusions visible? |
| Owned | Is someone responsible for resolution or delivery? |
| Authorized | Has an appropriate person approved the interpretation? |
| Current | Does the requirement reflect the controlling version? |

Do not force certainty where the source is incomplete.

A requirement can remain:

- open;
- ambiguous;
- conflicting;
- blocked;
- assumed pending confirmation; or
- not supported by the supplied materials.

---

# From requirements to use cases

A requirement set does not automatically prove that Claude should be used.

A viable use case connects:

```text
Business outcome
      +
User or stakeholder
      +
Repeatable task
      +
Authorized inputs
      +
Measurable output
      +
Acceptable risk
      +
Clear human ownership
```

## Use-case definition template

| Dimension | Question |
|---|---|
| Outcome | What measurable improvement is sought? |
| User | Who performs or receives the work? |
| Current process | How is the work done today? |
| Trigger | What starts the workflow? |
| Inputs | Which sources and systems are authorized? |
| AI contribution | What probabilistic language work is appropriate? |
| Retained human work | Which decisions, exceptions, and approvals remain human? |
| Deterministic work | Which rules, calculations, and validations require code or fixed logic? |
| Output | What artifact or action is produced? |
| Acceptance criteria | How is quality and completion measured? |
| Risks | What can go wrong and who is affected? |
| Escalation | What blocks automation or requires expert review? |

## Capability trap

Weak framing:

```text
Claude can summarize documents, so we should automate document review.
```

Stronger framing:

```text
The proposal team spends eight hours per RFP manually building a requirement inventory.
Claude may extract and organize candidate requirements from the authorized package,
while proposal leadership validates interpretation and owns final coverage.
Success is measured by requirement recall, source traceability, cycle time,
and the number of material omissions found during final review.
```

A product capability becomes a use case only when it is tied to an operational problem and controlled outcome.

---

# Project versus one-off conversation

The recurring RFP workflow is better suited to a Project than an isolated chat because the work benefits from:

- a persistent project knowledge base;
- project-specific instructions;
- recurring source and formatting conventions;
- repeatable chats within one workspace; and
- stable context for the proposal workflow.

Current official Claude guidance states that Projects provide self-contained workspaces with project knowledge and project instructions used across chats within that project. Official Skills guidance describes Skills as reusable procedures that load when relevant and can work across Claude rather than being limited to one Project. citeturn472072search0turn472072search1turn472072search3

A durable division is:

```text
Project knowledge      → project-specific background and approved sources
Project instructions   → project-specific behavior and output expectations
Skill                   → reusable procedure for a repeatable task
Human review            → interpretation, clarification, prioritization, approval
```

This lesson uses that product distinction only to explain workspace fit. Module 5 covers configuration and knowledge management in depth.

---

# Requirements-analysis protocol

```text
1. Define the business need and intended decision
          ↓
2. Inventory and classify the source package
          ↓
3. Identify controlling and superseded sources
          ↓
4. Extract atomic candidate requirements with traceability
          ↓
5. Classify explicit, implied, ambiguous, missing, conflicting, and assumed items
          ↓
6. Link existing answers and evidence
          ↓
7. Pressure-test interpretation, completeness, conflicts, and testability
          ↓
8. Resolve or assign clarifications
          ↓
9. Approve the requirement baseline
          ↓
10. Convert approved requirements into workflow stages and acceptance tests
```

---

# Common anti-patterns

## Narrative summary instead of requirements register

**Failure:** Obligations cannot be assigned, tested, or checked for coverage.

**Repair:** Return atomic rows with source locations and statuses.

## Treating inferred requirements as explicit

**Failure:** The team may commit to an obligation the source never imposed.

**Repair:** Label inference and require human confirmation.

## One-pass extraction

**Failure:** Hidden, subordinate, conflicting, or duplicate requirements remain undetected.

**Repair:** Use a separate pressure-test pass against the full source package.

## Ignoring source authority

**Failure:** An old draft, email, or base document overrides a controlling amendment.

**Repair:** Define the source hierarchy and current version before extraction.

## Missing acceptance criteria

**Failure:** The team cannot prove completion.

**Repair:** Convert each approved requirement into an observable test where possible.

## Solving ambiguity with confident prose

**Failure:** The output looks complete but hides unresolved decisions.

**Repair:** Preserve ambiguous, missing, conflicting, and not-supported statuses.

## Starting from Claude's capabilities

**Failure:** A feature is mistaken for a viable use case.

**Repair:** Begin with the business outcome, current process, users, risk, and acceptance criteria.

## Uploading an undifferentiated source pile

**Failure:** Drafts, amendments, reference examples, and internal answers are treated as equally authoritative.

**Repair:** Label each source's role and authority before analysis.

---

# Exam reasoning pattern

For requirements and use-case scenarios:

1. start with the business outcome rather than the feature;
2. request structured extraction rather than narrative summarization;
3. preserve requirement-to-source traceability;
4. separate explicit statements from inference and assumptions;
5. flag ambiguity, conflicts, missing details, and superseded sources;
6. perform a second pressure-test pass;
7. define acceptance criteria and ownership;
8. retain human authority for clarification and approval;
9. use a Project for recurring, context-rich work when appropriate; and
10. convert the approved baseline into workflow stages and tests.

```text
Broad business need        → define actor, output, data, frequency, and success
Long source package        → structured requirement register
Precise row without source → add traceability
Hidden implication         → classify and confirm
Two plausible meanings     → clarification question
Old and amended clauses    → resolve source authority
No completion test         → add acceptance criterion
Feature-first proposal     → restate operational outcome and control model
```

---

# Knowledge check

## Question 1

Why is `we need better reporting` not yet a requirement?

**Answer:** It does not define the audience, decision, data, frequency, format, owner, constraints, or acceptance criteria needed to build and verify the work.

## Question 2

Why should requirement extraction return a table rather than only a narrative summary?

**Answer:** A table makes each obligation distinct, traceable, assignable, testable, and reviewable.

## Question 3

What is the difference between an explicit and implied requirement?

**Answer:** An explicit requirement is directly stated. An implied requirement is inferred from another clause, criterion, or dependency and must be labeled and confirmed.

## Question 4

Why use a separate pressure-test pass?

**Answer:** The second pass challenges completeness and interpretation, surfacing hidden clauses, conflicts, duplicates, ambiguous language, and untestable requirements.

## Question 5

What should happen when the source does not specify a material detail?

**Answer:** Record it as missing or ambiguous, assign a clarification owner, and avoid inventing a value.

## Question 6

When does a Claude capability become a viable use case?

**Answer:** When it is connected to a measurable business outcome, repeatable task, authorized inputs, controlled responsibility, acceptance criteria, and clear human ownership.

## Question 7

Why may a recurring RFP workflow belong in a Project?

**Answer:** It benefits from stable project knowledge, project instructions, recurring source material, and repeated work within a focused workspace.

## Question 8

Who approves the final interpretation of a material requirement?

**Answer:** An authorized human owner, not the model.

---

# Flashcards

## Flashcard 1

**Q:** What does requirements analysis convert?

**A:** Messy business inputs into structured, traceable, testable, owned requirements.

## Flashcard 2

**Q:** What are the core requirement classes?

**A:** Explicit, implied, ambiguous, missing, conflicting, assumption, constraint, and acceptance criterion.

## Flashcard 3

**Q:** What is traceability?

**A:** The ability to connect a requirement to its controlling source and exact location.

## Flashcard 4

**Q:** What is pressure-testing?

**A:** A second review that challenges interpretation, completeness, conflicts, hidden conditions, and testability.

## Flashcard 5

**Q:** What should Claude do when the evidence is silent?

**A:** Mark the field not found, missing, or ambiguous rather than inventing it.

## Flashcard 6

**Q:** What turns a business need into a task definition?

**A:** Actor, purpose, trigger, inputs, work, output, audience, timing, constraints, ownership, and acceptance criteria.

## Flashcard 7

**Q:** What turns a capability into a use case?

**A:** A business outcome, user, repeatable task, authorized inputs, measurable output, acceptable risk, and human ownership.

## Flashcard 8

**Q:** Who owns clarification and approval?

**A:** The authorized human team.

---

# Short recap

```text
1. Start with the business need and intended decision.
2. Curate and label the source package.
3. Extract atomic requirements into a structured register.
4. Preserve exact source traceability.
5. Separate explicit facts from implications and assumptions.
6. Flag ambiguity, missing details, conflicts, and superseded sources.
7. Pressure-test the first extraction.
8. Add ownership and acceptance criteria.
9. Obtain human clarification and approval.
10. Convert the approved baseline into workflow stages and tests.
```

> Claude can structure the evidence and expose the questions. The team still decides what the requirement means and whether it is approved.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute procurement, legal, proposal, architecture, or other professional advice.

## Source and currency note

The preparation-course material for this lesson was supplied on August 3, 2026. Product-specific descriptions were checked against official Claude Help Center guidance on August 3, 2026. Product availability and behavior can change.

Official references:

- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)

## Related material

- [Module 4 Introduction](01-module-introduction.md)
- [Module 4 overview](../README.md)
- [Requirements Analysis prompts](../../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)
- [Requirements Traceability and Pressure-Test Pattern](../../../patterns/requirements-traceability-pressure-test-pattern.md)
