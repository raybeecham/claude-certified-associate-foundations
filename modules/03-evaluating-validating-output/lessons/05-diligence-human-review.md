# Lesson 5: Diligence — When Human Review Is Non-Negotiable

## Overview

Some AI-assisted outputs must not be released as generated drafts, even when they are polished, well organized, and apparently correct.

Diligence means deciding those review thresholds **before** the output exists. The release rule should come from policy, consequence, evidence, and professional responsibility—not from how impressive the draft looks in the moment.

> Human review is a release control, not a compliment paid to a good draft.

This lesson develops five decisions:

1. how to identify tasks that require human review;
2. how to calibrate review using stakes, reversibility, audience, and regulatory exposure;
3. which output classes should be placed behind fixed do-not-ship gates;
4. when to stop iterating with Claude and escalate to a qualified person; and
5. what meaningful human review must actually include.

---

# Plain-English explanation

Claude can help write, summarize, compare, calculate, and organize information. But Claude cannot accept professional accountability for what you send, file, publish, or act on.

A beginner can decide whether human review is mandatory by asking four questions:

```text
What happens if this is wrong?
          ↓
Can the action be undone?
          ↓
Who will see or rely on it?
          ↓
Does a law, rule, contract, policy, or professional duty govern it?
```

When the possible harm is high, the action is difficult to reverse, the audience is external or powerful, or the work is regulated, a qualified human must review the output before release.

The central idea is:

> The better a draft looks, the easier it may be to forget that appearance does not remove the review requirement.

---

# One analogy: an aircraft preflight check

An aircraft can look ready to fly. The cabin may be clean, the screens may turn on, and the engines may sound normal.

That does not allow the crew to skip the preflight checklist.

Certain checks are mandatory because the cost of a missed problem is too high:

- fuel quantity must be confirmed;
- control surfaces must be checked;
- weather and route conditions must be reviewed;
- maintenance issues must be resolved or formally accepted; and
- authorized people must sign off before departure.

AI-assisted work has similar release gates.

```text
Polished draft
      ≠
Cleared for release
```

An internal brainstorming note may be comparable to moving an aircraft inside a hangar: low consequence and easy to stop.

A filed regulatory report, final client deliverable, or public legal statement is comparable to takeoff: once released, the consequences can be difficult or impossible to reverse.

The lesson is:

> Preflight requirements are based on risk, not on whether the aircraft looks convincing from the gate.

---

# Diligence means precommitting the review rule

A weak workflow asks after generation:

```text
Does this draft look good enough to send?
```

A stronger workflow decides before generation:

```text
What class of output is this?
          ↓
What review gate applies?
          ↓
Who is qualified to review it?
          ↓
What evidence and checks are required?
          ↓
Who has authority to release it?
```

Precommitment prevents three common errors:

1. **fluency bias** — a polished draft receives less scrutiny than policy requires;
2. **deadline bias** — time pressure silently lowers the review standard; and
3. **ownership diffusion** — everyone assumes someone else checked the important parts.

A review policy should be attached to the **use case**, not improvised for each individual output.

---

# The four risk thresholds

## Threshold 1: Stakes

Ask:

> What is the cost if this output is wrong, incomplete, misleading, or misused?

Possible consequences include:

- financial loss;
- legal exposure;
- regulatory findings;
- safety harm;
- denial of benefits or services;
- reputational damage;
- breach of contract;
- incorrect executive decisions;
- loss of client trust; and
- downstream rework.

### Review rule

```text
Higher consequence of error
          ↓
Stronger evidence, validation, and human review
```

High-cost errors require human review even when the output appears highly confident and cites sources.

### Beginner example

A typo in a private brainstorming note may have almost no consequence. A wrong revenue figure in a board presentation may change a decision and become part of the official record.

The prose could look equally polished in both cases. The stakes are not equal.

---

## Threshold 2: Reversibility

Ask:

> If this is wrong, can we undo the action easily and completely?

### More reversible

- an unsent draft;
- an internal working note;
- a sandbox calculation;
- a proposed agenda;
- a private list of brainstorming ideas; and
- a recommendation that has not triggered action.

