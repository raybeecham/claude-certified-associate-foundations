# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — teaching and quiz are complete. Key Takeaways and Module Complete remain open.

## Module thesis

> Governance is a practitioner skill: classify the use case, feature, data, policy, and ethical impact before deployment; preserve accountable human authority; audit real behavior; and monitor outcomes over time.

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
Ethical-impact review
      ↓
Human approval, recourse, monitoring, and escalation
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
- [x] [06. Ethical Implications](lessons/06-ethical-implications.md)
- [ ] 07. Module 6 Quiz
  - [x] [Quiz — Full marks, 5/5](lessons/07a-module-6-quiz.md)
  - [ ] Takeaways
- [ ] 08. Module Complete

---

# Completion record

```text
Module 6 teaching sections: Complete
Module 6 quiz:              Full marks — 5 of 5
Key takeaways:              Open
Module complete:            Open
```

---

# Integrated governance framework

## 1. Classify the use case

Screen the proposed use through four Delegation criteria:

| Criterion | Question |
|---|---|
| Reversibility | Can an incorrect result be caught and undone before harm? |
| Consequence of error | What happens if the result is wrong? |
| Human creativity or empathy | Does care, authenticity, judgment, or relationship ownership need to remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

Identify the **load-bearing criterion**—the factor that would move the use into another classification if it changed.

| Classification | Meaning |
|---|---|
| Fully appropriate | Reversible, low consequence, grounded, and not dependent on special human authority or empathy |
| Appropriate with human review | AI assistance is useful, but a qualified pre-use gate is required |
| Inappropriate | AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, or policy constraints |

A review gate must state **who** reviews, **what** they verify, and **when** review occurs before use or consequence.

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

## 2. Evaluate Skill and feature trust

```text
Skill scope
      ×
Session permissions
      =
Effective reach
```

Review:

1. **Source** — publisher, owner, version, distribution path, approval, and support.
2. **Reach** — files, connectors, tools, code, secrets, persistence, and external actions available in the actual session.
3. **Appropriateness** — whether capability and access are proportionate to the approved task.

```text
Internal
      ≠
Vetted
```

Choose **Enable**, **Escalate**, or **Decline** under the correct authority.

## 3. Classify data before entry

| Tier | Typical data | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

```text
Classify data
      ↓
Confirm approved environment
      ↓
Minimize or redact when valid
      ↓
Choose persistence and feature controls
```

Redaction is valid only when it lowers identification risk and preserves task validity.

```text
Feature control applied
      ≠
Data approved for processing
```

Incognito, Memory, retention, export, and sandboxing are bounded controls—not processing authorization.

## 4. Apply policy as a Diligence habit

```text
Written policy
      ↓
Observed practice
      ↓
Usage audit
      ↓
Diligence gap
      ↓
Containment and corrective action
      ↓
Verified closure and re-audit
```

A Diligence gap record should include:

- current controlling requirement and version;
- observed behavior and evidence;
- scope, frequency, risk, and affected parties;
- root cause;
- immediate containment;
- durable corrective action;
- owner and due date;
- closure test; and
- status.

```text
Contained
      ≠
Remediated
      ≠
Verified closed
```

Audits must remain proportionate and authorized.

```text
Audit authority
      ≠
Unlimited surveillance authority
```

## 5. Review ethical implications

```text
Accurate wording
      ≠
Fair treatment
      ≠
Ethical sufficiency
```

Review bias entry points across:

- prompts and assumptions;
- source selection and representation;
- labels, categories, criteria, and examples;
- generated tone, certainty, and omissions;
- human edits; and
- downstream decision rules.

A six-part ethical review asks:

1. Who is affected?
2. What harm or benefit could result?
3. What would fair treatment require?
4. What transparency or disclosure is appropriate?
5. Who retains human authority, explanation, correction, and recourse?
6. Can the team decide, or must it escalate?

```text
Structured reasoning completed
      ≠
Authority to decide
```

Escalate when scale, potential harm, vulnerable groups, disputed fairness standards, unclear disclosure obligations, or organizational standing exceed the team’s authority.

---

# Module 6 quiz result

```text
Full marks — 5 of 5
```

The original public-safe quiz demonstrated command of:

1. classifying consequential final decisions;
2. evaluating unknown executable Skills;
3. separating processing authorization from persistence controls;
4. diagnosing policy-to-practice Diligence gaps; and
5. identifying hidden bias in automated exclusions.

## Quiz shortcut

