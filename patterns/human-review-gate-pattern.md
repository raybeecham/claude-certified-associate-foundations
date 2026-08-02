# Human Review Gate Pattern

## Purpose

Use this pattern to place qualified human review before AI-assisted outputs create consequential, external, regulated, sensitive, or difficult-to-reverse effects.

The pattern converts vague instructions such as `have someone check it` into a defined release control with a trigger, reviewer, evidence package, approval authority, and recorded disposition.

> Review gates should be triggered by risk and use, not by whether the generated output looks suspicious.

---

## Problem

AI-assisted outputs can be:

- fluent but unsupported;
- accurate in parts but materially incomplete;
- grounded but based on the wrong or stale source;
- numerically explained but incorrectly calculated;
- internally consistent but factually wrong;
- professionally polished but unauthorized for release; or
- improved through several rounds while still lacking required human judgment.

When review is improvised after generation, teams may lower the standard because:

- the draft looks convincing;
- a deadline is near;
- the author has already invested time in it;
- no reviewer was assigned;
- accountability is diffuse; or
- another prompt round feels easier than escalation.

---

## Context

Use this pattern when an AI-assisted output may:

- be sent to a client, partner, executive, regulator, auditor, court, or public audience;
- support a material financial, operational, legal, safety, medical, employment, benefits, eligibility, or access decision;
- contain confidential, regulated, privileged, or highly sensitive information;
- create or authorize an external action;
- alter production systems or official records;
- become difficult to retract or correct;
- rely on professional judgment the model cannot own; or
- reach diminishing returns through repeated iteration.

Do not apply the heaviest gate to every low-stakes internal draft. Review should remain proportionate.

---

## Core forces

The design must balance:

- speed versus consequence;
- automation versus accountability;
- traceability versus actual verification;
- reviewer cost versus release risk;
- iteration versus escalation;
- consistency versus independent judgment;
- reversibility versus urgency; and
- helpful model output versus organizational authority.

---

## Four threshold model

Evaluate four conditions before defining the release path.

| Threshold | Question | High-risk indicators |
|---|---|---|
| **Stakes** | What happens if the output is wrong? | Harm, material financial impact, rights, legal exposure, safety, major trust or operational consequences |
| **Reversibility** | Can the action or communication be undone? | Filing, publication, payment, deletion, production change, signed position, decision already acted upon |
| **Audience** | Who will see or rely on it? | Client, executive, public, regulator, auditor, court, oversight or affected person |
| **Regulatory exposure** | What rules govern it? | Law, regulation, contract, audit control, professional duty, security or privacy policy |

### Controlling rule

```text
Highest credible threshold
          ↓
Minimum review requirement
```

Do not average a severe threshold away.

---

## Automatic review gates

Create policy-defined categories that always require qualified human review.

Common gates include:

1. final client, partner, or external deliverables;
2. audit-critical or financially material calculations;
3. regulated, confidential, privileged, or highly sensitive information;
4. public, legal, regulatory, or incident communications;
5. safety-critical or medically consequential recommendations;
6. decisions affecting employment, benefits, access, rights, or eligibility;
7. production-impacting security or system changes;
8. irreversible tool actions;
9. official records, filings, approvals, or attestations; and
10. outputs where missing evidence or authority remains material.

The organization must define the exact list and controlling requirements.

---

## Recommended design

```text
Classify use case
      ↓
Assess four thresholds
      ↓
Apply automatic gates
      ↓
Define qualified reviewer
      ↓
Assemble evidence package
      ↓
Perform validation
      ↓
Human reviews and intervenes
      ↓
Record release disposition
      ↓
Execute action only after approval
      ↓
Monitor and correct if needed
```

---

## Step 1: Classify the use case

Record:

- business purpose;
- output type;
- intended audience;
- decision or action supported;
- data classification;
- whether the output is working, advisory, draft, final, or authoritative;
- tools or external actions involved; and
- governing policy, contract, standard, or regulation.

Without this classification, review requirements remain ambiguous.

---

## Step 2: Assess the thresholds

Use evidence rather than optimism.

