# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** Complete — all teaching sections, quiz, Key Takeaways, and the Module Complete checkpoint are finished. Module 7: Troubleshooting is up next.

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
- [x] 07. Module 6 Quiz
  - [x] [Quiz — Full marks, 5/5](lessons/07a-module-6-quiz.md)
  - [x] [Key Takeaways](lessons/07b-key-takeaways.md)
- [x] [08. Module Complete](lessons/08-module-complete.md)

---

# Completion record

```text
Course checkpoint:          1 of 1 passed
Module 6 teaching sections: Complete
Module 6 quiz:              Full marks — 5 of 5
Key takeaways:              Complete
Module complete:            Complete
```

---

# Integrated governance framework

## 1. Governance is practitioner judgment

```text
Policy exists
      ≠
Policy applied
      ≠
Responsible outcome
```

- **Delegation** defines what Claude may prepare, what remains human-controlled, and what should not be delegated.
- **Diligence** requires ownership, verification, transparency where appropriate, evidence, monitoring, and escalation.

## 2. Classify the use case

Screen each use through:

| Criterion | Question |
|---|---|
| Reversibility | Can an incorrect result be caught and undone before harm? |
| Consequence of error | What happens if the result is wrong? |
| Human creativity or empathy | Must care, authenticity, judgment, or relationship ownership remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

Identify the **load-bearing criterion** and classify the use as:

```text
Fully appropriate
Appropriate with human review
Inappropriate for AI ownership
```

A human-review gate must define **who**, **what**, and **when** before use or consequence.

## 3. Treat a Skill as software

```text
Skill contents
      ×
Session permissions
      =
Effective reach
```

Review source, owner, version, distribution, instructions, scripts, dependencies, bundled files, data access, connectors, tools, external actions, persistence, least privilege, tests, monitoring, and rollback.

```text
Internal
      ≠
Vetted
```

Choose **Enable**, **Escalate**, or **Decline** under the correct authority.

## 4. Classify data before entry

| Tier | Typical data | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and approved environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

```text
Classify
      ↓
Confirm processing approval
      ↓
Minimize or redact
      ↓
Select feature controls
```

Redaction is valid only when it reduces identification risk and preserves task validity.

```text
Incognito / Memory / sandboxing
      ≠
Permission to process disallowed data
```

## 5. Apply policy as a Diligence habit

```text
Written policy
      ↓
Observed practice
      ↓
Diligence gap
      ↓
Containment
      ↓
Root-cause repair
      ↓
Verified closure and re-audit
```

Translate policy into observable behavior, controls, evidence, ownership, review cadence, and escalation. Bound audits to authorized and necessary evidence.

```text
Contained
      ≠
Remediated
      ≠
Verified closed
```

## 6. Review ethical implications

```text
Accurate wording
      ≠
Fair treatment
      ≠
Ethical sufficiency
```

Review:

- affected parties;
- prompt framing, sources, labels, criteria, examples, and downstream use;
- possible harms and benefits;
- task-specific fairness;
- disclosure and transparency;
- accountable human authority;
- explanation, correction, and recourse; and
- escalation when scale, harm, or standing exceeds the team’s authority.

```text
Structured reasoning completed
      ≠
Authority to decide
```

---

# Module 6 quiz result

```text
Full marks — 5 of 5
```

The original public-safe quiz demonstrated command of:

1. consequential use-case classification;
2. Skill source and effective-reach review;
3. processing authorization versus persistence controls;
4. policy-to-practice Diligence gaps; and
5. hidden bias in automated exclusions.

---

# Five durable takeaways

```text
1. Governance is a practitioner skill.
2. Screen use cases with Delegation criteria.
3. Treat a Skill as software.
4. Classify data before it enters a feature.
5. Review ordinary outputs for bias, fairness, and transparency.
```

---

# Associate path

| Module | Capability | Status |
|---|---|---|
| M1 — Product & Model Selection | Choose the right entry point, model, and features | Complete |
| M2 — Prompting | Build structured prompts and adapt them to the task | Complete |
| M3 — Output Evaluation | Validate output and identify mandatory human review | Complete |
| M4 — Workflow Integration | Map responsibilities and redesign workflows safely | Complete |
| M5 — Configuration | Configure and maintain Projects, instructions, and knowledge | Complete |
| **M6 — Governance** | Apply use-case, data, policy, and ethics judgment responsibly | **Complete** |
| **M7 — Troubleshooting** | Diagnose underperformance and optimize workflows | **Up next** |
| M8 — Course Summary & Next Steps | Consolidate learning and prepare for the exam | Final synthesis |

---

# Transition to Module 7

```text
Governed use case
      ↓
Observed underperformance
      ↓
Failure classification and localization
      ↓
Targeted intervention
      ↓
Verification and optimization
```

Module 6 asked whether a use should proceed and under which boundaries. Module 7 asks why an approved workflow is underperforming and what the smallest responsible repair is.

Governance remains active during troubleshooting. Performance improvements must not bypass data, permission, fairness, review, recourse, or accountability controls.

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
- [Module 6 Key Takeaways](lessons/07b-key-takeaways.md)
- [Module 6 Complete](lessons/08-module-complete.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)
- [Organizational Policies and Diligence prompts](../../prompts/module-06/05-organizational-policies-diligence-prompts.md)
- [Ethical Implications prompts](../../prompts/module-06/06-ethical-implications-prompts.md)
- [Module 6 quiz and remediation prompts](../../prompts/module-06/07a-module-6-quiz-prompts.md)
- [Module 6 Key Takeaways prompts](../../prompts/module-06/07b-key-takeaways-prompts.md)
- [Module 6 completion and transition prompts](../../prompts/module-06/08-module-complete-prompts.md)

## Engineering patterns

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)
- [Skill Trust and Feature-Risk Pattern](../../patterns/skill-trust-and-feature-risk-pattern.md)
- [Data Classification and Feature-Control Pattern](../../patterns/data-classification-and-feature-control-pattern.md)
- [Governance Diligence Gap Closure Pattern](../../patterns/governance-diligence-gap-closure-pattern.md)
- [Ethical Impact Review and Escalation Pattern](../../patterns/ethical-impact-review-and-escalation-pattern.md)

## Extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Completion criteria

- [x] I completed all Module 6 teaching sections.
- [x] I completed the Module 6 quiz with full marks, 5/5.
- [x] I completed the Module 6 takeaways.
- [x] I completed the Module 6 checkpoint, 1/1.
- [x] I can classify appropriate, human-reviewed, and inappropriate uses.
- [x] I can identify the load-bearing criterion and define an operational gate.
- [x] I can evaluate Skill source, contents, effective reach, and proportionality.
- [x] I can classify data and separate processing authorization from persistence controls.
- [x] I can translate policy into observable controls and run a bounded audit.
- [x] I can distinguish containment, remediation, and verified closure.
- [x] I can identify bias entry points and define a task-specific fairness standard.
- [x] I can determine disclosure, explanation, correction, and recourse requirements.
- [x] I can preserve human accountability and escalate beyond my authority.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance or ethics reviews, internal policies, regulated records, private employee or applicant data, proprietary Skill bundles, credentials, incident details, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute ethics, privacy, legal, regulatory, security, compliance, employment, medical, financial, procurement, records-management, audit, or operational advice.
