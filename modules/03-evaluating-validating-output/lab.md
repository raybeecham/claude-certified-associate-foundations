# Lab: Grounded-Output Evaluation Harness

## Scenario

A Claude-powered assistant reviews post-quantum cryptography migration evidence and produces:

- control status;
- evidence summary;
- gap;
- confidence;
- source citation; and
- executive narrative.

Stakeholders report that the narrative sounds credible, but some citations do not support the claims.

## Objectives

- Convert stakeholder concerns into measurable criteria.
- Build a representative evaluation set.
- Select appropriate graders.
- Define hard release gates and regression reporting.

## Tasks

### Task 1: Success criteria

Define thresholds for:

- required-field completeness;
- schema validity;
- control-status accuracy;
- claim grounding;
- citation accuracy;
- unsupported specificity;
- privacy;
- consistency;
- latency; and
- reviewer correction time.

Mark each criterion as:

- hard gate;
- optimization metric; or
- monitoring metric.

### Task 2: Evaluation set

Design 20 cases:

- 8 normal;
- 3 missing evidence;
- 3 conflicting sources;
- 2 stale or superseded sources;
- 2 prompt injection;
- 1 unauthorized source request; and
- 1 long-input case.

For each case, specify the expected behavior and severity if it fails.

### Task 3: Graders

Assign a grader:

| Property | Code | Human | Model-assisted | Combination |
|---|---|---|---|---|
| JSON schema | | | | |
| Allowed status label | | | | |
| Citation exists | | | | |
| Citation supports claim | | | | |
| Executive usefulness | | | | |
| High-impact recommendation | | | | |
| Sensitive-data disclosure | | | | |

Justify every selection.

### Task 4: Claim-level validation

Define a procedure that labels each claim:

- supported;
- partially supported;
- unsupported; or
- contradicted.

Include how quoted evidence and citation spans are checked.

### Task 5: Regression report

Create a template comparing baseline and candidate versions by:

- objective;
- input slice;
- severity;
- latency;
- cost;
- reviewer burden; and
- new failures.

## Deliverable

Create `evaluation-plan.md` and a small machine-readable `eval-cases.json`.

## Acceptance criteria

- [ ] Criteria are measurable.
- [ ] Critical failures cannot be hidden by an average.
- [ ] Evaluation cases reflect real distribution and risk.
- [ ] Exact properties use deterministic checks.
- [ ] Nuanced or consequential judgment has qualified human oversight.
- [ ] Citation support is verified, not merely citation presence.
- [ ] A holdout set is preserved for final validation.

<details>
<summary>Model solution outline</summary>

Schema validity, required fields, labels, identifiers, and citation existence are code-graded. Claim support can use a calibrated model-assisted rubric with quoted source spans, but high-severity or ambiguous cases require human adjudication. Any unauthorized disclosure or unsupported high-impact recommendation is a hard release block.

</details>