| Threshold | Rating | Evidence |
|---|---|---|
| Stakes | Low / Material / High | Consequences and affected parties |
| Reversibility | Low / Material / High | Correction, rollback, or retraction path |
| Audience | Low / Material / High | Recipient, authority, and reliance |
| Regulatory exposure | Low / Material / High | Governing obligations |

A `High` rating may independently require mandatory review.

---

## Step 3: Apply automatic gates

Evaluate whether policy already decides the question.

```text
Automatic gate applies?
      ├─ Yes → mandatory qualified review
      └─ No  → proportionate review based on thresholds
```

Do not allow the model to waive an automatic gate.

---

## Step 4: Define a qualified reviewer

A named role is insufficient unless the role has the necessary capabilities.

Required reviewer properties may include:

- domain expertise;
- authority to reject or escalate;
- understanding of the audience and intended use;
- access to original sources and calculations;
- knowledge of applicable policy;
- enough time for substantive review;
- independence from the draft where needed; and
- ability to stop the release or action.

### Meaningful-review test

```text
Expertise
  + Authority
  + Context
  + Evidence access
  + Time
  + Intervention rights
  = Meaningful human review
```

A person merely present in the workflow does not satisfy the gate.

---

## Step 5: Assemble the evidence package

The reviewer should receive more than the final prose.

Depending on the use case, include:

- original requirements;
- authoritative source set;
- claim-evidence ledger;
- extracted quotations;
- deterministic calculations;
- data lineage;
- assumptions and unknowns;
- conflicting evidence;
- prior versions and changes;
- tool-call or external-action records;
- applicable policies and standards; and
- known limitations.

The evidence package should allow independent inspection.

---

## Step 6: Perform required validation

Choose checks based on the property being evaluated.

| Property | Stronger check |
|---|---|
| Exact value | Code or authoritative system lookup |
| Calculation | Reproducible deterministic recomputation |
| Source support | Claim-to-source and quote review |
| Completeness | Requirements and source-coverage matrix |
| Internal consistency | Repeated-fact comparison |
| Bias | Common criteria, counterevidence and affected-group review |
| Sensitive data | Classification, authorization and disclosure review |
| Professional fitness | Qualified domain review |
| External action | Tool receipt and external-state confirmation |

No single grader is sufficient for every dimension.

---

## Step 7: Conduct substantive human review

The reviewer should be able to:

1. challenge unsupported assumptions;
2. inspect critical claims and sources;
3. recalculate or request recalculation;
4. identify missing requirements;
5. qualify certainty;
6. correct or reject the draft;
7. escalate unresolved authority or evidence gaps; and
8. withhold approval.

A review that cannot change the outcome is ceremonial.

---

## Step 8: Record disposition

Use an explicit controlled status:

| Disposition | Meaning |
|---|---|
| **Release** | Criteria and review requirements are met for the stated use |
| **Edit and re-review** | Bounded corrections are required before approval |
| **Verify** | Material evidence or calculation remains unresolved |
| **Escalate** | Greater expertise, authority, or policy interpretation is required |
| **Reject** | The output is unreliable, unsafe, unauthorized, or unfit for purpose |

Record:

- output version;
- reviewer;
- evidence reviewed;
- material changes;
- unresolved limitations;
- decision;
- date; and
- approving authority.

---

## Step 9: Enforce the gate before action

The review gate must occur before:

- send;
- publish;
- file;
- approve;
- sign;
- pay;
- delete;
- update an official record;
- change production; or
- notify affected parties.

Where consequences are material, use technical controls in addition to written procedure:

- draft-only permissions;
- approval workflows;
- transaction holds;
- separate execution roles;
- protected branches;
- dual control;
- immutable logs; or
- read-back verification.

A prompt instruction alone is not an enforcement mechanism.

---

## Iteration-versus-escalation branch

Prompt iteration is appropriate while the remaining problem is prompt-fixable.

### Continue iterating when

- the defect is clearly localized;
- relevant evidence is available;
- one targeted instruction is likely to help;
- previous rounds show measurable improvement;
- review gates have not been bypassed; and
- consequences remain contained.

