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
Triage disposition
```

> **Module thesis:** Fluency is not proof, accuracy alone is not delivery readiness, and appearance is not the same axis as risk.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [x] [04. Fact-Checking & Grounding](lessons/04-fact-checking-grounding.md)
- [x] [05. Diligence: When Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [x] [06. Editing & Adapting for Audience](lessons/06-editing-adapting-audience.md)
- [x] [07. Choosing Output Formats](lessons/07-choosing-output-formats.md)
- [ ] 08. Exercise: Triage the Output Set
  - [x] [Exercise — 4/4 correct](lessons/08a-triage-output-set.md)
  - [ ] Self-Assessment
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
Triage: ready, revise, or human override
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

## Three exercise verdicts

| Verdict | Use |
|---|---|
| **Ready to use** | Adequate for the stated low-risk use, possibly after light editing |
| **Needs revision** | A bounded defect can be repaired, verified, and re-evaluated |
| **Needs human override** | Consequence, authority, uncertainty, or governing obligations require qualified human control |

## Mapping to the wider module

| Exercise verdict | Wider actions |
|---|---|
| Ready to use | Release for the stated use |
| Needs revision | Edit and/or Verify |
| Needs human override | Escalate, reconstruct, or Reject |

## Course exercise result

```text
4 of 4 classifications correct
```

The completed classifications demonstrated:

- proportionate use of a low-stakes internal draft;
- deterministic repair of an inconsistent total;
- source validation for untraceable statistics; and
- mandatory qualified review for a regulatory submission.

> The roughest-looking output may be the lowest risk. The cleanest-looking output may carry the strongest review gate.

---

# Triage protocol

```text
1. Define intended use and audience
          ↓
2. Assess output condition
          ↓
3. Apply requirements, sources, and professional standards
          ↓
4. Apply stakes, reversibility, audience, and governing obligations
          ↓
5. Identify the controlling issue
          ↓
6. Choose ready, revise, or human override
          ↓
7. State the next action and owner
```

Use this sentence structure:

```text
[VERDICT] because [CONTROLLING REASON]; next, [REQUIRED ACTION].
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

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Editing and Audience Adaptation prompts](../../prompts/module-03/06-editing-adapting-audience-prompts.md)
- [Choosing Output Formats prompts](../../prompts/module-03/07-choosing-output-formats-prompts.md)
- [Triage Output Set prompts](../../prompts/module-03/08a-triage-output-set-prompts.md)

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
```

For scenario questions:

1. identify intended use and audience;
2. assess the output against requirements and evidence;
3. identify bounded defects;
4. apply stakes, reversibility, audience, and governing obligations;
5. recognize automatic human-review gates;
6. separate appearance from risk;
7. choose ready to use, needs revision, or needs human override; and
8. state the required next action.

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
- [ ] I completed the Triage self-assessment.
- [ ] I can apply the three evaluation references.
- [ ] I can distinguish output condition from use risk.
- [ ] I can distinguish ready to use, needs revision, and needs human override.
- [ ] I can identify bounded defects suitable for revision.
- [ ] I can recognize mandatory human-review gates.
- [ ] I can state a controlling reason and next action.
- [ ] I can validate material claims and calculations independently.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish format validity from semantic correctness.
- [ ] I completed the Module 3 quiz and takeaways.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, audit, compliance, communications, data-engineering, or other professional advice.

## Official reading

Product behavior can change. Verify current official documentation.

- [Artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Create and edit files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
