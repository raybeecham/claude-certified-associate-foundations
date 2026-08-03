# Module 4: Workflow Integration & Solution Design

Associate Persona · Official Exam Domain 4 · **16% of the exam blueprint**

> **Status:** In progress — Module 4 is the active module.

## Module thesis

> Workflow value comes from deciding what to delegate—not from automating everything.

```text
Business need
      ↓
Traceable requirements and viable use case
      ↓
Current-process research and planning
      ↓
Solution design and iteration
      ↓
Delegation mapping
      ↓
Value and limitation communication
      ↓
Validated workflow
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Analyzing Requirements & Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [ ] 03. Research, Planning & Process Optimization
- [ ] 04. Solution Design, Development & Iteration
- [ ] 05. Delegation Mapping
- [ ] 06. Communicating Value & Limitations
- [ ] 07. Exercise: Redesign a Workflow
- [ ] 08. Module 4 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 09. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Module 3 to Module 4 bridge

Module 3 asked whether an output was trustworthy and releasable. Module 4 expands the boundary to the complete process.

```text
Business objective
      ↓
Requirements and acceptance criteria
      ↓
Workflow stages and responsibilities
      ↓
Inputs, state, decisions, approvals, and side effects
      ↓
Stage-level validation and recovery
      ↓
Operational outcome
```

---

# Foundation 1: Personal use versus workflow integration

```text
I use Claude
      ↓
One person supplies context, reviews, and adapts

Our workflow uses Claude
      ↓
A team follows repeatable stages with defined
inputs, controls, ownership, state, and outcomes
```

```text
Repeated prompting
      ≠
Designed workflow
```

## Delegation modes

| Mode | Appropriate responsibility |
|---|---|
| AI-appropriate | Interpretation, classification, synthesis, drafting, and options under bounded criteria |
| Human-retained | Authority, accountability, professional judgment, exceptions, and approval |
| Collaborative | Claude prepares or analyzes while a human evaluates and decides |
| Deterministic | Exact calculations, schemas, fixed rules, routing, and authorization checks |
| Tool-owned | Controlled retrieval, transformation, external actions, and system interaction |
| Storage-owned | Authoritative records, durable state, checkpoints, logs, and version history |

```text
Probabilistic language work → model
Exact rule or calculation   → deterministic component
External action             → controlled tool
Durable state               → system of record
Authority and accountability → human or organization
```

```text
Generate recommendation
      ≠
Authorize action
```

---

# Foundation 2: Requirements and use-case analysis

Real workflows commonly begin with long documents, email threads, notes, forms, or verbal requests. These must be converted into requirements that can be assigned, built, and tested.

```text
Messy inputs
      ↓
Candidate requirements
      ↓
Traceability and classification
      ↓
Pressure-test
      ↓
Human clarification and approval
      ↓
Requirement baseline
```

## Business need versus task definition

```text
We need better reporting
```

is not yet actionable. A task definition should identify:

- actor and purpose;
- trigger and authorized inputs;
- work and output;
- audience and timing;
- constraints;
- owner and approver;
- acceptance criteria; and
- failure or escalation behavior.

## Requirement classes

| Class | Meaning |
|---|---|
| Explicit | Directly stated in the source |
| Implied | Inferred from criteria, dependencies, or cross-references |
| Ambiguous | Supports multiple material interpretations |
| Missing | Needed for a buildable or testable task but absent |
| Conflicting | Relevant sources disagree |
| Assumption | Temporary premise pending confirmation |
| Constraint | Limits the solution or method |
| Acceptance criterion | Defines observable completion |

```text
Extracted fact
      ≠
Implied requirement
      ≠
Analyst assumption
```

## Requirements register

| ID | Requirement | Class | Source/location | Coverage | Gap | Owner | Acceptance criterion |
|---|---|---|---|---|---|---|---|
| R-001 | Atomic obligation | Explicit | Document §x.x | Complete/Partial/Open | Clarification | Role | Observable test |

Every material row should be traceable to an exact source location.

## Pressure-test pass

After extraction, separately check for:

- omitted clauses and hidden conditions;
- requirements split or merged incorrectly;
- duplicate obligations;
- superseded language and amendments;
- implications mislabeled as explicit;
- examples mistaken for mandates;
- assumptions presented as facts;
- incomplete internal answers;
- missing actors, dates, formats, data, owners, or tests; and
- requirements that cannot be verified.

```text
Requirement extracted
      ↓
