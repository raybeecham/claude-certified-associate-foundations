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
Delegation mapping and control boundaries
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
- [x] [05. Delegation Mapping](lessons/05-delegation-mapping.md)
- [ ] 06. Communicating Value & Limitations
- [ ] 07. Exercise: Redesign a Workflow
- [ ] 08. Module 4 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 09. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Workflow integration

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

# Foundation 3: Research, planning, and optimization

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

Material calculations should be executed over actual data, reviewed, and reconciled. Claude can synthesize scenarios and trade-offs; accountable humans retain budget, risk, feasibility, and approval decisions.

Map the current process before optimizing it. Identify whether the controlling bottleneck is retrieval, synthesis, calculation, handoff, review, state, or authority.

---

# Foundation 4: Solution iteration

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

Preserve approved requirements, data definitions, constraints, prior decisions, acceptance criteria, known risks, unresolved questions, and version history.

```text
Minimum useful prototype
      ≠
Production-ready solution
```

Feedback should be classified as requirement, correctness, usability, accessibility, performance, disclosure, preference, new requirement, or out of scope. Release-blocking defects take priority over preferences.

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

Stop or escalate when progress becomes cosmetic or the remaining issue requires unavailable evidence, authority, architecture, security, accessibility, data governance, or production engineering.

---

# Foundation 5: Delegation mapping

Delegation Mapping assigns every atomic workflow step to the component best suited for it.

## Three criteria

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
| Human-retained | Authority, professional judgment, exception handling, approval, binding action |
| Deterministic | Fixed rules, schemas, routing, authorization checks |
| Tool-owned | Controlled retrieval or external side effect |
| Storage-owned | Durable workflow state and authoritative records |

## Work-first sequence

```text
Business outcome
      ↓
Atomic workflow steps
      ↓
Work type, consequence, and side effects
      ↓
Delegation classification
      ↓
Validation, review, and exception handling
      ↓
Skill, Project, code, tool, storage, and human-gate assignment
```

```text
Map the work first.
Assign features second.
```

## Contract-review map

| Step | Delegation | Control |
|---|---|---|
| Extract clauses | AI-appropriate | Completeness check |
| Flag playbook departures | AI-appropriate | Skill or approved procedure; clause and rule trace |
| Draft redline and rationale | Collaborative | Lawyer reviews every edit |
| Approve or reject change | Human-retained | Authorized legal approval |
| Compute penalty exposure | AI with code execution | Formula, units, assumptions, reconciliation |
| Sign and send | Human-retained | Authorized signatory and controlled action |

## Onboarding-document map

| Step | Delegation | Control |
|---|---|---|
| Pull approved new-hire fields | AI with code execution | Schema and record validation |
| Draft approved template | AI-appropriate | Skill carries template and required clauses |
| Personalize welcome note | Collaborative | Hiring manager edits and approves |
| Confirm compensation | Human-retained | Authorized source-record verification |
| Send signed offer | Human-retained | Approved version, recipient, and sender confirmation |

The domains differ, but the decision pattern remains:

```text
Mechanical and reversible preparation → delegate with validation
Drafting and interpretation            → AI or collaborative
Exact material calculation             → code execution
High-stakes approval                    → human-retained
Irreversible external action            → human approval before execution
```

## Over-delegation signals

- Claude approves the work it drafted;
- a classification automatically triggers a consequential action;
- an irreversible step lacks an approval gate;
- exact rules are assigned to probabilistic judgment;
- calculations are generated as prose;
- human review is mentioned but not staffed; or
- success on one step is used to justify the next step.

```text
High-quality draft
      ≠
Authority to approve
      ≠
Permission to execute
```

## Common mapping errors

```text
Halo delegation
→ evaluate every stage independently

Collaborative in name only
→ define reviewer, evidence, criteria, time, and intervention rights

Feature-first mapping
→ map work before Skills or integrations

Hidden side effect
→ show send, sign, file, pay, publish, or update as a separate stage

Mechanical-but-material
→ assess downstream propagation and validate deterministically
```

---

# Integrated workflow protocol

```text
1. Define the business outcome and accountable owner
2. Establish the requirement baseline
3. Select and validate research and data inputs
4. Execute and reconcile material calculations
5. Map the current workflow and bottleneck
6. Generate solution options and prototype the highest-risk assumptions
7. Gather evidence, refine through bounded changes, and regression-test
8. Decompose the workflow into atomic steps
9. Assess reversibility, stakes, accountability, and side effects
10. Assign model, code, deterministic, tool, storage, and human responsibilities
11. Place qualified review before consequential or irreversible action
12. Test handoffs, exceptions, failures, and recovery
13. Record owners, approvals, limitations, and evidence
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Analyzing Requirements and Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [Research, Planning, and Process Optimization](lessons/03-research-planning-process-optimization.md)
- [Solution Design, Development, and Iteration](lessons/04-solution-design-development-iteration.md)
- [Delegation Mapping](lessons/05-delegation-mapping.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)
- [Requirements Analysis prompts](../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)
- [Research and Planning prompts](../../prompts/module-04/03-research-planning-process-optimization-prompts.md)
- [Solution Design and Iteration prompts](../../prompts/module-04/04-solution-design-development-iteration-prompts.md)
- [Delegation Mapping prompts](../../prompts/module-04/05-delegation-mapping-prompts.md)

## Engineering patterns

- [Requirements Traceability and Pressure-Test Pattern](../../patterns/requirements-traceability-pressure-test-pattern.md)
- [Verified Planning Workflow Pattern](../../patterns/verified-planning-workflow-pattern.md)
- [Evidence-Driven Prototype Iteration Pattern](../../patterns/evidence-driven-prototype-iteration-pattern.md)
- [Delegation Boundary Mapping Pattern](../../patterns/delegation-boundary-mapping-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Reversible extraction or drafting  → AI-appropriate or collaborative
Exact numeric calculation          → code execution + review
Fixed policy or authorization rule → deterministic logic
Professional approval              → human-retained
Sign, send, file, pay, or publish   → approval before controlled execution
Skill already exists               → does not determine delegation
Previous AI stage succeeded        → evaluate next stage independently
```

For Delegation scenarios:

1. map the actual work;
2. identify atomic stages and side effects;
3. assess reversibility, stakes, and accountability;
4. separate preparation from authority;
5. route exact rules and calculations to deterministic execution;
6. make collaborative review real and staffed;
7. expose irreversible actions;
8. retain human accountability for consequential decisions;
9. check for halo delegation and over-delegation; and
10. choose the least autonomous design that achieves the outcome.

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [x] I completed Analyzing Requirements and Use Cases.
- [x] I completed Research, Planning, and Process Optimization.
- [x] I completed Solution Design, Development, and Iteration.
- [x] I completed Delegation Mapping.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can build and pressure-test a traceable requirement register.
- [ ] I can separate research, computation, synthesis, and human judgment.
- [ ] I can define a bounded prototype and controlled iteration loop.
- [ ] I can classify every workflow step by reversibility, stakes, and accountability.
- [ ] I can distinguish AI, code-executed, collaborative, human, deterministic, tool, and storage responsibilities.
- [ ] I can detect halo delegation and ceremonial review.
- [ ] I can place human approval before irreversible action.
- [ ] I can assign Skills and tools only after the work is mapped.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential contracts, employment records, compensation data, requirements, prototypes, internal systems, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, employment, compensation, architecture, security, compliance, or operational advice.

## Official reading

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
