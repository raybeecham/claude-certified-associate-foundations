# Module 4: Workflow Integration & Solution Design

Associate Persona · Official Exam Domain 4 · **16% of the exam blueprint**

> **Status:** In progress — Module 4 is the active module.

## Why this domain matters

A useful AI response is not yet a reliable workflow.

There is a difference between:

```text
I use Claude
      ↓
Personal productivity habit

Our workflow uses Claude
      ↓
Repeatable team process with defined stages,
responsibilities, controls, and outcomes
```

Workflow integration determines how a business objective becomes a repeatable process with clear inputs, responsibilities, decision points, tools, state, validation, human review, and recovery behavior.

```text
Business requirement
        ↓
Use-case analysis
        ↓
Research and process planning
        ↓
Solution design
        ↓
Delegation mapping
        ↓
Development and iteration
        ↓
Value and limitation communication
        ↓
Validated workflow
```

> **Module thesis:** Workflow value comes from deciding what to delegate—not from automating everything.

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [ ] 02. Analyzing Requirements & Use Cases
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

## Learning progression

```text
Understand the module and workflow objective
              ↓
Analyze requirements, stakeholders, and use cases
              ↓
Research the current process and identify constraints
              ↓
Plan and optimize the workflow
              ↓
Design, develop, test, and iterate the solution
              ↓
Map responsibilities through Delegation criteria
              ↓
Communicate value, limitations, risks, and tradeoffs
              ↓
Redesign a representative workflow
              ↓
Demonstrate integrated judgment under quiz conditions
```

---

# Module 3 to Module 4 bridge

Module 3 established whether an output is trustworthy and releasable.

```text
Requirements
      ↓
Candidate output
      ↓
Evaluation and validation
      ↓
Release, revise, verify, escalate, or reject
```

Module 4 expands the unit of analysis from one output to the full workflow.

```text
Business objective
      ↓
Workflow stages
      ↓
Model, human, tool, storage, and deterministic responsibilities
      ↓
Inputs, state, decisions, approvals, and side effects
      ↓
Stage-level validation and recovery
      ↓
Operational outcome
```

The transition question is:

> How should the workflow be designed so that reliable output is produced consistently rather than recovered through manual effort each time?

---

# Introduction foundation

## Personal use versus workflow integration

A personal interaction usually depends on one person's live judgment. A team workflow must make that judgment explicit and repeatable.

| Dimension | Personal use | Designed workflow |
|---|---|---|
| Trigger | Individual decides | Defined event, request, or stage |
| Inputs | Selected informally | Authorized input contract |
| Prompt | Adapted conversationally | Versioned task specification |
| State | Often held in conversation | Persisted in a durable system |
| Validation | User judgment | Defined checks and acceptance criteria |
| Approval | Often the same user | Assigned reviewer and approver |
| Failure handling | Manual retry | Timeout, retry, fallback, escalation, rollback |
| Accountability | Individual | Named role or organization |
| Measurement | Subjective usefulness | Stage and business outcomes |

```text
Repeated prompting
      ≠
Designed workflow
```

## Delegation as the anchor

Delegation assigns each workflow responsibility to the component best suited for it.

| Mode | Appropriate responsibility |
|---|---|
| **AI-appropriate** | Interpretation, classification, synthesis, drafting, or options under bounded criteria |
| **Human-retained** | Authority, accountability, professional judgment, exceptions, consequential approval |
| **Collaborative** | Claude prepares or analyzes while a human evaluates and decides |
| **Deterministic** | Exact calculations, schemas, fixed rules, routing, authorization checks |
| **Tool-owned** | Controlled retrieval, transformation, external actions, system interaction |
| **Storage-owned** | Authoritative records, durable state, checkpoints, logs, version history |

```text
Probabilistic language work → model
Exact rule or calculation   → deterministic component
External action             → controlled tool
Durable state               → storage or system of record
Authority and accountability → human or organization
```

## Task delegation versus decision delegation

A workflow may safely delegate preparation without delegating authority.

```text
Claude extracts, summarizes, classifies, or drafts
                    ↓
Human evaluates evidence and consequences
                    ↓
Authorized person approves or rejects
                    ↓
Controlled tool executes any side effect
```

```text
Generate recommendation
      ≠
Authorize action
```

The farther a stage moves from reversible preparation toward consequential action, the stronger its deterministic controls, validation, review, and approval requirements become.

## Two-team lesson

Two teams can use the same product on the same process and receive opposite outcomes.

The safer design:

- delegates clause extraction and draft redlining;
- retains lawyer review and final decision authority;
- preserves evidence and proposed changes; and
- validates the work before release.

The unsafe design:

- treats classification as sufficient for approval;
- lets the model accept supposedly low-risk clauses;
- removes qualified review from consequential decisions; and
- discovers the error only after an obligation is created.

The controlling distinction is:

```text
Useful AI task
      ≠
Safe AI-owned decision
```

---

# Delegation-first workflow review

```text
1. Define the business outcome
          ↓
2. Map the current stages and owners
          ↓
3. Identify decisions, calculations, actions, and state
          ↓
4. Mark each stage AI-appropriate, human-retained,
   collaborative, deterministic, tool-owned, or storage-owned
          ↓
5. Add validation and approval boundaries
          ↓
6. Define failure, fallback, and escalation behavior
          ↓
7. Measure workflow and business outcomes
```

