# Lesson 5: Choosing Models

## Overview

The capability layer determines what Claude can do. Model selection determines how well the model is likely to perform the task, how quickly it responds, and how much usage or API cost the workflow consumes.

The certification teaches a durable three-tier decision frame:

1. **Haiku** for fast, structured, high-volume work.
2. **Sonnet** for most professional drafting, synthesis, and analysis.
3. **Opus** for complex judgment, ambiguous inputs, and work where quality outranks speed.

> [!IMPORTANT]
> The tier names, current model versions, default model, plan availability, and automatic switching behavior can change. Learn the decision logic, then verify the live product before deployment or publication.

## Learning objectives

After completing this lesson, you should be able to:

- explain the capability, speed, and cost trade-off among model tiers;
- select Haiku, Sonnet, or Opus using the certification framework;
- recognize when Sonnet is the appropriate starting point;
- identify structured, high-volume work that may fit Haiku;
- identify ambiguous, high-consequence work that may justify Opus;
- explain why the strongest model is not automatically the best model;
- select a model using representative evaluations rather than intuition alone;
- design escalation and routing patterns across tiers;
- distinguish model selection from grounding, Code Execution, and human review; and
- account for current model versions and pricing without memorizing volatile product details.

## The certification decision frame

Use this table for the exam unless the scenario provides evidence that changes the choice.

| Task profile | Model tier | Core reason |
|---|---|---|
| Routine extraction, classification, formatting, or summarization at volume | Haiku | Speed and efficiency matter, and the task is clearly structured |
| Most professional drafting, synthesis, research assistance, and analysis | Sonnet | Balanced quality and speed across general knowledge work |
| Complex judgment, ambiguous inputs, multi-layered reasoning, or high-consequence synthesis | Opus | The quality ceiling matters more than response speed |

```text
Structured + high volume + low ambiguity
                  |
                  v
                Haiku

Most professional knowledge work
                  |
                  v
                Sonnet

Ambiguous + complex + quality-sensitive
                  |
                  v
                 Opus
```

This is a starting heuristic, not proof that a model meets the requirement.

## The three selection dimensions

Model selection balances three primary concerns.

### Capability

Ask:

- How much reasoning depth does the task require?
- Are the inputs clear or ambiguous?
- Does the task require interpretation across multiple sources?
- How severe is the consequence of a weak answer?
- Does the workflow require advanced coding, agentic behavior, or tool use?

### Speed

Ask:

- Is the user waiting interactively?
- Is the workflow processing hundreds or thousands of items?
- What is the acceptable time to first response?
- What is the acceptable end-to-end latency?
- Does slower output create an operational bottleneck?

### Cost and usage

Ask:

- Is usage metered per token or per call?
- What is the expected input and output volume?
- Will the workflow run once, daily, or millions of times?
- Does a higher tier consume scarce subscription usage headroom?
- Can routing or batching reduce unnecessary high-tier use?

```text
                 Capability
                    /\
                   /  \
                  /    \
                 /      \
             Cost ------ Speed
```

A good choice satisfies the quality requirement without paying unnecessary latency or usage cost.

## Haiku

### Best fit

Haiku is the efficiency-oriented tier in the certification model.

Strong candidates include:

- classification against a clear label set;
- extraction into a fixed schema;
- straightforward summarization;
- formatting and normalization;
- routing or triage;
- repeated processing across many independent items;
- sub-tasks inside a larger workflow; and
- low-consequence work where errors can be detected cheaply.

### Why volume matters

A small latency or cost difference becomes significant when repeated across hundreds or thousands of requests.

```text
Single request savings
        x
Number of requests
        =
Operational impact
```

### Haiku risk pattern

Haiku may be underpowered when the task contains:

- subtle exceptions;
- conflicting evidence;
- ambiguous instructions;
- long chains of dependent reasoning;
- nuanced stakeholder judgment; or
- high costs for missed edge cases.

### Example

