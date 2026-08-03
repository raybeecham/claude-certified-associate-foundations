# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** In progress — all teaching sections and the Module 7 quiz are complete. Key Takeaways and Module Complete remain open.

## Module thesis

> Troubleshooting and optimization form one controlled loop: diagnose the responsible layer, translate feedback into a specific adjustment, instrument the recurring workflow, promote validated fixes into the correct maintained layer, and measure whether the result improves without weakening governance.

```text
Observed underperformance
      ↓
Diagnosis and feedback
      ↓
Workflow instrumentation
      ↓
Rule / reference / procedure placement
      ↓
Guarded pilot
      ↓
Measured adoption, revision, or rollback
```

## Course-aligned roadmap

- [x] [01. Diagnosing Underperforming Prompts & Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [x] [02. Adjusting Approach from Feedback](lessons/02-adjusting-approach-from-feedback.md)
- [x] [03. Optimizing Workflows](lessons/03-optimizing-workflows.md)
- [ ] 04. Module 7 Quiz
  - [x] [Module 7 Quiz — Full marks, 5/5](lessons/04a-module-7-quiz.md)
  - [ ] Key Takeaways
- [ ] 05. Module Complete

## Completion record

```text
Module 7 teaching sections: Complete
Module 7 quiz:              Full marks — 5 of 5
Key Takeaways:              Open
Module Complete:            Open
```

## 1. Diagnose the failure

| Symptom | Likely cause | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract details |
| Started well, then degraded | Context overload | Restart from a verified summary |
| Specific repeatable error | Wrong feature or model | Select the correct capability |
| Used to work, now performs poorly | Stale configuration | Review maintained dependencies |
| Still unavailable after cheaper tests | Expectation mismatch | Reshape the task |

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

## 2. Translate feedback into a persistent repair

```text
Output critique
      ↓
Observable defect
      ↓
Missing condition
      ↓
Controlling lever
      ↓
Bounded adjustment
      ↓
Representative validation
      ↓
Local fix or durable promotion
```

```text
Reaction
      ≠
Instruction
```

| Reaction | Specific adjustment | Lever |
|---|---|---|
| Too generic | State the audience and desired action | Prompt context or instruction |
| Wrong tone | Define observable tone constraints | Standing instruction |
| Missed the point | Put the required question first | Prompt objective |
| Same field missing repeatedly | Add it to the maintained procedure | Skill or workflow |
| Test records included | Add exact exclusion and verification | Code, query, or control |

## 3. Instrument and optimize the recurring workflow

Observe one full cycle and record:

- repeated context entry;
- recurring corrections;
- manual formatting;
- duplicate research or calculation;
- handoffs and waiting;
- verification;
- operator-to-operator variance; and
- rework.

### Three friction signals

| Signal | Meaning | Typical repair |
|---|---|---|
| Repetition | Same content or instruction every run | Shared context or standing rule |
| Correction | Same output defect repaired every cycle | Configuration or deterministic control |
| Variance | Different operators get different results | Shared procedure, knowledge, and validation |

Required human review, privacy checks, approvals, and segregation of duties remain controls rather than removable friction.

## Rule–reference–procedure placement

| Type | Correct home |
|---|---|
| Rule | Project or standing instruction |
| Reference | Governed knowledge or source |
| Procedure | Skill or workflow |
| Deterministic logic | Code, query, schema, or technical control |
| One-time detail | Current prompt |

```text
Rule      → instruction
Reference → knowledge
Procedure → Skill or workflow
Exact logic → deterministic control
```

## Measure and pilot

Select the target metric before changing the workflow. Possible metrics include time per cycle, revision rounds, consistency, verified accuracy, defect rate, latency, cost, approval time, and user effort.

Use quality, safety, privacy, fairness, accountability, and maintenance burden as guardrails.

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

A single improved run is not proof.

## Module 7 quiz result

```text
Full marks — 5 of 5
```

The original public-safe quiz demonstrated command of:

1. recognizing first-response under-specification;
2. diagnosing a model or feature mismatch;
3. applying the cheapest-fix-first diagnostic sequence;
4. promoting recurring corrections into durable configuration; and
5. targeting the measured workflow bottleneck.

### Quiz shortcut

```text
Wrong on first response
→ inspect specification

Persistently shallow on a speed-oriented route
→ test model fit

Cause unknown
→ run the diagnostic sequence

Same correction every cycle
→ validate and promote

Measured bottleneck is variance
→ standardize the procedure
```

## Integrated Module 7 protocol

```text
1. Define expected and observed behavior
2. Diagnose specification, context, capability, configuration, or task fit
3. Translate feedback into an observable defect and missing condition
4. Identify the controlling lever
5. Observe one complete recurring workflow cycle
6. Record repetition, correction, variance, handoffs, and rework
7. Classify fixes as rules, references, procedures, or deterministic controls
8. Build the smallest shared change
9. Select primary and guardrail metrics
10. Pilot with the baseline retained
11. Test representative and edge cases
12. Measure quality, consistency, time, cost, and governance impact
13. Adopt, revise, revert, or stop optimizing
14. Assign ownership, versioning, rollback, monitoring, and review cadence
```

## Current module resources

### Lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)
- [Optimizing Workflows for Efficiency and Effectiveness](lessons/03-optimizing-workflows.md)
- [Module 7 Quiz](lessons/04a-module-7-quiz.md)

### Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)
- [Optimizing Workflows prompts](../../prompts/module-07/03-optimizing-workflows-prompts.md)
- [Module 7 quiz and remediation prompts](../../prompts/module-07/04a-module-7-quiz-prompts.md)

### Engineering patterns

- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Feedback-to-Configuration Promotion Pattern](../../patterns/feedback-to-configuration-promotion-pattern.md)
- [Workflow Efficiency Audit and Promotion Pattern](../../patterns/workflow-efficiency-audit-and-promotion-pattern.md)

### Extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

```text
Weak output                              → diagnose before rewriting
Wrong on first response                  → inspect specification
Specific shallow output                  → inspect model or feature fit
Cause not yet known                      → run the diagnostic sequence
Same correction every cycle             → validate and promote
Different users, different formats       → standardize procedure and validation
Optimization has no baseline             → cannot prove improvement
Review gate called friction              → preserve required governance
Speed improves but accuracy falls        → optimization failed
```

## Completion criteria

- [x] I completed all Module 7 teaching sections.
- [x] I completed the Module 7 quiz with full marks, 5/5.
- [ ] I completed the Module 7 Key Takeaways.
- [ ] I can classify the common underperformance causes.
- [ ] I can convert vague feedback into an observable defect and testable instruction.
- [ ] I can identify repetition, correction, variance, and required controls.
- [ ] I can apply the rule–reference–procedure placement test.
- [ ] I can choose the metric that reflects the workflow's purpose.
- [ ] I can design a guarded pilot with a baseline and rollback.
- [ ] I can measure net improvement rather than local speed alone.
- [ ] I can preserve governance while troubleshooting and optimizing.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private prompts or outputs, confidential workflow timings, proprietary procedures, production logs, credentials, internal configuration, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.

## Source note

The Module 7 quiz material was supplied on August 3, 2026. The repository records the learner's reported result of full marks, 5/5, while using original public-safe scenarios rather than reproducing proprietary quiz wording.