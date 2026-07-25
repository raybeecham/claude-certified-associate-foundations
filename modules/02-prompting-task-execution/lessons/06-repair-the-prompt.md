# Lesson 6: Repair the Underperforming Prompt

## Overview

This exercise combines the major skills from Module 2:

- diagnose an underperforming prompt from its output;
- recover the author's actual objective;
- identify specification gaps;
- map each repair to a prompt component;
- reject instructions that sound useful but close no important gap;
- assemble the repaired components into a coherent task specification; and
- use deterministic tools when the requested result depends on reliable counting or calculation.

> A repaired prompt is not merely longer. Every added instruction should correct a known failure or protect a required result.

## Course exercise result

The learner completed the preparation-course exercise with:

```text
All stages correct
```

The completed exercise demonstrated correct identification of all five targeted component gaps, correct mapping of the repair fragments, rejection of the nonessential tone distractor, and correct assembly of the final prompt.

The proprietary exercise wording is not reproduced here. The scenario and prompts below are original study material that test the same skills.

## The complete repair workflow

```text
Weak prompt
    ↓
Observe the disappointing output
    ↓
Recover the real decision need
    ↓
Diagnose specification gaps
    ↓
Map each repair to a component
    ↓
Reject decorative instructions
    ↓
Assemble the minimum sufficient specification
    ↓
Run with the correct tools
    ↓
Validate the result
```

This is more disciplined than simply asking Claude to `try again`.

## Original exercise scenario

### Weak prompt

```text
Review the service feedback and recommend what we should improve.
```

### Disappointing output

The response returns broad observations such as:

- users want quicker help;
- documentation could be clearer;
- some customers mention account setup; and
- the team should consider improving support.

The response is plausible but not decision-ready. It does not show how often each issue occurred, cite the actual evidence, establish priorities, or explain how the findings were counted.

### Actual goal

A customer-experience lead has 180 written support comments. She needs the four most frequently raised issues, each supported by a representative quotation and an approximate share of the responses, so she can select priorities for the next service-improvement sprint.

## Stage 1: Diagnose the gaps

The weak prompt under-specifies five useful components.

| Component | What is missing | Consequence |
|---|---|---|
| Role or operating frame | No evidence-oriented analytical perspective | The response may default to a generic summary instead of a structured issue analysis |
| Context | No dataset size, source type, audience, or decision purpose | Claude cannot calibrate the analysis to the evidence or the intended decision |
| Task | `Review` and `recommend` do not define the analytical operation | The response may summarize instead of count, rank, and prioritize |
| Constraints and process | No quote, frequency, counting, ambiguity, or tool requirements | The findings may be vague, estimated, unsupported, or inconsistent |
| Output format | No required decision-ready structure | The result may be difficult to compare or act on |

### Engineering note on role

A role is not mandatory in every prompt. It belongs only when the perspective changes how the task should be performed.

In this scenario, an analytical operating frame is useful because it emphasizes:

- evidence coding;
- frequency calculation;
- traceability to source comments;
- separation of findings from recommendations; and
- decision-oriented communication.

A decorative role such as `world-class genius` would add no comparable value.

## Stage 2: Map each repair to its component

### Role or operating frame

```text
Act as a customer-insights analyst.
```

This establishes an evidence-oriented perspective without claiming authority the model does not possess.

### Context

```text
The attached dataset contains 180 written support comments collected during the last service cycle. The customer-experience lead will use the result to select priorities for the next improvement sprint.
```

This supplies the evidence set, its size, the audience, and the downstream decision.

### Task

```text
Identify and rank the four most frequently raised service issues.
```

This replaces vague verbs with a specific analytical operation.

### Constraints and process

```text
For each issue:
- report the number and approximate percentage of comments that mention it;
- include one representative quotation;
- explain the practical effect on the customer;
- distinguish direct evidence from interpretation; and
- use code execution to calculate frequencies rather than estimating them.
```

