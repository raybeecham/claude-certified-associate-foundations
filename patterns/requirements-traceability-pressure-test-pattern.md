# Requirements Traceability and Pressure-Test Pattern

## Purpose

Use this pattern to convert unstructured business material into a reviewable requirement baseline that preserves source authority, exposes uncertainty, and supports later workflow design.

> Structure the requirements, then challenge the structure before treating it as truth.

## Problem

Requirements often arrive as documents, email threads, meeting notes, examples, and verbal asks. A single narrative summary can hide:

- omitted obligations;
- merged requirements;
- ambiguous terms;
- implied conditions;
- conflicting versions;
- unsupported assumptions;
- missing owners; and
- requirements that cannot be tested.

## Inputs

- business need and intended outcome;
- source inventory and authority hierarchy;
- approved, draft, superseded, reference, and internal-answer material;
- stakeholders and decision owners;
- governing constraints; and
- known deadlines and acceptance standards.

## Requirement states

| State | Meaning |
|---|---|
| Explicit | Directly stated in the controlling source |
| Implied | Inferred from criteria, dependencies, or cross-references |
| Ambiguous | Supports multiple material interpretations |
| Missing | Needed for a buildable or testable task but absent |
| Conflicting | Relevant sources disagree |
| Assumption | Temporary premise pending confirmation |
| Constraint | Limits the solution or method |
| Acceptance criterion | Defines observable completion |

## Recommended design

```text
Define business outcome
      ↓
Inventory and rank sources
      ↓
Extract atomic requirements
      ↓
Attach exact traceability
      ↓
Classify requirement state
      ↓
Link existing evidence and ownership
      ↓
Pressure-test coverage and interpretation
      ↓
Resolve clarifications and conflicts
      ↓
Approve baseline
      ↓
Map to workflow stages and tests
```

## Requirement record

Each row should include:

- stable ID;
- short label;
- full requirement statement;
- classification;
- controlling source and exact location;
- conditions and exceptions;
- answer or evidence status;
- ambiguity or gap;
- owner and approver;
- acceptance criterion; and
- change history where needed.

## Pressure-test controls

Review the first extraction for:

1. omitted clauses and subordinate conditions;
2. requirements split too narrowly or combined too broadly;
3. duplicate obligations;
4. superseded language and amendment conflicts;
5. implied requirements mislabeled as explicit;
6. examples mistaken for mandates;
7. assumptions presented as facts;
8. internal answers that do not satisfy the source;
9. missing actors, dates, formats, data sources, or owners; and
10. requirements that cannot be tested.

## Source-authority rule

```text
Current controlling source
      >
Superseded source
      >
Reference example
```

The exact hierarchy depends on the domain. When authority is unclear, preserve the conflict and assign a human decision rather than silently choosing.

## Requirement-quality test

A strong requirement is, where applicable:

- necessary;
- traceable;
- clear;
- atomic;
- feasible;
- testable;
- bounded;
- owned;
- authorized; and
- current.

## Use-case handoff

An approved requirement set becomes a viable AI use case only when it connects:

```text
Measurable outcome
+ user and current process
+ repeatable task
+ authorized inputs
+ bounded AI contribution
+ retained human authority
+ deterministic controls
+ acceptance criteria
+ risk and escalation
```

## Failure modes

### Narrative-only summary

**Risk:** Work cannot be assigned or tested.

**Control:** Use atomic traceable rows.

### Inference laundering

**Risk:** An interpretation becomes an apparent obligation.

**Control:** Label implied requirements and require confirmation.

### One-pass confidence

**Risk:** Hidden conditions and omissions survive.

**Control:** Run a separate pressure-test pass.

### Version blindness

**Risk:** Draft or superseded language controls the output.

**Control:** Inventory and rank sources first.

### Untestable requirements

**Risk:** Completion cannot be demonstrated.

**Control:** Add measurable acceptance criteria or preserve the unresolved gap.

### Feature-first design

**Risk:** Claude capability is mistaken for business value.

**Control:** Start with outcome, process, risk, and ownership.

## Metrics

Possible measures include:

- requirement recall;
- percentage with exact source traceability;
- ambiguity rate;
- unresolved conflict rate;
- answer-coverage rate;
- percentage with owner and acceptance criterion;
- material omissions found after baseline approval;
- clarification cycle time; and
- downstream rework caused by requirement defects.

## Compact decision rule

```text
If a requirement cannot be traced, classified, interpreted consistently, owned, and tested,
it is not ready to drive workflow design.
```

## Related material

- [Analyzing Requirements and Use Cases](../modules/04-workflow-integration-solutions-design/lessons/02-analyzing-requirements-use-cases.md)
- [Module 4 Introduction](../modules/04-workflow-integration-solutions-design/lessons/01-module-introduction.md)
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md)
- [Grounded Verification Pattern](grounded-verification-pattern.md)
