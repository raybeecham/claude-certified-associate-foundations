# Evaluation Canvas

Define how the workflow will be judged before optimizing prompts or models.

## 1. Evaluation objective

What claim are we testing?

> Example: The workflow can classify approved documents with at least 95 percent precision while escalating ambiguous cases.

> 

## 2. Unit of evaluation

- [ ] Individual response
- [ ] Extracted field
- [ ] Classified item
- [ ] Generated document
- [ ] Tool call
- [ ] End-to-end workflow
- [ ] Human decision support
- [ ] Other: 

## 3. Representative test set

| Case type | Number | Why included |
|---|---:|---|
| Normal | | |
| Edge | | |
| Missing data | | |
| Conflicting evidence | | |
| Adversarial or injected content | | |
| High-consequence | | |
| Tool failure | | |
| Out-of-distribution | | |

## 4. Metrics

| Dimension | Metric | Threshold | Weight |
|---|---|---|---:|
| Factual accuracy | | | |
| Grounding | | | |
| Completeness | | | |
| Instruction following | | | |
| Structured-output validity | | | |
| Calculation accuracy | | | |
| Privacy and safety | | | |
| Tool reliability | | | |
| Latency | | | |
| Cost or usage | | | |
| Human revision burden | | | |
| Escalation quality | | | |

## 5. Severe failures

List failures that block release regardless of average score.

- 

Examples:

- unsupported consequential claim;
- unauthorized disclosure;
- incorrect irreversible action;
- silently dropped records;
- failure to escalate a prohibited case; or
- fabricated citation.

## 6. Grading method

| Check | Grader | Calibration method |
|---|---|---|
| Exact field or formula | Code-based | Known expected output |
| Nuanced quality | Qualified human | Rubric and anchor examples |
| Scalable review | Model-assisted | Human calibration and audit |
| Source support | Claim-to-source check | Primary-source verification |

## 7. Baseline and candidates

| Configuration | Prompt version | Model | Tools | Result |
|---|---|---|---|---|
| Baseline | | | | |
| Candidate A | | | | |
| Candidate B | | | | |

Hold prompt, sources, tools, and test cases constant when isolating model changes.

## 8. Acceptance decision

- [ ] Quality floor met.
- [ ] No release-blocking failure occurred.
- [ ] Latency target met.
- [ ] Cost or usage target met.
- [ ] Human revision is acceptable.
- [ ] Rollback configuration is available.

**Decision:** Approve / Approve with restrictions / Revise / Reject

**Evidence:**

> 

## 9. Ongoing monitoring

| Signal | Threshold | Owner | Action |
|---|---|---|---|
| Escaped error rate | | | |
| Reviewer override rate | | | |
| Source freshness failure | | | |
| Tool failure rate | | | |
| Latency or cost drift | | | |
| Safety event | | | |

## 10. Reevaluation triggers

Re-run evaluation when:

- the model changes;
- the prompt or Skill changes;
- tools or connectors change;
- the source set changes;
- policy or business rules change;
- the user population changes;
- a severe failure occurs; or
- monitoring shows material drift.
