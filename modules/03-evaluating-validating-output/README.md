# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

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

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
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

## Introduction foundation

Professional AI use contains an accountability asymmetry:

```text
Immediate, visible benefit
          ↓
Faster drafting and synthesis

Delayed, less visible risk
          ↓
Rework, poor decisions, credibility loss, or harm
```

A polished output can contain one plausible unsupported claim among many correct statements. The reviewer must therefore evaluate evidence and consequence rather than relying on tone, confidence, or surface coherence.

The introduction anchors the module in two AI Fluency competencies:

```text
Discernment → How should this output be evaluated?
Diligence   → What responsibility must be satisfied before it is used?
```

It also introduces **verification debt**: unresolved validation work that accumulates when AI-assisted generation exceeds the workflow's review capacity.

## Accuracy and completeness foundation

Discernment begins by checking the output against three stable references:

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

### Beginner version

Ask:

```text
Did it do what I asked?
        ↓
Does it match the evidence?
        ↓
Would it be acceptable in the real setting where it will be used?
```

Then separate two questions:

```text
Accuracy     → Is what is present correct?
Completeness → Is anything important missing?
```

An output can be accurate but incomplete. A project summary may correctly state a target date while omitting the approval dependency that determines whether the date is realistic.

### Grocery-order analogy

Reviewing AI output is like checking a grocery delivery:

- requirements are the order list;
- source material is the receipt and product labels; and
- professional standards include basic quality and safety expectations.

Receiving the correct pasta does not make the delivery complete when the sauce is missing. Correct visible statements do not compensate for omitted decision-critical information.

### Three-way verdict

```text
Ready to use
Needs revision
Needs human override
```

The verdict must be scoped to the intended audience and use. A discussion starter may be ready for an internal meeting but not ready for a client, regulator, or final operational decision.

## Four durable capabilities

### 1. Discernment

Evaluate what the output says and what it leaves out.

Key questions:

- Is each material claim accurate?
- Is the response complete enough for its intended purpose?
- Are assumptions, inferences, and facts distinguished?
- Does the answer contradict itself or the supplied evidence?
- Could framing, omissions, or generalizations introduce bias?

The lesson uses this repeatable protocol:

```text
Define purpose and stakes
          ↓
Check requirements
          ↓
Check source support
          ↓
Check professional standards
          ↓
Review accuracy
          ↓
Review completeness
          ↓
Assign and document a verdict
```

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

Human review is not a ceremonial final glance. It must be performed by someone with the authority, expertise, context, evidence access, and time needed to detect and correct consequential errors.

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

The three-way lesson verdict maps into the wider module triage model:

| Lesson verdict | Wider module action |
|---|---|
| Ready to use | Release for the stated use |
| Needs revision | Edit or verify, then re-evaluate |
| Needs human override | Escalate, reconstruct, or reject |

## Learning objectives

By the end of this module, you should be able to:

- distinguish fluent output from verified output;
- assess accuracy and completeness against an explicit purpose;
- evaluate output against requirements, source material, and professional standards;
- separate visible inaccuracies from material omissions;
- calibrate review depth to consequence, reversibility, uncertainty, and evidence quality;
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

### Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Discernment: Accuracy and Completeness](lessons/02-discernment-accuracy-completeness.md)

### Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)

### Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)

### Existing module files

- [notes.md](notes.md): Exam-focused evaluation concepts and decision rules
- [lab.md](lab.md): Applied evaluation exercise with acceptance criteria
- [flashcards.md](flashcards.md): Baseline active-recall cards
- [quiz.md](quiz.md): Extended original scenario quiz

Additional course-aligned lessons and notebooks will be added as each section is completed.

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

## Accuracy and completeness exam shortcut

```text
Requirements           → Did it do all requested work?
Source material        → Does the evidence support each material claim?
Professional standards → Is the result fit for real use?
Accuracy               → Is what is present correct?
Completeness           → Is anything material missing?
Stakes                 → How much review is required?
```

For verdict questions:

- choose **ready to use** only when requirements, evidence, standards, and review depth all pass for the stated use;
- choose **needs revision** when bounded defects can be corrected and rechecked; and
- choose **needs human override** when the stakes, uncertainty, missing authority, missing evidence, or severity of defects require qualified human ownership.

Do not confuse a citation, confident tone, polished structure, or a generally correct answer with complete professional fitness.

## Exam lens

For scenario questions:

1. identify what property needs evaluation;
2. determine the intended purpose and stakes;
3. check requirements, sources, and professional standards;
4. distinguish factual accuracy from completeness, consistency, bias, audience fit, and format;
5. choose the least subjective reliable check;
6. escalate when the consequences exceed the model's authority or the available evidence; and
7. do not confuse confidence, polish, or citations alone with correctness.

The strongest answer usually establishes criteria and tests before changing the prompt. Match the grader to the property being measured. Exact labels favor deterministic checks, while nuanced policy, domain expertise, or high-impact judgment requires qualified human review.

## Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed the Discernment: Accuracy and Completeness lesson.
- [ ] I can explain the accountability asymmetry in professional AI use.
- [ ] I can distinguish Discernment from Diligence.
- [ ] I can identify verification debt in a workflow.
- [ ] I can apply the three evaluation references.
- [ ] I can review accuracy and completeness separately.
- [ ] I can calibrate review depth to the stakes.
- [ ] I can distinguish ready to use, needs revision, and needs human override.
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

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, compliance, or other professional advice. Product behavior, interfaces, policies, and documentation can change. Current authoritative terms, policies, documentation, and organizational requirements control when conflicts exist.

## Official reading

Product behavior and evaluation recommendations can change. Verify current official guidance before relying on implementation-specific details.

- [AI Fluency Framework overview](https://www.anthropic.com/ai-fluency/overview)
- [AI Fluency: Discernment](https://www.anthropic.com/ai-fluency/discernment)
- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
