# Ethical Impact Review and Escalation Pattern

## Problem

AI-assisted outputs can be policy-compliant and technically accurate while still creating unfair treatment, misleading transparency, unequal burden, weak recourse, or decisions beyond the team’s ethical authority.

Common symptoms include:

- one group described more negatively than another;
- similar cases evaluated under different standards;
- biased prompts or sources treated as neutral;
- AI assistance concealed where disclosure may be material;
- consequential people-facing use approved from a single example;
- affected people given no explanation or appeal path; and
- teams resolving large-scale ethical questions without appropriate standing.

## Context

Use this pattern when AI-assisted work:

- affects people, opportunity, access, treatment, reputation, or compensation;
- produces hiring, evaluation, performance, eligibility, or service recommendations;
- communicates to distinct demographic or stakeholder groups;
- may require disclosure of AI assistance;
- has unclear fairness criteria;
- involves vulnerable or protected populations;
- scales one decision across many people; or
- presents an ethical question that policy does not resolve directly.

## Forces

The design must balance:

- utility and efficiency;
- fairness and consistency;
- relevance of task criteria;
- transparency and audience expectations;
- privacy and data minimization;
- human accountability;
- explainability and evidence;
- recourse and correction;
- organizational authority;
- scale and monitoring; and
- uncertainty that cannot be eliminated by prompting.

## Recommended design

```text
Define use and affected parties
      ↓
Inspect framing, sources, criteria, and output
      ↓
Assess harm and distribution
      ↓
Define fair treatment
      ↓
Determine disclosure
      ↓
Define human authority and recourse
      ↓
Test representative cases
      ↓
Decide or escalate
      ↓
Monitor outcomes
```

## 1. Define the use and affected parties

Record:

- bounded use case;
- direct users;
- people whose treatment, opportunity, reputation, or access may change;
- vulnerable or low-power groups;
- accountable decision owner;
- downstream users; and
- people who may have difficulty challenging the result.

```text
User of the tool
      ≠
Only person ethically affected
```

## 2. Inspect bias entry points

Review:

- prompt wording and assumptions;
- source selection and representativeness;
- labels and categories;
- evaluation criteria;
- examples and few-shot demonstrations;
- generated wording and tone;
- omitted context;
- human edits; and
- downstream decision rules.

```text
Neutral-looking output
      ≠
Neutral process
```

## 3. Assess harm and distribution

Identify:

- possible physical, financial, professional, social, or reputational harm;
- severity and reversibility;
- who receives benefits;
- who carries risk or burden;
- whether errors concentrate on particular groups;
- scale of deployment;
- whether effects accumulate over time; and
- whether recourse is realistically available.

## 4. Define a fair-outcome standard

State:

- which cases should be treated consistently;
- which distinctions are relevant to the task;
- which characteristics or proxies should not influence the result;
- what evidence standard applies;
- what variation is acceptable;
- how inconsistent tone or recommendations will be detected; and
- what correction or appeal process is required.

```text
Identical process
      ≠
Fair process by default
```

## 5. Determine transparency and disclosure

Evaluate:

- organizational policy;
- audience expectations;
- professional or contractual duties;
- materiality of AI assistance;
- risk of misleading authorship or expertise claims;
- human review performed;
- consequence of concealment; and
- timing and placement of disclosure.

Disclosure should be accurate, proportionate, understandable, and consistent with the real workflow.

## 6. Define human authority and recourse

Specify:

- qualified reviewer;
- evidence reviewed;
- timing before consequence;
- authority to modify, reject, or stop;
- explanation responsibility;
- affected-party correction or appeal path;
- escalation route; and
- retained review evidence.

```text
Human review mentioned
      ≠
Human authority operational
```

## 7. Test representative cases

Include:

- relevant user or subject groups;
- edge cases;
- matched-case comparisons;
- different tones and certainty levels;
- proxy-characteristic checks;
- false-positive and false-negative consequences;
- high-impact examples;
- disclosure comprehension; and
- recourse usability.

One successful example is insufficient evidence for a scaled people-facing workflow.

## 8. Decide whether to escalate

Escalate when:

- affected population is large;
- harm may be severe or difficult to reverse;
- protected or vulnerable groups are involved;
- fairness criteria are disputed;
- the team lacks expertise or authority;
- transparency obligations are materially unclear;
- surveillance, manipulation, or power imbalance is present;
- no meaningful recourse exists; or
- policy assigns the decision elsewhere.

```text
Reasoning completed
      ≠
Authority to decide
```

Escalation should provide analysis and open questions rather than an unsupported final verdict.

## 9. Record the disposition

Use:

- Approve;
- Approve with constraints;
- Redesign;
- Defer pending evidence or specialist review; or
- Reject.

Record owner, rationale, tests, controls, residual uncertainty, escalation conditions, and review date.

## 10. Monitor actual outcomes

After deployment, review:

- outcome differences;
- recurring complaints or appeals;
- override patterns;
- unexplained group-level variation;
- disclosure failures;
- new affected populations;
- scale changes;
- policy or legal changes; and
- whether controls operate under deadline pressure.

## Controls

- affected-party map;
- bias-entry-point audit;
- fair-outcome standard;
- matched-case testing;
- disclosure decision;
- qualified human gate;
- explanation and recourse path;
- escalation threshold;
- ethical decision record;
- outcome monitoring; and
- scheduled and event-triggered review.

## Common failure modes

### Ethics reviewed only after output generation

**Why it fails:** Bias can enter through the prompt, sources, criteria, and workflow.

**Repair:** Review the complete decision chain.

### Same treatment assumed to equal fairness

**Why it fails:** Uniform application of irrelevant or biased criteria can reproduce unfair outcomes.

**Repair:** Define relevant similarity, justified differences, and effect monitoring.

### Disclosure decided by personal preference

**Why it fails:** Audience, policy, materiality, and professional obligations may differ.

**Repair:** Use a documented disclosure decision.

### Human review without intervention rights

**Why it fails:** The reviewer cannot protect affected people before consequence.

**Repair:** Assign evidence, timing, authority, and escalation.

### Team decides outside its standing

**Why it fails:** Good reasoning does not create organizational authority.

**Repair:** Escalate with a structured issue brief.

### No recourse

**Why it fails:** Affected people cannot correct errors or challenge unfair treatment.

**Repair:** Add explanation, correction, and appeal paths or redesign the use.

## Decision record

```text
Use case:
Affected parties:
Potential benefits:
Potential harms:
Bias entry points:
Fair-outcome standard:
Transparency decision:
Human authority:
Recourse:
Tests and evidence:
Residual uncertainty:
Escalation threshold:
Disposition:
Owner:
Review date:
```

## Compact rule

> Identify who is affected, inspect where bias can enter, define what fair treatment requires, determine appropriate disclosure, preserve human authority and recourse, and escalate when scale, harm, or standing exceeds the team’s mandate.

## Public-repository rule

Use fictional, generic, synthetic, public, or explicitly authorized scenarios. Do not include private employee evaluations, applicant data, protected-characteristic records, confidential ethics reviews, internal escalation records, or reconstructed proprietary course content.