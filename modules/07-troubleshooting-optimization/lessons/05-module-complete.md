# Module 7 Complete: Troubleshooting & Optimization

## Completion status

```text
Associate-path checkpoint: 1 of 1 passed
Module 7 teaching sections: Complete
Module 7 quiz:              Full marks — 5 of 5
Key Takeaways:              Complete
Module 7:                   Complete
```

You can now diagnose underperformance and optimize Claude-assisted workflows when results fall short.

> Troubleshoot systematically, and each iteration becomes evidence for a better prompt, configuration, or workflow.

---

# What you can now do

You can:

- recognize under-specification, context overload, capability mismatch, stale configuration, and expectation mismatch;
- read symptom timing without treating it as proof;
- isolate one likely cause before changing the system;
- build a minimal reproducible case;
- test one hypothesis with one bounded change;
- translate vague reactions into observable defects and actionable instructions;
- decide whether a correction belongs in a prompt, instruction, knowledge source, Skill, deterministic control, or human gate;
- instrument recurring workflows for repetition, correction, variance, waiting, handoffs, and rework;
- select a target metric and guardrail metrics before optimizing;
- run guarded pilots with a retained baseline and rollback path;
- measure net improvement rather than local speed alone; and
- preserve governance, human review, privacy, fairness, and accountability during optimization.

---

# The complete Module 7 loop

```text
Observed underperformance
      ↓
Define expected versus observed behavior
      ↓
Diagnose specification, context, capability,
configuration, or task fit
      ↓
Isolate one testable hypothesis
      ↓
Make one bounded change
      ↓
Translate recurring feedback into a durable fix
      ↓
Place rules, references, procedures,
and exact logic correctly
      ↓
Pilot against the baseline
      ↓
Measure quality, consistency, time, cost,
and governance impact
      ↓
Adopt / revise / revert / reshape
```

---

# Four durable principles

## 1. Underperformance has discoverable causes

```text
Specification
Context
Feature or model
Configuration
Task fit or expectation
```

Do not begin with a model upgrade or a complete rewrite. Begin with the cheapest controlled test.

## 2. Isolate before you fix

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
```

Changing several variables at once destroys causal evidence.

## 3. Every disappointing output is data

```text
Reaction
      ≠
Instruction
```

A recurring correction should be translated into a specific condition, validated, and promoted to the correct maintained layer.

## 4. Optimize deliberately

```text
Instrument
      ↓
Find friction
      ↓
Place the fix
      ↓
Pilot
      ↓
Measure
```

A workflow is improved only when the target metric improves without unacceptable degradation in quality, reliability, governance, or maintainability.

---

# Associate-path progress

| Module | Capability | Status |
|---|---|---|
| M1 — Product & Model Selection | Choose the right entry point, model, and features | Complete |
| M2 — Prompting | Build structured prompts and adapt them to the task | Complete |
| M3 — Output Evaluation | Validate output and place non-negotiable human review | Complete |
| M4 — Workflow Integration | Map and redesign workflows safely | Complete |
| M5 — Configuration | Configure and maintain Projects, instructions, and knowledge | Complete |
| M6 — Governance | Apply use-case, data, policy, and ethics judgment | Complete |
| **M7 — Troubleshooting** | **Diagnose underperformance and optimize workflows** | **Complete** |
| **M8 — Course Summary & Next Steps** | **Recap the journey, prepare for the exam, and recognize escalation boundaries** | **Up next** |

---

# Transition to Module 8

Module 7 focused on repairing and improving individual workflows.

Module 8 will synthesize the full Associate path:

```text
Select the right capability
      ↓
Specify the task
      ↓
Evaluate the output
      ↓
Integrate the workflow
      ↓
Maintain the configuration
      ↓
Govern the use
      ↓
Troubleshoot and optimize
      ↓
Prepare for the exam and identify
when Associate-level judgment is not enough
```

The transition question is:

> Can you combine the seven domains into one coherent decision process, explain the boundaries of Associate-level work, and prepare to apply that reasoning under exam conditions?

---

# Final Module 7 self-check

You should be able to explain:

1. why a weak first response usually suggests under-specification;
2. why degradation over time points toward context problems;
3. why repeatable error types may require a different feature or model;
4. why “used to work” triggers configuration maintenance;
5. why expectation mismatch is tested last;
6. why feedback must become a specific instruction;
7. when a fix stays local and when it is promoted;
8. the rule–reference–procedure placement test;
9. why a baseline and guardrails are required; and
10. when to adopt, revise, revert, reshape, or stop optimizing.

---

# Public-repository scenario policy

Examples must remain fictional, generic, synthetic, public, or explicitly authorized. Do not publish private prompts or outputs, production logs, confidential workflow timings, credentials, proprietary procedures, client information, or reconstructed proprietary course questions.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.