```text
Final consequential determination
→ retain authorized human ownership

Unknown executable Skill
→ inspect source, bundle, and effective reach

Confidential approved data with no ordinary persistence
→ Incognito may fit, subject to organizational retention

Policy and real use diverge
→ record and close a Diligence gap

Automated exclusions receive no human review
→ bias and fairness risk
```

## Quiz reasoning sequence

```text
Identify the governance concern
      ↓
Locate the controlling Module 6 concept
      ↓
Distinguish capability from authority and approval
      ↓
Name the human role, control, or escalation path
      ↓
Reject convenience and stronger-model distractors
```

---

# Integrated governance protocol

```text
1. Define the use case, users, affected parties, and accountable owner
2. Run reversibility, consequence, human-element, and accountability criteria
3. Identify the load-bearing criterion and human gate
4. Establish Skill or feature source, contents, reach, and proportionality
5. Define and classify the minimum required data
6. Confirm the approved environment and persistence controls
7. Identify the controlling policy and version
8. Translate policy into observable controls and evidence
9. Audit actual and planned use against policy
10. Record gaps, containment, root causes, corrective actions, and owners
11. Identify bias entry points and define fair treatment
12. Determine disclosure, human authority, explanation, and recourse
13. Test representative and edge cases
14. Escalate when scale, harm, standing, or policy requires it
15. Monitor outcomes and revisit after material change
16. Approve, constrain, redesign, defer, decline, or reject
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
- [Skill Trust and Feature-Level Risk](lessons/03-skill-trust-feature-level-risk.md)
- [Data Sensitivity, Privacy & Feature Controls](lessons/04-data-sensitivity-privacy-feature-controls.md)
- [Organizational Policies and Diligence](lessons/05-organizational-policies-diligence.md)
- [Ethical Implications](lessons/06-ethical-implications.md)
- [Module 6 Quiz](lessons/07a-module-6-quiz.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)
- [Organizational Policies and Diligence prompts](../../prompts/module-06/05-organizational-policies-diligence-prompts.md)
- [Ethical Implications prompts](../../prompts/module-06/06-ethical-implications-prompts.md)
- [Module 6 quiz and remediation prompts](../../prompts/module-06/07a-module-6-quiz-prompts.md)

## Engineering patterns

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)
- [Skill Trust and Feature-Risk Pattern](../../patterns/skill-trust-and-feature-risk-pattern.md)
- [Data Classification and Feature-Control Pattern](../../patterns/data-classification-and-feature-control-pattern.md)
- [Governance Diligence Gap Closure Pattern](../../patterns/governance-diligence-gap-closure-pattern.md)
- [Ethical Impact Review and Escalation Pattern](../../patterns/ethical-impact-review-and-escalation-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Final unreviewed consequential decision → inappropriate for AI ownership
Unknown Skill with broad reach          → inspect and escalate
Incognito                               → persistence control, not authorization
Approved path is too difficult          → systemic Diligence gap
People filtered before human review     → bias and unfair-exclusion risk
Stronger model suggested                → check whether governance is the real defect
```

For Module 6 scenarios:

1. identify the affected people and consequence;
2. classify the use case before selecting the model;
3. inspect feature source and effective reach;
4. classify data before choosing controls;
5. apply the current policy rather than remembered guidance;
6. distinguish containment from verified closure;
7. identify the most direct ethical concern;
8. preserve accountable human authority and recourse;
9. escalate beyond the team’s standing; and
10. document a defensible rationale.

---

# Completion criteria

- [x] I completed all Module 6 teaching sections.
- [x] I completed the Module 6 quiz with full marks, 5/5.
- [ ] I completed the Module 6 takeaways.
- [ ] I can classify appropriate, human-reviewed, and inappropriate uses.
- [ ] I can identify the load-bearing criterion and define an operational gate.
- [ ] I can evaluate Skill source, contents, effective reach, and proportionality.
- [ ] I can classify data and separate processing authorization from persistence controls.
- [ ] I can translate policy into observable controls and run a bounded audit.
- [ ] I can distinguish containment, remediation, and verified closure.
- [ ] I can identify bias entry points and define a task-specific fairness standard.
- [ ] I can determine disclosure, explanation, correction, and recourse requirements.
- [ ] I can preserve human accountability and escalate beyond my authority.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance or ethics reviews, internal policies, regulated records, private employee or applicant data, proprietary Skill bundles, credentials, incident details, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute ethics, privacy, legal, regulatory, security, compliance, employment, public-benefits, medical, financial, records-management, or operational advice.

## Source note

The Module 6 quiz material was supplied on August 3, 2026. The repository records the learner’s reported result of full marks, 5/5, while using original public-safe scenarios rather than reproducing proprietary quiz wording.
