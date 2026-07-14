# Lesson 4: Capability Layer, Skills and Code Execution

## Overview

Entry points determine **where** work happens. The capability layer determines **what Claude can do inside that work environment**.

Professional workflows often require more than text generation. They may need persistent background, a repeatable procedure, executed calculations, or continuity across sessions. The capability layer separates those needs into distinct architectural concerns.

This lesson introduces the four-layer model and focuses on Skills and Code Execution:

1. **Projects carry context.**
2. **Skills define procedures.**
3. **Code Execution performs and verifies computations.**
4. **Memory carries relevant continuity across sessions.**

> [!IMPORTANT]
> The layers are independent. Use only the combination the task requires. A one-off explanation may need none of them. A recurring analytical workflow may use all four.

## Learning objectives

After completing this lesson, you should be able to:

- distinguish entry points from capability features;
- explain the different roles of Projects, Skills, Code Execution, and Memory;
- decide when a reusable procedure should become a Skill;
- explain why Skills reduce variance without eliminating review;
- perform a basic trust evaluation before enabling a Skill;
- decide when computation should be executed rather than generated as prose;
- identify the limits of Code Execution as a verification control; and
- combine capability layers without adding unnecessary complexity.

## The four-layer model

Each layer answers a different question.

| Layer | Primary purpose | Design question |
|---|---|---|
| Projects | Persistent workstream context | What background, sources, and standing instructions should apply? |
| Skills | Reusable procedure | How should this task be performed consistently? |
| Code Execution | Executed computation and file operations | What should be calculated, transformed, visualized, or generated programmatically? |
| Memory | Cross-session continuity | Which relevant facts or preferences should carry forward? |

```text
Professional task
      |
      +-- Context needed repeatedly? ----------> Project
      |
      +-- Procedure repeated consistently? ----> Skill
      |
      +-- Numeric or data result must run? ----> Code Execution
      |
      +-- Relevant continuity across sessions? -> Memory
```

The layers are composable, not hierarchical prerequisites. A Skill can be useful inside or outside a Project. Code Execution can support a one-off Chat or a recurring Project workflow. Memory can assist continuity without replacing a curated Project knowledge base.

## Separate context, procedure, computation, and continuity

A common design error is placing every requirement into one large prompt. The four-layer model provides a cleaner separation of concerns.

| Concern | Appropriate home | Example |
|---|---|---|
| Stable background | Project knowledge | Public policies, approved terminology, reference documents |
| Durable workstream rules | Project instructions | Audience, source hierarchy, required review gates |
| Repeatable task procedure | Skill | How to create a standardized status report or review a spreadsheet |
| Deterministic operation | Code Execution | Calculate totals, normalize dates, deduplicate records |
| Cross-session preference | Memory | Preferred writing style or recurring format preference |
| Current task input | Conversation | This week's updates or the file being analyzed now |

A well-designed workflow puts information in the narrowest layer that matches its lifecycle.

---

## Projects carry context

Projects answer:

> What background knowledge and standing instructions apply to this workstream?

A Project is useful when the work recurs and depends on stable context. It can contain curated knowledge, standing instructions, and separate conversations for related tasks.

Projects do not define every detailed procedure, perform calculations by themselves, or guarantee that every Project conversation knows the full content of every other thread.

### Example

A recurring public-policy analysis Project might contain:

- approved public source material;
- a glossary of terms;
- standing instructions for citations and uncertainty;
- required deliverable structure; and
- separate conversations for research, analysis, and review.

The Project establishes the operating environment. Other capability layers can be added when the workflow needs them.

---

## Skills define procedures

### What a Skill is

A Skill is a reusable procedure for a task type. It tells Claude how to approach that task in a consistent way.

The course model describes built-in Skills for common professional document tasks, such as creating, editing, or analyzing spreadsheets, documents, presentations, and PDFs. Custom Skills can support organization-specific or task-specific workflows when enabled and approved.

In the course model, Skills are associated with the account or workspace rather than being stored as the configuration of one specific Project. A relevant Skill can therefore apply in conversations inside or outside a Project. Product availability, administration, and invocation behavior can change, so verify current behavior in official documentation and workspace settings.