Check source support
      ↓
Check completeness and interpretation
      ↓
Clarify or approve
```

## Use-case viability

A Claude capability becomes a viable use case only when it connects:

```text
Measurable business outcome
+ user and current process
+ repeatable task
+ authorized inputs
+ bounded AI contribution
+ retained human authority
+ deterministic controls
+ acceptance criteria
+ risk and escalation
```

Weak:

```text
Claude can summarize documents, so automate document review.
```

Stronger:

```text
The team spends eight hours building a requirement inventory.
Claude may extract and organize candidate requirements from approved sources,
while an authorized reviewer owns interpretation and final coverage.
```

## Project and Skill fit

For recurring, context-rich work:

```text
Project knowledge    → project-specific sources and background
Project instructions → project-specific behavior and output requirements
Skill                → reusable procedure that can activate across Claude
Human review         → clarification, prioritization, and approval
```

Current official Claude guidance describes Projects as self-contained workspaces with project knowledge and instructions, while Skills provide reusable procedures that load when relevant and can work across Claude. Product behavior can change. citeturn472072search0turn472072search1turn472072search3

---

# Requirements-analysis protocol

```text
1. Define the business outcome and intended decision
2. Inventory sources and establish authority
3. Extract atomic requirements with exact traceability
4. Classify explicit, implied, ambiguous, missing, conflicting, and assumed items
5. Link current answers and evidence
6. Pressure-test coverage, interpretation, authority, and testability
7. Resolve or assign clarification questions
8. Add owners and acceptance criteria
9. Approve the requirement baseline
10. Map approved requirements to workflow stages and tests
```

---

# Durable engineering foundation

Later lessons will extend this baseline into:

- current-process research;
- process optimization;
- interactive, fixed, application, or bounded-agent pattern selection;
- responsibility partitioning;
- tool contracts;
- state management;
- retries, timeouts, idempotency, fallback, rollback, and compensation;
- stage-level observability;
- solution iteration; and
- stakeholder communication.

A production workflow may need input validation, deterministic calculations, provenance checks, human approval, durable state, audit logs, monitoring, and incident ownership.

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Analyzing Requirements and Use Cases](lessons/02-analyzing-requirements-use-cases.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)
- [Requirements Analysis prompts](../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)

## Engineering pattern

- [Requirements Traceability and Pressure-Test Pattern](../../patterns/requirements-traceability-pressure-test-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

For requirements and use-case scenarios:

```text
Broad need                  → define actor, output, data, timing, and success
Long source package         → structured requirement register
Requirement lacks source    → add exact traceability
Hidden implication          → classify and confirm
Multiple interpretations    → clarification question
Base and amendment conflict → resolve source authority
No completion test          → add acceptance criterion
Feature-first proposal      → restate business outcome and controls
```

Choose structured extraction over a narrative summary, preserve uncertainty, run a second pressure-test pass, and retain human authority for interpretation and approval.

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [x] I completed Analyzing Requirements and Use Cases.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can explain Delegation and its responsibility modes.
- [ ] I can translate a business need into a testable task definition.
- [ ] I can build a traceable requirement register.
- [ ] I can distinguish explicit, implied, ambiguous, missing, conflicting, and assumed requirements.
- [ ] I can pressure-test a requirement set.
- [ ] I can distinguish a product capability from a viable use case.
- [ ] I can research and map a current-state workflow.
- [ ] I can identify unsuitable automation targets.
- [ ] I can create a component responsibility matrix.
- [ ] I can design tool, state, validation, and approval boundaries.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential solicitations, proposal materials, workflows, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute procurement, proposal, architecture, legal, compliance, or other professional advice.