### Escalate when

- improvement has plateaued;
- the same defect persists;
- later rounds make only cosmetic changes;
- new rounds create regressions;
- the required evidence is unavailable;
- the model lacks authority;
- qualified professional interpretation is needed;
- the output falls into a mandatory-review category; or
- an irreversible action is approaching.

```text
Prompt problem     → targeted iteration
Evidence problem   → obtain evidence
Tool problem       → repair workflow
Authority problem  → escalate
Judgment problem   → qualified human review
```

---

## Ownership model

AI assistance does not become the accountable owner.

Assign human or organizational ownership for:

- task definition;
- evidence authorization;
- validation design;
- review;
- approval;
- execution;
- monitoring; and
- correction.

```text
Model generates or assists
          ↓
Human validates and approves
          ↓
Organization releases and owns consequences
```

---

## Practical examples

### Routine internal agenda

- low stakes;
- reversible;
- internal audience;
- no regulatory exposure.

**Control:** Basic self-review; no specialist gate.

### Board financial summary

- material stakes;
- executive audience;
- difficult to correct after presentation;
- governed financial information.

**Control:** Deterministic recomputation plus qualified financial review.

### External proposal with flat improvement curve

- external audience;
- material trust consequence;
- repeated prompt rounds no longer improve substance.

**Control:** Stop iteration and obtain independent colleague review.

---

## Failure modes

### Review triggered by appearance

A polished output bypasses the gate.

**Control:** Trigger by use-case classification and thresholds.

### Human rubber stamp

The reviewer lacks expertise, evidence or intervention rights.

**Control:** Define reviewer qualification and required actions.

### Review after release

The output is sent or executed before approval.

**Control:** Put a technical and procedural hold before the side effect.

### Citation substitution

Grounding is treated as final approval.

**Control:** Separate traceability, validation, professional review and authorization.

### Universal escalation

Every routine draft is sent to a specialist.

**Control:** Preserve proportionate review for green work.

### Endless iteration

Prompting continues after evidence, authority or judgment has become the blocker.

**Control:** Use explicit escalation criteria and improvement-curve review.

### Accountability diffusion

No one is named as the release owner.

**Control:** Record approver, executor and correction owner.

---

## Implementation checklist

### Policy

- [ ] Output classes are defined.
- [ ] Automatic review gates are documented.
- [ ] Four-threshold criteria are documented.
- [ ] Qualified reviewer roles are named.
- [ ] Release authority is explicit.
- [ ] Prohibited preapproval actions are listed.

### Evidence

- [ ] Requirements are available.
- [ ] Sources are authoritative and current.
- [ ] Material claims are traceable.
- [ ] Calculations are reproducible.
- [ ] Unknowns and conflicts are visible.
- [ ] Sensitive-data handling is authorized.

### Workflow

- [ ] Gate occurs before irreversible action.
- [ ] Reviewer can intervene.
- [ ] Approval is recorded.
- [ ] Tool actions are independently confirmed.
- [ ] Rollback or correction path is defined.
- [ ] Monitoring owner is assigned.

### Iteration

- [ ] Acceptance criteria are defined.
- [ ] Improvement is measured by round.
- [ ] Plateau signals are monitored.
- [ ] Evidence, tool, authority and judgment gaps are distinguished.
- [ ] Escalation path is available.

---

## Compact decision rule

```text
If consequence, irreversibility, audience, or governing obligations are material,
place a qualified human-review gate before release or action.

If prompting no longer improves the evidence, authority, or judgment,
stop iterating and escalate.
```

---

## Related material

- [Module 3: Diligence — When Human Review Is Non-Negotiable](../modules/03-evaluating-validating-output/lessons/05-diligence-human-review.md)
- [Grounded Verification Pattern](grounded-verification-pattern.md)
- [Failure Signature Review Pattern](failure-signature-review-pattern.md)
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md)
- [Governance Canvas](../ai-systems-engineering/worksheets/governance-canvas.md)
- [Evaluation Canvas](../ai-systems-engineering/worksheets/evaluation-canvas.md)
