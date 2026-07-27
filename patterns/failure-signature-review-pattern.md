# Failure Signature Review Pattern

## Intent

Use this pattern to detect AI-output defects that remain plausible on a casual read.

The pattern focuses on:

- hallucinations;
- contradictions;
- biased framing;
- silent omissions; and
- capability claims that require external confirmation.

> The reviewer does not wait for the output to look wrong. The reviewer looks for signatures that indicate where evidence, consistency, coverage, or action verification may have failed.

## Problem

Fluent generation creates a specific review risk:

```text
Plausible language
       +
Missing or weak support
       =
A defect that survives casual review
```

Typical weak review behaviors include:

- trusting precise details because they sound authoritative;
- reading long documents locally rather than comparing repeated facts;
- accepting a recommendation that mirrors the prompt's preferred conclusion;
- assuming a detailed output covered every required source; and
- treating a conversational action claim as proof that an external change occurred.

## Use when

Apply this pattern when an output contains one or more of the following:

- client-facing or public claims;
- numbers, dates, quotations, citations, or named sources;
- long-form analysis with repeated facts;
- comparisons or recommendations;
- a prompt that implies a preferred answer;
- a batch of files or documents;
- legal, financial, compliance, medical, safety, employment, or other consequential subject matter;
- claimed external actions; or
- output that is polished enough to discourage skepticism.

## Do not use as a substitute for

- authoritative source review;
- qualified professional judgment;
- deterministic calculation;
- application-side validation;
- external-system confirmation;
- security controls;
- permissions and approvals; or
- organizational release authority.

## Inputs

The pattern works best with:

1. intended purpose and audience;
2. consequence of error;
3. original requirements;
4. authorized source set;
5. generated output;
6. tool and connector records;
7. professional or organizational standards; and
8. known acceptance criteria.

## Core distinctions

### Hallucination

A claim is presented with more support than the evidence justifies.

### Inconsistency

Two parts of the output, or the output and its evidence, cannot all be correct at once.

### Bias

Framing, selection, emphasis, or scrutiny is uneven relative to the evidence and criteria.

### Completeness failure

A material source, requirement, option, condition, or risk is absent.

### Capability hallucination

The output claims that an external action occurred without verified tool execution and external-state confirmation.

## Signature matrix

| Signature | Likely defect | Evidence required | Default action |
|---|---|---|---|
| Precise claim without provenance | Fabricated specific | Authoritative source, scope, date, method | Verify |
| Citation cannot be opened | Fabricated citation | Accessible source record | Reject or verify |
| Citation supports only part of claim | Overstatement | Exact supporting passage | Qualify or revise |
| Absolute answer in conditional domain | Certainty mismatch | Current authoritative guidance and expert review | Escalate |
| Same metric has multiple values | Internal inconsistency | Governing source and deterministic reconciliation | Revise |
| Summary conflicts with table | Summary-detail mismatch | Table, source, calculation | Revise |
| Output strongly favors prompt's assumed answer | Confirmation bias | Neutral criteria, counterevidence, alternatives | Reframe and re-run |
| One option receives more scrutiny | Unequal treatment | Common criteria and evidence standard | Re-evaluate |
| Expected source not represented | Coverage failure | Source inventory and processing record | Verify or reject |
| Difficult source gets unusually short treatment | Processing or omission risk | Page/section coverage | Reinspect |
| Claimed action lacks tool receipt | Capability hallucination | Tool call, result, identifier, external read-back | Treat as not performed |

## Review flow

```text
Purpose and stakes
       ↓
Claim and action inventory
       ↓
Precision-provenance scan
       ↓
Certainty-evidence calibration
       ↓
Consistency comparison
       ↓
Bias challenge
       ↓
Coverage verification
       ↓
External-action confirmation
       ↓
Disposition and corrective action
```

## Step 1: Define purpose and stakes

Record:

- intended audience;
- intended decision or action;
- consequence if wrong;
- reversibility;
- approved evidence;
- freshness requirement;
- required reviewer expertise; and
- release authority.

