# Lesson 8: Module 1 Quiz Review

## Overview

This lesson reviews the major selection decisions from Module 1 through original scenario-based questions.

It covers:

1. entry-point selection;
2. Project configuration;
3. Skills and Code Execution;
4. model-tier selection;
5. Context Management; and
6. Project-scoped Memory.

> [!IMPORTANT]
> The questions below are original study material. They reinforce the same concepts as the preparation course without reproducing proprietary assessment wording.

## Course checkpoint result

The learner completed the five-question course checkpoint with a score of:

```text
5 / 5
```

That result demonstrates correct application of the module framework across recurring workflows, verified computation, model tiers, context recovery, and Project-scoped continuity.

A perfect score is a strong signal, but durable readiness requires explaining why the correct answer is stronger than every distractor.

## Learning objectives

After completing this lesson, you should be able to:

- select a Project when stable context recurs;
- place reusable evidence in Project knowledge;
- place durable behavior in standing instructions;
- use Code Execution for consequential calculations;
- identify structured, high-volume work appropriate for Haiku;
- recover a degraded conversation through a validated summary and clean restart;
- separate unrelated workstreams with distinct Projects and scoped Memory;
- distinguish Research from uploaded-source analysis;
- evaluate third-party Skills before enablement;
- distinguish context-length limits from usage limits; and
- explain why model capability does not replace verification.

## Exam strategy

For every scenario, extract the signals before reading the answers.

Use this sequence:

```text
1. Recurrence
2. Stability of background
3. Current-information requirement
4. Calculation requirement
5. Output or deliverable form
6. Ambiguity and consequence
7. Continuity and context health
8. Validation and human review
```

Then ask:

```text
Where should the work happen?
What capabilities are required?
Which model is the minimum qualified tier?
How should context be managed?
What controls remain outside the model?
```

---

# Part 1: Core certification-style quiz

Answer all five questions before opening the answer key.

## Question 1: Recurring access review

A security analyst performs a quarterly access review. Each quarter, the analyst uploads a new access-export file, compares it with an approved role matrix that changes infrequently, and produces the same exception-report format.

Which configuration is the best fit?

- **A.** Open a new Chat each quarter and upload both files every time.
- **B.** Create a Project with the role matrix in Project knowledge, durable exception-report rules in Project instructions, and Code Execution for the comparison.
- **C.** Use Research because the access records change every quarter.
- **D.** Store the prior reports in Memory and use them as the primary source of truth.

## Question 2: Financial exposure calculation

An analyst must calculate projected financial exposure using six numeric inputs, a variable annual rate, monthly compounding, and three scenarios.

Which approach is most trustworthy?

- **A.** Ask Claude to reason through the calculation in prose and review the answer visually.
- **B.** Use Code Execution, document the formula and assumptions, run the scenarios, and reconcile the output.
- **C.** Use Research to find a comparable public calculation.
- **D.** Store the six inputs in Memory so Claude can calculate them consistently.

## Question 3: High-volume structured classification

A team must classify 25,000 short public records into five categories. The taxonomy is explicit, representative examples are available, and uncertain records enter an exception queue.

Which model tier is the best starting point under the certification framework?

- **A.** Haiku
- **B.** Sonnet
- **C.** Opus
- **D.** Always use the default model because tier selection is unrelated to volume.

## Question 4: Context degradation

A consultant has spent several hours in one conversation developing a complex analysis. Claude now omits an early constraint, contradicts an accepted decision, and focuses almost entirely on the latest message.

What should the consultant do next?

- **A.** Upgrade to Opus and keep the current conversation unchanged.
- **B.** Repeat the missing instruction and continue indefinitely in the same thread.
- **C.** Generate and validate a state-capsule summary, persist durable information in the proper location, and restart in a clean conversation.
- **D.** Turn on Research so Claude receives more information.

## Question 5: Workstream separation

A professional supports two unrelated confidential workstreams with different terminology, stakeholders, source material, and approval chains.

Which configuration best reduces cross-workstream context leakage?

- **A.** Keep both workstreams in one long Chat and label each message.
- **B.** Use one Project, but clear Memory manually before switching topics.
- **C.** Create separate Projects and keep Project-scoped context and Memory within the relevant workstream.
- **D.** Use a different model tier for each workstream.

<details>
<summary>Part 1 answer key and rationales</summary>

## Question 1 answer: B

**Best configuration:** Project knowledge + Project instructions + Code Execution.

### Why it is correct

- The workflow recurs quarterly.
- The role matrix is stable reusable evidence.
- The report requirements are durable workstream behavior.
- The comparison uses real records and should be executed and reconciled.
- The new access export remains current-cycle input.

### Why the other answers are weaker

