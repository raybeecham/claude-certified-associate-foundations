# Lesson 7: Choosing Output Formats — Inline, Artifacts, Structured, and Code-Executed

## Overview

Output format is not only a presentation decision. It affects:

- how easily the result can be reviewed;
- whether it can be reused or edited;
- whether another system can consume it;
- whether calculations can be reproduced;
- whether uncertainty and provenance remain visible; and
- how much confidence the result deserves.

> Choose the output modality by the purpose, consumer, and reliability requirement—not by which format looks most impressive.

This lesson distinguishes four common paths:

1. **Inline output** for contextual work inside the conversation.
2. **Artifacts or files** for standalone deliverables that will be edited, reused, or shared.
3. **Structured output** for consistent fields, comparison, validation, or downstream consumption.
4. **Code-executed output** for calculations, transformations, charts, and processed files that must be computed and reproducible.

A crucial distinction:

```text
Inline, artifact, and structured output → presentation and delivery choices
Code execution                          → computation and verification method
```

Code execution can produce an inline answer, a structured table, a chart, or a reusable file.

---

# Plain-English explanation

Different jobs need different kinds of answers.

Ask:

```text
Who or what will use this result?
          ↓
Will it stay inside the conversation or become a deliverable?
          ↓
Does another person need to edit or reuse it?
          ↓
Does software need predictable fields?
          ↓
Do numbers need to be calculated rather than estimated?
```

A quick explanation for yourself may be fine inline.

A policy memo should probably be a standalone document.

A record that enters another system should use a defined schema.

A revenue total should be calculated by code over the actual rows—not generated as prose.

The central rule is:

> The more the result will be reused, parsed, reported, or trusted numerically, the more explicit and verifiable its format and production method must be.

---

# One analogy: choosing a container and a measuring tool

Imagine preparing materials for delivery.

- An **inline response** is a note handed directly to someone standing beside you.
- An **artifact or file** is a labeled binder that can travel, be revised, and stand on its own.
- A **structured format** is a shipping crate with defined compartments so every item goes in a known place.
- **Code execution** is the calibrated scale and measuring equipment used to determine the weight, dimensions, and totals before the package is labeled.

The container and the measuring method solve different problems.

A beautifully labeled crate does not prove that the weight printed on it is correct.

A calibrated scale can produce an exact measurement, but the operator can still weigh the wrong package or use the wrong unit.

```text
Good container
      ≠
Correct measurement

Executed measurement
      ≠
Correct logic, input, or interpretation
```

The finished delivery may need both: a reliable computation and an appropriate container.

---

# Format 1: Inline output

Inline output is content returned directly in the conversation.

## Best for

- quick explanations;
- short recommendations;
- conversational follow-up;
- questions that depend on the current context;
- low-stakes working notes;
- small comparisons; and
- results the user will act on immediately without separate distribution.

## Strengths

- fast;
- contextual;
- easy to clarify;
- low overhead; and
- well suited to iterative conversation.

## Limitations

- may depend on surrounding conversation context;
- is less suitable as a controlled standalone deliverable;
- may be difficult to version or distribute formally;
- can hide structure inside prose; and
- does not make generated numbers more reliable.

## Example

```text
The draft meets the requested length and tone, but the recommendation is not supported by the attached evidence. Revise before use.
```

This is useful as an immediate conversational finding. It does not need to become a separate document.

## Inline selection rule

Use inline output when:

```text
Immediate human use
+ low reuse
+ limited structure
+ no formal delivery requirement
```

---

# Format 2: Artifacts and reusable files

Artifacts and generated files are appropriate when the result should stand apart from the conversation and continue to be edited, referenced, downloaded, shared, or reused.

Examples include:

- reports;
- memos;
- proposals;
- presentations;
- spreadsheets;
- code;
- diagrams;
- web pages;
- PDFs; and
- reusable templates.

## Best for

