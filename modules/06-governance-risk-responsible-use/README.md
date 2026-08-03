# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — Module 6 is the active module.

## Module thesis

> Governance is a practitioner skill: classify the use case, feature, data, policy, and ethical impact before deployment; retain accountable human authority; audit actual behavior; and monitor the decision over time.

```text
Proposed use case
      ↓
Appropriateness classification
      ↓
Skill and feature trust review
      ↓
Data classification and feature controls
      ↓
Policy application and Diligence audit
      ↓
Ethical review
      ↓
Human approval, monitoring, and escalation
      ↓
Approve / constrain / redesign / defer / reject
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
- [x] [03. Skill Trust & Feature-Level Risk](lessons/03-skill-trust-feature-level-risk.md)
- [x] [04. Data Sensitivity, Privacy & Feature Controls](lessons/04-data-sensitivity-privacy-feature-controls.md)
- [x] [05. Organizational Policies & Diligence](lessons/05-organizational-policies-diligence.md)
- [ ] 06. Ethical Implications
- [ ] 07. Module 6 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 08. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Governance as practitioner judgment

Governance appears in daily choices about use cases, uploads, Skills, connectors, permissions, review gates, affected people, and escalation.

```text
Policy exists
      ≠
Decision is automatic
```

Diligence verifies ownership, evidence, policy, approvals, monitoring, and escalation. Delegation defines what Claude may prepare, what remains human-controlled, and what should not be delegated.

```text
Diligence = ownership + verification + documented judgment
```

---

# Foundation 2: Appropriate versus inappropriate use cases

Screen each use through four Delegation criteria:

| Criterion | Core question |
|---|---|
| Reversibility | Can an incorrect output be caught and undone before harm? |
| Consequence of error | What is the cost if the output is wrong? |
| Human creativity or empathy | Does judgment, care, authenticity, or relationship ownership need to remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

```text
Claude can produce output
      ≠
Claude should own the task
      ≠
Organization may use it without controls
```

Identify the **load-bearing criterion**—the criterion that would move the classification if it changed.

## Three classifications

| Classification | Meaning |
|---|---|
| Fully appropriate | Reversible, low consequence, grounded, and not dependent on special human authority or empathy |
| Appropriate with human review | AI assistance is useful, but a qualified pre-use gate is required |
| Inappropriate | AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, or policy constraints |

A human-review gate must state **who** reviews, **what** they verify, and **when** review occurs before use or consequence.

---

# Foundation 3: Skill trust and feature-level risk

A Skill is a software-like package containing instructions, scripts, dependencies, and resources. Its practical risk depends on the environment in which it runs.

```text
Skill scope
      ×
Session permissions
      =
Effective reach
```

Review:

1. **Source** — publisher, owner, version, distribution, approval, and support.
2. **Reach** — files, connectors, tools, code, secrets, persistence, and external actions available in the actual session.
3. **Appropriateness** — whether the capability and access are proportionate to the approved task.

```text
Internal
      ≠
Vetted
```

```text
Useful capability
      ≠
Necessary capability
      ≠
Proportionate capability
```

Choose **Enable**, **Escalate**, or **Decline** under the correct authority.

---

# Foundation 4: Data sensitivity, privacy, and feature controls

Classify data before it enters a chat, Project, file upload, connector, Memory, Skill, or code-execution workflow.

```text
Classify data
      ↓
Confirm approved processing environment
      ↓
Minimize or redact when valid
      ↓
Choose feature and persistence controls
      ↓
Review, delete, monitor, or escalate
```

## Rapid three-tier screen

| Tier | Typical data | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

```text
Uncertain classification
      ↓
Use the more sensitive tier
      ↓
Seek authorized clarification
```

Redaction is valid only when it reduces identification risk **and** preserves the task’s validity.

```text
Name removed
      ≠
Person de-identified
```

Incognito, Memory, and sandboxing are bounded controls.

```text
Feature control applied
      ≠
