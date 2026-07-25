# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the next active module.

## Why this domain matters

A plausible output is not evidence of a reliable result. Evaluation determines whether an answer is accurate, complete, grounded, internally consistent, appropriate for its audience, and safe to use.

Module 2 focused on specifying intended behavior. Module 3 focuses on inspecting observed behavior.

```text
Prompt specification
        ↓
Candidate output
        ↓
Discernment
        ↓
Verification and grounding
        ↓
Human-review decision
        ↓
Edit, release, escalate, or reject
```

> **Module thesis:** Fluency is not proof. An output must be evaluated against evidence, requirements, audience needs, and the consequences of error.

## Course-aligned lesson map

- [ ] 01. Module Introduction
- [ ] 02. Discernment: Accuracy & Completeness
- [ ] 03. Hallucinations, Inconsistencies & Bias
- [ ] 04. Fact-Checking & Grounding
- [ ] 05. Diligence: When Review Is Non-Negotiable
- [ ] 06. Editing & Adapting for Audience
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
Adapt the content for its actual audience
              ↓
Choose a usable output format
              ↓
Triage: release, edit, verify, escalate, or reject
```

## Four durable capabilities

### 1. Discernment

Evaluate what the output says and what it leaves out.

Key questions:

- Is each material claim accurate?
- Is the response complete enough for its intended purpose?
- Are assumptions, inferences, and facts distinguished?
- Does the answer contradict itself or the supplied evidence?
- Could framing, omissions, or generalizations introduce bias?

### 2. Grounding

Trace important claims back to evidence rather than relying on confident wording.

```text
Claim
  ↓
Source
  ↓
Support
  ↓
Scope and date
  ↓
Verified, qualified, unsupported, or conflicting
```

Grounding includes checking whether a cited source actually supports the claim, whether the source is authoritative for the question, and whether its scope and currency are appropriate.

### 3. Diligence

Match the depth of review to the consequences of error.

```text
Low consequence      → proportionate review
Material consequence → stronger validation
High consequence     → qualified human review is non-negotiable
```

Human review is not a ceremonial final glance. It must be performed by someone with the authority, expertise, context, and time needed to detect and correct consequential errors.

### 4. Adaptation and triage

A factually sound output may still be unusable if it is poorly framed, overly technical, incomplete for the audience, or returned in the wrong format.

The final decision is not merely `good` or `bad`:

```text
Release
Edit
Verify
Escalate
Reject
```

## Learning objectives

By the end of this module, you should be able to:

- distinguish fluent output from verified output;
- assess accuracy and completeness against an explicit purpose;
- identify hallucinations, contradictions, unsupported claims, and biased framing;
- verify material claims against authoritative and current evidence;
- distinguish grounded fact from inference, assumption, and uncertainty;
- determine when human review is required and what qualifies as meaningful review;
- adapt accurate content for different audiences without changing its meaning;
- choose output formats that make the result easier to inspect and use;
- triage outputs into release, edit, verify, escalate, or reject decisions;
- construct representative test sets with normal, edge, conflicting, missing, and adversarial cases;
- select code-based, human, and model-assisted grading methods; and
- distinguish average performance from release-blocking failures.

## Current module resources

- [notes.md](notes.md): Exam-focused evaluation concepts and decision rules
- [lab.md](lab.md): Applied evaluation exercise with acceptance criteria
- [flashcards.md](flashcards.md): Baseline active-recall cards
- [quiz.md](quiz.md): Extended original scenario quiz

Course-aligned lessons and prompt notebooks will be added as each section is completed.

## Module 2 to Module 3 bridge

Module 2 established the intended output contract:

```text
Task + evidence + constraints + output + success criteria
```

Module 3 asks whether the observed result satisfies that contract:

```text
Requirement
    ↓
Evaluation criterion
    ↓
Evidence or test
    ↓
Observed result
    ↓
Pass, revise, escalate, or fail
```

A vague requirement cannot be evaluated reliably. Conversely, a strong prompt does not remove the need to inspect the result.

## Exam lens

For scenario questions:

1. identify what property needs evaluation;
2. determine what evidence or reviewer can evaluate it;
3. distinguish factual accuracy from completeness, consistency, bias, audience fit, and format;
4. choose the least subjective reliable check;
5. escalate when the consequences exceed the model's authority or the available evidence; and
6. do not confuse confidence, polish, or citations alone with correctness.

The strongest answer usually establishes criteria and tests before changing the prompt. Match the grader to the property being measured. Exact labels favor deterministic checks, while nuanced policy, domain expertise, or high-impact judgment requires qualified human review.

## Completion criteria

- [ ] I can assess accuracy and completeness against a defined purpose.
- [ ] I can identify hallucinations, contradictions, unsupported claims, and biased framing.
- [ ] I can verify claim-to-source support, authority, scope, and currency.
- [ ] I can explain when human review is non-negotiable.
- [ ] I can adapt an output for an audience without distorting its meaning.
- [ ] I can choose an output format that supports inspection and use.
- [ ] I can triage an output into release, edit, verify, escalate, or reject.
- [ ] I can build a representative evaluation set.
- [ ] I can justify the selected grader or review method.
- [ ] I completed the preparation-course exercise, quiz, and takeaways.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Official reading

Product behavior and evaluation recommendations can change. Verify current official guidance before relying on implementation-specific details.

- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
