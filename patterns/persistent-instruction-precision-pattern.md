# Persistent Instruction Precision Pattern

## Problem

Teams place vague aspirations into persistent instructions and assume the desired behavior will follow consistently.

Examples include:

- be professional;
- be accurate;
- be concise;
- do not hallucinate; and
- make the report good.

These phrases do not define evidence, failure behavior, or observable output.

## Context

Use this pattern when a recurring workspace needs stable behavior across conversations, including verification, formatting, tone, uncertainty, review, or escalation behavior.

## Recommended design

```text
Identify recurring behavior
      ↓
Separate behavior from facts and procedures
      ↓
Define trigger and evidence boundary
      ↓
Define required and failure behavior
      ↓
Define observable output
      ↓
Apply two-reader test
      ↓
Test, version, approve, and maintain
```

## Instruction contract

For each material instruction, record:

- ID;
- purpose;
- trigger;
- scope;
- required behavior;
- prohibited behavior;
- evidence boundary;
- missing-data behavior;
- conflict behavior;
- observable output;
- owner;
- version;
- tests;
- approval;
- effective date; and
- review date.

## Precision rule

```text
Vague aspiration
      ≠
Testable instruction
```

A strong instruction states what Claude should do, what it may rely on, what it should do when the requirement cannot be satisfied, and how compliance can be observed.

## Two-reader test

Ask whether two competent readers would interpret the instruction the same way.

If not, add:

- defined terms;
- measurable thresholds;
- named formats;
- source boundaries;
- examples;
- failure behavior; or
- precedence.

## Mechanism boundaries

```text
Behavior → Project instructions
Facts → Project knowledge
Procedure → Skill
Continuity → scoped Memory
Exact rule or authorization → deterministic control
Temporary exception → current request
Secret → approved secret handling
```

Do not duplicate the same responsibility across several mechanisms.

## Failure behavior

Every instruction that depends on evidence should define one or more allowed outcomes:

- supported;
- unknown;
- unverified;
- conflicting;
- not applicable;
- requires clarification; or
- requires escalation.

## Control pairing

Natural-language instructions cannot independently enforce identity, permissions, data isolation, external-action restrictions, approval authority, or exact business rules.

Pair consequential instructions with:

- least-privilege access;
- deterministic validation;
- tool restrictions;
- human review;
- approval gates;
- logging; and
- systems of record.

## Test design

Use:

- positive tests;
- missing-evidence tests;
- conflict tests;
- bypass attempts;
- format exceptions;
- unrelated-task tests;
- draft-versus-approved tests; and
- regression tests after change.

## Common failure modes

### Vague language

**Repair:** define observable behavior and thresholds.

### No uncertainty behavior

**Repair:** define unknown, unverified, conflict, clarification, or escalation outcomes.

### Instruction overload

**Repair:** move facts, procedures, state, and exact controls to their proper layers.

### Conflicting rules

**Repair:** record authority, owner, scope, version, and resolution path.

### Instruction treated as enforcement

**Repair:** add technical, deterministic, and human controls.

### Untested change

**Repair:** rerun representative and regression cases before release.

## Compact decision rule

> Put stable behavior in persistent instructions, make every material rule observable under the two-reader test, define what happens when it cannot be satisfied, and pair consequential guardrails with enforceable controls.

## Review checklist

- Is the requirement truly durable behavior?
- Is it separate from facts and procedures?
- Is the trigger clear?
- Is the evidence boundary explicit?
- Is failure behavior defined?
- Is the output observable?
- Would two readers interpret it the same way?
- Are conflicts and precedence documented?
- Are technical and human controls paired where needed?
- Are tests, owner, version, and review date present?
