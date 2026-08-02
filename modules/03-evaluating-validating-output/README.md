# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — all teaching, exercise, quiz, and takeaway sections are complete. Module Complete remains open.

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
Triage and self-assessment
        ↓
Quiz and takeaway synthesis
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
- [ ] 10. Module Complete

## Completion record

```text
Triage exercise: 4/4 correct
Module 3 quiz: Full marks — 7/7
Optional self-assessment: Complete
Key takeaways: Reviewed
```

---

# Six durable takeaways

## 1. Accountability stays with the releasing human or organization

```text
Model assists
      ↓
Human evaluates and approves
      ↓
Organization releases and owns the consequences
```

AI assistance does not transfer professional duty, approval authority, data-handling obligations, or responsibility to correct errors.

## 2. Evaluate against three references

```text
Requirements
    +
Source material
    +
Professional standards
```

Then review accuracy and completeness separately:

```text
Accuracy     → Is what is present correct?
Completeness → Is anything material missing?
```

Review depth is calibrated to consequence, reversibility, audience, uncertainty, and governing obligations.

## 3. Plausible is not verified

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → verify tool and external state
```

A polished statement may still be unsupported, incomplete, inconsistent, biased, or unexecuted.

## 4. Build verification into the prompt

Use:

- explicit permission for `unknown` or `not covered`;
- a defined evidence boundary;
- auditable source locations;
- quote-first analysis for long or consequential material;
- controlled support statuses; and
- required independent checks.

```text
Citation present
      ≠
Claim supported
```

## 5. Know review thresholds in advance

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What rule, contract, policy, standard, or duty applies?
```

Mandatory-review classes include final external deliverables, audit-critical calculations, regulated or sensitive work, public or legal communications, consequential decisions, and irreversible actions.

Meaningful review requires expertise, authority, context, evidence access, time, independence, and intervention rights.

## 6. Pick the format by reliability

```text
Inline, artifact, structured → presentation and delivery
Code execution               → computation and processing
```

Use code execution for material calculations, but remember:

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

---

# Integrated evaluation workflow

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

## Integrated release question

```text
Is the output correct enough,
complete enough,
supported enough,
reviewed enough,
appropriate enough,
and reproducible enough
for this exact use?
```

---

# Exam shortcuts

```text
Accurate figures, missing factor → completeness review
Precise claim, no source         → fabricated-specific risk
Document-only task               → restrict sources + permit unknown + cite
Subtotal mismatch                → execute and reconcile
Two audiences                    → truth-preserving variants
Exact multi-variable math        → code execution + logic review
Overlapping sources              → curate inputs first
High-stakes external use         → qualified human review
```

For scenario questions:

1. identify the intended use and audience;
2. determine what property remains unproven;
3. select the smallest evidence, computation, adaptation, or review control that establishes it;
4. reject alternatives based only on confidence, polish, repetition, model tier, formatting, or schema validity; and
5. conclude with release, edit, verify, escalate, or reject.

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
- [Module 3 Quiz](lessons/09a-module-3-quiz.md)
- [Module 3 Key Takeaways](lessons/09b-key-takeaways.md)

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
- [Module 3 quiz and remediation prompts](../../prompts/module-03/09a-module-3-quiz-prompts.md)
- [Module 3 Key Takeaways prompts](../../prompts/module-03/09b-key-takeaways-prompts.md)

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

# Completion criteria

- [x] I completed all Module 3 teaching sections.
- [x] I completed the Triage exercise with 4/4 correct.
- [x] I completed the optional self-assessment.
- [x] I completed the Module 3 quiz with full marks, 7/7.
- [x] I reviewed the six Module 3 takeaways.
- [ ] I can apply the three evaluation references consistently.
- [ ] I can review accuracy and completeness separately.
- [ ] I can detect hallucinations, contradictions, omissions, and biased framing.
- [ ] I can distinguish citation presence from actual support.
- [ ] I can validate material claims and calculations independently.
- [ ] I can apply the four Diligence thresholds.
- [ ] I can define meaningful human-review qualifications.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish presentation format from computation method.
- [ ] I can curate inputs and preserve reproducibility evidence.
- [ ] I can triage an output and state the controlling next action.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples, questions, and reflections must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential conversation text, client data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, audit, compliance, communications, data-engineering, or other professional advice.

## Official reading

Product behavior can change. Verify current official documentation.

- [AI Fluency Framework overview](https://www.anthropic.com/ai-fluency/overview)
- [AI Fluency: Discernment](https://www.anthropic.com/ai-fluency/discernment)
- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
