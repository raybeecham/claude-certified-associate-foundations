# Lesson 1: Module Introduction

## Overview

Governance is not a policy binder that sits outside the work. It is a practitioner skill exercised whenever someone decides whether a use case, data upload, Skill, connector, or workflow is appropriate.

```text
Proposed use
      ↓
Practitioner judgment
      ↓
Policy, data, feature, and ethical review
      ↓
Controls, approval, monitoring, or rejection
```

A single inappropriate use can create consequences far beyond one task. Sensitive data placed in the wrong environment, an untrusted Skill given broad access, or a policy violation at a critical moment can trigger incident response, loss of trust, or a broader pause in AI adoption.

> Governance keeps adoption moving by making responsible decisions repeatable before harm occurs.

---

# Plain-English explanation

Using Claude responsibly requires more than knowing how to prompt it.

A practitioner must decide:

- whether the use case is suitable;
- whether the data may be processed in the selected environment;
- whether the Skill, connector, or feature is sufficiently trusted;
- which organizational policies apply;
- what human judgment remains required;
- who could be affected;
- what ethical concerns remain; and
- whether the use should be approved, constrained, redesigned, deferred, or rejected.

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

---

# One analogy: a building inspector

A building inspector does not design every room or perform every construction task.

The inspector asks whether the structure, materials, access routes, and safeguards meet the conditions for safe use.

Governance works similarly:

- policy defines boundaries;
- technical controls reduce exposure;
- practitioners inspect the actual use;
- qualified owners approve or reject consequential decisions; and
- monitoring confirms that conditions remain valid after launch.

> Governance is where capability meets permission, accountability, and consequence.

---

# Governance as a practitioner skill

Policy establishes the formal boundary, but practitioners encounter the real decision in context.

Examples include:

- whether a confidential file may be uploaded;
- whether a third-party Skill may run code;
- whether a connector should receive write access;
- whether Claude may draft or influence a high-impact decision;
- whether a human reviewer has enough expertise and authority;
- whether an output could create unfair or misleading effects; and
- whether uncertainty requires escalation.

```text
Policy exists
      ≠
Decision is automatic
```

The practitioner must connect the policy to the actual data, feature, workflow, audience, and consequence.

---

# Two governing competencies

The supplied course frames Module 6 through two AI Fluency competencies.

## Diligence

Diligence concerns ownership and verification.

Ask:

- Who owns the decision?
- What evidence supports the judgment?
- Which policy or standard applies?
- Has the data classification been confirmed?
- Has the feature or Skill been vetted?
- Is the review meaningful rather than ceremonial?
- Are approvals and exceptions recorded?
- Is there monitoring and an escalation path?

```text
Diligence
=
Ownership
+ verification
+ documented judgment
```

## Delegation

Delegation supplies criteria for deciding whether the work should be assigned to Claude at all.

Assess:

- reversibility;
- stakes;
- accountability;
- required expertise;
- affected parties;
- transparency;
- human authority;
- external side effects; and
- failure consequences.

```text
Can Claude contribute?
      ↓
What may Claude prepare?
      ↓
What must remain human-controlled?
      ↓
What should not be delegated?
```

Diligence verifies the conditions. Delegation defines the boundary.

---

# Four learning goals

## 1. Identify appropriate and inappropriate use cases

Evaluate whether the proposed use is:

- appropriate;
- appropriate only with added constraints;
- high-impact and escalation-required;
- restricted;
- unsuitable; or
- prohibited.

Do not rely only on usefulness or technical feasibility.

## 2. Apply data sensitivity, privacy, and regulatory considerations

Before using data, determine:

- classification;
- ownership;
- permitted environment;
- minimum necessary data;
- retention and deletion requirements;
- sharing and connector scope;
- applicable privacy or regulatory obligations; and
- incident-response expectations.

```text
Data available
      ≠
Data approved for use
```

## 3. Follow organizational policy and governance standards

Responsible use requires current organizational guidance.

Confirm:

- approved products and plans;
- acceptable-use boundaries;
- required security, privacy, legal, compliance, records, or ethics review;
- exception authority;
- documentation requirements;
- monitoring duties; and
- escalation paths.

```text
No clear prohibition found
      ≠
Use automatically approved
```

## 4. Understand ethical implications

Ethical review extends beyond formal compliance.

Consider:

- fairness and disparate impact;
- bias and representation;
- autonomy and consent;
- transparency and deception;
- surveillance and power imbalance;
- accessibility;
- recourse and correction;
- labor and role impacts; and
- misuse potential.

