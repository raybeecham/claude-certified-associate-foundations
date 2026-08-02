# Module 3 Notebook: Diligence and Human Review

These prompts are study aids and workflow-design templates. They do not replace organizational policy, qualified professional review, approval authority, or current legal and regulatory requirements.

Use fictional, generic, synthetic, public, or explicitly authorized information.

---

## 1. Four-threshold risk assessment

```text
Evaluate the proposed AI-assisted output against four review thresholds:

1. Stakes — What could happen if it is wrong, incomplete, misleading, or misused?
2. Reversibility — Can the communication or action be undone completely and cheaply?
3. Audience — Who will see, rely on, approve, or act on it?
4. Regulatory exposure — What laws, contracts, policies, standards, or professional duties apply?

For each threshold, classify the risk as Low, Material, or High and explain the evidence.

Then state:
- the highest controlling threshold;
- whether a mandatory human-review gate applies;
- the required reviewer expertise and authority;
- the validation required before release; and
- the permitted disposition: release, edit, verify, escalate, or reject.

Do not average away a High condition because other thresholds are Low.
```

---

## 2. Precommitted review-gate designer

```text
Design a review gate for the following AI-assisted use case.

Use case:
[DESCRIBE THE TASK, AUDIENCE, DATA, DECISION, AND OUTPUT]

Define before generation:
1. output category;
2. intended use and audience;
3. automatic review triggers;
4. prohibited actions before approval;
5. required evidence and deterministic checks;
6. required reviewer role, expertise, authority, and access;
7. approval record or system of record;
8. release, edit, verify, escalate, and reject criteria; and
9. retention or traceability requirements.

Return a concise policy table and an executable checklist.
```

---

## 3. Do-not-ship policy builder

```text
Create a do-not-ship-without-human-review policy for an organization using AI-assisted drafting and analysis.

At minimum, address:
- final client or partner deliverables;
- audit-critical or financially material calculations;
- regulated, confidential, or highly sensitive information;
- public or legal communications with lasting consequence;
- safety-critical recommendations;
- decisions affecting rights, access, employment, benefits, or eligibility;
- irreversible tool actions; and
- production-impacting security or system changes.

For each category, define:
- examples;
- required reviewer;
- required evidence or validation;
- prohibited action before approval;
- approval record; and
- escalation path.

Do not claim that the prompt itself enforces the policy. Identify the technical and procedural controls required.
```

---

## 4. Meaningful-human-review test

```text
Assess whether the proposed human review is meaningful or ceremonial.

Review process:
[DESCRIBE THE REVIEWER AND REVIEW STEP]

Evaluate whether the reviewer has:
- relevant expertise;
- authority to approve, reject, or escalate;
- context about the intended use and audience;
- access to source evidence and calculations;
- enough time and attention;
- independence to challenge the draft;
- defined review criteria; and
- the ability to intervene before release.

Return:
1. pass/fail by dimension;
2. missing reviewer capabilities;
3. whether the current gate is adequate;
4. required remediation; and
5. a revised review-step definition.
```

---

## 5. Final client deliverable gate

```text
Evaluate this proposed final client deliverable before release.

Materials:
- draft deliverable;
- requirements or statement of work;
- source package;
- calculation files;
- known limitations; and
- approval policy.

Check:
1. requirement coverage;
2. claim-to-source support;
3. calculation reproducibility;
4. internal consistency;
5. material omissions and uncertainty;
6. confidentiality and authorized disclosure;
7. audience, tone, and organizational position;
8. professional-standard compliance;
9. reviewer qualifications and approval evidence; and
10. unresolved issues that block release.

Return one disposition:
- Release;
- Edit and re-review;
- Verify additional claims;
- Escalate; or
- Reject.

Do not use a generally polished appearance as evidence of readiness.
```

---

## 6. Financial-materiality review

