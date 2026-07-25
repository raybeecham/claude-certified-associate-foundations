# Module 2 Prompt Notebook: Strategy by Task Type

Use these prompts to practice matching the prompt's control-latitude balance to analysis, research, drafting, and brainstorming tasks.

Use fictional, synthetic, public, or explicitly authorized information.

## 1. Task-type classifier

### Use when

You need to identify the dominant strategy before writing the prompt.

```text
Classify the request below as one or more of:
- analysis;
- research;
- drafting;
- brainstorming;
- extraction;
- classification;
- planning; or
- another task type.

Request:
[REQUEST]

Return:
1. dominant task type;
2. secondary task types;
3. evidence required;
4. what should be tightly controlled;
5. what should remain flexible;
6. whether the request should be decomposed; and
7. the reason for each conclusion.
```

## 2. Control-latitude planner

### Use when

You know the task type but need to decide what to tighten or loosen.

```text
Task type:
[TASK TYPE]

Task:
[TASK]

Create a control-latitude plan.

Use a table with these columns:
- Prompt element;
- Tight / Moderate / Loose;
- Why;
- Failure if too tight;
- Failure if too loose; and
- Recommended wording.

Evaluate:
- objective;
- role;
- context;
- evidence;
- process;
- constraints;
- output contract;
- uncertainty behavior; and
- success criteria.
```

## 3. Analysis prompt architect

### Use when

The task requires comparison, evaluation, prioritization, or judgment.

```text
Design an analysis prompt for the task below.

Task:
[TASK]

Evidence available:
[EVIDENCE]

Define:
1. the analytical question;
2. criteria and definitions;
3. standard, baseline, or comparison point;
4. authorized evidence;
5. scope and exclusions;
6. missing and conflicting evidence behavior;
7. required rationale;
8. output structure; and
9. validation checks.

Do not allow unsupported assumptions.
If the task includes consequential calculations, separate them for Code Execution or another deterministic method.
```

## 4. Research strategy builder

### Use when

The answer requires current or external evidence.

```text
Create a research strategy for:
[RESEARCH QUESTION]

Define:
- exact question;
- date or currency boundary;
- geographic, sector, or organizational scope;
- primary-source preferences;
- acceptable secondary sources;
- excluded source types;
- search versus deep Research recommendation;
- citation requirements;
- event-date versus publication-date handling;
- conflict-resolution behavior;
- unverified-claim behavior; and
- final output structure.

Explain why the proposed retrieval depth matches the task.
```

## 5. Source-backed research prompt

### Use when

You want a ready-to-use research prompt with verification discipline.

```text
Research the following question:
[QUESTION]

Scope:
[SCOPE]

Time boundary:
[DATE RANGE]

Source hierarchy:
1. [PRIMARY SOURCE TYPE]
2. [SECONDARY SOURCE TYPE]
3. [OTHER ACCEPTABLE SOURCE]

Requirements:
- cite every material factual claim;
- distinguish publication date from event date;
- separate source-supported fact from inference;
- surface source conflicts;
- flag claims that cannot be verified;
- do not create citations from memory; and
- include a source register with title, publisher, date, source type, and relevance.

Return:
[OUTPUT CONTRACT]
```

## 6. Drafting prompt architect

### Use when

The source content is known and the challenge is communication.

```text
Design a drafting prompt for:
[DELIVERABLE]

Define:
- audience;
- purpose;
- reader action or decision;
- approved facts;
- tone;
- length;
- format;
- required points;
- prohibited claims;
- phrases that must be preserved exactly, if any; and
- review requirements.

Keep content and structure controlled while leaving normal word choice and sentence construction flexible.
```

## 7. Brainstorming divergence prompt

### Use when

You need range before evaluation.