- substantial standalone content;
- deliverables with their own structure;
- content that will go through several revision rounds;
- documents that need version control or approval;
- files that will be used outside the conversation; and
- content whose layout matters.

## Strengths

- separates the deliverable from conversational commentary;
- supports editing and iteration;
- can preserve headings, tables, code, or layout;
- provides a clearer review object; and
- is easier to reuse in another workflow.

## Limitations

- standalone appearance can create false confidence;
- generated files still require factual and professional review;
- sharing may expose attachments, context, or sensitive content depending on the product surface;
- versions can diverge; and
- an editable artifact is not automatically the approved release version.

## Artifact integrity rule

```text
Artifact created
      ≠
Deliverable approved
```

The workflow must identify:

- which version is current;
- which version was reviewed;
- who approved it;
- what source package supports it; and
- whether the released copy matches the approved copy.

---

# Format 3: Structured output

Structured output uses predictable fields and relationships instead of free-form prose.

Common structures include:

- Markdown tables;
- CSV;
- JSON;
- XML;
- YAML;
- typed records;
- database rows;
- checklists;
- matrices; and
- forms with required fields.

## Best for

- repeated records;
- comparisons;
- classification;
- extraction;
- batch processing;
- downstream automation;
- import into another system;
- deterministic validation; and
- situations where missing fields must be visible.

## Example schema

```json
{
  "claim": "string",
  "source": "string",
  "location": "string",
  "support_status": "supported | qualified | unsupported | conflicting | not_covered",
  "review_action": "keep | revise | verify | escalate | remove"
}
```

A schema can force the output to expose missing support instead of hiding it in polished paragraphs.

## Strengths

- consistent fields;
- easier comparison;
- easier machine processing;
- validation can detect missing or malformed values;
- supports sorting, filtering, and aggregation; and
- reduces ambiguity about the expected output shape.

## Limitations

- syntactically valid structure can still contain false information;
- an invented value fits inside JSON as easily as a verified value;
- overly rigid schemas can omit important nuance;
- tables can hide assumptions or provenance; and
- downstream systems may treat model-generated fields as authoritative unless controls are added.

## Structured-output rule

```text
Valid schema
      ≠
Valid meaning
```

Validate both:

1. **structure:** required fields, types, allowed values, and constraints;
2. **semantics:** factual support, correct classification, completeness, and professional fitness.

---

# Format 4: Code-executed output

Code execution is the preferred path when the task depends on exact calculation, aggregation, transformation, filtering, charting, or file processing.

Examples include:

- summing a spreadsheet column;
- grouping sales by account;
- calculating averages, confidence intervals, or variances;
- identifying duplicates;
- transforming file formats;
- validating schemas;
- generating charts;
- reconciling two datasets;
- sorting and ranking records; and
- producing processed files.

## Why prose is weak for material calculations

A language model generates probable text. It can describe arithmetic correctly while producing an incorrect result.

A prose answer such as:

```text
Total revenue was approximately $4.8 million.
```

may look reasonable without documenting:

- which rows were included;
- which date field was used;
- whether refunds were deducted;
- whether duplicate invoices existed;
- which currency applied;
- whether pending transactions were excluded; or
- how the sum was calculated.

## What code execution adds

```text
Actual input data
      ↓
Explicit filtering and transformation logic
      ↓
Executed calculation
      ↓
Computed result
      ↓
Reproducible table, chart, or file
```

For the same code, inputs, and environment, the executed operation can be rerun and inspected.

## What code execution does not guarantee

Claude writes or selects the code. The code may contain:

- an incorrect filter;
- a wrong date boundary;
- a unit error;
- an inappropriate statistical method;
- an incorrect join;
- duplicate counting;
- missing-value mishandling;
- an incorrect business rule; or
- a chart that visually misrepresents the data.

The input data may also be incomplete, stale, mislabeled, or wrong.

Therefore:

```text
Executed successfully
      ≠
Logically correct
      ≠
Based on correct data
      ≠
Approved for release
```

