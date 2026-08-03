# Use-Case Appropriateness Classification Pattern

## Problem

Teams often decide whether to use AI based on capability, convenience, or intuition. This produces inconsistent decisions, vague risk language, and ceremonial human review.

## Context

Use this pattern when evaluating whether Claude should assist with or participate in a proposed use case, especially when the work affects people, money, access, employment, health, legal rights, customer relationships, or organizational commitments.

## Recommended design

```text
Define bounded use case
      ↓
Assess reversibility, consequence, human element, and accountability
      ↓
Identify the load-bearing criterion
      ↓
Classify the use case
      ↓
Define the human gate or retained role
      ↓
Record conditions, owner, monitoring, and escalation
```

## Four criteria

### Reversibility

Can an incorrect output be detected and undone before consequence? Consider whether harm can realistically be repaired, not merely whether a record can be edited.

### Consequence of error

Assess physical, financial, legal, fairness, privacy, reputational, opportunity, operational, and relationship harms.

### Human creativity or empathy

Determine whether judgment, care, authenticity, relationship ownership, negotiation, or professional context is central to the work.

### Accountability

Identify the person or organization answerable for the result. Confirm that the accountable role has expertise, evidence, time, authority, intervention rights, and an escalation path.

## Load-bearing criterion

Name the criterion that would move the classification if it changed.

```text
All criteria considered
      ↓
One criterion controls the boundary
      ↓
Decision becomes explainable
```

## Classifications

### Fully appropriate

Reversible, low consequence, suitably grounded, no special human element, and normal review is sufficient.

### Appropriate with human review

AI assistance is useful, but consequence, fairness, relationship sensitivity, policy exposure, or accountability requires a pre-use gate.

### Inappropriate

AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, policy prohibition, or absence of meaningful review.

## Human gate contract

Every human-reviewed classification must define:

- **Who:** accountable and qualified reviewer;
- **What:** specific evidence, facts, risks, fairness, or policy conditions checked;
- **When:** review before use or consequence;
- authority to reject or modify;
- exception and escalation path; and
- retained approval evidence.

```text
Human in the loop
      ≠
Operational human gate
```

## Decision record

Record:

- use-case owner;
- intended outcome;
- users and affected parties;
- four-criteria assessment;
- load-bearing criterion;
- classification;
- gate or retained human role;
- policy and data conditions;
- monitoring and escalation;
- approver; and
- review date.

## Failure modes

### Capability-first approval

**Repair:** evaluate consequence, reversibility, human element, and accountability before capability.

### Vague review

**Repair:** define who, what, and when.

### Single-criterion shortcut

**Repair:** run all four and name the controlling criterion.

### Model accountability

**Repair:** assign accountability to a human or organization with intervention rights.

### Rubber-stamp gate

**Repair:** require qualified, evidence-based review before consequence.

### Vague risk language

**Repair:** name the criterion, consequence, gate, and owner.

## Compact decision rule

> Run all four Delegation criteria, name the load-bearing one, classify the use case, and treat the who/what/when human gate—or the retained human role—as part of the classification itself.