A system must classify 20,000 public support messages into six well-defined categories. The examples are representative, the output schema is fixed, and uncertain items are routed to human review.

**Reasonable starting tier:** Haiku.

The final decision still depends on measured precision, recall, latency, and cost.

## Sonnet

### Best fit

Sonnet is the balanced tier in the certification model and the preferred starting point for most professional knowledge work.

Strong candidates include:

- business and technical drafting;
- document review;
- synthesis across a manageable source set;
- research assistance;
- structured analysis;
- code explanation and routine coding;
- report development;
- meeting and decision summaries; and
- tasks that need strong quality without the highest available reasoning tier.

### Why Sonnet is the default starting point

Sonnet often provides enough capability for professional work while preserving better speed and usage efficiency than the highest tier.

Use Sonnet first when:

- the task is more than mechanical;
- the inputs are mostly clear;
- professional quality is required;
- the consequence is meaningful but controlled by review; and
- there is no evidence yet that the task requires Opus.

### Upgrade signal

Consider Opus when evaluation shows that Sonnet consistently struggles with:

- ambiguous evidence;
- multi-stage reasoning;
- nuanced trade-offs;
- difficult edge cases;
- long-horizon planning; or
- quality requirements that remain unmet after reasonable prompt and context improvements.

### Downgrade signal

Consider Haiku when evaluation shows that:

- the task is highly structured;
- the output contract is narrow;
- the quality threshold is still met;
- volume is large; and
- speed or cost materially improves.

## Opus

### Best fit

Opus is the higher-capability tier in the certification model.

Strong candidates include:

- strategic analysis;
- complex multi-document synthesis;
- nuanced judgment;
- ambiguous or incomplete inputs;
- complex planning;
- advanced technical review;
- consequential client-facing or executive deliverables;
- tasks with several interacting constraints; and
- work where quality is more important than response speed.

### Opus does not remove controls

A stronger model does not eliminate the need for:

- authoritative sources;
- citations;
- Code Execution for calculations;
- privacy and authorization controls;
- evaluation;
- human review; or
- accountable final decisions.

```text
Higher capability
       !=
Guaranteed correctness
```

### High stakes versus high capability

High-stakes work may justify testing Opus, but the consequence of the task also requires stronger controls around the model.

A model tier is one component of a governed workflow, not the governance mechanism itself.

## A better production rule: use the minimum qualified model

The strongest practical principle is:

> Use the fastest and least costly model that meets the validated quality threshold for the use case.

This avoids two failure modes.

### Under-resourcing

A model is selected for speed or cost even though it fails important edge cases.

### Over-engineering

The most capable model is used for routine work where a lower tier performs equally well against the actual success criteria.

### Qualification process

1. Define the task and consequence.
2. Define measurable success criteria.
3. Build a representative evaluation set.
4. Test candidate models with the same prompts, tools, and evidence.
5. Measure quality, latency, and cost.
6. Review severe failures individually.
7. Select the minimum model that passes.
8. Monitor production drift and model changes.

## Evaluation before selection

Do not select a model only from a marketing description or tier name.

Evaluate with:

- real or representative inputs;
- normal cases;
- edge cases;
- adversarial or malformed inputs;
- missing evidence;
- long-context examples;
- tool calls, if applicable;
- required output schemas; and
- human-reviewed expected outcomes.

### Useful metrics

| Task type | Example metrics |
|---|---|
| Classification | Precision, recall, F1, abstention quality |
| Extraction | Field accuracy, schema validity, missing-field rate |
| Drafting | Rubric score, completeness, source support, revision burden |
| Analysis | Factual accuracy, reasoning quality, edge-case handling |
| Tool use | Tool-selection accuracy, argument validity, recovery rate |
| Coding | Test pass rate, defect rate, maintainability review |
| High-consequence work | Severe-failure rate, reviewer overrides, escaped-error rate |

The average score is not sufficient when a rare failure can cause major harm.

## Model escalation and routing

A workflow does not have to use one model for every item.

### Simple routing pattern

