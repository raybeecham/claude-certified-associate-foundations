# Module 2 Key Takeaways — Prompt Notebook

Use these prompts for recall, transfer, oral review, and remediation. Replace bracketed text with fictional, public, synthetic, or explicitly authorized material.

---

## 1. Five-takeaway recall drill

```text
Test my recall of the five Module 2 takeaways:
1. structure over cleverness;
2. context gaps;
3. decomposition;
4. diagnostic iteration; and
5. task-strategy fit.

Ask one short question at a time. After each answer:
- mark it Correct, Partial, or Incorrect;
- identify the missing idea;
- give a one-sentence correction; and
- continue to the next takeaway.

Do not reveal later answers early.
```

---

## 2. Component-stack inspection

```text
Inspect the prompt below using Role, Context, Task, Constraints, and Output Format.

Prompt:
[PROMPT]

For each component:
- state whether it is present, useful, missing, or decorative;
- predict the output consequence;
- recommend the smallest repair; and
- identify anything that should remain flexible.

End with a minimum-sufficient repaired prompt.
```

---

## 3. Hidden-context recovery

```text
A user wrote this prompt:

[PROMPT]

The output was generic:
[OUTPUT]

Infer only the likely categories of context that may be missing. Do not invent facts.

Return:
1. What the author may know that the model was not told;
2. The three highest-value clarification questions;
3. A prompt skeleton with placeholders for the missing context; and
4. A warning against including irrelevant background.
```

---

## 4. Minimum-sufficient-context editor

```text
Review the context package below for an AI task.

Task:
[TASK]

Context package:
[CONTEXT]

Classify every context item as:
- Essential;
- Useful but optional;
- Stale or conflicting;
- Irrelevant; or
- Requires verification.

Then produce a minimum-sufficient context block that preserves everything needed to perform and validate the task.
```

---

## 5. Decomposition detector

```text
Determine whether this request should remain one prompt or be decomposed:

[REQUEST]

Assess:
- number of primary verbs;
- stage dependencies;
- shared evidence;
- intermediate validation needs;
- deterministic operations;
- tool calls or side effects;
- independent parallel branches; and
- error-propagation risk.

Return:
1. Decision: Single task / Sequential decomposition / Shared-foundation parallel workflow;
2. Rationale;
3. Proposed stages;
4. Input, Process, Output, and Validation for each stage; and
5. Human approval points.
```

---

## 6. Shared-foundation workflow builder

```text
Several deliverables must be created from the same source material.

Source:
[SOURCE DESCRIPTION]

Deliverables:
[DELIVERABLES]

Design a workflow that:
- extracts the shared factual foundation;
- validates that foundation before drafting;
- identifies which deliverables can run in parallel;
- gives every branch a versioned state capsule;
- performs a final consistency review; and
- defines what happens if the shared foundation changes.
```

---

## 7. Failure-localization drill

```text
Analyze the following prompt and output.

Prompt:
[PROMPT]

Output:
[OUTPUT]

Acceptance criteria:
[CRITERIA]

Use this sequence:
Observe → Diagnose → Modify → Validate → Decide

Return:
- the dominant symptom;
- the most likely responsible component;
- evidence for the diagnosis;
- one targeted revision;
- what should remain unchanged;
- a regression check; and
- a stopping rule.
```

---

## 8. One-change iteration log

```text
Help me run a controlled prompt iteration.

Original prompt:
[PROMPT]

Original output:
[OUTPUT]

Observed failure:
[FAILURE]

Create an iteration log with:
- hypothesis about the responsible component;
- one proposed change;
- expected improvement;
- protected working elements;
- comparison criteria;
- regression risks; and
- continue/stop decision after the next output.
```

---

## 9. Prompt-failure versus system-failure classifier

```text
Classify the following failure as primarily:
- Prompt specification;
- Missing or weak evidence;
- Model selection;
- Context degradation;
- Tool design or permissions;
- Deterministic computation;
- Evaluation design;
- Governance or approval; or
- Workflow architecture.

Scenario:
[SCENARIO]

Explain why prompt revision is or is not the right first intervention. Recommend the smallest system-level repair.
```

---

## 10. Task-strategy planner

```text
Classify this request as analysis, research, drafting, brainstorming, or a hybrid:

[REQUEST]

For each relevant task type, identify:
- what determines validity;
- what should be tightly controlled;
- what benefits from latitude;
- evidence requirements;
- uncertainty behavior;
- output requirements; and
- evaluation method.

If hybrid, decompose it into task-appropriate stages.
```

