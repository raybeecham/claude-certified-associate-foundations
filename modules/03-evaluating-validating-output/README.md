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
Release, edit, verify, escalate, or reject
```

> **Module thesis:** Fluency is not proof, accuracy alone is not delivery readiness, and presentation format is not verification.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [x] [04. Fact-Checking & Grounding](lessons/04-fact-checking-grounding.md)
- [x] [05. Diligence: When Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [x] [06. Editing & Adapting for Audience](lessons/06-editing-adapting-audience.md)
- [x] [07. Choosing Output Formats](lessons/07-choosing-output-formats.md)
- [ ] 08. Exercise: Triage the Output Set
  - [ ] Exercise
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
Triage: release, edit, verify, escalate, or reject
```

---

# Foundations

## 1. Accuracy and completeness

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
    ↓
Stakes-calibrated verdict
```

Accuracy asks whether what appears is correct. Completeness asks whether anything material is missing.

## 2. Failure patterns

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → verify tool and external state
```

## 3. Fact-checking and grounding

```text
Evidence boundary
      ↓
Permission for unknown
      ↓
Claim-to-source mapping
      ↓
Support classification
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

## 4. Diligence and review gates

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What law, contract, policy, standard, or duty applies?
```

Mandatory-review classes include final external deliverables, audit-critical calculations, regulated or sensitive work, public or legal communications, consequential decisions, and irreversible actions.

## 5. Editing and audience adaptation

```text
Facts, figures, uncertainty, risks, and obligations → remain invariant
Selection, depth, tone, order, and format           → adapt to audience
```

Use separate clarity, tone, formatting, invariant, and disclosure reviews.

## 6. Output formats and execution

The output container and computation method solve different problems.

```text
Inline, artifact, and structured output → delivery and presentation
Code execution                          → computation and processing
```

### Inline

Use for immediate contextual guidance inside the conversation.

### Artifact or reusable file

Use for standalone content that must be edited, reused, versioned, shared, or formally reviewed.

```text
Artifact created
      ≠
Deliverable approved
```

### Structured output

Use defined fields or schemas for consistent extraction, comparison, validation, and machine consumption.

```text
Valid schema
      ≠
Valid meaning
```

### Code-executed path

Use for material calculations, filtering, transformations, charts, reconciliation, and processed files.

```text
Inspect inputs
      ↓
Define business rules
      ↓
Review critical logic
      ↓
Execute
      ↓
Reconcile outputs
      ↓
Retain code and parameters
      ↓
Apply required human review
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

### Input curation

Before processing:

1. de-duplicate exact and near-duplicate sources;
2. identify authoritative and superseded versions;
3. label approved, draft, raw, processed, current, and reference inputs;
4. prune irrelevant content;
5. restrict sensitive material; and
6. inspect schema, units, currencies, dates, identifiers, and missing values.

---

# Output modality matrix

| Requirement | Inline | Artifact/file | Structured | Code-executed path |
|---|---:|---:|---:|---:|
| Quick conversational answer | Strong | Weak | Optional | If computation needed |
| Standalone deliverable | Weak | Strong | Optional | If processing needed |
| Repeated editing and reuse | Weak | Strong | Moderate | Produces reusable results |
| Machine consumption | Weak | Moderate | Strong | Often produces structured files |
| Exact aggregation | Weak | Weak alone | Weak alone | Strongest path |
| Chart from data | Weak | Strong destination | Strong source table | Required for computed chart |
| Formal version and approval | Weak | Strong | Moderate | Retain code and output artifacts |

Modalities may be combined:

```text
Code-executed analysis
        ↓
Structured result table
        ↓
Chart
        ↓
Standalone report
        ↓
Inline executive summary
```

---

# Four durable capabilities

## Discernment

Evaluate what the output says, what it contradicts, and what it leaves out.

## Grounding

Trace material claims to authoritative evidence and inspect actual support.

## Diligence

Match review depth to consequence and place qualified review before irreversible release or action.

## Adaptation and triage

Preserve verified content, select a usable format, and choose:

```text
Release
Edit
Verify
Escalate
Reject
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

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Editing and Audience Adaptation prompts](../../prompts/module-03/06-editing-adapting-audience-prompts.md)
- [Choosing Output Formats prompts](../../prompts/module-03/07-choosing-output-formats-prompts.md)

## Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)
- [Grounded Verification Pattern](../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../patterns/human-review-gate-pattern.md)
- [Audience Adaptation Pattern](../../patterns/audience-adaptation-pattern.md)
- [Output Format and Reliability Pattern](../../patterns/output-format-reliability-pattern.md)

## Existing module files

- [notes.md](notes.md): Exam-focused evaluation concepts and decision rules
- [lab.md](lab.md): Applied evaluation exercise with acceptance criteria
- [flashcards.md](flashcards.md): Baseline active-recall cards
- [quiz.md](quiz.md): Extended original scenario quiz

---

# Exam shortcuts

```text
Quick contextual guidance        → inline
Standalone editable deliverable  → artifact or file
Machine-consumed records         → structured schema
Material numeric calculation     → code execution
Chart from uploaded data         → execute + validate result table
Dirty source package             → curate before generation
Successful code with wrong rule  → review logic and reconcile
```

For scenario questions:

1. identify consumer and downstream use;
2. distinguish conversational from standalone output;
3. identify editability, reuse, and machine-readability needs;
4. separate presentation format from computation method;
5. use code execution for exact material calculations and charts;
6. validate code logic, inputs, units, filters, and reconciliations;
7. validate structured syntax and semantic meaning separately;
8. curate inputs through de-duplication, labeling, and pruning;
9. preserve provenance and reproducibility evidence;
10. apply audience adaptation and review gates; and
11. choose release, edit, verify, escalate, or reject.

---

# Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed Accuracy and Completeness.
- [x] I completed Hallucinations, Inconsistencies, and Bias.
- [x] I completed Fact-Checking and Grounding.
- [x] I completed Diligence and Human Review.
- [x] I completed Editing and Audience Adaptation.
- [x] I completed Choosing Output Formats.
- [ ] I can apply the three evaluation references.
- [ ] I can review accuracy and completeness separately.
- [ ] I can identify hallucinations, contradictions, omissions, and biased framing.
- [ ] I can distinguish citation presence from actual support.
- [ ] I can validate material claims and calculations independently.
- [ ] I can apply the four Diligence thresholds.
- [ ] I can define meaningful human-review qualifications.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish inline, artifact, structured, and code-executed paths.
- [ ] I can separate format validity from semantic correctness.
- [ ] I can curate an input package.
- [ ] I can define and audit a reproducibility package.
- [ ] I can triage an output into release, edit, verify, escalate, or reject.
- [ ] I completed the preparation-course exercise, quiz, and takeaways.
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
