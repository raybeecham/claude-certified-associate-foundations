# Module 1 Prompt Notebook: Capability Layer Scenario

These prompts help analyze and redesign recurring professional workflows using Projects, Skills, Code Execution, Memory, and human review. Use only fictional, synthetic, public, or authorized information.

## 1. Recurring workflow decomposition

### Use when

A repeated task is being rebuilt from scratch in every Chat.

```text
Act as an AI workflow architect.

Recurring task:
[DESCRIBE TASK]

Current monthly or recurring process:
[DESCRIBE PROCESS]

Separate the workflow into:
- stable background context;
- reusable reference material;
- standing workstream rules;
- repeatable procedure;
- current-cycle inputs;
- deterministic calculations or transformations;
- appropriate cross-session continuity;
- authoritative systems of record;
- human judgments; and
- approval or verification controls.

For each item, recommend the correct home:
- Project knowledge;
- Project instructions;
- Skill;
- Code Execution;
- Memory;
- current conversation;
- external authoritative system;
- human review; or
- exclude.

Return a migration table and target-state architecture.
```

## 2. Capability-layer redesign plan

### Use when

You want an end-to-end design for a recurring high-consequence workflow.

```text
Redesign the following workflow using only the capability layers justified by the requirements.

Workflow:
[DESCRIBE WORKFLOW]

Requirements:
[LIST REQUIREMENTS]

For Project, Skill, Code Execution, Memory, and human review, state:
1. whether it is needed;
2. the requirement it addresses;
3. what belongs in that layer;
4. what must not be placed there;
5. owner;
6. maintenance cadence;
7. risks;
8. controls;
9. validation method; and
10. exit or rollback condition.

Prefer the least complex architecture that preserves accuracy, traceability, and accountability.
```

## 3. Stable-versus-variable classifier

### Use when

A prompt mixes durable configuration with current task details.

```text
Classify every requirement and input below as stable, slowly changing, or cycle-specific.

Content:
[PASTE CONTENT]

For each item, return:
- classification;
- expected lifetime;
- source of truth;
- recommended storage layer;
- review cadence;
- risk if stale; and
- action.

Use these placement rules:
- stable workstream context -> Project;
- repeatable procedure -> Skill;
- current-cycle evidence -> current conversation;
- calculation or transformation -> Code Execution;
- general cross-session preference -> Memory, when appropriate;
- authoritative operational state -> external record.
```

## 4. Project configuration builder

### Use when

Stable context and report requirements need to be moved from repeated prompts into a Project.

```text
Build a Project configuration for this recurring workflow.

Workflow purpose:
[PURPOSE]

Stable background:
[BACKGROUND]

Authorized reusable sources:
[SOURCES]

Audience and output requirements:
[REQUIREMENTS]

Create:
1. concise Project standing instructions;
2. proposed knowledge-base inventory;
3. source hierarchy;
4. terminology rules;
5. missing-evidence behavior;
6. escalation thresholds;
7. review requirements;
8. document versioning and refresh rules; and
9. a list of temporary details that must remain outside the Project configuration.
```

## 5. Skill procedure builder for recurring reports

### Use when

The same analytical and formatting procedure repeats every cycle.

```text
Design a reusable Skill specification for this recurring report.

Inputs:
[INPUTS]

Required analysis:
[ANALYSIS]

Required output:
[OUTPUT]

Define:
- trigger conditions;
- required inputs and precondition checks;
- ordered analytical steps;
- source restrictions;
- applicability or classification criteria;
- calculations that must be routed to Code Execution;
- missing-data behavior;
- required sections and schema;
- escalation conditions;
- prohibited assumptions;
- review checklist;
- allowed variation; and
- invariants that must remain consistent.

Do not claim the Skill guarantees correctness.
```

## 6. Code Execution and reconciliation plan

### Use when

Numeric figures or data transformations appear in a consequential report.

```text
Create a Code Execution plan for the following calculations and data transformations.

Inputs:
[DESCRIBE INPUTS]

Required outputs:
[DESCRIBE OUTPUTS]

Before execution, define:
- data source and authorization;
- schema and row-count checks;
- formulas;
- units;
- business keys;
- missing-value handling;
- duplicate handling;
- assumptions;
- known-case tests; and
- acceptance criteria.

After execution, require:
- results;
- code or formula summary;
- before-and-after reconciliation;
- excluded records;
- warnings and exceptions;
- validation results; and
- generated files.

Do not silently discard data or infer missing values.
```

## 7. Prior-report knowledge-base review

### Use when

Historical reports are proposed as reusable Project knowledge.

