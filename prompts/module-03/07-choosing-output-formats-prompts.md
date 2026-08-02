# Module 3 Notebook: Choosing Output Formats

Use these prompts to select and validate output modalities. They are study aids, not universal production instructions.

---

## 1. Output modality selector

```text
Recommend the best output modality for this task.

Task:
[TASK]

Evaluate:
- intended consumer;
- immediate versus standalone use;
- editability and reuse;
- machine-readability;
- numeric reliability;
- required charts or files;
- review and approval needs; and
- sensitivity or disclosure constraints.

Choose one or a combination of:
- inline response;
- artifact or reusable file;
- structured output;
- code-executed analysis.

Explain the choice and required validation. Do not treat presentation format as proof of correctness.
```

---

## 2. Inline response contract

```text
Return a concise inline response for immediate conversational use.

Include:
- direct answer;
- material caveat;
- next action;
- source or calculation note when relevant.

Do not create a standalone artifact unless the result requires reuse, formal delivery, complex structure, or a downloadable file.
```

---

## 3. Artifact or file contract

```text
Create a standalone deliverable for [AUDIENCE AND PURPOSE].

Define:
- file or artifact type;
- required sections;
- version identifier;
- source and calculation references;
- review status;
- editable versus final elements;
- disclosure restrictions; and
- approval requirements.

The deliverable must stand on its own without relying on hidden conversation context.
```

---

## 4. Structured schema designer

```text
Design a structured output schema for this workflow.

Workflow:
[DESCRIPTION]

For every field, define:
- name;
- type;
- required or optional;
- allowed values;
- missing-data behavior;
- provenance requirement;
- validation rule; and
- downstream consumer.

Separate structural validation from semantic and factual validation.
```

---

## 5. Structured extraction prompt

```text
Extract records from the supplied sources using this schema:
[SCHEMA]

Rules:
- use null for absent values;
- do not infer unsupported values;
- preserve units, dates, and conditions;
- include source and location for material fields;
- classify uncertainty explicitly;
- validate schema conformance; and
- list semantic conflicts separately.
```

---

## 6. Code-execution analysis contract

```text
Analyze the attached data using code execution.

Before computing:
1. inspect the files and schema;
2. state inclusion and exclusion rules;
3. define date boundaries, duplicate handling, missing values, units, currencies, and signs;
4. identify ambiguous business rules; and
5. mark the result provisional if a material rule is unresolved.

Then:
- execute the calculation;
- retain reproducible code or calculation logic;
- report row counts before and after filtering;
- reconcile against available control totals;
- return a structured result table;
- generate charts only from computed results; and
- state limitations and review requirements.
```

---

## 7. Spreadsheet revenue analysis

```text
From the attached sales workbook, calculate total recognized revenue for [DATE RANGE] and rank the top [N] accounts.

First inspect:
- date field;
- status values;
- currency;
- credit and refund handling;
- duplicate identifiers;
- missing values;
- account-name normalization; and
- control totals.

Use code execution. Return:
1. calculation rules;
2. row-count reconciliation;
3. exact total;
4. ranked account table;
5. chart based on the result table;
6. code or reproducibility record; and
7. limitations and required approval.
```

---

## 8. Input-curation manifest

```text
Review the proposed input set before analysis.

For each item, classify:
- Include;
- Exclude;
- Replace;
- Clarify; or
- Restrict.

Identify:
- duplicates and near-duplicates;
- superseded versions;
- authoritative versus reference sources;
- approved versus draft content;
- raw versus processed data;
- irrelevant material;
- missing required inputs;
- sensitive content; and
- metadata or schema problems.

Return a curated-input manifest and the authoritative source hierarchy.
```

---

## 9. De-duplication review

```text
Inspect this source set for duplicate, near-duplicate, or superseded material.

For each group:
- list the related items;
- identify the likely controlling version;
- compare meaningful differences;
- assess double-counting or conflict risk; and
- recommend which versions to retain.

Do not silently discard conflicting material.
```

---

## 10. Code logic audit

