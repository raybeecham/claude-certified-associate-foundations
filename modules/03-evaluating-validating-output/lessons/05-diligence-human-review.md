# Lesson 5: Diligence — When Human Review Is Non-Negotiable

## Overview

Some AI-assisted outputs must not be released as generated drafts, even when they are polished, well organized, and apparently correct.

Diligence means deciding those review thresholds **before** the output exists. The release rule should come from policy, consequence, evidence, and professional responsibility—not from how impressive the draft looks in the moment.

> Human review is a release control, not a compliment paid to a good draft.

This lesson develops five decisions:

1. how to identify tasks that require human review;
2. how to calibrate review using stakes, reversibility, audience, and regulatory exposure;
3. which output classes belong behind fixed do-not-ship gates;
4. when to stop iterating with Claude and escalate to a qualified person; and
5. what meaningful human review must actually include.

---

# Plain-English explanation

Claude can help write, summarize, compare, calculate, and organize information. But Claude cannot accept professional accountability for what you send, file, publish, approve, or act on.

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

An internal brainstorming note is comparable to moving an aircraft inside a hangar: low consequence and easy to stop.

A filed regulatory report, final client deliverable, or public legal statement is comparable to takeoff: once released, the consequences may be difficult or impossible to reverse.

> Preflight requirements are based on risk, not on whether the aircraft looks convincing from the gate.

---

# Precommit the review rule

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

Precommitment reduces:

- **fluency bias:** polished output receives less scrutiny than policy requires;
- **deadline bias:** time pressure silently lowers the standard; and
- **ownership diffusion:** everyone assumes someone else checked the important parts.

The review rule should attach to the **use case**, not be improvised for each output.

---

# The four risk thresholds

## Threshold 1: Stakes

Ask:

> What is the cost if this output is wrong, incomplete, misleading, or misused?

Possible consequences include:

- financial loss;
- legal or regulatory exposure;
- safety harm;
- denial of rights, benefits, or services;
- breach of contract;
- reputational damage;
- incorrect executive decisions;
- loss of client trust; and
- downstream rework.

```text
Higher consequence of error
          ↓
Stronger evidence, validation, and human review
```

High-cost errors require human review even when the output sounds confident and contains citations.

## Threshold 2: Reversibility

Ask:

> If this is wrong, can the communication or action be undone easily and completely?

### More reversible

- an unsent draft;
- an internal working note;
- a sandbox calculation;
- a proposed agenda;
- a private brainstorm; and
- a recommendation that has not triggered action.

### Less reversible

- a sent client deliverable;
- a filed report;
- a public statement;
- a signed position;
- a payment or transfer;
- deletion or alteration of official records;
- a production change; and
- a decision affecting rights, access, employment, benefits, or eligibility.

```text
Harder to reverse
      ↓
Higher release threshold
```

## Threshold 3: Audience

Ask:

> Who will see, rely on, approve, or act on the output?

| Audience | Typical review posture |
|---|---|
| Private working notes | Light, proportionate review |
| Internal peer discussion | Requirement and obvious-error review |
| Management or executive | Stronger evidence, clarity, and completeness review |
| Client or partner | Formal human review and approval |
| Public audience | Publication, legal, brand, and factual review as applicable |
| Regulator, auditor, court, or oversight body | Qualified review, authoritative evidence, and documented approval |

```text
Wider or more authoritative audience
               ↓
Stronger review and approval requirements
```

## Threshold 4: Regulatory exposure

Ask:

> Does a law, regulation, contract, policy, standard, or professional duty govern this output or its use?

Exposure may arise from:

- contractual reporting duties;
- audit and financial-control procedures;
- privacy and data-handling rules;
- records-retention requirements;
- accessibility obligations;
- industry standards;
- professional licensing duties;
- security controls; and
- organizational approval policy.

```text
Governed use case
      ↓
Apply the controlling rule and required reviewer
```

AI assistance does not remove the governing obligation. A model cannot grant legal authority, professional approval, or policy compliance to its own output.

---

# Risk posture: green, yellow, and red

Do not reduce the thresholds to a simplistic average. One severe condition can control the gate.

| Posture | Typical characteristics | Review action |
|---|---|---|
| **Green** | Low stakes, reversible, internal, unregulated | Proportionate self-review or peer check |
| **Yellow** | Material decision support, management audience, partial external use, moderate consequence | Structured evidence review and identified human approver |
| **Red** | High stakes, hard to reverse, external or regulatory audience, sensitive or controlled domain | Qualified human review is mandatory before release |

> The most severe credible threshold controls the minimum review requirement.

---

# The do-not-ship-without-review list

The course-aligned core identifies four fixed classes.

