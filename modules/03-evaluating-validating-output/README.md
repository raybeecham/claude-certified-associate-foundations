# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

## Why this domain matters

A plausible output is not evidence of a reliable result. Evaluation determines whether an answer is accurate, complete, grounded, internally consistent, appropriately framed, suitable for its audience, and safe to use.

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

> **Module thesis:** Fluency is not proof. An output must be evaluated against evidence, requirements, internal consistency, audience needs, and the consequences of error.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
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

## Failure-pattern foundation

Plausible language does not reveal whether a claim is supported, a document is internally consistent, the framing is fair, the evidence set is complete, or an external action occurred.

### Beginner version

Ask:

```text
Did Claude add anything the evidence does not support?
                         ↓
Does one part disagree with another?
                         ↓
Does the framing unfairly favor one conclusion?
                         ↓
Did it skip an important source, option, risk, or condition?
                         ↓
Did it claim an action without a verified tool result?
```

These questions map to:

| Failure family | Meaning |
|---|---|
| Hallucination | A claim is presented with more support than the evidence justifies |
| Inconsistency | Parts of the output, or the output and evidence, cannot all be correct |
| Bias | Selection, framing, emphasis, or scrutiny is uneven relative to criteria and evidence |
| Completeness failure | A material source, requirement, option, condition, or risk is absent |
| Capability hallucination | An external action is claimed without verified execution and external-state confirmation |

### Road-trip analogy

A generated route can fail even when it looks polished:

- a nonexistent road is a hallucination;
- conflicting directions are an inconsistency;
- favoring the scenic route despite a fastest-route objective is bias;
- omitting a road closure is a completeness failure; and
- claiming the hotel was booked without a booking capability or receipt is a capability hallucination.

### High-value signatures

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → tool and external-state verification
```

### Durable action boundary

Claude capabilities vary by product surface, connected tools, permissions, and approvals. The stable rule is:

> An external action is verified only when the required capability was available, the action was invoked successfully, and the resulting external state or artifact confirms completion.

A conversational statement is not an action receipt.

## Four durable capabilities

### 1. Discernment

Evaluate what the output says, what it contradicts, and what it leaves out.

Key questions:

- Is each material claim accurate and supported?
- Is the response complete enough for its intended purpose?
- Are assumptions, inferences, and facts distinguished?
- Does the answer contradict itself or the supplied evidence?
- Could framing, omissions, or unequal scrutiny introduce bias?
- Did the output claim an external action without confirmation?

The combined discernment protocol is:

```text
Define purpose and stakes
          ↓
Check requirements and coverage
          ↓
Inventory material claims and actions
          ↓
Check source support and professional standards
          ↓
Review accuracy and completeness
          ↓
Scan hallucination signatures
          ↓
Compare repeated facts
          ↓
Challenge favored conclusions
          ↓
Confirm external actions
          ↓
Assign and document a disposition
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

Grounding includes checking whether a cited source exists, whether it supports the full claim, whether it is authoritative for the question, and whether scope, conditions, and currency are appropriate.

### 3. Diligence

Match review depth to the consequences of error.

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

The earlier three-way lesson verdict maps into the wider triage model:

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
- detect plausible-but-unsupported claims and fabricated specifics;
- calibrate language certainty to evidence strength;
- identify internal, source, temporal, and arithmetic inconsistencies;
- identify confirmation, selection, framing, and omission bias;
- distinguish fair treatment from false balance;
- verify source and requirement coverage across document batches;
- verify claimed external actions using tool and system records;
- calibrate review depth to consequence, reversibility, uncertainty, and evidence quality;
- verify material claims against authoritative and current evidence;
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
- [Hallucinations, Inconsistencies, and Bias](lessons/03-hallucinations-inconsistencies-bias.md)

### Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)

### Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)

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

## Failure-pattern exam shortcut

```text
Precise number with no source  → fabricated-specific risk
Citation exists but mismatches → claim-support failure
Absolute answer in conditional domain → certainty mismatch
Repeated fact has two values   → inconsistency
Prompt assumes conclusion      → confirmation-bias risk
Required file absent           → completeness failure
Action claimed without receipt → capability hallucination
```

For scenario questions:

1. identify the visible signature;
2. determine whether the defect is support, consistency, framing, coverage, or capability;
3. select the authoritative evidence or system record needed;
4. use deterministic checks for repeated values and arithmetic;
5. neutralize prompts that assume the conclusion;
6. verify all required sources and criteria were covered;
7. require qualified human review where stakes or authority demand it; and
8. choose release, edit, verify, escalate, or reject.

Do not confuse precision, confidence, repetition, citations, volume, or a claimed action with proof.

## Exam lens

For scenario questions:

1. identify what property needs evaluation;
2. determine the intended purpose and stakes;
3. check requirements, sources, professional standards, and coverage;
4. distinguish accuracy from completeness, consistency, bias, audience fit, and format;
5. identify high-risk signatures rather than reading every line with equal suspicion;
6. choose the least subjective reliable check;
7. escalate when consequences exceed the model's authority or the available evidence; and
8. do not confuse confidence, polish, precision, citations, or action language with correctness.

The strongest answer usually establishes criteria and tests before changing the prompt. Exact labels, repeated values, schemas, and arithmetic favor deterministic checks. Nuanced professional judgment, contested evidence, or high-impact decisions require qualified human review.

## Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed the Discernment: Accuracy and Completeness lesson.
- [x] I completed the Hallucinations, Inconsistencies, and Bias lesson.
- [ ] I can explain the accountability asymmetry in professional AI use.
- [ ] I can distinguish Discernment from Diligence.
- [ ] I can identify verification debt in a workflow.
- [ ] I can apply the three evaluation references.
- [ ] I can review accuracy and completeness separately.
- [ ] I can identify plausible unsupported claims and fabricated specifics.
- [ ] I can calibrate certainty to evidence strength.
- [ ] I can build a repeated-fact consistency matrix.
- [ ] I can identify confirmation, selection, framing, and omission bias.
- [ ] I can distinguish bias control from false balance.
- [ ] I can verify source and requirement coverage.
- [ ] I can verify a claimed external action using tool and system evidence.
- [ ] I can calibrate review depth to the stakes.
- [ ] I can distinguish ready to use, needs revision, and needs human override.
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
- [Claude capability hallucinations](https://support.claude.com/en/articles/8241188-claude-is-producing-links-that-don-t-work-and-falsely-claiming-that-it-has-sent-emails-or-produced-external-documents-what-s-going-on)
- [Manage Claude's tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)