## Code-execution verification chain

```text
Inspect inputs
      ↓
Define business rules
      ↓
Write or generate code
      ↓
Review critical logic
      ↓
Execute
      ↓
Check outputs and reconciliations
      ↓
Retain code, parameters, and result
      ↓
Apply qualified human review where required
```

---

# Practical example: Q3 revenue and top accounts

## Task

A sales manager uploads a fictional workbook and asks:

```text
Report total recognized Q3 revenue and the three highest-revenue accounts.
```

The workbook contains:

- transaction date;
- invoice identifier;
- account;
- amount;
- currency;
- transaction status; and
- transaction type.

## Prose-only path

```text
Q3 revenue was about $4.9 million. The largest accounts were Atlas, Meridian, and Northstar.
```

The answer is fluent, but the reviewer cannot tell whether Claude:

- filtered July 1 through September 30 correctly;
- excluded pending invoices;
- deducted credit notes;
- removed duplicate invoice rows;
- converted currencies; or
- grouped account names consistently.

This is an estimate-shaped sentence, not a verified financial result.

## Code-executed path

The workflow first defines the rules:

```text
Date range: 2026-07-01 through 2026-09-30
Status: recognized only
Currency: USD only unless conversion rates are provided
Credits: subtract credit notes
Duplicates: one record per invoice-line identifier
Account grouping: normalized account name
```

Illustrative code logic:

```python
q3 = sales[
    (sales["transaction_date"] >= "2026-07-01")
    & (sales["transaction_date"] <= "2026-09-30")
    & (sales["status"] == "recognized")
    & (sales["currency"] == "USD")
].drop_duplicates(subset=["invoice_line_id"])

q3["net_amount"] = q3.apply(
    lambda row: -row["amount"] if row["transaction_type"] == "credit" else row["amount"],
    axis=1,
)

total_revenue = q3["net_amount"].sum()
top_accounts = (
    q3.groupby("normalized_account")["net_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
```

Illustrative computed output:

| Result | Value |
|---|---:|
| Total recognized Q3 revenue | $4,863,275 |
| Atlas Systems | $780,400 |
| Meridian Group | $705,125 |
| Northstar Services | $642,000 |

## Required checks

Before reporting the result:

- confirm the date field and quarter definition;
- reconcile row count before and after de-duplication;
- confirm status values;
- review credits and refunds;
- check for non-USD records;
- confirm account normalization;
- compare the total with an authoritative report or control total; and
- review the code and result if the figure is material.

## Output package

A strong deliverable might combine several formats:

1. **Inline:** a concise explanation of the result and limitations.
2. **Structured table:** exact totals and ranked accounts.
3. **Chart:** top-account comparison.
4. **Reusable file:** processed workbook or CSV.
5. **Code or calculation record:** reproducible logic and parameters.

The calculation method and delivery format work together.

---

# Input curation shapes output quality

A well-designed output cannot fully compensate for poor inputs.

```text
Curated inputs
      ↓
Clear role and source hierarchy
      ↓
Predictable processing
      ↓
Cleaner, more reviewable output
```

The three course-aligned techniques are:

## 1. De-duplicate

Remove duplicate or near-duplicate copies that may:

- be counted twice;
- contain conflicting revisions;
- overweight repeated information;
- create inconsistent citations; or
- waste context and review effort.

Record which version is authoritative.

## 2. Label and structure

Make each input's role explicit.

Example:

```text
approved_policy_v3.pdf      → controlling policy
policy_draft_redline.docx   → proposed changes only
responses_raw.csv           → unreviewed submissions
responses_validated.csv     → approved analysis input
```

Labels should distinguish:

- approved versus draft;
- authoritative versus reference;
- current versus superseded;
- raw versus processed;
- internal versus external; and
- trusted versus untrusted.

## 3. Prune irrelevant material

Remove content that does not help answer the question.