These requirements make the result traceable, actionable, and quantitatively defensible.

### Output format

```text
Return a ranked table with columns for Rank, Issue, Comment Count, Approximate Share, Representative Quote, Customer Effect, and Recommended Next Step.
```

This converts the analysis into a comparable decision artifact.

## The distractor test

A possible extra fragment is:

```text
Make the report polished and professional.
```

This is not necessarily harmful, but it does not repair the dominant failure.

The original output failed because it lacked:

- evidence grounding;
- frequency counts;
- ranking;
- traceability;
- decision context; and
- an actionable structure.

`Polished and professional` does not close any of those gaps.

> A prompt instruction earns its place when it changes a result dimension that matters to success.

## Stage 3: Assemble the repaired prompt

A clean order is:

```text
Operating frame
      ↓
Context and decision use
      ↓
Task
      ↓
Evidence, process, and constraints
      ↓
Output contract
      ↓
Validation behavior
```

### Repaired prompt

```text
Act as a customer-insights analyst.

The attached dataset contains 180 written support comments collected during the last service cycle. The customer-experience lead will use the result to select priorities for the next improvement sprint.

Identify and rank the four most frequently raised service issues.

Analysis requirements:
- develop a concise coding scheme for the issues before counting;
- report the number and approximate percentage of comments that mention each issue;
- include one representative quotation for each issue;
- explain the practical effect on the customer;
- distinguish direct evidence from interpretation;
- use code execution to calculate frequencies rather than estimating them;
- do not invent missing details; and
- flag comments that are ambiguous or cannot be classified confidently.

Return a ranked table with columns for Rank, Issue, Comment Count, Approximate Share, Representative Quote, Customer Effect, and Recommended Next Step.

After the table, include:
1. the coding rules used;
2. any limitations that could affect the ranking; and
3. a short validation note confirming that the counts were calculated from the supplied dataset.
```

## Why each line carries weight

| Prompt element | Failure it repairs | Result it protects |
|---|---|---|
| Customer-insights analyst frame | Generic summarization | Evidence-oriented analysis |
| Dataset size and decision use | Missing context | Correct scale and relevance |
| Identify and rank four issues | Vague task | Specific analytical outcome |
| Coding scheme | Inconsistent categorization | Repeatable counting |
| Count and percentage | Unsupported prioritization | Quantitative ranking |
| Representative quotation | Weak traceability | Source-grounded findings |
| Customer effect | Themes without meaning | Decision relevance |
| Code execution | Estimated arithmetic | Deterministic calculation |
| Missing-data rules | Invented certainty | Honest uncertainty |
| Ranked table | Unstructured result | Fast comparison and action |
| Method and limitation notes | Hidden assumptions | Auditability |

## A deeper issue: counting requires a measurement design

Requesting code execution is not sufficient by itself. Code can count reliably only after the categories and counting rules are defined.

```text
Raw comments
    ↓
Coding scheme
    ↓
Classification rules
    ↓
Machine-assisted or human-reviewed labels
    ↓
Deterministic counts
    ↓
Ranked findings
```

Before counting, define:

### Unit of analysis

What is being counted?

- one survey response;
- one sentence;
- one distinct complaint;
- one mention; or
- one respondent who raised the issue at least once.

For most survey-priority decisions, the most interpretable unit is:

> Number of responses that mention an issue at least once.

### Multi-label behavior

One response may mention more than one issue. Decide whether:

- each response may receive multiple issue labels; or
- each response must be assigned one primary issue.

A multi-label approach is usually more faithful for open-text feedback, but percentages may then total more than 100%.

### Denominator

Clarify whether the percentage uses:

- all 180 responses;
- only nonblank responses;
- only comments judged relevant; or
- total issue mentions.

The denominator must be reported so the percentage is interpretable.

### Category design

Categories should be:

