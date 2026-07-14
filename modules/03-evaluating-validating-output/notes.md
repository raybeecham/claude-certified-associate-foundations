# Notes: Evaluating & Validating Claude's Output

## 1. Define success before optimization

Evaluation answers a practical question:

> What observable evidence would convince us that this system is acceptable for its intended use?

Success criteria should be:

- specific;
- measurable;
- achievable;
- relevant to the use case; and
- tied to a release or operational decision.

A polished answer can still fail because it is unsupported, inconsistent, late, too expensive, privacy-invasive, or unusable by the downstream workflow.

## 2. Use multidimensional criteria

Typical dimensions include:

| Dimension | Example measure |
|---|---|
| Task fidelity | Correct label or required elements present |
| Grounding | Percentage of factual claims supported by allowed evidence |
| Citation accuracy | Citation supports the attached claim |
| Completeness | Required controls or fields covered |
| Relevance | No material off-topic content |
| Consistency | Variation across repeated runs remains within tolerance |
| Privacy | No prohibited data disclosure |
| Safety/policy | No disallowed recommendation or action |
| Tone | Calibrated rubric for audience and purpose |
| Latency | Percentile end-to-end response time |
| Cost | Cost per successful task or per thousand tasks |
| Tool reliability | Correct tool and valid parameters |
| Human effort | Review time and correction rate |

An aggregate score should not hide a severe failure. Define hard gates, such as zero unauthorized data disclosures in a release test.

## 3. Build a representative evaluation set

A useful set mirrors the real task distribution and deliberately expands risk coverage.

Include:

- normal cases;
- boundary cases;
- missing information;
- conflicting sources;
- irrelevant content;
- ambiguous instructions;
- long inputs;
- malformed inputs;
- multilingual or domain-specific variations where applicable;
- prompt injection attempts;
- unauthorized requests; and
- cases with known correct abstention or escalation.

Separate a development set from a final holdout set when prompt tuning is substantial. Otherwise, repeated optimization can overfit the known examples.

## 4. Select the grader

### Code-based grading

Use when correctness can be determined deterministically.

Examples:

- exact classification labels;
- required JSON keys;
- type and range validation;
- regex or string checks;
- arithmetic;
- citation identifiers that must exist;
- latency thresholds; and
- permission boundaries.

Strengths: scalable, consistent, auditable.

Limitations: may miss semantic quality.

### Human grading

Use when evaluation requires expertise, judgment, or accountability.

Examples:

- nuanced policy interpretation;
- legal or clinical review;
- tone and empathy;
- strategic usefulness;
- high-impact decisions; and
- ambiguous source conflicts.

Strengths: contextual judgment and accountability.

Limitations: cost, speed, reviewer inconsistency, and fatigue. Use reviewer guidance, calibration, and adjudication.

### Model-assisted grading

Use for scalable semantic assessment when a reliable rubric can be defined.

Controls:

- explicit dimensions and scoring anchors;
- examples of each score;
- independent evidence;
- periodic human calibration;
- bias and position testing;
- agreement monitoring; and
- deterministic checks for properties that do not require a model.

Do not treat an automated model grader as ground truth.

## 5. Grounding and citation validation

For evidence-bound tasks, evaluate at the claim level.

A useful procedure:

1. Extract factual claims.
2. Identify the cited source for each claim.
3. Verify that the source contains supporting evidence.
4. Check whether the claim adds unsupported specificity.
5. Check whether material counterevidence was omitted.
6. Mark claims as supported, partially supported, unsupported, or contradicted.
7. Calculate grounding and citation metrics.
8. Route high-severity unsupported claims for review.

Controls that reduce hallucination include:

- restricting the task to provided sources;
- permitting “unknown”;
- requiring source quotations or exact passages;
- requiring citations;
- verifying citations; and
- using a separate validation step.

In high-stakes use, always include qualified validation before reliance.

## 6. Consistency and variance

A single successful run does not establish reliability. Repeat cases when variation matters.

Measure:

- exact agreement for categorical tasks;
- schema validity rate;
- semantic similarity where appropriate;
- score variance;
- citation stability;
- tool-selection rate; and
- worst-case outcomes.

Do not demand identical prose when the actual requirement is stable factual content. Define the consistency target at the right level.

## 7. Regression testing

A change can improve one dimension while degrading another. Run the same evaluation set when changing:

- model or version;
- system instructions;
- prompt template;
- examples;
- tool descriptions or schemas;
- retrieval logic;
- source collection;
- output format; or
- policy controls.

Compare:

- pass rates by objective and severity;
- new versus resolved failures;
- latency and cost;
- tool-call behavior;
- human-review burden; and
- distributional slices.

Maintain a record of the accepted baseline and the reason for release.

## 8. Severity matters

Use a severity framework.

| Severity | Example | Release treatment |
|---|---|---|
| Critical | Unauthorized action or sensitive-data disclosure | Block |
| High | Unsupported high-impact recommendation | Block or formal exception |
| Medium | Important omission requiring reviewer correction | Threshold and remediation |
| Low | Minor style or formatting issue | Track and improve |

A 95% average can be unacceptable if the remaining 5% includes critical failures.

## 9. Evaluation traps

### Optimizing only average quality

This can hide failures in minority languages, rare input forms, adversarial cases, or high-risk categories.

### Using the training examples as the test

This measures memorization of the prompt examples rather than generalization.

### Grading style instead of truth

Fluent language can receive high subjective scores even when unsupported.

### Letting the same model generate and validate without controls

The validator can share the same blind spot. Use independent evidence, deterministic checks, and human calibration.

### Changing multiple variables

You cannot attribute the result to a specific intervention.

## 10. Release decision template

```text
Use case:
Version under test:
Evaluation set version:
Success criteria:
Hard gates:
Metric results:
Slice results:
New regressions:
Human review findings:
Residual risk:
Decision:
Approver:
Rollback:
Monitoring:
```

## 11. Review questions

1. Which criteria should be hard gates rather than averages?
2. When is exact-match grading appropriate?
3. How do you verify a citation rather than merely checking that one exists?
4. Why should a final holdout set be preserved?
5. How can a model-assisted grader be calibrated?
