# Module 6: Governance, Risk & Responsible Use

Associate Persona · Official Exam Domain 6

> **Status:** Roadmap staged — Module 5 is complete. No Module 6 lesson is marked complete yet.

## Module thesis

> Responsible use requires deciding whether a use case should proceed, what data and feature boundaries apply, who remains accountable, and how policy, ethics, monitoring, and escalation govern the system over time.

```text
Proposed use case
      ↓
Appropriateness assessment
      ↓
Feature and Skill trust review
      ↓
Data sensitivity and privacy controls
      ↓
Organizational policy and diligence
      ↓
Ethical-impact analysis
      ↓
Human approval, monitoring, and escalation
      ↓
Responsible-use decision
```

---

# Course-aligned roadmap

- [ ] 01. Module Introduction
- [ ] 02. Appropriate vs Inappropriate Use Cases
- [ ] 03. Skill Trust & Feature-Level Risk
- [ ] 04. Data Sensitivity, Privacy & Feature Controls
- [ ] 05. Organizational Policies & Diligence
- [ ] 06. Ethical Implications
- [ ] 07. Module 6 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 08. Module Complete

No lesson is marked complete until its corresponding preparation-course material is supplied and converted into original public-safe study content.

---

# Module 5 to Module 6 bridge

Module 5 established how to configure and maintain a reliable operating environment.

```text
Configured Project
+ governed knowledge
+ precise instructions
+ scoped connectors
+ maintained Skills and Memory
      ↓
Repeatable operating baseline
```

Module 6 asks whether that configured capability should be used for a particular purpose and under what controls.

```text
Repeatable capability
      ↓
Use-case suitability
      ↓
Data and privacy boundaries
      ↓
Policy and feature-risk review
      ↓
Ethical and stakeholder impact
      ↓
Approval, monitoring, and accountability
```

The transition question is:

> The environment is configured correctly—but is the use case appropriate, are the data and feature controls sufficient, and who owns the consequences?

---

# Durable governance foundation

The repository already contains extended governance, risk, and responsible-use material. It will be mapped to the supplied course sections as they arrive.

## 1. Appropriate versus inappropriate use

A technically possible use case is not automatically an appropriate one.

Assess:

- intended outcome;
- affected people and decisions;
- stakes and reversibility;
- legal, policy, contractual, and professional constraints;
- required expertise;
- transparency and disclosure;
- data sensitivity;
- human authority;
- failure consequences;
- appeal or correction paths; and
- whether the use is prohibited, restricted, or unsuitable.

```text
Model can perform task
      ≠
Organization should deploy task
```

High-impact decisions require stronger evidence, meaningful human review, clear accountability, and escalation.

## 2. Skill trust and feature-level risk

Features should be evaluated by what they can access, execute, persist, or change.

Risk considerations include:

- source and publisher trust;
- code or script execution;
- connector permissions;
- file-system or external-system access;
- hidden dependencies;
- update and distribution behavior;
- data retention;
- prompt-injection exposure;
- external side effects;
- approval requirements; and
- rollback or disable paths.

```text
Feature available
      ≠
Feature approved
      ≠
Feature trusted for this use case
```

A Skill or connector should not inherit trust merely because it is convenient or previously worked in a different context.

## 3. Data sensitivity, privacy, and feature controls

Classify data before selecting an environment or feature.

Consider:

- public, internal, confidential, restricted, regulated, or controlled data;
- personal information;
- client or third-party restrictions;
- intellectual property;
- credentials and secrets;
- geographic or residency constraints;
- retention requirements;
- training or product-use settings;
- connector and sharing permissions;
- Memory and continuity settings;
- logging and export behavior; and
- deletion, revocation, and incident response.

```text
Data accessible
      ≠
Data approved for processing
```

Apply data minimization and least privilege. Use only the information, access, retention, and features required for the approved purpose.

## 4. Organizational policy and diligence

Responsible operation requires current organizational guidance, not assumptions about what is allowed.

Diligence may require:

- reviewing acceptable-use and AI policies;
- confirming approved products and plans;
- checking data-classification rules;
- identifying required security, privacy, legal, records, compliance, or ethics review;
- documenting exceptions;
- retaining approvals;
- monitoring changes in product behavior and policy;
- assigning accountable owners; and
- defining incident and escalation paths.

```text
No policy found
      ≠
Use is automatically permitted
```

When policy is unclear, pause or narrow the use case and seek authorized clarification.

## 5. Ethical implications

Ethical review extends beyond policy compliance.

Examine:

- fairness and disparate impact;
- representation and bias;
- autonomy and consent;
- deception or manipulation;
- surveillance and power imbalance;
- accessibility;
- explainability;
- affected-party recourse;
- labor and role impacts;
- environmental or resource considerations;
- misuse potential; and
- whether benefits and risks are distributed fairly.

```text
Policy-compliant
      ≠
Ethically sufficient
```

Ethical uncertainty should be surfaced rather than hidden behind technical feasibility or business value.

## 6. Meaningful human oversight

A nominal human-in-the-loop is insufficient when the reviewer lacks:

