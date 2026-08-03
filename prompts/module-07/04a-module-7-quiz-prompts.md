# Module 7 Quiz and Remediation Prompts

Use these prompts to practice troubleshooting and optimization judgment with fictional or sanitized scenarios.

## 1. Classify the symptom

```text
Analyze this underperforming workflow.

Expected behavior:
[describe]

Observed behavior:
[describe]

Timing:
[first response / degraded over time / repeatable error / used to work / persistent mismatch]

Classify the most likely cause as:
- under-specification;
- context overload;
- wrong feature or model;
- stale configuration; or
- expectation mismatch.

Explain the evidence, the cheapest controlled test, and one alternate hypothesis.
```

## 2. Audit the task specification

```text
Review this prompt against:
1. objective;
2. context and evidence;
3. constraints;
4. output format; and
5. success criteria.

Identify only the missing elements that could explain the observed defect. Do not rewrite unrelated parts.
```

## 3. Test model fit

```text
Design a controlled comparison to determine whether this task is mismatched to the selected model.

Hold constant:
- prompt;
- evidence;
- tools;
- configuration; and
- evaluation cases.

Change only the model. Define quality, latency, and cost metrics and a keep/revert rule.
```

## 4. Run the cheapest-fix-first sequence

```text
Apply this sequence to the scenario:
1. specification;
2. context;
3. feature and model fit;
4. configuration;
5. task fit.

At each stage, state:
- the evidence to inspect;
- the minimum test;
- the possible repair; and
- the condition for moving to the next stage.
```

## 5. Translate recurring feedback

```text
Feedback: [too generic / wrong tone / missing field / inconsistent structure / other]

Convert the reaction into:
- observable defect;
- missing condition;
- controlling lever;
- one bounded change;
- validation cases; and
- local-fix versus durable-promotion decision.
```

## 6. Choose the durable home

```text
Classify each recurring requirement as:
- one-time detail;
- rule;
- reference;
- procedure;
- deterministic logic; or
- human approval.

Place it in:
- current prompt;
- instruction;
- maintained knowledge;
- Skill/workflow;
- code/query/schema/control; or
- human gate.

Explain why the other locations are weaker.
```

## 7. Identify the bottleneck

```text
Workflow steps and timings:
[paste fictional measurements]

Optimization objective:
[state the metric]

Identify:
- measured bottleneck;
- repetition, correction, or variance;
- proposed intervention;
- primary metric;
- guardrail metrics;
- pilot design; and
- rollback condition.
```

## 8. Reject general-speed distractors

```text
A proposed optimization upgrades the model, adds another reviewer, or starts work earlier.

Determine whether it removes the measured bottleneck or merely shifts work. Compare it with a source-level repair.
```

## 9. Design a guarded pilot

```text
Create a pilot plan for this workflow optimization.

Include:
- baseline;
- representative users and cases;
- primary metric;
- quality and governance guardrails;
- number of cycles;
- old-path availability;
- approval owner;
- adoption threshold;
- rollback trigger; and
- post-adoption monitoring.
```

## 10. Diagnose formatting variance

```text
Several operators produce accurate content in different formats, creating reconciliation work.

Explain why the root cause is variance, identify the correct shared procedure or template control, and define how to measure the reduction in reconciliation time.
```

## 11. Oral certification drill

Answer each in 30–60 seconds:

1. Why does first-response failure point toward under-specification?
2. When is a model change justified?
3. Why is the diagnostic sequence ordered cheapest-fix-first?
4. When should a recurring correction be promoted?
5. How do you distinguish a rule, reference, and procedure?
6. Why is adding reviewers not necessarily optimization?
7. What proves an optimized workflow is better?
8. When should optimization stop?

## 12. Generate original practice cases

```text
Create five original Module 7 scenario questions.

Cover:
- under-specification;
- model or feature mismatch;
- diagnostic sequencing;
- durable promotion; and
- bottleneck-targeted optimization.

Use fictional scenarios, four answer choices, one best answer, and an explanation that names the controlling concept. Do not imitate proprietary course wording.
```

## Result record

```text
Module 7 quiz: Full marks — 5 of 5
Competencies demonstrated:
- root-cause classification;
- diagnostic sequencing;
- model and feature fit;
- persistent correction capture; and
- measured workflow optimization.
```