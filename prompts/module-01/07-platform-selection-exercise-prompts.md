# Module 1 Prompt Notebook: Platform Selection Exercise

These prompts help combine entry-point, capability-layer, model-tier, and context-management decisions for one task. Use only fictional, synthetic, public, or authorized information.

## 1. Four-decision platform selector

### Use when

A new task needs a complete Claude configuration rather than a model recommendation alone.

```text
Act as an AI workflow architect.

Task:
[DESCRIBE TASK]

Recommend:
1. entry point: Chat, Project, Artifact, Research, or a combination;
2. capability layer: Project, Skill, Code Execution, Memory, none, or a combination;
3. starting model tier: Haiku, Sonnet, or Opus;
4. context strategy: current conversation, Project instructions, Project knowledge, Memory, state capsule, or authoritative external record;
5. validation and human-review controls.

Evaluate:
- recurrence;
- stability of background context;
- current-information needs;
- source diversity;
- output format;
- procedure repeatability;
- numeric or file-generation requirements;
- ambiguity;
- consequence of error;
- request volume;
- latency;
- cost or usage;
- data sensitivity; and
- expected lifecycle.

Return:
- recommended architecture;
- rationale for every component;
- unnecessary features to exclude;
- risks and controls;
- conditions that would change the recommendation; and
- a compact architecture diagram.
```

## 2. Scenario-to-configuration matcher

### Use when

You want to practice matching scenarios to predefined configuration cards.

```text
Match each scenario to one configuration. Use every configuration exactly once.

Scenarios:
[PASTE SCENARIOS]

Configurations:
[PASTE CONFIGURATIONS]

For each match, identify:
- recurrence signal;
- entry-point signal;
- capability-layer signal;
- model-tier signal;
- context strategy;
- verification requirement; and
- why the closest alternative is weaker.

Do not reveal the answer key until after presenting a blank response table for the learner.
```

## 3. Model trade-off justification coach

### Use when

A learner selected a model but needs to explain the trade-off clearly.

```text
Evaluate the following one-sentence model justification.

Scenario:
[SCENARIO]

Learner answer:
[ANSWER]

Score from 0 to 2 for:
- correct tier;
- specific task signal;
- benefit gained;
- cost accepted;
- awareness of alternatives.

Then provide:
1. total score out of 10;
2. strengths;
3. missing reasoning;
4. a minimally edited stronger sentence; and
5. an exemplary sentence.

A strong answer must state what the model buys and what it costs.
```

## 4. Incorrect-selection diagnosis

### Use when

A learner chose the wrong configuration and needs to understand the misconception.

```text
Diagnose this platform-selection error.

Scenario:
[SCENARIO]

Learner selection:
[SELECTION]

Correct selection:
[CORRECT SELECTION]

Determine whether the error came from misunderstanding:
- recurrence;
- entry points;
- Projects;
- Skills;
- Code Execution;
- Memory;
- current information;
- Artifacts;
- model tiers;
- context lifecycle; or
- human review.

Return:
- root misconception;
- scenario signal that was missed;
- why the selected configuration is weaker;
- a corrective decision rule;
- one new practice question targeting the same misconception.
```

## 5. Configuration simplifier

### Use when

A proposed workflow may contain unnecessary capabilities or an oversized model.

```text
Simplify the proposed Claude architecture below.

Task:
[TASK]

Proposed architecture:
[ARCHITECTURE]

For each element, classify it as:
- required;
- useful but optional;
- unjustified;
- misplaced; or
- requires evaluation.

Assess:
- setup cost;
- maintenance burden;
- permission scope;
- context overhead;
- latency;
- usage or API cost;
- validation burden; and
- failure modes.

Return the least complex architecture that still satisfies the task's quality, evidence, computation, output, and governance requirements.
```

## 6. Configuration-card generator

### Use when

You want fresh scenario-matching practice without reusing course wording.

```text
Create six original professional scenarios and six unique Claude configuration cards.

The set must test:
- one current-information Research case;
- one recurring Project + Skill case;
- one nuanced Opus deliverable case;
- one one-off Chat + Artifact case;
- one Code Execution dataset case;
- one recurring Project + Skill + Code Execution case.

Requirements:
- use fictional or public contexts only;
- vary industries and roles;
- avoid obvious keyword giveaways;
- make at least two distractors plausible for each scenario;
- use every card exactly once;
- include a separate answer key with rationales;
- include one model trade-off writing prompt; and
- do not reproduce certification-course wording.
```

## 7. Code Execution trigger audit

### Use when

A scenario may contain hidden calculations or file-generation requirements.

```text
Review the task below for Code Execution triggers.

Task:
[TASK]

Identify every requested output involving:
- arithmetic;
- percentages;
- statistics;
- thresholding;
- projections;
- data cleaning;
- deduplication;
- joins;
- charts;
- spreadsheets;
- downloadable documents; or
- reproducible transformations.

For each trigger, specify:
- operation;
- input;
- method;
- assumptions;
- validation;
- reconciliation; and
- whether Haiku, Sonnet, or Opus is needed for the surrounding language task.

Do not treat successful execution as proof that the method is correct.
```

## 8. Context-placement extension

### Use when

The configuration is correct but the workflow still mixes stable and temporary information.

```text
For the selected platform configuration below, classify every information item into:
- current conversation;
- Project standing instructions;
- Project knowledge;
- Memory;
- Skill procedure;
- state capsule;
- authoritative external record; or
- do not retain.

Configuration:
[CONFIGURATION]

Information inventory:
[INVENTORY]

For each item, return:
- location;
- rationale;
- scope;
- lifetime;
- authority;
- review cadence;
- sensitivity; and
- deletion or refresh trigger.
```

## 9. Model escalation design

### Use when

The workflow contains routine cases and difficult exceptions.

```text
Design a tiered model-routing workflow for this task.

Task:
[TASK]

Define:
- cases suitable for Haiku;
- escalation signals for Sonnet;
- escalation signals for Opus;
- deterministic validation at each stage;
- human-review triggers;
- severe failure thresholds;
- latency and cost metrics;
- fallback behavior; and
- rollback conditions.

Use observable signals such as missing fields, schema failures, conflicting evidence, out-of-distribution inputs, high-risk categories, or evaluator failures. Do not rely only on model-reported confidence.
```

## 10. Integrated platform-selection rubric

### Use when

You need to score a complete architecture answer.

```text
Score the proposed platform-selection answer from 0 to 2 on each dimension:

- entry point;
- capability layer;
- model tier;
- context strategy;
- current-information handling;
- deterministic computation;
- output format;
- validation;
- human accountability;
- simplicity and efficiency.

Scenario:
[SCENARIO]

Proposed answer:
[ANSWER]

Return:
- score out of 20;
- strongest decisions;
- material omissions;
- over-engineered elements;
- corrected architecture; and
- a concise exam-ready rationale.
```

## Suggested study exercise

1. Complete the six scenarios in the Platform Selection exercise without reading the answer key.
2. Use prompt 3 to score the Opus justification.
3. Use prompt 4 on every incorrect match.
4. Use prompt 6 to generate a fresh six-scenario drill.
5. Repeat until you can explain the scenario signals without relying on configuration letters.

## Related material

- [Platform Selection Exercise](../../modules/01-platform-model-foundations/lessons/07-platform-selection-exercise.md)
- [Core Entry Points prompts](03-core-entry-points-prompts.md)
- [Capability Layer prompts](04-capability-layer-skills-code-execution-prompts.md)
- [Choosing Models prompts](05-choosing-models-prompts.md)
- [Context Management prompts](06-context-management-prompts.md)