## 1. Final client deliverables

Examples include final reports, presentations, formal recommendations, assessments, contractual deliverables, and externally shared analyses.

Typical controls:

- requirement coverage;
- factual and source verification;
- completeness review;
- calculation reproducibility;
- confidentiality review;
- subject-matter review; and
- approval by the accountable owner.

## 2. Audit-critical or financially material calculations

Examples include financial statements, forecasts, pricing models, audit schedules, regulatory reports, material budgets, and calculations used to authorize payment.

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

Examples may include personal information, protected health information, controlled government information, privileged legal material, trade secrets, nonpublic financial data, security-sensitive architecture, credentials, and regulated case records.

Human review must confirm both content and handling:

- authorized use;
- approved environment;
- least-necessary data scope;
- access restrictions;
- retention and disclosure requirements;
- recipient authorization; and
- required logging or traceability.

A factually correct answer can still be unsafe because the data was handled or disclosed improperly.

## 4. Public or legal communications with lasting consequences

Examples include press statements, public incident communications, legal notices, contract positions, statements to regulators, testimony, compliance claims, and communications that may create reliance or waive rights.

Prompt quality does not substitute for legal, communications, executive, compliance, or policy approval.

## Engineering extension

Organizations commonly add mandatory gates for:

- safety-critical recommendations;
- medical or benefits decisions;
- hiring, promotion, discipline, or employment decisions;
- production-impacting security changes;
- irreversible tool actions;
- decisions affecting access, rights, or eligibility; and
- outputs that combine incomplete evidence with consequential action.

These gates should be established by organizational policy and applicable law, not invented by the model during a conversation.

---

# Meaningful human review

Human review is not meaningful merely because a person opened the document or clicked approve.

A qualified reviewer needs:

1. **Expertise** to detect material errors.
2. **Authority** to approve, reject, or escalate.
3. **Context** about purpose, audience, and consequence.
4. **Evidence access** to sources, calculations, and records.
5. **Time and attention** for more than a surface scan.
6. **Independence where needed** to challenge the draft.
7. **A defined standard** such as criteria, a checklist, or policy.
8. **Intervention rights** before release or action.

```text
Human present
      ≠
Meaningful human review
```

## Meaningful-review record

| Field | Example content |
|---|---|
| Output and version | Report v1.4 |
| Intended use | Final client decision briefing |
| Reviewer | Named role or person |
| Reviewer qualifications | Domain expertise and approval authority |
| Evidence reviewed | Source package, calculations, claim ledger |
| Material changes | Corrected figure, added condition, narrowed conclusion |
| Unresolved limitations | Missing source, conflicting evidence, unknown assumption |
| Disposition | Release / Edit / Verify / Escalate / Reject |
| Approval record | Workflow approval, signed review, ticket, or system record |

---

# Accountability stays with the releasing human or organization

```text
Model assists
      ↓
Human validates and approves
      ↓
Organization releases and owns the consequences
```

When you approve, send, publish, file, or act on AI-assisted work, you adopt the output for that use.

The model does not become the accountable author, approver, regulated professional, or decision owner.

---

# Iteration versus escalation

Prompt iteration is useful while the remaining defect is prompt-fixable.

## Continue iterating when

- the failed component is known;
- relevant evidence is available;
- one targeted change is likely to help;
- each round produces measurable improvement;
- no mandatory review gate is being bypassed; and
- consequences remain contained.

## Escalate when

- the last rounds produce only cosmetic changes;
- the same defect persists;
- new rounds introduce regressions;
- the required evidence is unavailable;
- the model lacks authority;
- professional interpretation or accountable judgment is required;
- the output belongs to a mandatory-review class; or
- an irreversible action is approaching.

```text
Prompt problem     → targeted iteration
Evidence problem   → obtain evidence
Tool problem       → repair workflow
Authority problem  → escalate
Judgment problem   → qualified human review
```

More prompting cannot manufacture missing authority, unavailable evidence, or professional accountability.

## Flat improvement curve

Track improvement against acceptance criteria rather than the number of words changed.

```text
Round 1 → major substantive gain
Round 2 → useful correction
Round 3 → small improvement
Round 4 → cosmetic change
Round 5 → cosmetic change or regression
```

When the curve flattens, the right next step may be a fresh reviewer rather than another prompt.

---

# Three escalation scenarios

## Scenario A: the fast yes

Claude drafts a private internal agenda for a routine meeting.

- **Stakes:** Low.
- **Reversibility:** Easy to edit.
- **Audience:** Internal.
- **Regulatory exposure:** None identified.

### Decision

Perform a basic check and use it. Specialist escalation would be disproportionate.

