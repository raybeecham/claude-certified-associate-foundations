# Governance Diligence Gap Closure Pattern

## Problem

Organizations may have current AI policies while day-to-day use quietly diverges from them.

Common symptoms include:

- sensitive data entering an unapproved environment;
- Skills enabled without review;
- human gates bypassed under deadline pressure;
- stale policy language embedded in Projects or procedures;
- expired exceptions remaining active; and
- corrective actions marked complete without evidence.

The core problem is not merely that a rule was broken. It is that required and observed practice are no longer aligned.

## Context

Use this pattern when:

- auditing actual or planned AI use;
- reviewing adherence to organizational policy;
- investigating a near miss or recurring deviation;
- validating required human review;
- managing policy exceptions;
- reviewing approved entry points, Skills, connectors, or data use; or
- assessing whether governance controls remain operational after change.

## Forces

The design must balance:

- policy fidelity;
- privacy and proportionate monitoring;
- practitioner usability;
- business deadlines;
- root-cause correction;
- accountable ownership;
- evidence quality;
- exception flexibility;
- technical enforceability; and
- continuous improvement.

## Recommended design

```text
Identify controlling policy
      ↓
Translate policy into observable controls
      ↓
Sample authorized evidence of real use
      ↓
Record Diligence gaps
      ↓
Contain immediate exposure
      ↓
Correct root cause
      ↓
Verify closure
      ↓
Re-audit and monitor
```

## 1. Establish the controlling requirement

Record:

- policy or standard;
- version and effective date;
- owner;
- applicable users, data, features, and workflows;
- required approvals;
- allowed exceptions; and
- superseded guidance.

```text
Policy remembered
      ≠
Current controlling policy
```

## 2. Translate policy into observable practice

Each material rule should map to:

- expected practitioner behavior;
- workflow or technical control;
- evidence;
- accountable owner;
- review frequency; and
- escalation condition.

A requirement that cannot be observed or verified is likely to become ceremonial.

## 3. Bound the audit

Define:

- review period;
- sampled workflows or Projects;
- approved evidence sources;
- privacy limits;
- audit owner;
- sampling method;
- severity criteria; and
- handling of discovered sensitive information.

```text
Governance audit
      ≠
Unlimited surveillance
```

## 4. Record the Diligence gap

A gap record should contain:

- requirement;
- observed behavior;
- evidence;
- frequency and scope;
- affected parties;
- consequence;
- root cause;
- containment;
- corrective action;
- owner and due date;
- closure test; and
- status.

## 5. Separate containment from correction

Immediate containment limits current exposure.

Examples:

- remove sensitive material;
- disable an unvetted Skill;
- revoke excessive connector access;
- pause a workflow;
- restore a required reviewer; or
- notify the authorized owner.

Corrective action prevents recurrence.

Examples:

- repair the approved workflow;
- add a technical gate;
- clarify policy;
- update configuration;
- narrow permissions;
- add a backup reviewer;
- revise incentives or deadlines; or
- establish exception management.

```text
Contained
      ≠
Remediated
      ≠
Verified closed
```

## 6. Diagnose root cause

Consider:

- unclear policy;
- poor discoverability;
- inconvenient approved path;
- missing technical controls;
- excessive default access;
- outdated configuration;
- insufficient staffing;
- deadline pressure;
- unclear ownership;
- stale training;
- product or feature change; and
- informal exception practices.

Avoid treating every deviation as individual negligence.

## 7. Prefer durable controls

A durable corrective-action hierarchy is:

```text
Policy and ownership clarity
      ↓
Workflow and configuration repair
      ↓
Technical access or approval controls
      ↓
Training and communication
      ↓
Monitoring and re-audit
```

Training alone is insufficient when the compliant path remains unclear, slow, or technically bypassable.

## 8. Manage exceptions explicitly

Every exception needs:

- controlling requirement;
- rationale;
- scope;
- duration;
- affected data and users;
- risk assessment;
- compensating controls;
- approving authority;
- owner;
- monitoring;
- expiration; and
- closure or renewal decision.

```text
Exception granted
      ≠
Permanent exemption
```

## 9. Verify closure

Closure evidence should show that:

- the required behavior changed;
- the control operates;
- the bypass path is removed or monitored;
- the owner accepted responsibility;
- no new material risk was introduced; and
- the result persists across representative cases.

## 10. Re-audit after change

Review after:

- policy updates;
- new features or entry points;
- Skill or connector changes;
- data-classification changes;
- team or owner changes;
- incidents or near misses;
- exception expiration; and
- operational scaling.

## Controls

- current policy register;
- observable-control mapping;
- authorized audit plan;
- Diligence-gap register;
- root-cause analysis;
- immediate containment;
- corrective-action tracker;
- exception register;
- closure tests;
- re-audit schedule; and
- retained evidence.

## Failure modes

### One-time acknowledgment

Users completed policy training once, but routine behavior is never checked.

**Repair:** establish recurring and event-triggered audits.

### Reminder-only remediation

The same deviation returns because the workflow and permissions never changed.

**Repair:** address the root cause and technical bypass path.

### Closed without evidence

An owner reports that the issue is fixed.

**Repair:** require a defined verification test and retained evidence.

### Audit overreach

Monitoring collects more personal or sensitive data than governance requires.

**Repair:** bound the audit and apply minimization and access controls.

### Permanent exception

A temporary bypass remains active after its need ends.

**Repair:** require expiration, renewal authority, and closure review.

### Stale policy baseline

The audit compares behavior with superseded guidance.

**Repair:** identify the controlling version before assessment.

## Compact decision rule

> Compare observed behavior with the current controlling policy, record the gap, contain immediate exposure, repair the root cause, verify closure with evidence, and re-audit after material change.

## Review checklist

- Is the controlling policy and version known?
- Is the requirement translated into observable behavior?
- Is the audit bounded and authorized?
- Is the gap supported by evidence?
- Are containment and corrective action separated?
- Is root cause identified?
- Is the action owned and time-bound?
- Are exceptions explicit and expiring?
- Is closure independently verifiable?
- Is re-audit scheduled?
