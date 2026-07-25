# Module 2 Prompt Notebook: Repair the Prompt

These prompts are original study aids for diagnosing and repairing underperforming task specifications. Use fictional, public, synthetic, or explicitly authorized materials only.

## 1. Output-to-gap diagnostic

```text
You are helping me diagnose an underperforming AI task specification.

Inputs:
- Original prompt: [PROMPT]
- Output produced: [OUTPUT]
- Actual user goal: [GOAL]

Analyze the mismatch.

Return a table with:
1. Observed output deficiency
2. Required result dimension
3. Missing or mishandled component
4. Smallest targeted repair
5. Evidence that the repair addresses the failure
6. What should remain unchanged

Consider:
- role or operating frame;
- context;
- task;
- evidence boundary;
- constraints;
- process;
- tool requirements;
- output contract;
- uncertainty behavior;
- task strategy; and
- workflow decomposition.

Do not rewrite the complete prompt yet.
```

## 2. Component-gap matrix

```text
Inspect the task below and evaluate each component.

Task:
[TASK]

For each component, mark:
- Sufficient
- Missing
- Ambiguous
- Over-specified
- Not needed

Components:
- Role or operating frame
- Context
- Task
- Evidence
- Constraints
- Process
- Tools
- Output format
- Uncertainty behavior
- Success criteria

For every item not marked Sufficient or Not needed, propose one concise repair.
Do not add a component merely because it appears in the checklist.
```

## 3. Real-goal recovery

```text
The prompt and output below did not meet the author's need.

Prompt:
[PROMPT]

Output:
[OUTPUT]

Known downstream use:
[USE]

Infer only the task requirements that are directly supported by the known use.
Separate your response into:
1. Explicit requirements
2. Reasonable but unconfirmed assumptions
3. Questions that materially affect the specification
4. Likely success criteria

Do not invent organizational facts or silently replace the author's objective.
```

## 4. Distractor detector

```text
Below are candidate instructions for repairing a prompt.

Original failure:
[FAILURE]

Required result:
[RESULT]

Candidate instructions:
[LIST]

For each candidate, classify it as:
- Essential repair
- Useful enhancement
- Decorative or low-value
- Harmful over-specification
- Belongs in a different workflow stage

Explain which required result dimension each retained instruction protects.
```

## 5. Minimum sufficient specification builder

```text
Build the shortest task specification that reliably supports the stated goal.

Goal:
[GOAL]

Authorized evidence:
[EVIDENCE]

Downstream use:
[USE]

Risk level:
[LOW / MEDIUM / HIGH]

Required output:
[OUTPUT]

First identify the minimum necessary controls.
Then assemble the prompt using only components that carry functional weight.
After the prompt, list every included component and explain why it is necessary.
```

## 6. Quantitative feedback-analysis repair

```text
Repair the weak request below so that open-text feedback can be analyzed reproducibly.

Weak request:
[REQUEST]

Dataset description:
[DESCRIPTION]

Decision supported:
[DECISION]

The repaired task must define:
- unit of analysis;
- coding scheme development;
- multi-label behavior;
- denominator;
- ambiguity handling;
- deterministic counting and percentage calculation;
- representative quote selection;
- output structure;
- limitations; and
- human review.

Do not perform the analysis. Return the repaired task specification and a validation checklist.
```

## 7. Coding-scheme designer

```text
Using the supplied sample comments, propose an initial issue-coding scheme.

Requirements:
- categories must be distinct and decision-relevant;
- define each category;
- give inclusion and exclusion rules;
- provide one positive and one boundary example;
- identify likely overlaps;
- allow an Unknown or Other category where appropriate; and
- do not count final frequencies yet.

Return:
1. coding table;
2. overlap risks;
3. questions requiring human resolution; and
4. a recommendation on whether multi-label classification is appropriate.
```

## 8. Deterministic-tool routing plan

```text
Decompose the task below into work that should be performed by:
- language-model reasoning;
- deterministic code;
- retrieval or search;
- human review; or
- human decision.

Task:
[TASK]

Return a table with:
1. Stage
2. Input
3. Operation
4. Execution mode
5. Output
6. Validation
7. Failure behavior

Explain why prose generation should not be used for any exact arithmetic or record-counting operation.
```

