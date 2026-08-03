# Lesson 2: Appropriate vs Inappropriate Use Cases

## Overview

Appropriateness is a structured governance judgment, not a gut feeling.

The same Delegation criteria used to map workflow steps can screen an entire use case:

1. reversibility;
2. consequence of error;
3. need for human creativity or empathy; and
4. accountability.

```text
Proposed use case
      ↓
Evaluate all four Delegation criteria
      ↓
Identify the load-bearing criterion
      ↓
Classify the use case
      ↓
Define the human gate or retained role
      ↓
Document the rationale
```

> The goal is not merely to say `yes`, `no`, or `human review`. The goal is to explain why the classification is defensible and what control changes it.

---

# Plain-English explanation

A task may look easy for Claude and still be inappropriate.

A task may also be consequential and still be appropriate when a qualified human reviews it before use.

The decision depends on more than technical capability.

Ask:

- Can a wrong output be caught and undone?
- What happens if it is wrong?
- Does the work require human judgment, empathy, or relationship ownership?
- Who remains answerable for the outcome?

```text
Claude can produce output
      ≠
Claude should own the task
      ≠
Organization may use the output without controls
```

---

# One analogy: load-bearing walls

A building can have many walls, but only some are load bearing.

Removing a decorative wall changes the room. Removing a load-bearing wall changes whether the structure remains safe.

Use-case criteria work the same way.

All four matter, but one may control the classification. If that criterion changed, the use case would move from fully appropriate to human-reviewed, or from human-reviewed to inappropriate.

> Naming the load-bearing criterion makes the decision explainable to a risk, policy, legal, compliance, or business reviewer.

---

# The four Delegation criteria

## 1. Reversibility

Ask:

> Can an incorrect output be detected and undone before it causes harm?

Examples:

- a draft internal FAQ can be edited before publication;
- a draft customer email can be corrected before sending;
- an automated denial already sent to an applicant may be difficult to reverse;
- a final legal filing or medical determination may create consequences before correction is possible.

```text
Reversible before consequence
      ↓
Lower delegation barrier

Irreversible or difficult to remedy
      ↓
Higher delegation barrier
```

Reversibility is not only whether something can technically be changed. It includes whether the harm, relationship damage, lost opportunity, or legal effect can realistically be repaired.

## 2. Consequence of error

Ask:

> What is the cost if the output is wrong?

Consider:

- physical harm;
- financial loss;
- legal or regulatory exposure;
- unfair treatment;
- reputational damage;
- loss of access or opportunity;
- privacy harm;
- operational disruption; and
- harm to trust or relationships.

Higher consequence generally requires stronger evidence, deterministic checks, qualified review, or rejection of the use case.

```text
Low consequence
      ≠
No review needed in every case
```

A low-consequence task may still require human ownership because of empathy, relationship, or accountability.

## 3. Need for human creativity or empathy

Ask:

> Does the task depend on judgment, care, relationship, lived context, or empathy that a person must supply?

Examples include:

- condolence messages;
- sensitive performance discussions;
- conflict resolution;
- pastoral or therapeutic relationships;
- negotiations involving trust;
- decisions requiring contextual professional judgment; and
- communications where authenticity itself matters.

Claude may help generate options or a first draft, but the human role may remain load bearing.

```text
AI assistance
      ≠
Human relationship delegated
```

## 4. Accountability

Ask:

> Who is answerable for the outcome, and can that person meaningfully exercise accountability over the AI-assisted result?

Accountability requires more than being named after the fact.

The accountable role needs:

- authority;
- expertise;
- access to evidence;
- time to review;
- clear criteria;
- ability to reject or modify the output;
- visibility before consequence; and
- an escalation path.

```text
Accountability named
      ≠
Accountability exercised
```

A model cannot accept legal, professional, managerial, or organizational accountability.

---

# The criteria interact

The four criteria are not a checklist where one unfavorable answer always ends the analysis.

A reversible, low-consequence task may still need a person because the human element is central.

A high-consequence task may still be usable with AI assistance when:

- the AI contribution is bounded;
- evidence is available;
- exact calculations are verified;
- a qualified reviewer examines the relevant risk;
- review occurs before use; and
- the human retains authority.

```text
Run all four criteria
      ↓
Identify which criterion controls the classification
      ↓
Design around that criterion
```

## The load-bearing criterion

The load-bearing criterion is the one that would change the classification if it changed.

Examples:

- A condolence-note draft may be reversible and low consequence, but the human relationship requirement is load bearing.
- A financial summary may be consequential, but accountability becomes manageable when a named reviewer validates it before use.
- A final professional determination may remain inappropriate because non-transferable professional accountability and irreversibility are load bearing.

Record the load-bearing criterion in the decision rationale.

---

# Three classifications

## 1. Fully appropriate

Use when the task is:

- reversible;
- low consequence;
- supported by suitable evidence;
- not dependent on special human empathy or authority; and
- subject to normal quality review.

Example:

> Draft an internal FAQ from approved policy documents.

The output can be checked and corrected before internal use, and the source boundary is clear.

## 2. Appropriate with human review

Use when AI assistance is useful but a human gate is required because of:

- consequence;
- fairness;
- policy exposure;
- relationship sensitivity;
- professional judgment;
- external communication; or
- retained accountability.

The classification is incomplete until the gate is defined.

## 3. Inappropriate

Use when the AI role cannot be made responsible through bounded assistance and meaningful human control.

Indicators include:

- irreversible or difficult-to-remedy harm;
- non-transferable professional responsibility;
- a prohibited or disallowed use;
- no qualified reviewer;
- no realistic pre-use review;
- unacceptable fairness or privacy risk;
- essential human care or relationship ownership; or
- consequences too severe for the proposed control model.

