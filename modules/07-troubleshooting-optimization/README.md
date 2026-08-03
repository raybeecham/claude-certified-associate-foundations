# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** Complete — teaching, quiz, Key Takeaways, and Module Complete are finished.

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
- [x] [05. Module Complete](lessons/05-module-complete.md)

## Completion record

```text
Associate-path checkpoint: 1 of 1 passed
Module 7 teaching sections: Complete
Module 7 quiz:              Full marks — 5 of 5
Key Takeaways:              Complete
Module 7:                   Complete
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

Place validated recurring fixes correctly:

| Need | Correct home |
|---|---|
| One-time detail | Current prompt |
| Recurring rule | Project or standing instruction |
| Shared reference | Governed knowledge or source |
| Repeatable procedure | Skill or workflow |
| Exact calculation, filter, or gate | Code, query, schema, or technical control |
| Required approval | Human workflow gate |

## 4. Optimize deliberately

Observe one complete workflow cycle and record repetition, correction, variance, waiting, handoffs, rework, and required controls.

```text
Rule          → instruction
Reference     → knowledge
Procedure     → Skill or workflow
Exact logic   → deterministic control
One-time fact → current prompt
```

Select the target metric before changing the workflow, retain the baseline, pilot representative cases, preserve guardrails, and adopt only when the measured gain survives validation.

```text
Fastest workflow
      ≠
Best workflow
```

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
14. Adopt, revise, revert, reshape, or stop optimizing
```

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

# Current module resources

## Lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)
- [Optimizing Workflows for Efficiency and Effectiveness](lessons/03-optimizing-workflows.md)
- [Module 7 Quiz](lessons/04a-module-7-quiz.md)
- [Module 7 Key Takeaways](lessons/04b-key-takeaways.md)
- [Module 7 Complete](lessons/05-module-complete.md)

## Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)
- [Optimizing Workflows prompts](../../prompts/module-07/03-optimizing-workflows-prompts.md)
- [Module 7 quiz and remediation prompts](../../prompts/module-07/04a-module-7-quiz-prompts.md)
- [Module 7 Key Takeaways prompts](../../prompts/module-07/04b-key-takeaways-prompts.md)
- [Module 7 completion and transition prompts](../../prompts/module-07/05-module-complete-prompts.md)

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

# Transition to Module 8

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

Module 8 will recap the seven domains, prepare for the certification exam, and clarify escalation boundaries to Developer- and Architect-level work.

---

# Completion criteria

- [x] I completed all Module 7 teaching sections.
- [x] I completed the Module 7 quiz with full marks, 5/5.
- [x] I completed the Module 7 Key Takeaways.
- [x] I completed Module 7 and passed its checkpoint.
- [x] I can classify underperformance across specification, context, capability, configuration, and task fit.
- [x] I can isolate a cause through one hypothesis and one bounded test.
- [x] I can translate vague critique into an observable adjustment.
- [x] I can place recurring rules, references, procedures, and exact logic correctly.
- [x] I can instrument a workflow and identify repetition, correction, and variance.
- [x] I can choose target and guardrail metrics.
- [x] I can design a guarded pilot with a baseline and rollback.
- [x] I can preserve governance while troubleshooting and optimizing.

## Product-verification note

Product behavior changes. Current official Anthropic documentation and authorized organizational guidance control implementation-specific decisions.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential prompts, outputs, workflow measurements, production incidents, credentials, proprietary configuration, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.
