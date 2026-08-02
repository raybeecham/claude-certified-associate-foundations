# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

## Module thesis

> Fluency is not proof. Accuracy alone is not delivery readiness, and responsible use requires evidence, proportionate review, appropriate presentation, and explicit release judgment.

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
Quiz synthesis
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
- [ ] 09. Module 3 Quiz
  - [x] [Quiz — Full marks, 7/7](lessons/09a-module-3-quiz.md)
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
Triage the output and review your own behavior
              ↓
Integrate the framework under quiz conditions
```

---

# Evaluation framework

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
```

Accuracy asks whether what is present is correct. Completeness asks whether anything material is missing.

## 2. Failure signatures

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → verify tool and external state
```

## 3. Grounding and fact-checking

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

## 4. Diligence

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What rule, contract, policy, or duty applies?
```

Mandatory-review classes include final external deliverables, audit-critical calculations, regulated or sensitive work, public or legal communications, consequential decisions, and irreversible actions.

## 5. Audience adaptation

```text
Facts, figures, uncertainty, risks, and obligations → remain invariant
Selection, depth, tone, order, and format           → adapt to audience
```

## 6. Output format and execution

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

## 7. Triage

```text
Output condition
      +
Intended-use risk
      ↓
Ready to use / Needs revision / Needs human override
```

The triage exercise was completed with **4 of 4 classifications correct**.

## 8. Self-assessment

```text
Discernment → Did the response actually fit the question and requirements?
Diligence   → Was the output checked before use at a level appropriate to the stakes?
```

The optional reflection documented a shift from generic prompting toward explicit specification and verification.

---

# Module 3 quiz result

```text
Full marks — 7 of 7
```

The quiz demonstrated command of seven judgment domains:

| Domain | Governing distinction |
|---|---|
| Accuracy and completeness | Correct visible content does not prove full coverage |
| Hallucination detection | Precise unsupported details require provenance |
| Grounded prompting | Restrict sources, permit unknowns, require citations |
| Internal consistency | Recompute and reconcile numeric contradictions |
| Audience adaptation | Preserve truth while changing depth and presentation |
| Numeric reliability | Execute material calculations and review logic |
| Input curation | De-duplicate, label, and prune before rerunning |

## Quiz shortcut

```text
Accurate figures, missing factor → completeness review
Precise claim, no source         → fabricated-specific risk
Document-only task               → source restriction + unknown + citation
Subtotal mismatch                → execute and reconcile
Two audiences                    → truth-preserving variants
Exact multi-variable math        → code execution + logic review
Overlapping sources              → curate inputs first
```

## Quiz reasoning sequence

```text
Observe the scenario
      ↓
Identify what remains unproven
      ↓
Select the evidence, computation, adaptation, or review control
      ↓
Reject irrelevant complexity
      ↓
State the next responsible action
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
- [Module 3 Quiz](lessons/09a-module-3-quiz.md)

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

# Exam lens

For scenario questions:

1. identify intended use and audience;
2. compare the output with requirements and evidence;
3. separate accuracy from completeness;
4. detect unsupported precision, contradictions, bias, and omissions;
5. define the evidence boundary and strongest source;
6. use deterministic computation for material math;
7. preserve factual invariants across audience versions;
8. curate duplicate or contradictory inputs;
9. apply stakes, reversibility, audience, and governing obligations;
10. choose the smallest responsible intervention; and
11. conclude with release, edit, verify, escalate, or reject.

Do not confuse confidence, polish, citations, schema validity, execution success, or a stronger model with proof.

---

# Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed Accuracy and Completeness.
- [x] I completed Hallucinations, Inconsistencies, and Bias.
- [x] I completed Fact-Checking and Grounding.
- [x] I completed Diligence and Human Review.
- [x] I completed Editing and Audience Adaptation.
- [x] I completed Choosing Output Formats.
- [x] I completed the Triage exercise with 4/4 correct.
- [x] I completed the optional self-assessment.
- [x] I completed the Module 3 quiz with full marks, 7/7.
- [ ] I completed the Module 3 takeaways.
- [ ] I can apply the three evaluation references consistently.
- [ ] I can review accuracy and completeness separately.
- [ ] I can identify hallucinations, contradictions, omissions, and biased framing.
- [ ] I can distinguish citation presence from actual support.
- [ ] I can validate material claims and calculations independently.
- [ ] I can apply the four Diligence thresholds.
- [ ] I can define meaningful human-review qualifications.
- [ ] I can preserve invariant content across audience versions.
- [ ] I can distinguish presentation format from computation method.
- [ ] I can curate an input package and preserve reproducibility evidence.
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
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
