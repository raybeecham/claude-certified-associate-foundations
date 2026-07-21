# Module 2 Worked Build Prompts

Use these exercises to observe how each task-specification component changes output quality. Use fictional, public, synthetic, or explicitly authorized material.

## 1. Component audit

```text
Audit the prompt below against Role, Context, Task, Constraints, and Output Format.

For each component:
- state whether it is present, partial, or missing;
- quote the relevant wording;
- explain the likely output failure; and
- propose the smallest useful repair.

Prompt:
[PASTE PROMPT]
```

## 2. Incremental build

```text
Start with this vague request:
[PASTE REQUEST]

Build five versions by adding only one major component at a time:
1. Task
2. Context and audience
3. Role, only if useful
4. Constraints and evidence boundary
5. Output contract and missing-data behavior

After each version, explain:
- what ambiguity was removed;
- what failure became less likely;
- what remains unspecified; and
- whether the added text is necessary.
```

## 3. Minimal specification

```text
Rewrite this request using the minimum sufficient specification rather than the longest possible prompt.

Request:
[PASTE REQUEST]

Return:
1. Revised prompt
2. Components included
3. Components intentionally omitted
4. Why the prompt is sufficient for the task's consequence and complexity
```

## 4. Quantify relevance

```text
The prompt below uses vague relevance language such as important, material, notable, or significant.

Prompt:
[PASTE PROMPT]

Replace vague selection language with testable criteria. Do not invent business thresholds. Where a threshold requires stakeholder input, mark it as [DECISION NEEDED].
```

## 5. Output-contract design

```text
Design an output contract for this downstream use:
[DESCRIBE RECIPIENT OR SYSTEM]

Specify:
- format;
- required fields or sections;
- order;
- length;
- allowed values where relevant;
- missing-data behavior; and
- release-blocking defects.

Do not perform the underlying task yet.
```

## 6. Role necessity test

```text
Evaluate whether a role instruction is useful for this task:
[PASTE TASK]

Compare:
A. No role
B. A specific professional role
C. A decorative role such as "world-class expert"

Explain which version is best and why. Prefer no role when it does not materially change perspective, vocabulary, assumptions, depth, or method.
```

## 7. Prompt versus system diagnosis

```text
A workflow produced this failure:
[DESCRIBE FAILURE]

Classify the likely cause as one or more of:
- prompt specification;
- missing or poor evidence;
- model selection;
- context degradation;
- deterministic computation;
- tool access or permissions;
- evaluation;
- governance or decision authority.

Recommend the smallest responsible repair. Do not default to rewriting the prompt.
```

## 8. Before-and-after evaluator

```text
Compare these two prompts without executing them.

Prompt A:
[PASTE]

Prompt B:
[PASTE]

Score each from 1-5 for:
- audience fit;
- task clarity;
- evidence boundary;
- scope control;
- output usability;
- missing-data behavior; and
- evaluability.

Explain exactly which wording causes each difference.
```

## 9. Thirty-second preflight

```text
Run a concise preflight on this prompt:
[PASTE PROMPT]

Check:
- Role: useful or unnecessary?
- Context: what cannot be inferred safely?
- Task: one clear primary action?
- Constraints: measurable and relevant?
- Output: exact usable shape?
- Evidence: authorized source boundary?
- Failure: defined missing-data behavior?

Return only blocking gaps and the smallest fixes.
```

## 10. Teach-back

```text
Ask me five scenario questions, one at a time, about building a prompt from weak to strong. Focus on diagnosing the missing component rather than memorizing definitions. After each answer, explain the strongest reasoning and why plausible alternatives are weaker.
```
