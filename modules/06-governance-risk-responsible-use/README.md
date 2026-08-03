# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — Module 6 is the active module.

## Module thesis

> Governance is a practitioner skill: decide whether a use case should proceed, what data and feature boundaries apply, who remains accountable, and how policy, ethics, monitoring, and escalation govern the work.

```text
Proposed use case
      ↓
Practitioner judgment
      ↓
Delegation and Diligence
      ↓
Data, feature, policy, and ethical review
      ↓
Human approval, monitoring, and escalation
      ↓
Approve / constrain / redesign / defer / reject
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [ ] 02. Appropriate vs Inappropriate Use Cases
- [ ] 03. Skill Trust & Feature-Level Risk
- [ ] 04. Data Sensitivity, Privacy & Feature Controls
- [ ] 05. Organizational Policies & Diligence
- [ ] 06. Ethical Implications
- [ ] 07. Module 6 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 08. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Module 5 to Module 6 bridge

Module 5 established how to configure and maintain a reliable operating environment.

Module 6 asks whether that capability should be used for a particular purpose and under what conditions.

```text
Configured capability
      ↓
Use-case suitability
      ↓
Data and feature boundaries
      ↓
Policy and ethical judgment
      ↓
Accountability, monitoring, and response
```

The transition question is:

> The environment is configured correctly—but is this use appropriate, are the data and controls sufficient, and who owns the consequences?

---

# Foundation 1: Governance as a practitioner skill

Governance is not only a policy document or a final approval meeting. It appears in daily decisions such as:

- whether confidential data may be uploaded;
- whether a third-party Skill may run code;
- whether a connector should have write access;
- whether Claude may influence a consequential decision;
- whether human review is meaningful;
- whether the workflow could create unfair effects; and
- whether uncertainty requires escalation.

```text
Policy exists
      ≠
Decision is automatic
```

Policy defines the formal boundary. Practitioners apply that boundary to the actual use case, data, feature, audience, and consequence.

A single inappropriate use can affect the wider AI program through incident response, loss of trust, restricted access, or a temporary adoption freeze.

---

# Foundation 2: Diligence and Delegation

## Diligence

Diligence concerns ownership and verification.

```text
Diligence
=
Ownership
+ verification
+ documented judgment
```

Ask:

- Who owns the decision?
- What evidence supports it?
- Which policy applies?
- Has the data classification been confirmed?
- Has the Skill, connector, or feature been vetted?
- Are approvals and exceptions recorded?
- Is monitoring defined?
- Where does escalation go?

## Delegation

Delegation determines whether the work should be assigned to Claude and what must remain human-controlled.

Assess:

- reversibility;
- stakes;
- accountability;
- required expertise;
- affected parties;
- transparency;
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

Diligence verifies the conditions. Delegation defines the responsibility boundary.

---

# Foundation 3: Appropriate versus inappropriate use

A technically possible use is not automatically appropriate.

```text
Model can perform task
      ≠
Organization should deploy task
```

Assess:

- intended outcome;
- affected people and decisions;
- stakes and reversibility;
- legal, policy, contractual, and professional constraints;
- data sensitivity;
- required expertise;
- transparency and disclosure;
- human authority;
- failure consequences; and
- appeal or correction paths.

Possible outcomes are:

| Outcome | Meaning |
|---|---|
| Approve | Conditions are satisfied |
| Approve with constraints | Proceed within explicit limits |
| Redesign | Change workflow, data, feature, or authority boundaries |
| Defer | Required evidence, policy, or approval is missing |
| Reject | The use is prohibited, unsuitable, or unjustifiably risky |

---

# Foundation 4: Skill trust and feature-level risk

Features should be evaluated by what they can access, execute, persist, or change.

Review:

- publisher and provenance;
- instructions, scripts, and dependencies;
- code execution;
- connector and file access;
- external actions;
- update and distribution behavior;
- retention and logging;
- prompt-injection exposure;
- approval boundaries; and
- disable or rollback paths.

```text
Feature available
      ≠
Feature approved
      ≠
Feature trusted for this use case
```

Trust must be evaluated in the current context rather than inherited from convenience or prior use.

---

# Foundation 5: Data sensitivity, privacy, and controls

Classify data before choosing an environment or feature.

Consider:

- public, internal, confidential, restricted, regulated, or controlled data;
- personal information;
- client and third-party restrictions;
- intellectual property;
- credentials and secrets;
- geographic or residency constraints;
- retention and deletion;
- connector and sharing permissions;
- Memory and persistence;
- logging and export; and
- incident response.

```text
Data accessible
      ≠
Data approved for processing
```

Apply minimization and least privilege. Use only the data, access, retention, and features required for the approved purpose.

---

# Foundation 6: Organizational policy and Diligence

Responsible operation requires current organizational guidance rather than assumptions.

Diligence may require:

- reviewing acceptable-use and AI policies;
- confirming approved products and plans;
- checking data-classification requirements;
- identifying security, privacy, legal, compliance, records, or ethics review;
- documenting exceptions;
- retaining approvals;
- assigning accountable owners; and
- defining incident and escalation paths.

```text
No policy found
      ≠
