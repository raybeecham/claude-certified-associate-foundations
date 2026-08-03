# Lesson 6: Communicating Value and Limitations to Stakeholders

## Overview

A workflow is not fully integrated until the people who rely on it understand what it does, what it does not do, what value has been observed, and where human responsibility remains.

Stakeholders may include:

- operational managers;
- executives;
- clients;
- legal or compliance teams;
- security and risk functions;
- end users;
- reviewers and approvers; and
- people affected by the workflow.

The communication goal is not to make the system sound impressive. It is to set an accurate expectation that remains credible when the first visible error occurs.

> Trust comes from bounded claims, visible controls, and evidence—not from confident language.

A useful stakeholder message contains four parts:

```text
What Claude does
      +
What Claude does not do
      +
What value has been observed
      +
What human and technical controls remain
      ↓
Credible workflow description
```

---

# Plain-English explanation

Compare these two statements:

```text
Claude handles contract review.
```

```text
Claude extracts clauses, flags departures from the approved playbook,
and drafts proposed redlines. A lawyer reviews and approves every change
before anything is sent.
```

The first statement hides the actual workflow boundary. It suggests that Claude owns interpretation, approval, and perhaps transmission.

The second statement explains:

- the AI-owned preparation steps;
- the retained human decision;
- the approval boundary; and
- the point at which the output may leave the organization.

The second statement is more useful because a stakeholder can evaluate the real capability and control model.

---

# One analogy: a product label

A trustworthy product label tells the buyer:

- what the product contains;
- what it is designed to do;
- how it should be used;
- what warnings apply; and
- who should not rely on it without additional support.

A label that says only `powerful`, `automatic`, or `intelligent` does not help someone use the product safely.

Workflow communication works the same way.

```text
Capability claim without boundary
      =
Marketing language

Capability claim with scope, evidence, and controls
      =
Operational description
```

---

# The capability-boundary statement

Use this structure:

```text
Claude [performs bounded tasks].
It does not [retain authority, approve, or execute prohibited actions].
[Named human or role] reviews or approves [consequential output or decision].
Observed value is [measured result] under [scope and period].
Known limitations include [material failure modes or dependencies].
```

Example:

```text
Claude extracts clauses, compares them with the approved playbook,
and drafts proposed redlines. It does not approve contract changes or send
contracts. A lawyer reviews every proposed change and an authorized signatory
controls final transmission. In the pilot, median review time decreased by
approximately half while the approval standard remained unchanged. Claude may
miss obligations expressed indirectly, so the flags guide rather than replace
the lawyer's full review.
```

Each part carries a different kind of information:

| Element | Question answered |
|---|---|
| Bounded capability | What work does Claude perform? |
| Exclusion | What work or authority is not delegated? |
| Human control | Who reviews, approves, or acts? |
| Evidence | What result has actually been observed? |
| Scope | Under what conditions was the result observed? |
| Limitation | Where can the workflow fail or require escalation? |

---

# Value claims need evidence

A statement such as:

```text
Review time is down about half.
```

should be supported by a defined measure.

Record:

- baseline period;
- pilot or comparison period;
- sample size;
- included and excluded cases;
- metric definition;
- source system;
- quality or approval standard;
- error, correction, or escalation rate; and
- known confounding factors.

```text
Observed improvement
      ≠
Universal capability
      ≠
Guaranteed future result
```

Safer wording:

```text
During the six-week pilot covering standard agreements,
median first-pass review time decreased from X to Y,
while every change continued to require lawyer approval.
Complex and nonstandard agreements were excluded.
```

This is more credible than a broad claim that AI `cuts contract review time by 50%` in all settings.

---

# Same workflow, different audiences

The facts and control model remain invariant. The depth and emphasis change.

## Legal lead

Needs:

- workflow detail;
- source and playbook boundaries;
- known failure modes;
- review responsibilities;
- exception handling; and
- evidence available for each proposed change.

Example:

```text
Claude extracts clauses, flags departures from the approved playbook,
and drafts proposed redlines with source and rule references.
It does not approve changes. You review every proposed edit.
A known failure mode is missing obligations expressed indirectly,
so the flags support rather than replace the full legal read.
```

