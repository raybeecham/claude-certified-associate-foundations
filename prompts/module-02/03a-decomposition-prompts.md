# Module 2 — Task Decomposition Prompts

Use fictional, synthetic, public, or explicitly authorized information.

## 1. Hidden-task detector

```text
Analyze the request below and identify every distinct task hidden inside it.
For each task, name the primary verb, input, output, and success criterion.
Then recommend whether the work should remain one task or be decomposed.

Request:
[PASTE REQUEST]
```

## 2. Sequential workflow builder

```text
Turn the request below into the smallest useful sequence of dependent stages.
For each stage specify:
- objective;
- input;
- process;
- output;
- validation;
- dependency; and
- human approval point, if needed.

Request:
[PASTE REQUEST]
```

## 3. Pipeline rule audit

```text
Review this proposed workflow using the pipeline rule:
Input → Process → Output → Validation.
Identify missing handoffs, ambiguous outputs, and validation gaps.

Workflow:
[PASTE WORKFLOW]
```

## 4. Vendor-evaluation decomposition

```text
Design a four-stage vendor evaluation workflow:
1. derive criteria;
2. score vendors;
3. analyze trade-offs;
4. recommend.

Use only the supplied requirements and vendor materials.
Define stage outputs, evidence rules, validation gates, and final human decision authority.
```

## 5. Over-decomposition check

```text
Review the workflow below for unnecessary fragmentation.
Identify stages that share the same objective, evidence, method, and validation and could be merged safely.
Also identify stages that must remain separate.

Workflow:
[PASTE WORKFLOW]
```

## 6. Conversation-boundary planner

```text
For each workflow stage below, recommend whether it should:
- remain in the same conversation;
- begin in a clean conversation; or
- run in an independent parallel context.

Base the decision on dependency, context degradation, trusted sources, permissions, and anchoring risk.

Stages:
[PASTE STAGES]
```

## 7. Failure-localization exercise

```text
A final recommendation is poor.
Trace which upstream stage most likely failed based on the symptoms below.
Explain what should be rerun and what downstream work must be invalidated.

Workflow:
[PASTE WORKFLOW]
Symptoms:
[DESCRIBE FAILURE]
```

## 8. Deterministic boundary finder

```text
Identify which stages in this AI workflow should use generative reasoning and which should use deterministic computation or validation.
Explain every boundary.

Workflow:
[PASTE WORKFLOW]
```

## 9. Decomposition comparison

```text
Create two designs for this request:
1. a single-prompt version;
2. a decomposed workflow.

Compare auditability, error propagation, context load, latency, cost, and review burden.

Request:
[PASTE REQUEST]
```

## 10. Teach-back

```text
Teach task decomposition to a colleague using one business example.
Explain:
- why the single prompt underperforms;
- how stages are selected;
- why intermediate outputs matter;
- when to keep stages together or separate; and
- the danger of over-decomposition.
```
