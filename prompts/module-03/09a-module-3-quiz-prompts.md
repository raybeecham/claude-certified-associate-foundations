# Module 3 Notebook: Quiz and Remediation

Use these prompts to practice the seven judgment domains assessed in the Module 3 quiz. They are original study aids, not reconstructed course questions.

---

## 1. Seven-domain scenario generator

```text
Create seven original scenario-style multiple-choice questions covering:
1. accuracy versus completeness;
2. hallucination signatures;
3. source restriction and auditable grounding;
4. internal inconsistency and deterministic reconciliation;
5. audience adaptation;
6. code-executed numeric reliability; and
7. input curation.

For each question:
- provide four plausible answers;
- identify the best answer;
- explain the controlling principle;
- explain why each distractor is weaker; and
- avoid proprietary or remembered exam wording.
```

---

## 2. Accuracy-versus-completeness drill

```text
Review the supplied output and requirements.

Create two separate findings:
- Accuracy: which present claims are correct or incorrect?
- Completeness: which required elements, risks, sources, or dependencies are absent?

Do not treat correct visible content as proof of full coverage.

Return:
1. accuracy findings;
2. completeness findings;
3. materiality of each gap;
4. recommended repair; and
5. release disposition.
```

---

## 3. Fabricated-specific detector

```text
Scan this output for precise claims that create an appearance of authority.

Flag:
- percentages;
- dates;
- dollar values;
- quotations;
- names;
- citations;
- benchmark results;
- legal or policy references; and
- exact capability claims.

For each, provide:
- claim;
- source or provenance;
- scope and date;
- support status;
- verification action; and
- consequence if wrong.
```

---

## 4. Closed-source grounding prompt

```text
Answer the question using only the supplied documents.

Rules:
- do not use general knowledge;
- say `not covered by the supplied materials` when evidence is absent;
- cite the document and most precise available location for every material claim;
- quote the controlling passage before analysis when the text is consequential;
- identify conflicts between sources; and
- do not resolve ambiguity without evidence.
```

---

## 5. Citation-support audit

```text
Audit every citation in this draft.

For each claim-citation pair, determine:
- whether the source exists;
- whether the cited location can be found;
- whether it supports the full claim;
- whether conditions or exceptions were omitted;
- whether the source is authoritative and current; and
- whether conflicting evidence exists.

Classify each as Supported, Qualified, Unsupported, Conflicting, or Not Covered.
```

---

## 6. Reconciliation mismatch drill

```text
The supplied table contains totals, subtotals, and line items.

Perform a reconciliation review:
1. identify every arithmetic inconsistency;
2. locate authoritative input records;
3. define inclusion, exclusion, unit, sign, date, and duplicate rules;
4. recompute using code or another deterministic method;
5. explain each variance;
6. correct dependent narrative claims; and
7. state whether human review is required before release.

Do not repair a numeric contradiction through prose or formatting alone.
```

---

## 7. Audience-variant exercise

```text
Using one verified content model, produce:
1. an executive version;
2. a working-team version; and
3. an external-recipient version.

Preserve across all versions:
- material facts and figures;
- uncertainty;
- decision-changing risks;
- dependencies;
- obligations; and
- approved positions.

Adapt:
- selection;
- order;
- depth;
- vocabulary;
- tone;
- format; and
- disclosure.

Provide an invariant-check table after drafting.
```

---

## 8. Code-execution decision drill

```text
Determine whether this task requires code execution.

Assess:
- exactness required;
- number of variables;
- filtering and grouping;
- date boundaries;
- duplicate and missing-value rules;
- units and currencies;
- downstream reporting consequence;
- need for charts or processed files; and
- reproducibility requirements.

Return:
- prose acceptable;
- code execution recommended; or
- code execution mandatory before consequential use.

Explain the required logic review and reconciliation.
```

---

## 9. Code logic review

```text
Review the generated calculation code before relying on the result.

Check:
- source files and versions;
- schema assumptions;
- date range;
- filters;
- joins;
- groupings;
- duplicate handling;
- missing values;
- units and currency;
- signs, credits, or refunds;
- formulas and statistical method;
- control totals; and
- consistency between result table, chart, and narrative.

Classify every check as Pass, Fail, or Needs Review.
```