## 9. Prompt assembly optimizer

```text
Below are prompt fragments in an arbitrary order.

Fragments:
[FRAGMENTS]

Arrange them into a coherent sequence:
1. operating frame, when useful;
2. context and decision use;
3. authorized evidence;
4. primary task;
5. process and constraints;
6. tools;
7. output contract;
8. uncertainty behavior; and
9. success criteria.

Remove redundant or decorative fragments.
Explain every removal and every material ordering decision.
```

## 10. Repaired-prompt evaluator

```text
Evaluate the repaired prompt below against the original failure and actual goal.

Original prompt:
[ORIGINAL]

Original output failure:
[FAILURE]

Actual goal:
[GOAL]

Repaired prompt:
[REPAIRED]

Score 0-2 for:
- task clarity;
- context sufficiency;
- evidence control;
- measurable constraints;
- tool fit;
- output contract;
- uncertainty handling;
- validation design;
- control-latitude calibration; and
- downstream usability.

Identify:
1. remaining material gaps;
2. unnecessary instructions;
3. likely regressions;
4. the single highest-value next repair; and
5. whether the prompt is ready to run.
```

## 11. One-change repair drill

```text
For each weak prompt below, identify only the dominant defect and one targeted repair.

A. Review these incident reports.
B. Summarize all major procurement risk.
C. Write a professional update for the project.
D. Brainstorm ideas, evaluate each against twelve criteria, and return only the winner.
E. Extract the required fields into the supplied JSON schema.

For each, provide:
- dominant task type;
- predicted output symptom;
- dominant defect;
- one repair;
- one element to preserve; and
- whether the prompt may already be sufficient given missing context.
```

## 12. Feedback-analysis acceptance test

```text
Create an acceptance-test checklist for an output that ranks themes from open-text feedback.

The checklist must test:
- source traceability;
- coding-rule consistency;
- count accuracy;
- denominator clarity;
- percentage calculation;
- quote fidelity;
- privacy handling;
- ranking logic;
- ambiguity handling;
- distinction between frequency and priority; and
- human approval.

Return deterministic checks separately from reviewer judgments.
```

## 13. Repair versus redesign decision

```text
Determine whether the failure below should be addressed by:
- prompt repair;
- task decomposition;
- context reconstruction;
- better evidence;
- a different model or capability;
- deterministic tooling;
- governance or authorization controls; or
- human escalation.

Failure description:
[FAILURE]

Return:
1. likely root cause;
2. supporting evidence;
3. correct intervention layer;
4. why prompt wording alone is or is not sufficient; and
5. the next validation step.
```

## 14. Oral certification drill

```text
Quiz me with ten short scenarios about prompt repair.

Cover:
- vague task verbs;
- missing context;
- missing constraints;
- weak output contracts;
- decorative role instructions;
- over-constrained brainstorming;
- exact counting without code;
- evidence versus representative quotes;
- prompt failure versus system failure; and
- minimum sufficient specification.

Ask one question at a time.
After my answer:
1. mark it correct, partially correct, or incorrect;
2. explain the dominant issue;
3. give the smallest effective repair; and
4. continue to the next scenario.
```

## 15. Reflection log

```text
Help me record a completed prompt-repair exercise.

Inputs:
- Weak prompt: [PROMPT]
- Output failure: [FAILURE]
- Real goal: [GOAL]
- Components repaired: [COMPONENTS]
- Distractor rejected: [DISTRACTOR]
- Final prompt: [FINAL]
- Result: [RESULT]

Create a concise study log with:
1. failure diagnosis;
2. component mapping;
3. final repair rationale;
4. tool-selection decision;
5. validation plan;
6. what I learned; and
7. one transfer example from another domain.
```

## Usage discipline

When practicing prompt repair:

- diagnose before rewriting;
- compare the output against the real decision need;
- add only components that protect a required result;
- preserve working elements;
- separate decorative instructions from functional controls;
- use code for exact arithmetic and counting;
- define the measurement rules before counting;
- validate both the prompt and the resulting output; and
- retain human judgment for consequential decisions.
