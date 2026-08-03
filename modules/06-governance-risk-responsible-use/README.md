# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** In progress — Module 6 is the active module.

## Module thesis

> Governance is a practitioner skill: decide whether a use case should proceed, whether its features and data are trustworthy for the task, who remains accountable, and how policy, ethics, monitoring, and escalation govern the work.

```text
Proposed use case
      ↓
Appropriateness classification
      ↓
Skill and feature trust review
      ↓
Data, policy, and ethical review
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
| Reversibility | Can a wrong output be caught and undone before harm? |
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

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

## The gate is part of the classification

A human-review gate must state:

- **Who** reviews;
- **What** they verify; and
- **When** review occurs before use or consequence.

It also needs evidence, time, intervention authority, escalation, and retained approval evidence.

```text
Human in the loop
      ≠
Operational human gate
```

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

## The three trust checks

### Source

Establish:

- publisher;
- owner;
- distribution path;
- current version;
- approval evidence;
- update and support path; and
- bundle integrity or provenance.

```text
Internal
      ≠
Vetted
```

Anthropic-provided and organization-reviewed Skills are lower-risk starting points for their documented purpose, not universal guarantees.

### Reach

Map what the Skill could access or change in the real session:

- files and directories;
- Project knowledge;
- connectors;
- code execution;
- tools and external systems;
- secrets exposed to the runtime;
- read, write, create, send, publish, modify, and delete actions;
- logs and retained outputs; and
- sensitive or regulated data.

Inspect the actual bundle:

- instructions;
- scripts;
- dependencies;
- bundled files;
- tool references;
- external calls;
- file paths;
- retention behavior; and
- actions beyond the stated purpose.

### Appropriateness

Ask whether the Skill is the smallest capability that meets the approved task.

```text
Useful capability
      ≠
Necessary capability
      ≠
Proportionate capability
```

Apply least privilege: reduce files, connectors, write permissions, external actions, persistence, and audience to the minimum required.

## Trust is contextual

```text
Same Skill
+ different data
+ different connectors
+ different permissions
=
different risk decision
```

Trust belongs to the Skill–environment–use-case combination, not the Skill name alone.

## Three outcomes

| Outcome | Use when |
|---|---|
| Enable | Source, reach, appropriateness, policy, tests, monitoring, and disable paths are clear |
| Escalate | The Skill may be useful, but broader authority or specialist review is required |
| Decline | Source is unverifiable, access is disproportionate, policy conflicts exist, or review cannot make the use responsible |

```text
Trust check failed
      ≠
Always permanent ban
```

It means the current user should not enable the capability under the current authority and conditions.

---

# Worked Skill portfolio

| Skill | Source | Reach | Appropriateness | Outcome |
|---|---|---|---|---|
| Anthropic-provided document formatter | Established | Task-matched document handling | Fits approved non-sensitive document task | Enable with normal controls |
| Unknown analytics booster | Unknown publisher | Scripts, broad files, unrelated connectors | Disproportionate to stated task | Escalate or decline |
| Internal status-report Skill | Known sister team, no current review | Shared repository access and stale policy template | Useful method, excessive current reach | Escalate and request narrower reviewed version |

---

# Feature-level risk generalization

Apply the same proportionality habit to connectors, code execution, tools, integrations, Memory, and external actions.

```text
Who provides it?
What can it access, execute, persist, or change?
Is that reach proportionate to the approved task?
```

```text
Feature enabled
      ≠
