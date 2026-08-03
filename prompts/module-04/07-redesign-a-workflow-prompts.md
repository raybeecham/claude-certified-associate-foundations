# Module 4 Prompt Notebook: Redesign a Workflow

These exercises use fictional or generic workflows. Do not paste confidential receipts, financial records, employee data, credentials, or internal policy material into public study work.

## 1. Atomic workflow map

```text
Map the supplied workflow into atomic stages.
For each stage, identify:
- trigger;
- input;
- work performed;
- output;
- side effect;
- current owner;
- consequence if wrong; and
- whether the result is reversible.
Do not assign AI features yet.
```

## 2. Three-criteria assessment

```text
For each workflow stage, assess:
1. reversibility;
2. stakes; and
3. accountability.
Rate each Low, Medium, or High and explain the controlling reason.
```

## 3. Delegation classification

```text
Classify every stage as:
- automated;
- collaborative; or
- human-retained.
For each classification, explain why the other two are weaker.
```

## 4. Feature assignment

```text
After the work is mapped, assign the most appropriate implementation feature:
- Skill;
- code execution;
- deterministic logic;
- controlled external tool;
- storage or system of record;
- no AI feature required.
Do not let an existing feature determine the delegation decision.
```

## 5. Expense-workflow drill

```text
Map this fictional expense workflow:
1. extract receipt line items;
2. compare expenses with policy;
3. total the report and calculate policy variance;
4. draft an exception note;
5. approve or reject;
6. submit the approved report for payment.
Return a table with delegation, feature, reason, validation, reviewer, and approval boundary.
```

## 6. Skill-versus-code test

```text
For every automated or collaborative step, determine whether it primarily needs:
- a repeatable procedure;
- exact calculation;
- both; or
- neither.
Assign Skills to maintained procedures and code execution to exact calculations.
Explain any combined design.
```

## 7. Policy-exception route

```text
Design the exception route for ambiguous policy findings.
Include:
- evidence provided to the reviewer;
- reviewer qualifications;
- decision options;
- escalation conditions;
- required rationale; and
- retained audit evidence.
```

## 8. Calculation contract

```text
Write a code-execution contract for expense totals and policy limits.
Specify:
- required columns;
- currency and unit rules;
- duplicate detection;
- inclusion and exclusion rules;
- policy-limit logic;
- formulas;
- reconciliation checks;
- error behavior; and
- retained outputs.
```

## 9. Meaningful-review test

```text
Evaluate whether the proposed human review is operational.
Check for:
- named role;
- expertise;
- evidence access;
- criteria;
- time;
- authority to reject;
- intervention rights;
- exception path; and
- approval record.
Label ceremonial review as a control failure.
```

## 10. Hidden-side-effect scan

```text
Scan the workflow for broad stages that hide consequential actions.
Split out any action such as:
- send;
- submit;
- pay;
- sign;
- file;
- publish;
- grant access; or
- update an official record.
Place authorization immediately before the side effect.
```

## 11. Halo-delegation audit

```text
Identify every place where success on an earlier AI step is being used to justify more autonomy later.
For each, reassess the later step independently using reversibility, stakes, accountability, and side effects.
```

## 12. Audit-evidence design

```text
Create an evidence register for the redesigned workflow.
Include:
- original source records;
- extracted data;
- policy version;
- cited rules;
- calculation code and output;
- reviewer decisions;
- approval evidence;
- external-action identifier; and
- correction or rollback history.
```

## 13. Failure-path design

```text
For each stage, define:
- likely failure;
- detection method;
- retry rule;
- fallback;
- escalation owner;
- stop condition; and
- recovery or correction path.
Do not retry a financial side effect without idempotency protection.
```

## 14. Original workflow practice

```text
Create a six-stage fictional workflow in a different domain.
Require at least:
- one Skill step;
- one code-executed step;
- one collaborative step;
- one human-retained approval;
- one irreversible external action; and
- one exception path.
Then provide the model map and rationale.
```

## 15. Oral certification drill

```text
Give me one workflow stage at a time.
I will answer:
- delegation mode;
- appropriate feature;
- controlling reason;
- required validation; and
- approval boundary.
Challenge halo delegation, generated arithmetic, ceremonial review, and hidden side effects.
```

## Compact redesign card

```text
Map work first.
For every stage ask:
- Is it reversible?
- What are the stakes?
- Who owns accountability?
- Does it require exact computation?
- Does it create an external side effect?
- What must be validated?
- Who reviews?
- Who approves?
- What evidence is retained?

Procedure → Skill
Calculation → Code execution
Drafting → AI or collaborative
Approval → Human-retained
External action → Approval before controlled execution
```
