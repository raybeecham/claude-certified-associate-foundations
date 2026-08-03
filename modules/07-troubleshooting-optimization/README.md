# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** In progress — all Module 7 teaching sections are complete. Quiz, Key Takeaways, and Module Complete remain open.

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
  - [ ] Module 7 Quiz
  - [ ] Key Takeaways
- [ ] 05. Module Complete

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

A reaction describes how the output feels. An instruction defines what must change.

| Reaction | Specific adjustment | Lever |
|---|---|---|
| Too generic | State the audience and desired action | Prompt context or instruction |
| Wrong tone | Define observable tone constraints | Standing instruction |
| Missed the point | Put the required question first | Prompt objective |
| Same field missing repeatedly | Add it to the maintained procedure | Skill or workflow |
| Test records included | Add exact exclusion and verification | Code, query, or control |

```text
Correct correction
+ wrong layer
=
fragile repair
```

## 3. Instrument and optimize the recurring workflow

Run one complete cycle while recording every manual step:

- repeated context entry;
- recurring corrections;
- manual formatting;
- duplicate research or calculation;
- handoffs and waiting;
- verification;
- user-to-user variation; and
- rework.

This creates the optimization backlog.

### Three friction signals

| Signal | Meaning | Typical repair |
|---|---|---|
| Repetition | Same content or instruction every run | Shared context or standing rule |
| Correction | Same output defect repaired every cycle | Configuration or deterministic control |
| Variance | Different operators get different results | Shared procedure, knowledge, and validation |

```text
Repeated manual effort
      ≠
Unavoidable work
```

Required human review, privacy checks, approvals, and segregation of duties are controls—not removable friction.

## Rule–reference–procedure placement test

| Type | Question | Correct home |
|---|---|---|
| Rule | What must always be true? | Project or standing instruction |
| Reference | What source material does every run need? | Governed knowledge or source |
| Procedure | What ordered method must be followed? | Skill or workflow |
| Deterministic logic | What exact calculation, filter, or gate must execute? | Code, query, schema, or technical control |
| One-time detail | What applies only to this run? | Current prompt |

```text
Rule      → instruction
Reference → knowledge
Procedure → Skill or workflow
Exact rule → deterministic control
```

## Consolidate carefully

Combine steps only when the change preserves:

- permission boundaries;
- independent approval;
- data scope;
- failure visibility;
- testability; and
- rollback.

```text
Fewer steps
      ≠
Better workflow automatically
```

## Measure the improvement

Select the metric before changing the workflow.

Possible primary metrics:

- time per cycle;
- revision rounds;
- consistency across users;
- verified accuracy;
- defect rate;
- latency;
- cost;
- approval time; and
- user effort.

Use guardrails for quality, safety, privacy, fairness, accountability, and maintenance burden.

```text
Fastest workflow
      ≠
Best workflow
```

## Guarded rollout

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

A single successful run is not proof. Keep the old approach available until the optimized version survives representative and edge-case testing.

## Diminishing returns

Stop when:

- the target metric is met;
- further gains are marginal;
- complexity or maintenance exceeds benefit;
- risk increases; or
- additional tuning becomes its own recurring friction.

## Worked workflow audit

A fictional weekly reporting process takes about 45 minutes per analyst.

| Friction | Classification | Placement |
|---|---|---|
| Background repasted each run | Reference | Shared Project knowledge |
| Report format rebuilt manually | Procedure | Shared Skill |
| Verification varies by analyst | Rule and control | Standing instruction plus release check |

After a guarded pilot, the cycle falls to about 25 minutes, one revision round is removed, and format and verification become consistent.

The gain is adopted only after source authority, data boundaries, review gates, and rollback are confirmed.

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
12. Measure net time, quality, consistency, cost, and governance impact
13. Adopt, revise, revert, or stop optimizing
14. Assign ownership, versioning, rollback, monitoring, and review cadence
```

## Current module resources

### Lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)
- [Optimizing Workflows for Efficiency and Effectiveness](lessons/03-optimizing-workflows.md)

### Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)
- [Optimizing Workflows prompts](../../prompts/module-07/03-optimizing-workflows-prompts.md)

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
Vague critique                           → convert reaction into instruction
Same correction every cycle             → validate and promote
Repeated context                         → governed reference or Project knowledge
Recurring rule                           → standing instruction
Multi-step repeatable method             → Skill or workflow
Exact calculation or exclusion           → deterministic control
Different users, different results       → standardize procedure and validation
Optimization has no baseline             → cannot prove improvement
One improved run                         → pilot representative cycles
Review gate called friction              → preserve required governance
Speed improves but accuracy falls        → optimization failed
Target metric reached                    → stop tuning and monitor
```

## Completion criteria

- [x] I completed Diagnosing Underperforming Prompts & Outputs.
- [x] I completed Adjusting Approach from Feedback.
- [x] I completed Optimizing Workflows.
- [ ] I can classify the common underperformance causes.
- [ ] I can convert vague feedback into an observable defect and testable instruction.
- [ ] I can identify repetition, correction, variance, and required controls.
- [ ] I can apply the rule–reference–procedure placement test.
- [ ] I can choose the metric that reflects the workflow's purpose.
- [ ] I can design a guarded pilot with a baseline and rollback.
- [ ] I can measure net improvement rather than local speed alone.
- [ ] I can define a stop condition for diminishing returns.
- [ ] I can preserve governance while troubleshooting and optimizing.
- [ ] I completed the Module 7 quiz and Key Takeaways.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private prompts or outputs, confidential workflow timings, proprietary procedures, production logs, credentials, internal configuration, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.