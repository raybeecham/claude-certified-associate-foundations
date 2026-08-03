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
- [x] [02. Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
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

# Foundation 1: Governance as practitioner judgment

Governance is applied through daily choices about use cases, uploads, Skills, connectors, review gates, affected people, and escalation.

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

A technically possible task is not automatically appropriate.

Screen every proposed use with four Delegation criteria:

| Criterion | Question |
|---|---|
| Reversibility | Can an incorrect output be detected and undone before harm? |
| Consequence of error | What happens if the output is wrong? |
| Human creativity or empathy | Does judgment, care, authenticity, or relationship ownership need to remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

```text
Claude can produce output
      ≠
Claude should own the task
      ≠
Organization may use it without controls
```

## The load-bearing criterion

Run all four criteria, then name the one that controls the classification.

The load-bearing criterion is the one that, if changed, would move the use case between classifications.

```text
All criteria considered
      ↓
Load-bearing criterion named
      ↓
Defensible classification
```

Examples:

- A condolence-note draft may be reversible and low consequence, but the human relationship requirement is load bearing.
- A financial summary may be consequential, but a qualified pre-use review can restore accountability and practical reversibility.
- A final professional determination may remain inappropriate because accountability cannot transfer and consequences may be difficult to reverse.

---

# Three classifications

## Fully appropriate

Use when the task is reversible, low consequence, suitably grounded, not dependent on special human empathy or authority, and subject to normal quality review.

## Appropriate with human review

Use when AI assistance is useful but consequence, fairness, relationship sensitivity, policy exposure, or accountability requires a qualified pre-use gate.

## Inappropriate

Use when AI ownership cannot be made responsible because of irreversibility, severe consequence, non-transferable accountability, essential human care, policy prohibition, or the absence of meaningful review.

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

---

# The gate is part of the classification

`Appropriate with human review` is incomplete until the gate is operational.

| Gate element | Required question |
|---|---|
| Who | Which accountable and qualified role reviews? |
| What | Which facts, risks, evidence, fairness, or policy conditions are checked? |
| When | At what point before use or consequence does review occur? |

A complete gate also gives the reviewer evidence, time, authority to reject or modify, an escalation path, and retained approval evidence.

```text
Human in the loop
      ≠
Operational human gate
```

If the who, what, and when cannot be stated, the use case is not ready to run.

---

# Worked portfolio

| Use case | Classification | Load-bearing criterion | Required control |
|---|---|---|---|
| Draft internal FAQ from approved policy documents | Fully appropriate | Reversibility and low consequence | Normal source and owner review |
| Summarize resumes into a proposed shortlist | Appropriate with human review | Accountability and consequence | Hiring reviewer checks job relevance, unsupported inference, fairness, and policy before any decision or contact |
| Generate a final medical or legal determination | Inappropriate for AI ownership | Non-transferable accountability | Qualified professional makes and owns the determination |
| Draft a response to a billing complaint | Appropriate with human review | Accountability | Support agent verifies account facts, policy, disclosures, and tone before send |

---

# Defensible rationale format

```text
Use case:
[bounded description]

Classification:
Fully appropriate / Appropriate with human review / Inappropriate

Delegation criteria:
- Reversibility:
- Consequence of error:
- Human creativity or empathy:
- Accountability:

Load-bearing criterion:
[criterion and why it controls]

Human gate or retained role:
- Who:
- What:
- When:

Conditions and controls:
[data, policy, evidence, permissions, monitoring]

Decision owner:
[accountable role]
```

This replaces `it feels risky` with a reviewable governance decision.

---

# Broader governance foundation

Later lessons will extend this baseline into:

- Skill provenance, code, dependencies, access, persistence, and side effects;
- data sensitivity, privacy, minimization, retention, and feature controls;
- organizational AI policy, diligence, approvals, exceptions, and records;
- fairness, consent, accessibility, transparency, and recourse;
- prompt injection, exfiltration, unauthorized action, and misuse;
- meaningful human oversight, monitoring, escalation, and incident response.

```text
Feature available
      ≠
Feature approved
      ≠
Feature trusted for this use case
```

```text
Data accessible
      ≠
Data approved for processing
```

```text
Policy-compliant
      ≠
Ethically sufficient
```

---

# Use-case screening protocol

```text
1. Define the bounded use case and intended outcome
2. Identify users, affected parties, and decision context
3. Assess reversibility before consequence
4. Assess the consequence of error
5. Assess need for human creativity, empathy, or relationship ownership
6. Identify who retains accountability
7. Check policy, data, and prohibited-use boundaries
8. Identify the load-bearing criterion
9. Classify as fully appropriate, human-reviewed, or inappropriate
10. Define the who, what, and when gate or retained human role
11. Record conditions, evidence, monitoring, and escalation
12. Approve, constrain, redesign, defer, or reject
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)

## Engineering pattern

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Low-stakes reversible drafting       → often fully appropriate
Consequential recommendation         → human-reviewed with explicit gate
Essential empathy or relationship    → retain human ownership
Final professional determination     → human professional owns the decision
Human in the loop                    → require who, what, and when
Criteria interact                    → identify the load-bearing criterion
Accountability assigned to Claude    → invalid; retain human accountability
Feels risky                          → replace with criterion-based rationale
```

For appropriateness scenarios:

1. define the exact use case;
2. run all four Delegation criteria;
3. avoid capability-first reasoning;
4. identify the load-bearing criterion;
5. preserve non-transferable accountability;
6. define meaningful review before consequence;
7. distinguish AI assistance from AI ownership;
8. name the retained human role;
9. document conditions and escalation; and
10. choose a defensible classification.

---

# Completion criteria

- [x] I completed the Module 6 introduction.
- [x] I completed Appropriate vs Inappropriate Use Cases.
- [ ] I can assess reversibility, consequence, human element, and accountability.
- [ ] I can identify the load-bearing criterion.
- [ ] I can distinguish fully appropriate, human-reviewed, and inappropriate uses.
- [ ] I can define an operational who / what / when review gate.
- [ ] I can preserve non-transferable human accountability.
- [ ] I can evaluate Skill trust and feature-level risk.
- [ ] I can classify data and apply privacy controls.
- [ ] I can locate and apply organizational policy.
- [ ] I can identify ethical implications beyond compliance.
- [ ] I can define meaningful human oversight and incident response.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance reviews, internal policies, restricted data, private personnel or applicant records, client identities, medical or legal determinations, credentials, proprietary risk assessments, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, medical, employment, financial, privacy, security, compliance, ethics, or operational advice.

## Source note

The Appropriate vs Inappropriate Use Cases course material was supplied on August 3, 2026. Current law, policy, organizational controls, and qualified professional judgment govern real use cases.