Noise can create:

- irrelevant themes;
- false contradictions;
- unnecessary token use;
- accidental disclosure;
- weak source selection; and
- more complicated review.

## Engineering extension: inspect the schema

For data tasks, also confirm:

- field names and types;
- units and currencies;
- date formats and time zones;
- unique identifiers;
- missing-value conventions;
- allowed categorical values;
- duplicate rules;
- version and extraction date; and
- control totals.

> Clean, labeled, minimal inputs are easier to reason about, easier to process, and easier to audit.

---

# Output modality decision matrix

| Requirement | Inline | Artifact or file | Structured | Code-executed path |
|---|---:|---:|---:|---:|
| Quick conversational response | Strong | Weak | Optional | Only if computation needed |
| Standalone deliverable | Weak | Strong | Optional | If calculations or processing needed |
| Repeated editing and reuse | Weak | Strong | Moderate | Produces reusable outputs |
| Machine consumption | Weak | Moderate | Strong | Often produces structured files |
| Exact aggregation or calculation | Weak | Weak by itself | Weak by itself | Strongest path |
| Charts from data | Weak | Strong destination | Strong source table | Required for computed chart |
| Schema validation | Weak | Weak | Strong | Strong with validation code |
| Formal version and approval | Weak | Strong | Moderate | Retain code and output artifacts |

Several modalities may be combined.

Example:

```text
Code-executed calculation
        ↓
Structured results table
        ↓
Artifact report
        ↓
Inline executive summary
```

---

# A reliability ladder for numeric work

| Level | Output | Reliability contribution |
|---:|---|---|
| 0 | Prose-generated estimate | Plausible wording only |
| 1 | Structured model-generated values | Consistent shape, not verified math |
| 2 | Values with source-row references | Better traceability |
| 3 | Code-executed calculation | Reproducible computation |
| 4 | Reconciliation against control totals or independent implementation | Stronger validation |
| 5 | Qualified review and approval | Consequential release basis |

The ladder is cumulative. A code-executed result can still require reconciliation and human approval.

---

# The format selection protocol

```text
1. Define the consumer and intended action
          ↓
2. Determine whether the output is conversational or standalone
          ↓
3. Determine editability, reuse, and machine-readability needs
          ↓
4. Identify calculations, transformations, or charts requiring execution
          ↓
5. Curate and label the inputs
          ↓
6. Define the output contract or schema
          ↓
7. Produce the result using the appropriate modality
          ↓
8. Validate structure, semantics, calculations, and provenance
          ↓
9. Apply audience adaptation and human-review gates
          ↓
10. Release the reviewed version and retain reproducibility evidence
```

## Output contract

Before generation, define:

- consumer;
- purpose;
- delivery channel;
- standalone versus conversational use;
- required fields or sections;
- file type;
- editability;
- machine-readability;
- calculation and precision requirements;
- citation and provenance requirements;
- validation rules;
- version and approval requirements; and
- sensitive-data restrictions.

---

# Paste-ready prompts

## Format selector

```text
Recommend the output modality for this task.

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

Explain why, identify validation requirements, and do not treat presentation format as proof of correctness.
```

## Structured-output contract

```text
Return the result using this schema:
[SCHEMA]

Rules:
- include every required field;
- use only the allowed values;
- use null for missing values rather than inventing them;
- separate source facts from inference;
- include provenance for material fields;
- validate the structure before returning it; and
- list semantic uncertainties separately.
```

## Code-executed data analysis

```text
Analyze the attached data using code execution.

Before computing:
1. inspect the files and schema;
2. state the inclusion, exclusion, date, duplicate, missing-value, unit, and currency rules;
3. identify ambiguous fields or missing business rules; and
4. stop for clarification or mark the result provisional if a material rule is unresolved.

Then:
- execute the calculation;
- return the code or a reproducible calculation record;
- provide row counts before and after filtering;
- reconcile against any available control total;
- produce a structured result table;
- generate a chart only from the computed table; and
- state limitations and required human review.
```

