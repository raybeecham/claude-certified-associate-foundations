# Module 2 Quiz and Remediation Prompt Notebook

Use these prompts to practice the reasoning behind Module 2 scenario questions. Do not memorize answer letters. Explain the failure, locate the responsible component or workflow decision, and justify the smallest effective repair.

## Notebook goals

Practice:

- component diagnosis;
- task decomposition;
- targeted iteration;
- task-strategy fit;
- deterministic tool routing;
- distractor rejection; and
- concept-specific remediation.

---

## 1. Five-domain quiz generator

```text
Create an original five-question scenario quiz covering:
1. component-based prompt specification;
2. sequential task decomposition;
3. targeted prompt iteration;
4. strategy calibration for brainstorming; and
5. deterministic verification through code.

Requirements:
- use fictional professional scenarios;
- provide four answer choices per question;
- include one strongest answer and three plausible distractors;
- do not reveal the answer key until after all questions;
- avoid copying known course or exam wording;
- after the quiz, explain why the correct answer is strongest and why each distractor is weaker.
```

## 2. Symptom-to-defect drill

```text
Give me ten short output symptoms from AI-assisted work.

For each symptom, ask me to identify the dominant cause from:
- role;
- context;
- task;
- constraints;
- output contract;
- evidence boundary;
- decomposition;
- task strategy;
- execution layer; or
- validation.

Do not show the answers until I respond.
Afterward, grade each diagnosis and identify the smallest effective repair.
```

## 3. Distractor analysis

```text
Present five prompting scenarios with four answer choices each.
For every question, make the incorrect choices represent common distractor patterns such as:
- switch to a stronger model;
- ask the model to try harder;
- increase length;
- retry unchanged;
- rewrite everything;
- trust unverified arithmetic; or
- apply final filters too early.

After I answer, explain:
1. the observed symptom;
2. the dominant design defect;
3. why the best answer addresses it; and
4. why the nearest distractor is tempting but insufficient.
```

## 4. Component specification scenario

```text
Give me a weak professional drafting prompt that produces generic output.
Ask me to repair it using only the minimum necessary changes.

Require me to identify:
- missing context;
- missing audience or purpose;
- ambiguous task language;
- missing constraints;
- missing output format; and
- any decorative instruction that should not be added.

Grade the repair for functional completeness rather than prompt length.
```

## 5. Decomposition oral drill

```text
Give me a complex evaluation request containing at least four dependent reasoning stages.
Ask me to explain aloud:
- why one-pass execution is risky;
- what intermediate outputs are required;
- where validation gates belong;
- which stages must remain sequential;
- whether any work can safely run in parallel; and
- how the final recommendation should trace to prior evidence.

Challenge any stage that lacks a clear input, process, output, or validation rule.
```

## 6. Iteration diagnosis drill

```text
Provide:
- an original prompt;
- the output it produced; and
- explicit acceptance criteria.

Make most of the output correct, with one or two quality dimensions failing.
Ask me to:
1. identify what already passes;
2. localize the failed component;
3. propose one targeted revision;
4. define what must be preserved;
5. define a regression check; and
6. state a stopping condition.

Do not accept a wholesale rewrite unless the prompt is foundationally incomplete.
```

## 7. Brainstorming calibration drill

```text
Give me four brainstorming prompts:
- one under-specified;
- one appropriately calibrated;
- one over-constrained;
- one that mixes divergence and convergence.

Ask me to classify each prompt and repair the defective ones.

Require the repairs to distinguish:
- hard guardrails that belong in round one;
- final-selection filters that should be deferred;
- requested volume;
- dimensions of variety; and
- the later convergence stage.
```

## 8. Execution-layer selection drill

```text
Give me ten mixed tasks that combine language reasoning with exact operations.
Examples may involve:
- averages or medians;
- frequency counts;
- date calculations;
- sorting;
- duplicate detection;
- evidence synthesis;
- drafting; or
- qualitative interpretation.

For each task, ask me to assign responsibility to:
- model reasoning;
- code execution;
- retrieval or search;
- deterministic validation; or
- human review.

After I answer, explain any unsafe or unreliable routing decisions.
```

