# Module 2 — Component Stack Prompts

Use fictional, synthetic, public, or explicitly authorized information.

## 1. Component audit

```text
Review the prompt below against these five components:
1. Role
2. Context
3. Task
4. Constraints
5. Output format

For each component, state:
- whether it is present;
- whether it is sufficient;
- the likely failure caused by any gap; and
- the smallest useful revision.

Prompt:
[PASTE PROMPT]
```

## 2. Minimum sufficient prompt

```text
Convert the request below into the shortest prompt that removes material ambiguity.
Do not add a role unless a professional perspective changes the task.

Request:
[DESCRIBE REQUEST]

Return:
- revised prompt;
- components used;
- components intentionally omitted;
- why the result is sufficient.
```

## 3. Context-gap finder

```text
Identify information that exists in the requester's head or environment but is not available to the model.
Group gaps by audience, situation, prior decisions, definitions, source material, scope, assumptions, and exclusions.
Do not invent missing facts.

Request:
[PASTE REQUEST]
```

## 4. Verb precision

```text
Analyze the primary task verb in this prompt.
Explain whether the requested action is summarize, compare, extract, classify, draft, evaluate, rank, recommend, or something else.
Rewrite the task sentence using one unambiguous primary verb.

Prompt:
[PASTE PROMPT]
```

## 5. Constraint repair

```text
The output from this prompt was unusable because it was [too long / too broad / wrong tone / included prohibited content / omitted required content].
Identify the missing or weak constraint and repair only that component.

Prompt:
[PASTE PROMPT]
```

## 6. Output-contract designer

```text
Design an output contract for the task below based on the downstream consumer.
Specify structure, fields or sections, length, ordering, and missing-data behavior.

Task:
[DESCRIBE TASK]
Downstream consumer:
[PERSON OR SYSTEM]
```

## 7. Engineering extension

```text
Expand this five-component prompt only where necessary by adding:
- evidence boundary;
- process;
- uncertainty behavior;
- success criteria; and
- review requirements.

Explain why each added element is necessary.

Prompt:
[PASTE PROMPT]
```

## 8. Compare three versions

```text
Create three versions of this request:
1. vague baseline;
2. official five-component version;
3. engineering version with evidence, uncertainty, and success criteria.

Compare expected specificity, grounding, editing burden, and validation difficulty.

Request:
[DESCRIBE REQUEST]
```