### Skill versus Project

Projects and Skills solve different problems.

| Project | Skill |
|---|---|
| Carries workstream context | Defines a reusable procedure |
| Holds standing instructions and curated knowledge | Encapsulates how a task should be performed |
| Scoped to a persistent workstream | Can apply wherever the task type is relevant |
| Answers "what should Claude know here?" | Answers "how should Claude do this?" |

### Example

A Project may contain the background and evidence for a recurring reporting workstream. A report-generation Skill may define the steps used to transform current updates into the approved report structure.

```text
Project context
   +-- Background
   +-- Approved sources
   +-- Audience and terminology

Skill procedure
   +-- Validate required inputs
   +-- Classify status and risks
   +-- Apply report structure
   +-- Flag missing evidence
   +-- Produce review checklist
```

### What belongs in a Skill

A useful Skill specification may define:

- triggering task type;
- required inputs;
- ordered procedure;
- source restrictions;
- required output sections;
- formatting rules;
- missing-data behavior;
- escalation conditions;
- prohibited actions;
- validation steps; and
- review expectations.

Temporary facts do not belong in a reusable Skill. They belong in the current conversation or the relevant Project knowledge.

## Skills reduce variance, not eliminate it

A Skill can make procedure, structure, and terminology more consistent. It does not convert Claude into deterministic software.

| Can become more consistent | Can still vary |
|---|---|
| Required sections | Prose wording |
| Procedure order | Supporting examples |
| Input checks | Sentence structure |
| Output schema | Emphasis within allowed bounds |
| Source rules | Explanatory detail |
| Review checklist | Stylistic phrasing |

The correct goal is controlled variation. Define which properties must remain invariant and which may vary.

### Example prompt: define a variation contract

```text
For this recurring procedure, separate the requirements into:

1. invariants that must remain consistent on every run;
2. elements that may vary within an approved range;
3. facts that must be grounded in current inputs;
4. results that require deterministic validation; and
5. conditions that require human review.

Return the result as a control table before executing the procedure.
```

## Skills require a trust evaluation

A Skill may influence how Claude processes files, data, or connected resources available in the session. Treat enablement as a software and data-governance decision, not merely a convenience setting.

### Minimum trust review

| Review area | Questions |
|---|---|
| Source | Who created and maintains the Skill? |
| Purpose | What task does it claim to perform? |
| Procedure | What instructions or code does it contain? |
| Data access | What files, connectors, or information could it receive? |
| Permissions | What actions or resources can it use? |
| External communication | Can data leave the approved environment? |
| Integrity | Is the source reviewable and versioned? |
| Approval | Is it provided by Anthropic or approved by the organization? |
| Monitoring | How will unexpected behavior be detected? |
| Revocation | How can it be disabled or removed? |

Lower-risk starting points include Anthropic-provided capabilities and Skills that have completed the organization's review process. Third-party Skills should not be enabled solely because their descriptions appear useful.

### Security rule

> Do not grant a Skill more data or permissions than the task requires.

This is an application of least privilege.

### Example prompt: Skill trust review

```text
Review the following Skill before enablement.

Skill source:
[SOURCE]

Declared purpose:
[PURPOSE]

Requested permissions and accessible data:
[DETAILS]

Evaluate:
- provenance;
- instruction and code transparency;
- permission scope;
- data exposure;
- external communication;
- supply-chain risk;
- update mechanism;
- logging and monitoring;
- revocation path; and
- organizational approval.

Return a recommendation of approve, approve with restrictions, require further review, or reject. Do not infer safety from the Skill description alone.
```

---

## Code Execution performs computation

### What Code Execution is

Code Execution is a sandboxed environment in which Claude can write and run code to perform calculations, transform data, create visualizations, or generate supported files.

The user does not need to author the code manually. Claude can construct the program, execute it, inspect the result, and return the output or generated file when the product supports that workflow.

### Why execution differs from prose generation

