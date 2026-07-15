# Module 1 Prompt Notebook: Capability Layer Checkpoint

These prompts help classify workflow components into Project standing instructions, Project knowledge, Skills, Code Execution, current task inputs, and human review.

Use only fictional, synthetic, public, or authorized information.

## 1. Capability placement classifier

### Use when

A workflow contains mixed instructions, documents, procedures, and calculations.

```text
Classify each workflow component into the narrowest appropriate layer:

- Project standing instructions;
- Project knowledge;
- Skill;
- Code Execution;
- current task input;
- Memory;
- authoritative external system;
- human review; or
- exclude.

Components:
[PASTE COMPONENTS]

For each component, return:
- classification;
- rationale;
- expected lifetime;
- scope;
- source or owner;
- sensitivity;
- validation requirement; and
- maintenance or deletion trigger.

Apply these distinctions:
- standing instructions define durable workstream behavior;
- Project knowledge supplies curated reusable evidence;
- Skills define repeatable procedures;
- Code Execution performs calculations or transformations;
- current task input applies only to this cycle;
- human review owns consequential judgment.
```

## 2. Standing instructions versus knowledge review

### Use when

Project configuration mixes behavioral rules with source material.

```text
Separate the content below into:

1. Project standing instructions;
2. Project knowledge;
3. current-cycle task inputs;
4. reusable Skill procedure;
5. Code Execution operations; and
6. content that should not be retained.

Content:
[PASTE CONTENT]

For every item, explain whether it defines:
- how Claude should behave;
- what Claude should know;
- what Claude should analyze now;
- how the recurring task should be performed; or
- what must be computed.

Flag any current-cycle document that is being retained as permanent knowledge without a clear authorization or lifecycle need.
```

## 3. Contract-review workflow architect

### Use when

A recurring contract-review process should be redesigned using capability layers.

```text
Design a governed contract-review workflow using:
- Project standing instructions;
- Project knowledge;
- a reusable Skill;
- Code Execution;
- current-cycle contract inputs; and
- qualified human review.

Review purpose:
[PURPOSE]

Approved playbook or reference set:
[REFERENCES]

Required report:
[OUTPUT]

Potential calculations:
[CALCULATIONS]

Define:
1. what belongs in standing instructions;
2. what belongs in Project knowledge;
3. what remains cycle-specific;
4. the ordered Skill procedure;
5. which calculations use Code Execution;
6. source and citation rules;
7. privacy and retention controls;
8. escalation conditions;
9. human approval responsibilities; and
10. acceptance criteria.

Do not claim that Claude provides final legal advice.
```

## 4. Contract-review Skill builder

### Use when

The same extraction, comparison, classification, and reporting procedure repeats.

```text
Create a reusable Skill specification for a contract-review procedure.

Authorized inputs:
[INPUTS]

Approved playbook:
[PLAYBOOK]

Required output:
[OUTPUT]

Define:
- trigger conditions;
- required inputs;
- precondition checks;
- clause extraction method;
- comparison procedure;
- risk classification rules;
- evidence and quotation requirements;
- calculations routed to Code Execution;
- missing-data behavior;
- escalation conditions;
- prohibited assumptions;
- output schema;
- human-review checklist;
- invariants; and
- allowed variation.

The procedure should support qualified review, not replace it.
```

## 5. Variable-rate exposure calculation plan

### Use when

A contract contains a penalty, fee, credit, or adjustment that depends on multiple variables.

```text
Create a Code Execution plan for the following variable-rate contract calculation.

Clause text:
[CLAUSE]

Authorized input values:
[INPUTS]

Before calculating:
1. identify variables, units, dates, tiers, caps, floors, and trigger conditions;
2. separate explicit clause terms from assumptions;
3. identify ambiguous language requiring qualified review;
4. define the formula or algorithm;
5. define boundary and known-case tests; and
6. define reconciliation checks.

After execution, return:
- clause interpretation used;
- formula;
- inputs;
- intermediate results;
- final result;
- boundary tests;
- assumptions;
- exceptions;
- reproducibility notes; and
- required human validation.

Stop rather than inventing a method when the clause is ambiguous.
```

## 6. Source-material lifecycle review

### Use when

A Project is accumulating every document ever analyzed.

```text
Review the following Project document inventory.

Inventory:
[PASTE INVENTORY]

Classify each item as:
- retain as approved reusable Project knowledge;
- retain temporarily for the active review cycle;
- archive outside Claude in the authoritative record system;
- replace with a current version;
- remove as duplicate;
- remove as stale;
- remove as unauthorized or sensitive; or
- requires owner review.

Return:
- classification;
- authority;
- scope;
- sensitivity;
- retention basis;
- expiration or review date;
- risk if stale; and
- action.

Do not assume that every reviewed document belongs in permanent Project knowledge.
```

## 7. Human-review boundary designer

### Use when

Automation has been added to a consequential review process.

```text
Define the human-review boundary for this workflow.

Workflow:
[DESCRIBE WORKFLOW]

Identify:
- decisions Claude may draft;
- decisions Claude may not finalize;
- calculations requiring independent validation;
- ambiguous clauses requiring specialist review;
- high-risk departures requiring escalation;
- evidence the reviewer must inspect;
- reviewer qualifications;
- required approval record;
- override documentation; and
- stop conditions.

Return a RACI-style responsibility table and final approval checklist.
```

## 8. Generate new capability-layer checkpoint questions

### Use when

You want more original practice without reproducing course or exam questions.

```text
Create 10 original scenario-based practice questions on capability-layer placement.

Test these distinctions:
- standing instructions versus Project knowledge;
- Project knowledge versus current-cycle input;
- Project instructions versus Skill;
- language generation versus Code Execution;
- Memory versus Project configuration;
- automation versus human accountability.

Requirements:
- use fictional professional scenarios;
- do not reproduce proprietary course or exam wording;
- include four answer options;
- identify the correct answer;
- explain why it is correct;
- explain why each distractor is wrong; and
- vary difficulty from basic to advanced.
```

## Suggested study exercise

1. Use prompt 1 on five workflow components from your own fictional scenario.
2. Use prompt 2 to test whether you can distinguish behavior from knowledge.
3. Use prompt 5 to examine why executed calculation still requires interpretation review.
4. Use prompt 8 to create a fresh practice set and score yourself without notes.

## Related material

- [Capability Layer checkpoint](../../modules/01-platform-model-foundations/lessons/04c-capability-layer-checkpoint.md)
- [Skills and Code Execution prompts](04-capability-layer-skills-code-execution-prompts.md)
- [Memory prompts](04a-capability-layer-memory-prompts.md)
- [Capability Layer scenario prompts](04b-capability-layer-scenario-prompts.md)
- [Capability patterns](../../patterns/capability-patterns.md)