```text
Policy-compliant
      ≠
Ethically sufficient
```

---

# The daily governance decision

A practical decision sequence is:

```text
1. Define the proposed use and affected people
2. Assess stakes, reversibility, and accountability
3. Check policy and prohibited-use boundaries
4. Classify data and confirm the processing environment
5. Vet Skills, connectors, tools, Memory, and feature access
6. Apply minimization and least privilege
7. Identify human review, approval, and appeal requirements
8. Assess fairness, consent, transparency, and misuse
9. Define monitoring, incident response, and escalation
10. Approve, constrain, redesign, defer, or reject
```

The strongest answer is not always `yes` or `no`. It may be a narrower use case with different data, fewer permissions, stronger review, or no external action.

---

# Governance decision outcomes

| Outcome | Meaning |
|---|---|
| Approve | Conditions are satisfied and controls are operational |
| Approve with constraints | Proceed only within explicit limits |
| Redesign | Change workflow, data, feature, or authority boundaries |
| Defer | Required evidence, policy, or approval is missing |
| Reject | The use is prohibited, unsuitable, or unjustifiably risky |

```text
Responsible judgment
      ≠
Automatic approval
      ≠
Automatic prohibition
```

---

# Worked example: an untrusted analysis Skill

A team wants to install a third-party Skill that summarizes sensitive internal reports.

A weak review asks:

```text
Does the Skill produce a useful summary?
```

A governance review asks:

- Who published it?
- What instructions, scripts, and dependencies does it contain?
- What data can it access?
- Does it execute code or call external systems?
- Is the processing environment approved for the reports?
- What is retained or logged?
- Who reviews the output?
- Can the Skill be disabled or rolled back?
- What policy approval is required?

Possible result:

```text
Do not enable for sensitive reports yet.
First inspect the Skill, restrict access,
validate the environment, and obtain approval.
```

The issue is not whether Claude can summarize. The issue is whether this Skill, data, environment, and control set are appropriate together.

---

# Common governance mistakes

## Policy-as-paperwork

Governance is treated as a document created after the system is built.

**Repair:** apply governance during use-case, data, feature, and workflow design.

## Capability equals permission

A feature can perform an action, so the team assumes it may.

**Repair:** verify policy, authorization, data, and accountability conditions.

## Nominal human review

A human is listed, but lacks expertise, evidence, time, or intervention authority.

**Repair:** define meaningful oversight with explicit criteria and decision rights.

## Convenience-based trust

A Skill or connector worked before, so it is trusted in a more sensitive context.

**Repair:** evaluate trust for the current use case, data, permissions, and consequences.

## Compliance-only ethics

The use satisfies policy, so broader stakeholder harms are ignored.

**Repair:** assess fairness, consent, transparency, accessibility, power, and recourse.

---

# Exam lens

```text
Useful use case with high stakes        → assess appropriateness and human authority
Sensitive data proposed for upload      → classify data and verify approved environment
Untrusted Skill requests broad access   → inspect source, code, permissions, and side effects
Policy is unclear                       → pause, narrow, or seek authorized clarification
Human reviewer lacks authority          → oversight is not meaningful
Use is compliant but potentially unfair → perform ethical-impact analysis
```

For introductory governance scenarios:

1. identify the decision and affected parties;
2. distinguish capability from appropriateness;
3. apply Delegation criteria;
4. apply Diligence through ownership and verification;
5. classify data and feature risk;
6. locate applicable policy and approval authority;
7. evaluate ethical implications;
8. define meaningful oversight;
9. establish monitoring and escalation; and
10. choose approve, constrain, redesign, defer, or reject.

---

# Short recap

```text
1. Governance is a practitioner skill.
2. One inappropriate use can affect an entire AI program.
3. Policy sets boundaries, but practitioners apply them in context.
4. Diligence means ownership and verification.
5. Delegation determines what Claude should and should not own.
6. Technical capability does not establish appropriateness.
7. Data, features, policy, and ethics must be assessed together.
8. Human review must be meaningful and operational.
9. Governance continues through monitoring and incident response.
10. Responsible outcomes include approve, constrain, redesign, defer, or reject.
```

## Educational-use notice

This lesson is an unofficial educational resource. It does not constitute legal, privacy, security, compliance, ethics, employment, medical, financial, records-management, or operational advice. Product behavior, terms, and policies can change; current official documentation and organizational policy control.