### Less reversible

- a sent client deliverable;
- a filed report;
- a public statement;
- a signed agreement;
- an employment or benefits decision;
- a payment or transfer;
- deletion or modification of records;
- a production change; and
- a communication that affects legal rights or obligations.

### Review rule

```text
Harder to reverse
      ↓
Higher release threshold
```

A draft that can be corrected before anyone relies on it does not require the same control as an external action that creates lasting consequences.

---

## Threshold 3: Audience

Ask:

> Who will see, rely on, or act on the output?

Audience changes the review requirement.

| Audience | Typical posture |
|---|---|
| Individual working notes | Light, proportionate review |
| Internal peer discussion | Requirement and obvious-error review |
| Management or executive audience | Stronger evidence, clarity, and completeness review |
| Client or partner | Formal human review and approval |
| Public audience | Publication, legal, brand, and factual review as applicable |
| Regulator, auditor, court, or oversight body | Qualified review, authoritative evidence, and documented approval |

### Review rule

```text
Wider or more authoritative audience
               ↓
Stronger review and approval requirements
```

An output that is appropriate as an internal discussion starter may be unacceptable as a final client or regulatory deliverable.

---

## Threshold 4: Regulatory exposure

Ask:

> Does a law, regulation, contract, policy, standard, or professional duty govern this output or its use?

Regulatory exposure includes more than formal government filings. It may also arise from:

- contractual reporting duties;
- audit requirements;
- financial-control procedures;
- privacy and data-handling rules;
- records-retention requirements;
- accessibility obligations;
- industry standards;
- professional licensing duties;
- security controls; and
- organizational approval policies.

### Review rule

```text
Governed use case
      ↓
Apply the controlling rule and required reviewer
```

AI assistance does not remove or dilute the governing obligation.

A model cannot grant legal authority, professional approval, or policy compliance to its own output.

---

# Risk posture: green, yellow, and red

The four thresholds should not be reduced to a simplistic score. A single severe condition can require escalation.

A useful qualitative model is:

| Posture | Typical characteristics | Review action |
|---|---|---|
| **Green** | Low stakes, reversible, internal, unregulated | Proportionate self-review or peer check |
| **Yellow** | Material decision support, management audience, partial external use, moderate consequence | Structured evidence review and identified human approver |
| **Red** | High stakes, hard to reverse, external or regulatory audience, sensitive or controlled domain | Qualified human review is mandatory before release |

> The most severe applicable threshold controls the release gate.

Do not average a red condition away because the other three appear low risk.

---

# The do-not-ship-without-review list

The preparation material identifies four classes that should be placed behind fixed human-review gates.

## 1. Final client deliverables

Examples:

- final presentations;
- formal recommendations;
- assessments;
- reports;
- contractual deliverables;
- externally shared analyses; and
- client communications that represent an organizational position.

Required controls may include:

- factual and source verification;
- completeness review;
- brand and tone review;
- subject-matter review;
- confidentiality review;
- approval by the accountable owner; and
- confirmation that calculations and citations are reproducible.

## 2. Audit-critical or financially material calculations

Examples:

- financial statements;
- forecasts used for decisions;
- pricing models;
- material budgets;
- audit schedules;
- regulatory financial reports;
- cost or savings claims; and
- calculations used to authorize payment.

Required controls may include:

```text
Authoritative inputs
        ↓
Reproducible formula or code
        ↓
Independent recalculation
        ↓
Variance reconciliation
        ↓
Qualified financial or control review
        ↓
Approval
```

Fluent explanation does not validate arithmetic.

## 3. Regulated, confidential, or highly sensitive data

Examples may include:

- personal information;
- protected health information;
- controlled government information;
- privileged legal material;
- trade secrets;
- nonpublic financial data;
- security-sensitive architecture;
- credentials and secrets; and
- regulated research or case records.

Human review must confirm both the **content** and the **handling process**:

