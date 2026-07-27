# Lesson 2: Discernment — Accuracy, Completeness, and Fitness

## Overview

Evaluation is not a general impression that an answer looks polished or sounds intelligent. It is a structured comparison between the output and three fixed references:

1. the requirements for the task;
2. the source material or evidence; and
3. the professional standards that govern the work.

> Discernment means checking an output against stable references instead of trusting fluency, confidence, or first impressions.

The same protocol should be used whether the reviewer is relaxed, rushed, impressed by the writing, or skeptical of it.

## Plain-English explanation

Claude can produce an answer that sounds right without being fully right.

To review it, ask three simple questions:

```text
Did it do what I asked?
        ↓
Does it match the evidence?
        ↓
Would this be acceptable in the real setting where it will be used?
```

Then ask two separate quality questions:

```text
Accuracy     → Is what is present correct?
Completeness → Is anything important missing?
```

A response can pass one and fail the other.

For example, a project summary may correctly state that deployment begins on August 12. If it omits that deployment still depends on security approval, the statement may be accurate but the summary is incomplete and potentially misleading.

## One analogy: checking a grocery delivery

Imagine ordering groceries for a dinner.

- **Requirements** are the shopping list you submitted.
- **Source material** is the receipt and the product labels.
- **Professional standards** are basic food-safety and quality expectations.

You review the delivery in two ways:

```text
Accuracy
Did the store send the correct items?

Completeness
Did every required item arrive?
```

Receiving the correct pasta does not compensate for a missing sauce. Likewise, an AI output can contain only true statements and still fail because it leaves out the one fact needed to make a sound decision.

## The three evaluation references

### Reference 1: Requirements

Requirements define what the output was supposed to accomplish.

Re-read the original request, task contract, rubric, or acceptance criteria. Check every required element rather than remembering the request approximately.

Questions to ask:

- Did the output answer the primary question?
- Did it cover every requested section or field?
- Did it use the required scope, audience, time period, and format?
- Did it follow the requested evidence boundary?
- Did it handle missing information as specified?
- Did it provide the reasoning, comparisons, or recommendations requested?

A useful technique is a requirements traceability table:

| Requirement | Present? | Correct? | Evidence | Action |
|---|---|---|---|---|
| Required section or claim | Yes / No | Yes / No / Unclear | Source or observation | Keep / Revise / Verify |

This prevents the easy parts of the task from hiding omitted requirements.

### Reference 2: Source material

Source review asks whether the output accurately represents the evidence it claims to summarize, analyze, or quote.

Do not rely on a general sense that Claude probably read the file correctly. Trace material claims back to the relevant source.

For each important claim, check:

- Can the claim be located in the source?
- Does the source support the full claim, not merely part of it?
- Were qualifications, exceptions, minimums, dates, units, or conditions preserved?
- Is a quotation verbatim and attributed correctly?
- Is the source current enough for the task?
- Does another source conflict with it?

```text
Output claim
      ↓
Source location
      ↓
Exact supporting content
      ↓
Conditions and limitations
      ↓
Supported / Qualified / Unsupported / Conflicting
```

A claim may be numerically correct but still misleading when an important condition is omitted.

### Reference 3: Professional standards

Professional standards ask whether the result would be acceptable in the field or workflow where it will be used.

An output may follow the prompt and still be unfit for professional use.

Examples of professional-standard failures include:

- a number without a unit or denominator;
- a recommendation without reasoning;
- a quotation without a source location;
- a legal or regulatory conclusion without review by qualified counsel or compliance personnel;
- a financial figure without a reproducible calculation;
- a risk rating without defined criteria;
- a medical statement presented as personalized advice;
- a technical conclusion that ignores known operating limits;
- a citation that cannot be opened or does not support the claim; and
- an executive recommendation that hides material uncertainty.

Professional standards can come from:

- laws and regulations;
- organizational policies;
- contractual requirements;
- technical standards;
- documented procedures;
- quality-control practices;
- professional ethics;
- audience expectations; and
- domain-specific review norms.

The model should not be treated as the authority that defines whether its own output satisfies those standards.

## Accuracy and completeness are separate reviews

### Accuracy

Accuracy asks whether the information that appears in the output is correct.

Common accuracy defects:

- fabricated facts;
- incorrect numbers;
- misquoted text;
- wrong dates;
- incorrect attribution;
- unsupported causal claims;
- overconfident inference;
- incorrect calculations; and
- conclusions that do not follow from the evidence.

