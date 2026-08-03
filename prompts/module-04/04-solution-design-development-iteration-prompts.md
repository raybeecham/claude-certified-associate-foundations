# Module 4 Notebook: Solution Design, Development, and Iteration

Use these prompts to run bounded, evidence-driven design cycles. Examples must be fictional, synthetic, public, or explicitly authorized.

---

## 1. Design-context baseline

```text
Create the stable design context for this solution.

Capture:
- users and use cases;
- approved requirements;
- constraints;
- data definitions;
- prior decisions and rationale;
- acceptance criteria;
- known risks;
- excluded scope;
- unresolved questions; and
- current version.

Do not invent missing decisions. Mark them for owner resolution.
```

## 2. Meaningfully different options

```text
Generate three meaningfully different solution approaches for [PROBLEM].

For each option, provide:
- workflow pattern;
- model contribution;
- deterministic components;
- tools and data;
- human responsibilities;
- value hypothesis;
- limitations;
- implementation effort; and
- highest-risk assumption.

Avoid cosmetic variants.
```

## 3. Prototype hypothesis

```text
Turn the selected option into a prototype hypothesis.

Define:
- user;
- problem;
- expected improvement;
- core task to test;
- highest-risk assumptions;
- included and excluded scope;
- test data;
- success criteria;
- failure criteria; and
- prohibited uses.
```

## 4. Smallest useful prototype

```text
Design the smallest prototype that can test the stated hypothesis.

Include only features necessary to test:
- the core user task;
- material calculations or data mappings;
- the main interaction;
- the riskiest assumption; and
- required review controls.

Explain why every included feature is necessary.
```

## 5. Feedback classifier

```text
Classify each feedback item as:
- requirement failure;
- correctness failure;
- usability;
- accessibility;
- performance;
- privacy or disclosure;
- preference;
- new requirement; or
- out of scope.

For each, record severity, evidence, owner, decision, and required test.
```

## 6. Controlled change request

```text
Write a bounded refinement request using:
- observed problem;
- evidence;
- likely cause;
- requested change;
- expected improvement;
- requirements that must remain unchanged;
- regression tests; and
- acceptance criteria.
```

## 7. Regression plan

```text
Given this proposed change, identify:
1. directly affected requirements;
2. previously working behavior at risk;
3. data and calculation checks;
4. accessibility and disclosure checks;
5. user tests; and
6. rollback conditions.
```

## 8. Artifact dashboard cycle

```text
Create or refine an internal dashboard prototype using approved synthetic data.

Requirements:
- preserve metric names, units, and definitions;
- never invent missing values;
- calculate filtered totals from the underlying records;
- show active filters;
- provide no-data behavior;
- use color plus text or symbols;
- apply the approved direction-of-improvement rule; and
- create a clean print layout.

After the change, provide an acceptance and regression checklist.
```

## 9. Prototype-production gap

```text
Assess this prototype for production readiness.

Review:
- security;
- privacy and data classification;
- accessibility;
- scale and performance;
- state and persistence;
- monitoring and support;
- versioning and release control;
- failure recovery;
- authorization; and
- approval.

Return:
- prototype-valid;
- production gap;
- required owner;
- next evidence; and
- disposition.
```

## 10. Iteration stop decision

```text
Review the iteration history and choose:
- continue;
- accept for learning;
- redesign;
- escalate; or
- stop.

Use acceptance progress, regression rate, unresolved risk, evidence quality,
architecture needs, authority gaps, and marginal value of another cycle.
```

## 11. Design decision log

```text
Create a versioned decision log with:
- decision ID;
- date;
- context;
- options considered;
- evidence;
- decision;
- rationale;
- consequences;
- owner;
- review trigger; and
- superseded decision.
```

## 12. Oral certification drill

Answer in two or three sentences:

1. What is the iteration loop?
2. Why generate options before prototyping?
3. What should a prototype prove?
4. Why keep design context stable?
5. How should feedback be classified?
6. What is a regression check?
7. Why can a working artifact still be unfit for production?
8. When should iteration stop?

---

# Compact iteration card

```text
CONTEXT
[requirements / users / constraints / decisions]

HYPOTHESIS
[what the prototype should prove]

SCOPE
[included / excluded / prohibited use]

OBSERVATION
[what happened]

CLASSIFICATION
[requirement / correctness / usability / accessibility / performance / disclosure / preference]

CHANGE
[bounded modification]

TESTS
[acceptance / regression]

DECISION
[continue / accept / redesign / escalate / stop]
```
