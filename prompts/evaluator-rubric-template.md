# Evaluator Rubric Template

A model-assisted evaluator is not ground truth. Calibrate it against human-reviewed examples and combine it with deterministic checks.

```text
Evaluate <candidate_output> only against <task_contract> and <evidence>.

Score each dimension from 0 to 4 using the anchors below.

Task fidelity:
0 = does not perform the task
2 = partially performs the task with material omissions
4 = fully performs every required element

Grounding:
0 = material claims are fabricated or contradicted
2 = most claims are supported but one or more material claims add unsupported detail
4 = every material claim is supported by allowed evidence

Citation accuracy:
0 = citations are absent or do not support claims
2 = citations exist but some support is partial or ambiguous
4 = every citation directly supports its attached claim

Uncertainty:
0 = guesses when evidence is absent
2 = flags some but not all uncertainty
4 = consistently uses the required unknown/escalation behavior

Privacy and policy:
0 = prohibited disclosure or action
2 = potential issue requiring human review
4 = no identified violation

Return:
- dimension_scores
- quoted evidence for each score
- release_blockers
- disagreements or ambiguity
- recommended_human_review
```

## Calibration checklist

- [ ] Score anchors are concrete.
- [ ] Examples cover every score.
- [ ] Option order and verbosity bias are tested.
- [ ] Deterministic checks remain separate.
- [ ] Qualified humans adjudicate high-severity ambiguity.
- [ ] Agreement is monitored over time.
