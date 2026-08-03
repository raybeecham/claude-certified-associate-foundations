# Module 4: Workflow Integration & Solution Design

Associate Persona · Official Exam Domain 4 · **16% of the exam blueprint**

> **Status:** In progress — Module 4 is the active module.

## Module thesis

> Workflow value comes from deciding what to delegate, validating what is produced, and describing the resulting capability without overstatement.

```text
Business need
      ↓
Traceable requirements and viable use case
      ↓
Verified research and executed analysis
      ↓
Process planning and optimization
      ↓
Evidence-driven solution iteration
      ↓
Delegation mapping and control boundaries
      ↓
Accurate value and limitation communication
      ↓
Workflow redesign exercise
      ↓
Validated workflow
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Analyzing Requirements & Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [x] [03. Research, Planning & Process Optimization](lessons/03-research-planning-process-optimization.md)
- [x] [04. Solution Design, Development & Iteration](lessons/04-solution-design-development-iteration.md)
- [x] [05. Delegation Mapping](lessons/05-delegation-mapping.md)
- [x] [06. Communicating Value & Limitations](lessons/06-communicating-value-limitations.md)
- [x] [07. Exercise: Redesign a Workflow — all six correct](lessons/07-redesign-a-workflow.md)
- [ ] 08. Module 4 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 09. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Integrated workflow model

## 1. Workflow integration

```text
I use Claude
      ≠
Our workflow uses Claude
```

A designed workflow defines stages, authorized inputs, responsibilities, state, validation, review, failure behavior, approval, and measurable outcomes.

| Responsibility | Appropriate owner |
|---|---|
| Interpretation, synthesis, drafting, options | Model under bounded criteria |
| Exact calculation, schema, fixed rule | Deterministic component or code execution |
| Retrieval or external side effect | Controlled tool |
| Durable state and authoritative record | Storage or system of record |
| Professional judgment, approval, accountability | Human or organization |

```text
Generate recommendation
      ≠
Authorize action
```

## 2. Requirements and use cases

```text
Messy inputs
      ↓
Atomic candidate requirements
      ↓
Traceability and classification
      ↓
Pressure-test
      ↓
Human clarification and approval
      ↓
Requirement baseline
```

Requirement classes include explicit, implied, ambiguous, missing, conflicting, assumption, constraint, and acceptance criterion.

```text
Extracted fact
      ≠
Implied requirement
      ≠
Analyst assumption
```

A viable use case connects a measurable outcome, a real user and process, authorized inputs, a bounded AI contribution, retained human authority, deterministic controls, acceptance criteria, and escalation.

## 3. Research, planning, and optimization

```text
Research and synthesis
      +
Executed computation
      +
Human judgment and authority
      ↓
Defensible plan
```

| Need | Preferred path |
|---|---|
| Straightforward current fact | Web search |
| Deeper multi-source investigation | Research |
| Supplied-document question | Closed-source analysis |
| Internal operational truth | Approved internal system |
| Exact metric or transformation | Code execution |
| Missing organizational constraint | Human clarification |

```text
Plausible number in prose
      ≠
Computed result
```

Map the current process before optimizing it. Target the controlling bottleneck rather than adding Claude everywhere.

## 4. Solution iteration

```text
Stable design context
      ↓
Meaningfully different options
      ↓
Prototype hypothesis
      ↓
Smallest useful prototype
      ↓
Observed evidence and feedback
      ↓
Bounded refinement
      ↓
Acceptance and regression tests
      ↓
Continue / accept / redesign / escalate / stop
```

```text
Minimum useful prototype
      ≠
Production-ready solution
```

Classify feedback before acting. Prioritize correctness, security, accessibility, disclosure, and release-blocking defects over preference.

## 5. Delegation mapping

```text
Reversibility
+ Stakes
+ Accountability
↓
Minimum responsible delegation posture
```

| Mode | Typical responsibility |
|---|---|
| AI-appropriate | Bounded extraction, classification, synthesis, or drafting |
| AI with code execution | Exact calculations, transformations, and reconciliation |
| Collaborative | Claude prepares; qualified human evaluates and decides |
| Human-retained | Authority, professional judgment, exceptions, approval, binding action |
| Deterministic | Fixed rules, schemas, routing, authorization checks |
| Tool-owned | Controlled retrieval or external side effect |
| Storage-owned | Durable workflow state and authoritative records |

```text
Map the work first.
Assign features second.
```

Over-delegation signals include AI approving its own work, classification automatically triggering consequence, generated arithmetic, ceremonial review, or hidden irreversible actions.

## 6. Communicating value and limitations

```text
What Claude does
      +
What Claude does not do
      +
What value has been observed
      +
What limitations and controls remain
      ↓
Credible workflow description
```

Adapt depth and vocabulary for each audience. Preserve capability boundaries, verified metrics, uncertainty, limitations, human gates, and approval authority.

```text
Audience adaptation
      ≠
Risk concealment
```

---

# Workflow redesign exercise

## Completion record

```text
Strong map — all six steps correct
```

The fictional expense-report workflow was mapped as follows:

| Step | Delegation | Feature | Governing reason |
|---|---|---|---|
| Extract receipt line items and amounts | Automated | Skill | Mechanical, reversible, reviewable |
| Compare expenses with travel policy | Collaborative | Skill | Repeatable procedure with human review for ambiguity and exceptions |
| Total report and calculate policy variance | Automated | Code execution | Exact numeric work must be computed and reconciled |
| Draft exception summary | Collaborative | Neither required by default | AI drafts from verified findings; approver confirms context |
| Approve or reject report | Human-retained | None | Financial accountability and authority do not delegate |
| Submit approved report for payment | Human-retained before controlled execution | Controlled system | Financially material external action |

## Feature selections

```text
Best Skill step:
Step 2 — policy comparison

