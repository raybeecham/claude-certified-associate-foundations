# Three-Reference Discernment Pattern

## Intent

Evaluate an AI-assisted output against stable references before deciding whether it is fit for use.

The pattern separates:

- what the task required;
- what the evidence supports;
- what professional practice requires;
- whether present content is accurate;
- whether material content is missing; and
- how deeply the output must be reviewed given the stakes.

## Problem

AI-generated output can be polished, plausible, and mostly correct while still containing:

- one unsupported claim;
- one omitted condition;
- one missing requirement;
- one misleading generalization;
- one unverified calculation; or
- one professional-standard failure.

Reviewers often rely on surface quality, memory of the request, or the model's own confidence. These are weak substitutes for a repeatable evaluation method.

## Context

Use this pattern when an output will:

- support a decision;
- summarize supplied evidence;
- be sent to another person;
- represent an organization;
- contain factual claims, figures, quotations, or recommendations;
- be published or submitted;
- trigger an action; or
- create material consequences if wrong or incomplete.

Use a lighter form for low-stakes provisional work. Use stronger evidence and qualified review for high-consequence work.

## Core model

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

## The three references

### 1. Requirements

Determine whether the output satisfies the actual task contract.

Check:

- primary objective;
- audience;
- scope;
- required sections or fields;
- requested comparisons or reasoning;
- evidence boundaries;
- missing-data behavior;
- output format; and
- acceptance criteria.

Do not review from memory when the original request or rubric is available.

### 2. Source material

Determine whether material claims match the authorized evidence.

Check:

- claim-to-source traceability;
- exact figures and units;
- quotations and attribution;
- conditions, minimums, exceptions, and dependencies;
- date and currency;
- source authority;
- conflicting evidence; and
- whether the source supports the full claim.

### 3. Professional standards

Determine whether the output is acceptable for the domain and intended use.

Check relevant:

- laws and regulations;
- organizational policy;
- contractual requirements;
- technical standards;
- documented procedures;
- professional ethics;
- evidence norms;
- calculation requirements;
- approval requirements; and
- audience expectations.

The model must not be treated as the final authority on whether its own output meets these standards.

## Separate quality dimensions

### Accuracy

Ask:

> Is what is present correct, supported, and appropriately qualified?

Possible defects:

- fabricated fact;
- wrong number;
- incorrect date;
- bad attribution;
- unsupported inference;
- incorrect calculation;
- contradiction; or
- overstated certainty.

### Completeness

Ask:

> Is anything material required for the intended use missing?

Possible defects:

- omitted requirement;
- missing option;
- absent exception;
- missing dependency;
- missing risk;
- missing unit or denominator;
- incomplete source coverage;
- missing uncertainty; or
- omitted decision-relevant condition.

Accuracy and completeness must be evaluated independently.

## Review-depth decision

```text
Consequence of error
        +
Reversibility
        +
Uncertainty
        +
Evidence quality
        +
Audience and intended action
        ↓
Required review depth
```

### Low consequence

Use proportionate review:

- requirement check;
- obvious-error scan;
- fit-for-audience review; and
- explicit provisional status.

### Material consequence

Use structured validation:

- requirement traceability;
- claim-level checks for material statements;
- completeness checklist;
- independent calculation checks; and
- documented verdict.

### High consequence

Require:

- authoritative current evidence;
- reproducible methods;
- claim-level verification;
- qualified human review;
- documented approval; and
- refusal to release when support or authority is insufficient.

## Procedure

### Step 1: Define purpose and stakes

Record:

- intended use;
- audience;
- decision or action;
- consequence if wrong;
- reversibility;
- evidence standard; and
- required reviewer authority.

### Step 2: Build a requirement checklist

Convert the request into discrete items.

Mark each:

- met;
- partially met;
- missing; or
- unclear.

### Step 3: Build a material-claim inventory

List claims that affect the decision, including:

- figures;
- dates;
- quotations;
- comparisons;
- causal statements;
- risk statements;
- recommendations; and
- statements of compliance or eligibility.

### Step 4: Trace claims to evidence

For each material claim, record:

| Claim | Source | Location | Support | Conditions | Status |
|---|---|---|---|---|---|
| | | | Full / Partial / None / Conflict | | Verified / Qualified / Unsupported / Conflicting |

### Step 5: Apply professional standards