- was use authorized;
- was the correct environment selected;
- was access limited appropriately;
- were retention and disclosure rules followed;
- was sensitive content minimized; and
- is the intended recipient authorized to receive it?

A factually correct answer can still be unsafe because the data was handled or disclosed improperly.

## 4. Public or legal communications with lasting consequences

Examples:

- press statements;
- public incident communications;
- legal notices;
- contract positions;
- statements to regulators;
- testimony or declarations;
- public claims about performance or compliance; and
- communications that may create reliance or waive rights.

These require review by people with the appropriate authority and expertise. Prompt quality does not substitute for legal, communications, executive, compliance, or policy approval.

---

# Engineering extension: additional common mandatory-review gates

Organizations often add fixed review gates for:

- safety-critical recommendations;
- medical or benefits decisions;
- employment, promotion, discipline, or hiring decisions;
- security changes with production impact;
- irreversible tool actions;
- decisions affecting access, rights, or eligibility;
- high-impact risk classifications;
- material scientific or technical claims; and
- outputs that combine incomplete evidence with consequential action.

These extensions should be defined by organizational policy and applicable law, not invented by the model during a conversation.

---

# Meaningful human review

Human review is not meaningful merely because a person opened the document or clicked approve.

A qualified review requires the reviewer to have:

1. **Expertise** — enough subject knowledge to detect material errors.
2. **Authority** — the power to approve, reject, or escalate the output.
3. **Context** — understanding of the purpose, audience, and consequences.
4. **Evidence access** — ability to inspect sources, calculations, and records.
5. **Time and attention** — enough capacity to perform more than a surface scan.
6. **Independence where needed** — freedom to challenge the draft and its author.
7. **A defined review standard** — criteria, checklist, or policy against which to judge the output.

```text
Human present
      ≠
Meaningful human review
```

## A meaningful-review record

For material outputs, record:

| Field | Example |
|---| and decision-making.
- **Audience:** Executive.
- **Regulatory or governance exposure:** Material.

### Decision

Recompute the figures and require authorized financial review.

The polished appearance does not affect the gate.

## Scenario C: proposal iteration has plateaued

A team has revised an external proposal five times. The last three rounds change sentence rhythm and minor wording but do not improve the argument, evidence, or fit to the client's priorities.

- **Stakes:** Material external deliverable.
- **Reversibility:** Corrections after delivery may damage credibility.
- **Audience:** Client.
- **Iteration signal:** Diminishing returns.

### Decision

Stop prompting. Obtain a fresh review from a colleague with relevant context and authority.

The escalation trigger is the flat improvement curve, not an obvious error.

---

# A pre-release review gate

Use a written gate for material outputs.

## Step 1: Classify the use

Record:

- purpose;
- audience;
- decision or action supported;
- data sensitivity;
- governing requirements; and
- whether the output is draft, advisory, or final.

## Step 2: Assess the thresholds

| Threshold | Low | Material | High |
|---|---|---|---|
| Stakes | Minor inconvenience | Operational or reputational effect | Harm, legal, financial, safety, rights, or major trust effect |
| Reversibility | Easy to edit or discard | Correctable with cost | Difficult or impossible to reverse |
| Audience | Private or small internal | Management, partner, or limited external | Executive, client, public, legal, audit, or regulator |
| Regulatory exposure | None identified | Policy or contractual controls | Legal, regulatory, licensed, audit, or mandatory obligations |

## Step 3: Apply automatic gates

Check whether the output falls into a do-not-ship category.

## Step 4: Define the required reviewer

Record:

- name or role;
- required expertise;
- authority;
- evidence access;
- review scope; and
- approval method.

## Step 5: Complete validation

Examples:

- source audit;
- deterministic recomputation;
- privacy or sensitivity check;
- bias and completeness review;
- professional-standard check;
- external-state confirmation; and
- conflict or uncertainty resolution.

## Step 6: Record disposition

```text
Release
Edit and re-review
Verify additional claims
Escalate
Reject
```

## Step 7: Preserve evidence

Where required, retain:

- reviewed version;
- source package;
- calculations;
- reviewer comments;
- approval record;
- known limitations; and
- release date and audience.