Claude's language generation is probabilistic. It can explain arithmetic and often produce correct results, but a plausible-looking number is not evidence that the calculation was actually performed correctly.

Code Execution changes the method:

```text
Language-only request
   |
   +-- Generate a plausible numerical answer

Code Execution request
   |
   +-- Define operation
   +-- Run code
   +-- Observe output
   +-- Report result
```

The second path provides an executed result and a reproducible method.

### Use Code Execution when

- numeric results will be used, reported, or compared;
- totals, averages, projections, or statistics are required;
- data must be cleaned, normalized, joined, filtered, or deduplicated;
- a chart or visualization is required;
- a spreadsheet or structured file must be produced;
- repetitive transformations should be automated;
- a calculation should be reproduced or audited; or
- a large dataset exceeds what should be reasoned through manually in prose.

### Common examples

| Task | Why Code Execution helps |
|---|---|
| Calculate summary statistics | Executes the formulas rather than guessing |
| Normalize dates | Applies a consistent transformation across all rows |
| Deduplicate records | Uses explicit matching rules and reports affected rows |
| Reconcile two tables | Performs joins and exception reporting |
| Generate a chart | Creates the visualization from the underlying data |
| Build a workbook | Produces a real structured file with formulas and sheets |
| Validate a checksum | Runs the algorithm on the supplied input |
| Compare scenario projections | Applies the same model to each scenario |

## Executed does not mean automatically correct

Code Execution verifies that code ran and produced an output. It does not automatically prove that:

- the input data was complete or authorized;
- the correct formula was selected;
- units were interpreted correctly;
- assumptions were valid;
- missing values were handled appropriately;
- the code was free of logic errors;
- the visualization was not misleading; or
- the generated file met every business requirement.

A trustworthy workflow validates both **execution** and **methodology**.

```text
Correct inputs
      +
Correct method
      +
Successful execution
      +
Validated output
      =
Usable result
```

### Minimum validation for computational work

1. Confirm the source and scope of the input data.
2. Record assumptions, units, and missing-value behavior.
3. Inspect or summarize the generated code and formulas.
4. Test known cases or spot-check results independently.
5. Reconcile totals before and after transformation.
6. Review warnings, excluded rows, and errors.
7. Validate the final chart or file against acceptance criteria.
8. Preserve enough detail to reproduce the result.

### Example prompt: verified data transformation

```text
Use Code Execution for this task.

Input:
[ATTACHED DATASET]

Perform these operations:
1. inspect the schema and data types;
2. report row count, missing values, and duplicate candidates;
3. normalize dates to ISO 8601;
4. deduplicate using the stated business key;
5. calculate the requested summary statistics;
6. reconcile row counts and totals before and after transformation;
7. create the requested visualization; and
8. export the cleaned data and an audit report.

Before executing, state:
- assumptions;
- proposed method;
- treatment of missing or invalid values; and
- acceptance checks.

After executing, return:
- results;
- transformations performed;
- code or formula summary;
- exceptions and warnings;
- reconciliation results; and
- generated files.

Do not silently discard rows or invent missing values.
```

## Code Execution and sensitive data

Sandboxing does not remove the need for data governance.

Before uploading or processing data, confirm:

- the user is authorized to provide it;
- the environment is approved for its sensitivity;
- unnecessary fields have been removed;
- credentials and secrets are excluded;
- generated files do not expose hidden sensitive fields;
- retention and sharing rules are understood; and
- outputs receive appropriate access controls.

---

## Memory persists continuity

Memory is introduced here as the continuity layer and covered in greater depth in the next lesson.

Memory answers:

> Which relevant facts, preferences, or ongoing details should carry forward across sessions without being re-entered?

Memory does not replace:

- Project standing instructions;
- a curated Project knowledge base;
- authoritative source documents;
- task-specific input; or
- formal records and version control.

A useful first distinction is:

| Need | Better fit |
|---|---|
| Stable workstream context and sources | Project |
| Reusable task procedure | Skill |
| Executed calculation or transformation | Code Execution |
| Relevant cross-session preference or continuity | Memory |

---

## Combining the layers

### Example: recurring analytical report

