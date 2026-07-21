# Module 2 — Parallel Case Prompt Notebook

Use fictional, synthetic, public, or explicitly authorized material only.

## 1. Identify the shared foundation

```text
A single source must produce these deliverables:
- [DELIVERABLE 1]
- [DELIVERABLE 2]
- [DELIVERABLE 3]

Identify the information or interpretation all three outputs depend on. Define the shared foundation that should be created and validated before drafting begins.
```

## 2. Design the extraction artifact

```text
Design a structured extraction artifact for this source:
[SOURCE DESCRIPTION]

The artifact must support these downstream outputs:
[OUTPUTS]

Specify fields, source-reference requirements, missing-data behavior, uncertainty labels, and acceptance criteria.
```

## 3. Create a validation gate

```text
Review this proposed shared foundation:
[FOUNDATION]

Evaluate completeness, accuracy, traceability, internal consistency, uncertainty, and fitness for downstream use. Return:
1. blocking defects;
2. non-blocking concerns;
3. corrections required;
4. approval recommendation.
```

## 4. Classify dependencies

```text
Given this workflow:
[STAGES]

Classify every pair of stages as:
- sequential dependency;
- safe to run in parallel;
- conditionally parallel; or
- unrelated.

Explain the dependency evidence and identify the earliest safe fan-out point.
```

## 5. Build parallel task contracts

```text
Using this approved shared foundation:
[FOUNDATION]

Create separate task contracts for these audiences:
[AUDIENCES AND DELIVERABLES]

For each contract specify objective, audience, allowed evidence, constraints, output format, uncertainty behavior, and success criteria. Do not alter the underlying facts.
```

## 6. Create a branch state capsule

```text
Create a compact state capsule that can be supplied to independent drafting branches. Include:
- approved facts;
- source references;
- canonical terminology;
- effective dates;
- unresolved questions;
- prohibited claims;
- version identifier;
- review requirements.

Source foundation:
[FOUNDATION]
```

## 7. Reconcile parallel outputs

```text
Compare these parallel deliverables against the approved foundation:
[FOUNDATION]

Deliverables:
[OUTPUTS]

Identify contradictions, terminology drift, date mismatches, unsupported implications, inconsistent uncertainty, and audience adaptation that changes meaning. Return a reconciliation table and corrected language.
```

## 8. Diagnose propagation risk

```text
Analyze this workflow for error propagation:
[WORKFLOW]

Identify:
1. shared upstream assumptions;
2. defects that could contaminate multiple outputs;
3. validation gates;
4. rollback points;
5. outputs requiring human approval.
```

## 9. Fan-out/fan-in exercise

```text
Turn this overloaded request into a fan-out/fan-in workflow:
[REQUEST]

Use this structure:
Shared source → extraction → validation → parallel branches → reconciliation → final release.

For each stage define Input, Process, Output, Validation, owner, and failure behavior.
```

## 10. Teach-back

```text
Explain the shared-foundation parallel pattern to a colleague using one original example. Distinguish:
- sequential work;
- parallel work;
- fan-out;
- fan-in;
- shared state;
- validation gates.

End with a five-question self-test.
```
