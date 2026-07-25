# Module 2 Prompt Notebook: Strategy Checkpoint

Use these prompts to practice diagnosing the dominant weakness in a task specification and proposing one targeted repair. Use only fictional, public, synthetic, or authorized examples.

## 1. Dominant-weakness classifier

```text
Act as a prompt-diagnostics coach.

Prompt:
[PASTE PROMPT]

Classify the dominant weakness as one of:
- Role
- Context
- Task
- Constraints
- Output format
- Evidence boundary
- Task strategy
- Workflow design
- No material defect

Return:
1. dominant task type;
2. likely output symptom;
3. dominant weakness;
4. evidence from the prompt;
5. one targeted repair;
6. what should remain unchanged; and
7. any secondary weakness that should wait until the next iteration.

Do not rewrite the entire prompt unless the original is unusably underspecified.
```

## 2. Single-change repair drill

```text
Give me ten original weak prompts, one at a time.

For each prompt, require me to provide:
- the dominant weakness;
- one sentence explaining the likely failure;
- exactly one repair; and
- one element I would preserve.

Use a balanced mix of:
- ambiguous tasks;
- missing context;
- missing constraints;
- missing output formats;
- weak evidence boundaries;
- task-strategy mismatch; and
- over-specification.

After I answer, score the diagnosis from 0 to 2 and explain whether my repair was targeted or overly broad.
```

## 3. Under-specified or over-specified

```text
Generate twelve original prompts and ask me to classify each as:
- under-specified;
- appropriately calibrated;
- over-specified; or
- a system problem rather than a prompt problem.

Include:
- analysis;
- research;
- drafting;
- brainstorming;
- extraction;
- classification;
- calculation; and
- a task with unauthorized data.

After each answer, explain which dimensions determine validity and which dimensions benefit from latitude.
```

## 4. Component close-call coach

```text
Create eight close-call scenarios where two diagnoses appear plausible.

Use pairs such as:
- Context versus Constraints
- Task versus Output format
- Constraints versus Task strategy
- Evidence boundary versus Context
- Prompt defect versus Model selection
- Prompt defect versus Context degradation
- Prompt defect versus Code Execution
- Prompt defect versus Human review

For each scenario, ask me to choose the dominant diagnosis and justify why the alternative is secondary.
```

## 5. Brainstorming calibration repair

```text
Review the brainstorming prompt below.

Prompt:
[PASTE PROMPT]

Identify:
1. the goal;
2. hard guardrails that must remain;
3. constraints that should be deferred;
4. whether generation and evaluation are mixed;
5. a divergence-round prompt;
6. a separate convergence-round prompt; and
7. the criteria for deciding when to move from divergence to convergence.

Preserve necessary safety, legal, brand, and scope boundaries.
```

## 6. Prompt checkpoint generator

```text
Generate a four-question prompt-diagnosis checkpoint.

Requirements:
- one ambiguous task;
- one missing-scope case;
- one missing-context case;
- one over-constrained brainstorming case;
- no copied course or exam wording;
- one dominant weakness per question; and
- one best targeted repair.

Hide the answer key until I submit all four answers.

Score:
- 1 point for the dominant diagnosis;
- 1 point for a targeted repair; and
- 1 point for explaining why a plausible alternative is weaker.
```

## 7. Prompt audit table

```text
Audit the prompt below using this table:

| Dimension | Present? | Calibrated? | Evidence | Repair priority |
|---|---:|---:|---|---|
| Role | | | | |
| Context | | | | |
| Task | | | | |
| Constraints | | | | |
| Output format | | | | |
| Evidence boundary | | | | |
| Uncertainty behavior | | | | |
| Task-strategy fit | | | | |

Prompt:
[PASTE PROMPT]

Then identify only the highest-priority repair for the next iteration.
```

## 8. Repair-without-regression review

```text
Compare the original and revised prompts.

Original:
[PASTE ORIGINAL]

Revision:
[PASTE REVISION]

Determine:
- what defect the revision attempted to fix;
- whether the change addresses that defect;
- which working requirements were preserved;
- whether the revision introduced over-specification;
- whether useful latitude was lost;
- whether any new ambiguity was introduced; and
- the smallest next action.
```

## 9. Prompt diagnosis oral drill

```text
Conduct a ten-question oral drill on prompt diagnosis.

Ask one question at a time.

For every answer, require me to state:
1. task type;
2. predicted failure;
3. dominant weakness;
4. one repair;
5. what remains unchanged; and
6. whether the prompt needs more control or more latitude.

Do not provide the answer before I respond.
```

## 10. System-versus-prompt boundary

```text
For each failure below, classify the primary intervention as:
- Prompt repair
- Evidence or retrieval repair
- Model change
- Context reset
- Code Execution or deterministic method
- Tool or permission repair
- Governance or authorization repair
- Human review

Failures:
[PASTE FAILURES]

For each classification, explain why adding prompt detail would or would not solve the problem.
```

## 11. Minimum sufficient specification

```text
Given the task below, produce three versions:
1. under-specified;
2. minimum sufficient specification; and
3. over-specified.

Task:
[DESCRIBE TASK]

Annotate which details are essential for validity, which are optional, and which reduce useful latitude without adding value.
```

## 12. Distractor analysis

```text
Create five original multiple-choice questions about prompt diagnosis.

Each question must contain:
- one best targeted repair;
- one distractor that adds irrelevant detail;
- one distractor that changes the model or tool unnecessarily;
- one distractor that over-corrects and removes useful latitude.

After I answer, explain the scenario signal that controls the choice.
```

## Suggested study sequence

1. Run the under-specified or over-specified drill.
2. Complete the component close-call coach.
3. Run the four-question checkpoint.
4. Finish with the oral drill.

## Related material

- [Strategy Checkpoint](../../modules/02-prompting-task-execution/lessons/05b-strategy-checkpoint.md)
- [Strategy by Task Type](../../modules/02-prompting-task-execution/lessons/05a-strategy-by-task-type.md)
- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Prompt Calibration Pattern](../../patterns/prompt-calibration-pattern.md)
