# Model Selection Patterns

## Purpose

These patterns help select and operate Claude models using measured quality, speed, cost, volume, and consequence rather than tier prestige.

The certification uses the Haiku, Sonnet, and Opus frame. Current model names and product availability change, so apply the patterns to the models actually available at the time of use.

## Pattern summary

| Pattern | Use when | Primary principle |
|---|---|---|
| Structured Volume | A clear task repeats at high volume | Start with Haiku and validate |
| Balanced Professional Default | General knowledge work needs strong quality and speed | Start with Sonnet |
| Capability-First Analysis | Ambiguous or complex work needs the highest quality ceiling | Test Opus |
| Minimum Qualified Model | Several models may meet the requirement | Select the fastest, least costly passing model |
| Escalation Cascade | Most cases are easy but some are difficult | Route by observable failure signals |
| Quality Floor Before Cost | Cost optimization could hide unacceptable failures | Define the quality threshold first |
| Version-Pinned Deployment | Reproducibility and change control matter | Record exact model configuration |
| Controlled Migration | A new model version may regress important cases | Compare on the same evaluation set |
| Diagnose Before Upgrade | Poor performance may come from another system layer | Fix the actual root cause |
| Model Does Not Replace Controls | A stronger model is being treated as a safety mechanism | Preserve grounding, execution, and review |

---

## Pattern 1: Structured Volume

### Problem

A large number of routine items must be classified, extracted, summarized, routed, or reformatted.

### Context

Use this pattern when:

- the task has a narrow schema;
- examples are representative;
- ambiguity is low;
- volume is high;
- latency or cost compounds across requests;
- deterministic validation is available; and
- exceptions can be routed elsewhere.

### Design

Start with Haiku or the current efficiency-oriented model.

Validate:

- field accuracy;
- precision and recall;
- schema validity;
- exception rate;
- latency;
- cost per accepted output; and
- severe edge-case failures.

### Control

Route uncertain, malformed, high-risk, or out-of-distribution cases to a stronger model or human review.

### Decision rule

> Use an efficiency tier for structured volume only after it passes the actual quality threshold.

---

## Pattern 2: Balanced Professional Default

### Problem

A professional workflow needs strong drafting, synthesis, analysis, or document review without clear evidence that the highest tier is required.

### Design

Start with Sonnet or the current balanced model.

Evaluate whether it satisfies:

- factual accuracy;
- completeness;
- instruction following;
- grounding;
- organization;
- edge-case handling;
- revision burden; and
- latency target.

### Adjustment

- Downgrade structured sub-tasks when Haiku passes.
- Upgrade difficult exceptions when Sonnet fails material requirements.

### Decision rule

> Sonnet is a baseline hypothesis for professional work, not an exemption from evaluation.

---

## Pattern 3: Capability-First Analysis

### Problem

The task includes ambiguous evidence, multiple interacting constraints, long chains of reasoning, nuanced judgment, or expensive revision.

### Design

Start by testing Opus or the current high-capability tier.

Strong signals include:

- conflicting sources;
- incomplete information requiring careful interpretation;
- several stakeholder objectives;
- complex strategy;
- difficult technical analysis;
- long-horizon planning;
- high-consequence synthesis; and
- repeated lower-tier failure on representative tests.

### Control

Preserve:

- authoritative evidence;
- uncertainty labeling;
- deterministic checks;
- human expert review; and
- rollback to a validated workflow.

### Decision rule

> Use higher capability when reasoning quality is the bottleneck, not merely because the task is important.

---

## Pattern 4: Minimum Qualified Model

### Problem

Teams select either the cheapest model or the strongest model without identifying the minimum capability required.

### Design

1. Define the quality floor.
2. Build representative tests.
3. Hold prompts, tools, sources, and rubrics constant.
4. Compare candidate models.
5. Weight severe failures more than stylistic differences.
6. Select the fastest and least costly model that passes.
7. Monitor continued performance.

### Decision rule

> Optimize cost and latency only after the model clears the required quality floor.

---

## Pattern 5: Escalation Cascade

### Problem

One model tier is used for every case even though the workload contains both routine items and difficult exceptions.

### Design

```text
Routine item
    |
    v
Efficiency tier
    |
    +-- Passes external checks --------> Accept
    |
    +-- Fails or ambiguous ------------> Balanced tier
                                           |
                                           +-- High-risk exception --> High-capability tier
                                                                       |
                                                                       v
                                                                  Human review
```

### Routing signals

Use observable signals such as:

- missing fields;
- schema failure;
- conflicting evidence;
- evaluator score below threshold;
- high-risk classification;
- tool failure;
- out-of-distribution input;
- unresolved ambiguity; and
- repeated inconsistency.

