# Module 2 Lesson 1 Prompt Notebook

These prompts reinforce the lesson that prompting is structured task specification rather than clever phrasing.

## 1. Convert a vague request into a task specification

```text
I will provide a vague request.

Rewrite it as a clear task specification containing:
1. objective;
2. audience;
3. authorized inputs or evidence;
4. relevant constraints;
5. required process, if needed;
6. output contract;
7. missing-data or uncertainty behavior; and
8. success criteria.

Use only details I provide. Mark any necessary missing information as [NEEDS INPUT] rather than inventing it.

Vague request:
[PASTE REQUEST]
```

## 2. Diagnose the missing prompt component

```text
Review the prompt and the resulting output.

Identify the single most important failed or missing component. Choose from:
- objective;
- audience;
- context;
- evidence boundary;
- constraints;
- process;
- output contract;
- uncertainty behavior;
- success criteria; or
- a non-prompt system layer.

Return:
1. diagnosis;
2. evidence from the prompt or output;
3. the smallest targeted repair;
4. a revised prompt fragment; and
5. why rewriting the entire prompt would be unnecessary.

Prompt:
[PASTE PROMPT]

Output:
[PASTE OUTPUT]
```

## 3. Separate prompt failures from system failures

```text
Classify each observed problem by its most likely primary layer:
- prompt or task specification;
- evidence or retrieval;
- model selection;
- context management;
- deterministic computation;
- evaluation and validation;
- governance or human approval; or
- workflow design.

For each problem, provide:
- primary layer;
- reasoning;
- recommended intervention; and
- what not to try first.

Problems:
[PASTE PROBLEMS]
```

## 4. Minimum sufficient clarity editor

```text
Edit the prompt for minimum sufficient clarity.

Preserve every requirement that materially affects execution, safety, or evaluation. Remove repetition, decorative role-play, irrelevant background, and constraints that do not support the objective.

Return:
1. revised prompt;
2. removed material and why it was unnecessary;
3. retained requirements and why each matters; and
4. unresolved ambiguity that still requires user input.

Prompt:
[PASTE PROMPT]
```

## 5. Task-type strategy classifier

```text
Analyze the proposed task and identify its primary task type and any secondary task types.

Possible types include:
- analysis;
- research;
- drafting;
- brainstorming;
- extraction;
- classification;
- planning;
- transformation;
- coding; and
- evaluation.

Return:
1. primary task type;
2. secondary task types;
3. prompting strategy required;
4. evidence requirements;
5. output contract recommendation;
6. major failure risks; and
7. whether decomposition is needed.

Task:
[DESCRIBE TASK]
```

## 6. Diagnostic revision request

```text
Convert the vague revision request into a diagnostic revision instruction.

A strong revision instruction should:
- identify what already works;
- name the failed quality dimension;
- specify the required change;
- preserve unaffected content;
- define acceptance criteria; and
- avoid adding unsupported information.

Original output:
[PASTE OUTPUT]

Vague revision request:
[EXAMPLE: Make this better]
```

## 7. Prompt teach-back evaluator

```text
Evaluate my explanation of this principle:

"A prompt is a task specification, not a magic phrase."

Score the explanation from 0 to 2 on each dimension:
- distinction between intent and instructions;
- explanation of ambiguity reduction;
- understanding of prompt components;
- distinction between prompt and system failures;
- explanation of diagnostic iteration; and
- use of a practical example.

Return the score, evidence, misconceptions, and one targeted remediation exercise.

My explanation:
[PASTE EXPLANATION]
```

## 8. Before-and-after prompt comparison

```text
Compare two prompts intended to accomplish the same task.

For each prompt, assess:
- objective clarity;
- audience clarity;
- evidence boundaries;
- constraints;
- required process;
- output contract;
- uncertainty behavior;
- evaluability; and
- unnecessary complexity.

Then explain which prompt is stronger, where the weaker prompt delegates important decisions to the model, and how to improve it without making it needlessly long.

Prompt A:
[PASTE]

Prompt B:
[PASTE]
```

## Usage note

These prompts are learning aids. Do not treat the resulting diagnosis as proof that the prompt is the only failing layer. Verify evidence quality, model suitability, context state, deterministic operations, authorization, and human-review requirements separately.