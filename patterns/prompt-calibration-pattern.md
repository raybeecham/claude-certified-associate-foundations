# Prompt Calibration Pattern

## Pattern summary

Use enough specification to protect validity and usability, but preserve latitude where variation improves the result.

```text
Under-specified → Minimum sufficient specification → Over-specified
```

## Problem

Prompt quality can fail in two directions.

An under-specified prompt forces the model to infer the audience, task, scope, evidence, constraints, or output shape.

An over-specified prompt controls dimensions that should remain flexible, producing stiff drafts, repetitive ideas, premature convergence, or unnecessary complexity.

The common mistake is assuming that every weak output needs more detail.

## Context

Use this pattern when:

- a prompt produces generic or off-target output;
- a draft is accurate but mechanical;
- brainstorming lacks variety;
- a research task is unfocused;
- analysis is opinionated or unsupported;
- iterations keep adding detail without improving usability; or
- several prompt components are present but the task strategy still feels wrong.

## Forces

The design must balance:

- validity versus creative range;
- repeatability versus natural variation;
- completeness versus cognitive and context load;
- control versus adaptability;
- early exploration versus final selection; and
- prompt complexity versus maintenance cost.

## Recommended design

### Step 1: Identify the dominant task type

Classify the current stage as:

- analysis;
- research;
- drafting;
- brainstorming;
- extraction;
- classification;
- planning; or
- another bounded task.

Hybrid tasks should usually be decomposed before calibration.

### Step 2: Identify validity controls

Ask what must be true for the output to be acceptable.

Examples:

| Task type | Validity controls |
|---|---|
| Analysis | Criteria, evidence, scope, ambiguity handling |
| Research | Question, sources, currency, citations, verification |
| Drafting | Audience, purpose, approved facts, tone, format |
| Brainstorming | Goal, hard boundaries, requested range |
| Extraction | Source, field definitions, schema, missing-data behavior |
| Classification | Taxonomy, examples, uncertain-case handling |

### Step 3: Identify useful latitude

Ask where variation adds value.

Examples:

- phrasing in analysis;
- search path and synthesis in research;
- sentence construction in drafting;
- direction and novelty in brainstorming;
- ordering of equivalent items; and
- alternative options during planning.

### Step 4: Diagnose the calibration state

```text
If essential validity controls are missing → Under-specified
If validity is protected and latitude remains → Calibrated
If nonessential controls suppress useful variation → Over-specified
```

### Step 5: Make the smallest repair

For under-specification:

- sharpen the task;
- add missing context;
- define scope;
- establish an evidence boundary;
- add a necessary constraint; or
- specify the output contract.

For over-specification:

- remove decorative role language;
- loosen sentence-level rules;
- defer final-selection filters;
- separate divergence from convergence;
- remove redundant constraints; or
- decompose the work into stages with different control levels.

### Step 6: Validate the effect

Check whether the repair:

- improves the target quality dimension;
- preserves working requirements;
- avoids new ambiguity;
- avoids unnecessary rigidity; and
- reduces editing or review burden.

## Calibration continuum

| State | Prompt behavior | Likely output | Repair direction |
|---|---|---|---|
| Under-specified | Critical details remain implicit | Generic, broad, misprioritized, or incorrectly shaped | Add targeted control |
| Calibrated | Validity controls are explicit and useful latitude remains | Usable, task-appropriate output | Preserve and evaluate |
| Over-specified | Nonessential rules constrain exploration or phrasing | Stiff, repetitive, narrow, or overfit output | Remove or defer control |

## Divergence-convergence pattern

Brainstorming often needs two prompt states rather than one compromise prompt.

```text
Divergence
Goal + hard guardrails + volume + range
        ↓
Idea pool
        ↓
Convergence
Criteria + filtering + ranking + development
```

Do not force final-stage feasibility, ranking, and brand filters into the first generation pass unless they are true non-negotiable boundaries.

## Example

### Over-specified

```text
Generate five campaign concepts. Each must use the same five-word headline pattern, fit all twelve final evaluation criteria, be immediately feasible, and be ranked while generated.
```

### Calibrated divergence

```text
Generate 25 distinct campaign concepts for operations leaders.

Hard guardrails:
- do not make unsupported numerical claims;
- avoid fear-based messaging; and
- remain relevant to reporting efficiency.

Range across practical, aspirational, educational, and contrarian angles. Do not rank or eliminate ideas yet.
```

### Separate convergence

```text
Evaluate the 25 concepts against audience relevance, differentiation, credibility, and implementation effort. Shortlist five and explain the trade-offs.
```

## Failure modes

### More-detail reflex

Adding details without diagnosing the failure increases prompt length but not quality.

### Constraint accumulation

Every revision adds rules, but no obsolete or redundant rule is removed.

### Premature convergence

The model must generate and reject ideas in the same first pass.

### Decorative specificity

Verbose roles and instructions create the appearance of precision without changing the task.

### Uniform control

The same tight prompt style is applied to analysis, research, drafting, and brainstorming.

### No acceptance test

The prompt is changed without checking whether the target symptom improved.

## Controls

- Define the target quality dimension before revising.
- Change one significant variable at a time when practical.
- Preserve validated content and requirements.
- Separate hard boundaries from preferences.
- Mark constraints as `now`, `later`, or `never needed`.
- Use representative outputs to compare calibration choices.
- Stop when additional specification adds more maintenance than value.

## Decision rule

> Tighten what determines validity. Loosen what benefits from variation.

## Compact checklist

```text
What task type is this?
What must be controlled?
What may vary?
Is the prompt under-specified or over-specified?
What one change would improve calibration most?
What working elements must remain unchanged?
How will I verify the repair?
```

## Related patterns

- [Task Strategy Fit Pattern](task-strategy-fit-pattern.md)
- [Failure Localization Pattern](failure-localization-pattern.md)
- [Task Specification Before Prompting](task-specification-before-prompting.md)