---

## 10. Input-curation exercise

```text
Review this source package before analysis.

For each file, classify:
- controlling source;
- current supporting source;
- draft;
- superseded;
- duplicate or near-duplicate;
- irrelevant;
- sensitive or restricted; or
- unclear.

Return:
1. include/exclude/clarify decision;
2. authoritative source hierarchy;
3. material differences that must be preserved;
4. double-counting or contradiction risk; and
5. the curated package to use for rerun.
```

---

## 11. Distractor analysis

```text
For each multiple-choice question, analyze why the incorrect answers are tempting.

Classify each distractor as one of:
- trust polish or confidence;
- switch models prematurely;
- repeat the same request;
- self-certification;
- reformat a substantive defect;
- confuse structure with truth;
- ignore intended-use risk; or
- leave noisy inputs unchanged.

Then state the controlling reason the correct answer is stronger.
```

---

## 12. Smallest responsible intervention

```text
Given this scenario, identify the smallest intervention that actually establishes the missing property.

Possible intervention types:
- completeness review;
- source verification;
- citation audit;
- deterministic computation;
- audience adaptation;
- input curation;
- qualified human review; or
- rejection and reconstruction.

Explain why broader or more expensive interventions are unnecessary and why weaker interventions are insufficient.
```

---

## 13. Property-to-test mapping

```text
Map each output property to the strongest practical test.

Properties:
- requirement coverage;
- factual accuracy;
- completeness;
- source support;
- internal consistency;
- arithmetic correctness;
- audience fit;
- schema validity;
- semantic correctness;
- sensitive-data handling;
- release authority.

For each, identify:
- test or evidence;
- tool or reviewer;
- pass criteria;
- failure action; and
- whether the test is independent.
```

---

## 14. Timed oral quiz

Answer each in no more than 30 seconds:

1. Why can an accurate report still fail?
2. What is the signature of a fabricated specific?
3. What three instructions strengthen closed-source grounding?
4. What should resolve an inconsistent subtotal?
5. What remains invariant across audience versions?
6. Why is code execution stronger than prose for material math?
7. What remains unproven after code executes?
8. Why should duplicate sources be removed?
9. Why is a higher model tier often the wrong first fix?
10. What is the difference between traceability and release approval?

---

## 15. Full-workflow transfer exercise

```text
Evaluate this AI-assisted deliverable from beginning to release.

Perform:
1. requirement and completeness review;
2. hallucination and inconsistency scan;
3. claim-to-source grounding;
4. deterministic calculation review;
5. Diligence threshold assessment;
6. audience adaptation review;
7. output-format and input-curation review;
8. triage disposition; and
9. release-decision record.

Return Release, Edit, Verify, Escalate, or Reject with the controlling reason.
```

---

## 16. Remediation planner

```text
The learner missed the following quiz domain:
[DOMAIN]

Create a focused remediation plan containing:
- the governing distinction;
- one beginner explanation;
- one original scenario;
- one distractor analysis;
- one applied exercise;
- one flashcard;
- one observable mastery criterion; and
- a transfer question in a different domain.
```

---

## 17. Full-marks retention check

```text
Create a spaced-review schedule for the seven Module 3 quiz domains.

Include review prompts for:
- 24 hours;
- 3 days;
- 7 days;
- 14 days; and
- 30 days.

Use scenario transfer and explanation, not memorized answer wording.
```

---

# Compact quiz card

```text
MISSING FACTOR?
→ Completeness review

PRECISE, NO SOURCE?
→ Fabricated-specific risk

DOCUMENT-BOUND TASK?
→ Restrict sources + permit unknown + cite locations

NUMBERS CONFLICT?
→ Execute and reconcile

DIFFERENT AUDIENCES?
→ Preserve invariants, adapt presentation

MATERIAL MATH?
→ Code execution + logic review

NOISY SOURCES?
→ De-duplicate, label, prune
```
