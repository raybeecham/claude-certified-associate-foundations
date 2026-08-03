# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** Roadmap staged — Module 6 is complete. No Module 7 section is marked complete yet.

## Module thesis

> Troubleshooting is disciplined diagnosis: observe the failure, localize the responsible stage, change the smallest relevant variable, and verify that the repair improves the target behavior without weakening governance or causing regressions.

```text
Observed underperformance
      ↓
Evidence and reproduction
      ↓
Failure classification and localization
      ↓
Targeted adjustment
      ↓
Representative validation
      ↓
Workflow optimization and monitoring
```

---

# Course-aligned roadmap

- [ ] 01. Diagnosing Underperforming Prompts & Outputs
- [ ] 02. Adjusting Approach from Feedback
- [ ] 03. Optimizing Workflows
- [ ] 04. Module 7 Quiz
  - [ ] Module 7 Quiz
  - [ ] Key Takeaways
- [ ] 05. Module Complete

No section is marked complete until its corresponding preparation-course material is supplied and converted into original public-safe study content.

---

# Module 6 to Module 7 bridge

Module 6 established whether a use case should proceed and under what data, feature, policy, ethical, and accountability boundaries.

Module 7 begins after an approved workflow underperforms.

```text
Governed workflow
      ↓
Unexpected or weak result
      ↓
Diagnose the responsible layer
      ↓
Apply the narrowest responsible repair
      ↓
Verify quality, safety, and operational impact
```

The transition question is:

> The workflow is approved and governed—but why is it underperforming, where is the failure located, and what is the smallest repair that survives validation?

Governance remains active during troubleshooting. Performance improvements must not weaken data controls, permissions, human-review gates, fairness, disclosure, recourse, or accountability.

---

# Durable troubleshooting foundation

The repository already contains extended troubleshooting material. It will be mapped to the supplied course sections as they arrive.

## 1. Diagnose before editing

Uncontrolled prompt tweaking produces fragile systems.

Start with:

- the expected behavior;
- the observed behavior;
- a reproducible example;
- the relevant inputs and configuration;
- a known-good baseline where available;
- the stage at which the failure first appears; and
- evidence that distinguishes competing explanations.

```text
Output is weak
      ≠
Prompt is automatically the cause
```

Potential failure layers include:

- task definition;
- source quality or context;
- prompt structure;
- model fit;
- tool selection;
- tool parameters or schema;
- connector access;
- code execution;
- truncation or stop behavior;
- workflow sequencing;
- human-review design;
- evaluation criteria;
- latency or reliability constraints; and
- stale configuration.

## 2. Reproduce and establish a baseline

A useful diagnostic case should be small enough to inspect but representative enough to preserve the failure.

```text
Large failing workflow
      ↓
Minimal reproducible case
      ↓
Known-good or expected baseline
      ↓
Controlled comparison
```

Without a baseline, changes may feel better while remaining unmeasured.

## 3. Form one hypothesis

State one explanation that can be tested.

Examples:

- the prompt omits a required constraint;
- the source context is incomplete;
- a tool schema encourages the wrong argument;
- the model is selecting an inappropriate tool;
- the output is truncated;
- a review step is placed too late;
- the workflow repeats expensive work;
- an optimization reduced accuracy; or
- feedback reveals a requirement that was never captured.

## 4. Change one variable at a time

```text
One hypothesis
      ↓
One bounded change
      ↓
One comparison
      ↓
Keep / revise / revert
```

Changing prompt, model, tools, context, and workflow together prevents attribution.

## 5. Validate beyond the example

A fix should be tested against:

- the original failing case;
- representative normal cases;
- edge cases;
- adversarial or boundary cases where appropriate;
- quality and completeness criteria;
- latency and cost constraints;
- governance controls; and
- regression risks.

```text
One example improved
      ≠
Workflow repaired
```

## 6. Optimize the workflow, not only the prompt

Optimization may involve:

