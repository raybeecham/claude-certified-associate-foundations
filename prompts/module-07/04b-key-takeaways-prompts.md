# Module 7 Key Takeaways Prompts

Use these prompts to review diagnosis, feedback adjustment, durable promotion, and workflow optimization.

## 1. Four-takeaway recall

```text
Explain the four durable Module 7 takeaways in plain English:
1. Underperformance has discoverable causes.
2. Isolate before you fix.
3. Every disappointing output is data.
4. Optimize deliberately.

For each takeaway, provide:
- one sentence of meaning;
- one common mistake;
- one practical example; and
- one decision rule.
```

## 2. Cheapest-fix-first diagnosis

```text
Analyze this underperforming AI-assisted task:
[describe the task, prompt, output, timing, model, tools, context, and configuration]

Check the causes in this order:
1. under-specification;
2. context overload or drift;
3. wrong feature or model;
4. stale configuration;
5. expectation mismatch.

Return:
- expected behavior;
- observed behavior;
- most likely cause;
- evidence;
- cheapest discriminating test;
- alternate hypothesis;
- one bounded change;
- pass/fail criteria; and
- keep, revise, revert, or reshape decision.
```

## 3. Symptom-timing drill

```text
Classify each symptom as most consistent with under-specification, context overload, wrong feature/model, stale configuration, or expectation mismatch.

For each case:
- name the likely cause;
- explain why the timing matters;
- state what evidence would confirm it;
- give the first repair; and
- name one plausible alternate cause.

Cases:
[insert cases]
```

## 4. One-variable experiment

```text
Design a controlled troubleshooting experiment for this failure:
[describe failure]

Hold all nonessential variables constant.
Return:
- primary hypothesis;
- independent variable;
- controlled variables;
- baseline;
- test case;
- representative cases;
- success criteria;
- governance checks;
- rollback condition; and
- interpretation rules for each possible result.
```

## 5. Reaction-to-instruction translation

```text
Translate each vague reaction into an observable, testable instruction or control.

For each reaction, identify:
- observable defect;
- missing condition;
- controlling lever;
- exact adjustment;
- validation method; and
- whether the fix should remain local or be promoted.

Reactions:
- too generic;
- wrong tone;
- missed the point;
- inconsistent format;
- keeps omitting a required field;
- includes records that should be excluded.
```

## 6. Correct placement test

```text
Classify each recurring need as a rule, reference, procedure, deterministic control, human gate, or one-time detail.

Then place it in the correct home:
- current prompt;
- Project instruction;
- Project knowledge or governed source;
- Skill or workflow;
- code/query/schema/technical control; or
- human approval gate.

Explain why alternative locations would be fragile or inappropriate.

Needs:
[insert needs]
```

## 7. Promotion decision

```text
A correction worked in one conversation:
[describe correction and result]

Decide whether it should be promoted into configuration.
Assess:
- recurrence likelihood;
- who else needs it;
- correct configuration layer;
- scope;
- owner;
- representative tests;
- conflicts;
- approval;
- versioning;
- rollback; and
- review trigger.

Return: keep local, promote conditionally, or promote.
```

## 8. Workflow friction audit

```text
Audit this recurring workflow for removable friction:
[describe every step]

Identify:
- repetition;
- recurring correction;
- operator variance;
- duplicate research or calculation;
- manual formatting;
- waiting and handoffs;
- rework; and
- required governance controls that must remain.

Create an optimization backlog with:
- friction;
- root cause;
- rule/reference/procedure/control classification;
- proposed placement;
- expected benefit;
- risk;
- owner; and
- validation method.
```

## 9. Metric selection

```text
Select the primary optimization metric for this workflow:
[describe workflow and purpose]

Compare:
- cycle time;
- revision rounds;
- consistency;
- verified accuracy;
- defect rate;
- latency;
- cost;
- approval time; and
- user effort.

Return:
- primary metric;
- rationale;
- baseline method;
- target;
- guardrail metrics;
- stop condition; and
- what would count as a failed optimization.
```

## 10. Guarded pilot design

```text
Design a guarded pilot for this workflow optimization:
[describe current workflow and proposed change]

Include:
- retained baseline;
- pilot users;
- representative cases;
- edge cases;
- primary metric;
- quality and governance guardrails;
- success threshold;
- monitoring;
- rollback trigger;
- decision owner; and
- adopt, revise, or revert criteria.
```

## 11. Optimization distractor analysis

```text
A workflow has this measured bottleneck:
[describe bottleneck and metric]

Evaluate these proposed fixes:
[list fixes]

For each fix, state whether it:
- removes the bottleneck;
- shifts the work;
- improves an unrelated metric;
- weakens a control;
- adds maintenance burden; or
- lacks evidence.

Recommend the narrowest intervention that directly improves the target metric.
```

## 12. Diminishing-returns check

```text
Review this sequence of optimization rounds:
[provide rounds, metrics, costs, and defects]

Determine whether to continue, stop, revise, or roll back.
Consider:
- marginal gain;
- added complexity;
- maintenance burden;
- quality change;
- governance risk;
- user effort; and
- whether further tuning has become new friction.
```

## 13. Full Module 7 synthesis

```text
Given this recurring underperforming workflow:
[describe workflow]

Apply the complete Module 7 sequence:
1. define expected and observed behavior;
2. diagnose the likely cause;
3. isolate it with one bounded test;
4. translate feedback into a specific adjustment;
5. validate the repair;
6. decide whether to promote it;
7. instrument one full cycle;
8. identify repetition, correction, and variance;
9. apply the rule-reference-procedure test;
10. select target and guardrail metrics;
11. design a guarded pilot;
12. define rollback and stop conditions.

Return a concise decision record.
```

## 14. Oral certification drill

```text
Quiz me orally on Module 7.
Ask one scenario at a time and wait for my answer.
Cover:
- symptom timing;
- cheapest-fix-first diagnosis;
- one-variable testing;
- reaction versus instruction;
- promotion into configuration;
- rule/reference/procedure placement;
- bottleneck-targeted optimization;
- baseline and guardrail metrics;
- guarded rollout; and
- diminishing returns.

After each answer:
- grade it;
- identify the strongest reasoning;
- identify the missing distinction; and
- provide a model answer.
```

## Public-repository rule

Use fictional, generic, synthetic, public, or explicitly authorized scenarios. Do not paste confidential prompts, outputs, workflow timings, production logs, internal configuration, credentials, remembered live-exam questions, or reconstructed proprietary course content.
