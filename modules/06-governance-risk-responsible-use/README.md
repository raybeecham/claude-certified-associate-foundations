# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — teaching, quiz, and Key Takeaways are complete. Module Complete remains open.

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
- [ ] 08. Module Complete

---

# Completion record

```text
Module 6 teaching sections: Complete
Module 6 quiz:              Full marks — 5 of 5
Key takeaways:              Complete
Module complete:            Open
```

---

# Five durable takeaways

## 1. Governance is a practitioner skill

Governance is exercised through daily decisions about use cases, uploads, Skills, connectors, review gates, disclosure, accountability, and escalation.

```text
Policy exists
      ≠
Policy applied
      ≠
Responsible outcome
```

The AI Fluency Framework connects this work to:

- **Delegation:** deciding what work to do with AI, what remains human-controlled, and what should not be delegated; and
- **Diligence:** selecting systems thoughtfully, being transparent where required, verifying outputs, and taking responsibility for what is used or shared.

```text
Delegation → responsibility boundary
Diligence  → ownership and verification
```

## 2. Screen use cases with the Delegation criteria

| Criterion | Core question |
|---|---|
| Reversibility | Can an error be detected and corrected before harm? |
| Consequence of error | What happens if the output is wrong? |
| Human creativity or empathy | Must care, authenticity, judgment, or relationship ownership remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

Identify the **load-bearing criterion**—the factor that would change the classification if it changed.

| Classification | Meaning |
|---|---|
| Fully appropriate | Reversible, low consequence, grounded, and not dependent on special human authority or empathy |
| Appropriate with human review | AI assistance is useful, but a qualified pre-use gate is required |
| Inappropriate | AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, or policy constraints |

A review gate must state:

```text
Who reviews?
What do they verify?
When does review occur?
```

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

## 3. A Skill is software

Current Claude documentation describes Skills as folders containing instructions, scripts, and resources. Skills require code execution to be enabled.

```text
Skill contents
      ×
Session permissions
      =
Effective reach
```

Review three dimensions:

1. **Source** — publisher, owner, version, distribution path, approval, and support.
2. **Reach** — files, connectors, tools, code, secrets, persistence, and external actions available in the real session.
3. **Appropriateness** — whether the capability and access are proportionate to the approved task.

```text
Internal
      ≠
Vetted
```

Choose **Enable**, **Escalate**, or **Decline** under the correct authority. Less-trusted Skills, including those shared by colleagues, require review of bundled files, scripts, dependencies, resources, and external references before enablement.

## 4. Know data sensitivity before it enters a feature

```text
Classify
      ↓
Confirm processing approval
      ↓
Minimize or redact
      ↓
Select feature controls
      ↓
Retain, delete, monitor, or escalate
```

| Tier | Typical data | Default action |
|---|---|---|
| Green | Public, synthetic, anonymized, aggregated, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and approved environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

Redaction is valid only when it lowers identification risk and preserves task validity.

```text
Name removed
      ≠
Person de-identified
```

### Feature-control boundaries

- **Incognito:** excluded from ordinary chat history and Memory, but still subject to retention and, for Team or Enterprise accounts, organizational exports.
- **Memory:** provides continuity and follows applicable retention and export controls; it is not an authoritative or unrestricted sensitive-data store.
- **Code execution:** processes files in an execution environment, but sandboxing does not establish that the data may be processed there.

```text
Not in history or Memory
      ≠
Not retained
      ≠
Data approved for processing
```

```text
Sandboxed processing
      ≠
Approved processing
```

## 5. Ethical risk hides in ordinary outputs

```text
Accurate wording
      ≠
Fair treatment
      ≠
Ethical sufficiency
```

Review bias across:

- prompt framing and assumptions;
- source selection and representation;
- labels, categories, criteria, and examples;
- generated tone, certainty, and omissions;
- human edits; and
- downstream decision rules.

```text
Neutral-looking output
      ≠
Neutral process
```

A fairness review asks who is affected, what opportunities or burdens may change, whether similar cases are treated consistently, whether differences are justified, whether proxy characteristics influence results, and whether explanation, correction, and appeal are available.

Disclosure depends on policy, audience expectations, professional or contractual obligations, materiality of AI assistance, human review, and the risk of misleading authorship or expertise claims.

```text
No explicit disclosure rule found
      ≠
Concealment automatically appropriate
```

Escalate when the affected population is large, harm may be significant, vulnerable groups may be affected, fairness standards are contested, the team lacks standing, disclosure duties are unclear, or meaningful recourse is absent.

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

1. classifying consequential final decisions;
2. evaluating unknown executable Skills;
3. separating processing authorization from persistence controls;
4. diagnosing policy-to-practice Diligence gaps; and
5. identifying hidden bias in automated exclusions.

---

# Integrated Module 6 checklist

```text
1. Is the use appropriate under all four Delegation criteria?
2. What is the load-bearing criterion?
3. Is a who / what / when human gate required?
4. Is every Skill, connector, or tool vetted for source and effective reach?
5. Is access proportionate and least privilege?
6. What is the data classification?
7. Is the account, organization, product, and entry point approved?
8. Has unnecessary data been removed?
9. Are history, Memory, retention, export, and deletion controls understood?
10. Which policy and version control the use?
11. Does observed practice match policy?
12. Have Diligence gaps and exceptions been closed with evidence?
13. Who is affected, and what does fair treatment require?
14. Is disclosure appropriate or required?
15. Are explanation, correction, appeal, monitoring, and escalation available?
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
- [Module 6 Key Takeaways](lessons/07b-key-takeaways.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)
- [Organizational Policies and Diligence prompts](../../prompts/module-06/05-organizational-policies-diligence-prompts.md)
- [Ethical Implications prompts](../../prompts/module-06/06-ethical-implications-prompts.md)
- [Module 6 quiz and remediation prompts](../../prompts/module-06/07a-module-6-quiz-prompts.md)
- [Module 6 Key Takeaways prompts](../../prompts/module-06/07b-key-takeaways-prompts.md)

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
Technically capable but consequential       → apply Delegation criteria
Final unreviewed determination              → retain human ownership
Unknown or broad Skill                      → inspect source, bundle, and reach
Confidential data with unclear approval     → stop and verify entry point
Incognito selected for Red data             → insufficient; authorization comes first
Policy and behavior diverge                 → Diligence gap
Routine output affects people               → review bias, fairness, and disclosure
Team lacks authority to settle ethical issue → escalate with documented reasoning
```

---

# Completion criteria

- [x] I completed all Module 6 teaching sections.
- [x] I completed the Module 6 quiz with full marks, 5/5.
- [x] I completed the Module 6 takeaways.
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

# Product-verification note

This module was reviewed against official Anthropic material available on August 3, 2026. Current documentation describes Delegation and Diligence as AI Fluency competencies; Skills as folders of instructions, scripts, and resources that require code execution; less-trusted Skills as requiring review before enablement; and Incognito chats as excluded from ordinary history and Memory while still subject to retention and organizational export controls.

Product behavior, plan availability, contracts, compliance eligibility, zero-data-retention arrangements, regulated-data handling, and organizational settings can change. Current official documentation and authorized organizational or Anthropic account guidance control real deployments.

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance or ethics reviews, internal policies, regulated records, private employee or applicant data, proprietary Skill bundles, credentials, incident details, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute ethics, privacy, legal, regulatory, security, compliance, employment, medical, financial, procurement, records-management, audit, or operational advice.