Use automatically permitted
```

When policy is unclear, pause or narrow the use and seek authorized clarification.

---

# Foundation 7: Ethical implications

Ethical review extends beyond formal compliance.

Examine:

- fairness and disparate impact;
- representation and bias;
- autonomy and consent;
- transparency and deception;
- surveillance and power imbalance;
- accessibility;
- recourse and correction;
- labor and role impacts;
- misuse potential; and
- distribution of benefits and harms.

```text
Policy-compliant
      ≠
Ethically sufficient
```

Ethical uncertainty should be surfaced rather than hidden behind technical feasibility or business value.

---

# Foundation 8: Meaningful oversight and security

A nominal human-in-the-loop is insufficient when the reviewer lacks:

- expertise;
- evidence access;
- time;
- review criteria;
- intervention authority;
- independence; or
- escalation.

```text
Human review mentioned
      ≠
Human oversight operational
```

Threat-model:

- prompt injection;
- malicious or untrusted Skills;
- data exfiltration;
- overbroad connector permissions;
- unauthorized external actions;
- stale dependencies;
- supply-chain risk;
- unsafe automation; and
- sensitive logging.

Use layered controls:

```text
Policy
+ least privilege
+ source and input validation
+ tool restrictions
+ deterministic checks
+ human approval
+ logging and monitoring
+ incident response
```

No single prompt or instruction can provide these protections by itself.

---

# Governance decision protocol

```text
1. Define the proposed use, users, and affected parties
2. Assess stakes, reversibility, and accountability
3. Check prohibited, restricted, and unsuitable uses
4. Classify data and confirm the processing environment
5. Review Skills, connectors, tools, Memory, and feature risk
6. Apply minimization and least privilege
7. Review policy and required approvals
8. Assess fairness, consent, transparency, accessibility, and recourse
9. Define meaningful human oversight
10. Threat-model misuse, injection, exfiltration, and unauthorized action
11. Establish monitoring, escalation, and incident response
12. Approve, constrain, redesign, defer, or reject
```

---

# Worked introduction example

A team wants to install a third-party Skill that summarizes sensitive internal reports.

A weak review asks only whether the summaries look useful.

A governance review asks:

- who published the Skill;
- what code and dependencies it contains;
- which data it can access;
- whether the environment is approved;
- whether it calls external systems;
- what is retained or logged;
- who reviews the result;
- how it can be disabled; and
- which approval is required.

Possible disposition:

```text
Defer for sensitive reports.
Inspect the Skill, restrict access,
validate the environment, and obtain approval.
```

The issue is not only whether Claude can summarize. It is whether this Skill, data, environment, and control set are appropriate together.

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)

## Existing extended practice

- [notes.md](notes.md): Governance, data, risk, oversight, and responsible-use concepts
- [lab.md](lab.md): Applied threat-model and governance exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

---

# Exam lens

```text
Useful but high-impact use             → assess appropriateness and human authority
Sensitive data proposed for upload     → classify and verify environment
Untrusted Skill requests broad access  → inspect source, code, permissions, and effects
Policy is unclear                      → pause, narrow, or seek clarification
Reviewer lacks expertise or authority  → oversight is not meaningful
Use is compliant but potentially unfair → perform ethical-impact analysis
```

For introductory scenarios:

1. identify the decision and affected parties;
2. distinguish capability from appropriateness;
3. apply Delegation criteria;
4. apply Diligence through ownership and verification;
5. classify data and feature risk;
6. locate policy and approval authority;
7. evaluate ethical implications;
8. define meaningful oversight;
9. establish monitoring and escalation; and
10. choose approve, constrain, redesign, defer, or reject.

---

# Completion criteria

- [x] I completed the Module 6 introduction.
- [ ] I can explain governance as a practitioner skill.
- [ ] I can apply Diligence through ownership and verification.
- [ ] I can apply Delegation criteria to appropriateness decisions.
- [ ] I can distinguish capability, appropriateness, and approval.
- [ ] I can identify appropriate, constrained, restricted, unsuitable, and prohibited uses.
- [ ] I can evaluate Skill trust and feature-level risk.
- [ ] I can classify data and apply minimization and privacy controls.
- [ ] I can locate and apply organizational policy.
- [ ] I can identify ethical implications beyond compliance.
- [ ] I can define meaningful human oversight.
- [ ] I can identify injection, exfiltration, and unauthorized-action controls.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance reviews, internal policies, restricted data, private incident reports, client identities, credentials, connector identifiers, proprietary risk assessments, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, privacy, security, compliance, ethics, employment, medical, financial, records-management, or operational advice.

## Source note

The Module 6 introduction was supplied on August 3, 2026. Product behavior, policies, and terms can change. Current official documentation and organizational policy control if they conflict with course or repository material.