## Practice executive

Needs:

- business outcome;
- scale and scope;
- retained oversight;
- risk posture;
- cost or cycle-time effect; and
- decision or investment required.

Example:

```text
In the pilot, review time decreased by about half for standard agreements,
with the same lawyer-approval requirement. The next decision is whether the
observed savings justify expanding the controlled workflow to a larger set of
agreement types.
```

## Client risk function

Needs:

- where AI participates;
- what data or documents it receives;
- what decisions remain human;
- whether external action is automatic;
- oversight and evidence;
- incident and escalation path; and
- material limitations.

Example:

```text
AI assists with clause extraction and draft preparation.
Qualified legal personnel review and approve every term.
No agreement is signed or sent without authorized human approval.
Exceptions and uncertain playbook matches are escalated for manual review.
```

## Invariant content

The following must not change across audience versions:

- actual workflow boundary;
- verified metrics;
- uncertainty;
- known limitations;
- retained human gate;
- data and source scope;
- approval and execution model; and
- material obligations or risks.

```text
Audience adaptation
      ≠
Risk concealment
```

---

# Description applied outward

A precise prompt defines what Claude should do, what evidence it may use, and what output is required.

Stakeholder description applies the same discipline in the opposite direction.

```text
Prompt description
→ specifies the task to Claude

Stakeholder description
→ specifies Claude's role to people
```

Both require:

- scope;
- boundaries;
- inputs;
- outputs;
- constraints;
- uncertainty;
- validation; and
- ownership.

---

# Document human oversight

Do not write only:

```text
Human review is included.
```

A meaningful control description identifies:

- reviewer role;
- required expertise;
- items reviewed;
- evidence available;
- approval criteria;
- exception path;
- authority to reject or stop;
- timing relative to external action; and
- retained record of approval.

Example:

```text
Every client-bound redline is reviewed by an assigned lawyer against the
source contract and approved playbook before release. The lawyer may reject,
modify, or escalate any proposal. The approved version and reviewer decision
are retained before the authorized signatory sends the contract.
```

```text
Review gate named
      ≠
Review gate operational
```

---

# Good and bad messaging

| Overstated | Accurate |
|---|---|
| Our AI system reviews contracts automatically. | Claude prepares clause extraction, playbook comparisons, and proposed redlines. A lawyer reviews and approves every change before release. |
| Claude handles onboarding. | Claude prepares approved-template documents and personalized draft text. HR verifies compensation and an authorized person sends the signed offer. |
| The workflow is fully automated. | Defined preparation and calculation stages are automated; approvals and binding external actions remain human-controlled. |
| It is as good as an expert. | It performs specified preparation tasks under tested conditions; qualified experts retain interpretation and approval. |
| The system eliminates errors. | The workflow reduces selected manual steps and includes validation and review controls; defects and exceptions remain possible. |
| Claude guarantees compliance. | Claude can flag candidate departures from configured rules; compliance judgment and approval remain with authorized personnel. |

---

# Phrases that quietly overstate

## `Fully automated`

Often hides:

- manual data preparation;
- human approvals;
- exception handling;
- monitoring;
- corrections; or
- external-action controls.

## `Claude handles X`

Collapses multiple workflow stages into one phrase and removes the human and deterministic components from view.

## `As good as a person`

Uses an undefined comparison group and usually ignores case complexity, failure distribution, accountability, and human judgment.

## `Eliminates risk`

A workflow may reduce one risk while adding model, data, integration, monitoring, or overreliance risks.

## `Guaranteed`

Should be avoided unless an enforceable deterministic property and its exact scope have been established.

## Repair method

Replace the phrase with:

```text
Specific task
+ observed evidence
+ scope
+ known limitation
+ retained control
```

---

# Stakeholder communication protocol

```text
1. Identify the audience and decision
2. State the business problem and workflow scope
3. Describe Claude's bounded tasks
4. State what Claude does not own
5. Name deterministic, tool, storage, and human responsibilities
6. Report only measured value with scope and method
7. Explain known failure modes and dependencies
8. Describe review, approval, exception, and incident controls
9. Adapt depth and language without changing material facts
10. Confirm expectations before expansion or release
```

