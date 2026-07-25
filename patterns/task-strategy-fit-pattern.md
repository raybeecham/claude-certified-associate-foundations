# Task Strategy Fit Pattern

## Intent

Match the prompt's degree of control and creative latitude to the dominant task type.

## Problem

A single fixed prompting style performs poorly across different tasks.

- Analysis becomes vague when criteria and evidence are loose.
- Research becomes unreliable when scope, currency, and sources are weak.
- Drafting becomes stiff when every phrase is over-specified.
- Brainstorming becomes repetitive when evaluation begins before divergence.

The component stack remains useful, but each component should not receive the same emphasis in every task.

## Context

Use this pattern when designing or repairing prompts for:

- analysis;
- research;
- drafting;
- brainstorming; or
- workflows that combine several of these modes.

## Forces

The design must balance:

- reliability versus variation;
- source discipline versus synthesis freedom;
- consistency versus natural language;
- divergence versus feasibility;
- speed versus depth;
- task simplicity versus decomposition overhead; and
- model assistance versus human accountability.

## Solution

### Step 1: Identify the dominant task type

Ask what transformation the model must perform.

| Task type | Transformation |
|---|---|
| Analysis | Evidence into judgment |
| Research | Question into sourced evidence and synthesis |
| Drafting | Approved content into audience-specific communication |
| Brainstorming | Goal and boundaries into a broad option set |

### Step 2: Identify validity controls

Determine what must be constrained for the result to be usable.

```text
Validity controls may include:
criteria
sources
time boundary
factual inputs
audience
tone
format
hard guardrails
uncertainty behavior
```

### Step 3: Identify useful latitude

Determine where variation adds value.

```text
Useful latitude may include:
phrasing
organization
search path
synthesis approach
idea direction
novel combinations
```

### Step 4: Apply the task-specific posture

| Task type | Tighten | Loosen |
|---|---|---|
| Analysis | Criteria, evidence, standards, ambiguity rules | Phrasing |
| Research | Question, sources, dates, citations, verification | Search path and synthesis |
| Drafting | Audience, purpose, facts, tone, length, format | Word choice and transitions |
| Brainstorming | Goal, hard guardrails, volume, diversity dimensions | Direction and novelty |

### Step 5: Decompose hybrid requests

If a request contains more than one transformation, separate the stages.

```text
Research
   ↓
Validate evidence
   ↓
Analyze
   ↓
Brainstorm options
   ↓
Evaluate options
   ↓
Draft communication
```

Each stage receives its own strategy and validation gate.

### Step 6: Validate task-strategy fit

Check whether the output shows signs of over-constraint or under-constraint.

| Symptom | Likely condition |
|---|---|
| Generic judgment | Analysis under-constrained |
| Unsupported or stale claims | Research under-constrained |
| Mechanical prose | Drafting over-constrained |
| Repetitive ideas | Brainstorming over-constrained |
| Wildly irrelevant ideas | Brainstorming under-constrained |
| Shallow multi-part answer | Hybrid task not decomposed |

## Example

### Request

```text
Research recent market changes, identify strategic options, recommend one, and write an executive memo.
```

### Weak design

One prompt asks for all transformations at once.

### Pattern application

1. Research current evidence with source and date controls.
2. Validate the evidence set.
3. Analyze implications against explicit criteria.
4. Brainstorm options without ranking during the first ideation pass.
5. Evaluate options using approved criteria.
6. Draft the executive memo for the defined audience.
7. Perform source, consistency, and human review.

## Controls

- Use current retrieval when the task depends on changing facts.
- Require source traceability for research claims.
- Do not treat brainstormed ideas as validated facts or recommendations.
- Do not ask prose generation to perform consequential calculations.
- Preserve human responsibility for high-impact conclusions and publication.
- Verify feature availability and organizational permissions before relying on Search, Research, or connectors.

## Failure modes

### Maximum specificity everywhere

The prompt eliminates useful variation and produces rigid, repetitive outputs.

### Maximum creativity everywhere

The prompt produces unsupported analysis, unreliable research, and unusable deliverables.

### Task-label substitution

The prompt says “analyze” or “research” without defining what those operations require.

### Premature convergence

Brainstorming and ranking occur in the same first pass, suppressing range.

### Citation theater

The prompt asks for citations but provides no grounded source mechanism or verification step.

### Hybrid-task compression

Several distinct task modes are packed into one request, creating shallow treatment of each.

## Decision rule

> Tighten what determines validity. Loosen what benefits from variation.

## Compact checklist

```text
What is the dominant task type?
What must be controlled?
Where does variation help?
What evidence is required?
What happens when evidence is missing?
Does the task need decomposition?
How will the result be validated?
```

## Related material

- [Strategy by Task Type](../modules/02-prompting-task-execution/lessons/05a-strategy-by-task-type.md)
- [Task Specification Before Prompting](task-specification-before-prompting.md)
- [Failure Localization Pattern](failure-localization-pattern.md)
- [Task Strategy prompt notebook](../prompts/module-02/05a-strategy-by-task-type-prompts.md)
