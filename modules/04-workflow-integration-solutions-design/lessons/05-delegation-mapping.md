# Lesson 5: Delegation Mapping

## Overview

Delegation mapping converts a workflow from a list of activities into an explicit responsibility design.

The central question is not:

```text
Where can we use Claude?
```

It is:

```text
For each workflow step, who or what should own the work,
what validation is required, and who retains authority?
```

A strong map assigns each stage to the component best suited for it:

- Claude for bounded interpretation, drafting, classification, and synthesis;
- code execution or deterministic logic for exact calculations and fixed rules;
- Skills for repeatable procedures and formatting conventions;
- tools for controlled retrieval or external actions;
- storage or systems of record for durable state; and
- humans for authority, accountability, professional judgment, exceptions, and irreversible decisions.

> Map the work first. Assign features second.

---

# Plain-English explanation

A workflow can contain several very different kinds of work.

One step may be mechanical and reversible. Another may require professional judgment. Another may perform an exact calculation. Another may send something externally and create a binding consequence.

Treating all four steps the same creates either underuse or over-delegation.

A useful mapping sequence is:

```text
Workflow step
      ↓
What kind of work is this?
      ↓
How reversible is it?
      ↓
What happens if it is wrong?
      ↓
Who owns the decision or consequence?
      ↓
Which component should perform the step?
      ↓
What validation and approval gate is required?
```

The map should make hidden human review visible. A statement such as `AI drafts, human reviews` is not a control unless a qualified reviewer is actually assigned, has the evidence, and has authority to intervene.

---

# One analogy: assigning roles in a surgical team

A surgical team does not assign every task to the most technically capable machine or the fastest person.

Different responsibilities belong to different roles:

- imaging equipment produces measurements;
- software may assist with planning;
- nurses prepare and monitor;
- specialists interpret findings;
- the surgeon makes consequential decisions; and
- documented protocols control handoffs and checks.

A machine performing one step well does not inherit authority over the next step.

Workflow delegation follows the same rule:

```text
Strong performance on Step 1
      ≠
Authority to own Step 2
```

> Capability does not automatically confer accountability.

---

# The three core Delegation criteria

The course examples can be evaluated using three recurring criteria.

## 1. Reversibility

Ask:

- Can the result be easily edited, discarded, or rerun?
- Has the output left the internal workspace?
- Has an official record changed?
- Has money, access, employment status, or a legal obligation been affected?

Reversible preparation work is easier to delegate than an irreversible external action.

## 2. Stakes

Ask:

- What harm follows if the step is wrong?
- Does it affect legal, financial, personnel, safety, compliance, or customer outcomes?
- Could the error propagate into later stages?
- Is the step merely informational, or does another person rely on it?

A low-stakes extraction step may be AI-appropriate. A high-stakes approval normally remains human-controlled.

## 3. Accountability

Ask:

- Who is authorized to make this decision?
- Who must explain and defend it later?
- Who owns exceptions?
- Who can accept the risk?
- Who is responsible for correction?

Accountability does not move to Claude merely because Claude produced a strong draft.

## Combined decision rule

```text
More reversible + lower stakes + bounded task
→ stronger candidate for AI delegation

Less reversible + higher stakes + accountable judgment
→ human-retained or collaborative with a real approval gate
```

These criteria establish the minimum delegation posture. Data sensitivity, evidence quality, policy, contractual obligations, and organizational controls can require stronger safeguards.

---

# Delegation modes

| Mode | Meaning | Typical examples |
|---|---|---|
| **AI-appropriate** | Claude can perform the bounded step, subject to validation | extract clauses, summarize sources, classify against a reviewable taxonomy |
| **AI-appropriate with code execution** | Exact data processing or calculation is executed rather than estimated | compute exposure, reconcile records, validate totals |
| **Collaborative** | Claude prepares work; a human evaluates and decides | draft redline, propose rationale, personalize communication |
| **Human-retained** | Authority, accountability, professional judgment, or irreversible action stays human | approve terms, confirm compensation, sign and send |
| **Deterministic** | Fixed rule, schema, authorization check, or exact logic belongs in code or a rules engine | required-field check, policy threshold, access validation |
| **Tool-owned** | A controlled tool performs a defined external operation | retrieve a record, update a system after approval, send an approved item |
| **Storage-owned** | Durable state and authoritative records remain outside the prompt | workflow status, approved version, audit trail |

A workflow stage may combine modes. For example, Claude can draft, code can calculate, a human can approve, and a tool can execute the approved action.

---

# Map the work before assigning features

The correct order is:

```text
Business outcome
      ↓
Current workflow steps
      ↓
Inputs, decisions, calculations, actions, and consequences
      ↓
Delegation classification
      ↓
Validation and review gates
      ↓
Feature and architecture selection
```