A fictional operations team produces a monthly public-data performance report.

| Layer | Role in the workflow |
|---|---|
| Project | Stores public reference documents, terminology, audience, and reporting rules |
| Skill | Defines the repeatable report-generation procedure |
| Code Execution | Cleans the monthly dataset, calculates metrics, and creates charts |
| Memory | Carries the user's stable style and collaboration preferences where appropriate |

```text
Monthly dataset
      |
      v
Project context and source rules
      |
      v
Skill procedure
      |
      v
Code Execution for metrics and charts
      |
      v
Draft report
      |
      v
Evidence checks and human review
```

The workflow does not become reliable merely because all four layers are present. Reliability still depends on good inputs, narrow permissions, validated procedures, correct methods, and review.

## Capability-selection matrix

| Requirement | Capability to consider | Reason |
|---|---|---|
| Same background reused across sessions | Project | Avoid repeated context loading |
| Same procedure used across task instances | Skill | Standardize execution steps |
| Numbers must be calculated or reconciled | Code Execution | Run deterministic operations |
| Data must be cleaned or transformed | Code Execution | Apply consistent programmatic rules |
| Output must be a generated supported file | Code Execution or document Skill | Create the real deliverable |
| Stable preference should carry forward | Memory | Preserve relevant continuity |
| One-off explanation | None required | Keep the workflow simple |

## Common mistakes

### Mistake 1: Treating a Project as a procedure

A Project supplies context and instructions, but a reusable multi-step task may be better represented as a Skill.

### Mistake 2: Treating a Skill as deterministic software

A Skill improves procedural consistency. Generated language can still vary and still requires review.

### Mistake 3: Assuming executed output is automatically correct

Code can faithfully execute the wrong formula. Validate the method, inputs, and result.

### Mistake 4: Enabling a third-party Skill without review

Convenience does not replace provenance, permission, and data-access assessment.

### Mistake 5: Using every capability by default

Each layer introduces setup, maintenance, access, and review considerations. Use the least complex combination that satisfies the task.

### Mistake 6: Using Memory as a formal knowledge repository

Memory supports continuity. Authoritative and versioned information belongs in controlled sources or a curated Project.

## Certification lens

Scenario questions are likely to test whether you can identify the missing capability rather than recall a feature definition.

Ask:

1. Is the problem repeated context? Consider a Project.
2. Is the problem repeated procedure? Consider a Skill.
3. Is the problem numeric correctness, data transformation, visualization, or file generation? Consider Code Execution.
4. Is the problem cross-session continuity? Consider Memory.
5. What review remains necessary after adding the capability?

A strong answer selects only the capabilities that address the stated requirements.

## Think like an AI engineer

The key design principle is separation of concerns:

> Context is not procedure. Procedure is not computation. Computation is not continuity.

Treat each as a separate control surface. This makes the workflow easier to maintain, test, secure, and explain.

## Hands-on lab

### Part 1: Select the capability layers

For each scenario, select Project, Skill, Code Execution, Memory, none, or a combination.

1. A one-time request to rewrite a short paragraph.
2. A weekly report that uses the same background and section structure.
3. A spreadsheet containing 80,000 records must be normalized and deduplicated.
4. A user wants Claude to retain a stable preference for concise executive summaries.
5. A team repeatedly converts approved source material into the same review checklist.
6. A recurring dashboard uses stable reference documents, a standard procedure, calculated metrics, and generated charts.

For each answer, explain:

- what requirement triggered the capability;
- what should remain outside that capability;
- what validation is still required; and
- whether the capability adds more value than overhead.

### Part 2: Design a Skill

Choose a recurring professional task and write a Skill specification containing:

- purpose;
- trigger;
- required inputs;
- ordered steps;
- source rules;
- output contract;
- missing-data behavior;
- prohibited actions;
- validation; and
- human review.

Then separate the specification into:

- invariants;
- allowed variation; and
- task-specific facts.

### Part 3: Compare generation with execution

Use a small public or synthetic dataset.

