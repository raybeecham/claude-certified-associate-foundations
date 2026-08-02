# Lesson 9A: Module 3 Quiz — Output Evaluation and Validation

## Completion record

```text
Result: Full marks — 7 of 7
```

The preparation-course quiz demonstrated full coverage of:

1. accuracy versus completeness;
2. fabricated specifics and hallucination signatures;
3. source restriction, explicit uncertainty, and auditable citations;
4. internal inconsistency and deterministic recomputation;
5. audience-specific adaptation;
6. code-executed calculation for material numeric work; and
7. input curation through de-duplication, labeling, and pruning.

This public lesson uses original fictional scenarios rather than reproducing proprietary quiz questions.

---

# What the quiz measures

The quiz does not reward surface proofreading alone. It tests whether the learner can identify the controlling reliability problem and choose the smallest responsible intervention.

```text
Observe the output and intended use
          ↓
Identify the dominant quality or risk property
          ↓
Select the evidence, computation, adaptation, or review control
          ↓
Reject attractive but irrelevant alternatives
          ↓
State the next responsible action
```

The central question is not:

```text
Does this answer look good?
```

It is:

```text
What property must be established before this output may be trusted or used?
```

---

# Seven-domain assessment map

| Domain | Diagnostic question | Strong intervention |
|---|---|---|
| Completeness | What required factor may be absent? | Compare against requirements and source coverage |
| Hallucination | What precise claim lacks support? | Verify provenance or remove/qualify the claim |
| Grounding | What evidence boundary should control? | Restrict sources, permit unknowns, require citations |
| Consistency | Which values or claims conflict? | Recompute or reconcile against authoritative evidence |
| Audience fit | Who needs which depth and framing? | Produce truth-preserving audience variants |
| Numeric reliability | Must the result be exact and reproducible? | Execute code and review the logic |
| Input quality | Are sources duplicated, stale, or contradictory? | Curate, label, and prune before rerunning |

---

# Original seven-question quiz

## Question 1: Accurate but incomplete

A project assessment contains correct dates, costs, and staffing figures. The reviewer notices that the requested dependency analysis is absent.

What is the best response?

A. Approve it because every visible figure is correct.  
B. Run a separate completeness review against the requirements and add the missing dependency analysis.  
C. Switch models and regenerate without changing the evaluation criteria.  
D. Ask the model whether anything is missing and accept its answer.

**Best answer: B**

Accuracy and completeness fail independently. Correct visible content does not establish that all decision-relevant content is present.

---

## Question 2: Precise unsupported benchmark

A technology brief states that `72% of comparable organizations completed migration within nine months`, but provides no source, population, method, or date.

What is the dominant risk?

A. A minor formatting defect.  
B. A fabricated or unsupported specific that looks authoritative because it is precise.  
C. A problem solved by selecting a larger model.  
D. No meaningful risk because the number is plausible.

**Best answer: B**

Precision creates an expectation of provenance. A precise statistic without traceable support is a high-value hallucination signature.

---

## Question 3: Closed-source policy analysis

A reviewer needs answers based only on an uploaded policy and its approved amendments.

Which instruction is strongest?

A. Answer the questions clearly and confidently.  
B. Use only the supplied policy package, state `not covered` when the evidence is silent, and cite the controlling section for each material claim.  
C. Produce five answers and select the majority result.  
D. Use general knowledge to fill any missing policy detail.

**Best answer: B**

The response defines the evidence boundary, permits a supported non-answer, and makes material claims auditable.

---

## Question 4: Reconciliation mismatch

A structured cost table intended for an oversight report lists a subtotal of `$1,248,000`, while its line items sum to `$1,213,000`.

What should happen before use?

A. Accept the subtotal because the table is professionally formatted.  
B. Execute a reproducible recomputation, reconcile the discrepancy to the source records, and revise the table before review.  
C. Submit the report and explain the mismatch afterward.  
D. Reformat the subtotal in bold so the inconsistency is clearer.

**Best answer: B**

The defect is an internal arithmetic contradiction. Format changes do not resolve it, and a governed deliverable must not be released with the mismatch unresolved.

---