### Anti-signal

Do not route solely from the model's own confidence statement.

### Decision rule

> Route based on validated difficulty and risk signals, not model self-assurance.

---

## Pattern 6: Quality Floor Before Cost

### Problem

A lower-cost model looks attractive, but the workflow has not defined what failure is unacceptable.

### Design

Define:

- required average quality;
- maximum severe-failure rate;
- minimum precision or recall;
- schema-validity threshold;
- maximum human revision time;
- edge-case requirements;
- abstention behavior; and
- escalation coverage.

Only then compare:

- token cost;
- usage headroom;
- latency;
- throughput; and
- operational complexity.

### Decision rule

> Cheap failure is still failure.

---

## Pattern 7: Version-Pinned Deployment

### Problem

A production result cannot be reproduced because the team recorded a family name but not the exact model configuration.

### Design

Record:

- model ID and version;
- provider and endpoint;
- effort or thinking settings;
- prompt version;
- tool definitions;
- source-set version;
- retrieval settings;
- output schema;
- evaluation version; and
- rollout date.

### Decision rule

> A model family is a category. A reproducible deployment requires an exact configuration.

---

## Pattern 8: Controlled Migration

### Problem

A new model appears to be an upgrade, so the team changes it without regression testing.

### Design

1. Freeze the baseline workflow.
2. Run the current and candidate models on the same cases.
3. Compare quality, latency, cost, schema validity, tool use, refusal behavior, and human revision.
4. Inspect severe failures.
5. Roll out in stages.
6. Monitor and retain rollback.

### Anti-pattern

Do not simultaneously change:

- model;
- prompts;
- tools;
- retrieval;
- source material; and
- evaluation criteria.

### Decision rule

> Treat a model change as a controlled system change, not a drop-in replacement.

---

## Pattern 9: Diagnose Before Upgrade

### Problem

A poor answer is assumed to prove that the model is underpowered.

### Competing root causes

- missing current evidence;
- stale Project knowledge;
- contradictory instructions;
- context overload;
- weak output schema;
- missing Code Execution;
- tool failure;
- retrieval error;
- unauthorized or incomplete data;
- poor evaluation; or
- missing human review.

### Design

Test each plausible cause before upgrading the model.

### Decision rule

> Upgrade only when capability is the demonstrated bottleneck.

---

## Pattern 10: Model Does Not Replace Controls

### Problem

A higher-tier model is treated as a substitute for workflow controls.

### Design

Keep the appropriate controls:

| Requirement | Control |
|---|---|
| Current factual accuracy | Authoritative sources, web search, Research, or retrieval |
| Correct calculations | Code Execution plus method validation |
| Structured output | Schema validation |
| Data authorization | Access control and policy |
| High-consequence decision | Qualified human review |
| Repeatable procedure | Skill and tests |
| Persistent context | Curated Project knowledge and instructions |
| Cross-session preference | Appropriately scoped Memory |

### Decision rule

> Capability improves the candidate output. Controls determine whether the output is safe and fit for use.

---

## Model-selection anti-patterns

### Prestige routing

Always selecting the strongest model because it appears more professional.

### Cost-first routing

Selecting the cheapest model before defining the quality requirement.

### One-tier architecture

Using one model for routine, ambiguous, and high-risk cases without routing.

### Self-confidence routing

Escalating only when the model says it is uncertain.

### Unpinned production

Recording only a tier name while model behavior changes underneath the workflow.

### Benchmark-only selection

Using public benchmark scores instead of testing the actual prompts, sources, tools, and edge cases.

### Upgrade as troubleshooting

Changing models before investigating context, evidence, prompt, tool, or data failures.

## Model-selection checklist

1. What is the task and output contract?
2. How structured or ambiguous are the inputs?
3. What is the consequence of error?
4. What is the request volume?
5. What latency is acceptable?
6. What is the quality floor?
7. What severe failures matter most?
8. Which candidate models will be tested?
9. What remains constant during comparison?
10. What triggers escalation?
11. What controls remain outside the model?
12. What exact version and settings will be deployed?
13. How will performance and cost be monitored?
14. What triggers rollback or requalification?

## Related material

- [Choosing Models lesson](../modules/01-platform-model-foundations/lessons/05-choosing-models.md)
- [Choosing Models prompt notebook](../prompts/module-01/05-choosing-models-prompts.md)
- [Capability patterns](capability-patterns.md)
- [Memory patterns](memory-patterns.md)

## Version-awareness note

The certification's Haiku, Sonnet, and Opus logic is durable, but current model names, versions, pricing, latency, context limits, effort controls, plan availability, and defaults can change. Verify current official Anthropic documentation before deployment.