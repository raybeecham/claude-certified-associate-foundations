# Lesson 7: Exercise — Redesign a Workflow

## Completion record

```text
Result: Strong map — all six steps correct
```

The exercise tested whether the learner could:

- classify workflow stages as automated, collaborative, or human-retained;
- distinguish repeatable procedure work from exact computation;
- place a Skill on a procedure-heavy stage;
- place code execution on a numeric stage;
- preserve human accountability for approval; and
- retain human control over an irreversible financial action.

This public lesson uses an original fictional expense-report workflow rather than reproducing proprietary course questions.

---

# Exercise objective

Delegation mapping becomes useful when it is applied end to end rather than one stage at a time in isolation.

The exercise asks:

```text
What work happens at each stage?
      ↓
How reversible is it?
      ↓
What are the stakes?
      ↓
Who owns accountability?
      ↓
Which feature or control belongs there?
```

The goal is not maximum automation. The goal is a workflow that performs useful AI-assisted work while keeping exact calculation, approval, and irreversible financial action under the correct controls.

---

# Plain-English explanation

An expense report contains several different kinds of work:

- reading receipts;
- comparing expenses with policy;
- calculating totals;
- explaining exceptions;
- approving or rejecting the request; and
- sending an approved request for payment.

These should not all be delegated the same way.

```text
Mechanical extraction
      ≠
Policy judgment
      ≠
Exact calculation
      ≠
Approval
      ≠
Payment submission
```

Each stage receives its own delegation decision.

---

# One analogy: airport security lanes

An airport uses different controls for different stages.

- A scanner detects objects efficiently.
- A system checks document fields.
- A trained officer resolves ambiguous findings.
- An authorized official makes consequential decisions.

A good security process does not let the scanner make every decision simply because it works well at detection.

Expense workflows follow the same principle:

> Use automation for bounded detection and calculation. Retain people for ambiguity, approval, and consequential action.

---

# Workflow map

## Step 1: Extract receipt line items and amounts

**Delegation:** Automated  
**Feature:** Skill

### Why

- the task is mechanical;
- the output is reviewable;
- errors can be corrected before approval;
- the action does not itself create a financial consequence; and
- a maintained document-processing procedure improves consistency.

### Controls

- preserve receipt-to-row traceability;
- flag unreadable values;
- do not invent missing amounts;
- retain original receipt images; and
- validate required fields.

---

## Step 2: Compare expenses with travel policy

**Delegation:** Collaborative  
**Feature:** Skill

### Why

Claude can apply a maintained policy procedure and flag candidate departures, but policy language may contain exceptions, ambiguous categories, or context that requires human interpretation.

```text
Policy flag
      ≠
Final compliance decision
```

### Controls

- cite the controlling policy section;
- distinguish clear violation, possible exception, and insufficient evidence;
- assign edge cases to a qualified reviewer; and
- retain reviewer rationale.

---

## Step 3: Calculate totals and policy variance

**Delegation:** Automated  
**Feature:** Code execution

### Why

Totals, category limits, tax treatment, and over-or-under calculations are exact numerical operations.

```text
Generated arithmetic
      ≠
Executed arithmetic
```

### Controls

- define inclusion rules;
- validate currency and units;
- detect duplicate receipts;
- expose formulas;
- reconcile totals to line items; and
- retain calculation output.

---

## Step 4: Draft the exception summary

**Delegation:** Collaborative  
**Feature:** Neither required by default

### Why

Claude can draft a clear explanation from the flagged items and verified calculations. The approver must confirm tone, context, and whether the explanation accurately reflects the policy decision.

### Controls

- use only verified flags and calculations;
- preserve uncertainty;
- do not state that an item is approved or rejected;
- require approver edits or confirmation; and
- retain the final approved note.

---

## Step 5: Approve or reject the report

**Delegation:** Human-retained

### Why

The decision carries financial and organizational accountability. It may require context, exception authority, budget ownership, and responsibility for fairness or policy application.

```text
AI-prepared evidence
      ≠
Authority to approve
```

### Controls

- identify the authorized approver;
- provide source receipts, policy flags, calculations, and exception notes;
- allow rejection or return for correction;
- record rationale; and
- separate approval from preparation.

---

## Step 6: Submit the approved report for payment

**Delegation:** Human-retained before controlled execution

### Why

Submitting the report initiates an external, financially material action. The step is consequential and may be difficult to reverse.

