# Delegation Boundary Mapping Pattern

## Purpose

Use this pattern to assign each workflow step to the model, deterministic logic, a controlled tool, durable storage, or a human role according to reversibility, stakes, and accountability.

> Map the work first. Assign features second.

## Problem

Teams often over-delegate because:

- Claude performed a previous step well;
- a favored Skill or integration already exists;
- human review is mentioned but not staffed;
- irreversible actions are hidden inside broad stages; or
- drafting quality is mistaken for authority.

## Core criteria

```text
Reversibility
+ Stakes
+ Accountability
↓
Minimum responsible delegation posture
```

Additional constraints such as data sensitivity, policy, evidence quality, and contractual duties may require stronger controls.

## Responsibility modes

| Mode | Use |
|---|---|
| AI-appropriate | Bounded extraction, classification, synthesis, or drafting |
| AI with code execution | Exact calculations, transformations, and reconciliation |
| Collaborative | AI prepares; qualified human evaluates and decides |
| Human-retained | Authority, professional judgment, exception handling, approval, and binding action |
| Deterministic | Fixed rules, schemas, routing, and authorization checks |
| Tool-owned | Controlled retrieval or external side effect |
| Storage-owned | Durable workflow state and authoritative records |

## Workflow

```text
Define outcome and boundary
      ↓
Map atomic steps
      ↓
Identify work type and side effects
      ↓
Assess reversibility, stakes, accountability
      ↓
Assign delegation mode
      ↓
Add validation and exception path
      ↓
Place human gates before consequence
      ↓
Assign Skills, code, tools, and storage
      ↓
Test handoffs and failures
      ↓
Record owners and evidence
```

## Mapping schema

For every step retain:

- step ID;
- current owner;
- source of truth;
- work type;
- output;
- reversibility;
- stakes and propagation risk;
- accountable role;
- delegation mode;
- feature or component;
- validation;
- approval gate;
- side effect;
- exception route;
- retained evidence.

## Meaningful human review

A collaborative stage requires:

```text
Named reviewer
+ Relevant expertise
+ Authority
+ Source and intermediate-output access
+ Time
+ Review criteria
+ Intervention rights
+ Recorded disposition
```

A missing element turns the stated review into a control gap.

## Feature assignment

Only after mapping:

- **Skill:** repeatable procedure, template, checklist, or specialized workflow guidance;
- **code execution:** exact data processing and calculations;
- **Project:** stable workflow context, knowledge, and instructions;
- **deterministic logic:** fixed policy or authorization rule;
- **tool:** controlled external operation;
- **storage:** state, approved versions, and audit evidence;
- **human gate:** judgment, authority, and accountability.

## Over-delegation checks

Flag when:

- AI approves its own draft;
- classification automatically triggers a consequential action;
- exact rules are left to probabilistic judgment;
- a calculation is generated as prose;
- an irreversible action has no approval stage;
- human review lacks a real reviewer;
- exceptions have no owner; or
- prior AI success is used to justify a new delegation.

## Common failure modes

### Halo delegation

A later step is delegated because an earlier step succeeded.

**Control:** assess every step independently.

### Collaborative in name only

A review box exists in the diagram but no qualified person performs it.

**Control:** define reviewer, evidence, criteria, time, and authority.

### Feature-first mapping

A Skill or integration drives the workflow design.

**Control:** map the work and risk before selecting features.

### Hidden side effect

The map ends before send, sign, file, pay, publish, or update.

**Control:** make the external action an explicit stage.

### Mechanical-but-material

A simple field transfer can propagate a harmful error.

**Control:** assess downstream consequence and add deterministic checks.

## Decision rule

```text
Reversible bounded preparation
→ AI or collaborative assistance with validation

Exact calculation or fixed rule
→ code or deterministic component

Professional approval or risk acceptance
→ human-retained

Irreversible external action
→ authorized human approval before controlled execution
```

## Related material

- [Delegation Mapping](../modules/04-workflow-integration-solutions-design/lessons/05-delegation-mapping.md)
- [Human Review Gate Pattern](human-review-gate-pattern.md)
- [Requirements Traceability and Pressure-Test Pattern](requirements-traceability-pressure-test-pattern.md)
- [Evidence-Driven Prototype Iteration Pattern](evidence-driven-prototype-iteration-pattern.md)
