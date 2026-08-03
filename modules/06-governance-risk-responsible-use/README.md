# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — all Module 6 teaching sections are complete. Quiz, takeaways, and Module Complete remain open.

## Module thesis

> Governance is a practitioner skill: classify the use case, feature, data, policy, and ethical impact before deployment; preserve accountable human authority; audit actual behavior; and monitor the decision over time.

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
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 08. Module Complete

No later section is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Governance as practitioner judgment

Governance appears in routine decisions about use cases, uploads, Skills, connectors, permissions, review gates, affected people, and escalation.

```text
Policy exists
      ≠
Decision is automatic
```

Diligence verifies ownership, evidence, current policy, approval, monitoring, and escalation. Delegation defines what Claude may prepare, what remains human-controlled, and what should not be delegated.

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

Identify the **load-bearing criterion**—the factor that would move the use into a different classification if it changed.

| Classification | Meaning |
|---|---|
| Fully appropriate | Reversible, low consequence, grounded, and not dependent on special human authority or empathy |
| Appropriate with human review | AI assistance is useful, but a qualified pre-use gate is required |
| Inappropriate | AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, or policy constraints |

A human gate must state **who** reviews, **what** they verify, and **when** review occurs before use or consequence.

```text
Human in the loop
      ≠
Operational human gate
```

---

# Foundation 3: Skill trust and feature-level risk

A Skill is a software-like package containing instructions, scripts, dependencies, and resources. Its risk depends on the environment in which it runs.

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

Choose **Enable**, **Escalate**, or **Decline** under the correct authority.

---

# Foundation 4: Data sensitivity, privacy, and feature controls

Classify data before it enters a chat, Project, upload, connector, Memory, Skill, or code-execution workflow.

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

| Tier | Typical data | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

```text
Feature control applied
      ≠
Data approved for processing
```

Redaction is valid only when it lowers identification risk **and** preserves the task’s validity. Incognito, Memory, retention, export, and sandboxing are bounded controls rather than processing authorization.

---

# Foundation 5: Organizational policies and Diligence

Governance fails when written policy and observed practice drift apart.

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

Audits must also respect privacy and authority boundaries.

```text
Audit authority
      ≠
Unlimited surveillance authority
```

Exceptions require scope, duration, compensating controls, approving authority, monitoring, expiration, and renewal or closure decisions.

---

# Foundation 6: Ethical implications

Ethical risk can hide in routine outputs such as summaries, recommendations, evaluations, and audience-specific communications.

```text
Accurate wording
      ≠
Fair treatment
      ≠
Ethical sufficiency
```

## Bias entry points

Review:

- prompt framing and assumptions;
- source selection and representation;
- labels, categories, and evaluation criteria;
- examples and evidence standards;
- generated wording, tone, certainty, and omissions;
- human edits; and
- downstream decision rules.

```text
Neutral-looking output
      ≠
Neutral process
```

## Fairness review

Ask:

- Who is affected?
- Which opportunities, burdens, treatment, or reputation may change?
- Are relevantly similar cases treated consistently?
- Are material differences justified by the task?
- Are protected or proxy characteristics influencing results?
- Are evidence and certainty standards consistent?
- Can affected people receive explanation, correction, or appeal?

```text
Same process for everyone
      ≠
Fair outcome by default
```

## Transparency and disclosure

Disclosure depends on:

- organizational policy;
- audience expectations;
- professional or contractual obligations;
- materiality of AI assistance;
- risk of misleading authorship or expertise claims;
- human review performed; and
- consequence of concealment.

```text
No explicit disclosure rule found
      ≠
Concealment automatically appropriate
```

## Six-part ethical review

1. **Affected parties** — Who may benefit, be burdened, or be excluded?
2. **Potential harm** — What could go wrong, and how severe or reversible is it?
3. **Fair outcome** — What would justified and consistent treatment look like?
4. **Transparency** — What should subjects, users, or recipients know?
5. **Human authority and recourse** — Who reviews, intervenes, explains, or hears appeals?
6. **Decision and escalation** — Can the team decide, or is specialist review required?

```text
Name affected parties
      ↓
Describe possible harm
      ↓
Define fair treatment
      ↓
Determine disclosure
      ↓
Define review and recourse
      ↓
Decide or escalate
```

## Escalation threshold

Escalate when:

- the affected population is large;
- harm could be severe or difficult to reverse;
- vulnerable or protected groups may be affected;
- fairness criteria are contested;
- the team lacks expertise or organizational standing;
- surveillance, manipulation, or power imbalance is present;
- disclosure obligations are materially unclear;
- no meaningful recourse exists; or
- policy assigns the decision elsewhere.

```text
Structured reasoning completed
      ≠
Authority to decide
```

---

# Worked ethical case: performance-review summaries

A manager uses Claude to draft employee performance-review summaries from the manager’s notes.

## Ethical risks

- unequal tone across employees;
- inconsistent evidence standards;
- unsupported personality or motivation claims;
- amplification of subjective notes;
- different certainty levels;
- concealment of AI assistance where disclosure is required; and
- weak explanation or appeal paths.

## Required gate

- **Who:** Accountable manager, with HR or another qualified reviewer where required.
- **What:** Factual support, consistency, bias, tone, policy compliance, and unsupported inference.
- **When:** Before the review is finalized, shared, or used for compensation or promotion.

## Classification

```text
Appropriate with human review
+ fairness check
+ manager accountability
+ disclosure according to policy and context
```

The reasoning and gate make the decision defensible—not the verdict alone.

---

# Integrated governance protocol

```text
1. Define the use case, users, affected parties, and accountable owner
2. Run reversibility, consequence, human-element, and accountability criteria
3. Identify the load-bearing criterion and human gate
4. Establish Skill or feature source, contents, reach, and proportionality
5. Define and classify the minimum required data
6. Confirm the approved environment and feature controls
7. Identify the controlling policy and version
8. Translate policy into observable controls and evidence
9. Audit actual and planned use against policy
10. Record gaps, containment, root causes, corrective actions, and owners
11. Identify bias entry points and define fair treatment
12. Determine disclosure, human authority, explanation, and recourse
13. Test representative and edge cases
14. Escalate when scale, harm, standing, or policy requires it
15. Monitor actual outcomes and revisit after material change
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

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)
- [Organizational Policies and Diligence prompts](../../prompts/module-06/05-organizational-policies-diligence-prompts.md)
- [Ethical Implications prompts](../../prompts/module-06/06-ethical-implications-prompts.md)

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
People-facing output                       → review bias, fairness, and transparency
Biased prompt or evidence                  → correct upstream framing
Same process but unequal effects           → fairness risk remains
Disclosure requirement unclear             → seek guidance or disclose rather than conceal
Reviewer lacks standing                    → escalate
Large affected population                  → stronger testing and governance review
No appeal or correction path               → add recourse or redesign
Policy-compliant but unfair                 → ethics review still required
```

For ethical-implication scenarios:

1. identify who is affected;
2. inspect prompt, sources, criteria, and generated language;
3. assess stakes and distribution of harm;
4. define a justified fairness standard;
5. determine disclosure expectations;
6. preserve accountable human ownership;
7. provide explanation, correction, and appeal paths;
8. document the reasoning;
9. escalate beyond the team’s standing; and
10. monitor actual outcomes.

---

# Completion criteria

- [x] I completed all Module 6 teaching sections.
- [ ] I can assess reversibility, consequence, human element, and accountability.
- [ ] I can identify the load-bearing criterion and define an operational gate.
- [ ] I can distinguish source trust, effective reach, and feature appropriateness.
- [ ] I can classify data and apply valid minimization and feature controls.
- [ ] I can translate policy into observable behavior and run a bounded usage audit.
- [ ] I can distinguish containment, remediation, and verified closure.
- [ ] I can identify bias in prompts, sources, criteria, language, and workflow design.
- [ ] I can define a task-specific fairness standard.
- [ ] I can determine appropriate AI-use disclosure.
- [ ] I can preserve meaningful human authority, explanation, correction, and recourse.
- [ ] I can escalate when harm, scale, standing, or policy exceeds individual judgment.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance or ethics reviews, private employee or applicant records, protected-characteristic data, regulated records, credentials, organization-only escalation records, client identities, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute ethics, privacy, legal, regulatory, security, compliance, employment, human-resources, medical, financial, records-management, or operational advice.

## Source note

The Ethical Implications course material was supplied on August 3, 2026. Current organizational policy, law, contracts, professional obligations, qualified human judgment, and authorized governance or ethics review control real decisions.