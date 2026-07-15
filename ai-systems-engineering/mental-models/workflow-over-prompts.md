# Workflow Over Prompts

## The mistake

Treating every AI problem as a wording problem leads to endless prompt edits while larger system defects remain untouched.

A prompt cannot repair:

- missing evidence;
- unauthorized data;
- the wrong model;
- an unsuitable workspace;
- absent deterministic checks;
- uncontrolled tools;
- degraded context; or
- missing approval.

## The better model

```text
Business outcome
      ↓
Workflow architecture
      ↓
Evidence and state
      ↓
Model, tools, and controls
      ↓
Prompt
      ↓
Validation and decision
```

The prompt is an interface between the workflow and the model. It should express decisions already made elsewhere.

## Diagnostic questions

When output is weak, ask in this order:

1. Is the objective clear?
2. Is the evidence sufficient and current?
3. Is the task assigned to the right component?
4. Is the model qualified for the task?
5. Is context focused and consistent?
6. Is the prompt clear?
7. Are validation and escalation adequate?

## Example

Problem: a monthly financial report contains incorrect figures.

Weak response:

> Add “double-check every number” to the prompt.

Engineering response:

- move calculations to code;
- define formulas and units;
- reconcile source totals;
- preserve an audit trail;
- keep narrative generation separate; and
- require review before publication.

## Decision rule

> Change the prompt when the failure is instructional. Change the system when the failure is architectural.

## Practical habit

Before editing a prompt, classify the failure:

- objective;
- evidence;
- capability;
- model;
- context;
- instruction;
- validation;
- governance; or
- operation.

Then change one relevant variable and retest.
