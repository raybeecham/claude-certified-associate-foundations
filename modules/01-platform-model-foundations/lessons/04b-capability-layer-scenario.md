# Lesson 4B: Capability Layer Scenario

## A monthly report that became faster and more accurate

> **Illustrative scenario:** The organization, portfolio, timing, and performance results in this lesson are fictional and intended only to teach workflow design.

## Overview

This scenario shows how the capability layer can improve both efficiency and reliability without removing verification or human review.

A business analyst produces a regulatory tracking report every month. The task has four recurring stages:

1. collect the current month's regulatory updates;
2. determine which updates apply to the portfolio;
3. summarize the operational implications; and
4. format the findings using an approved report template.

The work is consequential, but its structure is stable. That combination makes it a strong candidate for layered workflow design.

The central lesson is:

> Reuse stable context, standardize the repeatable procedure, execute calculations, and keep verification in the workflow.

## Learning objectives

After completing this scenario, you should be able to:

- identify the recurring and variable elements in a professional workflow;
- map requirements to Projects, Skills, Code Execution, and Memory;
- distinguish workflow acceleration from removal of controls;
- explain why verification remains necessary after automation;
- calculate the operational benefit of a redesigned workflow;
- identify which capability layers are required and which are optional;
- define measures for quality, efficiency, and control effectiveness; and
- recognize when an encouraging performance trend is not proof of guaranteed future accuracy.

## Scenario setup

A business analyst prepares a monthly regulatory tracking report for a fictional investment portfolio.

Each report requires the same categories of work:

- review newly issued regulatory material;
- identify updates relevant to the portfolio;
- classify applicability and priority;
- summarize business implications;
- calculate affected counts or exposure figures;
- format the result using a defined template; and
- complete a verification review before publication.

The task is high consequence because an incorrect applicability decision or numeric figure could mislead decision-makers. At the same time, the workflow is repetitive enough to formalize.

## Months one and two: Chat-based workflow

During the first two months, the analyst performs the work in a normal Chat.

For each monthly cycle, she:

1. opens a new Chat;
2. uploads the current regulatory documents;
3. re-enters the portfolio background;
4. retypes the applicability criteria;
5. re-enters the required report structure;
6. asks Claude to analyze and draft the report;
7. independently verifies every numeric figure; and
8. reviews the final report before release.

```text
New monthly Chat
       |
       +-- Upload current regulatory documents
       +-- Re-enter portfolio context
       +-- Re-enter applicability criteria
       +-- Re-enter format instructions
       +-- Analyze updates
       +-- Draft report
       +-- Verify calculations
       +-- Human review
       +-- Publish
```

### Results

- Average session time: **65 minutes**
- Month one: **two numeric errors caught before publication**
- Month two: **one numeric error caught before publication**
- Verification step: **performed every month**
- Published errors: **none identified in the scenario**

The verification process worked. It prevented the detected errors from reaching the final report. However, the workflow remained inefficient and relied on language generation for computations that could be executed directly.

## Diagnosing the original workflow

The analyst separates the workflow into stable and variable elements.

### Stable elements

These remain substantially the same every month:

- portfolio background;
- approved terminology;
- applicability criteria;
- report audience;
- report structure;
- escalation thresholds;
- evidence requirements;
- review procedure; and
- calculation definitions.

### Variable elements

These change every reporting cycle:

- newly issued regulatory updates;
- current portfolio state;
- affected holdings or business areas;
- current numeric inputs;
- exceptions and uncertainties; and
- decisions requiring escalation.

### Design problem

The original workflow mixes all of these concerns into one monthly prompt.

```text
Stable context
      +
Repeatable procedure
      +
Current source material
      +
Numeric computation
      +
Review instructions
      =
One large, repeatedly reconstructed Chat workflow
```

The workflow produces usable output, but its architecture makes every session longer and exposes calculations to avoidable generative error.

## Month three: capability-layer redesign

The analyst redesigns the process around distinct responsibilities.

| Requirement | Capability layer | Why |
|---|---|---|
| Reusable portfolio background | Project knowledge | Stable context should not be re-entered monthly |
| Standing evidence and format rules | Project instructions | Durable workstream requirements should apply to every related conversation |
| Prior approved reports | Project knowledge, with version and authority labels | Useful examples and historical references can be reused |
| Repeatable report procedure | Skill | The same analytical and formatting sequence should be followed each month |
| Numeric calculations | Code Execution | Figures should be executed and reconciled rather than generated as prose |
| General working preferences | Memory, only if appropriate | Cross-session preferences may carry forward without becoming workstream evidence |
| Current regulatory updates | Current conversation input | The source set changes each reporting cycle |
| Final approval | Human review | Accountability remains with an authorized reviewer |