## Input-curation prompt

```text
Review the proposed input set before analysis.

Identify:
- duplicates and near-duplicates;
- superseded versions;
- authoritative versus reference sources;
- unclear labels;
- irrelevant material;
- missing required sources;
- sensitive information that should be removed or restricted; and
- schema or metadata problems.

Return a curated-input manifest with Include, Exclude, Replace, or Clarify decisions and the reason for each.
```

## Computation audit prompt

```text
Audit the executed analysis.

Check:
- input files and versions;
- row counts;
- filters and date boundaries;
- units, currencies, and signs;
- duplicate handling;
- missing-value behavior;
- formulas and business rules;
- groupings and joins;
- control-total reconciliation;
- chart consistency with the result table; and
- whether the narrative matches the computed result.

Classify each check as Pass, Fail, or Needs Review.
```

---

# Common anti-patterns

## Anti-pattern 1: Asking prose to perform material arithmetic

**Failure:** A plausible number is generated without a reproducible computation.

**Repair:** Use code execution over the actual data and retain the logic.

## Anti-pattern 2: Treating a structured format as factual validation

**Failure:** Invalid claims are returned inside valid JSON or a polished table.

**Repair:** Validate structure and semantics separately.

## Anti-pattern 3: Choosing an artifact because it looks professional

**Failure:** Standalone presentation creates false confidence.

**Repair:** Apply grounding, calculation checks, and review gates to the artifact.

## Anti-pattern 4: Executing unreviewed logic

**Failure:** The code runs successfully but applies the wrong rule.

**Repair:** Inspect business logic, inputs, filters, and reconciliations.

## Anti-pattern 5: Creating a chart directly from prose

**Failure:** The chart visualizes an unsupported number.

**Repair:** Generate charts from a computed and validated result table.

## Anti-pattern 6: Feeding duplicate or superseded sources

**Failure:** Repetition, conflicting versions, or double counting distorts the output.

**Repair:** De-duplicate and identify the controlling version.

## Anti-pattern 7: Providing an undifferentiated input pile

**Failure:** The model cannot distinguish approved, draft, raw, current, or irrelevant materials.

**Repair:** Label every input's role and authority.

## Anti-pattern 8: Output that cannot be reproduced

**Failure:** The final number has no retained input version, code, parameters, or row-level trace.

**Repair:** Preserve a reproducibility package.

## Anti-pattern 9: Correct code over incorrect data

**Failure:** Deterministic computation repeats a source-data error precisely.

**Repair:** Validate the source, schema, control totals, and extraction date.

---

# Exam reasoning pattern

For output-format scenarios:

1. identify the consumer and downstream use;
2. determine whether the result is conversational or standalone;
3. identify editability, reuse, and machine-consumption needs;
4. distinguish presentation format from computation method;
5. use structured formats when fields must be consistent or machine-readable;
6. use code execution when exact calculations, transformations, or charts matter;
7. remember that successful execution does not prove correct logic or data;
8. curate inputs through de-duplication, labeling, and pruning;
9. validate structure, semantics, calculations, and provenance;
10. apply audience adaptation and required human review; and
11. retain the reviewed version and reproducibility evidence.

```text
Quick conversational guidance → inline
Standalone editable deliverable → artifact or file
Machine-consumed records → structured schema
Material numeric calculation → code execution
Chart from uploaded data → code execution + validated table
Dirty source package → curate before generation
Successful code with wrong filters → review logic and reconcile
```

---

# Knowledge check

## Question 1

Why is output format a reliability decision?

**Answer:** The format affects inspectability, reproducibility, reuse, machine consumption, validation, and whether calculations are generated as prose or executed over actual data.

## Question 2

When is inline output appropriate?

**Answer:** When the result is contextual, conversational, used immediately, and does not need to stand alone as a formal deliverable.