Diligence does not mean sending every low-risk draft to an expert.

## Scenario B: the deceptive looks-fine output

Claude produces a clean financial summary for a board presentation.

- **Stakes:** High because the figures influence governance and decisions.
- **Reversibility:** Correction after presentation may not undo reliance.
- **Audience:** Executive or board.
- **Regulatory or control exposure:** Material.

### Decision

Recompute material figures deterministically and require authorized financial review.

The clean appearance is irrelevant to the gate.

## Scenario C: the slow creep

A team has revised an external proposal five times. Rounds three through five change wording but do not improve evidence, argument quality, or fit to the client's priorities.

- **Stakes:** Material external deliverable.
- **Reversibility:** Errors may damage trust after delivery.
- **Audience:** Client.
- **Iteration signal:** Diminishing returns.

### Decision

Stop prompting and obtain a fresh review from a colleague with relevant context and authority.

The escalation signal is the flat improvement curve, not a visible factual error.

---

# Practical example: board-deck financial summary

## Generated draft

```text
Operating costs declined 14% year over year, producing $3.2 million in annualized savings. The program is on track to exceed its full-year target.
```

The slide is concise, visually clean, and internally coherent.

## Diligence review

### Stakes

The figures affect executive oversight and resource decisions.

**Result:** High.

### Reversibility

The deck can be edited before presentation, but reliance during the meeting may be difficult to undo.

**Result:** Material to High.

### Audience

Board or executive audience.

**Result:** High.

### Regulatory or control exposure

The figures may connect to governed financial reporting or internal controls.

**Result:** Material to High.

## Required gate

1. Trace the inputs to the authoritative workbook or ledger.
2. Recompute the 14% reduction and $3.2 million savings deterministically.
3. Check whether `annualized` assumptions are valid.
4. Verify the full-year target and time period.
5. Review the narrative for unsupported certainty.
6. Obtain qualified financial and accountable-owner approval.

## Disposition

```text
Verify and escalate before release.
```

A polished slide cannot pass this gate on appearance alone.

---

# Pre-release review gate

## Step 1: Classify the use

Record purpose, audience, decision, data sensitivity, governing requirements, and whether the output is draft, advisory, or final.

## Step 2: Assess the thresholds

| Threshold | Low | Material | High |
|---|---|---|---|
| Stakes | Minor inconvenience | Operational or reputational effect | Harm, legal, financial, safety, rights, or major trust effect |
| Reversibility | Easy to edit or discard | Correctable with cost | Difficult or impossible to reverse |
| Audience | Private or small internal | Management, partner, or limited external | Executive, client, public, legal, audit, or regulator |
| Regulatory exposure | None identified | Policy or contractual controls | Legal, regulatory, licensed, audit, or mandatory obligations |

## Step 3: Apply automatic gates

Check whether the output belongs to a do-not-ship category.

## Step 4: Define the reviewer

Record role, expertise, authority, evidence access, review scope, and approval method.

## Step 5: Complete validation

Possible checks include source audit, deterministic recomputation, privacy review, completeness and bias review, professional-standard review, and external-state confirmation.

## Step 6: Record disposition

```text
Release
Edit and re-review
Verify additional claims
Escalate
Reject
```

## Step 7: Preserve evidence

Where required, retain the reviewed version, source package, calculations, reviewer comments, approval record, known limitations, release date, and audience.

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

## Review only when the draft looks wrong

**Failure:** Fluent high-risk errors bypass review.

**Repair:** Trigger review from precommitted use-case rules.

## Treating citations as sufficient

**Failure:** Traceability is mistaken for correctness, calculation validity, professional fitness, or approval.

**Repair:** Add independent validation and qualified review.

## Rubber-stamp review

**Failure:** The reviewer lacks expertise, evidence, time, authority, or intervention rights.

**Repair:** Define reviewer qualifications and required actions.

## Averaging away a red condition

**Failure:** One decisive high-risk threshold is diluted by several low-risk conditions.

**Repair:** Use the highest credible consequence and automatic gates.

## Escalating every output

**Failure:** Low-stakes work loses the efficiency benefit.

**Repair:** Use proportionate review for green work.

## Iterating after evidence or authority runs out

**Failure:** Additional prompts create cosmetic variation but cannot resolve the real gap.

**Repair:** Obtain evidence, repair the workflow, or escalate.

## Reviewing after the irreversible action

**Failure:** The output is sent, filed, published, or executed before approval.

**Repair:** Place the gate technically and procedurally before action.

## Transferring accountability to the model

**Failure:** AI origin is treated as an excuse for an unsupported or harmful result.

**Repair:** Assign a named human or organizational release owner.

---