## Redesigned architecture

```text
Current monthly regulatory updates
                |
                v
Project
  +-- Portfolio background
  +-- Approved terminology
  +-- Applicability criteria
  +-- Prior approved reports
  +-- Standing evidence and format rules
                |
                v
Skill
  +-- Validate required inputs
  +-- Review each update
  +-- Assess applicability
  +-- Summarize implications
  +-- Flag missing evidence
  +-- Apply report structure
                |
                v
Code Execution
  +-- Calculate affected counts
  +-- Reconcile totals
  +-- Generate tables or charts
  +-- Produce an audit trail
                |
                v
Draft report
                |
                v
Verification and human approval
                |
                v
Published report
```

## What each layer contributes

### Project: stable workstream context

The Project contains the information that should be available every month:

- portfolio description;
- approved scope;
- terminology;
- applicability rules;
- source hierarchy;
- escalation criteria;
- report requirements; and
- prior approved reports selected for reuse.

The Project reduces repeated setup and helps keep the workstream internally consistent.

### Skill: repeatable procedure

The Skill defines how the monthly analysis should be performed:

1. confirm that all required monthly inputs are present;
2. identify each regulatory update;
3. assess portfolio applicability using the approved criteria;
4. separate evidence from inference;
5. summarize implications;
6. route numeric tasks to Code Execution;
7. flag unresolved questions;
8. apply the report template; and
9. produce a reviewer checklist.

The Skill reduces procedural drift. It does not guarantee that every judgment or sentence is correct.

### Code Execution: executed calculations

Numeric work moves from language-only generation to executed operations.

Examples include:

- count of applicable updates;
- count of affected portfolio components;
- percentage of the portfolio affected;
- aggregation by regulatory category;
- comparison with the prior month; and
- reconciliation of report tables with source data.

The computational workflow records:

- input row counts;
- formulas or methods;
- assumptions;
- missing-value handling;
- excluded records;
- output totals; and
- reconciliation results.

### Memory: optional continuity

Memory is not required merely because the workflow is recurring.

Appropriate Memory candidates could include general preferences such as:

- lead with an executive summary;
- use concise headings;
- separate facts, assumptions, and unresolved questions; and
- include explicit next actions.

Portfolio facts, regulatory evidence, applicability rules, and approved report history belong in the Project or an authoritative record, not general Memory.

## Results after redesign

The scenario reports the following illustrative results:

- Session time falls from **65 minutes to 30 minutes**.
- Time saved per monthly cycle: **35 minutes**.
- Percentage reduction in session time: approximately **53.8%**.
- Annualized time savings at twelve reports per year: **420 minutes**, or **7 hours**.
- Verification remains in place.
- No errors are found during the verification step in months three through eight.

### Timing comparison

| Workflow stage | Chat-based workflow | Layered workflow |
|---|---:|---:|
| Reconstruct stable context and instructions | 20 minutes | 3 minutes |
| Analyze current updates | 25 minutes | 15 minutes |
| Calculate and reconcile figures | 10 minutes | 5 minutes |
| Verification and review | 10 minutes | 7 minutes |
| **Total** | **65 minutes** | **30 minutes** |

The exact stage allocation is illustrative. The important result is that repeated setup and manual computational effort were reduced without removing review.

## Faster does not mean less governed

The analyst did **not** improve the workflow by removing verification.

The redesign retained:

- source review;
- numeric reconciliation;
- exception reporting;
- human judgment about applicability;
- reviewer approval; and
- escalation when evidence was incomplete.

```text
Automation
     !=
Control removal
```

A trustworthy redesign automates repeatable mechanics while preserving or improving the controls that protect consequential decisions.

## Interpreting the zero-error period

No errors were found during months three through eight. This is encouraging evidence that the redesigned workflow may be performing better.

It is not proof that:

- future reports will contain no errors;
- the Skill can never drift;
- the Project knowledge will remain current;
- every regulatory judgment is correct;
- the Code Execution method is always valid; or
- verification can be removed.

Six error-free cycles are a performance signal, not a guarantee.

A mature workflow continues to measure:

- detected error rate;
- escaped error rate;
- verification coverage;
- false-positive and false-negative applicability decisions;
- time per report;
- unresolved-evidence count;
- reviewer overrides;
- stale-source findings; and
- computation reconciliation failures.

## The four diagnostic questions

The analyst used four questions to map the workflow to the capability layer.