---

## 11. Analysis strategy drill

```text
Turn the following analytical request into a reliable task specification:

[REQUEST]

Define:
- analytical question;
- evidence boundary;
- criteria;
- comparison standard;
- missing and conflicting evidence behavior;
- deterministic checks;
- output structure; and
- acceptance criteria.

Do not add stylistic constraints unrelated to analytical validity.
```

---

## 12. Research strategy drill

```text
Design a research prompt for this question:

[QUESTION]

Decide:
- whether supplied sources are sufficient;
- whether current web retrieval is required;
- time, geography, and scope boundaries;
- source hierarchy;
- primary versus secondary source use;
- citation requirements;
- conflict handling;
- fact versus inference labeling; and
- verification gaps.

Return the research prompt and a source-validation checklist.
```

---

## 13. Drafting strategy drill

```text
Create a drafting prompt from these facts:

Facts:
[FACTS]

Define:
- audience;
- communication purpose;
- desired reader action;
- required facts;
- prohibited claims;
- tone;
- length;
- format; and
- approval-sensitive language.

Leave word choice, transitions, and sentence construction flexible unless exact language must be preserved.
```

---

## 14. Brainstorming divergence drill

```text
Create a two-phase brainstorming workflow for this goal:

[GOAL]

Phase 1 must:
- preserve divergence;
- use only hard guardrails;
- request volume and distinct directions; and
- prohibit ranking or early rejection.

Phase 2 must:
- group ideas;
- apply evaluation criteria;
- identify trade-offs;
- rank candidates; and
- select ideas for development.

Explain which constraints belong in each phase and why.
```

---

## 15. Verified-computation router

```text
Review the task below and identify every operation that should be performed by code or another deterministic method rather than prose generation.

Task:
[TASK]

For each operation, define:
- required input;
- calculation or transformation;
- validation check;
- expected output;
- error handling; and
- how the result should be passed back into the narrative stage.
```

---

## 16. Decorative-instruction detector

```text
Review the proposed prompt fragments below.

Task goal:
[GOAL]

Fragments:
[FRAGMENTS]

Classify each fragment as:
- Functional and necessary;
- Functional but optional;
- Decorative;
- Misplaced for this task type;
- Duplicative; or
- Harmful over-specification.

For every functional fragment, name the output requirement or failure mode it protects.
```

---

## 17. Module 2 oral exam

```text
Run a ten-question oral exam on Module 2.

Cover:
- component stack;
- context gaps;
- sequential decomposition;
- parallel decomposition;
- targeted iteration;
- convergence;
- analysis strategy;
- research strategy;
- drafting strategy;
- brainstorming strategy; and
- deterministic verification.

Ask one scenario question at a time. Require me to:
1. identify the symptom;
2. name the dominant defect;
3. choose one targeted intervention; and
4. reject the closest distractor.

Score each answer from 0 to 2 and provide a final remediation plan.
```

---

## 18. Five-takeaway transfer exercise

```text
Apply all five Module 2 takeaways to this real or synthetic workflow:

[WORKFLOW]

Return five sections:
1. Structure: Which prompt components are required?
2. Context: What cannot be safely inferred?
3. Decomposition: What stages and validation gates are needed?
4. Iteration: How will failures be localized and repaired?
5. Strategy: Where should control and latitude change by stage?

Finish with a complete workflow diagram and the first-stage prompt.
```

---

## 19. Certification shortcut generator

```text
Create a one-page recall sheet for Module 2 using only these principles:
- structure over cleverness;
- context gaps;
- checkable decomposition;
- targeted iteration; and
- task-strategy fit.

For each principle include:
- one-sentence rule;
- common symptom;
- best intervention;
- nearest distractor; and
- one memory cue.
```

---

## 20. Module reflection log

```text
Help me record a Module 2 reflection.

Ask me for:
- the most useful principle;
- the concept I still confuse;
- one prompt I repaired;
- one workflow I decomposed;
- one case where I used too many constraints;
- one case where deterministic execution was required; and
- one action I will apply at work.

Then format my answers as:
- What I learned;
- Evidence of mastery;
- Remaining gaps;
- Application plan; and
- Review date.
```

---

## Public-repository rule

Use fictional, generic, synthetic, public, or explicitly authorized material. Do not place confidential data, credentials, proprietary workflows, engagement-identifying details, remembered live-exam questions, or reconstructed proprietary course content into these prompts.