- clearer task decomposition;
- better source selection;
- improved tool descriptions or schemas;
- fewer unnecessary calls;
- parallelizing independent work;
- caching stable context;
- moving deterministic operations to code;
- adding checkpoints;
- narrowing model use to stages that need it;
- improving error handling;
- adding fallback paths;
- changing review placement; or
- retiring steps that add cost without value.

A model change is only one possible intervention.

---

# Troubleshooting protocol

```text
1. Define expected and observed behavior
2. Capture inputs, configuration, tools, and environment
3. Reproduce the failure with a minimal representative case
4. Compare against a baseline or explicit success criteria
5. Classify the likely failure layer
6. Form one testable hypothesis
7. Change one relevant variable
8. Re-run the failing and control cases
9. Measure quality, completeness, latency, cost, and safety
10. Keep, revise, or revert the change
11. Run representative regression tests
12. Document the result, rollback path, and monitoring trigger
```

---

# Learning objectives

By the end of this module, you should be able to:

- diagnose underperforming prompts and outputs without immediately rewriting everything;
- distinguish prompt defects from context, model, tool, workflow, configuration, and evaluation defects;
- collect the minimum evidence needed for diagnosis;
- reproduce a problem with a minimal representative case;
- compare behavior with an explicit baseline;
- interpret feedback as evidence about requirements, process, or quality;
- form and test bounded hypotheses;
- change one variable at a time;
- validate repairs against representative and edge cases;
- optimize workflow quality, latency, cost, and reliability;
- preserve governance controls during optimization;
- document rollback, monitoring, and re-evaluation triggers; and
- recognize when the responsible repair belongs outside the prompt.

---

# Existing module resources

The repository already contains extended practice material that remains available while the course-aligned sections are developed.

- [notes.md](notes.md): Failure layers, diagnostic evidence, tool and workflow issues, latency, and optimization concepts
- [lab.md](lab.md): Applied troubleshooting exercise
- [flashcards.md](flashcards.md): Active-recall review
- [quiz.md](quiz.md): Original extended scenario quiz

Course-aligned lessons and Module 7 prompt notebooks will be added as each supplied section is completed.

---

# Exam lens

```text
Weak output                              → diagnose before rewriting
Single bad example                       → reproduce and test representative cases
Many variables changed at once           → attribution is lost
Tool fails despite clear prompt          → inspect schema, parameters, and access
Output ends unexpectedly                 → inspect stop and truncation behavior
Quality improved but latency doubled     → optimization tradeoff remains unresolved
Feedback reveals missing requirement     → update task contract, not merely wording
Model upgrade proposed first             → localize the failure before escalating capability
Fix weakens review or data controls       → reject or redesign the optimization
```

For troubleshooting scenarios:

1. define expected versus observed behavior;
2. gather diagnostic evidence;
3. identify the earliest failing stage;
4. distinguish symptom from cause;
5. state one testable hypothesis;
6. make one bounded change;
7. validate against a baseline;
8. test representative and edge cases;
9. measure tradeoffs and governance impact; and
10. keep, revise, revert, or escalate.

---

# Completion criteria

- [ ] I completed Diagnosing Underperforming Prompts & Outputs.
- [ ] I completed Adjusting Approach from Feedback.
- [ ] I completed Optimizing Workflows.
- [ ] I can classify failures without immediately editing the prompt.
- [ ] I can collect evidence and build a minimal reproducible case.
- [ ] I can distinguish prompt, context, model, tool, workflow, and evaluation defects.
- [ ] I can form one testable hypothesis and change one variable at a time.
- [ ] I can use feedback to identify missing requirements or workflow defects.
- [ ] I can validate a repair against representative and edge cases.
- [ ] I can optimize quality, latency, cost, and reliability without weakening governance.
- [ ] I can document rollback and monitoring.
- [ ] I completed the Module 7 quiz and Key Takeaways.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private production prompts, confidential incident details, proprietary logs, credentials, internal connector identifiers, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.

## Official reading

Product behavior and technical guidance can change. Verify current official documentation before relying on implementation-specific details.

- [Troubleshooting tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)
- [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Reducing latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
