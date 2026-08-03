# Module 7 — Diagnosing Underperformance Prompts

Use these prompts to practice failure localization rather than random prompt tweaking.

## 1. Classify the failure

```text
Analyze this underperforming Claude workflow.

Expected behavior:
[describe]

Observed behavior:
[describe]

Timing:
[first response / degraded over time / repeatable error / used to work / persistent mismatch]

Prompt:
[paste]

Context and configuration:
[describe]

Classify the primary hypothesis as:
- under-specification;
- context overload;
- wrong feature or model;
- stale configuration; or
- expectation mismatch.

Explain the evidence, identify the cheapest next test, and avoid recommending multiple simultaneous changes.
```

## 2. Five-component prompt audit

```text
Audit this prompt against five components:
1. objective;
2. context and evidence;
3. constraints;
4. output format; and
5. success criteria.

For each component, mark:
- present and adequate;
- present but ambiguous; or
- missing.

Recommend only the minimum additions needed to test whether under-specification is the cause.
```

## 3. Symptom-timing diagnosis

```text
Given the scenario below, use symptom timing to rank the likely causes.

Scenario:
[describe]

Rank:
1. most likely cause;
2. second likely cause;
3. less likely causes.

For the top cause, provide one controlled test. Explain why timing is evidence but not proof.
```

## 4. Context-overload check

```text
Review this long-session failure.

What worked earlier:
[describe]

What degraded later:
[describe]

Current authoritative instructions:
[list]

Identify:
- conflicting or irrelevant context;
- information that should be restated;
- information that belongs in a clean transfer summary;
- stable rules that should move into Project instructions or another persistent layer; and
- the smallest clean restart package.
```

## 5. Clean restart summary

```text
Create a clean restart summary containing only:
- objective;
- current state;
- authoritative constraints;
- source boundaries;
- required format;
- accepted decisions;
- unresolved questions; and
- next action.

Exclude obsolete discussion, failed experiments, and superseded instructions.
```

## 6. Feature-fit diagnostic

```text
Determine whether this task is using the wrong capability.

Task:
[describe]

Current entry point, model, and tools:
[describe]

Observed error:
[describe]

Assess whether the task requires:
- code execution;
- structured extraction;
- a connector or uploaded source;
- a deeper-reasoning model;
- a faster model;
- a different entry point; or
- no feature change.

Recommend the smallest capability change that directly addresses the diagnosed limitation.
```

## 7. Quantitative-error diagnostic

```text
A Claude response contains subtly wrong numbers.

Inputs:
[paste]

Expected calculation:
[describe]

Output received:
[paste]

Separate:
- arithmetic or aggregation errors;
- source-data errors;
- unit or definition mismatches;
- rounding choices;
- unsupported assumptions; and
- presentation errors.

Design a deterministic code-execution check and specify what must be verified by a human.
```

## 8. Model-fit review

```text
Assess whether model selection is the root cause of this underperformance.

Task requirements:
[describe depth, speed, cost, context, and reliability]

Current model behavior:
[describe]

Before recommending a different model, rule out:
- missing task specification;
- context problems;
- wrong feature choice;
- stale configuration; and
- unavailable evidence.

Then recommend keep, upgrade, downgrade, or route exceptions, with a validation plan.
```

## 9. Stale-configuration audit

```text
This workflow used to work and now underperforms.

Inventory and review:
- Project instructions;
- uploaded knowledge and source versions;
- Skills and dependencies;
- connectors and permissions;
- Memory;
- schemas and templates;
- review gates;
- policy references; and
- product or feature changes.

For each item, record:
- current version;
- expected behavior;
- evidence of drift;
- corrective action; and
- regression test.
```

## 10. Expectation-mismatch test

```text
Evaluate whether this requested outcome is realistically available.

Request:
[paste]

Assess:
- whether the result is knowable;
- whether the evidence exists;
- whether the selected feature can perform the action;
- whether professional or organizational judgment must remain human;
- whether certainty is being requested beyond the evidence; and
- whether the task can be reframed.

Return:
1. feasible as written;
2. feasible with controls;
3. needs reshaping; or
4. inappropriate or impossible.

Provide a bounded alternative when reshaping is required.
```

## 11. Exact-prediction repair

```text
Rewrite this exact future-prediction request into a responsible analytical task.

Original request:
[paste]

Replace the exact prediction with:
- scenario range;
- explicit assumptions;
- adjustable drivers;
- sensitivity analysis;
- confidence limits;
- missing evidence; and
- human decision ownership.
```

## 12. Minimal reproducible case

```text
Create a minimal reproducible case for this Claude failure.

Include only:
- expected behavior;
- observed behavior;
- exact prompt;
- minimum required context;
- model and entry point;
- enabled tools;
- relevant configuration version;
- source version;
- repeat steps; and
- pass/fail criteria.

Remove unrelated context and confidential details.
```

## 13. One-variable experiment

```text
Design a controlled troubleshooting experiment.

Primary hypothesis:
[describe]

Baseline:
[describe]

Change exactly one variable.

Define:
- experimental change;
- held-constant variables;
- representative cases;
- success metric;
- governance checks;
- rollback condition; and
- keep / revise / revert decision rule.
```

## 14. Failure gallery drill

```text
Classify each case and name the first repair:

1. The first summary omits decision criteria.
2. A long chat stops following an early format rule.
3. Totals are consistently off by small amounts.
4. A formerly reliable Project produces outdated language.
5. A user asks for next quarter's exact sales number.

For each, provide:
- primary diagnosis;
- timing clue;
- one controlled test; and
- smallest repair.
```

## 15. Distractor analysis

```text
For this troubleshooting scenario, explain why each common reaction may be wrong:
- switch immediately to the strongest model;
- rewrite the entire prompt;
- add more context;
- enable more tools;
- continue in the same long chat;
- conclude the task is impossible.

Then give the cheapest-fix-first sequence.
```

## 16. Governance-preserving repair

```text
Review this proposed performance fix.

Proposed fix:
[describe]

Check whether it weakens:
- data boundaries;
- least privilege;
- Skill or connector review;
- human approval;
- fairness checks;
- disclosure;
- explanation or recourse;
- monitoring; or
- escalation authority.

Recommend approve, constrain, redesign, or reject the fix.
```

## 17. Diagnostic decision record

```text
Produce a diagnostic decision record with:
- observed failure;
- expected behavior;
- symptom timing;
- primary and alternate hypotheses;
- evidence;
- minimal test;
- result;
- selected repair;
- regression checks;
- governance checks;
- rollback condition; and
- final disposition.
```

## 18. Oral certification drill

```text
Give me one Module 7 scenario at a time.

Require me to:
1. identify the symptom timing;
2. classify the likely root cause;
3. state the cheapest next test;
4. reject an attractive distractor;
5. define the bounded fix; and
6. explain how I would verify it.

After my answer, grade the reasoning and provide a stronger model answer.
```

## Public-repository rule

Use fictional, synthetic, public, or explicitly authorized scenarios. Do not paste confidential prompts, private source material, credentials, production logs, internal configuration, client information, remembered live-exam questions, or reconstructed proprietary course questions.
