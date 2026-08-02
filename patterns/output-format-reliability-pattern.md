# Output Format and Reliability Pattern

## Purpose

Use this pattern to select an output container and computation method that fit the consumer, downstream workflow, reuse needs, and consequence of error.

> Select the container for how the result will be used, and select the execution method for how much the result must be trusted.

## Problem

Format decisions are often made for appearance rather than reliability. Common failures include:

- copying conversational prose into a formal deliverable;
- treating a polished artifact as an approved result;
- treating valid JSON as factually valid;
- asking prose generation to perform material arithmetic;
- executing code with incorrect business rules;
- charting unreconciled values; and
- processing duplicate, superseded, or noisy inputs.

## Core distinction

```text
Inline, artifact, and structured output → delivery and presentation
Code execution                          → computation and processing
```

Code execution may produce any of the other output types.

## Selection dimensions

Evaluate:

1. consumer: human, machine, or both;
2. use: immediate, standalone, reusable, or formal;
3. structure: free-form, table, schema, or file;
4. computation: none, approximate, or exact;
5. reliability: conversational, operational, material, or audit-critical;
6. provenance: none, source citations, row-level trace, or reproducibility package;
7. approval: self-review, peer review, or qualified gate; and
8. sensitivity: public, internal, confidential, or regulated.

## Modality guidance

| Need | Preferred modality |
|---|---|
| Immediate contextual answer | Inline |
| Standalone editable deliverable | Artifact or file |
| Machine-consumed fields | Structured output |
| Exact calculation or transformation | Code execution |
| Calculated report | Code execution + structured table + artifact |
| Executive result from analysis | Code execution where needed + inline summary |

## Inline output

Use when the result is contextual, short-lived, immediately actionable, and does not need formal versioning.

### Controls

- keep material caveats visible;
- identify when the answer is provisional;
- do not report material calculations from prose alone; and
- move to a standalone artifact when reuse or approval is required.

## Artifact or reusable file

Use for substantial content that must stand alone, be edited, shared, versioned, or formally reviewed.

### Controls

- identify the current and approved version;
- include source and calculation references;
- ensure the file is self-contained;
- review disclosure and sensitivity; and
- confirm the released file matches the approved file.

```text
Artifact created
      ≠
Deliverable approved
```

## Structured output

Use predictable fields for extraction, classification, comparison, validation, or downstream automation.

### Controls

- define required fields and types;
- use controlled values;
- define missing-data behavior;
- retain provenance for material fields;
- validate schema conformance; and
- separately validate factual meaning.

```text
Valid schema
      ≠
Valid semantics
```

## Code execution

Use for exact calculations, transformations, filtering, reconciliation, charting, and file processing.

### Controls

```text
Inspect inputs
      ↓
Define business rules
      ↓
Review critical logic
      ↓
Execute
      ↓
Reconcile outputs
      ↓
Retain code and parameters
      ↓
Apply required human review
```

Successful execution proves only that the environment ran the instructions.

```text
Executed successfully
      ≠
Correct logic
      ≠
Correct data
      ≠
Correct interpretation
      ≠
Release approval
```

## Input curation

Before generation or execution:

1. de-duplicate exact and near-duplicate sources;
2. identify the authoritative version;
3. label approved, draft, raw, processed, current, and superseded inputs;
4. remove irrelevant material;
5. restrict sensitive material to authorized workflows;
6. inspect field names, types, units, currencies, dates, and identifiers; and
7. record missing sources or unresolved business rules.

## Reproducibility package

For material computed outputs, retain:

- input file names, versions, dates, or hashes;
- schema and business rules;
- code and dependencies;
- parameters and date boundaries;
- row counts before and after filtering;
- duplicate and missing-value treatment;
- result tables and charts;
- control-total reconciliation;
- known limitations; and
- reviewer and approval record.

## Reliability ladder

| Level | Method | Contribution |
|---:|---|---|
| 0 | Prose-generated number | Plausibility only |
| 1 | Structured model-generated value | Consistent shape |
| 2 | Source or row references | Traceability |
| 3 | Code-executed calculation | Reproducibility |
| 4 | Independent reconciliation | Stronger validation |
| 5 | Qualified review | Consequential release basis |

## Combined package pattern

```text
Curated inputs
      ↓
Code-executed analysis
      ↓
Validated structured table
      ↓
Chart generated from that table
      ↓
Standalone artifact
      ↓
Inline executive summary
      ↓
Human review and approval
```

## Common failure modes

### Prose arithmetic

A language model generates a plausible total without a reproducible calculation.

**Control:** Execute the calculation over the actual data.

### Schema confidence

Valid JSON is treated as factual proof.

**Control:** Validate structure and semantics separately.

### Artifact confidence

Professional appearance is mistaken for readiness.

**Control:** Apply grounding and review gates.

### Executed wrong rule

Code runs successfully with an incorrect filter, join, unit, or business rule.

**Control:** Review logic and reconcile to authoritative totals.

### Chart-first workflow

A visualization is built from an unsupported narrative value.

**Control:** Generate charts from validated computed tables.

### Noisy input package

Duplicates, obsolete versions, and irrelevant content distort analysis.

**Control:** Curate and label inputs first.

### Non-reproducible result

A number is released without retained code, parameters, and source version.

**Control:** Preserve the reproducibility package.

## Decision rule

```text
Quick, contextual human use      → inline
Standalone editing or delivery   → artifact or file
Machine-readable repeatability   → structured output
Material computation             → code execution
Consequential computed delivery  → combine computation, structure, artifact, and review
```

## Related material

- [Choosing Output Formats](../modules/03-evaluating-validating-output/lessons/07-choosing-output-formats.md)
- [Grounded Verification Pattern](grounded-verification-pattern.md)
- [Human Review Gate Pattern](human-review-gate-pattern.md)
- [Audience Adaptation Pattern](audience-adaptation-pattern.md)