```text
Review the AI-assisted financial summary and supporting workbook.

Requirements:
- identify all material figures and claims;
- trace each figure to authoritative inputs;
- document the formula or calculation rule;
- recompute material values deterministically;
- compare the recomputed values with the narrative;
- identify variances, unsupported assumptions, stale inputs, or unit errors;
- determine whether the output is audit-critical or financially material; and
- identify the qualified financial or control reviewer required.

Return:
1. material-figure register;
2. recalculation results;
3. variance table;
4. unresolved assumptions;
5. required human-review gate; and
6. release disposition.

Cell citations improve traceability but do not prove formula correctness or authorize release.
```

---

## 7. Sensitive-data diligence review

```text
Evaluate whether this AI-assisted workflow handles sensitive information appropriately.

Describe:
[DATA, ENVIRONMENT, USERS, TOOLS, RETENTION, AND OUTPUT]

Assess:
- data classification;
- authorization to use the data;
- minimum-necessary data scope;
- approved product surface and environment;
- access controls;
- storage and retention;
- connector and tool permissions;
- recipient authorization;
- disclosure risk;
- logging and traceability;
- human-review requirements; and
- governing policy, contract, or regulation.

Separate:
1. content accuracy;
2. data-handling compliance;
3. release authorization; and
4. unresolved policy questions.

Do not infer approval from the fact that the model was technically able to process the information.
```

---

## 8. Public or legal communication gate

```text
Review this proposed public, legal, regulatory, or incident communication.

Identify:
- every factual claim;
- every legal, compliance, or policy assertion;
- statements that could create reliance or waive rights;
- statements of certainty that exceed the evidence;
- confidentiality or privilege concerns;
- applicable approval roles;
- required source verification;
- current-versus-historical distinctions; and
- consequences if the statement is later corrected.

Return:
1. release-blocking issues;
2. claims requiring qualification;
3. required legal, communications, executive, or compliance reviewers;
4. prohibited publication action before approval; and
5. disposition.

Treat this as issue spotting, not professional legal advice.
```

---

## 9. Iteration-versus-escalation diagnostic

```text
Determine whether this AI-assisted task should continue through prompt iteration or escalate to a human expert.

Provide:
- original objective;
- prior prompt versions;
- outputs from each round;
- acceptance criteria;
- remaining defects; and
- available evidence and tools.

Analyze:
1. improvement by round;
2. whether the same defect persists;
3. whether later rounds create only cosmetic changes;
4. whether regressions are appearing;
5. whether the remaining gap is prompt-fixable;
6. whether missing evidence, authority, expertise, or professional judgment is the true blocker;
7. stakes and audience; and
8. whether a fresh independent reviewer is needed.

Return:
- continue iterating;
- make one targeted final revision;
- obtain missing evidence or fix the workflow; or
- stop and escalate.

Explain the decision using the improvement curve and risk thresholds.
```

---

## 10. Flat-improvement-curve review

```text
Compare these versions of an AI-assisted deliverable.

For each version, score or assess:
- factual support;
- requirement coverage;
- clarity;
- audience fit;
- risk disclosure;
- actionability;
- internal consistency; and
- acceptance-criteria compliance.

Then identify:
- the last round that produced material improvement;
- changes that are merely stylistic;
- unresolved issues requiring human judgment;
- any regressions; and
- whether another prompt round is likely to create value.

Do not recommend continued iteration solely because additional wording changes are possible.
```

---

## 11. Accountability and approval matrix

```text
Create an accountability matrix for an AI-assisted workflow.

Stages:
[LIST THE WORKFLOW STAGES]

Roles:
[LIST OWNERS, REVIEWERS, APPROVERS, AND OPERATORS]

For each stage, define:
- who prepares the work;
- who verifies evidence;
- who validates calculations;
- who reviews professional judgment;
- who approves release;
- who executes any external action;
- who monitors outcomes; and
- who owns correction or incident response.

Ensure that no stage assigns final accountability to the model.

Return a RACI-style table and identify any ownership gaps or conflicting approvals.
```

---

## 12. Review-gate placement analysis

```text
Map the workflow and identify where human-review gates must occur.

Workflow:
[DESCRIBE OR PASTE THE WORKFLOW]

For each send, publish, file, approve, delete, transfer, production change, or other side effect:
1. identify the action;
2. classify reversibility;
3. identify required evidence;
4. identify the required reviewer and approver;
5. define the technical or procedural hold point;
6. specify the approval record; and
7. define failure and rollback behavior.

Flag any review step that occurs after the irreversible action.
```

