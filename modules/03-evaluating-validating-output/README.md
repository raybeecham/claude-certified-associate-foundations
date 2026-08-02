# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** Complete — 2 of 2 checkpoints passed.

## Module thesis

> Fluency is not proof. Accuracy alone is not delivery readiness, and responsible use requires evidence, proportionate review, appropriate presentation, reproducible computation, and explicit release judgment.

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
Triage and release decision
```

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
- [x] 09. Module 3 Quiz
  - [x] [Quiz — Full marks, 7/7](lessons/09a-module-3-quiz.md)
  - [x] [Key Takeaways](lessons/09b-key-takeaways.md)
- [x] [10. Module Complete](lessons/10-module-complete.md)

## Completion record

```text
Course checkpoints:       2 of 2 passed
Triage exercise:          4 of 4 correct
Module 3 quiz:            Full marks — 7 of 7
Optional self-assessment: Complete
Key takeaways:            Reviewed
```

## Six durable takeaways

### 1. Accountability stays with the releasing human or organization

```text
Model assists
      ↓
Human evaluates and approves
      ↓
Organization releases and owns the consequences
```

### 2. Evaluate against three references

```text
Requirements
    +
Source material
    +
Professional standards
```

Then review accuracy and completeness separately.

### 3. Plausible is not verified

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → verify tool and external state
```

### 4. Build verification into the prompt and workflow

Use explicit uncertainty behavior, evidence boundaries, auditable citations, quote-first extraction, support classifications, authoritative validation, and deterministic checks.

```text
Citation present
      ≠
Claim supported
```

### 5. Know human-review thresholds in advance

```text
Stakes
Reversibility
Audience
Regulatory, contractual, policy, or professional exposure
```

Meaningful review requires expertise, authority, context, evidence access, time, independence, and intervention rights.

### 6. Pick the format by reliability

```text
Inline, artifact, structured → presentation and delivery
Code execution               → computation and processing
```

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

## Integrated evaluation workflow

```text
1. Define the task and intended use
          ↓
2. Check requirements, sources, and professional standards
          ↓
3. Review accuracy and completeness
          ↓
4. Scan failure signatures
          ↓
5. Ground and independently verify material claims
          ↓
6. Apply Diligence thresholds and review gates
          ↓
7. Adapt for the audience without changing the facts
          ↓
8. Select the output container and computation method
          ↓
9. Triage: release, edit, verify, escalate, or reject
          ↓
10. Record approval, limitations, and correction ownership
```

## Associate path

| Module | Capability | Status |
|---|---|---|
| M1 — Product & Model Selection | Choose the right entry point, model, and features | Complete |
| M2 — Prompting | Build structured prompts and adapt them to task type | Complete |
| **M3 — Output Evaluation** | Validate output and identify mandatory human review | **Complete** |
| **M4 — Workflow Integration** | Map workflows against Delegation criteria and redesign them safely | **Up next** |
| M5 — Configuration | Configure Projects, instructions, and knowledge | Later |
| M6 — Governance | Apply use-case, data, policy, and ethics judgment | Later |
| M7 — Troubleshooting | Diagnose and improve underperforming workflows | Later |
| M8 — Course Summary & Next Steps | Consolidate learning and prepare for the exam | Final synthesis |

## Transition to Module 4

Module 3 asked:

```text
Is this output trustworthy and releasable?
```

Module 4 asks:

```text
How should the surrounding workflow assign responsibility across
models, deterministic logic, tools, storage, and human reviewers?
```

Continue with [Module 4: Workflow Integration & Solutions Design](../04-workflow-integration-solutions-design/README.md).

## Current module resources

### Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Accuracy and Completeness](lessons/02-discernment-accuracy-completeness.md)
- [Hallucinations, Inconsistencies, and Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [Fact-Checking and Grounding](lessons/04-fact-checking-grounding.md)
- [Diligence and Human Review](lessons/05-diligence-human-review.md)
- [Editing and Audience Adaptation](lessons/06-editing-adapting-audience.md)
- [Choosing Output Formats](lessons/07-choosing-output-formats.md)
- [Triage Exercise](lessons/08a-triage-output-set.md)
- [Self-Assessment](lessons/08b-self-assessment.md)
- [Module 3 Quiz](lessons/09a-module-3-quiz.md)
- [Key Takeaways](lessons/09b-key-takeaways.md)
- [Module Complete](lessons/10-module-complete.md)

### Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Audience Adaptation prompts](../../prompts/module-03/06-editing-adapting-audience-prompts.md)
- [Output Formats prompts](../../prompts/module-03/07-choosing-output-formats-prompts.md)
- [Triage prompts](../../prompts/module-03/08a-triage-output-set-prompts.md)
- [Self-Assessment prompts](../../prompts/module-03/08b-self-assessment-prompts.md)
- [Quiz and remediation prompts](../../prompts/module-03/09a-module-3-quiz-prompts.md)
- [Key Takeaways prompts](../../prompts/module-03/09b-key-takeaways-prompts.md)
- [Completion and transition prompts](../../prompts/module-03/10-module-complete-prompts.md)

### Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)
- [Grounded Verification Pattern](../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../patterns/human-review-gate-pattern.md)
- [Audience Adaptation Pattern](../../patterns/audience-adaptation-pattern.md)
- [Output Format and Reliability Pattern](../../patterns/output-format-reliability-pattern.md)

## Optional extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Public-repository scenario policy

Examples, questions, and reflections must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential conversation text, client data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, audit, compliance, communications, data-engineering, or other professional advice.