The incorrect order is:

```text
We built a Skill
      ↓
Find a workflow step for it
```

A useful feature does not prove that a step is appropriate for AI.

## Feature assignment after mapping

Once the work is mapped:

- use a **Skill** for repeatable instructions, templates, checklists, and organization-specific procedures;
- use **code execution** for calculations, transformations, reconciliation, and file processing;
- use **Project knowledge and instructions** for stable workflow context;
- use controlled **tools** for retrieval and external actions;
- use **human-review gates** where judgment, authority, or consequence requires them; and
- store durable state and approvals in the appropriate system of record.

Current official guidance describes Skills as reusable folders of instructions, scripts, and resources that Claude loads for relevant specialized tasks. Official code-execution guidance describes a sandboxed environment for calculations, data analysis, file processing, and generated outputs. Product behavior and availability can change.

```text
Configured repeatable procedure
      >
Heroic prompting that depends on memory
```

Consistency from a maintained procedure is useful only when the underlying delegation decision is sound.

---

# Worked map 1: contract review

A fictional business team reviews agreements against an approved company playbook.

| Workflow step | Delegation | Why | Required control |
|---|---|---|---|
| Extract clauses from the contract | AI-appropriate | Mechanical, reversible, low-consequence preparation | Completeness check against the contract |
| Flag departures from the company playbook | AI-appropriate | Reversible comparison against bounded rules | Skill or approved procedure; citations to clause and playbook rule |
| Draft the redline and rationale | Collaborative | Claude can draft; interpretation and negotiation judgment remain human | Lawyer reviews every proposed edit and rationale |
| Approve or reject each change | Human-retained | High stakes and professional accountability | Authorized lawyer approval recorded |
| Compute financial exposure of a penalty clause | AI-appropriate with code execution | Numeric result must be computed from explicit terms | Review formula, units, assumptions, and reconciliation |
| Sign and send | Human-retained | Irreversible, external, and legally binding | Authorized signatory and controlled send action |

## What Claude genuinely contributes

Claude is not limited to producing a summary. It may:

- extract the clause inventory;
- compare wording with the approved playbook;
- identify candidate deviations;
- draft a proposed redline;
- explain the rationale; and
- organize issues by type or severity.

The human still owns:

- legal interpretation;
- negotiation strategy;
- exception approval;
- acceptance of risk;
- final wording; and
- signature and transmission.

```text
Claude does meaningful work
      +
Human retains consequential decisions
      =
Collaborative redesign
```

## Failure prevented by the map

Without an explicit map, a team may reason:

```text
Claude drafted the redline well
      ↓
Claude can probably approve low-risk clauses
```

That is halo delegation. Drafting performance does not establish legal authority or reliable risk acceptance.

---

# Worked map 2: onboarding documents

A fictional People team creates offer letters and onboarding packets from approved templates.

| Workflow step | Delegation | Why | Required control |
|---|---|---|---|
| Pull new-hire details from an approved HR export | AI-appropriate with code execution | Mechanical and reversible, but fields must be exact | Schema validation, required-field check, record-level trace |
| Draft the offer letter from the approved template | AI-appropriate | Reversible draft using controlled content | Skill carries template and required clauses; missing fields remain visible |
| Personalize the welcome note | Collaborative | Claude can draft; manager supplies authentic context and voice | Hiring manager edits and approves |
| Confirm compensation figures match the approved requisition | Human-retained | High stakes and accountable employment decision | Authorized People/compensation reviewer verifies source records |
| Send the signed offer | Human-retained | External, consequential, and difficult to reverse | Authorized sender confirms approved version and recipient |

## Same criteria, different domain

The subject matter is different from contract review, but the pattern remains stable:

```text
Mechanical and reversible preparation → delegate with validation
Drafting and personalization           → collaborative or bounded AI
High-stakes figure confirmation        → human-retained
Irreversible external action           → human-retained
```

Delegation is determined by the nature of the step, not the department name.

---

# A complete delegation map

A useful map should capture more than a single label.

| Field | Purpose |
|---|---|
| Step ID and name | Stable reference to the workflow stage |
| Current owner | Who or what performs it today |
| Input and source | What enters and which source controls |
| Work type | Extraction, synthesis, calculation, judgment, approval, action, or storage |
| Reversibility | Easy, moderate, or difficult to reverse |
| Stakes | Low, material, or high consequence |
| Accountable role | Who owns the result and exceptions |
| Delegation mode | AI, code, collaborative, human, deterministic, tool, or storage |
| Feature assignment | Skill, Project, code execution, tool, or none |
| Validation | What proves the stage result is acceptable |
| Review gate | Who reviews, with what evidence and authority |
| Side effect | What external or durable change can occur |
| Failure path | Retry, fallback, escalation, rollback, or stop |
| Evidence retained | Sources, outputs, approvals, and logs |

