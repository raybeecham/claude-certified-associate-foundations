# Module 4: Workflow Integration & Solution Design

Associate Persona · Official Exam Domain 4 · **16% of the exam blueprint**

> **Status:** In progress — Module 4 is the active module.

## Why this domain matters

A useful AI response is not yet a reliable workflow.

Workflow integration determines how a business objective becomes a repeatable process with clear inputs, responsibilities, decision points, tools, state, validation, human review, and recovery behavior.

Production quality comes from the surrounding system as much as the model. A sound design assigns each responsibility to the component best suited for it and makes side effects, state, retries, approvals, and failures explicit.

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

> **Module thesis:** Do not ask whether Claude can participate in a workflow. Ask which responsibilities should be delegated to Claude, which should remain deterministic or human-controlled, and how the complete process will be validated and improved.

---

# Course-aligned roadmap

- [ ] 01. Module Introduction
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

No course lesson files are marked complete until the corresponding preparation-course material is supplied and converted into original public-safe study content.

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

# Durable engineering foundation

The existing repository material provides an engineering foundation that will be mapped to the supplied course sections as they arrive.

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

Potential patterns include:

| Pattern | Appropriate when |
|---|---|
| Interactive chat | A human remains continuously engaged and the task is contextual or exploratory |
| Fixed workflow | Steps, inputs, decisions, and outputs are predictable |
| API-backed application | The capability must be embedded in a repeatable product or business process |
| Bounded agent | The task needs limited planning and tool selection within explicit permissions and stopping rules |

Prefer the simplest pattern that satisfies the requirements.

## Responsibility partitioning

A reliable workflow separates responsibilities among:

- **Model:** interpretation, classification, synthesis, drafting, and judgment under bounded criteria;
- **Deterministic logic:** calculations, schemas, exact business rules, validation, routing, and authorization checks;
- **Tools:** controlled retrieval, transformation, external actions, and system interaction;
- **Storage:** authoritative records, workflow state, checkpoints, logs, and durable context;
- **Human:** objective setting, exception handling, professional judgment, approval, and accountability.

```text
Probabilistic judgment → model
Exact rule or calculation → deterministic component
External capability → controlled tool
Durable state → storage or system of record
Authority and accountability → human or organization
```

## Tool contracts

A tool contract should define:

- purpose;
- inputs and types;
- required versus optional fields;
- allowed values;
- authorization and permissions;
- expected output;
- error behavior;
- timeouts;
- retry policy;
- idempotency requirements;
- side effects;
- approval boundary; and
- audit evidence.

The model should not be expected to infer operational guarantees that the tool contract does not provide.

## Reliability controls

A production workflow may need:

- input validation;
- schema validation;
- deterministic calculations;
- source and provenance checks;
- human approval gates;
- idempotency keys;
- timeout handling;
- bounded retries;
- fallback paths;
- rollback or compensation;
- checkpointed state;
- stage-level logging;
- monitoring and alerts; and
- incident ownership.

## State and context

Long-running workflow state should not exist only inside a prompt or conversation.

Store durable state in an appropriate system:

- task identifier;
- current stage;
- completed actions;
- approved inputs;
- output versions;
- tool results;
- pending approvals;
- retry count;
- unresolved exceptions; and
- final disposition.

## Observability

Measure more than final success.

Track stage-level outcomes such as:

- input accepted or rejected;
- retrieval coverage;
- tool success and latency;
- validation pass rate;
- human-review rate;
- escalation reasons;
- retry and fallback frequency;
- release-blocking defects;
- correction rate; and
- business outcome.

A workflow that fails silently or cannot explain its decisions is difficult to improve and unsafe to scale.

---

# Learning objectives

By the end of this module, you should be able to:

- translate a business objective into workflow requirements and acceptance criteria;
- distinguish a technology capability from a viable use case;
- analyze stakeholders, inputs, decisions, constraints, risks, and governing obligations;
- research and document the current-state process before proposing automation;
- identify bottlenecks, handoffs, duplicated work, missing evidence, and unsuitable automation targets;
- choose among interactive chat, fixed workflow, API-backed application, and bounded-agent patterns;
- partition model, deterministic, tool, storage, and human responsibilities;
- design precise tool contracts;
- place validation and human approval at the correct boundaries;
- handle retries, idempotency, timeouts, fallback, rollback, and compensation;
- persist long-running state outside the prompt;
- instrument stage-level outcomes;
- iterate using observed failures and acceptance criteria;
- apply Delegation criteria to determine what Claude should and should not own;
- communicate expected value without overstating capability;
- communicate limitations, dependencies, uncertainty, and human responsibilities;
- redesign an existing workflow using the minimum necessary complexity; and
- prefer the simplest architecture that satisfies the requirements.

---

# Current module resources

The repository already contains extended engineering material that will remain available while the course-aligned lessons are developed.

- [notes.md](notes.md): Workflow-integration concepts and exam-focused decisions
- [lab.md](lab.md): Applied workflow-design exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

Course-aligned lessons and Module 4 prompt notebooks will be added as each supplied section is completed.

---

# Exam lens

Workflow scenarios often tempt the learner to place too much responsibility on the model.

Prefer:

- deterministic components for authorization, exact calculations, schema validation, and fixed business rules;
- controlled tools for external actions;
- storage or systems of record for durable state;
- human approval for consequential or irreversible decisions; and
- bounded model autonomy with explicit criteria, permissions, and stopping rules.

For scenario questions:

1. identify the actual business objective;
2. clarify the current process and acceptance criteria;
3. determine which stages require probabilistic judgment;
4. assign exact rules and calculations to deterministic components;
5. identify external tools and their permission boundaries;
6. store durable state outside the prompt;
7. place validation before downstream side effects;
8. place approval before irreversible actions;
9. define retries, fallback, and failure ownership;
10. instrument stage-level outcomes; and
11. select the least complex workflow that meets the requirement.

```text
Model asked to authorize action    → move authority to deterministic or human control
Long-running state in prompt       → persist externally
Retry may repeat a side effect     → require idempotency
Tool failure has no recovery path  → define timeout, retry, fallback, and owner
Workflow succeeds only on average  → inspect stage-level failures
Complex agent for fixed process    → simplify to a deterministic workflow
```

---

# Completion criteria

- [ ] I completed the Module 4 introduction.
- [ ] I can analyze requirements and distinguish viable use cases from attractive capabilities.
- [ ] I can research and map a current-state workflow.
- [ ] I can identify process-optimization opportunities and unsuitable automation targets.
- [ ] I can create a component responsibility matrix.
- [ ] I can design a clear tool contract.
- [ ] I can identify where idempotency is required.
- [ ] I can place meaningful validation and human-approval gates.
- [ ] I can describe state management, observability, fallback, and rollback.
- [ ] I can apply Delegation criteria to workflow stages.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client names, confidential workflows, proprietary operating procedures, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute architecture, security, legal, compliance, operational, or other professional advice.

## Official reading

Product capabilities and recommendations can change. Verify current official documentation before relying on implementation-specific behavior.

- [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