```text
Generate [NUMBER] genuinely distinct ideas for:
[GOAL]

Hard guardrails:
- [GUARDRAIL 1]
- [GUARDRAIL 2]
- [GUARDRAIL 3]

Range dimensions:
- [DIMENSION 1]
- [DIMENSION 2]
- [DIMENSION 3]
- [DIMENSION 4]

For this round:
- do not rank;
- do not reject;
- do not merge similar ideas silently;
- do not optimize for feasibility beyond the hard guardrails; and
- label the core difference that makes each idea distinct.

Return a numbered list with a one-sentence explanation per idea.
```

## 8. Brainstorming convergence prompt

### Use when

A broad idea set already exists and selection should begin.

```text
Evaluate the idea set below only after preserving the original ideas.

Ideas:
[IDEAS]

Criteria:
[CRITERIA]

Process:
1. group related ideas without deleting them;
2. identify duplicates and explain the overlap;
3. score each idea against the criteria;
4. identify high-potential combinations;
5. surface risks and unknowns; and
6. recommend a shortlist with rationale.

Do not introduce new factual claims without evidence.
```

## 9. Hybrid-task decomposer

### Use when

One request contains research, analysis, ideation, and drafting.

```text
Decompose this request into stages:
[REQUEST]

For each stage, provide:
- dominant task type;
- objective;
- input;
- output;
- dependencies;
- what should be tightly controlled;
- what should remain flexible;
- validation gate; and
- whether the stage can run in parallel.

Use this preferred ordering when appropriate:
Research -> Validate -> Analyze -> Brainstorm -> Evaluate -> Draft -> Review

Do not combine stages merely to reduce prompt count.
```

## 10. Task-strategy mismatch diagnostic

### Use when

The output is weak and the prompt may use the wrong control-latitude balance.

```text
Review the prompt and output below.

Prompt:
[PROMPT]

Output:
[OUTPUT]

Diagnose:
1. dominant task type;
2. strategy actually used;
3. symptoms of over-constraint;
4. symptoms of under-constraint;
5. source or evidence defects;
6. whether task decomposition is needed;
7. the smallest responsible repair; and
8. what should remain unchanged.

Do not rewrite the whole prompt until the failure is localized.
```

## 11. Four-strategy comparison exercise

### Use when

You want to observe how the same topic changes across task types.

```text
Use this topic:
[TOPIC]

Create four different task specifications:
1. analysis;
2. research;
3. drafting; and
4. brainstorming.

For each, show:
- objective;
- tightened elements;
- loosened elements;
- evidence requirements;
- uncertainty behavior;
- output contract; and
- success criteria.

Then explain why copying one strategy across all four would reduce quality.
```

## 12. Task-strategy oral drill

### Use when

You want certification-style practice.

```text
Give me eight original professional scenarios, one at a time.

For each scenario, require me to answer:
1. dominant task type;
2. what to tighten;
3. what to loosen;
4. evidence requirement;
5. missing-information behavior;
6. whether retrieval is needed;
7. whether decomposition is needed; and
8. one-sentence prompt strategy.

Score each answer from 0 to 2 for:
- correct task classification;
- control-latitude reasoning;
- evidence discipline;
- decomposition judgment; and
- validation awareness.
```

## Suggested study sequence

1. Run the Task-Type Classifier.
2. Complete the Four-Strategy Comparison Exercise.
3. Practice one prompt each for analysis, research, drafting, and brainstorming.
4. Run the Hybrid-Task Decomposer.
5. Finish with the Task-Strategy Oral Drill.

## Related material

- [Strategy by Task Type](../../modules/02-prompting-task-execution/lessons/05a-strategy-by-task-type.md)
- [Component Stack](../../modules/02-prompting-task-execution/lessons/02a-component-stack.md)
- [Task Decomposition](../../modules/02-prompting-task-execution/lessons/03a-decomposition.md)
- [Iterating to Improve Output](../../modules/02-prompting-task-execution/lessons/04-iterating-to-improve-output.md)
- [Task Strategy Fit Pattern](../../patterns/task-strategy-fit-pattern.md)
