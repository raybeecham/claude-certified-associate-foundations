# Grounded Verification Pattern

## Intent

Create an inspectable evidence path from a material claim back to the source, then apply independent checks proportionate to the consequence of error.

Use this pattern when an output:

- summarizes or analyzes documents;
- contains citations;
- makes factual or quantitative claims;
- depends on current external information;
- supports a recommendation or decision;
- interprets a contract, policy, standard, or regulation;
- explains spreadsheet calculations; or
- will be shared with a client, regulator, executive, or other consequential audience.

> Grounding improves traceability. Verification determines whether the traced claim is actually reliable enough to use.

---

## Problem

AI-generated outputs can contain:

- plausible unsupported claims;
- invented details;
- real citations that do not support the claim;
- incomplete quotations;
- omitted exceptions;
- outdated or out-of-scope sources;
- unstable conclusions across repeated runs;
- incorrect calculations using correctly cited inputs; and
- conclusions that require authority or expertise the model does not possess.

A general instruction to `be accurate` does not create an evidence trail.

---

## Core distinction

```text
Citation
  ↓
Traceability

Traceability
  ↓
Support review

Support review
  ↓
Independent validation

Independent validation
  ↓
Qualified release decision
```

These stages are not interchangeable.

- A **citation** identifies a source or location.
- **Support review** checks whether the source justifies the full claim.
- **Independent validation** checks the claim through an authoritative source, deterministic method, or qualified reviewer.
- A **release decision** determines whether the result may be used for the stated purpose.

---

## Inputs

Define before generation:

| Input | Required decision |
|---|---|
| Intended use | What decision, communication, or action will the output support? |
| Stakes | What happens if a material claim is wrong or incomplete? |
| Evidence boundary | Supplied sources only, current external research, or both? |
| Source hierarchy | Which source controls when evidence differs? |
| Material claims | Which statements require explicit support? |
| Unknown behavior | What should happen when support is absent? |
| Citation format | What location is precise enough to audit? |
| Calculation method | Which operations require deterministic execution? |
| Human reviewer | Who has the expertise and authority to approve use? |
| Disposition set | Release, edit, verify, escalate, or reject? |

---

## Pattern

```text
1. Define purpose, stakes, and authority
               ↓
2. Define the evidence boundary
               ↓
3. Permit unknown and not-covered outcomes
               ↓
4. Extract or retrieve evidence
               ↓
5. Map claims to precise source locations
               ↓
6. Classify support
               ↓
7. Check coverage and conflicts
               ↓
8. Validate high-impact claims independently
               ↓
9. Recompute deterministic operations
               ↓
10. Obtain qualified review where required
               ↓
11. Record release disposition
```

---

## Step 1: Define purpose, stakes, and authority

Record:

- audience;
- decision or action;
- consequence of error;
- reversibility;
- regulatory, contractual, safety, or financial significance;
- required reviewer authority; and
- release threshold.

A low-stakes internal idea may require a lighter process than a regulatory submission. The evidence requirements should be selected before the answer is generated.

---

## Step 2: Define the evidence boundary

Choose explicitly:

### Closed-source

Use only supplied documents.

```text
Supplied evidence set
        ↓
Bounded retrieval and analysis
```

Use when the question is specifically about a contract, policy, report, workbook, or other fixed source package.

### Open research

Retrieve current evidence under a source hierarchy.

```text
Research question
      ↓
Primary or controlling sources
      ↓
Official guidance
      ↓
Reliable independent analysis
```

Use when currency, external facts, or independent validation are required.

### Mixed

Use supplied sources for one part and current authoritative sources for validation or context. Keep the two evidence classes visibly separate.

---

## Step 3: Permit unknown and not-covered outcomes

Use controlled uncertainty labels:

- `supported`;
- `qualified`;
- `unsupported`;
- `conflicting`;
- `not covered`; and
- `requires qualified review`.

Do not force a binary answer when the evidence does not justify one.

---

## Step 4: Extract or retrieve evidence

For long documents or consequential interpretation, use quote-first extraction.

