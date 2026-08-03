# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — Module 6 is the active module.

## Module thesis

> Governance is a practitioner skill: classify the use case, feature, data, policy, and ethical impact before deployment; retain accountable human authority; and monitor the decision over time.

```text
Proposed use case
      ↓
Appropriateness classification
      ↓
Skill and feature trust review
      ↓
Data classification and feature controls
      ↓
Policy and ethical review
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
- [ ] 05. Organizational Policies & Diligence
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

Screen every use case against four Delegation criteria:

| Criterion | Core question |
|---|---|
| Reversibility | Can an incorrect output be detected and undone before harm? |
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

## Load-bearing criterion

Run all four criteria, then name the one that controls the classification—the criterion that would move the use case if it changed.

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

Review three dimensions:

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

## Minimum necessary data

Before applying a feature control, determine whether the task needs each field.

Possible actions include:

- remove unused columns;
- aggregate records;
- pseudonymize identities;
- replace real data with synthetic examples;
- omit secrets entirely; and
- separate confidential context from analytical inputs.

```text
Available data
      ≠
Necessary data
```

## Redaction boundaries

Redaction is valid only when it reduces identification risk **and** preserves the task’s validity.

```text
Name removed
      ≠
Person de-identified
```

Review account identifiers, exact dates, rare job titles, precise locations, small groups, free text, and distinctive field combinations.

If identifiers are essential, use an approved environment or stop. Do not use superficial redaction to force sensitive data into an unapproved path.

## Code execution

Claude’s code-execution environment is sandboxed, but sandboxing does not establish that a data class may be processed there.

```text
Sandboxed
      ≠
Approved for every data class
```

Minimize uploaded files, remove secrets, review generated artifacts, and follow current network, retention, and deletion controls.

## Memory

Memory provides continuity but should not become an unreviewed archive or authoritative system of record.

```text
Useful to remember
      ≠
Appropriate to persist
```

Review sensitivity, staleness, export, retention, editing, deletion, and organizational controls.

## Incognito

Current Claude guidance describes Incognito chats as excluded from ordinary chat history and Memory. For Team and Enterprise accounts, organizational retention and export rules still apply.

```text
Not in history or Memory
      ≠
Not retained by the organization
      ≠
Permission to process Red data
```

Incognito is a persistence control. It is not a compliance approval or an approved entry point for regulated data.

## Processing and persistence are separate decisions

```text
Question 1:
May this data be processed here?

Question 2:
If yes, how may it be remembered, retained, exported, or deleted?
```

Answer Question 1 first.

---

# Worked data decisions

| Scenario | Classification | Decision |
|---|---|---|
| Anonymized survey trends | Green | Use code execution for verified counts; check small-group re-identification |
| Confidential acquisition draft | Yellow | Confirm policy and approved account; minimize details; use Incognito only if processing is allowed |
| Customer spreadsheet with PII | Yellow or Red | Redact and test indirect identifiers, or use an approved path; otherwise stop |
| Patient records | Red without confirmed compliant path | Do not upload; escalate to the authorized administrator or privacy function |

---

# Integrated governance protocol

```text
1. Define the bounded use case, users, affected parties, and owner
2. Run reversibility, consequence, human-element, and accountability criteria
3. Identify the load-bearing criterion and human gate
4. Establish Skill or feature source, contents, reach, and proportionality
5. Define the task’s minimum required data
6. Classify data under current organizational policy
7. Confirm the approved account, product, entry point, and retention environment
8. Minimize, redact, aggregate, pseudonymize, or synthesize where valid
9. Select execution, Memory, history, sharing, export, and deletion controls
10. Test re-identification risk and task validity
11. Record approval, monitoring, revocation, incident, and escalation paths
12. Approve, constrain, redesign, defer, decline, or reject
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
- [Skill Trust and Feature-Level Risk](lessons/03-skill-trust-feature-level-risk.md)
- [Data Sensitivity, Privacy & Feature Controls](lessons/04-data-sensitivity-privacy-feature-controls.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)
- [Data Sensitivity, Privacy & Feature Controls prompts](../../prompts/module-06/04-data-sensitivity-privacy-feature-controls-prompts.md)

## Engineering patterns

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)
- [Skill Trust and Feature-Risk Pattern](../../patterns/skill-trust-and-feature-risk-pattern.md)
- [Data Classification and Feature-Control Pattern](../../patterns/data-classification-and-feature-control-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Public or approved anonymized data       → usually Green
Confidential internal material           → Yellow; review first
Regulated data, credentials, or secrets  → Red without approved path
Incognito                                → history and Memory control, not permission
Sandbox                                  → execution isolation, not authorization
Name removed but unique details remain   → incomplete redaction
Sensitive identifiers unnecessary        → minimize or redact
Sensitive identifiers required           → approved environment or stop
Unsure between tiers                     → use the more sensitive tier
```

For data-sensitivity scenarios:

1. classify before upload;
2. identify the minimum necessary data;
3. map the rapid tier to current policy;
4. separate processing approval from persistence controls;
5. identify direct and indirect identifiers;
6. test whether redaction preserves task validity;
7. use Incognito only inside an approved processing boundary;
8. understand sandbox and Memory limits;
9. verify current organization settings rather than relying on plan assumptions; and
10. escalate when no approved path is established.

---

# Completion criteria

- [x] I completed the Module 6 introduction.
- [x] I completed Appropriate vs Inappropriate Use Cases.
- [x] I completed Skill Trust and Feature-Level Risk.
- [x] I completed Data Sensitivity, Privacy & Feature Controls.
- [ ] I can assess reversibility, consequence, human element, and accountability.
- [ ] I can identify the load-bearing criterion and define an operational gate.
- [ ] I can distinguish source trust, effective reach, and feature appropriateness.
- [ ] I can classify data as Green, Yellow, or Red and map it to current policy.
- [ ] I can identify minimum necessary data and valid minimization options.
- [ ] I can distinguish direct identifiers from indirect re-identification risk.
- [ ] I can explain why Incognito and sandboxing do not authorize regulated data.
- [ ] I can separate processing approval from Memory, history, retention, and export controls.
- [ ] I can locate and apply organizational policy.
- [ ] I can identify ethical implications beyond compliance.
- [ ] I can define meaningful oversight and incident response.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include regulated records, credentials, secrets, confidential transactions, private personnel or customer data, internal privacy findings, organization-only retention details, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute privacy, legal, regulatory, security, compliance, medical, financial, records-management, or operational advice.

## Product-verification note

The data-control material was reviewed against official Anthropic Help Center content available on August 3, 2026. Current guidance describes code execution as sandboxed and Incognito as excluded from ordinary history and Memory, while organizational retention and exports can still apply. Product behavior, plans, organizational settings, contracts, and policy can change; current official documentation and authorized organizational guidance control real decisions.