The same defect can receive different treatment depending on use. An unsupported market estimate in an internal brainstorm is not equivalent to the same estimate in a signed client report.

## Step 2: Build the claim and action inventory

Extract:

- factual claims;
- quantitative claims;
- dates;
- quotations;
- citations;
- attributions;
- causal statements;
- comparisons;
- recommendations;
- assumptions;
- statements of certainty;
- claimed external actions; and
- required elements absent from the output.

Assign materiality:

```text
Low     → does not materially affect use
Medium  → affects interpretation or action
High    → changes decision, compliance, cost, safety, or trust
```

## Step 3: Run the precision-provenance scan

For each precise detail, require:

- source identity;
- source location;
- date;
- population or scope;
- units and denominator;
- methodology where relevant;
- preserved qualifications; and
- conflict check.

### Decision rule

```text
High precision + weak provenance = high verification priority
```

## Step 4: Calibrate certainty to evidence

Classify the statement:

| Class | Definition |
|---|---|
| Verified fact | Direct support from appropriate evidence |
| Qualified fact | Supported with important conditions or limitations |
| Inference | Reasoned conclusion not stated directly in the source |
| Assumption | Working premise not established by evidence |
| Unsupported | Adequate support not identified |
| Conflicting | Relevant evidence disagrees |

Then compare the language strength with the class.

Examples:

```text
Unsupported claim + “definitely” → overstated
Qualified fact + “generally”     → may be proportionate
Verified fact + direct statement → appropriate
```

## Step 5: Check consistency

Compare repeated facts across:

- executive summary;
- body;
- tables;
- charts;
- appendices;
- calculations;
- recommendations; and
- source citations.

Use a consistency matrix:

| Fact | Location A | Location B | Governing evidence | Resolution |
|---|---|---|---|---|
| Annual cost | $84,000 | $91,000 | Proposal: $91,000 | Correct narrative |

Use deterministic extraction or calculation when volume makes manual comparison unreliable.

## Step 6: Challenge bias

### Prompt bias check

Ask whether the request assumes a conclusion:

```text
Build the case for X
Explain why X is best
Show that X will succeed
```

### Evidence balance check

For each option, compare:

- criteria applied;
- evidence quality;
- benefits discussed;
- risks discussed;
- uncertainty disclosed;
- alternatives considered; and
- scrutiny depth.

### Counterevidence test

Ask:

1. What evidence would weaken the favored conclusion?
2. Which credible alternative was underdeveloped?
3. Are selection and framing proportional to evidence?
4. Is the output creating false balance where evidence is one-sided?

## Step 7: Verify coverage

Build a matrix covering:

- source files;
- chapters;
- criteria;
- options;
- stakeholder groups;
- time periods;
- geographic scope; and
- known risk categories.

| Required item | Accessible? | Processed? | Represented? | Material gap? |
|---|---|---|---|---|
| Critical incident report | Yes | Unclear | No | Yes |

Check the hardest and highest-risk sources explicitly.

## Step 8: Confirm external actions

An action claim passes only when the complete chain is supported:

```text
Tool or integration available
             ↓
Correct tool invoked
             ↓
Approval or permission satisfied
             ↓
Tool returned success
             ↓
Identifier or artifact returned
             ↓
External state confirms expected result
```

### Action evidence examples

| Action | Confirmation |
|---|---|
| Email sent | Sent-message state or provider confirmation |
| Draft created | Draft appears in mailbox |
| Event created | Event read-back with expected details |
| File saved | File exists at confirmed path or drive location |
| Ticket filed | Ticket ID and accessible record |
| Data updated | Authoritative read-back shows new value |

If any critical link is missing, classify the action as `unverified` or `not performed`.

## Step 9: Choose disposition

| Disposition | Criteria |
|---|---|
| Release | Material claims, consistency, coverage, bias controls, and actions pass for stated use |
| Edit | Substance is supported; bounded presentation issue remains |
| Verify | Material evidence, arithmetic, consistency, or action confirmation is unresolved |
| Escalate | Qualified authority, expertise, or approval is required |
| Reject | Output is materially unsupported, contradictory, biased, incomplete, unsafe, or falsely claims action completion |