| Question | Layer it points to |
|---|---|
| Which parts of this task are the same every time? | Project standing instructions and Skill |
| Which reference material recurs across sessions? | Project knowledge base |
| Which outputs must be computed correctly rather than merely sound plausible? | Code Execution |
| Which relevant continuity should carry across sessions without re-entry? | Memory, when appropriate |

A fifth question should also be added:

| Additional question | Control it points to |
|---|---|
| Which decisions remain consequential, uncertain, or accountable to a person? | Verification and human review |

## Why both standing instructions and a Skill may be needed

The question "Which parts are the same every time?" can point to more than one layer.

### Put it in Project instructions when it defines the workstream

Examples:

- use the approved source hierarchy;
- write for the designated audience;
- distinguish evidence from inference;
- apply the workstream's escalation threshold; and
- follow the approved terminology.

### Put it in a Skill when it defines the task procedure

Examples:

- validate the monthly input package;
- assess each update in a specified sequence;
- produce an applicability table;
- route calculations to Code Execution;
- generate the report sections; and
- attach a review checklist.

The Project defines the operating environment. The Skill defines the reusable method.

## Prior reports in the knowledge base

Prior reports can be useful examples, but they require controls.

Before adding them:

- confirm that they are approved for reuse;
- label their reporting period;
- distinguish historical examples from current authority;
- remove superseded or incorrect versions;
- avoid treating old conclusions as current facts;
- identify any sensitive material; and
- define when historical reports should be archived or replaced.

A prior report is evidence of how work was previously presented. It is not automatically proof of the current regulatory state.

## Verification design

A monthly verification checklist could include:

### Source controls

- Every regulatory update is linked to an authoritative source.
- Publication dates and effective dates are confirmed.
- Superseded material is identified.
- Missing or inaccessible sources are reported.

### Applicability controls

- Applicability criteria are applied consistently.
- Ambiguous cases are escalated.
- Unsupported assumptions are labeled.
- Reviewer overrides are documented.

### Computational controls

- Inputs are complete and authorized.
- Formulas and units are documented.
- Totals reconcile with source data.
- Known-case tests pass.
- Excluded or invalid records are listed.

### Deliverable controls

- Required sections are present.
- Findings are supported by evidence.
- Numeric values match executed results.
- The final report receives accountable human approval.

## Capability-layer redesign worksheet

Use this table when redesigning a recurring workflow.

| Workflow element | Stable or variable? | Correct home | Owner | Review cadence | Failure if wrong |
|---|---|---|---|---|---|
| Background context | Stable | Project knowledge | Workstream owner | Quarterly | Incorrect scope |
| Standing rules | Stable | Project instructions | Process owner | Quarterly or on change | Inconsistent analysis |
| Ordered procedure | Stable | Skill | Skill owner | On change and test cycle | Procedure drift |
| Current monthly sources | Variable | Current conversation | Analyst | Every cycle | Stale analysis |
| Numeric calculations | Variable operation, stable method | Code Execution | Analyst or method owner | Every cycle | Incorrect figures |
| General output preference | Stable across workstreams | Memory, if appropriate | User | Monthly | Poor continuity |
| Final decision and release | Consequential | Human review | Authorized reviewer | Every cycle | Unapproved output |

## Efficiency calculation

The workflow improvement can be expressed as:

```text
Time saved per cycle = original time - redesigned time
                     = 65 - 30
                     = 35 minutes
```

```text
Percentage reduction = time saved / original time * 100
                     = 35 / 65 * 100
                     = approximately 53.8%
```

```text
Annual savings = 35 minutes * 12 cycles
               = 420 minutes
               = 7 hours
```

These measures capture direct session time only. A complete business case could also examine:

- avoided rework;
- reduced reviewer effort;
- fewer escaped errors;
- faster decision delivery;
- onboarding time;
- maintenance cost; and
- capability governance overhead.

## Common mistakes

### Removing verification because recent runs were clean

A clean period does not eliminate future risk. Keep consequence-based verification.

### Storing every historical report indefinitely

Uncurated historical documents can introduce stale conclusions and conflicting examples.

### Putting the full procedure in Project instructions

Workstream rules belong in Project instructions. A reusable ordered procedure may be better represented as a Skill.

### Treating Code Execution as proof of correctness

Execution proves that code ran. It does not prove that the formula, assumptions, inputs, or interpretation were correct.

### Using Memory for portfolio facts

Workstream evidence belongs in the Project or authoritative system. Memory is for appropriate continuity, not the source of truth.

### Measuring time but not quality

A workflow that is faster but produces more errors is not an improvement. Track both efficiency and outcome measures.

## Think like an AI engineer