```text
Incoming item
     |
     v
Haiku: structured first pass
     |
     +-- Clear and validated ----------> Accept
     |
     +-- Ambiguous or low confidence --> Sonnet
                                           |
                                           +-- Complex exception --> Opus
                                                                   |
                                                                   v
                                                              Human review
```

### Good routing signals

- missing required fields;
- conflicting evidence;
- out-of-distribution input;
- low evaluator score;
- failed schema validation;
- high-risk category;
- unresolved ambiguity;
- tool failure; or
- human escalation request.

### Routing warning

Do not use self-reported model confidence as the only routing signal. Use observable checks, external validation, and task-specific thresholds.

## What model selection cannot fix

A stronger model cannot compensate for every system failure.

| Problem | Better control |
|---|---|
| Current facts are missing | Web search, Research, retrieval, or supplied authoritative sources |
| A calculation must be correct | Code Execution plus method validation |
| The wrong documents were uploaded | Source and access review |
| The prompt is contradictory | Prompt and configuration repair |
| The Project knowledge is stale | Knowledge-base maintenance |
| The workflow lacks approval | Human-review design |
| The output schema is invalid | Deterministic schema validation |
| Sensitive data is unauthorized | Data governance and access control |

Upgrade the model only when the failure is actually capability-related.

## Subscription usage versus API cost

### Metered environments

In API or usage-budgeted environments, model selection directly affects per-call cost. Input length, output length, caching, tool use, and request volume all matter.

### Subscription environments

On a standard subscription surface, the user may not see a dollar amount for each request. Efficiency still matters through:

- response speed;
- usage limits;
- rate limits;
- remaining usage headroom; and
- the ability to complete more work within the plan.

The decision logic remains the same: do not spend higher-tier capability where the task does not require it.

## Current product reality, dated July 14, 2026

The certification pins the three-tier Haiku, Sonnet, and Opus framework. Current Anthropic documentation lists an evolved lineup that includes a fourth widely released tier, Claude Fable 5, above the current Opus tier.

| Current documented model | Current description | Comparative latency |
|---|---|---|
| Claude Fable 5 | Highest available capability for demanding reasoning and long-running agents | Slower |
| Claude Opus 4.8 | Complex agentic coding and enterprise work | Moderate |
| Claude Sonnet 5 | Strong combination of speed and intelligence | Fast |
| Claude Haiku 4.5 | Fastest, economical model with strong reasoning | Fastest |

This table is a dated product snapshot, not an exam memorization target.

> [!NOTE]
> The course's statement that Opus trades speed for capability remains directionally useful, but the current documentation characterizes the latest Opus model as moderate latency rather than simply slow. Always verify the current lineup and product surface.

Current official documentation also describes an `effort` control on recent Opus and Sonnet models. In production, tuning effort may sometimes improve the capability, latency, and cost balance without switching tiers.

## Versioning and model changes

Model selection includes selecting a version, not only a family name.

Production workflows should record:

- exact model identifier;
- provider and endpoint;
- effort or thinking settings;
- prompt version;
- tool definitions;
- retrieval configuration;
- evaluation-set version;
- latency and cost baseline; and
- rollback model.

When changing models:

1. freeze the current workflow configuration;
2. run the baseline model;
3. run the candidate model on the same evaluation set;
4. compare quality, latency, cost, schema validity, and tool behavior;
5. investigate severe regressions;
6. stage the rollout; and
7. maintain rollback capability.

Do not change the model, prompt, tools, and source set simultaneously if you need to understand the cause of a performance change.

## Worked scenarios

### Scenario 1: High-volume extraction

A team must extract five fields from 50,000 standardized public forms. The schema is fixed, examples are available, and failed records enter an exception queue.

**Starting tier:** Haiku.

**Validation:** field-level accuracy, schema validity, exception rate, latency, and cost.

### Scenario 2: Professional report draft

An analyst must synthesize several public reports into a concise briefing with source references and clearly labeled uncertainty.

