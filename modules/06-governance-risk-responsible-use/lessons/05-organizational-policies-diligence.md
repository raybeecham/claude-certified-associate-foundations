# Lesson 5: Organizational Policies and Diligence as a Habit

## Overview

Governance fails when policy and practice drift apart.

```text
Written policy
      ↓
Daily practitioner decisions
      ↓
Observed behavior
      ↓
Usage audit
      ↓
Diligence gaps
      ↓
Corrective action and re-audit
```

> Diligence is the repeated habit of applying current policy, verifying real behavior, recording exceptions, and closing gaps before they become incidents.

This lesson develops four capabilities:

1. applying governance consistently during routine work;
2. auditing actual and planned AI use against policy;
3. converting policy gaps into owned corrective actions; and
4. staying current as products, features, data practices, and policies change.

---

# Plain-English explanation

A policy does not govern a workflow merely because employees acknowledged it once.

Governance is present only when people repeatedly:

- classify the data;
- use approved products and entry points;
- vet Skills and connectors;
- preserve required human review;
- document exceptions;
- respond to policy changes; and
- correct noncompliant behavior.

```text
Policy acknowledged
      ≠
Policy operationalized
```

The risk often appears in ordinary decisions made under routine pressure rather than in deliberate misconduct.

---

# One analogy: preventive maintenance

A safety manual does not keep equipment reliable by sitting on a shelf.

Operators inspect the equipment, compare its condition with the standard, record defects, assign repairs, and verify that repairs worked.

Governance follows the same cycle:

```text
Standard
  ↓
Observe real use
  ↓
Identify deviation
  ↓
Repair the process
  ↓
Verify closure
```

---

# Governance as a sustained habit

Apply the framework to low-visibility decisions as well as obvious high-stakes work.

Routine examples include:

- uploading an internal draft;
- enabling a convenient Skill;
- connecting a new data source;
- using Incognito for confidential work;
- skipping a required review under deadline pressure;
- retaining outdated Project knowledge;
- allowing a personal copy of a procedure to drift; and
- sharing an AI-generated draft with a broader audience.

Small deviations accumulate into normal practice when they are not detected and corrected.

```text
Repeated exception
      ↓
Unrecorded norm
      ↓
Governance drift
```

---

# Policy-to-practice mapping

A policy should be translated into observable controls.

| Policy requirement | Observable practice | Evidence |
|---|---|---|
| Use approved entry points | Sensitive work occurs only in approved environments | Product, account, or access record |
| Classify data before use | Data tier recorded before upload or retrieval | Intake or decision record |
| Vet executable Skills | Source, contents, reach, and approval reviewed | Skill trust register |
| Require human approval | Qualified reviewer acts before consequence | Approval record or workflow event |
| Apply least privilege | Connector and tool access is narrowly scoped | Permission inventory |
| Maintain configurations | Instructions, knowledge, Skills, connectors, and Memory are reviewed | Maintenance record |
| Record exceptions | Authorized exception has owner, scope, expiration, and conditions | Exception register |

A requirement that cannot be observed or evidenced is difficult to audit and easy to bypass unintentionally.

---

# Usage audits

A usage audit compares actual or planned behavior with the controlling policy and approved configuration.

## Audit scope

Define:

- review period;
- teams, Projects, or workflows included;
- policy version;
- approved products and entry points;
- applicable data classes;
- Skills, connectors, and external actions;
- required review gates;
- exception records;
- sample method; and
- accountable audit owner.

## Evidence sources

Use only evidence that is authorized and necessary, such as:

- Project and configuration inventories;
- source and connector registers;
- access and permission records;
- approved usage records;
- review or approval logs;
- exception registers;
- maintenance records;
- incident reports; and
- interviews with workflow owners.

Do not create a governance audit that itself violates privacy, access, or monitoring policy.

```text
Audit authority
      ≠
Unlimited surveillance authority
```

---

# Diligence gaps

A Diligence gap is a difference between required governance and observed practice.

Examples include:

- sensitive data entered through an unapproved path;
- a Skill enabled without source or reach review;
- a connector retaining unused permissions;
- a required human gate skipped;
- a reviewer lacking evidence or intervention authority;
- a policy exception continuing after expiration;
- old policy language embedded in instructions or Skills;
- missing approval records;
- a high-impact use operating without monitoring; or
- users relying on an assumed rule instead of current guidance.

## Gap record

| Field | Purpose |
|---|---|
| Gap ID | Stable reference |
| Policy requirement | Controlling rule |
| Observed practice | What actually occurred |
| Evidence | Support for the finding |
| Scope and frequency | Isolated or systemic |
| Risk and affected parties | Potential consequence |
| Root cause | Why the gap occurred |
| Immediate containment | Near-term protection |
| Corrective action | Sustainable repair |
| Owner and due date | Accountability |
| Verification test | Closure evidence |
| Status | Open, accepted, remediated, verified |

```text
Gap identified
      ≠
Gap closed
```

Closure requires evidence that the corrective action changed the practice.

---

# Root causes and corrective actions

Do not treat every gap as an individual training failure.

Potential root causes include:

- policy is difficult to locate or interpret;
- approved entry points are unclear;
- the workflow makes the compliant path slower;
- permissions are overbroad by default;
- the review gate lacks staffing;
- product or feature behavior changed;
- configuration still encodes an old process;
- deadline pressure rewards bypassing controls;
- ownership is unclear; or
- exceptions are informal and untracked.