Best code-execution step:
Step 3 — totals and policy-limit calculations
```

Step 1 can also use a document-processing Skill. Step 2 most clearly demonstrates a maintained policy procedure.

## Why the map is defensible

```text
Procedure → Skill
Calculation → Code execution
Drafting → AI or collaborative
Approval → Human-retained
External financial action → Approval before controlled execution
```

The exercise preserves four critical separations:

1. procedure versus calculation;
2. assistance versus authority;
3. approval versus external execution; and
4. reversible preparation versus financial consequence.

## Audit evidence

A defensible workflow retains:

- source receipts;
- extracted line-item records;
- policy version and cited rules;
- policy flags and exception classifications;
- calculation code and outputs;
- human review rationale;
- approval record; and
- payment-submission identifier.

```text
Mapped delegation
      +
Operational controls
      +
Retained evidence
      =
Audit-ready workflow design
```

---

# Integrated workflow protocol

```text
1. Define the business outcome and accountable owner
2. Establish the requirement baseline
3. Select and validate research and data inputs
4. Execute and reconcile material calculations
5. Map the current workflow and controlling bottleneck
6. Generate options and prototype highest-risk assumptions
7. Gather evidence, refine through bounded changes, and regression-test
8. Decompose the workflow into atomic steps
9. Assess reversibility, stakes, accountability, and side effects
10. Assign model, code, deterministic, tool, storage, and human ownership
11. Place qualified review before consequential or irreversible action
12. Test handoffs, exceptions, failures, retries, and recovery
13. Retain source, calculation, review, approval, and external-action evidence
14. Measure workflow value and scope the claim
15. Communicate capability, exclusions, controls, and limitations accurately
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Analyzing Requirements and Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [Research, Planning, and Process Optimization](lessons/03-research-planning-process-optimization.md)
- [Solution Design, Development, and Iteration](lessons/04-solution-design-development-iteration.md)
- [Delegation Mapping](lessons/05-delegation-mapping.md)
- [Communicating Value and Limitations](lessons/06-communicating-value-limitations.md)
- [Exercise: Redesign a Workflow](lessons/07-redesign-a-workflow.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)
- [Requirements Analysis prompts](../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)
- [Research and Planning prompts](../../prompts/module-04/03-research-planning-process-optimization-prompts.md)
- [Solution Design and Iteration prompts](../../prompts/module-04/04-solution-design-development-iteration-prompts.md)
- [Delegation Mapping prompts](../../prompts/module-04/05-delegation-mapping-prompts.md)
- [Communicating Value and Limitations prompts](../../prompts/module-04/06-communicating-value-limitations-prompts.md)
- [Redesign a Workflow prompts](../../prompts/module-04/07-redesign-a-workflow-prompts.md)

## Engineering patterns

- [Requirements Traceability and Pressure-Test Pattern](../../patterns/requirements-traceability-pressure-test-pattern.md)
- [Verified Planning Workflow Pattern](../../patterns/verified-planning-workflow-pattern.md)
- [Evidence-Driven Prototype Iteration Pattern](../../patterns/evidence-driven-prototype-iteration-pattern.md)
- [Delegation Boundary Mapping Pattern](../../patterns/delegation-boundary-mapping-pattern.md)
- [Capability, Value, and Limitation Communication Pattern](../../patterns/capability-value-limitation-communication-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Mechanical extraction               → automate with validation
Repeatable policy procedure          → Skill
Ambiguous policy interpretation      → collaborative review
Exact totals and limits              → code execution
Draft explanatory note               → collaborative
Financial approval                   → human-retained
Payment submission                   → approval before controlled action
Previous stage succeeded             → still assess next stage independently
```

For redesign scenarios:

1. map atomic stages;
2. assess reversibility, stakes, accountability, and side effects;
3. assign Skills to repeatable procedures;
4. assign code execution to material calculations;
5. keep ambiguous judgment collaborative;
6. keep approval human-retained;
7. expose irreversible actions;
8. place approval before external consequence;
9. define exception and failure routes; and
10. retain reconstructable evidence.

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [x] I completed Analyzing Requirements and Use Cases.
- [x] I completed Research, Planning, and Process Optimization.
- [x] I completed Solution Design, Development, and Iteration.
- [x] I completed Delegation Mapping.
- [x] I completed Communicating Value and Limitations.
- [x] I completed the Redesign a Workflow exercise with all six steps correct.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can build and pressure-test a traceable requirement register.
- [ ] I can separate research, computation, synthesis, and human judgment.
- [ ] I can define a bounded prototype and controlled iteration loop.
- [ ] I can classify workflow stages by reversibility, stakes, and accountability.
- [ ] I can assign Skills and code execution to appropriate stages.
- [ ] I can detect over-delegation and ceremonial review.
- [ ] I can place approval before irreversible action.
- [ ] I can support value claims with scoped evidence.
- [ ] I can adapt messages without hiding limitations or controls.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential receipts, financial records, expense data, internal policies, contracts, client identities, pilot metrics, approval records, proprietary workflows, credentials, system identifiers, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute accounting, tax, legal, financial-control, risk, compliance, employment, architecture, security, or operational advice.