### Completeness

Completeness asks whether the output contains everything materially required for the intended use.

Common completeness defects:

- a required competitor, option, or category is missing;
- a relevant exception is omitted;
- only benefits are listed, while risks are absent;
- a recommendation omits implementation constraints;
- a price is shown without a minimum commitment;
- a schedule is shown without dependencies;
- a finding is presented without uncertainty or conflicting evidence;
- a summary omits the one factor that changes the decision; and
- an answer addresses the easy portions of a request but skips the difficult one.

### Why completeness is harder to detect

Incorrect content is visible on the page. Missing content is not.

```text
Accuracy defect     → something present is wrong
Completeness defect → something important is absent
```

To review completeness, compare the output against an external checklist:

- the original requirements;
- the source table of contents;
- a domain checklist;
- a decision framework;
- a required-field schema;
- a known set of options; or
- a qualified reviewer's expectations.

Do not ask only, `Is anything here wrong?`

Also ask:

> What would need to be present for someone to make the intended decision safely and competently?

## Fitness for purpose

Accuracy and completeness are evaluated against a purpose.

A short internal brainstorming note and a regulatory submission should not be judged by the same standard.

```text
Output quality = Accuracy + Completeness + Fitness for intended use
```

Fitness includes:

- the audience's level of expertise;
- the decision being supported;
- the consequence of error;
- required evidence quality;
- timing and currency;
- confidentiality and data restrictions;
- applicable policy or professional review; and
- whether the output will trigger an external action.

An output can be accurate and complete as a discussion starter but unfit to send to a customer, regulator, executive, or affected individual.

## Stakes calibration

The review depth should be proportional to the consequences of error.

### Low-stakes use

Examples:

- internal brainstorming;
- rough agenda ideas;
- early wording alternatives;
- nonbinding discussion starters; and
- reversible personal organization tasks.

Typical review:

- requirement check;
- obvious-error scan;
- audience and format check; and
- no unnecessary deep verification when the output is clearly provisional.

### Material-stakes use

Examples:

- client-facing summaries;
- operational recommendations;
- published market claims;
- project schedules;
- procurement comparisons; and
- management decisions.

Typical review:

- requirement traceability;
- source verification for material claims;
- completeness checklist;
- independent calculation checks; and
- documented revision or release decision.

### High-stakes use

Examples:

- legal analysis;
- financial reporting;
- compliance submissions;
- safety decisions;
- medical or benefits decisions;
- employment decisions;
- public statements with material consequences; and
- actions that are difficult to reverse.

Typical review:

- authoritative current evidence;
- claim-level verification;
- reproducible calculations;
- qualified human review;
- documented approval and accountability; and
- refusal to release when evidence or authority is insufficient.

> Review intensity is determined by consequence, not by how confident the output sounds.

## A practical beginner example

### Request

A manager asks Claude to summarize a project update for senior leadership.

The source notes say:

- production deployment is planned for August 12;
- the date depends on security approval;
- two high-priority defects remain open; and
- user training begins August 5.

### Generated summary

```text
The project is on track for production deployment on August 12. User training begins August 5, and the team is completing final readiness activities.
```

### Three-reference review

#### Requirements

The manager requested a leadership-ready status summary. The response gives a date and a concise status, but it does not include the material risks or dependencies needed by leadership.

**Result:** Partially met.

#### Source material

The August 12 date and August 5 training date match the notes. However, the phrase `on track` overstates the evidence because security approval is still pending and two high-priority defects remain open.

**Result:** Qualified and incomplete.

#### Professional standards

A leadership status report should disclose material dependencies and risks rather than imply certainty.

**Result:** Fails the decision-support standard.

### Verdict

**Needs revision.**

A corrected version might say:

```text
Production deployment remains targeted for August 12, subject to security approval and closure or accepted disposition of two high-priority defects. User training begins August 5. Leadership attention is required if either readiness condition remains unresolved at the next go/no-go review.
```

The repair preserves the supported dates while restoring the missing conditions and decision relevance.

## The discernment protocol

Use the same sequence for every meaningful output.

```text
1. Define purpose and stakes
          ↓
2. Check requirements
          ↓
3. Check source support
          ↓
4. Check professional standards
          ↓
5. Review accuracy
          ↓
6. Review completeness
          ↓
7. Assign a documented verdict
```

