# Module 1 Prompt Notebook: Quiz and Remediation

These prompts support scenario-question generation, self-grading, distractor analysis, mistake diagnosis, and focused remediation for Claude Platform & Model Foundations.

Use only fictional, synthetic, public, or authorized information. Do not use remembered or reconstructed live-exam questions.

## 1. Five-minute scenario quiz generator

### Use when

You want a fresh certification-style drill across Module 1.

```text
Create a five-question scenario quiz covering:
- entry-point selection;
- Project instructions versus Project knowledge;
- Skills and Code Execution;
- Haiku, Sonnet, and Opus selection;
- Context Management and Memory boundaries.

Requirements:
- use original scenarios;
- include four plausible options per question;
- make one option clearly best under the stated facts;
- avoid trivia and volatile product details;
- do not reveal answers until I submit all five;
- target completion in five minutes.

After I answer, grade each question and explain:
1. the controlling signal;
2. why the correct answer is strongest;
3. why each distractor is weaker; and
4. which lesson I should review for every miss.
```

## 2. Integrated configuration classifier

### Use when

A scenario requires entry-point, capability, model, context, and control decisions together.

```text
Analyze the scenario below.

Scenario:
[PASTE SCENARIO]

Recommend:
1. entry point: Chat, Project, Artifact, Research, or combination;
2. capability layers: Project instructions, Project knowledge, Skill, Code Execution, Memory, or none;
3. model tier: Haiku, Sonnet, or Opus;
4. context strategy: continue, checkpoint, summarize, restart, persist, or combination;
5. authoritative sources required;
6. validation and human review;
7. least-complex acceptable configuration; and
8. conditions that would change the answer.

Separate scenario facts from assumptions. Do not add capabilities without a requirement.
```

## 3. Self-grading rubric

### Use when

You have answered a scenario and want to evaluate the quality of your reasoning.

```text
Grade my answer using a 10-point rubric.

Scenario:
[SCENARIO]

My answer:
[ANSWER]

Score 0 to 2 for each:
- correct configuration;
- identification of the controlling scenario signal;
- explanation of the benefit;
- explanation of the cost or trade-off;
- explanation of why alternatives are weaker.

Then return:
- total score;
- strongest part;
- missing reasoning;
- corrected answer in one sentence;
- one follow-up question that tests the same concept differently.
```

## 4. Distractor audit

### Use when

You want to learn why plausible wrong answers are wrong.

```text
Audit the multiple-choice question below.

Question:
[QUESTION]

Options:
[OPTIONS]

For each option, identify:
- why a learner might select it;
- which true concept it partially invokes;
- why it is still weaker than the best answer;
- what additional scenario fact would make it correct; and
- the misconception it diagnoses.

Finish by naming the single controlling signal in the original scenario.
```

## 5. Mistake classifier

### Use when

You missed one or more questions and need to find the underlying reasoning error.

```text
Analyze my quiz mistakes.

Missed questions, my answers, and correct answers:
[PASTE RESULTS]

Classify each miss as one or more of:
- ignored recurrence;
- confused instructions with knowledge;
- missed a Code Execution trigger;
- over-selected the strongest model;
- under-selected model capability;
- confused current information with uploaded evidence;
- confused Artifact with persistence;
- confused Memory with authoritative state;
- missed context degradation;
- confused context limit with usage limit;
- omitted human review; or
- added unnecessary capability complexity.

Return:
1. error-pattern table;
2. root cause;
3. lesson to review;
4. corrective rule;
5. two original practice scenarios; and
6. retest criteria.
```

## 6. Model trade-off justification coach

### Use when

You need to write a one-sentence Haiku, Sonnet, or Opus justification.

```text
Review my model-selection sentence.

Scenario:
[SCENARIO]

Sentence:
[SENTENCE]

A strong sentence must identify:
- the model tier;
- the task signal controlling the choice;
- what the tier buys;
- what it costs; and
- why the trade-off is acceptable.

Return:
1. score from 0 to 10;
2. missing elements;
3. a tighter revision of no more than 45 words; and
4. the condition under which another tier would become preferable.
```

## 7. Code Execution trigger detector

### Use when

A scenario may hide a requirement for deterministic calculation or transformation.

```text
Review the scenario below and identify every operation that should use Code Execution.

Scenario:
[SCENARIO]

For each operation, state:
- input data;
- formula or transformation;
- assumptions and units;
- missing-value behavior;
- reconciliation or known-case test;
- output artifact; and
- human validation required.

Also identify any task that should remain language analysis rather than code.
```

## 8. Context-recovery drill

### Use when

You want practice deciding whether to continue, summarize, restart, or persist.

```text
Create five short scenarios involving context health.

Include:
- one healthy conversation that should continue;
- one conversation needing a checkpoint only;
- one requiring summarize and restart;
- one where durable information should be persisted to a Project;
- one where a stale Memory entry should be corrected or deleted.

Ask me to choose the action and explain why. After I answer, provide rationales and identify any incorrect assumptions.
```

## 9. Weak-area remediation plan

### Use when

Your score is below the readiness target.

```text
Build a focused remediation plan from these Module 1 results.

Results:
[PASTE SCORES AND MISSES]

Create a plan containing:
- weak objectives ranked by severity;
- exact lesson sections to review;
- flashcards to drill;
- three original questions per weak objective;
- one hands-on exercise;
- retest timing;
- passing threshold; and
- evidence that the weakness is resolved.

Prioritize judgment errors over memorization errors.
```

## 10. Question-quality reviewer

### Use when

You are writing new repository questions and want to prevent ambiguity or accidental copying.

```text
Review this proposed study question.

Question:
[QUESTION]

Evaluate:
- originality;
- alignment to a Module 1 objective;
- whether one answer is clearly best;
- quality and plausibility of distractors;
- reliance on volatile product facts;
- hidden assumptions;
- professional realism;
- safety and privacy;
- explanation quality; and
- whether the wording resembles proprietary assessment content too closely.

Return:
1. approve, revise, or reject;
2. identified problems;
3. revised original question;
4. answer and rationale; and
5. objective tag.
```

## Suggested study loop

1. Run prompt 1 under a five-minute timer.
2. Use prompt 3 to score the reasoning, not only the letter.
3. Use prompt 4 for every distractor you found tempting.
4. Use prompt 5 to identify recurring error patterns.
5. Use prompt 9 to remediate any objective below 80 percent.
6. Retake with new scenarios rather than memorizing wording.

## Related material

- [Module 1 quiz review](../../modules/01-platform-model-foundations/lessons/08-module-1-quiz.md)
- [Platform Selection Exercise](../../modules/01-platform-model-foundations/lessons/07-platform-selection-exercise.md)
- [Context Management prompts](06-context-management-prompts.md)
- [Choosing Models prompts](05-choosing-models-prompts.md)
- [Capability Layer checkpoint prompts](04c-capability-layer-checkpoint-prompts.md)