### Controls

- require approved status;
- confirm recipient and payment system;
- confirm final amount and currency;
- prevent duplicate submission;
- retain transaction or submission identifier; and
- provide recovery or escalation procedures.

---

# Model map

| Step | Delegation | Feature | Governing reason |
|---|---|---|---|
| Receipt extraction | Automated | Skill | Mechanical, reversible, reviewable |
| Policy comparison | Collaborative | Skill | Repeatable policy procedure with human interpretation for exceptions |
| Totals and variance | Automated | Code execution | Exact numerical work |
| Exception summary | Collaborative | Neither required | AI drafts; approver confirms context and decision language |
| Approve or reject | Human-retained | None | Financial accountability and authority |
| Submit for payment | Human-retained before controlled action | Controlled system | Irreversible or financially material side effect |

## Feature selections

```text
Best Skill step:
Step 2 — policy comparison

Best code-execution step:
Step 3 — totals and policy-limit calculations
```

Step 1 can also use a document-oriented Skill, but Step 2 most clearly demonstrates a maintained repeatable policy procedure.

---

# Why the map is strong

The completed map demonstrates four important boundaries.

## 1. Procedure versus calculation

```text
Repeatable instructions and policy logic → Skill
Exact arithmetic and transformations    → Code execution
```

## 2. Assistance versus authority

```text
Extract, flag, calculate, draft
      ↓
Human evaluates evidence
      ↓
Human approves or rejects
```

## 3. Approval versus execution

Approval and payment submission are separate stages. A valid approval does not mean the workflow should silently perform the external action.

## 4. Reviewability versus consequence

The early stages are reversible and reviewable. The later stages carry financial authority and external consequence.

---

# Audit-ready redesign

A defensible implementation would preserve this evidence:

| Evidence | Purpose |
|---|---|
| Original receipts | Source record |
| Extracted line-item table | Traceability and review |
| Policy version and cited sections | Rule provenance |
| Flag classifications | Clear versus ambiguous findings |
| Calculation code and output | Reproducibility |
| Human exception decisions | Accountability |
| Approval record | Authorization |
| Payment-submission identifier | External-action evidence |

```text
Mapped delegation
      +
Operational controls
      +
Retained evidence
      =
Audit-ready workflow design
```

---

# Common mistakes

## Automating approval because earlier stages worked

This is halo delegation. Extraction and calculation success do not establish approval authority.

## Calling policy review fully automated

Policy comparison may be automated, but ambiguous exceptions still require a real reviewer.

## Using a Skill for arithmetic

A Skill can define the procedure, but exact totals should be executed and reconciled.

## Treating approval and payment submission as one step

This hides an irreversible side effect and weakens control design.

## Naming human review without staffing it

A collaborative stage requires a qualified reviewer, evidence, criteria, time, and intervention rights.

---

# Knowledge checks

1. Why is policy comparison collaborative rather than fully automated?
2. Why is code execution preferable for totals?
3. What makes approval human-retained?
4. Why should payment submission be shown as a separate stage?
5. What evidence would an auditor need to reconstruct the workflow decision?

---

# Flashcards

**Q: What is the best feature for a repeatable policy-check procedure?**  
A: A Skill, with human review for ambiguity and exceptions.

**Q: What is the best feature for totals and limit calculations?**  
A: Code execution or another deterministic calculation path.

**Q: Does a strong draft justify automated approval?**  
A: No. Drafting quality does not transfer authority.

**Q: What stages stay human-retained in the expense workflow?**  
A: Approval or rejection and authorization before payment submission.

**Q: What makes the redesign audit-ready?**  
A: Explicit delegation, operational controls, traceability, reproducible calculations, approval evidence, and external-action records.

---

# Short recap

```text
1. Map every workflow stage independently.
2. Use Skills for repeatable procedures.
3. Use code execution for exact numeric work.
4. Keep ambiguous policy interpretation collaborative.
5. Keep financial approval human-retained.
6. Separate approval from payment submission.
7. Place approval before external consequence.
8. Preserve source, calculation, review, and action evidence.
9. Check for halo delegation.
10. Prefer the least autonomous design that achieves the outcome.
```

> The strongest workflow does not automate every step. It assigns each step to the component that can perform it responsibly.

---

# Public-repository note

This expense workflow is fictional and educational. It does not constitute accounting, tax, legal, employment, audit, or financial-control advice.