```text
Source
  ↓
Exact passage or cell
  ↓
Location
  ↓
Condition and context
```

For current research, record:

- title;
- issuing authority;
- publication date;
- event or effective date;
- source class;
- scope; and
- direct support.

---

## Step 5: Map claims to sources

Build a claim-evidence ledger.

| Claim ID | Claim | Materiality | Source | Location | Exact support | Condition | Status |
|---|---|---|---|---|---|---|---|
| C-001 | | High / Medium / Low | | | | | Supported / Qualified / Unsupported / Conflicting / Not covered |

A material recommendation should not rely on an unsupported claim.

---

## Step 6: Classify support

### Supported

The source directly supports the full claim within the relevant scope.

### Qualified

The source supports a narrower statement or includes a material condition.

### Unsupported

No adequate evidence was located.

### Conflicting

Relevant sources disagree and the conflict is unresolved.

### Not covered

The evidence set does not address the issue.

### Requires qualified review

The evidence exists, but the conclusion requires professional judgment, authority, or contextual knowledge beyond the model-assisted workflow.

---

## Step 7: Check coverage and conflicts

Grounding can still fail if the evidence set is incomplete.

Use a coverage matrix:

| Expected source | Accessed? | Processed? | Material evidence found? | Citation used? | Issue |
|---|---|---|---|---|---|
| | Yes / No | Yes / No | Yes / No | Yes / No | |

Check:

- every required document;
- controlling amendments or versions;
- difficult or unusually formatted sections;
- missing pages or tabs;
- conflicting clauses;
- stale sources;
- jurisdiction or product mismatch; and
- sources omitted because they do not support the preferred conclusion.

---

## Step 8: Validate independently

Use an authoritative source or independent test for claims that matter.

```text
Grounded claim
      ↓
Independent authoritative source or test
      ↓
Verified / Qualified / Rejected / Unresolved
```

Examples:

- executed contract versus model summary;
- current official regulation versus training-memory recall;
- system-of-record schedule versus generated timeline;
- official product documentation versus capability assumption;
- primary research versus unsupported generalization; and
- qualified expert interpretation versus model self-review.

A second model response is not independent validation.

---

## Step 9: Recompute deterministic operations

For arithmetic, exact matching, schemas, or repeated-value reconciliation:

```text
Authoritative inputs
      ↓
Deterministic method
      ↓
Reproducible result
      ↓
Narrative reconciliation
```

Check:

- units;
- signs;
- denominators;
- time periods;
- formulas;
- rounding;
- dependencies;
- filters; and
- versioned inputs.

A citation to the inputs does not prove the calculation.

---

## Step 10: Obtain qualified review

Human review is required when:

- the consequence of error is high;
- professional judgment is necessary;
- evidence conflicts;
- authority is unclear;
- the output may affect rights, benefits, safety, finances, compliance, or employment;
- interpretation is jurisdiction-specific or date-sensitive;
- an organization requires formal approval; or
- the available evidence cannot resolve a material issue.

The reviewer needs:

- expertise;
- authority;
- access to evidence;
- time to review;
- independence from the initial generation; and
- responsibility for the disposition.

---

## Step 11: Record disposition

| Disposition | Use when |
|---|---|
| **Release** | Applicable criteria, support, validation, and review requirements pass |
| **Edit** | Substance is sound but wording, structure, or audience fit requires correction |
| **Verify** | A material claim or calculation lacks sufficient confirmation |
| **Escalate** | Authority or expertise exceeds the current workflow |
| **Reject** | The output is materially unsupported, unsafe, contradictory, or unfit for purpose |

Record:

- scope of release;
- unresolved uncertainty;
- reviewer;
- evidence version;
- approval date; and
- follow-up condition.

---

## Grounding ladder

| Level | Evidence method | Appropriate interpretation |
|---|---|---|
| 0 | Fluent answer | Generated text only |
| 1 | Self-review or repeated runs | Instability and possible defects |
| 2 | Claim-to-source citations | Traceability to selected evidence |
| 3 | Quote-first, section-level, or cell-level grounding | More inspectable source connection |
| 4 | Independent authoritative validation | Stronger factual basis |
| 5 | Deterministic tests and qualified review | Consequential release basis |

