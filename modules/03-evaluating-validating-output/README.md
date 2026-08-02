# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

## Why this domain matters

A plausible output is not evidence of a reliable result. Evaluation determines whether an answer is accurate, complete, grounded, internally consistent, appropriately framed, suitable for its audience, and safe to use.

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
Release, edit, verify, escalate, or reject
```

> **Module thesis:** Fluency is not proof, and accuracy alone is not delivery readiness.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [x] [04. Fact-Checking & Grounding](lessons/04-fact-checking-grounding.md)
- [x] [05. Diligence: When Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [x] [06. Editing & Adapting for Audience](lessons/06-editing-adapting-audience.md)
- [ ] 07. Choosing Output Formats
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
Choose a usable output format
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

Ask:

```text
Did it do what I asked?
Does it match the evidence?
Would it be acceptable in the real setting where it will be used?
```

Accuracy asks whether what is present is correct. Completeness asks whether anything material is missing.

## 2. Failure patterns

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → tool and external-state verification
```

Failure families include hallucination, inconsistency, bias, silent omission, and capability hallucination.

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

Grounding creates traceability. Fact-checking and independent validation determine whether the claim is reliable.

## 4. Diligence and review gates

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What law, contract, policy, standard, or duty applies?
```

Mandatory-review classes include final external deliverables, audit-critical calculations, regulated or highly sensitive work, public or legal communications, consequential decisions, and irreversible actions.

```text
Expertise
  + Authority
  + Context
  + Evidence access
  + Time
  + Intervention rights
  = Meaningful human review
```

## 5. Editing and audience adaptation

A verified draft may still be unclear, poorly structured, written in the wrong register, or unsafe for the intended recipient.

Use three passes:

```text
Verified draft
      ↓
Clarity pass
      ↓
Tone pass
      ↓
Formatting pass
      ↓
Audience and integrity review
```

### Truth-preserving adaptation

```text
Facts, figures, uncertainty, risks, and obligations → remain invariant
Selection, depth, tone, order, and format           → adapt to audience
```

### Audience contract

Define:

- reader and expertise;
- purpose and expected decision;
- attention available;
- channel and format;
- tone and relationship;
- disclosure boundary; and
- material evidence that must remain visible.

### Candidate comparison

When quality matters, compare multiple drafts against the same criteria before selecting a base.

```text
Best-looking candidate
      ≠
Most accurate or complete candidate
```

Candidate comparison helps select a draft. It does not replace grounding, validation, or review.

---

# Four durable capabilities

## Discernment

Evaluate what the output says, what it contradicts, and what it leaves out.

## Grounding

Trace material claims to evidence with exact support, scope, date, and conditions.

## Diligence

Match review depth to consequence and place qualified human review before irreversible release or action.

## Adaptation and triage

Preserve verified content while changing the presentation for the audience, then choose:

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

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)
- [Editing and Audience Adaptation prompts](../../prompts/module-03/06-editing-adapting-audience-prompts.md)

## Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)
- [Grounded Verification Pattern](../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../patterns/human-review-gate-pattern.md)
- [Audience Adaptation Pattern](../../patterns/audience-adaptation-pattern.md)

## Existing module files

- [notes.md](notes.md): Exam-focused evaluation concepts and decision rules
- [lab.md](lab.md): Applied evaluation exercise with acceptance criteria
- [flashcards.md](flashcards.md): Baseline active-recall cards
- [quiz.md](quiz.md): Extended original scenario quiz

---

# Exam shortcuts

## Accuracy and completeness

```text
Requirements           → Did it do all requested work?
Source material        → Does evidence support each material claim?
Professional standards → Is the result fit for real use?
Accuracy               → Is what is present correct?
Completeness           → Is anything material missing?
```

## Failure patterns

```text
Precise number with no source         → fabricated-specific risk
Citation exists but mismatches        → claim-support failure
Repeated fact has two values          → inconsistency
Prompt assumes conclusion             → confirmation-bias risk
Required source absent                → completeness failure
Action claimed without receipt        → capability hallucination
```

## Fact-checking and grounding

```text
Evidence is silent         → permit unknown or not covered
Fixed document set         → restrict sources
Long or consequential text → quote first
Citation present           → inspect actual support
Runs disagree              → investigate instability
Runs agree                 → still verify material claims
Calculation matters        → recompute deterministically
```

## Diligence

```text
Low-stakes internal draft         → proportionate review
Final external deliverable        → qualified review
Audit-critical calculation        → deterministic verification + expert review
Regulated or sensitive work       → policy controls + authorized review
Irreversible action               → approval gate before execution
Iteration has plateaued           → fresh human judgment
```

## Editing for audience

```text
Accurate but verbose          → clarity pass
Accurate but wrong register   → tone pass
Accurate but hard to consume  → formatting pass
Same analysis, new audience   → preserve invariants and adapt depth
Several candidate drafts      → compare against common criteria
Short version drops a caveat  → restore decision-critical context
External version exposes internals → disclosure review
```

---

# Exam lens

For scenario questions:

1. identify what property needs evaluation;
2. determine purpose, stakes, audience, and governing obligations;
3. define the evidence boundary and authority hierarchy;
4. check requirements, sources, professional standards, and coverage;
5. distinguish accuracy, completeness, consistency, bias, audience fit, and format;
6. use deterministic checks for exact values and calculations;
7. identify required human-review gates;
8. preserve facts, uncertainty, risk, and obligations during adaptation;
9. distinguish safe brevity from misleading omission;
10. compare candidates by criteria rather than polish;
11. review disclosure before external release; and
12. choose release, edit, verify, escalate, or reject.

---

# Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed the Accuracy and Completeness lesson.
- [x] I completed the Hallucinations, Inconsistencies, and Bias lesson.
- [x] I completed the Fact-Checking and Grounding lesson.
- [x] I completed the Diligence and Human Review lesson.
- [x] I completed the Editing and Audience Adaptation lesson.
- [ ] I can apply the three evaluation references.
- [ ] I can review accuracy and completeness separately.
- [ ] I can identify hallucinations, contradictions, omissions, and biased framing.
- [ ] I can build a claim-evidence ledger and consistency matrix.
- [ ] I can distinguish citation presence from actual support.
- [ ] I can validate material claims and calculations independently.
- [ ] I can apply the four Diligence thresholds.
- [ ] I can define meaningful human-review qualifications.
- [ ] I can place a review gate before an irreversible action.
- [ ] I can define an audience contract.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish selective omission from misleading omission.
- [ ] I can compare candidate drafts against common criteria.
- [ ] I can review external adaptations for disclosure and commitments.
- [ ] I can choose a format that supports inspection and use.
- [ ] I can triage an output into release, edit, verify, escalate, or reject.
- [ ] I completed the preparation-course exercise, quiz, and takeaways.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, compliance, communications, or other professional advice. Current authoritative terms, policies, documentation, and organizational requirements control when conflicts exist.

## Official reading

- [AI Fluency Framework overview](https://www.anthropic.com/ai-fluency/overview)
- [AI Fluency: Discernment](https://www.anthropic.com/ai-fluency/discernment)
- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