## Question 5: One analysis, two audiences

A verified operational analysis must support an executive decision and a working-team action plan.

What is the best approach?

A. Send the same complete draft to both groups.  
B. Produce an executive version leading with decision, impact, risk, and ask, plus a working-team version preserving method, dependencies, owners, and next steps.  
C. Give the raw model output to executives and the edited output to the team.  
D. Remove uncertainty from the executive version to make it decisive.

**Best answer: B**

Audience adaptation changes selection, depth, tone, and structure while preserving the verified facts, uncertainty, risks, and obligations.

---

## Question 6: Material multi-variable calculation

A pricing recommendation depends on currency conversion, tiered discounts, credits, date boundaries, and tax treatment.

Which path is strongest?

A. Ask for a concise inline total and inspect whether it looks reasonable.  
B. Request the result in a polished table.  
C. Define the business rules, execute the calculation over the actual data, review the code, reconcile the result, and retain the reproducibility record.  
D. Find a comparable public figure and use it as a substitute.

**Best answer: C**

The problem is exact computation. Code execution creates an inspectable and rerunnable calculation, although the logic, inputs, and interpretation still require review.

---

## Question 7: Noisy source package

A learner provides seven files: three drafts of the same procedure, two copies of an old version, one approved procedure, and one unrelated reference. The resulting summary repeats contradictions.

What is the best repair?

A. Use the same files with a more capable model.  
B. Identify the approved controlling version, preserve any material redlines separately, remove duplicates and irrelevant material, label each remaining source, and rerun.  
C. Ask for a longer summary.  
D. Paste the same files into a fresh conversation.

**Best answer: B**

The dominant failure is input quality. Curating the source set removes the cause rather than asking the model to reconcile avoidable noise.

---

# Quiz reasoning patterns

## Pattern 1: Separate accuracy from completeness

```text
Visible content correct
      ≠
Required content complete
```

Always compare the output against the full requirement set and expected source coverage.

## Pattern 2: Precision demands provenance

```text
Exact percentage, date, quote, or citation
      ↓
Locate source, scope, method, date, and support
```

Confidence and specificity do not establish truth.

## Pattern 3: Build verifiability into the prompt

```text
Evidence boundary
      +
Permission for unknown
      +
Auditable locations
      =
More reviewable output
```

These controls reduce unsupported completion and expose evidence gaps.

## Pattern 4: Reconcile contradictions deterministically

When totals, repeated facts, or calculations conflict:

1. identify the authoritative input;
2. define the calculation rule;
3. execute or independently recompute;
4. reconcile the difference;
5. correct dependent claims; and
6. apply the required release gate.

## Pattern 5: Adapt the presentation, not the truth

```text
Facts, uncertainty, risks, and obligations → invariant
Depth, order, vocabulary, tone, and format → audience-specific
```

## Pattern 6: Code execution is not automatic correctness

```text
Executed successfully
      ≠
Correct business rule
      ≠
Correct source data
      ≠
Approved result
```

Review the logic, inputs, parameters, output, and reconciliation.

## Pattern 7: Curate inputs before asking for better output

```text
De-duplicate
      ↓
Identify controlling versions
      ↓
Label source roles
      ↓
Prune irrelevant material
      ↓
Rerun against a clean evidence set
```

---

# Common distractors

## Switching models before fixing the workflow

A stronger model still receives the same incomplete requirements, unsupported evidence, contradictory sources, or wrong business rules.

## Trusting confidence or polish

Professional wording and clean formatting are presentation properties, not verification properties.

## Repeating the same request

Repeated generation may expose instability but cannot establish correctness without evidence or deterministic testing.

## Asking the model to certify itself

Self-review can surface possible issues, but it is not independent proof or qualified approval.

## Reformatting a substantive defect

Tables, charts, and artifacts can make a defect easier to read without making it correct.

## Treating structured output as factual validation

A schema can constrain shape. It cannot make an unsupported value true.

## Leaving noisy inputs unchanged

Longer context or a fresh conversation does not resolve duplicate, superseded, contradictory, or irrelevant sources.

---

# Certification shortcut

