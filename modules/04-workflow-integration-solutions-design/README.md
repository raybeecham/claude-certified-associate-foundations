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
Verified research and executed analysis
      ↓
Process planning and optimization
      ↓
Evidence-driven solution iteration
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
- [x] [03. Research, Planning & Process Optimization](lessons/03-research-planning-process-optimization.md)
- [x] [04. Solution Design, Development & Iteration](lessons/04-solution-design-development-iteration.md)
- [ ] 05. Delegation Mapping
- [ ] 06. Communicating Value & Limitations
- [ ] 07. Exercise: Redesign a Workflow
- [ ] 08. Module 4 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 09. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Workflow integration and Delegation

```text
I use Claude
      ↓
Personal productivity

Our workflow uses Claude
      ↓
Repeatable stages, inputs, controls, ownership, state, and outcomes
```

```text
Repeated prompting
      ≠
Designed workflow
```

| Responsibility | Appropriate owner |
|---|---|
| Interpretation, synthesis, drafting, options | Model under bounded criteria |
| Exact calculation, schema, fixed rule | Deterministic component |
| Retrieval or external side effect | Controlled tool |
| Durable state and authoritative record | Storage or system of record |
| Professional judgment, approval, accountability | Human or organization |

```text
Generate recommendation
      ≠
Authorize action
```

---

# Foundation 2: Requirements and use cases

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

A viable use case connects a measurable outcome, user, current process, repeatable task, authorized inputs, bounded AI contribution, retained human authority, deterministic controls, acceptance criteria, and escalation path.

---

# Foundation 3: Research, planning, and process optimization

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

Material planning calculations should be executed over actual data, reviewed, and reconciled. Claude can synthesize scenarios and trade-offs; accountable humans retain budget, risk, feasibility, and approval decisions.

Map the current process before optimizing it. Identify whether the controlling bottleneck is retrieval, synthesis, calculation, handoff, review, state, or authority.

---

# Foundation 4: Solution design, development, and iteration

Claude contributes most effectively through an explicit learning loop.

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

## Stable design context

Preserve:

- approved requirements;
- users and use cases;
- source and data definitions;
- constraints;
- prior decisions and rationale;
- acceptance criteria;
- known risks;
- unresolved questions; and
- version history.

Projects can support continuity through project knowledge, project instructions, and related conversations. Product behavior can change, so verify current official documentation.

## Prototype scope

A prototype should test the highest-risk assumptions and core user task with the minimum necessary features.

Record:

- included and excluded scope;
- test data;
- prohibited uses;
- acceptance criteria;
- failure criteria; and
- required reviewers.

```text
Minimum useful prototype
      ≠
Production-ready solution
```

## Feedback classification

| Class | Example |
|---|---|
| Requirement | Missing region filter |
| Correctness | Total does not reconcile |
| Usability | User cannot locate a control |
| Accessibility | Meaning depends on color alone |
| Performance | Large input is too slow |
| Privacy or disclosure | Sensitive field is exposed |
| Preference | Different chart requested |
| New requirement | Printed output needs approval block |

Prioritize release-blocking defects over preferences.

## Controlled refinement

```text
Observed problem
      ↓
Likely cause
      ↓
Bounded change
      ↓
Expected improvement
      ↓
Preserved requirements
      ↓
Regression and acceptance tests
```

## Dashboard example

```text
Cycle 1: Show five verified metrics
Cycle 2: Add region filter and computed totals
Cycle 3: Add direction-aware deltas and print layout
```

The prototype can be created and refined through natural-language requests, but the team must still verify data mappings, totals, accessibility, disclosure, and sharing behavior.

A working artifact does not establish security, scale, persistence, operational support, or deployment approval.

## Iteration stopping rules

Continue when the next bounded change can produce meaningful evidence.

Stop or escalate when:

- the learning objective is met;
- changes become cosmetic;
- requirements conflict;
- evidence or authority is missing;
- architecture, security, accessibility, or data concerns exceed prototype scope; or
- production engineering is required.

```text
More iterations
      ≠
More progress
```

---

# Integrated workflow protocol

```text
1. Define the business outcome and accountable owner
2. Establish the requirement baseline
3. Select and validate research and data inputs
4. Execute and reconcile material calculations
5. Map the current workflow and bottleneck
6. Generate meaningfully different solution options
7. Define the prototype hypothesis and scope
8. Build the smallest useful prototype
9. Gather and classify evidence and feedback
10. Make bounded changes and run regression tests
11. Record decisions, limitations, and version history
12. Accept, continue, redesign, escalate, or stop
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Analyzing Requirements and Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [Research, Planning, and Process Optimization](lessons/03-research-planning-process-optimization.md)
- [Solution Design, Development, and Iteration](lessons/04-solution-design-development-iteration.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)
- [Requirements Analysis prompts](../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)
- [Research and Planning prompts](../../prompts/module-04/03-research-planning-process-optimization-prompts.md)
- [Solution Design and Iteration prompts](../../prompts/module-04/04-solution-design-development-iteration-prompts.md)

## Engineering patterns

- [Requirements Traceability and Pressure-Test Pattern](../../patterns/requirements-traceability-pressure-test-pattern.md)
- [Verified Planning Workflow Pattern](../../patterns/verified-planning-workflow-pattern.md)
- [Evidence-Driven Prototype Iteration Pattern](../../patterns/evidence-driven-prototype-iteration-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Need several approaches           → ideate bounded alternatives
Need to test one idea             → smallest useful prototype
Feedback received                 → classify and prioritize
Change requested                  → expected effect + regression tests
Iterations lose prior decisions   → stabilize context
Prototype demo succeeds           → production-readiness review still required
Cosmetic rounds with no gain      → stop or escalate
```

For solution-design scenarios:

1. preserve the requirement baseline;
2. generate options before committing;
3. define what the prototype must prove;
4. keep scope bounded;
5. gather observable feedback;
6. distinguish defects from preferences;
7. refine through controlled changes;
8. rerun affected and preserved tests;
9. retain human authority over requirements and acceptance; and
10. distinguish prototype success from deployment approval.

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [x] I completed Analyzing Requirements and Use Cases.
- [x] I completed Research, Planning, and Process Optimization.
- [x] I completed Solution Design, Development, and Iteration.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can build and pressure-test a traceable requirement register.
- [ ] I can separate research, computation, synthesis, and human judgment.
- [ ] I can define a reproducible planning analysis.
- [ ] I can create a stable design context.
- [ ] I can define a bounded prototype hypothesis and acceptance criteria.
- [ ] I can classify feedback and prioritize release-blocking issues.
- [ ] I can write controlled change requests with regression tests.
- [ ] I can distinguish prototype acceptance from production approval.
- [ ] I can apply Delegation criteria to workflow stages.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential requirements, datasets, prototypes, internal systems, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute product, software, architecture, security, accessibility, legal, compliance, or operational advice.

## Official reading

- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Publish and share artifacts](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)