Use the relevant checklist, rubric, qualified reviewer, or governing authority.

### Step 6: Review accuracy

Identify incorrect, unsupported, contradictory, or overstated content.

### Step 7: Review completeness

Compare the output to requirements, evidence coverage, domain expectations, and decision needs.

### Step 8: Assign a verdict

Use:

- **Ready to use**;
- **Needs revision**; or
- **Needs human override**.

Document scope and rationale.

## Verdict rules

### Ready to use

Choose only when:

- requirements are met;
- material claims are supported;
- important limitations are preserved;
- professional standards are satisfied;
- review depth matches the stakes; and
- the verdict is scoped to the intended use.

### Needs revision

Choose when:

- the defects are bounded;
- the evidence exists;
- the workflow has sufficient authority;
- the output can be repaired and rechecked; and
- qualified escalation is not yet necessary.

### Needs human override

Choose when:

- authoritative evidence is absent;
- the task requires domain authority;
- uncertainty is materially high;
- the output contains severe or systemic defects;
- the consequence of error is high;
- the model or current reviewer lacks authority; or
- the result should not be released from the AI draft alone.

Human override means substantive ownership, not ceremonial approval.

## Controls

### Requirements traceability

Keep the original request visible during review.

### Claim inventory

Prioritize claims that change decisions or create external consequences.

### External completeness checklist

Use a source outline, required-field schema, domain checklist, or qualified reviewer expectations.

### Deterministic verification

Use code, calculators, schemas, or independent systems for exact operations.

### Versioning

Record which output, prompt, evidence set, and source versions were reviewed.

### Reviewer qualification

Define the expertise, authority, evidence access, and time required for meaningful review.

### Explicit disposition

End with a documented release, revision, or escalation decision.

## Trade-offs

### More review improves confidence but costs time

Do not apply maximum review to every provisional low-stakes output.

### Source checking can reveal conflicting authority

A conflict may require qualification or escalation rather than forced resolution.

### Completeness checks require external knowledge

The output cannot reveal everything it omitted. Use independent checklists and reviewers.

### Human review is not automatically reliable

A rushed or unqualified person can miss the same defects as the model. Review design matters.

## Common failure modes

### Surface review only

Grammar and structure are checked; evidence and requirements are not.

### Citation presence mistaken for grounding

Links appear, but their actual support is not inspected.

### Accuracy-only review

Every visible statement is correct, but material content is missing.

### Universal readiness claim

An output is marked ready without stating the intended audience and use.

### Same review depth for every task

Low-stakes ideas and high-stakes determinations receive identical treatment.

### Model self-certification

The same model is asked whether its output is accurate and its answer is treated as proof.

### Ceremonial human approval

The reviewer lacks expertise, authority, evidence access, or time.

### Over-verification

Expensive review is applied to provisional work where the consequences are low and reversible.

## Example

A generated project update says a deployment is scheduled for August 12.

The source notes also state that the date depends on security approval and closure of two high-priority defects.

- Requirements: leadership needs status and risks.
- Source: the date is correct but conditional.
- Professional standard: material dependencies must be disclosed.
- Accuracy: the date is supported.
- Completeness: the conditions are missing.
- Stakes: material operational decision.

**Verdict:** Needs revision.

## Decision rule

> Check the output against requirements, sources, and professional standards; review accuracy and completeness separately; then choose review depth and disposition based on the consequences of error.

## Compact checklist

- [ ] Intended use and stakes are defined.
- [ ] Original requirements are open and traceable.
- [ ] Material claims are inventoried.
- [ ] Claims are checked against sources.
- [ ] Conditions, exceptions, units, and dates are preserved.
- [ ] Professional standards are applied.
- [ ] Accuracy is reviewed.
- [ ] Completeness is reviewed separately.
- [ ] Review depth is proportionate.
- [ ] Reviewer qualification is sufficient.
- [ ] Verdict and rationale are documented.
- [ ] Output version and evidence version are recorded.

## Related material

- [Discernment: Accuracy and Completeness](../modules/03-evaluating-validating-output/lessons/02-discernment-accuracy-completeness.md)
- [Failure Localization Pattern](failure-localization-pattern.md)
- [Evaluation Canvas](../ai-systems-engineering/worksheets/evaluation-canvas.md)
- [Evaluator Rubric Template](../prompts/evaluator-rubric-template.md)