Feature governed
```

For consequential capabilities, define monitoring, human approval, logging, revocation, rollback, and incident response.

---

# Skill trust register

| Field | Purpose |
|---|---|
| Skill ID and version | Stable identification |
| Publisher and owner | Provenance and accountability |
| Distribution path | Anthropic, organization, shared, personal, third-party |
| Stated purpose | Intended task |
| Bundle contents | Instructions, scripts, files, dependencies |
| Runtime requirements | Code execution, files, connectors, tools, network |
| Effective reach | Data and actions exposed during use |
| Data classification | Information processed |
| External actions | Create, update, send, publish, delete |
| Review status | Approved, conditional, pending, rejected |
| Tests | Functional, security, boundary, regression |
| Limitations | Residual risk |
| Disable or rollback | Containment path |
| Review date | Revalidation schedule |

---

# Integrated governance protocol

```text
1. Define the bounded use case, users, and affected parties
2. Run reversibility, consequence, human-element, and accountability criteria
3. Identify the load-bearing criterion and classification
4. Define the who / what / when gate or retained human role
5. Identify the Skill or feature, publisher, owner, and version
6. Inspect instructions, scripts, dependencies, files, and external calls
7. Map effective reach across the real environment
8. Compare access with task necessity, data sensitivity, and policy
9. Apply least privilege and preserve approval boundaries
10. Run functional, security, boundary, and regression tests
11. Record monitoring, residual risk, disable, and re-review triggers
12. Enable, escalate, decline, constrain, redesign, defer, or reject
```

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Appropriate vs Inappropriate Use Cases](lessons/02-appropriate-vs-inappropriate-use-cases.md)
- [Skill Trust and Feature-Level Risk](lessons/03-skill-trust-feature-level-risk.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-06/01-module-introduction-prompts.md)
- [Appropriate vs Inappropriate Use Cases prompts](../../prompts/module-06/02-appropriate-vs-inappropriate-use-cases-prompts.md)
- [Skill Trust and Feature-Level Risk prompts](../../prompts/module-06/03-skill-trust-feature-risk-prompts.md)

## Engineering patterns

- [Use-Case Appropriateness Classification Pattern](../../patterns/use-case-appropriateness-classification-pattern.md)
- [Skill Trust and Feature-Risk Pattern](../../patterns/skill-trust-and-feature-risk-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Unknown publisher with broad reach        → escalate or decline
Internal Skill without review evidence    → internal is not automatically vetted
Skill description narrower than contents  → inspect and treat as a red flag
Skill inherits broad session environment  → reduce effective reach
Capability exceeds task need              → choose narrower capability
User lacks approval authority             → escalate
Source, reach, and appropriateness clear   → enable with monitoring
Useful output                              → does not prove safe behavior
```

For Skill and feature-risk scenarios:

1. identify the exact feature and version;
2. establish publisher and owner;
3. inspect the bundle rather than relying on the name;
4. enumerate effective reach;
5. compare access with the approved task;
6. apply least privilege;
7. classify data and external actions;
8. confirm approval authority;
9. define tests, monitoring, and disable paths; and
10. choose enable, escalate, or decline.

---

# Completion criteria

- [x] I completed the Module 6 introduction.
- [x] I completed Appropriate vs Inappropriate Use Cases.
- [x] I completed Skill Trust and Feature-Level Risk.
- [ ] I can assess reversibility, consequence, human element, and accountability.
- [ ] I can identify the load-bearing criterion and define an operational gate.
- [ ] I can distinguish source trust, effective reach, and appropriateness.
- [ ] I can inspect Skill instructions, scripts, dependencies, and bundled files.
- [ ] I can apply least privilege to Skills and other features.
- [ ] I can choose enable, escalate, or decline under the correct authority.
- [ ] I can classify data and apply privacy controls.
- [ ] I can locate and apply organizational policy.
- [ ] I can identify ethical implications beyond compliance.
- [ ] I can define meaningful human oversight and incident response.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential Skill bundles, proprietary scripts, internal security findings, restricted data, private connector identifiers, credentials, organization-only review records, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute security, privacy, legal, compliance, procurement, software-assurance, or operational advice.

## Source note

The Skill Trust and Feature-Level Risk course material was supplied on August 3, 2026. Product behavior and organizational controls can change. Current official documentation and organizational policy govern real deployments.
