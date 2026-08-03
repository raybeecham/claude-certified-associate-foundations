# Lesson 7B: Module 6 Key Takeaways

## Overview

Module 6 turns governance from an abstract policy topic into a repeatable practitioner discipline.

```text
Use-case judgment
+ feature trust
+ data classification
+ policy Diligence
+ ethical review
=
responsible AI practice
```

The five takeaways in this lesson are durable because they remain useful even when products, features, plans, policies, or organizational controls change.

---

# 1. Governance is a practitioner skill

Governance is exercised through individual decisions about:

- whether a use case should proceed;
- which tasks may be delegated;
- what data may enter a feature;
- whether a Skill or connector is trustworthy for the environment;
- which human gate is required;
- whether disclosure is appropriate;
- when a policy gap needs remediation; and
- when the issue exceeds the practitioner’s authority and must be escalated.

```text
Policy exists
      ≠
Policy applied
      ≠
Responsible outcome
```

A policy sets boundaries. Practitioners translate those boundaries into daily behavior, evidence, controls, review gates, and escalation.

## AI Fluency connection

The AI Fluency Framework describes **Delegation** as deciding what work to do with AI and what to retain for people. It describes **Diligence** as responsible collaboration, including thoughtful system choice, transparency about AI’s role, verification, and ownership of outputs.

```text
Delegation → responsibility boundary
Diligence  → ownership and verification
```

Governance therefore depends on both:

- **Delegation:** Should Claude perform, assist, or avoid this work?
- **Diligence:** Who verifies the conditions, owns the output, and documents the decision?

---

# 2. Screen use cases with the Delegation criteria

Use four criteria:

| Criterion | Core question |
|---|---|
| Reversibility | Can an error be detected and corrected before harm? |
| Consequence of error | What happens if the output is wrong? |
| Human creativity or empathy | Must judgment, care, authenticity, or relationship ownership remain human? |
| Accountability | Who is answerable, and can that person meaningfully review and intervene? |

The criteria interact. The decision should identify the **load-bearing criterion**—the criterion that would change the classification if it changed.

## Three classifications

### Fully appropriate

The task is reversible, low consequence, suitably grounded, and does not require special human authority or empathy.

### Appropriate with human review

AI assistance is useful, but a material risk requires a qualified pre-use gate.

The gate must state:

```text
Who reviews?
What do they verify?
When does review occur?
```

It should also provide evidence, time, authority to reject or modify, escalation, and retained approval evidence.

### Inappropriate

AI ownership cannot be made responsible because of severe or irreversible consequence, non-transferable accountability, essential human care, policy prohibition, or the absence of meaningful review.

```text
Technically possible
      ≠
Appropriate
      ≠
Approved
```

---

# 3. A Skill is software

A Skill is not merely a prompt label. Current Claude documentation describes Skills as folders containing instructions, scripts, and resources that load dynamically for relevant tasks. Skills require code execution to be enabled.

That makes trust review a software-assurance decision.

## Three trust checks

### Source

Establish:

- publisher;
- owner;
- version;
- distribution path;
- approval evidence;
- update and support path; and
- provenance of the bundle.

```text
Internal
      ≠
Vetted
```

### Reach

Inspect the environment in which the Skill will run.

```text
Skill contents
      ×
Session access
      =
Effective reach
```

Review:

- bundled instructions and scripts;
- dependencies;
- uploaded files;
- connectors;
- tools;
- code execution;
- external network references;
- secrets exposed to the runtime;
- persistence and logging; and
- read, write, create, send, publish, modify, or delete actions.

### Appropriateness

Ask whether the capability and access are proportionate to the approved task.

```text
Useful capability
      ≠
Necessary capability
      ≠
Least-privilege capability
```

## Trust outcomes

| Outcome | Meaning |
|---|---|
| Enable | Source, contents, effective reach, policy, and task fit are clear |
| Escalate | Specialist review or higher approval is required |
| Decline | Source is unverifiable, access is disproportionate, or review cannot make the use responsible |

Official guidance warns that less-trusted Skills—including Skills shared by colleagues—should be reviewed before enabling, with particular attention to dependencies, bundled resources, scripts, and untrusted external sources.

---

# 4. Know data sensitivity before it enters a feature

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

## Rapid classification

| Tier | Typical examples | Default action |
|---|---|---|
| Green | Public, synthetic, aggregated, anonymized, or broadly cleared | Proceed under normal controls |
| Yellow | Internal, confidential, identifiable, unreleased, or uncertain | Review policy and approved environment first |
| Red | Regulated, secret, legally restricted, or unapproved third-party data | Keep out until an approved path exists |

When uncertain, use the more sensitive tier until an authorized owner clarifies the classification.

## Redaction and minimization

Remove information that the task does not need. Redaction is valid only when it:

1. reduces identification or confidentiality risk; and
2. preserves the validity of the task.

```text
Name removed
      ≠
Person de-identified
```

Indirect identifiers, exact dates, uncommon roles, precise locations, small populations, and free text can still identify people.

## Feature controls are bounded

### Incognito

Current Claude guidance says Incognito chats are not saved to ordinary chat history or Memory. They are still retained for a default period and, for Team or Enterprise accounts, can be included in organizational exports and remain subject to organizational retention settings.