The analyst did not ask only:

> How can I make Claude write this report faster?

She asked:

> Which responsibilities should be persisted, standardized, executed, and reviewed?

That systems question produced the improvement.

```text
Stable context ------> Project
Repeatable method ---> Skill
Computable outputs --> Code Execution
Useful continuity ---> Memory
Consequential result -> Verification and human review
```

## Certification lens

A certification scenario may describe a recurring, high-consequence workflow with repeated setup, consistent formatting, and numeric outputs.

The strongest answer will usually combine capabilities by responsibility:

- Project for stable context and knowledge;
- Skill for the repeatable procedure;
- Code Execution for numeric work;
- Memory only for appropriate cross-session continuity; and
- verification for consequential output.

Do not choose "use all features" merely because all are available. Justify each layer from a requirement.

## Knowledge check

### Question 1

Why did the analyst move portfolio background into a Project?

A. To guarantee identical prose every month  
B. To persist reusable workstream context and reduce repeated setup  
C. To replace the authoritative portfolio system  
D. To eliminate human review

**Answer:** B

### Question 2

What is the best reason to use a Skill in this scenario?

A. It stores all current regulatory facts permanently  
B. It guarantees that no errors can occur  
C. It standardizes the recurring analytical and formatting procedure  
D. It automatically approves the final report

**Answer:** C

### Question 3

Why did numeric calculations move to Code Execution?

A. Executed calculations are more appropriate than plausible language-only numbers  
B. Code Execution makes source documents authoritative  
C. Code Execution removes the need to inspect formulas  
D. It guarantees all applicability judgments

**Answer:** A

### Question 4

What does the zero-error period from months three through eight prove?

A. Verification can now be removed  
B. The workflow can never fail  
C. The observed performance is encouraging but does not guarantee future accuracy  
D. The Skill is deterministic

**Answer:** C

### Question 5

Which item is the weakest general Memory candidate?

A. Preferred executive-summary structure  
B. Preference for explicit assumptions  
C. Current portfolio holdings and regulatory applicability conclusions  
D. Preference for concise headings

**Answer:** C

### Question 6

What is the approximate reduction from 65 minutes to 30 minutes?

A. 35%  
B. 46.2%  
C. 53.8%  
D. 65%

**Answer:** C

## Flashcards

**Q:** What did the Project remove from the monthly workflow?  
**A:** Repeated entry of stable portfolio context, source rules, terminology, and standing format requirements.

**Q:** What did the Skill standardize?  
**A:** The recurring analytical, evidence-handling, formatting, and review-preparation procedure.

**Q:** Why use Code Execution for numeric figures?  
**A:** To execute and reconcile the calculation rather than rely on plausible language generation.

**Q:** Did the redesign remove verification?  
**A:** No. Verification remained a required control.

**Q:** What was the direct time saving per monthly report?  
**A:** 35 minutes.

**Q:** What was the approximate percentage reduction in session time?  
**A:** 53.8%.

**Q:** What does an error-free observation period demonstrate?  
**A:** Encouraging measured performance, not a guarantee of future correctness.

**Q:** Where should prior approved reports be stored?  
**A:** In curated Project knowledge when authorized, versioned, and clearly labeled as historical references.

**Q:** What belongs in Memory in this scenario?  
**A:** Only appropriate general continuity or preferences, not portfolio evidence or current regulatory conclusions.

**Q:** What fifth question complements the four capability questions?  
**A:** Which decisions remain consequential, uncertain, or accountable to a human reviewer?

## Key takeaways

1. Recurring high-consequence work benefits from separating stable context, procedure, computation, and continuity.
2. Projects reduce repeated context loading.
3. Skills standardize the reusable method but do not eliminate variation or review.
4. Code Execution reduces avoidable computational risk, but the method and inputs still require validation.
5. Memory is optional and should contain only appropriate cross-session continuity.
6. Faster workflows should retain or strengthen consequence-based controls.
7. Measure efficiency, quality, and control performance together.
8. A clean run history is evidence, not a guarantee.

## Related material

- [Capability Layer, Skills and Code Execution](04-capability-layer-skills-code-execution.md)
- [Capability Layer, Memory](04a-capability-layer-memory.md)
- [Capability Layer scenario prompts](../../../prompts/module-01/04b-capability-layer-scenario-prompts.md)
- [Capability patterns](../../../patterns/capability-patterns.md)
- [Memory patterns](../../../patterns/memory-patterns.md)

## Version-awareness note

Product capabilities, Skill administration, Memory behavior, Code Execution availability, and Project features can change. Treat current official documentation and organization policy as authoritative.