## Example row

| Step | Work type | Reversibility | Stakes | Delegation | Validation | Approval |
|---|---|---|---|---|---|---|
| Draft contract redline | Interpretation and drafting | Easy | Material | Collaborative | Clause/playbook trace and completeness review | Lawyer approves every edit |

---

# Recognizing over-delegation

Over-delegation occurs when the workflow gives Claude more authority than the risk profile supports.

Common signals include:

- Claude approves the work it drafted;
- a classification automatically triggers a consequential action;
- an irreversible step has no approval gate;
- a professional decision is framed as a routine content-generation task;
- a numerical estimate is used where an executed calculation is required;
- the human reviewer lacks time, expertise, evidence, or intervention authority; and
- the system treats absence of objection as approval.

## Drafting quality is not permission

```text
High-quality draft
      ≠
Authority to approve
      ≠
Permission to execute
```

A model may perform excellent preparatory work while remaining the wrong owner for the final decision.

---

# Common mapping errors

## Error 1: Halo delegation

**Failure:** A later step is assigned to Claude because the preceding step worked well.

**Example:** Strong clause extraction becomes unsupervised clause approval.

**Repair:** Evaluate every step independently against reversibility, stakes, accountability, evidence, and policy.

## Error 2: Collapsing collaborative into automated

**Failure:** `AI drafts, human reviews` becomes `AI drafts` because no real reviewer is staffed.

**Repair:** Name the reviewer, evidence package, review standard, service level, and intervention authority.

```text
Human mentioned in diagram
      ≠
Meaningful human review
```

## Error 3: Mapping the tool instead of the work

**Failure:** The workflow is designed around a favored Skill, artifact, or integration.

**Repair:** Map the current work, decisions, calculations, state, and consequences before assigning features.

## Error 4: Treating mechanical as automatically safe

**Failure:** A field-extraction step is labeled low risk even though one wrong value can create a harmful downstream action.

**Repair:** Evaluate propagation risk and add deterministic validation or human confirmation where needed.

## Error 5: Assigning exact rules to probabilistic judgment

**Failure:** Claude is expected to enforce a fixed eligibility, approval, or authorization rule.

**Repair:** Put the rule in deterministic logic and let Claude explain or prepare the inputs.

## Error 6: Hiding the irreversible action

**Failure:** The map ends at `prepare final output` and does not show the send, signature, filing, payment, or record update.

**Repair:** Include the side effect as its own stage with an explicit approval boundary.

## Error 7: No exception owner

**Failure:** The happy path is mapped, but ambiguous or conflicting cases have no destination.

**Repair:** Assign an exception route, accountable role, evidence requirements, and stopping rule.

---

# Delegation-mapping protocol

```text
1. Define the business outcome and workflow boundary
2. Map the work as it exists today
3. Separate each stage into atomic steps
4. Identify extraction, synthesis, calculation, judgment,
   approval, action, and storage work
5. Assess reversibility, stakes, and accountability
6. Classify each step's delegation mode
7. Add validation, evidence, and exception handling
8. Place human review before consequential or irreversible steps
9. Assign Skills, Projects, code execution, tools, and storage
10. Test the complete handoffs and failure paths
11. Record the map and accountable owners
12. Reassess after incidents, policy changes, or workflow drift
```

---

# Paste-ready prompts

## Workflow delegation mapper

```text
Map this workflow step by step before recommending features.

For every step, return:
- step and current owner;
- input and source of truth;
- work type;
- reversibility;
- stakes and propagation risk;
- accountable role;
- recommended delegation mode;
- validation;
- required human review;
- side effect;
- failure and escalation path; and
- evidence retained.

Use only these delegation modes:
AI-appropriate, AI with code execution, collaborative,
human-retained, deterministic, tool-owned, storage-owned.
```

## Over-delegation review

```text
Review the proposed map for over-delegation.

Flag:
- AI approval of its own work;
- irreversible actions without approval;
- fixed rules assigned to a language model;
- calculations generated as prose;
- human review without a named qualified reviewer;
- steps where errors propagate materially;
- absent exception ownership; and
- feature-first decisions unsupported by the workflow.

Recommend the smallest responsible correction.
```

## Meaningful-review test

```text
For every collaborative or human-review step, confirm:
- named role;
- expertise;
- authority;
- access to sources and intermediate outputs;
- time to perform the review;
- review criteria;
- ability to reject or modify; and
- recorded approval or disposition.

Treat any missing element as a control gap.
```

---

# Exam reasoning pattern

For Delegation scenarios:

1. map the work rather than the preferred feature;
2. separate preparation from authority;
3. assess reversibility, stakes, and accountability for each stage;
4. assign exact calculations and fixed rules to deterministic execution;
5. use Skills for repeatable procedures only after delegation is justified;
6. make collaborative review a staffed control;
7. expose irreversible actions as separate stages;
8. retain human approval for high-stakes or binding decisions;
9. identify over-delegation and halo delegation; and
10. choose the least autonomous design that achieves the outcome.

```text
Extract or draft, reversible        → AI-appropriate or collaborative
Exact numeric exposure              → code execution + review
Approve legal or employment term    → human-retained
Sign, send, file, or commit          → human-retained approval + controlled tool
Skill exists                         → does not determine delegation
AI did previous step well            → evaluate next step independently
```

---

# Knowledge check

## Question 1

Why must each workflow step be evaluated independently?

**Answer:** Success on one step does not establish that the next step has the same stakes, reversibility, evidence needs, or authority requirements.

## Question 2

What are the three central Delegation criteria?

**Answer:** Reversibility, stakes, and accountability.

## Question 3

Why is drafting a redline collaborative rather than fully automated?

**Answer:** Claude can prepare a useful draft, but interpretation, risk acceptance, and final approval require qualified human judgment.

## Question 4

Why should financial exposure be computed with code execution?

**Answer:** The result is numeric and material; it should be produced by explicit, reviewable calculation rather than estimated prose.

## Question 5

What is halo delegation?

**Answer:** Assigning a later step to AI because an earlier AI-performed step went well, without independently assessing the later step.

## Question 6

When is a collaborative stage actually automated?

**Answer:** When the stated human review is not staffed with a qualified reviewer who has evidence, time, authority, and intervention rights.

## Question 7

Why should features be assigned after the workflow map?

**Answer:** Tools and Skills should support justified responsibilities; they should not determine which responsibilities are safe to delegate.

## Question 8

What should happen before an irreversible external action?

**Answer:** Required validation and authorized human approval should occur before a controlled tool performs the action.

---

# Flashcards

## Flashcard 1

**Q:** What three criteria anchor Delegation Mapping?

**A:** Reversibility, stakes, and accountability.

## Flashcard 2

**Q:** What is AI-appropriate work?

**A:** Bounded work such as extraction, classification, synthesis, or drafting that is reviewable and appropriate to the risk.

## Flashcard 3

**Q:** What belongs in code execution?

**A:** Exact calculations, transformations, reconciliation, and other data steps requiring reproducible processing.

## Flashcard 4

**Q:** What belongs in a Skill?

**A:** Repeatable instructions, templates, scripts, and resources for a specialized procedure after the step is judged appropriate for AI.

## Flashcard 5

**Q:** What is collaborative delegation?

**A:** Claude prepares or analyzes while a qualified human evaluates and makes the decision.

## Flashcard 6

**Q:** What is over-delegation?

**A:** Giving Claude authority, autonomy, or side effects beyond what the step's risk profile supports.

## Flashcard 7

**Q:** What is halo delegation?

**A:** Delegating a step because a previous AI-performed step succeeded rather than evaluating the step independently.

## Flashcard 8

**Q:** What is the feature-order rule?

**A:** Map the work, classify responsibility, add controls, then assign Skills, code execution, tools, storage, and human gates.

---

# Short recap

```text
1. Map the work before choosing features.
2. Evaluate every step independently.
3. Use reversibility, stakes, and accountability.
4. Delegate bounded preparation work with validation.
5. Use code execution for exact data steps.
6. Use Skills for repeatable procedures after mapping.
7. Make collaborative review real and staffed.
8. Retain humans for authority and irreversible decisions.
9. Expose send, sign, file, and update actions explicitly.
10. Check the map for halo delegation and over-delegation.
```

> The safest redesign does not minimize human involvement. It places human judgment exactly where accountability and consequence require it.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, employment, compensation, architecture, compliance, or other professional advice.

## Source and currency note

This lesson expands preparation-course material supplied on **August 3, 2026**. Product-specific statements were checked against official Anthropic guidance on that date. Feature availability and behavior can change.

## Related material

- [Module Introduction](01-module-introduction.md)
- [Analyzing Requirements and Use Cases](02-analyzing-requirements-use-cases.md)
- [Research, Planning, and Process Optimization](03-research-planning-process-optimization.md)
- [Solution Design, Development, and Iteration](04-solution-design-development-iteration.md)
- [Module 4 overview](../README.md)
- [Delegation Mapping prompt notebook](../../../prompts/module-04/05-delegation-mapping-prompts.md)
- [Delegation Boundary Mapping Pattern](../../../patterns/delegation-boundary-mapping-pattern.md)
