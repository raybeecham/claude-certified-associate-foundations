# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

## Why this domain matters

A plausible output is not evidence of a reliable result. Evaluation determines whether an answer is accurate, complete, grounded, internally consistent, appropriate for its audience, delivered in a usable format, and safe to release.

```text
Prompt specification
        ↓
Candidate output
        ↓
Discernment
        ↓
Verification and grounding
        ↓
Diligence and human-review gate
        ↓
Audience adaptation
        ↓
Format and execution selection
        ↓
Triage and self-assessment
```

> **Module thesis:** Fluency is not proof, accuracy alone is not delivery readiness, and responsible use requires reviewing both the output and your own behavior.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [x] [04. Fact-Checking & Grounding](lessons/04-fact-checking-grounding.md)
- [x] [05. Diligence: When Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [x] [06. Editing & Adapting for Audience](lessons/06-editing-adapting-audience.md)
- [x] [07. Choosing Output Formats](lessons/07-choosing-output-formats.md)
- [x] 08. Exercise: Triage the Output Set
  - [x] [Exercise — 4/4 correct](lessons/08a-triage-output-set.md)
  - [x] [Optional Self-Assessment](lessons/08b-self-assessment.md)
- [ ] 09. Module 3 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 10. Module Complete

## Learning progression

```text
Inspect accuracy and completeness
              ↓
Detect hallucinations, inconsistencies, and bias
              ↓
Verify claims against authoritative evidence
              ↓
Determine when qualified human review is mandatory
              ↓
Adapt verified content for the audience
              ↓
Choose the output container and computation method
              ↓
Triage the output
              ↓
Review your own Discernment and Diligence behavior
```

---

# Evaluation foundations

## Accuracy and completeness

```text
Requirements
    +
Source material
    +
Professional standards
    ↓
Accuracy review
    +
Completeness review
```

Accuracy asks whether what is present is correct. Completeness asks whether anything material is missing.

## Failure signatures

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → verify tool and external state
```

## Grounding

```text
Evidence boundary
      ↓
Permission for unknown
      ↓
Claim-to-source mapping
      ↓
Independent validation
      ↓
Deterministic checks and qualified review
```

```text
Citation present
      ≠
Claim supported
```

## Diligence

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What rule, contract, policy, or duty applies?
```

## Audience adaptation

```text
Facts, figures, uncertainty, risks, and obligations → remain invariant
Selection, depth, tone, order, and format           → adapt to audience
```

## Output format and execution

```text
Inline, artifact, and structured output → delivery and presentation
Code execution                          → computation and processing
```

```text
Executed successfully
      ≠
Correct logic
      ≠
Correct data
      ≠
Release approval
```

---

# Triage foundation

Triage evaluates two different axes:

```text
Output condition
      +
Intended-use risk
      ↓
Verdict and next action
```

| Verdict | Use |
|---|---|
| **Ready to use** | Adequate for the stated low-risk use, possibly after light editing |
| **Needs revision** | A bounded defect can be repaired, verified, and re-evaluated |
| **Needs human override** | Consequence, authority, uncertainty, or governing obligations require qualified human control |

## Course exercise result

```text
4 of 4 classifications correct
```

The exercise demonstrated:

- proportionate use of a low-stakes internal draft;
- deterministic repair of an inconsistent total;
- source validation for untraceable statistics; and
- mandatory qualified review for a regulatory submission.

> The roughest-looking output may be the lowest risk. The cleanest-looking output may carry the strongest review gate.

---

# Self-assessment foundation

The optional self-assessment asks whether the learner applied the module's behavioral indicators to a real conversation.

```text
Discernment → Did the response actually fit the question and requirements?
Diligence   → Was the output checked before use at a level appropriate to the stakes?
```

## Recorded reflection

> My prompts were very generic initially, but I have since learned the different factors to consider, how to request the output more clearly, and why I need to verify the result before relying on it.

## Indicator comparison

| Indicator | Evidence in the reflection | Assessment |
|---|---|---|
| **Discernment** | The learner now considers task specification and whether the result fits the intended request | Developing into a deliberate strength |
| **Diligence** | The learner explicitly recognizes the need to verify output before use | Developing into a deliberate strength |

## Strong behavior

The learner has shifted from casual, generic prompting toward a structured workflow that considers context, constraints, evidence, output requirements, and evaluation.

## Next tightening action

Convert the general intention to `verify everything` into explicit controls:

```text
Material claim
      ↓
Authoritative source or test
      ↓
Recorded result
      ↓
Review threshold
      ↓
Release or escalation decision
```

This self-assessment is optional and qualitative. It is not scored.

---

# Integrated protocol

```text
1. Define the intended task and use
          ↓
2. Specify context, evidence, constraints, and output
          ↓
3. Evaluate requirements, accuracy, and completeness
          ↓
4. Detect hallucinations, contradictions, bias, and omissions
          ↓
5. Ground and validate material claims
          ↓
6. Apply Diligence thresholds and review gates
          ↓
7. Adapt for audience without changing the facts
          ↓
8. Select the output modality and computation method
          ↓
9. Triage: ready, revise, or human override
          ↓
10. Reflect on Discernment and Diligence behavior
```

---

# Current module resources

## Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Discernment: Accuracy and Completeness](lessons/02-discernment-accuracy-completeness.md)
- [Hallucinations, Inconsistencies, and Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [Fact-Checking and Grounding Techniques](lessons/04-fact-checking-grounding.md)
- [Diligence: When Human Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [Editing and Adapting Output for Your Audience](lessons/06-editing-adapting-audience.md)
- [Choosing Output Formats](lessons/07-choosing-output-formats.md)
- [Exercise: Triage the Output Set](lessons/08a-triage-output-set.md)
- [Self-Assessment: Score Your Own Conversation](lessons/08b-self-assessment.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Editing and Audience Adaptation prompts](../../prompts/module-03/06-editing-adapting-audience-prompts.md)
- [Choosing Output Formats prompts](../../prompts/module-03/07-choosing-output-formats-prompts.md)
- [Triage Output Set prompts](../../prompts/module-03/08a-triage-output-set-prompts.md)
- [Self-Assessment prompts](../../prompts/module-03/08b-self-assessment-prompts.md)

## Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)
- [Grounded Verification Pattern](../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../patterns/human-review-gate-pattern.md)
- [Audience Adaptation Pattern](../../patterns/audience-adaptation-pattern.md)
- [Output Format and Reliability Pattern](../../patterns/output-format-reliability-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam shortcuts

```text
Low-risk provisional draft       → ready with proportionate editing
Internal contradiction           → revise and recompute
Untraceable precise claim        → revise and validate sources
Regulatory or consequential use  → qualified human override
Response sounds good             → still compare with the actual question
Output will be used              → verify at a level matched to the stakes
Generic promise to verify        → define sources, tests, reviewers, and blockers
```

For scenario questions:

1. identify intended use and audience;
2. assess the output against requirements and evidence;
3. identify bounded defects;
4. apply stakes, reversibility, audience, and governing obligations;
5. recognize automatic human-review gates;
6. separate appearance from risk;
7. choose ready to use, needs revision, or needs human override;
8. state the required next action; and
9. distinguish Discernment behavior from Diligence behavior.

---

# Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed Accuracy and Completeness.
- [x] I completed Hallucinations, Inconsistencies, and Bias.
- [x] I completed Fact-Checking and Grounding.
- [x] I completed Diligence and Human Review.
- [x] I completed Editing and Audience Adaptation.
- [x] I completed Choosing Output Formats.
- [x] I completed the Triage the Output Set exercise with 4/4 correct.
- [x] I completed the optional Triage self-assessment.
- [ ] I can apply the three evaluation references.
- [ ] I can distinguish output condition from use risk.
- [ ] I can distinguish ready to use, needs revision, and needs human override.
- [ ] I can identify bounded defects suitable for revision.
- [ ] I can recognize mandatory human-review gates.
- [ ] I can state a controlling reason and next action.
- [ ] I can distinguish Discernment from Diligence in my own workflow.
- [ ] I can convert a general verification intention into explicit controls.
- [ ] I can validate material claims and calculations independently.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish format validity from semantic correctness.
- [ ] I completed the Module 3 quiz and takeaways.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples and reflections must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential conversation text, client data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, audit, compliance, communications, data-engineering, or other professional advice.

## Official reading

Product behavior can change. Verify current official documentation.

- [AI Fluency Framework overview](https://www.anthropic.com/ai-fluency/overview)
- [AI Fluency: Discernment](https://www.anthropic.com/ai-fluency/discernment)
- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
