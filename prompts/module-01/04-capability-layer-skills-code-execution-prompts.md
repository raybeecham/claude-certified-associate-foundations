# Module 1 Prompt Notebook: Capability Layer, Skills and Code Execution

These prompts help separate context, procedure, computation, and continuity. Replace bracketed fields with task-specific details and verify current feature availability, permissions, and workspace policy before use.

## 1. Capability-layer selector

### Use when

You need to determine which capability layers a task actually requires.

```text
Act as an AI workflow architect.

Task:
[DESCRIBE TASK]

Evaluate whether the workflow needs:
- Project;
- Skill;
- Code Execution;
- Memory;
- none; or
- a combination.

For each capability, state:
1. requirement it addresses;
2. information or procedure that belongs there;
3. information that should remain outside it;
4. setup and maintenance cost;
5. security and governance considerations;
6. validation still required; and
7. conditions that would change the recommendation.

Prefer the least complex combination that satisfies the task.
```

## 2. Context, procedure, computation, and continuity separator

### Use when

A workflow has accumulated one large prompt containing mixed concerns.

```text
Decompose the workflow below into four architectural concerns:

Workflow:
[DESCRIBE WORKFLOW OR PASTE CURRENT PROMPT]

Classify each requirement as:
- Project context or standing instruction;
- Skill procedure;
- Code Execution operation;
- Memory candidate;
- current conversation input;
- external authoritative record; or
- exclude.

Return a table with:
- requirement;
- classification;
- rationale;
- expected lifecycle;
- owner;
- sensitivity;
- validation; and
- migration action.

Flag any temporary fact that is incorrectly being made persistent.
```

## 3. Project versus Skill boundary review

### Use when

You are unsure whether instructions belong in a Project or a Skill.

```text
Review the following instructions and decide whether each belongs in:
- Project standing instructions;
- Project knowledge;
- a reusable Skill;
- the current task input; or
- nowhere.

Instructions and material:
[PASTE CONTENT]

Use this distinction:
- Project: what Claude should know and consistently honor for this workstream;
- Skill: how a recurring task should be executed;
- current input: what is true only for this task instance.

Return:
1. classification table;
2. proposed Project configuration;
3. proposed Skill outline;
4. temporary inputs; and
5. conflicts or duplication to remove.
```

## 4. Skill specification builder

### Use when

A repeated procedure should be formalized.

```text
Design a reusable Skill specification for this task.

Task type:
[TASK]

Users:
[USERS]

Authorized inputs:
[INPUTS]

Required outputs:
[OUTPUTS]

Define:
1. purpose and scope;
2. trigger conditions;
3. required inputs;
4. precondition checks;
5. ordered procedure;
6. source hierarchy;
7. prohibited assumptions;
8. missing-data behavior;
9. output schema;
10. formatting requirements;
11. deterministic checks;
12. escalation conditions;
13. human review requirements;
14. logging requirements;
15. privacy and security constraints; and
16. version and maintenance process.

Then separate:
- invariants;
- allowed variation;
- task-specific facts; and
- items that should remain outside the Skill.
```

## 5. Skill variance contract

### Use when

A Skill must produce consistent structure without requiring identical prose.

```text
Create a variance contract for the following Skill.

Skill:
[DESCRIBE SKILL]

Classify output properties as:
- invariant;
- allowed to vary within a defined range;
- grounded in current input;
- deterministically validated;
- human-reviewed; or
- prohibited.

Include:
- required sections;
- terminology;
- source restrictions;
- formatting;
- safety constraints;
- factual claims;
- calculations;
- examples;
- tone;
- recommendations; and
- uncertainty statements.

Return acceptance tests for each invariant property.
```

## 6. Skill trust and permission review

### Use when

A built-in, organization-provided, or third-party Skill is being considered.

```text
Perform a pre-enablement trust review for this Skill.

Skill name:
[NAME]

Creator and source:
[SOURCE]

Declared purpose:
[PURPOSE]

Instructions or code available for review:
[DETAILS]

Requested permissions:
[PERMISSIONS]

Potentially accessible data:
[DATA]

Evaluate:
- provenance and maintainer identity;
- source transparency;
- instruction or code integrity;
- update and versioning mechanism;
- requested permissions;
- least-privilege fit;
- file and connector access;
- external communication;
- data retention and logging;
- prompt-injection exposure;
- supply-chain risk;
- monitoring;
- incident response;
- revocation; and
- organizational approval.

Return:
1. risk rating;
2. approve, approve with restrictions, require further review, or reject;
3. required restrictions;
4. evidence gaps;
5. monitoring plan; and
6. re-review triggers.

Do not infer trust from branding or the Skill description alone.
```

## 7. Code Execution decision

### Use when

You need to decide whether a task should be handled through language generation or executed code.