### Step 1: Define purpose and stakes

Record:

- intended audience;
- intended decision or action;
- consequence if wrong;
- reversibility;
- required evidence quality; and
- required reviewer authority.

### Step 2: Check requirements

Convert the task into a checklist and mark every requirement:

- met;
- partially met;
- missing; or
- unclear.

### Step 3: Check source support

Trace every material factual claim, number, quotation, and recommendation input to evidence.

### Step 4: Check professional standards

Apply the standards that a competent practitioner would use in the relevant field.

### Step 5: Review accuracy

Identify incorrect, unsupported, contradictory, or overstated content.

### Step 6: Review completeness

Identify required facts, risks, exceptions, assumptions, options, or caveats that are absent.

### Step 7: Assign a documented verdict

State the verdict, reasoning, unresolved issues, and next action.

## Three-way triage

This lesson uses a simple three-state decision model.

| Verdict | When it applies | Required action |
|---|---|---|
| **Ready to use** | Requirements are met, material claims match the evidence, applicable standards are satisfied, and review depth fits the stakes | Release for the stated use |
| **Needs revision** | The output is close, but one or more specific defects can be corrected within the existing workflow | Document the gaps, revise, and recheck |
| **Needs human override** | The stakes, uncertainty, missing authority, missing evidence, or severity of error make the draft unsafe to use without qualified human ownership | Escalate, reconstruct, or use only as input to expert review |

`Ready to use` is always scoped to a particular use. An output ready for an internal discussion may not be ready for external publication.

`Needs human override` does not mean a person should merely approve the existing draft. It means a qualified person must take substantive control of the analysis, evidence, and final decision.

## The protocol applied to three original outputs

### Output A: Service-pricing comparison

A procurement analyst asks for a summary of three providers' published service prices using supplied rate sheets.

The response lists one provider at `$28 per request`. The rate sheet says `$28 per request with a 500-request monthly minimum`.

- **Requirements:** All three providers are included.
- **Source material:** A material commercial condition is omitted.
- **Professional standards:** The omission distorts total-cost comparison.
- **Stakes:** Material procurement decision.

**Verdict:** Needs revision.

**Repair:** Re-run the comparison using only the supplied rate sheets and require every price to include minimums, tiers, term commitments, and mandatory fees.

### Output B: Internal meeting-format ideas

A team asks for three ways to shorten a weekly coordination meeting. The response provides three feasible options with benefits and trade-offs.

- **Requirements:** Met.
- **Source material:** No factual source claims are required.
- **Professional standards:** Appropriate as an internal discussion starter.
- **Stakes:** Low and reversible.

**Verdict:** Ready to use for discussion.

Additional verification would add little value before the team tests an option.

### Output C: Records-retention gap analysis

A department asks Claude to compare its records policy against a regulatory requirement. The authoritative rule is not supplied or retrieved. The response confidently identifies five compliance gaps based on general model knowledge.

- **Requirements:** The format appears complete.
- **Source material:** The governing authority is absent.
- **Professional standards:** A compliance conclusion requires current authoritative text and qualified review.
- **Stakes:** Regulatory and potentially consequential.

**Verdict:** Needs human override.

The response may help a qualified compliance professional build a review checklist, but it is not a reliable compliance determination.

## Documenting the review

A short evaluation record improves traceability.

| Field | Entry |
|---|---|
| Output reviewed | Name or version |
| Intended use | Decision, audience, and channel |
| Stakes | Low / Material / High |
| Requirements result | Met / Partial / Failed |
| Source result | Supported / Qualified / Unsupported / Conflicting |
| Accuracy defects | List or `none found` |
| Completeness defects | List or `none found` |
| Professional-standard concerns | List |
| Verdict | Ready / Revise / Human override |
| Reviewer | Name or role |
| Next action | Release, repair, escalate, or reconstruct |

`None found` does not mean no defect exists. It means none was found through the documented review method.

## Common failure modes

### Surface-quality substitution

The reviewer treats grammar, organization, or confidence as evidence of correctness.

**Repair:** Trace material claims and required elements explicitly.

### Requirement amnesia

The reviewer reads the output without reopening the original request.

**Repair:** Convert the request into a checklist before reviewing.

### Source trust by association

A response contains citations, so the reviewer assumes it is grounded.

**Repair:** Open the sources and verify claim-level support, scope, and date.

### Accuracy-only review

Every statement checked is correct, but an omitted dependency changes the decision.

