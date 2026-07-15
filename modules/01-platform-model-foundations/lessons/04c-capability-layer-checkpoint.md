# Lesson 4C: Capability Layer Checkpoint

## Overview

This checkpoint tests whether you can place each part of a recurring workflow into the correct capability layer.

The four buckets used here are:

1. **Project standing instructions** for durable rules that define how Claude should behave within the workstream.
2. **Project knowledge or task source material** for the documents and facts Claude should analyze.
3. **Skill** for the repeatable procedure used to perform the task.
4. **Code Execution** for calculations that should be run rather than generated as plausible prose.

The central distinction is:

```text
Standing instructions define how Claude should behave.
Knowledge defines what Claude should know or analyze.
Skills define how the recurring task should be performed.
Code Execution performs the calculation.
```

> [!IMPORTANT]
> A workflow can use all four layers at once. The goal is not to choose one feature for the entire task. The goal is to assign each responsibility to the narrowest layer that matches its purpose.

## Learning objectives

After completing this checkpoint, you should be able to:

- distinguish standing instructions from knowledge;
- distinguish Project configuration from a reusable Skill;
- identify calculations that belong in Code Execution;
- separate reusable reference material from current-cycle source documents;
- explain why the same Project may contain both instructions and knowledge;
- map a recurring contract-review workflow to capability layers; and
- recognize where human legal review remains necessary.

## Scenario

A fictional company performs recurring contract reviews using an approved contract playbook.

Each review cycle contains five components:

1. a durable rule requiring Claude to identify clauses that depart from the playbook and summarize the departure;
2. the company's approved contract playbook;
3. the contract documents being reviewed in the current cycle;
4. a recurring procedure that extracts flagged clauses and formats them into the standard review report; and
5. a calculation of financial exposure from a variable-rate penalty clause.

Your task is to place each component into the most appropriate capability layer.

## Answer key

| Component | Correct layer | Why |
|---|---|---|
| Rule to flag departures from the playbook and explain each departure | Project standing instructions | It defines durable behavior and review expectations for the workstream |
| Approved contract playbook | Project knowledge | It is reusable reference material that supplies acceptable terms, required clauses, and risk thresholds |
| Contract documents for the current review cycle | Task source material, mapped to the knowledge bucket for this checkpoint | They are the evidence Claude must analyze for the current review |
| Procedure that extracts flagged clauses and formats the standard report | Skill | It is the repeatable method applied each time a contract is reviewed |
| Financial-exposure calculation for a variable-rate penalty clause | Code Execution | The result should be computed and validated rather than generated through language alone |

## Standing instructions

Standing instructions answer:

> How should Claude behave throughout this workstream?

Examples include:

- compare each relevant clause against the approved playbook;
- identify departures from approved terms;
- explain each departure in concise language;
- distinguish evidence from inference;
- avoid treating the model's analysis as final legal advice;
- flag ambiguous provisions for human review;
- use the approved terminology; and
- follow the required report structure.

### Why the departure rule belongs here

The rule is not a fact about one contract. It is not a calculation. It is not the full review procedure.

It is a durable expectation that should apply every time Claude works inside the contract-review Project.

```text
Durable workstream rule
        |
        v
Project standing instruction
```

### Example standing instruction

```text
For each reviewed contract, compare the relevant clauses with the approved contract playbook.

Flag any clause that materially departs from the approved position. For each flagged clause:
- quote or identify the relevant language;
- name the applicable playbook rule;
- explain the departure in one sentence;
- classify the issue using the approved risk scale; and
- mark uncertain cases for qualified human review.

Do not present the analysis as final legal advice.
```

## Project knowledge

Project knowledge answers:

> What reusable evidence or reference material should Claude use?

The approved contract playbook belongs here because it contains the organization's reusable rules and thresholds.

It may define:

- acceptable payment terms;
- required clauses;
- prohibited language;
- fallback positions;
- risk thresholds;
- escalation rules;
- approved definitions; and
- review examples.

### Why the playbook is not a standing instruction

The playbook contains substantive reference material. It tells Claude what the approved positions are.

Standing instructions tell Claude what to do with that material.

```text
Playbook
   = what the approved position is

Standing instruction
   = how Claude should compare and report
```

## Current contract documents

The contract documents are the source material for the current review cycle.

In the checkpoint's four-bucket model, they are placed in the **knowledge** bucket because they are documents Claude must know and analyze.

Architecturally, there is an important lifecycle distinction:

- the approved playbook is reusable Project knowledge;
- the current contract is cycle-specific task input;
- the contract should not automatically become permanent Project knowledge merely because it was uploaded for analysis.

### Recommended placement

```text
Reusable approved playbook
        -> Project knowledge

Current contract under review
        -> Current conversation or cycle-specific source input
```

This distinction prevents a Project knowledge base from becoming a permanent archive of every contract ever reviewed.

### Data-handling questions

Before uploading a contract, confirm:

- the user is authorized to provide it;
- the workspace is approved for the contract's sensitivity;
- unnecessary personal or confidential data is minimized;
- retention and deletion expectations are understood;
- access is limited to the correct reviewers; and
- generated excerpts do not expose more information than needed.

## Skill

A Skill answers:

> What repeatable procedure should Claude follow every time this task occurs?

The report-generation and clause-extraction procedure belongs in a Skill because the method repeats across review cycles.

A contract-review Skill might define:

1. confirm that the playbook and contract are available;
2. identify the relevant clauses;
3. compare each clause against the playbook;
4. extract departures;
5. classify risk using approved criteria;
6. separate direct evidence from interpretation;
7. route calculations to Code Execution;
8. format the standard review report;
9. identify unresolved questions; and
10. produce a human-review checklist.

### Skill versus standing instructions

| Standing instructions | Skill |
|---|---|
| Define durable workstream behavior | Define the ordered review procedure |
| Apply across related conversations | Activate when the task type is relevant |
| State source, tone, and escalation rules | Describe extraction, comparison, and formatting steps |
| Answer "how should Claude behave here?" | Answer "how should this task be performed?" |

### Skill limitation

A Skill improves procedural consistency. It does not guarantee:

- correct legal interpretation;
- identical prose;
- complete issue detection;
- correct source documents;
- valid calculations; or
- removal of the need for attorney or contract-specialist review.

## Code Execution

Code Execution answers:

> Which result should be calculated by running a method rather than generated as language?

A penalty clause with a variable rate may depend on:

- transaction value;
- duration;
- rate tiers;
- caps or floors;
- compounding rules;
- triggering conditions;
- currency; and
- effective dates.

That calculation should be executed and documented.

### Example computational workflow

```text
Clause terms
     +
Authorized financial inputs
     +
Documented formula
     |
     v
Code Execution
     |
     +-- calculate exposure
     +-- test boundary cases
     +-- apply caps and floors
     +-- record assumptions
     +-- return reconciliation
     |
     v
Reviewer validation
```

### Example prompt

```text
Use Code Execution to calculate the potential financial exposure from the penalty clause.

Inputs:
[AUTHORIZED INPUTS]

Before calculating:
- extract the formula and variables from the clause;
- identify ambiguous terms;
- state units, dates, rate tiers, caps, floors, and assumptions;
- stop and request clarification if the method cannot be determined reliably.

After calculating, return:
- formula used;
- input values;
- intermediate steps;
- final result;
- boundary-case tests;
- assumptions and uncertainties; and
- a warning that qualified review is still required.
```

### Executed does not mean legally correct

Code Execution can correctly run the wrong interpretation.

Therefore, validate:

1. the clause was interpreted correctly;
2. the correct inputs were used;
3. rates and units were normalized;
4. caps, floors, and dates were applied correctly;
5. boundary cases were tested; and
6. the result was reviewed by an accountable person.

## Why each layer is used

The checkpoint intentionally uses every layer at least once.

```text
Project standing instructions
        -> durable review behavior

Project knowledge or task sources
        -> playbook and contract evidence

Skill
        -> repeatable review and reporting procedure

Code Execution
        -> variable-rate financial calculation
```

The design is modular. Each layer owns one kind of responsibility.

## The most important exam distinction

### Standing instructions define behavior

Examples:

- always flag departures;
- cite the relevant playbook rule;
- escalate ambiguous cases;
- use the approved risk categories.

### Knowledge defines available evidence

Examples:

- the contract playbook;
- the contract under review;
- approved definitions;
- authorized reference documents.

A Project can contain both, but they serve different functions.

## Decision rules

Use these compact rules:

```text
Stable rule for the workstream      -> Project standing instructions
Reusable approved reference         -> Project knowledge
Current document to analyze         -> Current task source material
Repeatable ordered method            -> Skill
Calculation or transformation        -> Code Execution
Final legal or business judgment     -> Human review
```

## Additional practice

Classify each item before opening the answer.

### Item 1

"Use the organization's approved risk labels and escalate every critical deviation."

<details>
<summary>Answer</summary>

**Project standing instructions.** This is durable behavior for the workstream.