- **A:** It recreates stable context every quarter and repeats avoidable setup.
- **C:** Research is for current multi-source investigation, not comparison of an uploaded dataset with an approved internal reference.
- **D:** Memory is not an authoritative access-control repository and should not replace approved source material.

### Concept tested

Recurring workflow architecture and capability-layer placement.

## Question 2 answer: B

**Best approach:** Code Execution with method validation.

### Why it is correct

The required result is computational. Code Execution can run the formula, preserve assumptions, compare scenarios, and return reproducible outputs.

A trustworthy result requires:

- correct inputs;
- correct units;
- correct formula;
- successful execution;
- known-case or spot-check validation; and
- clear reporting of assumptions.

### Why the other answers are weaker

- **A:** Prose generation may produce a plausible but incorrect number.
- **C:** A comparable public scenario does not calculate the supplied case.
- **D:** Memory provides continuity, not deterministic calculation or authoritative storage of scenario inputs.

### Concept tested

Code Execution and computational verification.

## Question 3 answer: A

**Starting tier:** Haiku.

### Why it is correct

The task is:

- structured;
- high volume;
- low ambiguity;
- supported by representative examples;
- constrained by a fixed taxonomy; and
- protected by an exception queue.

Haiku is the certification model for efficient structured work at scale.

### Why the other answers are weaker

- **B:** Sonnet may work, but it spends additional capability where the clear task may not require it.
- **C:** Opus would over-resource a routine classification workflow unless evaluation reveals difficult ambiguity.
- **D:** Volume and task structure are central model-selection signals.

### Production qualification

Haiku should still pass measured thresholds for precision, recall, severe failure rate, latency, and cost before deployment.

### Concept tested

Minimum-qualified-model selection.

## Question 4 answer: C

**Best response:** Summarize, persist, and restart.

### Why it is correct

The symptoms are consistent with context degradation:

- early constraints are lost;
- accepted decisions are contradicted; and
- recent exchanges dominate the response.

The recovery sequence is:

```text
Summarize current state
        |
Validate the summary
        |
Persist durable information
        |
Start a clean conversation
```

### Why the other answers are weaker

- **A:** A stronger model does not restore missing or compressed context.
- **B:** Repeating one instruction may temporarily help but extends an already degraded thread and may leave other lost state unresolved.
- **D:** Additional external information adds context rather than repairing the lost internal state.

### Concept tested

Context health and the restart, summarize, persist framework.

## Question 5 answer: C

**Best configuration:** Separate Projects with scoped continuity.

### Why it is correct

Different stakeholders, terminology, evidence, confidentiality, and approvals create distinct context boundaries. Separate Projects reduce accidental leakage and conflicting assumptions.

### Why the other answers are weaker

- **A:** Labels do not create reliable context or access separation.
- **B:** Manual Memory clearing is error-prone and still leaves unrelated Project configuration and conversation history mixed.
- **D:** Model tiers affect capability and efficiency, not information boundaries.

### Concept tested

Project scoping and context isolation.

</details>

---

# Part 2: Advanced integrated quiz

These questions combine multiple Module 1 decisions.

## Question 6: Current market investigation

A planning team needs a source-backed comparison of major product announcements made by five competitors during the previous 30 days.

What is the best starting configuration?

- **A.** Chat + Haiku using pretrained knowledge only
- **B.** Research + Sonnet, followed by source review
- **C.** Project + Code Execution + Opus
- **D.** Artifact + Memory with no external search

## Question 7: Recurring narrative report without calculations

A program office produces the same weekly narrative update using stable terminology, the same audience, and a fixed report structure. No numeric analysis is required.

What is the best configuration?

- **A.** Project + Skill + Sonnet
- **B.** Research + Opus
- **C.** Code Execution + Haiku
- **D.** Incognito Chat + Artifact

## Question 8: Third-party Skill request

A third-party Skill claims it can generate high-quality reports, but it requests access to several connectors and its source is not reviewed by the organization.

What is the best response?

- **A.** Enable it because Skills automatically reduce risk.
- **B.** Enable it with confidential data to test its full capability.
- **C.** Review provenance, source, permissions, external communication, logging, revocation, and organizational approval before enabling it.
- **D.** Use Opus, because a stronger model neutralizes Skill risk.

## Question 9: High-stakes ambiguous deliverable

A leadership team needs a polished strategic document based on six reports containing conflicting evidence and uncertain assumptions. The output will be reviewed by executives before a major decision.

Which configuration is the strongest starting point?

- **A.** Chat + Haiku
- **B.** Project knowledge + Artifact + Opus, with source validation and human review
- **C.** Research + Code Execution only
- **D.** Memory + Skill with no reviewer

