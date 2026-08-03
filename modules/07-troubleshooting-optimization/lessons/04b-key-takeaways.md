# Module 7 Key Takeaways

## Overview

Troubleshooting and optimization are not random prompt edits. They are controlled loops that identify a cause, test a bounded repair, capture what works, and measure whether the workflow actually improved.

```text
Observe
  ↓
Diagnose
  ↓
Isolate
  ↓
Adjust
  ↓
Validate
  ↓
Promote and measure
```

This lesson consolidates four durable ideas from Module 7.

---

# 1. Underperformance has discoverable causes

A disappointing output is evidence that something in the system needs inspection. It is not proof that Claude cannot perform the task.

Use the cheapest-fix-first sequence:

```text
1. Specification
2. Context
3. Feature or model
4. Configuration
5. Task fit or expectation
```

Typical symptom patterns include:

| Symptom | Likely cause | First test |
|---|---|---|
| Wrong from the first response | Under-specification | Add the missing objective, context, constraints, format, or success criteria |
| Started correctly, then degraded | Context overload or drift | Restart from a verified summary and remove irrelevant history |
| Specific repeatable error | Wrong feature or model | Test the capability directly suited to the defect |
| Used to work, now performs poorly | Stale configuration | Review instructions, knowledge, Skills, connectors, schemas, and dependencies |
| Requested result remains unavailable | Expectation mismatch | Reshape the task into a bounded, supportable outcome |

```text
Weak output
      ≠
Tool incapable
```

The professional habit is to diagnose before forming a conclusion about capability.

---

# 2. Isolate before you fix

Naming the failure layer points toward the repair.

Possible layers include:

- prompt specification;
- conversation context;
- feature or model choice;
- maintained configuration;
- tool schema or parameters;
- workflow sequencing;
- evaluation criteria; and
- task fit.

Use controlled diagnosis:

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

Changing the prompt, model, tools, context, and workflow simultaneously destroys the evidence needed to know what worked.

A useful diagnostic record includes:

- expected behavior;
- observed behavior;
- symptom timing;
- primary and alternate hypotheses;
- evidence;
- minimal test;
- result;
- selected repair;
- representative regression checks;
- governance checks; and
- rollback condition.

```text
Symptom named
      ≠
Cause isolated
```

Isolation requires a test that distinguishes the proposed cause from plausible alternatives.

---

# 3. Every disappointing output is data

Feedback becomes useful only when it is translated into a specific adjustment.

```text
Reaction
      ≠
Instruction
```

Examples:

| Reaction | Specific instruction or control |
|---|---|
| Too generic | State the audience and desired action |
| Wrong tone | Define observable tone constraints |
| Missed the point | Put the required question first |
| Same field omitted every cycle | Add the field to the maintained procedure |
| Test records repeatedly included | Add deterministic exclusion and verification |

Then identify the controlling lever:

| Need | Correct home |
|---|---|
| One-time detail | Current prompt |
| Recurring rule | Project or standing instruction |
| Shared reference material | Project knowledge or governed source |
| Repeatable multi-step method | Skill or workflow |
| Exact calculation, filter, or gate | Code, query, schema, or technical control |
| Missing approval | Human workflow gate |

Current Claude guidance describes Projects as workspaces with knowledge and instructions used across chats in that Project. Skills package specialized instructions, scripts, and resources for repeatable tasks. These product details can change, so current official documentation controls implementation decisions.

A correction should be promoted when the same need will recur for the same person, another person, or another cycle.

```text
Correction discovered once
+ recurring need
+ validated behavior
=
candidate for durable configuration
```

A fix should not be promoted until its scope, owner, tests, approval, rollback, and review trigger are known.

---

# 4. Optimize deliberately

Optimization begins by observing one complete workflow cycle and writing down every repeated manual step.

Look for three signals:

| Signal | Meaning |
|---|---|
| Repetition | The same context or instruction is entered every run |
| Correction | The same output defect is repaired every cycle |
| Variance | Different users produce different results from the same task |

Then classify each fix:

```text
Rule          → instruction
Reference     → knowledge
Procedure     → Skill or workflow
Exact logic   → deterministic control
One-time fact → current prompt
```

Select the metric before changing the workflow. Possible primary metrics include:

- time per cycle;
- revision rounds;
- consistency across users;
- verified accuracy;
- defect rate;
- latency;
- cost;
- approval time; and
- user effort.

Use quality, privacy, fairness, accountability, maintainability, and reliability as guardrail metrics.

```text
Fastest workflow
      ≠
Best workflow
```

Use a guarded rollout:

```text
Baseline retained
      ↓
Optimized version piloted
      ↓
Representative cycles compared
      ↓
Quality and governance checked
      ↓
Adopt / revise / revert
```

Stop optimizing when the target metric is met, marginal gains become small, maintenance exceeds the benefit, or additional tuning creates new friction or risk.

---

# Integrated Module 7 decision sequence

```text
1. Define expected and observed behavior
2. Read symptom timing and classify likely causes
3. Run the cheapest relevant diagnostic test
4. Isolate one cause with one bounded change
5. Translate feedback into an observable instruction or control
6. Validate the original and representative cases
7. Promote recurring fixes to the correct maintained layer
8. Instrument the full recurring workflow
9. Select target and guardrail metrics
10. Pilot with the baseline and rollback available
11. Measure net improvement
12. Adopt, revise, revert, or stop optimizing
```

---

# Exam lens

```text
First response wrong                    → inspect specification
Long session degraded                  → inspect context
Specific repeatable error              → inspect feature or model fit
Used to work                           → inspect configuration
Exact unsupported outcome              → reshape the task
Vague critique                         → translate reaction into instruction
Same correction every cycle            → validate and promote
Different operators, different results → standardize procedure and evidence
No baseline                            → improvement cannot be demonstrated
Speed improves but quality falls       → optimization failed
```

---

# Quick recap

1. **Underperformance has discoverable causes.** Run the diagnostic sequence before blaming the tool.
2. **Isolate before you fix.** The failure layer determines the repair.
3. **Every disappointing output is data.** Translate critique into a specific adjustment and capture recurring fixes.
4. **Optimize deliberately.** Instrument the workflow, target the measured friction, pilot safely, and verify the gain.

---

## Product-verification note

The product-specific references in this lesson were checked against official Anthropic documentation available on August 3, 2026. Current guidance describes Projects as shared-context workspaces with project knowledge and instructions, Skills as repeatable task-specific packages, and code execution as a distinct capability. Product behavior and availability can change; current official documentation and authorized organizational guidance control real implementations.

## Public-repository rule

Examples must remain fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential prompts, outputs, workflow measurements, production incidents, credentials, proprietary configuration, remembered live-exam questions, or reconstructed proprietary course content.
