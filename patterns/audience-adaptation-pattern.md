# Audience Adaptation Pattern

## Purpose

Use this pattern to transform one verified analysis into audience-specific deliverables without changing the underlying facts, uncertainty, risks, dependencies, obligations, or approved commitments.

> Adapt the presentation to the reader while preserving the verified content model.

---

## Problem

A generated draft may be accurate yet still fail because it is:

- too long for the reader's attention;
- too technical or too shallow;
- written in the wrong register;
- poorly structured for the channel;
- missing the decision or requested action;
- unsafe for the recipient;
- inconsistent with another audience version; or
- shortened in a way that hides material context.

Organizations also create risk when several candidate drafts are combined based on style without reconciling their facts, assumptions, and certainty.

---

## Context

Use this pattern when:

- a verified analysis must become an executive summary, working-team update, client communication, public notice, regulator response, or other deliverable;
- one message must be adapted across several audiences;
- a raw AI draft requires professional editing;
- multiple drafts or model outputs must be compared;
- external disclosure differs from internal working detail; or
- the final deliverable must preserve traceability and review approval.

Do not use this pattern to polish unsupported content. Verification comes first.

---

## Core forces

The design must balance:

- brevity versus completeness;
- accessibility versus precision;
- confidence versus uncertainty;
- persuasion versus neutrality;
- disclosure versus confidentiality;
- executive scanability versus operational detail;
- consistency versus audience-specific depth; and
- speed versus professional review.

---

## Recommended design

```text
Verify source content
      ↓
Define audience contract
      ↓
Create invariant content model
      ↓
Choose information depth and disclosure boundary
      ↓
Apply clarity, tone, and formatting passes
      ↓
Compare candidates if needed
      ↓
Run invariant and disclosure checks
      ↓
Apply review and approval gate
      ↓
Release the reviewed version
```

---

## Step 1: Verify the source content

Before adaptation, confirm:

- material claims are supported;
- calculations are reproducible;
- source coverage is complete;
- contradictions are resolved;
- uncertainty is classified;
- risks and dependencies are known; and
- the source version is approved for adaptation.

```text
Unsupported draft
      +
Better wording
      =
More persuasive risk
```

---

## Step 2: Define the audience contract

Record:

| Dimension | Definition |
|---|---|
| Audience | Reader, role, and relationship |
| Expertise | Existing knowledge and vocabulary |
| Purpose | Why the communication exists |
| Decision or action | What should happen after reading |
| Stakes | Consequence of misunderstanding |
| Attention | Time and reading behavior |
| Channel | Email, slide, memo, report, dashboard, meeting, public notice |
| Tone | Formality, directness, neutrality, urgency |
| Disclosure | What may, must, or must not be shared |
| Evidence | Facts, caveats, and sources that must remain visible |

A vague instruction such as `make this executive-friendly` is not a sufficient contract.

---

## Step 3: Create the invariant content model

Identify content that must remain stable across versions.

### Invariants

- facts;
- figures, units, dates, and denominators;
- source-supported conclusions;
- uncertainty and confidence;
- material risks;
- dependencies and conditions;
- legal, contractual, regulatory, and policy obligations;
- approved commitments; and
- version and approval state.

### Adaptable elements

- selection;
- order;
- length;
- vocabulary;
- examples;
- method depth;
- headings;
- tone;
- visual structure; and
- location of supporting evidence.

### Restricted elements

- confidential details;
- internal debate;
- privileged material;
- security-sensitive information;
- personal or regulated data;
- unapproved commitments; and
- unsupported speculation.

---

## Step 4: Choose depth and disclosure boundary

Use the intended decision to determine what belongs in:

- the main message;
- supporting detail;
- an appendix;
- an internal-only note; or
- no audience-facing version.

### Decision-critical rule

Information belongs in the main message when removing it would change:

- the conclusion;
- the level of confidence;
- the risk posture;
- the recommended action;
- the reader's understanding of obligations; or
- the ability to make a responsible decision.

Do not hide decision-critical information in an appendix solely to make the main message cleaner.

---

## Step 5: Apply three editing passes

### Clarity pass

- lead with the main point;
- remove repetition;
- tighten sentences;
- replace vague references;
- define terms;
- separate facts from inference; and
- make decisions and actions explicit.

### Tone pass

- match formality and directness to the relationship;
- preserve evidence-calibrated certainty;
- avoid advocacy when neutrality is required;
- avoid diplomacy that conceals risk; and
- avoid commitments not supported or approved.

### Formatting pass

- structure for the reading pattern;
- use headings, bullets, tables, narrative, or visuals intentionally;
- keep key decisions and risks visible;
- place supporting detail where it can be found; and
- satisfy accessibility and channel requirements.

---

## Step 6: Compare candidates

When several drafts exist, apply a common rubric.