## Question 10: Usage limit versus context limit

A user reaches a weekly usage threshold while working across several short, clean conversations. None of the individual conversations is near its context limit.

Which statement is correct?

- **A.** The conversations must be suffering from context degradation.
- **B.** Usage limits and context limits are separate; the user should preserve progress and plan around the remaining usage window.
- **C.** Starting a new Chat will always reset the weekly allowance.
- **D.** Moving information into Memory will create more weekly usage capacity.

<details>
<summary>Part 2 answer key and rationales</summary>

## Question 6 answer: B

The previous 30 days require current evidence. Research is appropriate for multi-source investigation and Sonnet is the balanced starting tier for professional synthesis. Source review remains required.

## Question 7 answer: A

The task recurs, the context is stable, and the procedure and output format repeat. The Project holds context, the Skill defines the procedure, and Sonnet supports the narrative work.

Code Execution is unnecessary because no computation is described.

## Question 8 answer: C

Skills are executable or procedural supply-chain components. Their description is a claim, not proof of safety. Apply least privilege and do not enable the Skill until provenance, source, permissions, data flow, monitoring, and approval are understood.

## Question 9 answer: B

The evidence is ambiguous, multi-source, and consequential. Project knowledge organizes the source set, Artifact supports the deliverable lifecycle, Opus raises the reasoning ceiling, and human review retains accountability.

## Question 10 answer: B

A context limit constrains one conversation's working depth. A usage limit constrains the amount of service consumed over time. Hitting one does not prove the other has been reached.

</details>

---

# Scoring and remediation

## Score bands

| Score | Interpretation | Action |
|---|---|---|
| 10/10 | Strong command | Explain every distractor and continue to Key Takeaways |
| 8-9/10 | Ready with minor gaps | Review missed objectives and retake later |
| 6-7/10 | Developing | Revisit the relevant lesson and complete focused drills |
| 0-5/10 | Significant gaps | Repeat the module sequence before advancing |

## Miss-to-lesson map

| Missed question | Review |
|---|---|
| 1 or 7 | Core Entry Points and Capability Layer |
| 2 | Skills and Code Execution |
| 3 | Choosing Models |
| 4 | Context Management |
| 5 | Memory and context boundaries |
| 6 | Research versus Chat |
| 8 | Skill trust evaluation |
| 9 | Artifacts, Project knowledge, and Opus |
| 10 | Context limits versus usage limits |

## Required answer discipline

For every miss, write three sentences:

1. What signal in the scenario controls the answer?
2. Why is the correct configuration the best fit?
3. Why was the selected distractor weaker?

This converts recognition into reusable judgment.

---

# Five high-value flashcards

## Flashcard 1

**Q:** What configuration fits a recurring workflow with stable reference material and verified calculations?

**A:** Project context plus Code Execution, with a Skill when the procedure repeats.

## Flashcard 2

**Q:** What model is the certification starting point for structured high-volume classification?

**A:** Haiku, subject to measured quality thresholds.

## Flashcard 3

**Q:** What should happen when a long conversation loses early decisions and constraints?

**A:** Create and validate a summary, persist durable state, and restart in a clean conversation.

## Flashcard 4

**Q:** How should unrelated confidential workstreams be separated?

**A:** Use separate Projects and keep Project-scoped context and Memory within the relevant workstream.

## Flashcard 5

**Q:** Does Code Execution alone prove a result is correct?

**A:** No. Inputs, assumptions, formulas, units, logic, and outputs still require validation.

---

# Certification lens

The quiz tests selection logic, not feature memorization.

The strongest answer usually follows this pattern:

```text
Recurring stable context        -> Project
Repeatable procedure            -> Skill
Consequential calculation       -> Code Execution
Current multi-source evidence   -> Research
Editable deliverable            -> Artifact
Structured high-volume work     -> Haiku
Most professional work          -> Sonnet
Ambiguous high-stakes reasoning -> Opus
Degraded thread                 -> Summarize, persist, restart
Separate workstreams            -> Separate Projects and scoped continuity
```

## Final readiness test

You are ready to advance when you can:

- score at least 80 percent;
- explain why every correct answer is correct;
- explain why every distractor is weaker;
- identify the scenario signal before naming a feature; and
- state what validation or human review remains necessary.

## Related material

- [Platform Selection Exercise](07-platform-selection-exercise.md)
- [Context Management](06-context-management.md)
- [Choosing Models](05-choosing-models.md)
- [Capability Layer Checkpoint](04c-capability-layer-checkpoint.md)
- [Baseline Module 1 quiz](../quiz.md)
- [Quiz and remediation prompts](../../../prompts/module-01/08-module-1-quiz-prompts.md)