**Repair:** Run a separate completeness review against an external checklist.

### Uniform review depth

Low-stakes and high-stakes outputs receive the same casual review.

**Repair:** Determine consequence and required authority before choosing review depth.

### Ceremonial human review

A person scans the draft but lacks the expertise, evidence access, authority, or time to evaluate it.

**Repair:** Assign a qualified reviewer and a defined review method.

### Over-verification

A provisional, low-stakes brainstorming output receives expensive claim-level review that does not improve the intended use.

**Repair:** Use proportionate validation and keep the provisional status explicit.

## Exam reasoning pattern

For accuracy-and-completeness scenarios:

1. identify the intended purpose;
2. identify the three evaluation references;
3. separate accuracy from completeness;
4. determine the stakes;
5. choose proportionate review depth;
6. select the correct verdict; and
7. reject answers that rely on polish, confidence, or model self-review alone.

```text
Requirements          → Did it do the requested work?
Sources               → Does the evidence support it?
Professional standards → Is it fit for real use?
Accuracy              → Is what is present correct?
Completeness          → Is anything material missing?
Stakes                → How much review is required?
```

## Knowledge check

### Question 1

An output includes only correct statements but omits a contractual minimum that changes the total price. Did it pass accuracy and completeness?

**Answer:** It may pass a narrow accuracy check for the statements present, but it fails completeness and fitness for the pricing decision.

### Question 2

Why should the reviewer reopen the original request?

**Answer:** Because outputs often satisfy the easiest portions of a request while omitting other required elements. Memory is an unreliable requirements checklist.

### Question 3

What are the three fixed evaluation references?

**Answer:** Requirements, source material, and applicable professional standards.

### Question 4

When is an output `ready to use`?

**Answer:** When it meets the requirements, matches the evidence, clears applicable professional standards, and has received review proportionate to the stated use and stakes.

### Question 5

What is the difference between `needs revision` and `needs human override`?

**Answer:** Revision applies when a bounded defect can be corrected in the existing workflow. Human override applies when consequence, uncertainty, missing authority, missing evidence, or serious defects require qualified human ownership.

### Question 6

Why can over-verification be a mistake?

**Answer:** Review should be proportionate. Deep validation of a low-stakes provisional idea may consume more value than it creates, provided the output is clearly limited to that low-stakes use.

## Flashcards

### Flashcard 1

**Q:** What are the three evaluation references?

**A:** Requirements, source material, and professional standards.

### Flashcard 2

**Q:** What does accuracy ask?

**A:** Whether the content that is present is correct and supported.

### Flashcard 3

**Q:** What does completeness ask?

**A:** Whether anything material required for the intended use is missing.

### Flashcard 4

**Q:** Why are completeness defects difficult to spot?

**A:** Missing information does not draw attention to itself; the reviewer needs an external checklist or expectation set.

### Flashcard 5

**Q:** What determines review depth?

**A:** The consequence of error, reversibility, uncertainty, evidence quality, audience, and intended use.

### Flashcard 6

**Q:** What are the three verdicts in this lesson?

**A:** Ready to use, needs revision, and needs human override.

### Flashcard 7

**Q:** Is `ready to use` universal?

**A:** No. It is scoped to a specific audience, purpose, and level of stakes.

### Flashcard 8

**Q:** What is the key exam mistake in discernment questions?

**A:** Treating polish, confidence, or citations alone as proof that the output is accurate, complete, and fit for use.

## Short recap

```text
1. Check the requirements.
2. Trace material claims to sources.
3. Apply professional standards.
4. Review accuracy and completeness separately.
5. Calibrate review depth to the stakes.
6. Record: ready to use, needs revision, or needs human override.
```

The central rule is:

> Do not ask whether the output looks good. Ask whether it is correct, complete, supported, professionally acceptable, and safe for its intended use.

## Educational-use notice

This repository is an unofficial educational resource. Its examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, medical, compliance, or other professional advice.

## Related material

- [Module Introduction](01-module-introduction.md)
- [Module 3 overview](../README.md)
- [Accuracy and Completeness prompt notebook](../../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Three-Reference Discernment Pattern](../../../patterns/three-reference-discernment-pattern.md)
- [Evaluation Canvas](../../../ai-systems-engineering/worksheets/evaluation-canvas.md)
- [Evaluator Rubric Template](../../../prompts/evaluator-rubric-template.md)