</details>

### Item 2

A current, approved list of required data-protection clauses.

<details>
<summary>Answer</summary>

**Project knowledge.** It is reusable authoritative reference material.

</details>

### Item 3

A procedure that identifies governing-law clauses, compares them with approved positions, and produces a deviation table.

<details>
<summary>Answer</summary>

**Skill.** It defines the repeatable task procedure.

</details>

### Item 4

A calculation of total termination fees across three pricing periods.

<details>
<summary>Answer</summary>

**Code Execution.** The numeric result should be computed and reconciled.

</details>

### Item 5

A draft agreement received today for a single review.

<details>
<summary>Answer</summary>

**Current task source material.** In the checkpoint's simplified buckets, this maps to knowledge, but it should normally remain cycle-specific rather than permanent Project knowledge.

</details>

### Item 6

"Write all review summaries for a nontechnical procurement audience."

<details>
<summary>Answer</summary>

**Project standing instructions.** This defines a durable audience and communication rule.

</details>

## Mini knowledge check

### Question 1

What is the best distinction between standing instructions and Project knowledge?

A. Instructions are temporary, while knowledge is permanent.

B. Instructions define behavior, while knowledge supplies reference material and evidence.

C. Instructions are only for calculations, while knowledge is only for prose.

D. There is no meaningful difference.

<details>
<summary>Answer</summary>

**B.** Standing instructions define how Claude should behave. Knowledge provides what Claude should use or analyze.

</details>

### Question 2

Why should a variable-rate penalty calculation use Code Execution?

A. It guarantees the legal interpretation is correct.

B. It removes the need for human review.

C. It runs a documented calculation instead of relying on plausible language generation.

D. It automatically stores the result in Memory.

<details>
<summary>Answer</summary>

**C.** Execution improves computational reliability and reproducibility, but the interpretation and inputs still require validation.

</details>

### Question 3

Why does the report procedure belong in a Skill rather than only in Project instructions?

A. Skills store authoritative contract documents.

B. Skills define the reusable ordered method for the task.

C. Skills eliminate output variation.

D. Skills replace the Project.

<details>
<summary>Answer</summary>

**B.** The Skill encapsulates the repeated extraction, comparison, classification, and formatting procedure.

</details>

### Question 4

Should every reviewed contract be retained permanently in Project knowledge?

A. Yes, because more knowledge always improves quality.

B. Yes, because Projects automatically classify and delete stale files.

C. No. Current-cycle contracts are usually task inputs unless there is an authorized reason to retain them.

D. No, because Claude cannot analyze uploaded contracts.

<details>
<summary>Answer</summary>

**C.** Retention should follow purpose, authorization, sensitivity, and lifecycle requirements.

</details>

## Flashcards

**Q:** What do Project standing instructions define?

**A:** Durable behavior, rules, source use, tone, escalation, and output expectations for the workstream.

---

**Q:** What does Project knowledge provide?

**A:** Curated reusable reference material and evidence.

---

**Q:** Where does a repeatable contract-review procedure belong?

**A:** In a Skill.

---

**Q:** Where does a variable-rate financial exposure calculation belong?

**A:** In Code Execution, followed by method and result validation.

---

**Q:** Why can both standing instructions and knowledge live in one Project?

**A:** The instructions define how Claude behaves, while the knowledge defines what information Claude can use.

---

**Q:** Does a successful calculation remove the need for legal review?

**A:** No. Code can execute a formula correctly even when the clause interpretation or inputs are wrong.

## Certification lens

Expect the certification to test placement and reasoning rather than simple feature recall.

When presented with a workflow component, ask:

1. Is this a durable behavioral rule?
2. Is this evidence or reference material?
3. Is this a repeatable ordered procedure?
4. Is this a calculation or transformation?
5. Is a human still accountable for the final interpretation or decision?

## Key takeaways

- Standing instructions define behavior.
- Knowledge supplies reference material and task evidence.
- Skills define reusable procedures.
- Code Execution performs calculations and transformations.
- Current-cycle documents should not automatically become permanent Project knowledge.
- Capability layers improve organization and consistency, but they do not replace qualified human review.

## Related material

- [Skills and Code Execution](04-capability-layer-skills-code-execution.md)
- [Memory](04a-capability-layer-memory.md)
- [Capability Layer Scenario](04b-capability-layer-scenario.md)
- [Capability patterns](../../../patterns/capability-patterns.md)
- [Checkpoint prompts](../../../prompts/module-01/04c-capability-layer-checkpoint-prompts.md)