## Communication register

| Field | Content |
|---|---|
| Audience | Role and AI literacy |
| Decision needed | Approve pilot, expand, accept risk, use result, or monitor |
| Capability | Bounded tasks performed by Claude |
| Exclusions | Decisions and actions not delegated |
| Evidence | Measured result and method |
| Scope | Cases, period, users, and data |
| Controls | Validation, review, approval, monitoring |
| Limitations | Failure modes, assumptions, dependencies |
| Escalation | Who handles exceptions and incidents |
| Owner | Person accountable for the statement |

---

# Common failure modes

## Capability inflation

A narrow successful pilot is described as a broad organizational capability.

## Metric inflation

An observed cycle-time improvement is presented without scope, baseline, or quality measure.

## Hidden human labor

The message attributes the result to AI while omitting substantial review, correction, and exception work.

## Limitation dumping

A long generic disclaimer replaces a concise explanation of the material limitations relevant to the audience's decision.

## Audience distortion

An executive version removes uncertainty or review dependencies in the name of simplicity.

## Assurance theater

Controls are listed, but no owner, evidence, authority, or operational process exists.

---

# Practical example

A team is preparing a stakeholder briefing for the contract-review pilot.

## Evidence package

- standard agreements only;
- six-week pilot;
- median first-pass review time reduced;
- lawyer approval retained for every change;
- indirect obligations remain a known failure mode;
- nonstandard agreements require manual routing; and
- no contract is sent automatically.

## Executive briefing

```text
The pilot reduced median first-pass review time for standard agreements while
retaining lawyer approval for every change. Claude performs clause extraction,
playbook comparison, and draft redlining. Nonstandard agreements and uncertain
matches are routed for manual review. The expansion decision should consider
measured savings, exception volume, and the cost of maintaining the playbook.
```

## Risk briefing

```text
The system does not approve terms or transmit contracts. Qualified lawyers
review every proposed change against the source agreement and approved
playbook. Known risks include missed indirect obligations and stale playbook
rules. Exceptions are escalated, approvals are retained, and external action
requires an authorized signatory.
```

Both messages describe the same system. Neither hides the control boundary.

---

# Knowledge checks

1. Why is `Claude handles contract review` an unsafe description?
2. Which facts must remain invariant across executive and risk audiences?
3. What evidence is needed before claiming a 50% cycle-time improvement?
4. Why can explicit human gates increase stakeholder trust?
5. What makes `human review included` operationally incomplete?
6. How should a pilot result be scoped before communicating it?
7. Why is a long disclaimer not a substitute for material limitations?

---

# Flashcards

**Q:** What are the four parts of a credible capability message?  
**A:** Bounded AI task, exclusions, observed value, and retained controls or limitations.

**Q:** What should change across audiences?  
**A:** Depth, vocabulary, order, and emphasis.

**Q:** What must remain invariant?  
**A:** Capability boundary, verified evidence, uncertainty, limitations, and human controls.

**Q:** Why is `fully automated` usually misleading?  
**A:** It often hides review, exceptions, monitoring, correction, or external-action gates.

**Q:** What makes a value claim defensible?  
**A:** A defined metric, baseline, comparison period, scope, quality standard, and source.

**Q:** What is assurance theater?  
**A:** Naming controls that are not assigned, evidenced, authorized, or operational.

---

# Short recap

```text
1. Describe the real workflow, not an inflated label.
2. State what Claude does and does not own.
3. Report measured value with scope and method.
4. Name material limitations and dependencies.
5. Document qualified human review and approval.
6. Adapt detail to the audience without changing facts.
7. Avoid fully automated, handles X, guarantees, and human-level claims.
8. Preserve uncertainty and exception paths.
9. Keep a communication owner and evidence package.
10. Trust grows when value and limits are stated together.
```

> A credible stakeholder message makes the workflow understandable before the first failure makes its boundaries visible.

---

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential contract metrics, client names, internal risk findings, approval records, system identifiers, or nonpublic pilot results.

## Educational-use notice

This lesson is an unofficial educational resource and does not constitute legal, compliance, risk, communications, procurement, or operational advice.
