# Module 2: Iterating to Improve Output — Prompt Notebook

Use these prompts to practice diagnosis, targeted revision, regression checks, and stopping decisions.

## 1. Diagnose before rewriting

```text
Review the prompt and output below.

Prompt:
[PASTE PROMPT]

Output:
[PASTE OUTPUT]

Do not rewrite the prompt yet. First provide:
1. the specific output symptoms;
2. the most likely root cause for each symptom;
3. the prompt or system component responsible;
4. evidence from the output supporting the diagnosis; and
5. the smallest change you would test first.
```

## 2. Apply the one-change rule

```text
Given this prompt, output, and diagnosis, revise exactly one significant component.

Prompt:
[PASTE PROMPT]

Output:
[PASTE OUTPUT]

Diagnosis:
[PASTE DIAGNOSIS]

Return:
- component changed;
- revised language only;
- content that must remain unchanged;
- expected improvement;
- acceptance test for the next output.
```

## 3. Preserve working content

```text
The draft below is mostly correct. Identify the working sections and the defective section.

Draft:
[PASTE DRAFT]

Requirements:
[PASTE REQUIREMENTS]

Write a narrow revision instruction that:
- preserves all validated content;
- changes only the defective section;
- states the required improvement; and
- includes a regression check.
```

## 4. Build an iteration log

```text
Create an iteration log for the following prompt-development history.

[PASTE ROUNDS]

Use these columns:
Prompt version | Observed symptom | Suspected cause | Component changed | Evaluation result | Regression found | Next decision

Then explain which revisions produced evidence and which changed too many variables to interpret confidently.
```

## 5. Prompt failure or system failure?

```text
Classify each failure below as primarily:
- prompt specification;
- missing or weak evidence;
- model selection;
- context management;
- deterministic computation;
- tool or permission design;
- evaluation failure;
- governance or human authority.

Cases:
[PASTE CASES]

For each case, recommend the smallest responsible intervention and explain why prompt rewriting alone would or would not help.
```

## 6. Regression comparison

```text
Compare Output A and Output B against the rubric.

Rubric:
[PASTE RUBRIC]

Output A:
[PASTE OUTPUT A]

Output B:
[PASTE OUTPUT B]

Return a table showing pass, partial, or fail for every criterion. Identify:
- dimensions improved;
- dimensions unchanged;
- regressions;
- whether the revision should be accepted; and
- the next smallest change, if any.
```

## 7. Convergence and stopping

```text
Review the following iteration history and determine whether further prompting is justified.

[PASTE HISTORY]

Assess:
- remaining substantive defects;
- marginal gain from the last two rounds;
- likely value of another round;
- cost in time, tokens, and review;
- whether manual editing is now cheaper; and
- whether a human judgment boundary has been reached.

Conclude with Continue, Accept, Manual Edit, Escalate, or Stop.
```

## 8. Repair the delayed-deliverable email

```text
Run a controlled three-round improvement cycle on this prompt:

"Write a follow-up email to the client about the delayed deliverable."

Round 1: diagnose the missing components.
Round 2: add only the essential context and constraints.
Round 3: preserve the body and repair one remaining defect.

For every round, show:
- prompt change;
- expected output change;
- evaluation criteria; and
- stop or continue decision.
```

## 9. Diagnose an unsupported analysis

```text
A draft analysis is polished but contains unsupported claims, no citations, and confident conclusions despite missing data.

Design a targeted repair plan that separates:
- evidence problems;
- uncertainty behavior;
- output-contract problems;
- validation requirements; and
- human-review requirements.

Do not solve everything through prompt wording. State which controls belong elsewhere in the workflow.
```

## 10. Teach-back

```text
Teach the diagnostic iteration method to a colleague using:
- one sentence defining the method;
- the Observe → Diagnose → Modify → Validate → Decide loop;
- the one-change rule;
- one example of preserving working content;
- one example where the system, not the prompt, must change; and
- one stopping rule.

Keep the explanation under 300 words.
```

## Practice discipline

For each exercise, record what you changed and why. A better output is useful; a reproducible explanation of why it improved is more valuable.