---

# Review policy template

```text
Output category:
[DESCRIPTION]

Intended use and audience:
[USE AND AUDIENCE]

Risk thresholds:
- Stakes: Low / Material / High
- Reversibility: Low / Material / High
- Audience: Low / Material / High
- Regulatory exposure: Low / Material / High

Automatic review gate triggered:
[YES / NO AND WHY]

Required reviewer:
[ROLE, EXPERTISE, AUTHORITY]

Required validation:
[SOURCES, CALCULATIONS, PRIVACY, BIAS, PROFESSIONAL STANDARDS]

Prohibited action before approval:
[DO NOT SEND / FILE / PUBLISH / EXECUTE / DELETE / APPROVE]

Approval evidence:
[RECORD OR SYSTEM OF RECORD]

Disposition:
[RELEASE / EDIT / VERIFY / ESCALATE / REJECT]
```

---

# Common anti-patterns

## Anti-pattern 1: Review only when the draft looks wrong

**Failure:** Fluent high-risk errors bypass review.

**Repair:** Trigger review from precommitted risk thresholds.

## Anti-pattern 2: Treating citations as sufficient for high-stakes release

**Failure:** Traceability is mistaken for correctness, calculation validity, or approval.

**Repair:** Add independent verification and qualified review.

## Anti-pattern 3: Rubber-stamp human review

**Failure:** A reviewer is present but lacks time, expertise, evidence, or authority.

**Repair:** Define reviewer qualifications and intervention rights.

## Anti-pattern 4: Averaging the risk thresholds

**Failure:** One decisive high-risk condition is diluted by several low-risk conditions.

**Repair:** Use the highest credible consequence and automatic gates.

## Anti-pattern 5: Escalating every AI-assisted output

**Failure:** Low-stakes routine work loses the efficiency benefit.

**Repair:** Use proportionate review and preserve mandatory gates for material work.

## Anti-pattern 6: Iterating after authority or evidence has run out

**Failure:** Additional prompts create cosmetic variation but cannot resolve the real gap.

**Repair:** Obtain the missing evidence, fix the workflow, or escalate to a qualified owner.

## Anti-pattern 7: Reviewing after the irreversible action

**Failure:** The output is sent, filed, published, or executed before approval.

**Repair:** Place the gate technically and procedurally before the action.

## Anti-pattern 8: Transferring accountability to the model

**Failure:** The author treats AI origin as an excuse for an unsupported or harmful output.

**Repair:** Assign a named human or organizational owner for release.

---

# Exam reasoning pattern

For Diligence and human-review scenarios:

1. identify the intended use and audience;
2. evaluate stakes, reversibility, audience, and regulatory exposure;
3. check for an automatic do-not-ship category;
4. distinguish traceability from verification and approval;
5. determine what reviewer expertise and authority are required;
6. place the review before any irreversible action;
7. use deterministic verification for material calculations;
8. stop iterating when the remaining gap is evidence, authority, or professional judgment;
9. preserve accountability with the releasing human or organization; and
10. choose release, edit, verify, escalate, or reject.

```text
Low-stakes internal draft        → proportionate review
Final client deliverable         → qualified review
Audit-critical calculation       → deterministic verification + finance review
Regulated or sensitive content   → policy controls + authorized review
Public or legal communication    → qualified review before release
Iteration improvement has stalled → escalate for fresh human judgment
Irreversible action              → approval gate before execution
```

Do not choose `send because it looks accurate` when the risk thresholds require review.

---

# Knowledge check

## Question 1

Why should mandatory-review categories be defined before the draft is created?

**Answer:** Precommitment prevents deadline pressure, confidence, convenience, or polished wording from weakening the review standard at release time.

## Question 2

A final client report is well cited and contains no visible errors. Does it still require human review?

**Answer:** Yes. Final external use triggers a review gate because citations and polish do not establish complete correctness, professional fitness, or release authority.

## Question 3

What is the difference between reversibility and stakes?

**Answer:** Stakes measure the consequence if the output is wrong. Reversibility measures whether the resulting action or communication can be effectively undone.