## 9. Full-marks reconstruction

```text
I completed a five-question prompting foundations quiz with full marks.
Help me reconstruct the underlying reasoning without reproducing proprietary question wording.

For each capability below, create one original scenario and ask me to explain the governing rule:
- components;
- decomposition;
- diagnostic iteration;
- task-type strategy; and
- verified computation.

Score the explanation for transfer of understanding, not recall of exact phrasing.
```

## 10. Nearest-distractor challenge

```text
Create five difficult scenario questions where two options appear reasonable.
The correct answer should be the one that is:
- more targeted;
- better aligned to the observed symptom;
- less complex than necessary alternatives;
- more auditable; or
- more reliably validated.

After I answer, compare the correct option with the nearest distractor in a two-column table.
```

## 11. Remediation planner

```text
Grade my responses to a Module 2 scenario quiz.
For every missed question, return:
- primary concept missed;
- secondary concept involved;
- reasoning error;
- one lesson to revisit;
- one short practice task;
- one transfer question using a different scenario; and
- the evidence that would show remediation is complete.

Do not recommend rereading the entire module when a narrower repair is sufficient.
```

## 12. Quiz coverage auditor

```text
Review an original Module 2 quiz and assess whether it adequately covers:
- component prompting;
- decomposition;
- diagnostic iteration;
- task-strategy adaptation; and
- deterministic computation.

Return a table with:
- capability;
- questions that assess it;
- depth of assessment;
- likely blind spots;
- distractor quality; and
- proposed improvement.

Flag questions that test vocabulary recall instead of scenario reasoning.
```

## 13. Explain the rule, not the answer

```text
Ask me five original Module 2 multiple-choice questions one at a time.
After each answer, do not immediately say only correct or incorrect.
Ask me to explain:
- the symptom;
- the root cause;
- the targeted intervention;
- why the nearest alternative is weaker; and
- how I would validate the fix.

Grade the reasoning separately from the selected option.
```

## 14. Timed oral review

```text
Run a five-minute oral review of Module 2.
Ask one concise scenario question for each area:
1. component stack;
2. decomposition;
3. iteration;
4. strategy by task type; and
5. tool-based verification.

Allow approximately 45 seconds per response.
After all five, provide:
- score;
- strongest area;
- weakest area;
- one misconception to correct; and
- one final readiness drill.
```

## 15. Build a decision tree

```text
Help me build a compact decision tree for Module 2 scenario questions.
The tree should begin with the observed failure and route through questions such as:
- Is the objective unclear?
- Is necessary context missing?
- Is the output shape wrong?
- Are several dependent tasks combined?
- Is the task over-constrained for brainstorming?
- Is exact calculation being attempted through prose?
- Does most of the output already pass?

Return:
1. a text-based decision tree;
2. one example per branch; and
3. one common false positive per branch.
```

## 16. Transfer exercise

```text
Create one realistic workflow that includes all five Module 2 capabilities.
The workflow should require:
- repairing an under-specified request;
- decomposing the work;
- selecting different strategies for at least two task types;
- using code for one deterministic operation; and
- iterating on one failed output component.

Ask me to design the workflow before showing a model solution.
Evaluate my design for specification quality, auditability, tool routing, and validation.
```

## 17. Reflection log

```text
Help me record a Module 2 quiz reflection.
Ask me for:
- score;
- questions that felt uncertain;
- distractors I considered;
- concepts I applied confidently;
- any answers I chose correctly for the wrong reason;
- remediation completed; and
- readiness for the next module.

Convert my answers into a concise Markdown study log.
```

## Readiness standard

You are ready to move on when you can consistently:

- identify the dominant defect from the output symptom;
- choose targeted specification over vague effort language;
- decompose dependent work before recommending;
- revise failed components without discarding working ones;
- preserve brainstorming latitude before filtering; and
- route exact calculation to deterministic execution and validation.

## Public-repository content rule

Use only original, fictional, generic, synthetic, public, or explicitly authorized scenarios. Do not reproduce remembered live-exam questions, proprietary course questions, client material, confidential information, or engagement-identifying facts.