- distinct enough to compare;
- broad enough to capture meaningful patterns;
- defined with inclusion and exclusion rules;
- reviewed for overlap; and
- stable before the final count.

### Tie handling

Define what happens when two issues have the same count:

- report a tie;
- use severity as a secondary criterion;
- use recency as a secondary criterion; or
- ask a human reviewer to decide.

### Quote selection

A representative quote should:

- support the issue accurately;
- be typical rather than sensational;
- avoid personally identifiable information;
- preserve the respondent's meaning; and
- not imply that one quotation proves frequency.

## Tool selection is part of the specification

The task contains both generative and deterministic work.

| Work | Best execution mode |
|---|---|
| Propose an initial issue taxonomy | Language-model reasoning with human review |
| Apply issue labels | Model-assisted classification, rules, code, or a hybrid workflow |
| Count labels | Code execution |
| Calculate percentages | Code execution |
| Select quotations | Evidence-grounded retrieval with human review |
| Explain customer impact | Model synthesis grounded in the comments |
| Choose sprint priorities | Human decision informed by the analysis |

The model should not be asked to perform exact counting through prose when a deterministic tool is available.

## Validation plan

A decision-ready result should pass four checks.

### 1. Arithmetic validation

- counts match the classified records;
- percentages use the stated denominator;
- ranking follows the counts;
- ties are handled consistently; and
- rounding is documented.

### 2. Evidence validation

- every quotation exists in the supplied data;
- every quote supports the assigned issue;
- no quote contains unnecessary sensitive information; and
- findings do not rely on unsupported assumptions.

### 3. Classification validation

- category definitions are clear;
- overlapping categories are reviewed;
- ambiguous comments are flagged;
- a sample of labels is manually checked; and
- material disagreements are resolved before final ranking.

### 4. Decision validation

- the ranked issues answer the product or service decision;
- recommendations are tied to evidence;
- frequency is not treated as the only possible priority criterion; and
- a qualified human retains the final prioritization decision.

## Frequency is not the same as priority

The exercise asks for ranking by frequency because that is the author's stated need. In a production workflow, frequency may be only one decision dimension.

A broader prioritization model might consider:

```text
Priority = Frequency + Severity + Strategic Impact + Effort + Risk
```

This is conceptual, not a universal formula. The weights should be defined by the organization.

Do not silently replace the requested frequency ranking with a broader scoring model. Instead:

1. deliver the requested frequency analysis;
2. state its limitations; and
3. propose a separate prioritization stage when appropriate.

## The repair matrix

Use this worksheet when a prompt underperforms.

| Observed failure | Intended result | Missing or mishandled component | Targeted repair | Validation |
|---|---|---|---|---|
| | | Role / Context / Task / Constraints / Output / Evidence / Tool / Strategy | | |

### Repair questions

1. What did the output do?
2. What did the author actually need?
3. Which required result dimension was absent?
4. Which component should have specified it?
5. What is the smallest instruction that closes the gap?
6. Does the task require decomposition or a tool?
7. What instruction sounds useful but changes nothing important?
8. How will the repaired output be checked?

## Common repair failures

### Adding every possible component

Longer is not automatically better. Add only what supports correctness, usability, safety, or evaluation.

### Treating role as mandatory

Use a role when it changes the operating perspective. Do not add one mechanically.

### Adding tone before fixing substance

A polished generic answer is still generic.

### Asking for exact numbers without a deterministic method

Use code for counts, percentages, sorting, deduplication, and other exact operations.

### Counting before categories are stable

A precise count of an unstable taxonomy is still unreliable.

### Treating representative quotes as proof of prevalence

Quotes illustrate a finding. Counts establish prevalence.

### Treating the model's confidence as validation

Validate against source records, deterministic calculations, explicit criteria, and human review.

### Replacing the author's goal

Repair the prompt to serve the stated decision. Do not silently redesign the objective.

## Knowledge check

### Question 1

