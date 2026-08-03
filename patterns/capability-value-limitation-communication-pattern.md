# Capability, Value, and Limitation Communication Pattern

## Problem

Teams describe an AI-assisted workflow with broad labels such as `automated`, `handles`, or `human-level`. These claims hide workflow boundaries, human labor, limitations, and approval controls. Trust collapses when a visible failure reveals that the system did less—or relied on more human judgment—than stakeholders were told.

## Context

Use this pattern when communicating an AI-assisted workflow to managers, executives, clients, users, legal or compliance teams, security or risk functions, reviewers, or approvers.

## Forces

- Stakeholders need a concise explanation.
- Different audiences require different detail.
- Value claims create pressure to simplify or inflate.
- Human review can be hidden or described vaguely.
- Limitations can be omitted, overstated, or buried in generic disclaimers.
- Pilot evidence may not support scale-wide claims.
- The message itself may influence approval, adoption, or risk acceptance.

## Design

Build every stakeholder description from seven controlled elements:

```text
Bounded AI task
+ explicit exclusions
+ measured value
+ evidence scope
+ material limitations
+ human and technical controls
+ accountable message owner
```

## Sequence

```text
1. Identify audience and decision
2. Define the actual workflow boundary
3. State Claude's bounded tasks
4. State decisions and actions not delegated
5. Assemble evidence for each value claim
6. Scope the claim to cases, period, and conditions
7. Identify material limitations and dependencies
8. Document review, approval, exception, and incident controls
9. Adapt depth and emphasis without changing facts
10. Review and approve the stakeholder message
```

## Capability statement template

```text
Claude [bounded tasks].
It does not [excluded authority or actions].
[Named role] reviews or approves [consequential output].
Observed value is [measured result] under [scope and period].
Known limitations include [material failure modes or dependencies].
```

## Value-evidence contract

A defensible value claim records:

- metric definition;
- baseline;
- comparison period;
- case and user scope;
- source system;
- quality or approval standard;
- exceptions and corrections;
- confounding factors; and
- claim owner.

```text
Pilot observation
      ≠
Universal capability
      ≠
Guaranteed outcome
```

## Audience adaptation

Adapt:

- depth;
- vocabulary;
- order;
- examples;
- technical detail; and
- emphasis.

Preserve:

- capability boundary;
- verified metrics;
- scope;
- uncertainty;
- limitations;
- data boundary;
- review and approval model;
- external-action control; and
- material risk.

## Oversight contract

A human-review statement is operational only when it identifies:

- qualified reviewer;
- evidence available;
- review criteria;
- decision authority;
- intervention rights;
- exception route;
- timing before consequence; and
- retained approval record.

## Controls

- Maintain a communication register.
- Link value claims to source evidence.
- Review audience variants for invariant drift.
- Require a named owner and review date.
- Revalidate claims after workflow, model, data, or policy changes.
- Separate pilot evidence from production claims.
- State external actions and approval gates explicitly.

## Common failure modes

### Capability inflation

A narrow preparation task is described as end-to-end ownership.

### Metric inflation

A result is reported without baseline, sample, scope, or quality measure.

### Hidden human labor

Review, correction, exception handling, or approval is omitted from the value story.

### Audience distortion

Executive simplification removes uncertainty or material controls.

### Limitation dumping

A generic disclaimer replaces the specific limitations relevant to the decision.

### Assurance theater

Controls are named but not staffed, evidenced, authorized, or operational.

### Pilot generalization

Success on standard cases is presented as proof for all cases or future scale.

## Trade-offs

More precise communication may sound less dramatic, but it improves trust, risk decisions, adoption quality, incident handling, and long-term credibility.

## Decision rule

> Describe the workflow so that the first visible failure confirms the stated boundaries rather than contradicting them.

## Compact checklist

```text
TASK      → What does Claude perform?
EXCLUDE   → What does it not decide or execute?
VALUE     → What measured improvement is established?
SCOPE     → Under what cases, period, data, and conditions?
LIMIT     → What can fail or require escalation?
CONTROL   → Who reviews, approves, monitors, and intervenes?
AUDIENCE  → What detail does this stakeholder need?
OWNER     → Who approves the claim?
```

## Public-repository content rule

Use fictional, generic, synthetic, public, or explicitly authorized examples. Do not include confidential pilot metrics, client names, internal incidents, approval records, or nonpublic workflow details.