Data approved for processing
```

Processing permission must be resolved before persistence, history, export, or deletion controls are selected.

---

# Foundation 5: Organizational policies and Diligence

A policy that is followed only during visible reviews is not operational governance.

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

## Apply governance consistently

Routine decisions are where governance drift accumulates:

- uploading an internal draft;
- enabling a convenient Skill;
- connecting a new source;
- skipping a human gate under deadline pressure;
- retaining an expired exception;
- using an old policy reference; or
- assuming that an internal capability is already vetted.

```text
Repeated exception
      ↓
Unrecorded norm
      ↓
Governance drift
```

## Translate policy into observable controls

| Policy requirement | Observable practice | Evidence |
|---|---|---|
| Use approved entry points | Sensitive work occurs only in approved environments | Account, product, or access record |
| Classify data before use | Data tier recorded before upload or retrieval | Intake or decision record |
| Vet executable Skills | Source, contents, reach, and approval reviewed | Skill trust register |
| Require human approval | Qualified reviewer acts before consequence | Approval record |
| Apply least privilege | Connector and tool access is narrowly scoped | Permission inventory |
| Maintain configurations | Instructions, sources, Skills, connectors, and Memory are reviewed | Maintenance record |
| Record exceptions | Exception has authority, scope, controls, and expiration | Exception register |

```text
Policy acknowledged
      ≠
Policy operationalized
```

## Audit usage against policy

A usage audit should define:

- review period;
- policy version;
- teams, Projects, or workflows included;
- approved products and entry points;
- applicable data classes;
- Skills, connectors, and external actions;
- required human gates;
- exception records;
- authorized evidence sources;
- sample method; and
- accountable audit owner.

Audits must also respect privacy, access, and monitoring policy.

```text
Audit authority
      ≠
Unlimited surveillance authority
```

## Diligence gaps

A Diligence gap is the difference between required and observed behavior.

Examples include:

- unapproved data or entry-point use;
- unvetted Skills;
- excessive connector permissions;
- skipped review gates;
- stale policy language in Projects or procedures;
- missing approval evidence;
- expired exceptions; and
- high-impact uses without monitoring.

A gap record should include:

- controlling requirement;
- observed practice;
- evidence;
- scope and frequency;
- affected risk;
- root cause;
- immediate containment;
- corrective action;
- owner and due date;
- closure test; and
- status.

```text
Gap identified
      ≠
Gap closed
```

Closure requires evidence that the practice changed.

## Containment versus correction

Immediate containment limits current exposure.

Sustainable correction prevents recurrence.

```text
Contained
      ≠
Remediated
      ≠
Verified closed
```

Root causes may include unclear policy, inconvenient approved paths, overbroad permissions, outdated configuration, unstaffed gates, deadline pressure, unclear ownership, or untracked exceptions.

Prefer durable repairs:

```text
Clarify policy and ownership
      ↓
Repair workflow and configuration
      ↓
Narrow technical access
      ↓
Add approval and evidence requirements
      ↓
Train affected users
      ↓
Monitor and re-audit
```

Training alone does not repair a broken or bypassable workflow.

## Exception management

An exception should record:

- controlling requirement;
- reason;
- scope and duration;
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

## Stay current

Review after:

- policy revision;
- product or feature changes;
- Skill or connector updates;
- data-classification changes;
- role or ownership changes;
- incidents or near misses;
- exception expiration; or
- growth from prototype to operational dependency.

```text
Previously approved
      ≠
Permanently approved
```

---

# Worked usage-audit example

A fictional monthly audit finds three gaps.

| Gap | Immediate action | Durable repair |
|---|---|---|
| Unreleased product specification used in a non-approved entry point | Remove or contain the material and notify the owner | Clarify classification and approved-path guidance in the Project setup |
| Skill enabled without trust review | Disable or restrict pending review | Require source, bundle, reach, testing, and approval records |
| Client-report review gate skipped twice | Pause release until qualified review occurs | Add backup reviewer, technical release gate, and urgent escalation path |

```text
Invisible drift
      ↓