| Criterion | Question |
|---|---|
| Factual fidelity | Does it match the verified source? |
| Caveat preservation | Are uncertainty and conditions retained? |
| Completeness | Does the audience have what it needs? |
| Clarity | Is the meaning easy to understand? |
| Tone | Does the register fit the relationship? |
| Structure | Can the reader find the decision and evidence? |
| Actionability | Is the expected response clear? |
| Disclosure | Is content appropriately shared or withheld? |
| Compatibility | Can material be combined without conflicting assumptions? |
| Editing cost | How much remediation remains? |

```text
Polish
  ≠
Factual superiority
```

Select the strongest base against the full rubric, not the smoothest prose.

---

## Step 7: Run invariant and disclosure checks

### Invariant check

For every required item, verify:

- present;
- semantically equivalent;
- not weakened or overstated;
- correctly placed; and
- consistent across versions.

### Disclosure check

Verify:

- recipient authorization;
- confidential material;
- personal or regulated data;
- privileged or restricted content;
- approved commitments;
- public-position consistency; and
- forwarding or publication risk.

### Cross-audience consistency check

Compare all versions for:

- mismatched numbers;
- inconsistent certainty;
- risks disclosed to one group but misleadingly hidden from another;
- conflicting commitments;
- different definitions; and
- incompatible decisions.

---

## Step 8: Apply review and approval gate

Use the Human Review Gate Pattern when the adapted output is:

- final or external;
- financially material;
- public, legal, regulatory, or client-facing;
- sensitive or confidential;
- difficult to reverse; or
- consequential to decisions, rights, or operations.

The reviewer should compare the final adapted version with the verified content model and audience contract.

---

## Audience profiles

### Executive

Lead with:

- decision;
- impact;
- material risk;
- requested action.

Retain decision-changing uncertainty. Move detailed method to supporting material.

### Working team

Retain:

- evidence;
- method;
- assumptions;
- owners;
- dates;
- dependencies;
- open questions;
- next actions.

### Client or partner

Prioritize:

- supported outcome;
- implication;
- approved commitment;
- next step;
- accountable update.

Remove internal-only speculation and unapproved disclosure.

### Regulator or auditor

Prioritize:

- requirement;
- evidence;
- methodology;
- exception;
- control;
- owner;
- approval;
- traceability.

### Public audience

Prioritize:

- essential facts;
- impact;
- accessible context;
- approved action;
- necessary uncertainty and safety information.

---

## Failure modes

### Style before verification

Unsupported content becomes more persuasive.

**Control:** Verify first.

### Brevity removes a material condition

The short version misleads.

**Control:** Maintain an invariant checklist and main-message decision rule.

### Tone increases certainty

A provisional conclusion becomes definitive.

**Control:** Preserve support status and confidence.

### One draft for every audience

The message is too detailed for some and insufficient for others.

**Control:** Create separate versions from one content model.

### Internal speculation becomes external explanation

Unverified hypotheses create commitments or blame.

**Control:** Separate internal analysis from approved external messaging.

### Candidate merging creates contradictions

Attractive passages rely on incompatible assumptions.

**Control:** Reconcile every candidate to the same source and definitions.

### External disclosure is unchecked

Sensitive or privileged content reaches the wrong recipient.

**Control:** Include disclosure review in the adaptation workflow.

### Final version differs from reviewed version

Unapproved changes bypass the gate.

**Control:** version-lock the reviewed artifact and verify release identity.

---

## Implementation checklist

### Source integrity

- [ ] Verified source version identified.
- [ ] Facts and calculations checked.
- [ ] Uncertainty and risk classified.
- [ ] Obligations and commitments identified.

### Audience contract

- [ ] Audience and expertise defined.
- [ ] Purpose and decision defined.
- [ ] Attention and channel defined.
- [ ] Tone defined.
- [ ] Disclosure boundary defined.

### Adaptation

- [ ] Invariants marked.
- [ ] Main-message depth chosen.
- [ ] Clarity pass completed.
- [ ] Tone pass completed.
- [ ] Formatting pass completed.

### Integrity

- [ ] No misleading omission.
- [ ] No increased certainty.
- [ ] Risks and dependencies visible.
- [ ] Restricted content removed.
- [ ] Candidate assumptions reconciled.
- [ ] Cross-audience versions consistent.

### Release

- [ ] Required human review completed.
- [ ] Approval recorded.
- [ ] Final version matches reviewed version.
- [ ] Correct channel and recipients confirmed.

---

## Compact decision rule

```text
Preserve the verified content model.
Adapt selection, depth, tone, order, and format to the audience.
Restore anything whose omission changes the decision, risk, obligation, or confidence.
Release only the reviewed version.
```

---

## Related material

- [Editing and Adapting Output for Your Audience](../modules/03-evaluating-validating-output/lessons/06-editing-adapting-audience.md)
- [Human Review Gate Pattern](human-review-gate-pattern.md)
- [Grounded Verification Pattern](grounded-verification-pattern.md)
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md)
- [Prompt Planning Canvas](../ai-systems-engineering/worksheets/prompt-planning-canvas.md)
