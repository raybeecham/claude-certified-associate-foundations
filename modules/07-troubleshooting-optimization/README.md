# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** In progress — teaching, quiz, and Key Takeaways are complete. Module Complete remains open.

## Module thesis

> Troubleshooting and optimization form one controlled loop: diagnose the responsible layer, isolate it with a bounded test, translate feedback into a specific adjustment, promote recurring fixes into the correct maintained layer, and measure whether the workflow improves without weakening governance.

```text
Observed underperformance
      ↓
Diagnosis and isolation
      ↓
Feedback translated into adjustment
      ↓
Durable placement
      ↓
Guarded pilot
      ↓
Measured adoption, revision, or rollback
```

## Course-aligned roadmap

- [x] [01. Diagnosing Underperforming Prompts & Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [x] [02. Adjusting Approach from Feedback](lessons/02-adjusting-approach-from-feedback.md)
- [x] [03. Optimizing Workflows](lessons/03-optimizing-workflows.md)
- [x] 04. Module 7 Quiz
  - [x] [Module 7 Quiz — Full marks, 5/5](lessons/04a-module-7-quiz.md)
  - [x] [Key Takeaways](lessons/04b-key-takeaways.md)
- [ ] 05. Module Complete

## Completion record

```text
Module 7 teaching sections: Complete
Module 7 quiz:              Full marks — 5 of 5
Key Takeaways:              Complete
Module Complete:            Open
```

---

# Four durable takeaways

## 1. Underperformance has discoverable causes

Use the cheapest-fix-first sequence:

```text
1. Specification
2. Context
3. Feature or model
4. Configuration
5. Task fit or expectation
```

| Symptom | Likely cause | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract details |
| Started correctly, then degraded | Context overload or drift | Restart from a verified summary |
| Specific repeatable error | Wrong feature or model | Test the capability suited to the defect |
| Used to work, now performs poorly | Stale configuration | Review instructions, sources, Skills, connectors, and dependencies |
| Outcome remains unavailable | Expectation mismatch | Reshape the task |

```text
Weak output
      ≠
Tool incapable
```

## 2. Isolate before you fix

Name the failure layer before changing the system.

Possible layers include:

- prompt specification;
- conversation context;
- feature or model choice;
- maintained configuration;
- tool schema or parameters;
- workflow sequencing;
- evaluation criteria; and
- task fit.

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

Changing several variables at once destroys causal evidence.

## 3. Every disappointing output is data

```text
Reaction
      ≠
Instruction
```

| Reaction | Specific adjustment |
|---|---|
| Too generic | State the audience and desired action |
| Wrong tone | Define observable tone constraints |
| Missed the point | Put the required question first |
| Same field omitted every cycle | Add it to the maintained procedure |
| Test records repeatedly included | Add deterministic exclusion and verification |

Place validated recurring fixes correctly:

| Need | Correct home |
|---|---|
| One-time detail | Current prompt |
| Recurring rule | Project or standing instruction |
| Shared reference | Project knowledge or governed source |
| Repeatable procedure | Skill or workflow |
| Exact calculation, filter, or gate | Code, query, schema, or technical control |
| Required approval | Human workflow gate |

Current Claude documentation describes Projects as workspaces with knowledge and instructions used across chats in a Project, while Skills package repeatable task-specific instructions, scripts, and resources. Product behavior can change; current official documentation controls implementation decisions.

## 4. Optimize deliberately

Observe one complete workflow cycle and record:

- repetition;
- recurring correction;
- operator variance;
- duplicate research or calculation;
- manual formatting;
- waiting and handoffs;
- rework; and
- required controls that must remain.

```text
Rule          → instruction
Reference     → knowledge
Procedure     → Skill or workflow
Exact logic   → deterministic control
One-time fact → current prompt
```

Select the metric before changing the workflow. Possible primary metrics include time per cycle, revision rounds, consistency, verified accuracy, defect rate, latency, cost, approval time, and user effort.

Use quality, privacy, fairness, accountability, maintainability, and reliability as guardrails.

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

```text
Fastest workflow
      ≠
Best workflow
```

Stop when the target is met, marginal gains become small, maintenance exceeds the benefit, or further tuning becomes new friction.

---

# Module 7 quiz result

```text
Full marks — 5 of 5
```

The original public-safe quiz demonstrated command of:

1. first-response under-specification;
2. model or feature mismatch;
3. cheapest-fix-first diagnosis;
4. durable promotion of recurring corrections; and
5. optimization against the measured bottleneck.

---

# Integrated Module 7 protocol

```text
1. Define expected and observed behavior
2. Read symptom timing and classify likely causes
3. Run the cheapest discriminating test
4. Isolate one cause with one bounded change
5. Translate feedback into an observable instruction or control
6. Validate the failing and representative cases
7. Promote recurring fixes to the correct maintained layer
8. Instrument one full recurring workflow cycle
9. Identify repetition, correction, variance, handoffs, and rework
10. Apply the rule-reference-procedure test
11. Select target and guardrail metrics
12. Pilot with the baseline and rollback available
13. Measure net improvement
14. Adopt, revise, revert, or stop optimizing
```

---

# Current module resources

## Lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)
- [Optimizing Workflows for Efficiency and Effectiveness](lessons/03-optimizing-workflows.md)
- [Module 7 Quiz](lessons/04a-module-7-quiz.md)
- [Module 7 Key Takeaways](lessons/04b-key-takeaways.md)

## Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)
- [Optimizing Workflows prompts](../../prompts/module-07/03-optimizing-workflows-prompts.md)
- [Module 7 quiz and remediation prompts](../../prompts/module-07/04a-module-7-quiz-prompts.md)
- [Module 7 Key Takeaways prompts](../../prompts/module-07/04b-key-takeaways-prompts.md)

## Engineering patterns

- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Feedback-to-Configuration Promotion Pattern](../../patterns/feedback-to-configuration-promotion-pattern.md)
- [Workflow Efficiency Audit and Promotion Pattern](../../patterns/workflow-efficiency-audit-and-promotion-pattern.md)

## Extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

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

# Completion criteria

- [x] I completed all Module 7 teaching sections.
- [x] I completed the Module 7 quiz with full marks, 5/5.
- [x] I completed the Module 7 Key Takeaways.
- [ ] I can classify underperformance across specification, context, capability, configuration, and task fit.
- [ ] I can isolate a cause through one hypothesis and one bounded test.
- [ ] I can translate vague critique into an observable adjustment.
- [ ] I can place recurring rules, references, procedures, and exact logic correctly.
- [ ] I can instrument a workflow and identify repetition, correction, and variance.
- [ ] I can choose target and guardrail metrics.
- [ ] I can design a guarded pilot with a baseline and rollback.
- [ ] I can define a stop condition for diminishing returns.
- [ ] I can preserve governance while troubleshooting and optimizing.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

---

## Product-verification note

The product-specific references were checked against official Anthropic documentation available on August 3, 2026. Current guidance describes Projects as workspaces with knowledge and instructions used across Project chats, Skills as repeatable task-specific packages, and code execution as a distinct capability. Product behavior and availability can change; current official documentation and authorized organizational guidance control real implementations.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential prompts, outputs, workflow measurements, production incidents, credentials, proprietary configuration, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.
