# Module 6 Prompt Notebook: Appropriate vs Inappropriate Use Cases

Use fictional, synthetic, public, or explicitly authorized scenarios. Do not include confidential personnel, medical, legal, financial, or client decision records.

## 1. Four-criteria screening

```text
Evaluate this proposed AI use case:
[use case]

Assess:
- reversibility before consequence;
- consequence of error;
- need for human creativity, empathy, relationship, or professional judgment;
- accountability.

Then identify the load-bearing criterion and classify the use case as:
- fully appropriate;
- appropriate with human review; or
- inappropriate.

Explain the rationale without relying on technical capability alone.
```

## 2. Load-bearing criterion test

```text
For this use case:
[scenario]

Run all four Delegation criteria.
Then answer:
- Which criterion controls the classification?
- What hypothetical change to that criterion would move the classification?
- Why are the other criteria relevant but not controlling?
```

## 3. Human-gate design

```text
This use case has been classified as appropriate with human review:
[use case]

Define the gate in who / what / when form.
Include:
- accountable reviewer role;
- evidence available;
- specific risks or criteria reviewed;
- timing before consequence;
- authority to reject or modify;
- escalation path; and
- retained approval evidence.

Reject vague language such as `someone checks it`.
```

## 4. Gate adequacy audit

```text
Audit this proposed human gate:
[gate]

Check whether it defines:
- who reviews;
- reviewer expertise and accountability;
- what is verified;
- evidence access;
- when review occurs;
- authority to intervene;
- exception path; and
- proof of approval.

Return: adequate / incomplete / ceremonial.
```

## 5. Fully appropriate classification

```text
Determine whether this use case is fully appropriate:
[scenario]

Require evidence that it is:
- reversible before use;
- low consequence;
- grounded in suitable sources;
- not dependent on special human empathy or authority; and
- subject to normal quality review.

Identify any condition that would move it into human-reviewed status.
```

## 6. Inappropriate-use rationale

```text
Evaluate whether this use case should remain human-owned:
[scenario]

Identify:
- irreversible or difficult-to-remedy consequences;
- non-transferable professional or organizational accountability;
- essential human relationship or empathy;
- policy or fairness constraints;
- whether meaningful pre-use review is possible; and
- the human role that must retain ownership.

Use criterion-based language rather than `it feels risky`.
```

## 7. AI assistance versus ownership

```text
Decompose this use case into:
- AI-assistable preparation tasks;
- collaborative tasks;
- human-retained decisions;
- prohibited or unsuitable tasks.

For each, explain why assistance does or does not transfer accountability.
```

## 8. Portfolio classification

```text
Classify each use case in this portfolio:
[list]

For each provide:
- classification;
- four-criteria summary;
- load-bearing criterion;
- human gate or retained role;
- required conditions; and
- decision owner.
```

## 9. Condolence and relationship test

```text
A low-stakes, reversible communication task involves grief, trust, conflict, or a sensitive relationship.

Evaluate why reversibility and low consequence may not be sufficient for full delegation.
Identify the human-element criterion and define the appropriate AI-assistance boundary.
```

## 10. Consequential summary gate

```text
An AI-generated financial, operational, or compliance summary feeds a consequential decision.

Design controls for:
- source verification;
- calculation checks;
- qualified review;
- timing before use;
- decision authority;
- exception handling; and
- retained evidence.
```

## 11. Employment fairness review

```text
Evaluate this AI-assisted hiring workflow:
[workflow]

Assess:
- job relevance;
- unsupported inference;
- fairness and adverse-impact risk;
- accountability;
- candidate recourse;
- policy restrictions; and
- who / what / when review gate.

Do not assume a human reviewer automatically makes the workflow appropriate.
```

## 12. Customer communication boundary

```text
Evaluate an AI-drafted customer response involving billing, account access, or a disputed charge.

Identify:
- reversibility before send;
- consequence of factual error;
- relationship and tone concerns;
- company accountability;
- source-of-truth checks; and
- the required pre-send gate.
```

## 13. Classification stress test

```text
Take this classification and challenge it:
[classification and rationale]

Ask:
- Which assumption is weakest?
- Is the gate operational?
- Is review before consequence?
- Can accountability truly be exercised?
- Could harm realistically be reversed?
- Is a human element being understated?
- Would a policy or data constraint override the result?
```

## 14. Decision record

```text
Create a use-case appropriateness decision record with:
- use-case ID and owner;
- bounded purpose;
- users and affected parties;
- reversibility;
- consequence of error;
- human creativity or empathy requirement;
- accountability;
- load-bearing criterion;
- classification;
- human gate or retained role;
- policy and data conditions;
- monitoring and escalation;
- approver; and
- next review date.
```

## 15. Oral certification drill

```text
Give me five short scenarios one at a time.
Require me to state:
1. the classification;
2. the load-bearing criterion;
3. the who / what / when gate or retained human role.

After each answer, explain the strongest rationale and the most tempting distractor.
```