## Output artifact

A strong review produces:

```text
Failure Signature Review

Purpose and stakes
Claim inventory
Hallucination findings
Consistency findings
Bias findings
Coverage findings
Capability-action findings
Verification completed
Unresolved issues
Disposition
Conditions for release
Owner and next action
```

## Controls

### Evidence controls

- approved source hierarchy;
- source-location capture;
- current-date checks;
- citation resolution;
- conflict logging; and
- preserved qualifications.

### Consistency controls

- repeated-value extraction;
- schema validation;
- deterministic arithmetic;
- summary-to-detail reconciliation; and
- regression checks.

### Bias controls

- neutral task framing;
- common criteria;
- equal evidence standards;
- counterevidence requirement;
- alternative analysis; and
- qualified reviewer diversity where appropriate.

### Coverage controls

- source manifest;
- processing status;
- page or section coverage;
- required-field checklist;
- failed-input logging; and
- highest-risk-source confirmation.

### Action controls

- least-privilege tool access;
- explicit approval;
- idempotency where applicable;
- result identifier;
- authoritative read-back;
- duplicate-action prevention; and
- audit log.

## Model-assisted review

The model can help:

- inventory claims;
- identify repeated facts;
- generate a consistency table;
- surface possible counterarguments;
- map output coverage; and
- list external actions claimed.

It cannot independently prove:

- the truth of unsupported claims;
- the existence of missing sources;
- factual correctness outside the supplied evidence;
- successful external actions without system records;
- unbiased judgment in consequential domains; or
- release authority.

## Common failure modes

### Failure mode 1: Surface-only review

**Symptom:** Grammar and tone are checked, but evidence is not.

**Control:** Claim inventory and provenance review.

### Failure mode 2: Precision trust

**Symptom:** Exact figures are accepted because they look authoritative.

**Control:** Precision-provenance scan.

### Failure mode 3: Local reading

**Symptom:** Each paragraph reads well, but contradictions across sections survive.

**Control:** Repeated-fact consistency matrix.

### Failure mode 4: Preferred-answer analysis

**Symptom:** The response mirrors the requester's desired conclusion.

**Control:** Neutral criteria, counterevidence, and alternatives.

### Failure mode 5: Volume-as-coverage assumption

**Symptom:** A long output is mistaken for complete source coverage.

**Control:** Source and requirement coverage matrix.

### Failure mode 6: Conversational action confirmation

**Symptom:** `I sent it` is treated as proof.

**Control:** Tool record, identifier, and external read-back.

### Failure mode 7: Self-review as sole validation

**Symptom:** The model is asked whether its own answer is correct and the reply is accepted.

**Control:** Independent source, deterministic, system, or qualified human check.

## Trade-offs

This pattern increases review effort. Apply it proportionately.

Use deeper review when:

- consequences are material;
- errors are difficult to reverse;
- sources are complex or conflicting;
- many precise claims appear;
- outputs are long;
- recommendations affect decisions;
- external actions are claimed; or
- professional standards require documented review.

Use a lighter version for clearly provisional, low-consequence work, while preserving the provisional label and preventing downstream misuse.

## Compact checklist

```text
[ ] Purpose and stakes recorded
[ ] Material claims inventoried
[ ] Precise details traced to evidence
[ ] Certainty matches evidence strength
[ ] Repeated facts reconciled
[ ] Favored conclusion challenged
[ ] Source and requirement coverage confirmed
[ ] Claimed actions verified externally
[ ] Qualified review applied where required
[ ] Disposition and owner documented
```

## Decision rule

> When fluent output contains precision, repetition, preference, omissions, or claimed actions, inspect the corresponding evidence, consistency, coverage, and system state before release.

## Related material

- [Hallucinations, Inconsistencies, and Bias](../modules/03-evaluating-validating-output/lessons/03-hallucinations-inconsistencies-bias.md)
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md)
- [Failure Localization Pattern](failure-localization-pattern.md)
- [Evaluation Canvas](../ai-systems-engineering/worksheets/evaluation-canvas.md)