## Question 3

What is an artifact best suited for?

**Answer:** Significant standalone content that will be edited, reused, referenced, shared, or delivered outside the immediate conversation.

## Question 4

Does valid JSON prove that the values are correct?

**Answer:** No. Syntax and schema validation do not establish factual or semantic correctness.

## Question 5

Why is code execution stronger for material calculations?

**Answer:** It performs an explicit calculation over the actual inputs and can preserve code, parameters, row counts, and outputs for review and rerun.

## Question 6

What remains unproven after code executes successfully?

**Answer:** The correctness of the business logic, filters, method, source data, units, interpretation, and release decision.

## Question 7

What are the three core input-curation techniques?

**Answer:** De-duplicate sources, label and structure each input's role, and prune irrelevant material.

## Question 8

Can code execution and artifacts be used together?

**Answer:** Yes. Code can compute and validate results that are then delivered in a table, chart, spreadsheet, report, or other artifact.

---

# Flashcards

## Flashcard 1

**Q:** What is inline output?

**A:** A contextual conversational response intended for immediate use within the chat.

## Flashcard 2

**Q:** What is an artifact or reusable file?

**A:** Standalone content designed for editing, reuse, reference, sharing, or formal delivery.

## Flashcard 3

**Q:** What is structured output?

**A:** Information returned in predictable fields or a defined schema for comparison, validation, or downstream consumption.

## Flashcard 4

**Q:** What is code execution's role?

**A:** To run explicit calculations, transformations, validation, charting, and file processing over actual inputs.

## Flashcard 5

**Q:** Does executed code guarantee a correct answer?

**A:** No. The code, business rules, inputs, units, filters, and interpretation may still be wrong.

## Flashcard 6

**Q:** What is the difference between structural and semantic validation?

**A:** Structural validation checks format and fields; semantic validation checks whether the content is factually and professionally correct.

## Flashcard 7

**Q:** Why curate inputs?

**A:** To remove duplicates and noise, identify authoritative versions, clarify roles, reduce disclosure risk, and make processing more reliable.

## Flashcard 8

**Q:** What is the code-execution trust chain?

**A:** Inspect inputs, define rules, review logic, execute, reconcile, retain reproducibility evidence, and obtain required human review.

---

# Short recap

```text
1. Choose the modality by consumer, purpose, and reliability need.
2. Use inline output for immediate conversational work.
3. Use artifacts or files for standalone, editable deliverables.
4. Use structured formats for predictable fields and downstream consumption.
5. Use code execution for material calculations and transformations.
6. Treat execution as reproducible computation, not automatic correctness.
7. Validate code logic, inputs, units, filters, and results.
8. De-duplicate, label, and prune the input set.
9. Combine modalities when the workflow requires it.
10. Retain the reviewed version, code, parameters, and provenance.
```

> Pick the output container for how the result will be used, and pick the execution method for how much the result must be trusted.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute financial, legal, audit, compliance, data-engineering, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was dated June 2026. Product-specific statements were rechecked against official Anthropic documentation on **August 2, 2026**.

Official references:

- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)

Current Anthropic documentation describes artifacts as substantial standalone content in a dedicated window and describes code execution as a sandboxed tool for calculations, data analysis, visualizations, file processing, and file creation. Product availability, behavior, sharing rules, and interfaces can change, so verify current documentation and organizational controls before implementation.

## Related material

- [Editing and Adapting Output for Your Audience](06-editing-adapting-audience.md)
- [Diligence: When Human Review Is Non-Negotiable](05-diligence-human-review.md)
- [Module 3 overview](../README.md)
- [Choosing Output Formats prompt notebook](../../../prompts/module-03/07-choosing-output-formats-prompts.md)
- [Output Format and Reliability Pattern](../../../patterns/output-format-reliability-pattern.md)
- [Grounded Verification Pattern](../../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../../patterns/human-review-gate-pattern.md)
