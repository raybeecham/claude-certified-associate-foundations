# Module 1 Prompt Notebook: Choosing Models

These prompts support model-tier selection, controlled evaluations, routing, cost analysis, and migration planning. Replace bracketed text with fictional, synthetic, public, or authorized information.

Model names, versions, pricing, plan availability, and latency change. Verify current official Anthropic documentation before making a production recommendation.

## 1. Certification-tier selector

### Use when

You need to choose Haiku, Sonnet, or Opus using the certification framework.

```text
Act as an AI workflow architect.

Task:
[DESCRIBE TASK]

Recommend a starting tier:
- Haiku;
- Sonnet; or
- Opus.

Evaluate:
- task structure;
- ambiguity;
- reasoning depth;
- number and diversity of sources;
- consequence of error;
- request volume;
- latency requirements;
- cost or usage constraints;
- output complexity;
- tool use;
- review controls; and
- acceptable failure rate.

Return:
1. recommended tier;
2. rationale;
3. risk of using a lower tier;
4. trade-off of using a higher tier;
5. required evaluation cases;
6. success thresholds;
7. escalation conditions; and
8. controls that model selection does not replace.
```

## 2. Minimum-qualified-model evaluation

### Use when

You want to select the fastest and least costly model that meets the quality requirement.

```text
Design a controlled evaluation to identify the minimum qualified model.

Candidate models:
[MODELS]

Workflow:
[WORKFLOW]

Keep constant:
- prompt and system instructions;
- evidence set;
- tool definitions;
- output schema;
- test cases;
- scoring rubric; and
- review process.

Measure:
- factual accuracy;
- task completion;
- edge-case handling;
- severe failure rate;
- structured-output validity;
- tool-call reliability;
- latency;
- input and output usage;
- estimated cost;
- human revision time; and
- abstention or escalation quality.

Define a minimum quality floor before comparing cost.
Recommend the least costly and fastest model that clears the floor.
```

## 3. Representative evaluation-set builder

### Use when

A model decision is being made without enough realistic test cases.

```text
Create a representative evaluation set for this task.

Task:
[TASK]

Expected users and environment:
[CONTEXT]

Build cases covering:
- normal inputs;
- high-volume routine inputs;
- ambiguous inputs;
- incomplete evidence;
- conflicting evidence;
- malformed inputs;
- long-context cases;
- tool failures;
- adversarial or misleading content;
- high-consequence edge cases; and
- cases that should escalate to a human.

For each case, provide:
- input summary;
- expected behavior;
- unacceptable failure;
- scoring dimensions;
- severity weight; and
- review owner.

Do not include proprietary or unauthorized data.
```

## 4. Haiku suitability review

### Use when

A structured, high-volume workflow may benefit from a fast tier.

```text
Evaluate whether this workflow is a strong Haiku candidate.

Workflow:
[WORKFLOW]

Assess:
- label or schema clarity;
- input consistency;
- ambiguity;
- exception frequency;
- consequence of error;
- availability of examples;
- deterministic validation;
- human exception handling;
- volume;
- latency target; and
- cost sensitivity.

Return:
1. suitability rating;
2. required benchmark;
3. minimum precision, recall, or field-accuracy thresholds;
4. exception-routing rules;
5. cases that should bypass Haiku; and
6. conditions requiring Sonnet or Opus.
```

## 5. Sonnet baseline review

### Use when

You are determining whether Sonnet should remain the default for professional knowledge work.

```text
Evaluate Sonnet as the baseline model for this professional workflow.

Workflow:
[WORKFLOW]

Determine:
- which requirements Sonnet is likely to satisfy;
- which edge cases may require Opus;
- whether structured sub-tasks could use Haiku;
- source and grounding controls;
- Code Execution needs;
- human review requirements;
- evaluation metrics; and
- downgrade and upgrade criteria.

Return a baseline architecture and an escalation plan.
```

## 6. Opus justification memo

### Use when

A team wants to use Opus and needs an evidence-based justification.

```text
Write a model-selection justification for testing Opus.

Task:
[TASK]

Explain whether the task contains:
- ambiguous or conflicting evidence;
- multi-stage reasoning;
- nuanced judgment;
- interacting constraints;
- long-horizon planning;
- difficult edge cases;
- high revision cost; or
- a quality requirement that lower tiers have failed.

Include:
1. evidence that Sonnet or Haiku is insufficient;
2. expected quality benefit;
3. latency and usage trade-off;
4. evaluation plan;
5. controls that remain necessary;
6. rollback criteria; and
7. conditions under which Opus should not be used.

Do not justify Opus solely because the task is described as important.
```

## 7. Tiered routing architect

### Use when

A workflow can use lower tiers for routine items and escalate difficult cases.

