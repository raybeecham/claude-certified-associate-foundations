# Module 3 Notebook: Triage the Output Set

Use these prompts to practice rapid output disposition. The goal is to distinguish correctable defects from mandatory human-review gates.

---

## 1. Three-verdict triage

```text
Classify the output as:
- Ready to use;
- Needs revision; or
- Needs human override.

Evaluate:
1. requirements;
2. source support;
3. professional standards;
4. accuracy and completeness;
5. internal consistency and bias;
6. stakes;
7. reversibility;
8. audience; and
9. regulatory, contractual, or policy exposure.

Return:
- verdict;
- one controlling reason;
- next action; and
- unresolved uncertainty.
```

---

## 2. Two-axis matrix

```text
Evaluate this output on two axes.

Axis 1 — Output condition:
- accurate;
- complete;
- supported;
- consistent;
- fair;
- usable.

Axis 2 — Intended-use risk:
- consequence if wrong;
- reversibility;
- audience;
- governing obligations;
- required authority.

Place the scenario in a matrix and select the triage verdict.
```

---

## 3. Appearance-versus-risk drill

```text
For each scenario, separately score:
- surface polish;
- evidence quality;
- output defects;
- use risk; and
- required review level.

Identify cases where:
- rough output is low risk;
- polished output is high risk;
- bounded defects require revision; or
- mandatory review applies despite strong apparent quality.
```

---

## 4. Low-stakes brainstorm

```text
Scenario:
An internal workshop list is clearly provisional, contains several strong ideas and several generic ones, and will not be distributed externally.

Apply the triage protocol. Explain whether light editing, revision, or human override is proportionate.
```

---

## 5. Contradictory-total drill

```text
Scenario:
A summary total does not equal the visible line items.

Identify:
- the failure type;
- why prose regeneration is insufficient;
- the authoritative inputs needed;
- the deterministic calculation required;
- downstream claims to recheck; and
- the triage verdict.
```

---

## 6. Unsupported-statistics drill

```text
Scenario:
A brief contains precise percentages and growth claims without checkable sources.

For each claim, require:
- source;
- location;
- publication date;
- population and scope;
- methodology where relevant;
- support status; and
- keep, qualify, remove, or escalate action.

Then assign the triage verdict.
```

---

## 7. Regulatory-output drill

```text
Scenario:
A professionally written draft is intended for a regulator. Several claims have been spot-checked and appear accurate.

Apply:
- stakes;
- reversibility;
- audience;
- governing obligations;
- completeness risk;
- reviewer qualifications;
- approval evidence; and
- timing of the review gate.

Explain why spot-checking and polish do not satisfy the release requirement.
```

---

## 8. Verdict-plus-action formatter

```text
Write the triage finding in one sentence:

[VERDICT] because [CONTROLLING REASON]; next, [REQUIRED ACTION].

Then add:
- evidence needed;
- reviewer owner; and
- release blocker.
```

---

## 9. Revision-versus-override diagnostic

```text
Determine whether the defect should be revised within the workflow or escalated to human override.

Choose revision when:
- the defect is bounded;
- evidence and tools are available;
- authority is sufficient; and
- the use is not behind a mandatory gate.

Choose human override when:
- consequences are high;
- the action is difficult to reverse;
- governing obligations apply;
- qualified authority is missing;
- evidence is materially insufficient; or
- professional judgment is required.
```

---

## 10. Triage-to-five-actions mapping

```text
Map the three exercise verdicts to the wider release actions:

Ready to use → Release
Needs revision → Edit and/or Verify
Needs human override → Escalate, Reconstruct, or Reject

Explain which wider action is appropriate and why.
```

---

## 11. Spot-checking critique

```text
Assess whether spot-checking is adequate for this use case.

Consider:
- total claim count;
- claim materiality;
- completeness risk;
- source coverage;
- calculation risk;
- audience;
- governing requirements; and
- consequence if an unchecked claim is wrong.

Define the full review standard required.
```

---

## 12. Triage under time pressure

```text
You have two minutes to triage this output.

Use this order:
1. intended use;
2. automatic human-review gates;
3. material contradictions or unsupported claims;
4. calculation risk;
5. source coverage;
6. verdict and next action.

State what a fuller review must examine later.
```

---

## 13. Confidence-trap drill

```text
Identify any reasoning that relies on:
- polished appearance;
- confident tone;
- many citations;
- long output;
- agreement across model runs;
- a human merely being present; or
- a claimed external action.

Replace each weak signal with the evidence or control actually required.
```

---

## 14. Triage log

```text
Create a triage record containing:
- output identifier;
- intended use;
- audience;
- output condition findings;
- use-risk findings;
- controlling issue;
- verdict;
- next action;
- owner;
- evidence needed;
- review deadline; and
- final disposition.
```

---

## 15. Original four-case generator

```text
Create four new fictional triage cases:
1. low-stakes rough internal draft;
2. bounded calculation or consistency defect;
3. unsupported factual-claim defect; and
4. polished high-stakes governed output.

Do not reuse proprietary course wording. Include answer key and reasoning after a divider.
```

---

## 16. Oral certification drill

Answer each in two or three sentences:

1. What are the three triage verdicts?
2. What are the two triage axes?
3. Why can a messy output be ready to use?
4. Why can a polished output require human override?
5. When is revision preferable to escalation?
6. Why should conflicting totals be recomputed with code?
7. What makes precise statistics auditable?
8. Why is spot-checking insufficient for a regulatory filing?
9. What should every verdict include?
10. How do the three verdicts map to release, edit, verify, escalate, and reject?

---

# Compact triage card

```text
INTENDED USE
[Audience / Decision / Draft or Final]

OUTPUT CONDITION
[Requirements / Support / Accuracy / Completeness / Consistency / Bias / Format]

USE RISK
[Stakes / Reversibility / Audience / Governing Obligations]

CONTROLLING ISSUE
[ONE SENTENCE]

VERDICT
[Ready to use / Needs revision / Needs human override]

NEXT ACTION
[Release / Edit / Verify / Escalate / Reject]

OWNER AND EVIDENCE
[ROLE / SOURCES / CALCULATION / APPROVAL]
```