```text
Audit this code-executed analysis.

Check:
- input versions;
- schema assumptions;
- filters and date boundaries;
- units and currencies;
- signs and credit handling;
- duplicates;
- missing values;
- joins and groupings;
- formulas and statistical method;
- control-total reconciliation;
- chart consistency; and
- narrative consistency with computed results.

Return Pass, Fail, or Needs Review for each check.
```

---

## 11. Schema validation audit

```text
Validate this structured output against the supplied schema.

Perform two reviews:

Structural:
- required fields;
- types;
- allowed values;
- null rules;
- uniqueness;
- format constraints.

Semantic:
- factual support;
- classification correctness;
- completeness;
- provenance;
- uncertainty;
- professional fitness.

Do not treat structural validity as semantic correctness.
```

---

## 12. Human and machine dual-output design

```text
Design a dual-output package for this task:

1. human-readable summary;
2. machine-readable structured record.

Ensure both outputs share:
- the same source version;
- the same computed values;
- the same identifiers;
- the same uncertainty status; and
- the same approval state.

Define reconciliation checks to detect divergence between them.
```

---

## 13. Chart reliability review

```text
Review this chart and its source data.

Check:
- source table;
- aggregation logic;
- date range;
- units;
- axis scale;
- labels;
- sorting;
- omitted categories;
- annotations;
- visual distortion; and
- consistency with the narrative.

Require the chart to be regenerated from the validated result table if any mismatch exists.
```

---

## 14. Reproducibility package builder

```text
Create a reproducibility package for this computed result.

Include:
- input file names, hashes, versions, or dates;
- code and dependencies;
- parameters and business rules;
- row counts;
- output tables;
- control-total reconciliation;
- known limitations;
- reviewer and approval status; and
- instructions to rerun the calculation.
```

---

## 15. Format anti-pattern diagnosis

```text
Diagnose the output-format failure in this scenario.

Classify the dominant issue:
- prose used for material arithmetic;
- standalone artifact treated as approval;
- structured syntax treated as factual validation;
- code executed with incorrect logic;
- chart generated from unsupported data;
- duplicate or noisy inputs;
- non-reproducible result;
- wrong modality for consumer; or
- disclosure or sensitivity mismatch.

Recommend the smallest effective repair.
```

---

## 16. Modality-combination planner

```text
Design a combined output package using the minimum necessary modalities.

Possible layers:
- code-executed calculation;
- structured result table;
- chart;
- reusable artifact or file;
- inline executive summary.

For each layer, define:
- purpose;
- consumer;
- source of truth;
- validation;
- versioning; and
- approval requirement.
```

---

## 17. Release-package review

```text
Review the completed output package before release.

Confirm:
- the consumer received the correct modality;
- the standalone deliverable is self-contained;
- structured outputs pass schema and semantic checks;
- numeric results come from executed and reconciled computation;
- charts match the result table;
- inputs were curated;
- provenance and limitations are visible;
- sensitive content is controlled;
- the released version matches the approved version; and
- reproducibility evidence is retained.

Return Release, Edit, Verify, Escalate, or Reject.
```

---

## 18. Oral certification drill

Answer each in two or three sentences:

1. When should output remain inline?
2. When is an artifact preferable?
3. What does structured output improve?
4. Why does valid JSON not prove factual correctness?
5. Why is code execution preferred for material calculations?
6. What can still be wrong after code runs successfully?
7. How do code execution and artifacts work together?
8. Why curate inputs before generation?
9. What are the three main curation techniques?
10. What evidence should be retained for a computed result?

---

# Compact format-selection card

```text
CONSUMER
[Human / Machine / Both]

USE
[Immediate / Standalone / Reusable / Formal]

STRUCTURE
[Free-form / Table / Schema / File]

COMPUTATION
[None / Low-stakes estimate / Material executed calculation]

OUTPUT
[Inline / Artifact / Structured / Code-executed combination]

VALIDATION
[Schema / Sources / Code / Reconciliation / Human review]

INPUT CURATION
[De-duplicated / Labeled / Pruned / Schema checked]

REPRODUCIBILITY
[Inputs / Code / Parameters / Results / Approval]
```