```text
Not in history or Memory
      ≠
Not retained
      ≠
Data approved for processing
```

### Memory

Memory supports continuity but follows applicable retention and export controls. It should not become an unreviewed store for sensitive information or authoritative organizational state.

### Code execution sandbox

Code execution can process uploaded files in a sandboxed environment. Sandboxing limits execution exposure; it does not determine whether the data was permitted to enter that environment.

```text
Sandboxed processing
      ≠
Approved processing
```

The correct habit is:

> Classify first, confirm the approved path, minimize what is unnecessary, and then select history, Memory, retention, sandbox, sharing, export, and deletion controls.

---

# 5. Ethical risk hides in ordinary outputs

Ethical risk does not require a dramatic or obviously harmful system. It can appear in routine summaries, recommendations, evaluations, rankings, and communications.

```text
Accurate wording
      ≠
Fair treatment
      ≠
Ethical sufficiency
```

## Review bias entry points

Inspect:

- prompt framing and assumptions;
- source selection and representation;
- labels, categories, and evaluation criteria;
- examples and evidence thresholds;
- generated tone, certainty, and omissions;
- human edits; and
- downstream decision rules.

```text
Neutral-looking output
      ≠
Neutral process
```

## Define fairness for the task

Ask:

- Who is affected?
- What opportunities, burdens, treatment, or reputation may change?
- Are relevantly similar cases treated consistently?
- Are material differences justified?
- Are protected or proxy characteristics influencing results?
- Are evidence and certainty standards consistent?
- Can affected people receive explanation, correction, or appeal?

## Determine transparency and disclosure

Diligence includes transparency about AI’s role when the relevant audience needs to know. Disclosure depends on:

- policy;
- audience expectation;
- professional or contractual obligations;
- materiality of the AI contribution;
- risk of misleading authorship or expertise claims;
- human review performed; and
- consequence of concealment.

When the obligation is materially unclear, seek authorized guidance rather than silently concealing AI assistance.

## Know when to escalate

Escalate when:

- affected populations are large;
- potential harm is significant or difficult to reverse;
- vulnerable or protected groups may be affected;
- fairness standards are disputed;
- the team lacks expertise or organizational standing;
- surveillance, manipulation, or power imbalance is present;
- disclosure duties are materially unclear;
- no meaningful recourse exists; or
- policy assigns the decision elsewhere.

```text
Structured reasoning completed
      ≠
Authority to decide
```

---

# Integrated Module 6 checklist

Before approving an AI-assisted use, ask:

```text
1. Is the use case appropriate under all four Delegation criteria?
2. What is the load-bearing criterion?
3. Is a who / what / when human gate required?
4. Is every Skill, connector, or tool vetted for source and effective reach?
5. Is the capability proportionate and least privilege?
6. What is the data classification?
7. Is the selected account, organization, product, and entry point approved?
8. Has unnecessary data been removed?
9. Are history, Memory, retention, export, and deletion controls understood?
10. Which policy and version control the use?
11. Does observed practice match the policy?
12. Have Diligence gaps and exceptions been closed with evidence?
13. Who is affected, and what would fair treatment require?
14. Is disclosure appropriate or required?
15. Are explanation, correction, appeal, monitoring, and escalation available?
```

---

# Exam lens

```text
Technically capable but consequential       → apply Delegation criteria
Final unreviewed determination              → retain human ownership
Unknown or broad Skill                      → inspect source, bundle, and reach
Confidential data with unclear approval     → stop and verify the entry point
Incognito selected for Red data             → insufficient; authorization comes first
Policy and behavior diverge                 → Diligence gap
Routine output affects people               → review bias, fairness, and disclosure
Team lacks authority to settle ethical issue → escalate with documented reasoning
```

---

# Short recap

```text
1. Governance is practiced through daily decisions.
2. Delegation classifies the use; Diligence verifies and owns it.
3. Skills and powerful features require software-like trust review.
4. Data classification precedes every upload and feature control.
5. Fairness, transparency, and escalation belong in routine review.
```

> Responsible AI use is not a single approval. It is a maintained chain of judgment, evidence, controls, human accountability, and correction.

---

# Product-verification note

This lesson was reviewed against official Anthropic material available on August 3, 2026. Current documentation describes:

- Delegation and Diligence as core AI Fluency competencies;
- Skills as folders of instructions, scripts, and resources that require code execution;
- less-trusted Skills as requiring review before enablement;
- Incognito chats as excluded from ordinary history and Memory while still subject to retention and organizational export controls; and
- code execution and file creation as capabilities that process files through Claude’s execution environment.

Product behavior, plan availability, legal scope, contracts, compliance eligibility, zero-data-retention arrangements, regulated-data handling, and organizational controls can change. Verify current official documentation and obtain confirmation from authorized organizational or Anthropic account representatives for real regulated or compliance-scoped deployments.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, privacy, security, compliance, ethics, employment, medical, financial, records-management, procurement, audit, or operational advice.

## Related material

- [Module 6 overview](../README.md)
- [Module 6 Quiz](07a-module-6-quiz.md)
- [Module 6 Key Takeaways prompts](../../../prompts/module-06/07b-key-takeaways-prompts.md)