**Starting tier:** Sonnet.

**Validation:** completeness, source support, organization, factual accuracy, and revision burden.

### Scenario 3: Ambiguous strategic decision

A leadership team needs a multi-option strategy based on conflicting evidence, uncertain assumptions, long-term consequences, and several stakeholder constraints.

**Starting tier:** Opus.

**Validation:** reasoning quality, treatment of uncertainty, coverage of trade-offs, evidence use, and human expert review.

### Scenario 4: Tiered workflow

A system classifies routine cases at high volume, sends uncertain cases for deeper analysis, and routes high-risk exceptions to expert review.

**Architecture:** Haiku first pass, Sonnet or Opus escalation, deterministic checks, and human review.

### Scenario 5: Consequential calculation

A user asks for a complex financial projection.

**Model choice:** Sonnet or Opus may help interpret assumptions, but the calculation itself belongs in Code Execution. The model tier does not replace executed computation.

## Example prompts

### Model-selection recommendation

```text
Act as an AI evaluation architect.

Task:
[DESCRIBE TASK]

Recommend the appropriate certification tier:
- Haiku;
- Sonnet; or
- Opus.

Evaluate:
- task structure;
- ambiguity;
- reasoning depth;
- consequence of error;
- request volume;
- latency target;
- usage or cost constraints;
- source requirements;
- tool requirements;
- review controls; and
- escalation conditions.

Return:
1. recommended starting tier;
2. rationale;
3. lower-tier risk;
4. higher-tier trade-off;
5. evaluation plan;
6. success thresholds; and
7. conditions that trigger escalation or downgrade.
```

### Cross-model evaluation plan

```text
Design a controlled evaluation comparing Haiku, Sonnet, and Opus for this workflow.

Keep constant:
- prompt;
- source set;
- tool definitions;
- output schema;
- evaluation cases; and
- scoring rubric.

Measure:
- quality;
- severe failures;
- edge-case handling;
- latency;
- usage or cost;
- structured-output validity;
- tool reliability; and
- human revision effort.

Recommend the minimum qualified model, not automatically the highest tier.
```

## Common mistakes

### Always choosing the strongest model

This increases latency and usage without proving better results for the actual task.

### Always starting with the cheapest model

This can hide serious edge-case failures when the task is ambiguous or consequential.

### Treating Sonnet as universally correct

Sonnet is a strong general starting point, but structured workloads may qualify for Haiku and difficult tasks may require Opus.

### Using tier names instead of evaluations

Model descriptions guide initial testing. Representative evaluation determines deployment fitness.

### Assuming high stakes are solved by Opus

High stakes require grounding, controls, verification, and accountable review regardless of model tier.

### Ignoring model version changes

A new version may improve average performance while regressing a critical edge case.

### Mixing changes during migration

Changing the model, prompt, tools, and retrieval system together makes failures difficult to attribute.

## Hands-on lab

### Objective

Select and validate the minimum qualified model for a fictional professional workflow.

### Part 1: Define the task

Choose one:

- structured extraction;
- professional briefing;
- complex policy analysis; or
- high-volume classification.

Document:

- inputs;
- output contract;
- ambiguity;
- consequence;
- volume;
- latency target;
- review process; and
- severe failure definition.

### Part 2: Create an evaluation set

Build at least twelve cases:

- six normal cases;
- three edge cases;
- two incomplete-input cases; and
- one adversarial or misleading case.

### Part 3: Compare tiers

Run the same cases with the same prompt and score:

- correctness;
- completeness;
- grounding;
- schema validity;
- latency; and
- revision effort.

### Part 4: Decide

Select:

- the minimum qualified model;
- the escalation model;
- routing conditions;
- production monitoring; and
- rollback criteria.

### Acceptance criteria

- The recommendation is supported by measured results.
- Severe failures receive more weight than minor stylistic differences.
- The strongest model is not selected by default.
- Cost and latency are considered after the quality floor is defined.
- Human review remains where consequence requires it.

