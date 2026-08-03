# Module 6 Prompt Notebook: Data Sensitivity, Privacy & Feature Controls

Use fictional, synthetic, public, or explicitly authorized data descriptions. Do not paste regulated records, credentials, secrets, private customer data, confidential deal information, or proprietary datasets into these prompts.

## 1. Green / Yellow / Red classification

```text
Classify each data item as:
- Green: safe to use under normal controls;
- Yellow: review first;
- Red: keep out unless an approved path exists.

For each item, explain:
- owner;
- sensitivity;
- affected people;
- contractual or regulatory concern;
- uncertainty;
- required approval; and
- the safest next action.

When evidence is insufficient, use the more sensitive tier.

Data items:
[list]
```

## 2. Minimum-necessary-data review

```text
The proposed task is:
[task]

The available fields are:
[field list]

Identify:
- fields required for the task;
- fields that can be removed;
- fields that can be aggregated;
- fields that can be pseudonymized;
- credentials or secrets that must never be included;
- residual re-identification risk; and
- whether the task should use synthetic data instead.
```

## 3. Redaction audit

```text
Review this fictional or sanitized record for direct and indirect identifiers:
[record]

Check for:
- names;
- email and phone;
- account or employee identifiers;
- precise dates;
- locations;
- rare titles or attributes;
- small-population combinations;
- free-text identifiers; and
- linked reference numbers.

Return:
1. remaining identification risks;
2. proposed transformation;
3. analytical information lost;
4. whether the task remains valid; and
5. whether an approved environment is still required.
```

## 4. Redaction-versus-validity decision

```text
Determine whether redaction is suitable for this task:
[task and data description]

Answer:
- Which sensitive specifics are genuinely necessary?
- Which can be removed without changing the result?
- Would pseudonyms preserve relational analysis?
- Would aggregation create misleading results?
- Does de-identification still permit re-identification?
- Should the task be redesigned, moved to an approved environment, or stopped?
```

## 5. Processing approval versus persistence controls

```text
For this proposed use:
[description]

Separate two decisions:

A. Processing authorization
- Is this data class allowed in the selected account, product, plan, and entry point?
- Which policy, agreement, or approval establishes that?

B. Persistence controls
- Should it enter chat history?
- Should Memory use it?
- Could it appear in organization exports?
- What retention, deletion, and audit rules apply?

Do not use an Incognito or Memory setting as evidence that processing is authorized.
```

## 6. Incognito suitability review

```text
Assess whether Incognito is an appropriate control for this scenario:
[scenario]

Classify:
- underlying data tier;
- whether processing is allowed at all;
- whether ordinary chat history should be avoided;
- whether Memory should be excluded;
- organizational retention or export implications;
- additional required controls; and
- final disposition: use, use with conditions, or do not use.
```

## 7. Code-execution sandbox preflight

```text
Create a preflight checklist before processing this sanitized file with code execution:
[file and task description]

Include:
- approved environment;
- minimum necessary columns;
- sensitive fields to remove;
- secrets scan;
- network or package considerations;
- generated-output review;
- temporary artifact handling;
- logging and retention;
- human validation of calculations; and
- deletion or archival after completion.
```

## 8. Memory persistence decision

```text
For each item below, decide whether it belongs in:
- Project knowledge;
- scoped Memory;
- an authoritative system of record;
- the current conversation only; or
- nowhere in Claude.

Evaluate stability, sensitivity, authority, retention, staleness risk, user visibility, and deletion needs.

Items:
[list]
```

## 9. Plan and organization control check

```text
Create a verification checklist for a user who is unsure which Claude organization, plan, retention policy, Memory controls, export capabilities, and feature permissions apply.

Do not assume current settings from plan labels alone.
Include:
- active account and organization;
- product entry point;
- feature enablement;
- administrator owner;
- retention and export;
- Memory and history behavior;
- approved data classes;
- contractual or compliance status; and
- escalation contact.
```

## 10. Four-case classification drill

```text
Classify and justify these fictional cases:
1. anonymized survey trends;
2. confidential acquisition draft;
3. customer spreadsheet with personal identifiers;
4. regulated patient records.

For each, provide:
- Green / Yellow / Red;
- minimum necessary data;
- valid redaction or anonymization steps;
- feature-control options;
- what the controls do not solve;
- required approval; and
- final action.
```

## 11. Feature-control mismatch audit

```text
Review this proposed configuration:
[configuration]

Find mismatches such as:
- Incognito used as compliance approval;
- sandbox treated as data authorization;
- Memory used as a sensitive system of record;
- regulated data uploaded before approval;
- static retention assumptions;
- missing organization-export awareness;
- overbroad connector or file access; and
- secrets included in prompts or files.

Return the smallest responsible repair for each issue.
```

## 12. Data decision record

```text
Create a concise data-processing decision record with:
- task;
- data owner;
- data classification;
- minimum necessary fields;
- processing environment;
- policy or approval basis;
- redaction or anonymization;
- feature controls;
- retention and deletion;
- human reviewer;
- residual risks;
- escalation path;
- decision: approve, constrain, redesign, defer, or reject; and
- next review date.
```

## 13. Adversarial re-identification test

```text
Given this sanitized fictional dataset description:
[description]

Attempt a privacy-oriented challenge review:
- Which record combinations could identify a person?
- Which small groups are too distinctive?
- Which external knowledge could reconnect pseudonyms?
- Which free-text fields may leak identity?
- Which transformations reduce risk?
- At what point would the analysis become invalid?

Do not claim formal anonymization without sufficient evidence.
```

## 14. Oral certification drill

```text
Ask me one scenario question at a time about:
- Green / Yellow / Red classification;
- minimization;
- partial redaction;
- redaction that breaks the task;
- sandbox limits;
- Incognito and organizational retention;
- Memory persistence;
- regulated-data escalation; or
- plan and organization controls.

After each answer, grade the reasoning and explain the load-bearing governance issue.
Do not reproduce proprietary exam questions.
```

## Compact recall

```text
Classify first.
Confirm the approved environment.
Minimize what enters.
Redact only when task validity survives.
Choose feature and persistence controls.
Remember: Incognito is not authorization.
Stop when no approved path exists.
```
