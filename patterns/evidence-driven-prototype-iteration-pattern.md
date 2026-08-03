# Evidence-Driven Prototype Iteration Pattern

## Purpose

Use this pattern to turn AI-assisted design work into a controlled learning loop rather than a sequence of disconnected drafts.

> Each iteration should reduce uncertainty, preserve approved context, and produce evidence for the next decision.

## Problem

Teams often:

- ask for a complete solution in one prompt;
- restart context every round;
- accept unclassified feedback;
- add features without a requirement;
- fix one behavior while breaking another;
- confuse demo success with production readiness; or
- continue iterating after measurable progress has stopped.

## Core loop

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

## Required inputs

- approved requirements;
- user and use case;
- constraints;
- data definitions;
- acceptance criteria;
- known risks;
- decision and approval owners;
- prior decision log; and
- prototype version.

## Step 1: Stabilize context

Store project-specific knowledge and instructions, approved requirements, terminology, decisions, and unresolved questions in a durable workspace.

Do not rely on the model to reconstruct prior decisions from memory alone.

## Step 2: Generate alternatives

Require differences in architecture, interaction, delegation, or process—not just layout.

Compare options by:

- user value;
- requirement fit;
- risk;
- implementation effort;
- data and tool needs;
- human-review burden; and
- testability.

## Step 3: Define prototype hypothesis

```text
For [user],
this [prototype capability]
should improve [observable outcome]
under [stated conditions].
```

Record what would disprove the hypothesis.

## Step 4: Bound the prototype

Include only features needed to test the riskiest assumptions and core task.

Record exclusions and prohibited uses.

## Step 5: Gather structured evidence

Classify findings as:

- requirement;
- correctness;
- usability;
- accessibility;
- performance;
- privacy or disclosure;
- preference;
- new requirement; or
- out of scope.

## Step 6: Make a controlled change

```text
Observation
  → Cause hypothesis
  → Bounded change
  → Expected result
  → Preserved requirements
  → Regression tests
```

## Step 7: Re-test

Run:

- affected acceptance tests;
- previously passing regression tests;
- data and calculation checks;
- accessibility and disclosure checks; and
- user-task validation.

## Step 8: Record the decision

| Decision | Meaning |
|---|---|
| Continue | Another bounded test is justified |
| Accept for learning | Prototype met its stated learning objective |
| Redesign | Current approach cannot satisfy the requirement efficiently |
| Escalate | Missing authority, evidence, architecture, security, or expertise |
| Stop | Marginal value no longer justifies another cycle |

## Prototype-to-production gate

A production review should separately assess:

- authentication and authorization;
- data classification and privacy;
- security;
- accessibility;
- performance and scale;
- persistence and state;
- monitoring and support;
- release and rollback;
- audit evidence; and
- accountable approval.

```text
Working prototype
      ≠
Production-ready solution
```

## Dashboard example

```text
Cycle 1: display five verified metrics
Cycle 2: add region filter and computed totals
Cycle 3: add direction-aware deltas and print layout
```

Every cycle preserves metric definitions, source mapping, missing-data behavior, and previously passing tests.

## Metrics

Track:

- acceptance criteria passed;
- regressions introduced;
- high-severity defects remaining;
- user-task completion;
- feedback resolution rate;
- cycle time;
- changes rejected as preference or out of scope;
- prototype-to-production gaps; and
- marginal improvement by iteration.

## Failure modes

### One-shot build

**Control:** Prototype the riskiest assumptions first.

### Context drift

**Control:** Preserve requirements and decisions in a stable workspace.

### Feature accumulation

**Control:** Require requirement, user outcome, priority, and test for each feature.

### Preference before correctness

**Control:** Classify and prioritize feedback.

### No regression testing

**Control:** Define preserved behavior before each change.

### Endless iteration

**Control:** Use stopping rules and marginal-value review.

### Demo-to-production leap

**Control:** Apply a separate production-readiness gate.

## Decision rule

```text
Iterate while a bounded change can produce measurable evidence.
Stop or escalate when the remaining problem is authority, architecture,
security, missing requirements, or declining marginal value.
```

## Related material

- [Solution Design, Development, and Iteration](../modules/04-workflow-integration-solutions-design/lessons/04-solution-design-development-iteration.md)
- [Verified Planning Workflow Pattern](verified-planning-workflow-pattern.md)
- [Requirements Traceability and Pressure-Test Pattern](requirements-traceability-pressure-test-pattern.md)
- [Human Review Gate Pattern](human-review-gate-pattern.md)