1. Ask for totals and averages without requesting Code Execution.
2. Repeat the task using Code Execution.
3. Independently spot-check at least three results.
4. Compare reproducibility, transparency, and error handling.
5. Record whether the method, not only the final number, was correct.

### Part 4: Perform a trust review

Select a hypothetical third-party Skill and document:

- creator and provenance;
- requested permissions;
- accessible data;
- external communication;
- update channel;
- review evidence;
- monitoring plan;
- revocation method; and
- final recommendation.

## Knowledge check

1. What is the difference between a Project and a Skill?
2. Why can two runs of the same Skill produce different prose?
3. What should remain invariant in a well-designed Skill?
4. Why should a third-party Skill receive a trust evaluation?
5. When should Code Execution be preferred over ordinary language generation?
6. Does successful code execution prove that the analytical method was correct?
7. Which layer is best suited to stable cross-session preferences?
8. Why is using all four layers not automatically the best design?

### Answer guide

1. A Project carries workstream context and standing instructions. A Skill defines a reusable task procedure.
2. Claude remains probabilistic even when the procedure is configured.
3. Required steps, schemas, source restrictions, safety constraints, and validation rules should remain controlled.
4. A Skill can influence processing and may receive access to session data or resources. Provenance and permissions matter.
5. Use Code Execution when numeric results, transformations, charts, or generated files must be produced through an executed process.
6. No. The code may use incorrect inputs, assumptions, units, or formulas.
7. Memory, subject to current product behavior and data policy.
8. Each layer adds overhead and risk. Use only the capabilities justified by the task.

## Flashcards

**Q:** What question does a Project answer?  
**A:** What background knowledge and standing instructions apply to this workstream?

**Q:** What question does a Skill answer?  
**A:** How should this task be performed consistently?

**Q:** What question does Code Execution answer?  
**A:** What should be calculated, transformed, visualized, or generated through executed code?

**Q:** What question does Memory answer?  
**A:** Which relevant facts or preferences should carry forward across sessions?

**Q:** Do Skills eliminate output variation?  
**A:** No. They reduce procedural variance but generated outputs still vary and require review.

**Q:** Where should temporary task facts be placed?  
**A:** In the current conversation or task input, not in a reusable Skill.

**Q:** What is the first security principle for Skills?  
**A:** Review provenance and grant only the minimum data and permissions required.

**Q:** Why use Code Execution for reported numbers?  
**A:** It runs the calculation and provides a reproducible method rather than relying only on plausible language generation.

**Q:** Does sandboxed execution eliminate data-governance requirements?  
**A:** No. Authorization, minimization, sensitivity, retention, and access controls still apply.

**Q:** What does successful execution prove?  
**A:** That the code ran and produced an output, not automatically that the inputs or methodology were correct.

**Q:** What is the core architectural principle of the four-layer model?  
**A:** Separate context, procedure, computation, and continuity.

**Q:** Should every workflow use every capability?  
**A:** No. Use the least complex combination that meets the requirements.

## Key takeaways

- Entry points determine where work lives. Capability layers determine what Claude can do there.
- Projects carry persistent workstream context.
- Skills encode reusable procedures and improve consistency without removing variation.
- Skills require provenance, permission, and data-access review.
- Code Execution should be used for calculations, transformations, visualizations, and supported file generation when an executed result matters.
- Executed code still requires validation of inputs, assumptions, methodology, and outputs.
- Memory supports continuity and does not replace controlled sources or Project knowledge.
- Reliable workflows use the minimum justified combination of capabilities and preserve human review where consequences require it.

## Related material

- [Module Introduction](01-module-introduction.md)
- [How Claude Behaves](02-how-claude-behaves.md)
- [Core Entry Points](03-core-entry-points.md)
- [Core Entry Points worked example](03a-core-entry-points-worked-example.md)
- [Capability Layer prompt notebook](../../../prompts/module-01/04-capability-layer-skills-code-execution-prompts.md)
- [Capability patterns](../../../patterns/capability-patterns.md)

> [!NOTE]
> Product features, plan availability, administration, and implementation details can change. Verify current behavior in official Anthropic documentation and workspace settings.