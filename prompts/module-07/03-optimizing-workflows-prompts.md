# Module 7: Optimizing Workflows — Prompt Notebook

These prompts support workflow instrumentation, friction analysis, configuration placement, measured rollout, and optimization review.

Use fictional, synthetic, public, or explicitly authorized scenarios.

---

## 1. Observe one full workflow cycle

```text
Analyze this recurring workflow as an efficiency auditor.

Workflow:
[describe the steps]

For each step, record:
- manual action;
- repeated input;
- repeated correction;
- handoff or waiting time;
- verification performed;
- variation between users;
- estimated effort;
- likely root cause; and
- candidate optimization.

Return an optimization backlog ordered by expected value and risk.
Do not recommend removing required governance or human-review controls.
```

---

## 2. Classify friction signals

```text
Classify each observed friction as:
- repetition;
- correction;
- variance;
- required control;
- one-time exception; or
- uncertain.

For each item, explain:
1. why the classification fits;
2. whether the step is removable, reducible, or required;
3. the likely root cause; and
4. the smallest responsible intervention.
```

---

## 3. Build a friction register

```text
Convert these observations into a friction register with columns:
- step;
- manual action;
- frequency;
- time cost;
- quality impact;
- users affected;
- root cause;
- candidate fix;
- success metric;
- risk;
- owner; and
- status.

Observations:
[paste authorized observations]
```

---

## 4. Apply the rule–reference–procedure test

```text
For each proposed reusable fix, classify it as:
- rule;
- reference;
- procedure;
- deterministic business logic;
- one-time detail; or
- unclear.

Map each classification to the correct home:
- Project or standing instruction;
- governed knowledge or source;
- Skill or workflow;
- code, query, schema, or technical control;
- current prompt; or
- further analysis.

Explain why the other layers would be weaker or riskier.
```

---

## 5. Audit configuration placement

```text
Review this configured workflow for misplaced content.

Configuration:
[paste sanitized description]

Identify:
- procedures compressed into vague instructions;
- references embedded in instructions;
- exact business rules implemented only in prose;
- one-time details promoted too broadly;
- duplicated authority across layers;
- stale or ownerless configuration; and
- missing rollback or review dates.

Recommend the minimum placement changes.
```

---

## 6. Consolidation review

```text
Review these workflow steps for consolidation opportunities.

Steps:
[list steps]

For each possible consolidation:
- state the benefit;
- identify any permission, review, or data boundary;
- explain whether the steps may safely run together;
- name the new failure mode introduced; and
- provide a rollback plan.

Do not merge stages that require independent approval or different access scopes.
```

---

## 7. Select optimization metrics

```text
Choose the most appropriate primary and secondary metrics for this workflow.

Workflow purpose:
[describe purpose]

Candidate metrics:
- time per cycle;
- revision rounds;
- defect rate;
- consistency across users;
- completeness;
- verified accuracy;
- latency;
- cost;
- approval time;
- user effort;
- governance exceptions.

Explain:
1. which metric best reflects the workflow's purpose;
2. which metrics act as guardrails;
3. what baseline is needed;
4. what improvement threshold is meaningful; and
5. when optimization should stop.
```

---

## 8. Design a guarded pilot

```text
Design a pilot for this proposed workflow optimization.

Baseline:
[describe current process]

Proposed change:
[describe optimization]

Include:
- representative cases;
- participating users;
- baseline metrics;
- target metrics;
- quality and governance guardrails;
- edge cases;
- duration or number of cycles;
- approval owner;
- rollback conditions; and
- adopt, revise, or revert criteria.
```

---

## 9. Compare baseline and optimized workflow

```text
Compare the baseline and optimized workflow using the supplied evidence.

Baseline results:
[data]

Optimized results:
[data]

Evaluate:
- time;
- revision cycles;
- consistency;
- verified accuracy;
- defect rate;
- cost;
- user effort;
- governance impact; and
- maintenance burden.

Return:
1. measured gains;
2. regressions;
3. uncertainty;
4. whether the result generalizes; and
5. adopt, revise, or revert recommendation.
```

---

## 10. Detect false optimization

```text
Determine whether this change is a real optimization or merely moves work elsewhere.

Change:
[describe change]

Check whether it:
- saves time for one role while increasing work for another;
- removes visible steps but creates hidden rework;
- improves speed while reducing accuracy;
- standardizes an unvalidated workaround;
- increases maintenance or permission scope;
- weakens review, fairness, privacy, or accountability; or
- creates operator dependence elsewhere.

Explain the net effect.
```

---

## 11. Weekly reporting audit

```text
A fictional team spends 45 minutes per analyst on a weekly report.
Each analyst:
- repastes the same background;
- reformats the report manually; and
- performs a different set of checks.

Use the rule–reference–procedure test to design an optimized workflow.
Include:
- placement of each fix;
- baseline and target metrics;
- pilot plan;
- quality guardrails;
- governance checks;
- rollback conditions; and
- final decision criteria.
```

---

## 12. Promotion decision

```text
Evaluate whether this proposed improvement should be promoted into shared configuration.

Proposed fix:
[describe fix]

Assess:
- recurrence;
- number of users affected;
- evidence that the fix works;
- correct configuration home;
- ownership;
- versioning;
- conflict risk;
- testing;
- approval;
- rollback; and
- review cadence.

Return: keep local, pilot, promote, revise, or reject.
```

---

## 13. Diminishing-returns review

```text
Review this optimization program for diminishing returns.

Current baseline and results:
[data]

Remaining proposed changes:
[list]

Identify:
- gains already achieved;
- marginal benefit of each remaining change;
- added complexity;
- maintenance cost;
- regression risk;
- governance impact; and
- recommended stop condition.
```

---

## 14. Workflow optimization decision record

```text
Create a workflow optimization decision record with:
- workflow and owner;
- business objective;
- baseline;
- friction observed;
- root cause;
- proposed change;
- rule/reference/procedure classification;
- selected configuration layer;
- pilot design;
- success metrics;
- guardrails;
- test results;
- governance review;
- rollback plan;
- final disposition; and
- next review date.
```

---

## 15. Oral certification drill

```text
Act as a certification examiner.
Give me one short workflow-optimization scenario at a time.

Require me to:
1. identify repetition, correction, or variance;
2. classify the fix as a rule, reference, or procedure;
3. select the correct configuration layer;
4. choose a meaningful metric;
5. design a guarded pilot; and
6. decide whether to adopt, revise, or revert.

After I answer, grade the reasoning and provide a stronger response.
```

---

# Compact recall card

```text
Observe one full cycle.
Record repetition, correction, and variance.
Classify each fix as rule, reference, or procedure.
Place it in the correct maintained layer.
Select the metric before changing the workflow.
Pilot with the baseline still available.
Measure quality, consistency, time, cost, and governance.
Adopt, revise, or revert.
Stop when additional complexity exceeds the gain.
```