```text
Accurate figures, missing factor → completeness review
Precise claim, no source         → fabricated-specific risk
Document-only task               → source restriction + unknown + citation
Subtotal mismatch                → execute and reconcile
Two audiences                    → separate truth-preserving versions
Exact multi-variable math        → code execution + logic review
Overlapping sources              → curate inputs first
```

For each scenario:

1. identify the intended use;
2. identify the property that failed or remains unproven;
3. select the strongest evidence or computation method;
4. apply the required human-review threshold; and
5. state the release, revision, verification, escalation, or rejection action.

---

# Knowledge check

## Question 1

Can a report be accurate but incomplete?

**Answer:** Yes. Every included statement may be correct while a required or decision-critical factor is absent.

## Question 2

Why is an uncited precise statistic high risk?

**Answer:** Precision creates authority without proving provenance, population, method, scope, or currency.

## Question 3

What three prompt controls reduce hallucination in document-bound work?

**Answer:** Restrict the evidence set, permit explicit unknown or not-covered responses, and require auditable claim-to-source citations.

## Question 4

What should resolve an arithmetic contradiction?

**Answer:** Reproducible computation or authoritative-system reconciliation, followed by correction and review.

## Question 5

What remains fixed across audience variants?

**Answer:** Material facts, figures, uncertainty, risks, dependencies, obligations, and approved positions.

## Question 6

What remains unproven after code runs successfully?

**Answer:** The correctness of the code, business rules, data, filters, units, interpretation, and release authorization.

## Question 7

Why curate source inputs?

**Answer:** Duplicate, superseded, contradictory, unlabeled, or irrelevant sources increase noise, conflict, double counting, and review cost.

---

# Flashcards

## Flashcard 1

**Q:** What is the accuracy-completeness distinction?

**A:** Accuracy checks whether present content is correct; completeness checks whether required content is missing.

## Flashcard 2

**Q:** What is a fabricated specific?

**A:** A precise statistic, date, quotation, citation, or detail presented without adequate support.

## Flashcard 3

**Q:** What is the closed-source grounding trio?

**A:** Restrict to supplied sources, permit `unknown` or `not covered`, and require auditable citations.

## Flashcard 4

**Q:** What should happen when line items and subtotal conflict?

**A:** Recompute and reconcile before use.

## Flashcard 5

**Q:** How should one analysis serve two audiences?

**A:** Create separate versions from the same verified content model.

## Flashcard 6

**Q:** When is code execution preferred?

**A:** When exact calculation, transformation, filtering, reconciliation, or charting materially affects the result.

## Flashcard 7

**Q:** What are the three central input-curation actions?

**A:** De-duplicate, label and structure, and prune irrelevant material.

---

# Short recap

```text
1. Check completeness separately from accuracy.
2. Treat precise unsupported claims as high-risk.
3. Restrict document work to authorized sources and permit unknowns.
4. Recompute contradictions rather than reformatting them.
5. Adapt verified facts for each audience.
6. Execute material calculations and review the logic.
7. Curate noisy inputs before rerunning.
8. Do not confuse polish, structure, repetition, or model tier with proof.
9. Match review depth to the intended use and consequence.
10. Record the next responsible action.
```

> Full marks means recognizing what remains unproven and choosing the control that establishes it.

## Educational-use notice

This repository is an unofficial educational resource. All public quiz scenarios are original and fictional. The material does not constitute legal, financial, medical, audit, compliance, communications, data-engineering, or other professional advice.

## Related material

- [Self-Assessment](08b-self-assessment.md)
- [Exercise: Triage the Output Set](08a-triage-output-set.md)
- [Module 3 overview](../README.md)
- [Module 3 quiz prompt notebook](../../../prompts/module-03/09a-module-3-quiz-prompts.md)
- [Three-Reference Discernment Pattern](../../../patterns/three-reference-discernment-pattern.md)
- [Grounded Verification Pattern](../../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../../patterns/human-review-gate-pattern.md)
- [Audience Adaptation Pattern](../../../patterns/audience-adaptation-pattern.md)
- [Output Format and Reliability Pattern](../../../patterns/output-format-reliability-pattern.md)