Audited evidence
      ↓
Owned corrective actions
      ↓
Verified closure
```

The objective is not to assume malicious intent. It is to repair the conditions that allowed the deviation.

---

# Integrated governance protocol

```text
1. Define the use case, users, affected parties, and owner
2. Run reversibility, consequence, human-element, and accountability criteria
3. Identify the load-bearing criterion and human gate
4. Establish Skill or feature source, contents, reach, and proportionality
5. Define and classify the minimum required data
6. Confirm the approved environment and feature controls
7. Identify the controlling policy and version
8. Translate policy into observable controls and evidence
9. Audit actual and planned use against policy
10. Record gaps, containment, root causes, corrective actions, and owners
11. Manage exceptions and verify closure
12. Re-audit after material change
13. Assess ethical impact, monitoring, escalation, and incident response
14. Approve, constrain, redesign, defer, decline, or reject
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
- [Skill Trust and Feature-Level Risk](lessons/03-skill-trust-feature-level-risk.md)
- [Data Sensitivity, Privacy & Feature Controls](lessons/04-data-sensitivity-privacy-feature-controls.md)
- [Organizational Policies and Diligence](lessons/05-organizational-policies-diligence.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)
- [Organizational Policies and Diligence prompts](../../prompts/module-06/05-organizational-policies-diligence-prompts.md)

## Engineering patterns

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)
- [Skill Trust and Feature-Risk Pattern](../../patterns/skill-trust-and-feature-risk-pattern.md)
- [Data Classification and Feature-Control Pattern](../../patterns/data-classification-and-feature-control-pattern.md)
- [Governance Diligence Gap Closure Pattern](../../patterns/governance-diligence-gap-closure-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Policy acknowledged once                 → insufficient; apply continuously
Routine low-visibility deviation         → Diligence gap
Observed practice differs from policy    → record and remediate
Gap lacks owner or closure evidence      → not closed
Repeated bypass under deadline pressure  → repair workflow and approval control
Internal Skill assumed safe              → require trust review
Old practice after policy change         → re-evaluate
No current policy located                → pause or seek authorized clarification
Audit collects excessive personal data   → narrow the audit
Expired exception remains active         → close, renew, narrow, or escalate
```

For policy-and-Diligence scenarios:

1. identify the controlling policy and version;
2. translate it into observable practice and evidence;
3. compare actual or planned use with the requirement;
4. distinguish isolated error from systemic drift;
5. identify root cause;
6. separate containment from remediation;
7. assign owner, due date, and closure test;
8. manage exceptions explicitly;
9. verify closure; and
10. schedule re-audit.

---

# Completion criteria

- [x] I completed the Module 6 introduction.
- [x] I completed Appropriate vs Inappropriate Use Cases.
- [x] I completed Skill Trust and Feature-Level Risk.
- [x] I completed Data Sensitivity, Privacy & Feature Controls.
- [x] I completed Organizational Policies and Diligence.
- [ ] I can assess reversibility, consequence, human element, and accountability.
- [ ] I can identify the load-bearing criterion and define an operational gate.
- [ ] I can distinguish source trust, effective reach, and feature appropriateness.
- [ ] I can classify data and apply valid minimization and feature controls.
- [ ] I can translate policy requirements into observable behavior and evidence.
- [ ] I can run a bounded usage audit.
- [ ] I can record a Diligence gap and distinguish containment from correction.
- [ ] I can manage exceptions and verify closure.
- [ ] I can identify ethical implications beyond compliance.
- [ ] I can define meaningful oversight and incident response.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential policies, internal audit findings, regulated records, credentials, private personnel information, organization-only exception records, client identities, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute privacy, legal, regulatory, security, compliance, audit, employment, ethics, records-management, or operational advice.

## Source note

The Organizational Policies and Diligence course material was supplied on August 3, 2026. Current organizational policy, law, contracts, approved product settings, and authorized governance decisions control real use.