## Knowledge check

### Question 1

A company must classify 100,000 standardized records into four categories. The task has clear examples and uncertain cases are routed to review. Which certification tier is the best starting point?

A. Haiku
B. Sonnet
C. Opus
D. Always the newest model

**Answer:** A. Haiku.

### Question 2

A professional needs to draft and refine a technical report from a clear set of source documents. Which tier is the normal starting point?

A. Haiku
B. Sonnet
C. Opus
D. Code Execution only

**Answer:** B. Sonnet.

### Question 3

A strategy task contains conflicting evidence, multiple stakeholders, ambiguous assumptions, and high-quality requirements. Which tier should be tested first?

A. Haiku
B. Sonnet only
C. Opus
D. No model can assist

**Answer:** C. Opus.

### Question 4

True or false: Selecting Opus removes the need to verify factual claims.

**Answer:** False.

### Question 5

What is the best production rule?

A. Always use the cheapest model
B. Always use the most capable model
C. Use the minimum model that passes representative evaluations
D. Use the default model without testing

**Answer:** C.

### Question 6

A calculation is consequential and complex. Which statement is correct?

A. Opus makes Code Execution unnecessary
B. Haiku is always sufficient for calculations
C. Use a suitable model to interpret the task and Code Execution to run the calculation
D. Model selection has no relevance

**Answer:** C.

## Flashcards

**Q:** What tier is optimized for structured, high-volume work in the certification model?

**A:** Haiku.

**Q:** What is the normal starting tier for most professional knowledge work?

**A:** Sonnet.

**Q:** When is Opus the strongest certification choice?

**A:** When the task requires complex judgment, nuanced reasoning, interpretation of ambiguous inputs, or quality that outweighs speed.

**Q:** What three dimensions dominate model selection?

**A:** Capability, speed, and cost or usage.

**Q:** What is the minimum-qualified-model rule?

**A:** Use the fastest and least costly model that meets the validated quality threshold.

**Q:** Does a stronger tier guarantee factual accuracy?

**A:** No.

**Q:** What should remain constant during a controlled model comparison?

**A:** Prompts, source data, tools, output contract, evaluation cases, and rubric.

**Q:** What should trigger escalation to a stronger tier?

**A:** Observable quality failures, ambiguity, edge cases, high-risk categories, or failed validation, not self-reported confidence alone.

**Q:** Why are model IDs and versions important?

**A:** Different versions can behave differently, so production results must be reproducible and migration must be tested.

**Q:** Is Claude Fable 5 part of the certification's three-tier frame?

**A:** No. It is a current product-tier note, not the exam's core Haiku, Sonnet, and Opus framework.

## Certification lens

For the exam, remember:

```text
Haiku  = structured, fast, high volume
Sonnet = balanced default for professional work
Opus   = complex, ambiguous, quality-sensitive work
```

Then apply the trade-off:

```text
Do not under-resource complex work.
Do not over-engineer routine work.
```

## Engineering lens

For real deployment, remember:

```text
Tier description
      -> initial hypothesis
Representative evaluation
      -> evidence
Minimum qualified model
      -> deployment choice
Monitoring and regression tests
      -> continued fitness
```

## Key takeaways

- Haiku prioritizes speed and efficiency for structured work.
- Sonnet is the balanced starting point for most professional tasks in the certification frame.
- Opus is appropriate when ambiguity, reasoning complexity, and output quality dominate.
- A higher tier does not replace grounding, Code Execution, or human review.
- Select the minimum qualified model through representative evaluations.
- Routing can combine tiers efficiently.
- Model versions, pricing, plan availability, and latency characteristics change over time.
- The live product lineup currently extends beyond the certification's three-tier frame.

## Official reading

- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)

## Version-awareness note

The certification framework, current model lineup, model picker, default model, plan availability, automatic switching, effort controls, comparative latency, and pricing can change. Treat the current Claude product and official Anthropic documentation as authoritative at the time of use.