```text
Design a tiered model-routing workflow.

Incoming workload:
[WORKLOAD]

Available tiers:
- Haiku;
- Sonnet;
- Opus;
- human review.

Define:
- first-pass tier;
- deterministic prechecks;
- routing signals;
- ambiguity thresholds;
- high-risk categories;
- schema and evidence checks;
- escalation path;
- maximum retry count;
- human-review triggers;
- logging and traceability;
- fallback behavior; and
- success metrics.

Do not use self-reported confidence as the only routing signal.
```

## 8. Cost and usage comparison

### Use when

Model choice must account for workload scale and metered usage.

```text
Estimate the operational cost and usage profile for the candidate models.

Workload assumptions:
- requests per period: [COUNT]
- average input tokens: [INPUT]
- average output tokens: [OUTPUT]
- cache behavior: [DETAILS]
- retry rate: [RATE]
- escalation rate: [RATE]
- batch eligibility: [YES/NO]

Candidate pricing:
[CURRENT VERIFIED PRICING]

For each architecture, calculate:
- base input cost;
- base output cost;
- retry cost;
- escalation cost;
- total cost;
- cost per accepted output;
- expected latency; and
- quality assumptions.

Use Code Execution for arithmetic.
State the pricing date and source.
Do not recommend the cheapest option unless it meets the quality floor.
```

## 9. Model migration regression plan

### Use when

A workflow is moving to a new model version or tier.

```text
Create a controlled model-migration plan.

Current model and version:
[CURRENT]

Candidate model and version:
[CANDIDATE]

Workflow:
[WORKFLOW]

Freeze and record:
- prompts;
- tool definitions;
- source set;
- retrieval configuration;
- output schema;
- effort or thinking settings;
- evaluation data; and
- scoring rubric.

Compare:
- quality;
- severe failures;
- schema validity;
- tool behavior;
- latency;
- usage and cost;
- refusal or fallback behavior;
- human revision effort; and
- edge-case regressions.

Return:
1. test plan;
2. acceptance thresholds;
3. rollout stages;
4. monitoring;
5. rollback triggers; and
6. documentation updates.
```

## 10. Capability-failure diagnosis

### Use when

A workflow is performing poorly and the team assumes a stronger model is the solution.

```text
Diagnose whether this failure is truly caused by insufficient model capability.

Observed failure:
[FAILURE]

Current workflow:
[WORKFLOW]

Classify the likely root cause as:
- model capability;
- missing or stale evidence;
- contradictory instructions;
- context overload;
- poor output contract;
- missing Code Execution;
- tool design;
- retrieval failure;
- authorization or data-quality issue;
- missing human review; or
- unknown.

For each plausible cause, identify:
- evidence;
- test;
- corrective action;
- expected result; and
- whether a model upgrade is justified.

Prefer fixing the actual system defect over upgrading by default.
```

## 11. Subscription-surface efficiency review

### Use when

The user is not paying per API call but still has usage limits or latency constraints.

```text
Evaluate model efficiency on a subscription surface.

Task:
[TASK]

Consider:
- response speed;
- available model tiers;
- usage headroom;
- session length;
- request frequency;
- output length;
- task consequence;
- review burden; and
- fallback options.

Recommend the tier that preserves enough capability while avoiding unnecessary usage pressure.
Verify current plan behavior in the product before finalizing the recommendation.
```

## 12. Current-lineup verification

### Use when

A document mentions model names, defaults, availability, latency, or pricing that may have changed.

```text
Verify the current Claude model lineup using official Anthropic sources only.

Check:
- current model names and IDs;
- relative capability descriptions;
- comparative latency;
- context and output limits;
- pricing;
- plan and provider availability;
- model-picker defaults;
- automatic switching behavior;
- effort or thinking controls;
- deprecations; and
- migration guidance.

Return:
1. dated findings;
2. source links;
3. facts safe to publish;
4. facts that remain plan-specific or unclear; and
5. certification concepts that should remain version-neutral.
```

## Suggested study exercise

Apply prompts 1, 2, and 7 to three fictional workloads:

1. extraction from standardized forms;
2. drafting a professional briefing; and
3. strategic synthesis with conflicting evidence.

Compare the recommendations with the certification heuristic:

```text
Haiku  -> structured and high volume
Sonnet -> balanced professional default
Opus   -> complex and quality-sensitive
```

## Related material

- [Lesson 5: Choosing Models](../../modules/01-platform-model-foundations/lessons/05-choosing-models.md)
- [Model-selection patterns](../../patterns/model-selection-patterns.md)
- [Capability Layer lesson](../../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)
- [Evaluator rubric template](../evaluator-rubric-template.md)

## Version-awareness note

Model names, versions, comparative capability, model-picker defaults, effort settings, pricing, plan availability, and provider availability can change. Use current official Anthropic documentation and the actual product surface as the source of truth.