A feedback-summary prompt produces reasonable themes but no evidence or priority. Which repairs are most important?

- A. Add a more impressive role and a warmer tone.
- B. Define the dataset, ranking task, evidence requirements, deterministic counting method, and output structure.
- C. Increase the response length.
- D. Ask for more creativity.

**Answer:** B. The failure is missing task, context, evidence, process, and output specification.

### Question 2

Why might code execution still produce misleading counts?

**Answer:** The coding scheme, unit of analysis, denominator, and multi-label rules may be undefined or inconsistent.

### Question 3

What is the function of a representative quotation?

**Answer:** It provides traceability and illustrates the issue; it does not establish how frequent the issue is.

### Question 4

Why is `make it professional` a weak repair for a generic feedback analysis?

**Answer:** It changes presentation but does not add evidence, frequency, prioritization, or decision structure.

### Question 5

Must every repaired prompt contain a role?

**Answer:** No. Add a role only when a defined perspective materially improves task execution.

### Question 6

Who should make the final product-priority decision?

**Answer:** A qualified human decision-maker using the analysis as evidence.

## Flashcards

### Flashcard 1

**Q:** What are the three stages of prompt repair?

**A:** Diagnose the gaps, map each repair to a component, and assemble the minimum sufficient specification.

### Flashcard 2

**Q:** What distinguishes a useful prompt instruction from a distractor?

**A:** A useful instruction protects a result dimension required for success; a distractor does not close a material gap.

### Flashcard 3

**Q:** Why use code execution for frequency analysis?

**A:** To perform counting, percentage calculation, and sorting deterministically instead of estimating through prose.

### Flashcard 4

**Q:** What must be defined before exact counting begins?

**A:** The coding scheme, unit of analysis, denominator, multi-label rules, and treatment of ambiguity.

### Flashcard 5

**Q:** What does a quote provide that a count does not?

**A:** Qualitative evidence and an example of how the issue appears in the source data.

### Flashcard 6

**Q:** Is the longest repaired prompt usually the best?

**A:** No. The target is the minimum sufficient specification.

## Applied repair drill

For each weak request:

1. predict the likely disappointing output;
2. identify the author's probable decision need;
3. diagnose the component gaps;
4. add only the repairs that matter;
5. identify one plausible distractor instruction;
6. specify any required deterministic tool; and
7. define the output validation method.

### A

```text
Look at these incident reports and tell me what is happening.
```

### B

```text
Summarize these invoices and identify any problems.
```

### C

```text
Review the employee comments and recommend improvements.
```

### D

```text
Compare these implementation options and pick one.
```

## Certification lens

For exam-style prompt-repair questions:

1. compare the observed output with the actual goal;
2. identify the missing result dimensions;
3. map each missing dimension to the component that should control it;
4. reject instructions that do not address the failure;
5. select the least complex repair that makes the task testable;
6. route deterministic work to tools; and
7. retain human judgment for consequential decisions.

## Think like an AI systems engineer

The repaired prompt is one layer of the system.

```text
Decision need
    ↓
Authorized evidence
    ↓
Measurement design
    ↓
Task specification
    ↓
Model and tool execution
    ↓
Validation
    ↓
Human decision
```

> Complete specification means every component carries weight that the output depends on—not that every possible instruction is included.

## Related material

- [Component Stack](02a-component-stack.md)
- [Worked Build](02b-worked-build.md)
- [Iterating to Improve Output](04-iterating-to-improve-output.md)
- [Strategy Checkpoint](05b-strategy-checkpoint.md)
- [Repair-the-Prompt notebook](../../../prompts/module-02/06-repair-the-prompt-prompts.md)
- [Task Specification Before Prompting](../../../patterns/task-specification-before-prompting.md)
- [Failure Localization Pattern](../../../patterns/failure-localization-pattern.md)
- [Prompt Calibration Pattern](../../../patterns/prompt-calibration-pattern.md)
