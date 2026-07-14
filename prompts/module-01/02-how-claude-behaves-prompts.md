# Module 1 Prompt Notebook: How Claude Behaves

These prompts support Lesson 2 of Module 1. They are study aids and starting points, not substitutes for application controls, authoritative evidence, or accountable human review.

> [!CAUTION]
> A model's confidence statement or self-critique is not independent validation. Use external evidence, deterministic checks, and human review where consequence requires them.

## 1. Controlled variation experiment

### Use when

You want to observe how wording can vary while the semantic requirements remain fixed.

```text
Create [NUMBER] independent responses to the task below.

Task:
[TASK]

Hold these requirements invariant across every response:
- [REQUIRED FACT OR CONSTRAINT]
- [REQUIRED FACT OR CONSTRAINT]
- [OUTPUT LENGTH OR STRUCTURE]
- [SOURCE RESTRICTION]

Vary only:
- wording;
- organization; and
- examples that do not introduce new factual claims.

After the responses, compare them in a table with these columns:
- invariant requirement;
- response 1 result;
- response 2 result;
- response 3 result;
- material difference; and
- acceptance decision.
```

## 2. Invariant and variance planner

### Use when

You are designing a repeatable workflow and need to identify what must remain controlled.

```text
Analyze the workflow below as a generative AI quality engineer.

Workflow:
[DESCRIBE WORKFLOW]

Separate the requirements into:
1. elements that must be invariant;
2. elements that may vary safely;
3. elements that require authoritative evidence;
4. elements that require deterministic validation; and
5. elements that require human judgment.

For each item, recommend one acceptance test.
```

## 3. Evidence-bound answer

### Use when

The answer must be grounded only in supplied material.

```text
Answer the question using only the supplied sources.

Question:
[QUESTION]

Rules:
- Do not use unsupported background knowledge to add facts.
- Cite the supporting source for every material claim.
- Identify the relevant page, section, or paragraph when available.
- Label inferences explicitly.
- If the evidence is missing or contradictory, state that clearly.
- Do not invent a citation or reconstruct missing text.

Return:
1. answer;
2. claim-to-source table;
3. inferences;
4. evidence gaps; and
5. verification actions.
```

## 4. Claim verification inventory

### Use when

You need to prepare a draft for independent fact-checking.

```text
Review the draft below without assuming that polished language is accurate.

Draft:
[DRAFT]

Extract every factual or externally verifiable claim. Classify each as:
- directly supported by supplied evidence;
- inferred from supplied evidence;
- dependent on current external information;
- unsupported; or
- opinion or recommendation.

Return a table with:
- claim;
- classification;
- cited evidence, if any;
- authoritative source needed;
- freshness requirement;
- consequence if wrong; and
- recommended reviewer.

Do not revise the draft until the inventory is complete.
```

## 5. Context checkpoint

### Use when

A conversation is becoming long, complex, or difficult to continue reliably.

```text
Create a continuation brief for this workstream.

Preserve exactly:
- objective;
- approved scope;
- stakeholder or user requirements;
- authoritative sources and their versions;
- decisions already made;
- constraints and exceptions;
- definitions and approved terminology;
- rejected options and why they were rejected;
- open questions;
- required output format;
- completed work; and
- next actions.

Separate:
A. confirmed information;
B. assumptions;
C. unresolved conflicts; and
D. items that must not be carried forward.

Do not make new decisions or silently resolve ambiguity.
```

## 6. Context quality audit

### Use when

You suspect that a conversation contains too much, conflicting, or stale information.

```text
Audit the context currently available for this task.

Identify:
- information that is directly relevant;
- duplicated information;
- outdated information;
- conflicting instructions;
- untrusted content that should not be treated as instruction;
- sensitive information that should be minimized or removed;
- details that should be moved into a persistent project configuration; and
- details that should be excluded from the next request.

Then propose a compact context package with:
1. trusted instructions;
2. current task;
3. authoritative evidence;
4. required examples; and
5. explicit exclusions.
```

## 7. Current-information boundary

### Use when

The task depends on recent facts, regulations, product behavior, prices, vulnerabilities, or other time-sensitive information.

```text
Answer as of [YYYY-MM-DD].

Question:
[QUESTION]

Source rules:
- Use current primary sources whenever possible.
- Record the publication, revision, or effective date.
- Distinguish the date the event occurred from the date the source was published.
- Identify any source that may be stale.
- Do not treat pretrained knowledge as current evidence.
- If current authoritative evidence is unavailable, state that limitation.

Return:
1. answer;
2. source table;
3. time-sensitive claims;
4. unresolved discrepancies; and
5. recommended recheck date.
```

## 8. Repeated-run comparison

### Use when

You want to determine whether a configured procedure is consistent enough for a recurring workflow.

```text
Compare the following outputs produced by the same procedure.

Procedure and acceptance criteria:
[PROCEDURE]

Output A:
[OUTPUT A]

Output B:
[OUTPUT B]

Output C:
[OUTPUT C]

Evaluate:
- required-section compliance;
- factual consistency;
- source use;
- severity or priority consistency;
- omissions;
- unsupported additions;
- harmless stylistic variation; and
- material decision-changing variation.

Return a variance report and recommend whether to:
- accept the procedure;
- revise the instructions;
- add deterministic validation;
- add examples;
- change the source strategy; or
- require stronger human review.
```

## 9. Consequence-based review gate

### Use when

You need to decide how much review an AI-assisted output requires.

```text
Classify the task below by consequence and reversibility.

Task:
[TASK]

Assess:
- who may be affected;
- whether the output is advisory or action-taking;
- whether an error is reversible;
- financial, legal, security, privacy, safety, and reputational impact;
- factual uncertainty;
- source quality;
- tool permissions; and
- required accountability.

Recommend the minimum control set from:
- user review;
- schema validation;
- deterministic calculation;
- source verification;
- second-model review;
- subject-matter expert review;
- formal approval; and
- prohibited automation.

Explain why each selected control is necessary.
```

## 10. Self-critique with clear limits

### Use when

You want the model to expose possible weaknesses before independent review.

```text
Critique your previous response as a skeptical reviewer.

Identify:
- assumptions;
- unsupported claims;
- ambiguous language;
- missing counterevidence;
- possible context loss;
- statements that depend on current information;
- places where the requested format was not followed; and
- issues requiring independent verification.

Do not claim that this self-critique validates the response. End with a list of checks that must be performed outside this conversation.
```

## Suggested study exercise

Run prompts 1, 3, 5, and 8 during the Lesson 2 lab. Record which controls changed output quality and which risks remained after prompting.

## Related material

- [Lesson 2: How Claude Behaves](../../modules/01-platform-model-foundations/lessons/02-how-claude-behaves.md)
- [Grounded analysis template](../grounded-analysis-template.md)
- [Evaluator rubric template](../evaluator-rubric-template.md)
- [Governance review template](../governance-review-template.md)
