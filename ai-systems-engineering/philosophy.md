# Philosophy

## AI work is system design

A prompt is an instruction inside a larger system. The quality of the final result depends on the full chain surrounding that instruction.

```text
Business need
     ↓
Authorized evidence
     ↓
Workspace and capabilities
     ↓
Model and tools
     ↓
Context and prompt
     ↓
Candidate output
     ↓
Validation and review
     ↓
Decision or action
```

The prompt matters, but it is not the system.

## The mindset shift

Beginner question:

> What prompt should I write?

Engineering question:

> What system should produce, constrain, verify, and use the output?

The second question produces better prompts because it resolves the important decisions first.

## Five beliefs

### 1. The business outcome is the unit of design

Do not optimize for an impressive response. Optimize for an outcome such as:

- a supported decision;
- an accurate classification;
- a reviewed deliverable;
- a reconciled dataset;
- a tested code change; or
- a safe escalation.

### 2. Generative and deterministic components have different jobs

Use generative models for work such as:

- interpretation;
- synthesis;
- drafting;
- classification;
- planning;
- explanation; and
- option generation.

Use deterministic components for work such as:

- arithmetic;
- schema enforcement;
- identity and authorization;
- business-rule enforcement;
- current operational state;
- side effects;
- audit logging; and
- release gates.

### 3. Context is selected, not accumulated

More context is not automatically better. The goal is the smallest authorized, relevant, current, and authoritative context needed for the next action.

### 4. Capability must be earned by evaluation

Do not choose the cheapest model by default. Do not choose the strongest model by default. Define the quality floor and select the minimum configuration that passes representative tests.

### 5. Review scales with consequence

Low-consequence brainstorming may need only user judgment. A consequential analytical or operational result may require:

- source verification;
- deterministic checks;
- a second reviewer;
- subject-matter expertise;
- formal approval; or
- a prohibition on autonomous action.

## What this playbook is not

It is not:

- a collection of magic prompts;
- a promise that one platform fits every use case;
- a substitute for legal, security, privacy, or domain expertise;
- a justification for uploading unauthorized data;
- a claim that human review fixes every design flaw; or
- a framework for maximizing autonomy.

It is a method for making explicit, testable engineering decisions.

## The operating principle

> Do not optimize the prompt first. Optimize the system that produces, constrains, validates, and uses the prompt.

## Practical definition

**AI systems engineering** is the disciplined design of workflows that combine generative models, data, instructions, tools, deterministic controls, evaluation, and human responsibility to achieve a measurable outcome.

## Definition of done

An AI workflow is not done merely because it produces an answer. It is done when:

- the business objective is satisfied;
- the evidence is authorized and sufficient;
- the output passes defined checks;
- risks and uncertainty are visible;
- ownership and approval are clear;
- the result can be reproduced or explained; and
- the workflow can be monitored, corrected, and retired.
