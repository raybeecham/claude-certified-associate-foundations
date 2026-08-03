# Module 4 — Communicating Value and Limitations Prompts

Use fictional, generic, synthetic, public, or explicitly authorized workflow details.

## 1. Capability-boundary statement

```text
Describe this workflow for stakeholders using five fields:
1. what Claude does;
2. what Claude does not do;
3. who reviews or approves;
4. what measured value has been observed;
5. what material limitations remain.

Avoid broad phrases such as `handles`, `fully automated`, `guarantees`, or `human-level`.
```

## 2. Overstatement repair

```text
Rewrite each claim as a bounded operational description.
For each, identify what the original statement hid.

Claims:
- Our AI reviews contracts automatically.
- Claude handles onboarding.
- The system eliminates errors.
- It is basically as good as an expert.
```

## 3. Three-audience versions

```text
Using the same verified workflow facts, produce three versions:
- legal or technical lead;
- practice executive;
- client risk function.

Preserve the capability boundary, metrics, limitations, and human gates.
Change only depth, vocabulary, order, and emphasis.
```

## 4. Invariant-content audit

```text
Compare these audience versions.
Identify any change to:
- scope;
- metric;
- uncertainty;
- limitation;
- review gate;
- approval authority;
- data boundary; or
- external-action model.

Flag any audience adaptation that becomes concealment or overstatement.
```

## 5. Value-evidence ledger

```text
For each claimed benefit, return:
- metric definition;
- baseline;
- comparison period;
- sample or case scope;
- source system;
- quality standard;
- exception or correction rate;
- known confounders;
- safe claim wording.

Mark unsupported claims as `not established`.
```

## 6. Pilot-to-scale calibration

```text
A pilot succeeded on standard cases.
Create:
1. the strongest claim the evidence supports;
2. claims the evidence does not support;
3. dependencies for expansion;
4. monitoring needed at larger scale;
5. the decision an executive must make.
```

## 7. Human-oversight specification

```text
Turn the phrase `human review is included` into an operational control.
Specify:
- reviewer role and expertise;
- evidence available;
- items reviewed;
- decision criteria;
- authority to reject or stop;
- exception route;
- timing before external action;
- retained approval evidence.
```

## 8. Risk-function briefing

```text
Draft a concise assurance description for a risk function.
Cover:
- AI-assisted steps;
- prohibited or human-retained decisions;
- data and source scope;
- validation;
- review and approval;
- external actions;
- known failure modes;
- escalation and incident ownership.
```

## 9. Executive briefing

```text
Draft an executive description that leads with:
- business outcome;
- measured value and scope;
- retained oversight;
- principal limitation;
- next decision.

Do not remove uncertainty or human dependencies for brevity.
```

## 10. Technical-lead briefing

```text
Draft a technical or professional-lead description including:
- workflow stages;
- source boundaries;
- model-owned tasks;
- deterministic checks;
- human gates;
- known failure modes;
- exception routing;
- evidence retained.
```

## 11. Quiet-overstatement scan

```text
Scan the supplied stakeholder copy for these patterns:
- fully automated;
- handles X;
- guarantees;
- eliminates risk or error;
- as good as a person;
- intelligent decision-making;
- human review included.

For each, explain the hidden assumption and propose bounded replacement wording.
```

## 12. Limitation prioritization

```text
Classify limitations as:
- decision-relevant and must disclose;
- operational detail for specialist audiences;
- generic disclaimer with low decision value.

Explain why each classification fits the audience and decision.
```

## 13. Assurance-theater test

```text
Review the listed controls.
For each control, require:
- owner;
- trigger;
- evidence;
- authority;
- timing;
- intervention right;
- retained record.

Mark controls without these properties as `not operationalized`.
```

## 14. Communication register

```text
Create a register with:
Audience | Decision needed | Capability | Exclusions | Evidence | Scope |
Controls | Limitations | Escalation | Message owner | Review date
```

## 15. Oral certification drill

```text
Give me five short scenarios about communicating AI workflow value.
Ask me for the best stakeholder message.
After each answer, assess whether I:
- bounded the capability;
- preserved human authority;
- scoped the evidence;
- disclosed material limitations;
- calibrated to the audience;
- avoided overstatement.
```

## Compact communication card

```text
TASK      → What does Claude actually do?
BOUNDARY  → What does it not decide or execute?
EVIDENCE  → What measured value is supported, under what scope?
CONTROL   → Who reviews, approves, monitors, or intervenes?
LIMIT     → What failure mode or dependency matters?
AUDIENCE  → What depth and emphasis does this stakeholder need?
OWNER     → Who is accountable for the statement?
```