---

## 13. Fast-yes scenario drill

```text
Scenario:
Claude drafts a private internal agenda for a routine team meeting. It contains no sensitive information, creates no external action, and can be edited at any time.

Apply the four Diligence thresholds and explain:
- why specialist escalation is or is not required;
- what proportionate review remains appropriate;
- what would change the classification; and
- the correct disposition.
```

---

## 14. Deceptive-looks-fine scenario drill

```text
Scenario:
Claude produces a clean executive financial summary for a board presentation. The draft includes material revenue, cost, and forecast figures.

Apply:
- stakes;
- reversibility;
- audience;
- regulatory or governance exposure;
- calculation verification;
- reviewer qualifications;
- approval evidence; and
- release disposition.

Explain why the draft's polished appearance is irrelevant to the mandatory review gate.
```

---

## 15. Slow-creep scenario drill

```text
Scenario:
A team has revised an external proposal five times. The final three rounds changed wording but did not improve evidence, argument quality, or client fit.

Diagnose:
- the improvement curve;
- remaining defects;
- whether the gaps are prompt-fixable;
- stakes and audience;
- the value of a fresh reviewer; and
- the correct point to stop prompting.

Return an escalation recommendation and the review brief to give the colleague.
```

---

## 16. Release-decision record

```text
Create a release-decision record for this AI-assisted output.

Include:
- output identifier and version;
- intended use and audience;
- four-threshold assessment;
- automatic review gates triggered;
- sources and calculation artifacts reviewed;
- known limitations and unresolved uncertainty;
- reviewer identity, role, expertise, and authority;
- material changes made;
- approval or rejection decision;
- prohibited downstream uses;
- release date; and
- monitoring or correction owner.

Use only information supplied. Mark absent information as `unknown` rather than inventing it.
```

---

## 17. Human-review postmortem

```text
Conduct a postmortem for an AI-assisted output that was released with an error.

Analyze:
1. intended use and stakes;
2. which Diligence threshold was missed;
3. whether a mandatory-review category applied;
4. whether the reviewer was qualified and empowered;
5. whether the gate occurred before or after the irreversible action;
6. whether iteration continued after evidence or authority ran out;
7. ownership and approval gaps;
8. detection and correction timeline;
9. trust, financial, legal, operational, or safety consequences; and
10. preventive controls.

Return:
- root causes;
- contributing conditions;
- immediate remediation;
- policy or technical-control changes;
- owner and due date; and
- verification that the correction worked.
```

---

## 18. Oral certification drill

Answer each in two or three sentences:

1. What are the four Diligence thresholds?
2. Why should mandatory-review categories be decided in advance?
3. What distinguishes meaningful human review from ceremonial approval?
4. Why do citations not remove the need for review?
5. When should prompt iteration stop?
6. What does reversibility add beyond stakes?
7. Who owns an AI-assisted output after release?
8. Why should low-stakes internal work not be over-escalated?
9. Where should a review gate sit relative to an irreversible action?
10. What evidence should be retained for a material release decision?

---

# Compact review card

```text
DILIGENCE REVIEW CARD

Purpose and audience:
[ ] Defined

Four thresholds:
[ ] Stakes
[ ] Reversibility
[ ] Audience
[ ] Regulatory / contractual / policy exposure

Automatic gate:
[ ] Final external deliverable
[ ] Material or audit-critical calculation
[ ] Regulated or sensitive information
[ ] Public or legal communication
[ ] Consequential decision or irreversible action

Meaningful reviewer:
[ ] Expertise
[ ] Authority
[ ] Context
[ ] Evidence access
[ ] Time
[ ] Independence
[ ] Ability to intervene

Validation:
[ ] Sources checked
[ ] Calculations recomputed
[ ] Completeness and bias reviewed
[ ] Sensitive-data handling checked
[ ] Professional standards applied

Disposition:
[ ] Release
[ ] Edit and re-review
[ ] Verify
[ ] Escalate
[ ] Reject

Approval evidence:
[RECORD]
```