```text
Review the following prior reports before adding them to a Project knowledge base.

Reports:
[LIST REPORTS]

For each report, evaluate:
- approval status;
- reporting period;
- authority;
- sensitivity;
- current relevance;
- superseded content;
- known errors;
- usefulness as a format example;
- risk of stale conclusions influencing current work;
- retention period; and
- recommended action.

Classify each as:
- include as approved historical reference;
- include only as format example;
- replace with a newer version;
- archive outside active knowledge;
- exclude; or
- requires owner review.
```

## 8. Verification-control designer

### Use when

Automation is being added but review controls must remain explicit.

```text
Design a verification and approval plan for this recurring workflow.

Workflow:
[DESCRIBE WORKFLOW]

Consequences of error:
[DESCRIBE CONSEQUENCES]

Define controls for:
- source authority and freshness;
- input completeness;
- classification or applicability judgments;
- calculations and reconciliation;
- unsupported assumptions;
- exception handling;
- output completeness;
- reviewer accountability;
- approval evidence;
- escalation; and
- post-publication correction.

Separate automated checks from human judgments. Explain why each human review step remains necessary.
```

## 9. Workflow performance measurement plan

### Use when

You need to determine whether a redesigned workflow is actually better.

```text
Create a measurement plan comparing the current and redesigned workflows.

Current workflow:
[DESCRIBE]

Redesigned workflow:
[DESCRIBE]

Track at least:
- total cycle time;
- repeated setup time;
- analyst effort;
- reviewer effort;
- detected error rate;
- escaped error rate;
- verification coverage;
- unresolved-evidence count;
- reviewer overrides;
- stale-source findings;
- computation reconciliation failures;
- rework; and
- maintenance overhead.

For each metric, define:
- formula;
- data source;
- owner;
- collection cadence;
- baseline;
- target;
- warning threshold; and
- decision rule.

Do not interpret an error-free observation period as proof of permanent correctness.
```

## 10. Time-savings and break-even calculator

### Use when

You need a simple business case for a capability-layer redesign.

```text
Use Code Execution to calculate the operational impact of this workflow redesign.

Original time per cycle:
[MINUTES]

Redesigned time per cycle:
[MINUTES]

Cycles per year:
[NUMBER]

One-time setup effort:
[MINUTES OR HOURS]

Ongoing maintenance per cycle:
[MINUTES]

Calculate:
- gross time saved per cycle;
- percentage reduction;
- annual gross savings;
- annual maintenance cost;
- annual net savings;
- number of cycles to break even; and
- first-year net benefit.

State all formulas and assumptions. Return a summary table and sensitivity analysis for low, expected, and high adoption cases.
```

## 11. Zero-error-period interpretation

### Use when

A workflow has completed several cycles without detected errors.

```text
Evaluate the following performance claim:

Claim:
[PASTE CLAIM]

Observation period:
[PERIOD]

Number of completed cycles:
[NUMBER]

Verification method:
[DESCRIBE]

Explain:
- what the evidence supports;
- what it does not prove;
- whether sample size is sufficient for any conclusion;
- possible undetected errors;
- changes that could invalidate the result;
- controls that should remain;
- additional metrics needed; and
- wording that accurately communicates the result without overclaiming.
```

## 12. Capability-layer scenario practice

### Use when

You want to practice certification-style selection reasoning.

```text
Create five original scenario questions about a recurring professional workflow that may need Projects, Skills, Code Execution, Memory, and human review.

Requirements:
- do not copy certification or course questions;
- use fictional or public scenarios;
- include four answer choices;
- make at least two distractors plausible;
- provide the correct answer;
- explain why it is correct;
- explain why every distractor is weaker; and
- identify the requirement that points to each capability layer.
```

## Scenario design checklist

Before accepting a layered design, verify:

1. Stable context has a maintained owner.
2. Project knowledge is curated, authorized, and current.
3. The Skill defines procedure rather than temporary facts.
4. Code Execution includes method validation and reconciliation.
5. Memory contains only appropriate continuity.
6. Current-cycle evidence remains current-cycle input.
7. Authoritative facts remain in authoritative systems.
8. Human review remains where consequence or uncertainty requires it.
9. Metrics cover both speed and quality.
10. Rollback, correction, and maintenance are defined.

## Related material

- [Capability Layer scenario](../../modules/01-platform-model-foundations/lessons/04b-capability-layer-scenario.md)
- [Skills and Code Execution](../../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)
- [Memory](../../modules/01-platform-model-foundations/lessons/04a-capability-layer-memory.md)
- [Capability patterns](../../patterns/capability-patterns.md)
- [Memory patterns](../../patterns/memory-patterns.md)
