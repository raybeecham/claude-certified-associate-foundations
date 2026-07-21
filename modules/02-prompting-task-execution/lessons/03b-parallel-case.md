# Lesson 3B: Decompose a Parallel Case

## Overview

Some workflows produce several deliverables from the same source. The correct design is usually not to draft every deliverable immediately. First create and validate the shared foundation, then branch into independent outputs.

> Sequence the shared, high-risk foundation first. Parallelize only after it is trustworthy.

## Scenario

A communications manager must turn a dense policy change into:

- an internal announcement;
- a staff FAQ; and
- a short executive briefing.

The three deliverables have different audiences and formats, but all depend on the same interpretation of the policy.

## The unsafe approach

```text
Policy document
      ↓
Draft announcement + FAQ + executive brief in one pass
```

This design hides the extraction step. If the policy is misunderstood, the same error can propagate into all three deliverables.

## The shared-foundation workflow

```text
Policy document
      ↓
Stage 1: Extract substantive changes
      ↓
Stage 2: Validate the extraction
      ↓
      ├── Stage 3A: Draft staff announcement
      ├── Stage 3B: Draft staff FAQ
      └── Stage 3C: Draft executive briefing
      ↓
Stage 4: Cross-deliverable consistency review
```

## Stage 1: Extract the substantive changes

**Task:** Identify each material policy change and explain what it means in practice.

**Output:** A structured change register containing:

- policy section or source reference;
- previous state, when known;
- new requirement;
- affected audience;
- effective date;
- practical impact;
- unresolved ambiguity.

**Validation:** Every claim must be traceable to the source. Unsupported interpretations are labeled rather than presented as fact.

## Stage 2: Validate the shared foundation

Before drafting anything, confirm that the change register is:

- complete;
- accurate;
- internally consistent;
- source-grounded;
- clear about uncertainty; and
- approved by the appropriate human reviewer when consequences are meaningful.

This is the workflow gate. If the foundation fails, stop and repair it before branching.

## Stage 3: Branch into parallel deliverables

Once the shared change register is approved, the drafting tasks become largely independent.

### 3A: Staff announcement

**Audience:** General staff

**Goal:** Explain what changed, why it matters, when it takes effect, and what employees need to do.

**Output:** Clear, concise announcement with an action-oriented tone.

### 3B: Staff FAQ

**Audience:** Employees likely to have practical questions

**Goal:** Anticipate common questions and answer them using only the validated change register.

**Output:** Question-and-answer format organized by topic.

### 3C: Executive briefing

**Audience:** Senior leaders

**Goal:** Compress the change into business impact, decisions, risks, timing, and required leadership action.

**Output:** Short briefing focused on consequence rather than procedural detail.

## Why these stages can run in parallel

The three drafts:

- consume the same approved foundation;
- do not depend on one another;
- optimize for different audiences; and
- can be reviewed independently before integration.

Parallelism is appropriate only after dependencies are satisfied.

## Stage 4: Reconcile the outputs

Parallel work can drift. Run a consistency review across all three deliverables.

Check that:

- dates and requirements match;
- no deliverable contradicts the change register;
- terminology is consistent;
- uncertainty is represented consistently;
- audience-specific simplification has not changed the underlying meaning; and
- required actions align across documents.

## The fan-out/fan-in pattern

```text
Shared source
    ↓
Extract
    ↓
Validate
    ↓
Fan out into parallel drafts
    ↓
Fan in for consistency review
    ↓
Publish
```

This pattern applies to many professional workflows:

- one research base producing a report, presentation, and briefing;
- one dataset producing operational, executive, and technical views;
- one requirements set producing user stories, test cases, and training material;
- one incident record producing customer, leadership, and engineering communications.

## Decision rule

Use a shared-foundation parallel workflow when:

1. several outputs depend on the same interpretation or evidence;
2. an upstream error would contaminate every output;
3. the outputs differ mainly by audience, purpose, or format; and
4. the downstream tasks do not depend on each other once the foundation is approved.

## Same conversation or separate conversations?

Keep extraction and validation together so the reasoning and source references remain visible. After approval, separate conversations or workers may be useful for the parallel drafts because each has a distinct audience and output contract.

Use a shared state capsule containing:

- approved change register;
- source references;
- terminology;
- unresolved questions;
- prohibited claims; and
- version identifier.

Do not rely on informal memory to keep parallel branches aligned.

## Failure modes

| Failure | Cause | Better design |
|---|---|---|
| Same error in all outputs | Drafting began before validation | Validate the shared foundation first |
| Contradictory dates or requirements | Branches used different source states | Pin one approved version |
| Executive brief contains invented implications | Audience adaptation became unsupported inference | Require traceability to the change register |
| FAQ omits major concerns | Questions generated without coverage review | Map every substantive change to likely questions |
| Parallel outputs drift in terminology | No reconciliation stage | Add a fan-in consistency review |

## Knowledge check

1. Why should extraction happen before drafting the three deliverables?
2. What condition must be true before the drafting branches run in parallel?
3. Why is a final consistency review still needed after each draft is reviewed separately?

## Flashcards

**Q:** What is a shared foundation?

**A:** A validated intermediate artifact that multiple downstream tasks consume.

**Q:** What is fan-out?

**A:** Branching from one approved foundation into independent parallel tasks.

**Q:** What is fan-in?

**A:** Recombining parallel outputs for consistency, integration, or final review.

**Q:** When should tasks not run in parallel?

**A:** When one task depends on another task's output or when the shared evidence has not been validated.

**Q:** What is the main risk of drafting before extraction is confirmed?

**A:** One upstream misreading can propagate into every downstream deliverable.

## Applied exercise

Choose a source that must produce three different outputs. Design:

1. the shared extraction artifact;
2. its validation gate;
3. three downstream branches;
4. a state capsule for branch consistency; and
5. the final fan-in review.

For every stage, define Input, Process, Output, and Validation.

## Key takeaway

> Parallel work should begin only after the shared truth it depends on has been extracted, validated, and versioned.