# Exam reasoning pattern

For Diligence and human-review scenarios:

1. identify intended use and audience;
2. evaluate stakes, reversibility, audience, and regulatory exposure;
3. check for an automatic do-not-ship category;
4. distinguish traceability from verification and approval;
5. determine reviewer expertise and authority;
6. place review before irreversible action;
7. use deterministic checks for material calculations;
8. stop iterating when the blocker is evidence, authority, expertise, or professional judgment;
9. preserve accountability with the releasing human or organization; and
10. choose release, edit, verify, escalate, or reject.

```text
Low-stakes internal draft         → proportionate review
Final client deliverable          → qualified review
Audit-critical calculation        → deterministic verification + finance review
Regulated or sensitive content    → policy controls + authorized review
Public or legal communication     → qualified review before release
Iteration improvement has stalled → fresh human judgment
Irreversible action               → approval gate before execution
```

---

# Knowledge check

## Question 1

Why define mandatory-review categories in advance?

**Answer:** Precommitment prevents deadlines, convenience, confidence, or polished wording from weakening the standard at release time.

## Question 2

A final client report is well cited and has no visible errors. Does it still require human review?

**Answer:** Yes. Final external use triggers the gate because citations and polish do not establish complete correctness, professional fitness, or release authority.

## Question 3

What is the difference between stakes and reversibility?

**Answer:** Stakes measure the consequence if the output is wrong. Reversibility measures whether the resulting action or communication can be effectively undone.

## Question 4

What makes review meaningful?

**Answer:** The reviewer has relevant expertise, authority, context, evidence access, adequate time, independence, and the ability to change or stop the output.

## Question 5

When should iteration stop?

**Answer:** When improvement plateaus or the remaining gap requires missing evidence, authority, expertise, or accountable professional judgment.

## Question 6

Why is `reviewed by a human` an incomplete control?

**Answer:** It does not identify what was reviewed, whether the reviewer was qualified, which evidence was available, or whether the person could intervene.

## Question 7

Can low-stakes work proceed without specialist escalation?

**Answer:** Yes. Diligence requires proportionate review, not universal escalation.

## Question 8

Who owns an AI-assisted output after release?

**Answer:** The human or organization that approves, sends, publishes, or acts on it.

---

# Flashcards

## Flashcard 1

**Q:** What are the four Diligence thresholds?

**A:** Stakes, reversibility, audience, and regulatory, contractual, policy, or professional exposure.

## Flashcard 2

**Q:** What is the precommitment rule?

**A:** Define mandatory-review categories before the draft and before delivery pressure arises.

## Flashcard 3

**Q:** Which outputs require fixed review gates?

**A:** Final external deliverables, audit-critical or material calculations, regulated or highly sensitive work, public or legal communications, consequential decisions, and irreversible actions.

## Flashcard 4

**Q:** What makes human review substantive?

**A:** Expertise, authority, context, evidence access, time, independence, and intervention rights.

## Flashcard 5

**Q:** What does a flat improvement curve signal?

**A:** Prompt iteration may have reached diminishing returns and the work may need fresh human judgment or missing evidence.

## Flashcard 6

**Q:** Does grounding remove the need for human review?

**A:** No. Grounding improves traceability; consequential release may still require independent verification and qualified approval.

## Flashcard 7

**Q:** When must the gate occur?

**A:** Before the irreversible send, filing, publication, approval, deletion, or system action.

## Flashcard 8

**Q:** Who retains accountability?

**A:** The human or organization that releases or acts on the output.

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

> Review depth follows consequence, not confidence. When the cost of error, difficulty of reversal, audience, or governing obligations cross the threshold, qualified human review is mandatory.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, medical, compliance, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was dated June 2026. Supporting product and evaluation guidance was rechecked against official Anthropic sources on **August 2, 2026**.

Official references:

- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)

Anthropic's current Help Center notes that Claude for Excel is not recommended for final client deliverables without human review, audit-critical calculations without verification, replacing financial judgment, or highly sensitive and regulated models without appropriate controls. Product guidance can change; verify current official documentation and organizational policy before implementation.

## Related material

- [Fact-Checking and Grounding Techniques](04-fact-checking-grounding.md)
- [Hallucinations, Inconsistencies, and Bias](03-hallucinations-inconsistencies-bias.md)
- [Module 3 overview](../README.md)
- [Diligence and Human Review prompt notebook](../../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Human Review Gate Pattern](../../../patterns/human-review-gate-pattern.md)
- [Grounded Verification Pattern](../../../patterns/grounded-verification-pattern.md)
- [Governance Canvas](../../../ai-systems-engineering/worksheets/governance-canvas.md)
