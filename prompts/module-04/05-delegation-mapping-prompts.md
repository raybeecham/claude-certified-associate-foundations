# Module 4 Notebook: Delegation Mapping

Use these prompts to map work before assigning Claude features or automation.

---

## 1. Atomic workflow mapper

```text
Map this workflow into atomic steps.

For each step, return:
- step ID and name;
- current owner;
- input and source of truth;
- work type;
- output;
- consequence if wrong;
- side effect;
- exception path.

Do not recommend AI features yet.
```

## 2. Three-criteria assessment

```text
Assess every step independently using:
- reversibility;
- stakes;
- accountability.

Classify each as Low, Material, or High concern and explain the controlling factor.
```

## 3. Delegation classifier

```text
Assign one primary delegation mode to each workflow step:
- AI-appropriate;
- AI with code execution;
- collaborative;
- human-retained;
- deterministic;
- tool-owned;
- storage-owned.

State the required validation and approval boundary.
```

## 4. Contract-review map

```text
Map a fictional contract-review process covering:
- clause extraction;
- playbook comparison;
- redline drafting;
- legal approval;
- financial-exposure calculation;
- signature and sending.

Use reversibility, stakes, and accountability. Preserve final legal authority with the qualified human reviewer.
```

## 5. Onboarding-document map

```text
Map a fictional offer-letter and onboarding process covering:
- approved-data extraction;
- template drafting;
- welcome-note personalization;
- compensation confirmation;
- signature and sending.

Identify code-executed, AI, collaborative, and human-retained stages.
```

## 6. Over-delegation audit

```text
Audit this workflow for:
- AI approving its own work;
- irreversible actions without approval;
- exact rules assigned to the model;
- prose-generated calculations;
- missing exception owners;
- unstated side effects;
- ceremonial human review; and
- halo delegation.

Recommend the smallest responsible correction.
```

## 7. Meaningful-human-review test

```text
For each collaborative or human-review stage, verify:
- named role;
- expertise;
- authority;
- evidence access;
- time;
- review criteria;
- intervention rights;
- recorded disposition.

Return Pass, Gap, or Not Applicable.
```

## 8. Feature assignment

```text
After the delegation map is approved, assign the minimum necessary feature:
- Project knowledge or instructions;
- Skill;
- code execution;
- deterministic rule;
- controlled tool;
- storage or system of record;
- human gate.

Explain why each feature fits the mapped responsibility.
```

## 9. Halo-delegation drill

```text
Identify where strong performance on one step is being used to justify delegation of a different step. Explain why the second step requires its own risk and authority assessment.
```

## 10. Irreversible-action boundary

```text
List every send, sign, file, payment, access change, publication, or system update in this workflow. Make each a separate stage and define required approval before execution.
```

## 11. Calculation boundary

```text
Identify every numeric step. Route exact calculations, transformations, totals, and reconciliation to code execution or deterministic logic. Define how the result will be reviewed.
```

## 12. Exception-route designer

```text
For ambiguous, conflicting, unsupported, or failed cases, define:
- trigger;
- evidence package;
- accountable exception owner;
- allowed actions;
- stopping rule;
- audit record.
```

## 13. Delegation map review card

```text
WORKFLOW OUTCOME:
[Outcome]

STEP:
[Atomic step]

WORK TYPE:
[Extraction / Synthesis / Calculation / Judgment / Approval / Action / Storage]

REVERSIBILITY:
[Easy / Moderate / Difficult]

STAKES:
[Low / Material / High]

ACCOUNTABLE ROLE:
[Role]

DELEGATION:
[AI / Code / Collaborative / Human / Deterministic / Tool / Storage]

VALIDATION:
[Check]

APPROVAL:
[Gate]

FAILURE PATH:
[Retry / Escalate / Stop / Rollback]
```

## 14. Oral certification drill

Answer each in two or three sentences:

1. Why map work before features?
2. What are the three Delegation criteria?
3. What is halo delegation?
4. When is a collaborative stage actually automated?
5. Why does code execution belong in numeric stages?
6. Why does a Skill not determine whether delegation is safe?
7. Which stages are normally human-retained?
8. What must happen before an irreversible action?