```text
Determine whether this task should use Code Execution.

Task:
[DESCRIBE TASK]

Assess whether it includes:
- reported numeric output;
- calculations or projections;
- statistics;
- data cleaning or transformation;
- deduplication;
- joins or reconciliation;
- visualization;
- repetitive operations;
- supported file generation;
- reproducibility requirements; or
- audit requirements.

Return:
1. recommendation;
2. operations that should be executed;
3. operations that may remain language-only;
4. required inputs;
5. assumptions and units;
6. validation plan;
7. security and data-handling controls; and
8. acceptance criteria.
```

## 8. Verified computation request

### Use when

A numeric result will be used or reported.

```text
Use Code Execution for the following calculation.

Objective:
[OBJECTIVE]

Inputs:
[DATA OR FILES]

Required calculations:
[CALCULATIONS]

Before execution:
1. inspect the inputs;
2. state units and assumptions;
3. identify missing, invalid, or ambiguous values;
4. describe the method and formulas;
5. define expected checks; and
6. stop if the method cannot be justified.

During execution:
- preserve the original data;
- log transformations;
- do not silently discard records;
- report warnings and errors; and
- create reproducible code.

After execution, return:
- results;
- method summary;
- formulas or code summary;
- reconciliations;
- spot checks;
- exceptions;
- limitations; and
- generated outputs.
```

## 9. Data-cleaning and audit prompt

### Use when

A dataset must be transformed without losing traceability.

```text
Use Code Execution to clean the attached dataset.

Required operations:
[OPERATIONS]

First produce a data-quality profile containing:
- row and column counts;
- data types;
- missing values;
- invalid values;
- duplicate candidates;
- date and time formats;
- numeric ranges;
- category cardinality; and
- obvious anomalies.

Then propose the cleaning rules and wait for confirmation if any rule could remove or materially alter records.

After execution, produce:
1. cleaned dataset;
2. transformation log;
3. before-and-after reconciliation;
4. rejected or quarantined records;
5. assumptions;
6. code summary; and
7. audit report.

Do not impute, delete, merge, or overwrite ambiguous records silently.
```

## 10. Chart and visualization validator

### Use when

A chart will support a decision or published deliverable.

```text
Use Code Execution to create a visualization from the supplied data.

Decision the chart must support:
[DECISION]

Audience:
[AUDIENCE]

Before creating the chart:
- identify the correct measure and unit;
- confirm aggregation logic;
- check missing and excluded data;
- identify possible misleading scales;
- select the simplest suitable chart type; and
- define the source note.

After creating it, validate:
- labels;
- units;
- axis ranges;
- aggregation;
- sorting;
- accessibility;
- source attribution;
- consistency with the underlying data; and
- whether an alternative visual changes interpretation.

Return the chart, validation checklist, and any limitations.
```

## 11. Supported file-generation workflow

### Use when

The task requires a real editable file rather than prose describing one.

```text
Create the requested deliverable using the appropriate document capability and Code Execution where needed.

Deliverable type:
[SPREADSHEET, DOCUMENT, PRESENTATION, PDF, OR OTHER SUPPORTED FORMAT]

Purpose:
[PURPOSE]

Audience:
[AUDIENCE]

Source material:
[SOURCES]

Requirements:
[REQUIREMENTS]

Produce:
1. content and layout plan;
2. calculations or transformations that require execution;
3. generated editable file;
4. quality-control checklist;
5. source and assumption notes;
6. accessibility checks;
7. file-integrity checks; and
8. summary of what was created.

Do not claim a file was created unless an actual file is generated and validated.
```

## 12. Combined four-layer workflow architect

### Use when

A recurring analytical workflow may need all four capability layers.

```text
Design an end-to-end workflow using only the justified subset of:
- Project;
- Skill;
- Code Execution;
- Memory; and
- human review.

Use case:
[USE CASE]

For each layer, define:
- purpose;
- content or procedure stored there;
- lifecycle;
- owner;
- permissions;
- sensitive-data constraints;
- validation;
- maintenance; and
- failure mode.

Also define:
- current task inputs;
- authoritative external records;
- outputs;
- deterministic checks;
- review gates;
- logging;
- escalation; and
- retirement criteria.

Return:
1. capability-selection matrix;
2. architecture diagram;
3. workflow stages;
4. control matrix;
5. implementation sequence; and
6. success metrics.

Remove any capability whose value does not justify its overhead.
```

## Suggested study exercise

Apply prompts 1, 3, 6, 7, and 12 to a fictional monthly reporting workflow. Compare the resulting architecture with the four-layer model in the lesson.

## Related material

- [Capability Layer lesson](../../modules/01-platform-model-foundations/lessons/04-capability-layer-skills-code-execution.md)
- [Capability patterns](../../patterns/capability-patterns.md)
- [Core Entry Points prompts](03-core-entry-points-prompts.md)
- [Workflow orchestrator template](../workflow-orchestrator-template.md)
- [Governance review template](../governance-review-template.md)

## Public-repository content rule

Use fictional, generic, synthetic, or public scenarios. Do not place client names, nonpublic organizational details, confidential data, proprietary procedures, credentials, or engagement-identifying examples in these prompts.