## Stage inventory

| Stage | Current owner | Input | Work | Output | Consequence if wrong | Candidate delegation |
|---|---|---|---|---|---|---|
| Stage name | Role/system | Source | Activity | Result | Low/material/high | AI/Human/Collaborative/Deterministic/Tool/Storage |

The inventory makes work visible. It does not automatically decide the final architecture.

---

# Durable engineering foundation

The existing repository material provides an engineering foundation that will be mapped to later course sections as they arrive.

## Requirements and use-case analysis

Before selecting a workflow pattern, define:

- business objective;
- users and affected stakeholders;
- current process;
- inputs and authoritative systems;
- expected decisions and actions;
- output and success criteria;
- frequency, volume, and latency;
- data sensitivity;
- consequence of error;
- reversibility;
- governing policy or contract; and
- escalation conditions.

A technology capability is not a use case until it is connected to a real outcome, user, process, and acceptance criterion.

## Workflow-pattern selection

| Pattern | Appropriate when |
|---|---|
| Interactive chat | A human remains continuously engaged and the task is contextual or exploratory |
| Fixed workflow | Steps, inputs, decisions, and outputs are predictable |
| API-backed application | The capability must be embedded in a repeatable product or business process |
| Bounded agent | The task needs limited planning and tool selection within explicit permissions and stopping rules |

Prefer the simplest pattern that satisfies the requirements.

## Tool contracts

A tool contract should define:

- purpose;
- inputs and types;
- required and optional fields;
- allowed values;
- permissions;
- expected output;
- errors and timeouts;
- retry policy;
- idempotency;
- side effects;
- approval boundary; and
- audit evidence.

## Reliability controls

A production workflow may need:

- input and schema validation;
- deterministic calculations;
- provenance checks;
- human approval gates;
- idempotency keys;
- bounded retries;
- fallback paths;
- rollback or compensation;
- checkpointed state;
- stage-level logging;
- monitoring and alerts; and
- incident ownership.

## State and observability

Long-running workflow state should not live only inside a prompt.

Persist task identifiers, stages, completed actions, approved inputs, versions, tool results, pending approvals, retry counts, exceptions, and final dispositions in an appropriate system.

Measure stage-level outcomes such as input rejection, retrieval coverage, tool success, validation pass rate, review rate, escalation reasons, retries, fallbacks, correction rate, and business outcome.

---

# Learning objectives

By the end of this module, you should be able to:

- distinguish personal AI use from repeatable workflow integration;
- explain Delegation as the module's anchoring competency;
- separate task assistance from decision authority;
- classify stages as AI-appropriate, human-retained, collaborative, deterministic, tool-owned, or storage-owned;
- translate a business objective into workflow requirements and acceptance criteria;
- analyze stakeholders, inputs, decisions, constraints, risks, and governing obligations;
- research and document the current process before proposing automation;
- identify bottlenecks and unsuitable automation targets;
- choose an appropriate workflow pattern;
- partition model, deterministic, tool, storage, and human responsibilities;
- design tool contracts and approval boundaries;
- handle retries, idempotency, timeouts, fallback, and rollback;
- persist long-running state outside the prompt;
- instrument stage-level outcomes;
- iterate using observed failures and acceptance criteria;
- communicate value without overstating capability; and
- redesign a workflow using the minimum necessary complexity.

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)

## Existing extended practice

- [notes.md](notes.md): Workflow-integration concepts and exam-focused decisions
- [lab.md](lab.md): Applied workflow-design exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

---

# Exam lens

Workflow scenarios often tempt the learner to place too much responsibility on the model.

For introductory scenarios:

1. identify the business objective;
2. distinguish personal productivity from a repeatable team process;
3. map the stages;
4. separate task assistance from decision authority;
5. identify AI, human, collaborative, deterministic, tool, and storage responsibilities;
6. retain human accountability for consequential decisions;
7. place validation before side effects;
8. design failure and escalation paths;
9. measure business outcomes rather than prompt volume; and
10. prefer the simplest qualified workflow.

```text
One person uses a strong prompt      → productivity habit
Team repeats controlled stages       → workflow integration
Claude drafts, human decides          → collaborative delegation
Claude approves consequential action → over-delegation
Exact fixed rule assigned to model    → deterministic logic
No failure path                       → add fallback and escalation
```

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can explain Delegation and its responsibility modes.
- [ ] I can separate task delegation from decision authority.
- [ ] I can analyze requirements and viable use cases.
- [ ] I can research and map a current-state workflow.
- [ ] I can identify unsuitable automation targets.
- [ ] I can create a component responsibility matrix.
- [ ] I can design a clear tool contract.
- [ ] I can identify where idempotency is required.
- [ ] I can place validation and human-approval gates.
- [ ] I can describe state, observability, fallback, and rollback.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client names, confidential workflows, proprietary operating procedures, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, legal, compliance, operational, or other professional advice.

## Source note

The introduction was supplied on August 2, 2026. Product capabilities, terms, policies, and documentation can change. Current official Anthropic terms, policies, and documentation control if they conflict with course or repository material.