## Corrective-action hierarchy

Prefer durable system or workflow repairs over reminders alone.

```text
Clarify policy and ownership
      ↓
Repair configuration and workflow
      ↓
Narrow technical access
      ↓
Add required approval and evidence
      ↓
Train affected users
      ↓
Monitor and re-audit
```

Training can be useful, but it does not replace a broken workflow, missing control, or unstaffed gate.

---

# Staying current

Policies, laws, organizational risk decisions, products, features, and permissions can change.

Use both scheduled and event-triggered review.

## Scheduled review

Possible cadence depends on risk and change rate:

- monthly for active or rapidly changing workflows;
- quarterly for stable but material uses;
- annually for low-change archived uses; and
- more frequently for high-impact or regulated work.

## Event triggers

Review after:

- policy revision;
- new feature or connector availability;
- change in retention or Memory behavior;
- new Skill version;
- data-classification change;
- role or ownership change;
- expansion to new users or affected populations;
- incident or near miss;
- audit finding;
- new legal or contractual requirement; or
- a prototype becoming operational infrastructure.

```text
Previously approved
      ≠
Permanently approved
```

---

# Worked example: one-month usage audit

A fictional team reviews one month of approved AI-assisted work.

## Gap 1: Unreleased product document

**Observed practice:** A marketing employee used a non-approved entry point for an unreleased product specification.

**Likely root causes:** The approved path was unclear and the product document was treated as ordinary internal material.

**Corrective actions:**

- clarify the data-classification example;
- publish the approved entry-point rule in the Project setup;
- add a pre-upload classification prompt; and
- verify usage during the next review.

## Gap 2: Unvetted Skill

**Observed practice:** A useful Skill was enabled without a source, bundle, or effective-reach review.

**Likely root causes:** The Skill was internally shared and therefore assumed to be trusted.

**Corrective actions:**

- add a required Skill trust record;
- designate the approving role;
- inspect the bundle and reach;
- disable or restrict it pending review; and
- retest before approval.

## Gap 3: Human gate skipped

**Observed practice:** A recurring client report bypassed its required reviewer twice during deadline pressure.

**Likely root causes:** The reviewer was unavailable and the workflow allowed release without evidence of approval.

**Corrective actions:**

- define a backup qualified reviewer;
- prevent release until approval is recorded;
- establish an urgent escalation path; and
- monitor the next reporting cycles.

```text
Invisible drift
      ↓
Audited evidence
      ↓
Owned corrective actions
      ↓
Verified closure
```

None of the gaps requires assuming malicious intent. Governance focuses on repairing the conditions that allowed the deviations.

---

# Exception management

An exception should not become a permanent undocumented bypass.

Record:

- policy requirement;
- reason the standard control cannot be followed;
- affected use, data, users, and duration;
- risk assessment;
- compensating controls;
- approving authority;
- owner;
- effective and expiration dates;
- monitoring; and
- closure or renewal decision.

```text
Exception approved
      ≠
Policy requirement removed
```

Expired or expanded exceptions require new review.

---

# Diligence operating cycle

```text
1. Identify the controlling policy and version
2. Translate requirements into observable controls
3. Define the usage-audit scope and authorized evidence
4. Compare observed practice with required practice
5. Record each Diligence gap and affected risk
6. Identify root cause, not only the visible error
7. Contain immediate exposure
8. Assign durable corrective actions, owner, and due date
9. Retest and verify closure
10. Update policy, configuration, training, and monitoring
11. Re-audit on cadence and after material events
```

---

# Exam lens

```text
Policy acknowledged once                 → insufficient; apply continuously
Routine low-visibility deviation         → Diligence gap
Actual use differs from policy           → record and remediate
Gap found without owner or verification  → not closed
Repeated bypass under deadlines          → repair workflow and approval control
Internal Skill assumed safe              → require trust review
Old compliant practice after policy change → re-evaluate
No policy located                        → pause or seek authorized clarification
```

For policy-and-Diligence scenarios:

1. identify the controlling policy and version;
2. compare observable practice with the requirement;
3. distinguish isolated error from systemic drift;
4. identify root cause;
5. apply immediate containment when needed;
6. choose durable corrective action;
7. assign owner, due date, and evidence;
8. manage exceptions explicitly;
9. verify closure rather than accepting a promise; and
10. schedule re-review.

---

# Short recap

```text
1. Governance is sustained behavior, not one-time acknowledgment.
2. Routine decisions are where drift accumulates.
3. Audit actual and planned usage against current policy.
4. A policy requirement should map to observable practice and evidence.
5. A Diligence gap is the difference between required and observed behavior.
6. Diagnose root cause rather than blaming the user by default.
7. Prefer workflow and technical repairs over reminders alone.
8. Record exceptions with authority, scope, controls, and expiration.
9. Re-evaluate when policies, features, data, or workflows change.
10. A gap is closed only after corrective action is verified.
```

## Educational-use notice

This lesson is an unofficial educational resource. Organizational policy, law, contracts, product behavior, and regulatory requirements can change. Use current approved guidance and qualified legal, privacy, security, compliance, records, employment, and ethics review for real decisions.