- expertise;
- access to evidence;
- sufficient time;
- authority to intervene;
- independence;
- clear review criteria; or
- an escalation route.

```text
Human review mentioned
      ≠
Human oversight operational
```

For consequential decisions, define who reviews, what evidence they inspect, when review occurs, what criteria apply, what authority they retain, and how disagreements or appeals are handled.

## 7. Security and misuse risks

Threat-model:

- prompt injection;
- jailbreaks;
- malicious or untrusted Skills;
- data exfiltration;
- overbroad connector permissions;
- unauthorized external actions;
- hidden tool calls;
- stale dependencies;
- supply-chain risk;
- unsafe automation;
- logging of sensitive content; and
- misuse by authorized or unauthorized users.

Use layered controls:

```text
Policy
+ least privilege
+ input and source validation
+ tool restrictions
+ deterministic checks
+ human approval
+ logging and monitoring
+ incident response
```

No single prompt or instruction can provide these controls by itself.

---

# Governance decision protocol

```text
1. Define the proposed use case, users, and affected parties
2. Classify stakes, reversibility, and decision impact
3. Check prohibited, restricted, and unsuitable uses
4. Classify data and confirm an approved processing environment
5. Review Skills, connectors, tools, Memory, and feature-level risks
6. Apply least privilege, minimization, and retention controls
7. Review organizational policy and required approvals
8. Assess fairness, consent, transparency, accessibility, and recourse
9. Define meaningful human oversight and accountability
10. Threat-model misuse, prompt injection, exfiltration, and unauthorized action
11. Establish monitoring, logging, escalation, and incident response
12. Approve, constrain, redesign, defer, or reject the use case
```

---

# Learning objectives

By the end of this module, you should be able to:

- distinguish technically possible uses from appropriate uses;
- identify prohibited, restricted, high-impact, and unsuitable use cases;
- evaluate Skill and feature trust before enabling them;
- assess connector, code-execution, Memory, sharing, and persistence risks;
- classify data before selecting products, plans, and features;
- apply privacy, minimization, retention, and least-privilege controls;
- locate and apply organizational policy rather than assuming permission;
- document diligence, exceptions, approvals, and accountable owners;
- identify fairness, consent, transparency, accessibility, and recourse concerns;
- define meaningful human review for consequential uses;
- threat-model prompt injection, exfiltration, and unauthorized action;
- establish monitoring, incident response, and escalation paths; and
- distinguish model assistance from delegated organizational accountability.

---

# Existing module resources

The repository already contains extended practice material that remains available while the course-aligned lessons are developed.

- [notes.md](notes.md): Governance, data, risk, oversight, and responsible-use concepts
- [lab.md](lab.md): Applied threat-model and governance exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

Course-aligned lessons and Module 6 prompt notebooks will be added as each supplied section is completed.

---

# Exam lens

```text
Technically possible but high-impact       → assess appropriateness and oversight
Untrusted Skill or connector               → review source, permissions, code, and side effects
Sensitive data proposed for upload         → classify data and verify approved environment
Policy is unclear                          → seek authorized clarification
Human review has no authority or evidence  → oversight is not meaningful
Use is compliant but potentially unfair    → perform ethical-impact review
Prompt instruction says `do not disclose`  → still require technical privacy controls
Consequential action has no appeal path     → add recourse or redesign
```

For governance scenarios:

1. identify the affected people and decision;
2. assess stakes, reversibility, and misuse potential;
3. check current policy and prohibited-use boundaries;
4. classify data and processing environment;
5. inspect feature, Skill, connector, and permission risk;
6. apply minimization and least privilege;
7. define meaningful human oversight;
8. consider fairness, consent, transparency, accessibility, and recourse;
9. establish monitoring, incident response, and accountability; and
10. approve, constrain, redesign, defer, or reject.

---

# Completion criteria

- [ ] I completed the Module 6 introduction.
- [ ] I can distinguish appropriate, inappropriate, prohibited, restricted, and high-impact uses.
- [ ] I can evaluate Skill trust and feature-level risk.
- [ ] I can classify data before selecting an environment or feature.
- [ ] I can apply privacy, minimization, retention, and least-privilege controls.
- [ ] I can locate and apply organizational policy.
- [ ] I can document diligence, exceptions, approvals, and ownership.
- [ ] I can identify ethical implications beyond policy compliance.
- [ ] I can define meaningful human oversight.
- [ ] I can identify prompt-injection, exfiltration, and unauthorized-action controls.
- [ ] I can outline monitoring, escalation, and incident response.
- [ ] I completed the Module 6 quiz and takeaways.
- [ ] I completed the threat-model lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential governance reviews, internal policies, restricted data, private incident reports, client identities, credentials, connector identifiers, proprietary risk assessments, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, privacy, security, compliance, ethics, employment, medical, financial, records-management, or operational advice.

## Official reading

Policies and product capabilities can change. Verify current official documentation before relying on implementation-specific behavior.

- [Anthropic Usage Policy](https://www.anthropic.com/legal/aup)
- [Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)
- [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