## Question 4

What makes human review meaningful?

**Answer:** The reviewer has relevant expertise, authority, context, evidence access, adequate time, independence, and the ability to change or stop the output.

## Question 5

When should iteration stop and escalation begin?

**Answer:** When improvement has plateaued or the remaining gap requires unavailable evidence, authority, professional expertise, or a consequential judgment that prompting cannot supply.

## Question 6

Why is `reviewed by a human` an incomplete control description?

**Answer:** It does not identify what was reviewed, whether the reviewer was qualified, what evidence was available, or whether the person could intervene.

## Question 7

Can a low-stakes output be used quickly without specialist escalation?

**Answer:** Yes. Diligence requires proportionate review, not universal escalation. Routine internal, reversible, non-regulated work can often proceed after a basic check.

## Question 8

Who owns an AI-assisted output after release?

**Answer:** The human or organization that approves, sends, publishes, or acts on it retains accountability.

---

# Flashcards

## Flashcard 1

**Q:** What are the four Diligence thresholds?

**A:** Stakes, reversibility, audience, and regulatory, contractual, or policy exposure.

## Flashcard 2

**Q:** What is the precommitment rule?

**A:** Define mandatory-review categories before the draft and before delivery pressure arises.

## Flashcard 3

**Q:** What outputs should never rely on a Claude draft alone?

**A:** Final external deliverables, audit-critical or material calculations, regulated or highly sensitive work, public or legal communications, consequential decisions affecting people, and irreversible actions.

## Flashcard 4

**Q:** What makes human review substantive?

**A:** Expertise, authority, context, evidence access, adequate time, independence, and the ability to intervene.

## Flashcard 5

**Q:** What does a flat improvement curve signal?

**A:** Prompt iteration may have reached diminishing returns and the work may need fresh human judgment or missing evidence.

## Flashcard 6

**Q:** Does grounding remove the need for human review?

**A:** No. Grounding improves traceability; consequential release may still require independent verification and qualified approval.

## Flashcard 7

**Q:** When must the review gate occur?

**A:** Before the irreversible send, filing, publication, approval, deletion, or system action.

## Flashcard 8

**Q:** Who retains accountability for released AI-assisted work?

**A:** The human or organization that releases or acts on it.

---

# Short recap

```text
1. Decide review thresholds before release pressure appears.
2. Check stakes, reversibility, audience, and governing obligations.
3. Use fixed do-not-ship categories for consequential outputs.
4. Require reviewers with expertise, authority, evidence, time, and intervention rights.
5. Put the gate before the irreversible action.
6. Iterate only while the remaining problem is prompt-fixable.
7. Escalate when evidence, authority, expertise, or improvement has run out.
8. Keep accountability with the releasing human or organization.
9. Use proportionate review for routine low-stakes work.
10. Record the disposition and approval evidence.
```

The central rule is:

> Review depth follows consequence, not confidence. When the cost of error, difficulty of reversal, audience, or governing obligations cross the threshold, qualified human review is mandatory.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, medical, compliance, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was dated June 2026. Supporting product and evaluation guidance was rechecked against official Anthropic sources on **August 2, 2026**.

Official references:

- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)

Anthropic's current Help Center notes that Claude for Excel is not recommended for final client deliverables without human review, audit-critical calculations without verification, replacing financial judgment, or highly sensitive and regulated models without appropriate controls. Product features and guidance can change; verify current official documentation and organizational policy before implementation.

## Related material

- [Fact-Checking and Grounding Techniques](04-fact-checking-grounding.md)
- [Hallucinations, Inconsistencies, and Bias](03-hallucinations-inconsistencies-bias.md)
- [Module 3 overview](../README.md)
- [Diligence and Human Review prompt notebook](../../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Human Review Gate Pattern](../../../patterns/human-review-gate-pattern.md)
- [Grounded Verification Pattern](../../../patterns/grounded-verification-pattern.md)
- [Governance Canvas](../../../ai-systems-engineering/worksheets/governance-canvas.md)