The decision should name the human role that must retain the work.

---

# The human gate is part of the classification

`Appropriate with human review` does not mean:

```text
Someone will check it.
```

A defined gate states:

| Gate element | Required question |
|---|---|
| Who | Which accountable role reviews? |
| What | Which specific risks, facts, or criteria are verified? |
| When | At what point before use or consequence does review occur? |

A strong gate also records:

- evidence available to the reviewer;
- authority to reject or modify;
- exception and escalation path; and
- retained approval evidence.

## Weak gate

```text
A human remains in the loop.
```

## Defined gate

```text
Before any candidate is contacted, the hiring manager reviews the proposed shortlist for job-related evidence, unsupported inferences, and adverse-impact patterns, then approves or rejects each recommendation.
```

```text
Human review label
      ≠
Operational human gate
```

If the who, what, and when cannot be stated, the use case is not ready to run.

---

# Worked use-case portfolio

## Case 1: Draft an internal FAQ from approved policy documents

**Classification:** Fully appropriate.

**Reasoning:**

- reversible before publication;
- low consequence;
- factual source boundary is available;
- no special human-empathy requirement;
- normal owner review remains possible.

**Load-bearing criterion:** Reversibility and low consequence support normal delegation.

## Case 2: Summarize candidate resumes into a proposed shortlist

**Classification:** Appropriate with human review, subject to policy and fairness controls.

**Reasoning:**

- the task affects employment opportunity;
- bias and unsupported inference are material risks;
- accountability remains with the hiring organization;
- the output must remain a proposal, not a final selection.

**Load-bearing criterion:** Accountability and consequence of error.

**Gate:**

- **Who:** Authorized hiring manager or qualified recruiting reviewer.
- **What:** Job-related evidence, unsupported inference, consistency, fairness, and policy compliance.
- **When:** Before any applicant is rejected, ranked, or contacted based on the shortlist.

## Case 3: Generate a final medical or legal determination

**Classification:** Inappropriate for AI ownership.

**Reasoning:**

- consequences may be severe and difficult to reverse;
- professional judgment is required;
- accountability cannot transfer to the model;
- the professional must make and own the determination.

**Load-bearing criterion:** Non-transferable accountability, reinforced by consequence and irreversibility.

**Retained role:** Qualified medical or legal professional.

AI may support bounded research, summarization, or drafting where policy permits, but it does not own the final determination.

## Case 4: Draft customer-facing responses to billing complaints

**Classification:** Appropriate with human review.

**Reasoning:**

- a draft is reversible before sending;
- an incorrect statement about money can damage trust or create regulatory exposure;
- tone and relationship handling matter;
- the company remains accountable for the response.

**Load-bearing criterion:** Accountability.

**Gate:**

- **Who:** Authorized support agent.
- **What:** Accuracy against the account record, applicable billing policy, required disclosures, and tone.
- **When:** Before the response is sent.

---

# Defensible rationale format

Use this structure:

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

This converts `it feels risky` into a reviewable governance decision.

---

# Common failure modes

## 1. Capability-first approval

**Failure:** The use is approved because Claude can produce a plausible output.

**Repair:** Evaluate consequence, reversibility, human element, and accountability.

## 2. Human-in-the-loop theater

**Failure:** Human review is named without a reviewer, criteria, timing, or authority.

**Repair:** Define the who, what, and when gate.

## 3. Treating one criterion as the whole analysis

**Failure:** A reversible task is assumed fully appropriate despite fairness or relationship concerns.

**Repair:** Run all four criteria and identify the load-bearing one.

## 4. Accountability assigned to the model

**Failure:** The workflow describes Claude as responsible for the decision.

**Repair:** Name the accountable human or organizational role and its intervention rights.

## 5. Inappropriate use softened into a draft workflow

**Failure:** A non-transferable final determination is treated as acceptable because Claude only provides a `recommendation` that is routinely accepted.

**Repair:** Preserve real professional judgment and prohibit rubber-stamp review.

## 6. Vague rationale

**Failure:** The decision record says only `high risk` or `use caution`.

**Repair:** Name the criterion, consequence, gate, and retained role.

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

# Exam lens

```text
Low-stakes reversible drafting       → often fully appropriate
Consequential recommendation         → human-reviewed with explicit gate
Essential empathy or relationship    → retain human ownership
Final professional determination     → human professional owns the decision
Human in the loop                    → require who, what, and when
Four criteria conflict               → identify the load-bearing criterion
Accountability assigned to Claude    → invalid; retain human accountability
Feels risky                          → replace with criterion-based rationale
```

For appropriateness scenarios:

1. define the exact use case;
2. run all four Delegation criteria;
3. avoid capability-first reasoning;
4. identify the criterion that controls the classification;
5. preserve non-transferable accountability;
6. define meaningful review before consequence;
7. distinguish AI assistance from AI ownership;
8. state the retained human role;
9. document conditions and escalation; and
10. choose a defensible classification.

---

# Short recap

```text
1. Appropriateness is structured judgment, not intuition.
2. Screen every use case for reversibility, consequence, human element, and accountability.
3. The criteria interact.
4. Name the load-bearing criterion.
5. Fully appropriate uses are low-consequence and reversible.
6. Human-reviewed uses require an explicit gate.
7. A gate defines who reviews, what they verify, and when review occurs.
8. Inappropriate uses retain the human role that owns the consequence.
9. Accountability cannot transfer to a model.
10. A defensible rationale names the criterion, gate, and owner.
```

## Educational-use notice

This lesson is an unofficial educational resource. It does not constitute legal, medical, employment, financial, compliance, ethics, or other professional advice. Use cases and examples are fictional and must be adapted to current law, policy, organizational controls, and qualified professional judgment.