Decision rule:

> Use the lowest level that is genuinely sufficient for the consequence of error, but never label a lower level as if it established a higher one.

---

## Best-of-N subpattern

Use repeated generations as an instability detector.

```text
Same request and evidence
       ↓
Multiple candidate outputs
       ↓
Agreement and divergence map
       ↓
Targeted verification
```

### Useful findings

- changing facts;
- changing citations;
- changing conclusions;
- changing certainty;
- source-selection differences;
- omitted conditions; and
- unstable calculations.

### Prohibited interpretation

Do not treat majority agreement as factual confirmation.

---

## Product-citation subpattern

Product surfaces may provide citations to:

- document sections;
- emails;
- calendar events;
- Drive records;
- workbook cells;
- formulas; or
- other connected content.

Use product citations to reduce navigation cost.

Then verify:

1. the correct source was selected;
2. the citation opens;
3. the location contains the claimed information;
4. the context supports the full claim;
5. source coverage is complete;
6. formula or reasoning is correct; and
7. release review is satisfied.

```text
Clickable citation → easier inspection
Easier inspection   → not automatic correctness
```

---

## Controls

- Require controlled uncertainty labels.
- Use precise citation locations.
- Separate supplied-source facts from external research.
- Record source versions and effective dates.
- Require claim retraction when support is absent.
- Maintain a coverage matrix.
- Recompute material calculations.
- Use source hierarchies for conflicts.
- Require qualified approval for consequential use.
- Preserve an evidence and disposition record.

---

## Anti-patterns

### Citation theater

The output contains formal-looking citations that are not checked.

### Closed-source overreach

The supplied sources do not answer the question, but the output decides anyway.

### Self-consistency as proof

Repeated generations agree and are treated as independent confirmation.

### Quote cherry-picking

Accurate passages are selected while controlling or conflicting passages are omitted.

### Authoritative-but-inapplicable source

An official source is stale, out of scope, superseded, or from the wrong jurisdiction.

### Cited-input arithmetic

The inputs are traceable, but the formula is not independently verified.

### Human-review checkbox

A reviewer approves without adequate expertise, evidence access, time, or authority.

---

## Compact implementation template

```text
Purpose and stakes:
[INTENDED USE, CONSEQUENCE, REVERSIBILITY]

Evidence boundary:
[SUPPLIED SOURCES / CURRENT RESEARCH / MIXED]

Authority hierarchy:
[CONTROLLING ORDER]

Unknown behavior:
[NOT COVERED / UNSUPPORTED / CONFLICTING]

Grounding method:
[QUOTE FIRST / CLAIM-TO-SOURCE / CELL-LEVEL]

Citation contract:
[SOURCE AND PRECISE LOCATION]

Coverage check:
[EXPECTED SOURCES AND SECTIONS]

Independent validation:
[AUTHORITATIVE SOURCE OR TEST]

Deterministic checks:
[CALCULATION / MATCHING / SCHEMA]

Qualified reviewer:
[ROLE AND AUTHORITY]

Disposition:
[RELEASE / EDIT / VERIFY / ESCALATE / REJECT]
```

---

## Certification shortcut

```text
Evidence silent          → allow unknown
Fixed document set       → restrict sources
Long or consequential text → quote first
Material claim           → precise citation
Citation present         → inspect support
Runs disagree            → investigate instability
Runs agree               → still validate
Calculation              → deterministic check
High-stakes conclusion   → authoritative source and qualified review
```

## Related material

- [Fact-Checking and Grounding Techniques](../modules/03-evaluating-validating-output/lessons/04-fact-checking-grounding.md)
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](failure-signature-review-pattern.md)
- [Grounded Analysis Template](../prompts/grounded-analysis-template.md)
- [Evaluator Rubric Template](../prompts/evaluator-rubric-template.md)
- [Evaluation Canvas](../ai-systems-engineering/worksheets/evaluation-canvas.md)
