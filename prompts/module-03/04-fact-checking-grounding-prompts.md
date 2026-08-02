# Module 3 Prompt Notebook: Fact-Checking and Grounding

Use these prompts as study exercises and adaptable starting points. Replace placeholders with fictional, public, synthetic, or explicitly authorized material.

A prompt can improve verifiability, but it cannot guarantee factual correctness, source quality, domain authority, or release readiness by itself.

---

## 1. Permission to remain uncertain

```text
Use the supplied sources as the evidence boundary.

If they do not support an answer, state `not covered by the supplied materials` rather than estimating, filling gaps from general knowledge, or inventing a likely answer.

Separate the result into:
- supported findings;
- qualified findings;
- conflicting evidence;
- not covered; and
- questions requiring additional evidence.
```

### Study objective

Practice treating an explicit unknown as a valid output state.

---

## 2. Closed-source document analysis

```text
Answer the question using only the attached documents.

Do not use general knowledge or unstated assumptions.

For each material statement:
- name the source;
- cite the most precise available location;
- preserve conditions, exceptions, dates, and units; and
- label the statement supported, qualified, conflicting, or not covered.

Question:
[QUESTION]
```

### Study objective

Define a clear evidence boundary for document work.

---

## 3. Open-research source hierarchy

```text
Research the question using current sources.

Source hierarchy:
1. controlling or official primary sources;
2. official guidance or documentation;
3. reputable independent analysis;
4. secondary summaries only when primary material is unavailable.

For every material claim:
- cite the source;
- record the publication date and relevant event date;
- distinguish fact from inference;
- disclose conflicts; and
- identify any claim that remains unverified.

Question:
[QUESTION]
```

### Study objective

Separate open research from analysis of a fixed evidence set.

---

## 4. Auditable citation contract

```text
For every material factual claim, provide:
- source title;
- author or issuing organization when available;
- section, clause, page, table, cell, email, or record identifier;
- exact supporting text or value;
- scope and conditions; and
- support status.

Allowed support statuses:
- supported;
- qualified;
- unsupported;
- conflicting; and
- not covered.

Do not include an unsupported claim in the final recommendation.
```

### Study objective

Distinguish citation-shaped text from inspectable support.

---

## 5. Quote first, then analyze

```text
Before analyzing the question, extract the exact passages that bear on it.

For each passage:
- quote it verbatim;
- cite the precise source location;
- explain what issue it addresses; and
- note any surrounding condition or exception.

After the extraction is complete, analyze only the extracted evidence. If the evidence is insufficient or conflicting, say so before giving a conclusion.

Question:
[QUESTION]
```

### Study objective

Separate evidence extraction from interpretation.

---

## 6. Claim-evidence audit

```text
Audit the draft below.

Create a table with columns:
- claim;
- materiality;
- source;
- exact support;
- source location;
- scope or limitation;
- status; and
- required action.

If a claim lacks adequate support, do not defend it. Mark it for retraction, narrowing, removal, or escalation.

Draft:
[DRAFT]

Evidence set:
[SOURCES]
```

### Study objective

Turn a draft into a visible claim-to-source reconciliation.

---

## 7. Citation support checker

```text
For each citation in the response:
1. confirm that the source exists and can be accessed;
2. identify the exact cited passage;
3. compare the passage with the claim;
4. determine whether it supports the whole claim or only part of it;
5. identify omitted conditions, exceptions, dates, or scope; and
6. assign supported, qualified, unsupported, or conflicting.

Do not infer support merely because the source is relevant to the topic.
```

### Study objective

Test semantic support rather than citation presence.

---

## 8. Unsupported-claim retraction pass

```text
Review the answer for statements that cannot be supported by the authorized evidence.

For each unsupported statement:
- quote the statement;
- explain why the evidence is insufficient;
- retract it or replace it with the narrowest wording the evidence supports; and
- identify what additional source would be needed to restore the stronger claim.

Do not preserve unsupported specificity for stylistic reasons.
```

### Study objective

Practice evidence-driven retraction rather than defensive elaboration.

---

## 9. Best-of-N instability comparison

```text
Compare the following responses to the same question.

Do not decide truth by majority vote.

Identify:
- claims shared by all responses;
- claims that differ;
- numbers, dates, names, or citations that change;
- differences in certainty;
- omitted conditions;
- different source selections; and
- conclusions that require authoritative verification.

Return an instability map and a verification plan.

Responses:
[RESPONSES]
```

### Study objective

Use repeated generations to locate soft spots, not to create artificial consensus.

---

## 10. Authoritative-source validation

```text
Validate the material claims below against the controlling or most authoritative available sources.

For each claim:
- identify the appropriate source class;
- locate the current authoritative source;
- record the applicable date, version, jurisdiction, population, or product scope;
- compare the claim with the source;
- disclose conflicting authority; and
- classify the result as verified, qualified, unsupported, outdated, or not applicable.

Claims:
[CLAIMS]
```

### Study objective

Distinguish grounding to a selected source from independent factual validation.

---

## 11. Conflicting-source reconciliation

```text
The supplied sources may conflict.

Build a conflict table with:
- issue;
- source A position;
- source B position;
- date and authority of each source;
- whether one source supersedes or controls;
- unresolved ambiguity; and
- required escalation.

Do not silently merge incompatible statements.

Sources:
[SOURCES]
```

### Study objective

Make conflicting evidence visible instead of averaging it away.

---

## 12. Deterministic calculation verification

```text
Verify the calculation described in the draft.

1. Extract the governing inputs from the authoritative source.
2. Record units, dates, signs, and denominators.
3. State the formula or rule.
4. Recompute using code or another deterministic method.
5. Compare the computed result with the narrative.
6. Explain any discrepancy.
7. Preserve a reproducible calculation record.

Draft:
[DRAFT]

Source data:
[DATA]
```

### Study objective

Separate cited inputs from verified arithmetic.

---

## 13. Spreadsheet cell-grounding review

```text
For each material figure in the workbook explanation:
- identify the workbook tab and cited cells;
- trace formula dependencies;
- record source inputs and units;
- check the applicable time period;
- recompute the result independently;
- identify hard-coded assumptions; and
- state whether the cell citation establishes traceability, verification, or both.

Do not treat a cell citation as proof that the formula or assumption is correct.
```

### Study objective

Use cell-level citations as an audit path while retaining formula and human review.

---

## 14. Coverage plus grounding audit

```text
Before accepting the analysis, verify that the entire authorized evidence set was processed.

Create a coverage matrix with:
- expected source or section;
- access status;
- processed status;
- material claims extracted;
- citations used;
- unresolved parsing or access issue; and
- reviewer action.

Then identify any conclusion that relies on incomplete source coverage.
```

### Study objective

Prevent accurate quotations from creating a false impression of complete evidence review.

---

## 15. Grounding ladder classifier

```text
Classify the current verification approach at the highest level it genuinely satisfies:

0. fluent output only;
1. self-review or repeated runs;
2. claim-to-source citations;
3. quote-first or cell-level grounding;
4. independent authoritative validation;
5. deterministic testing plus qualified human review.

Explain:
- what evidence the current level provides;
- what it does not establish;
- the next required level for the stated stakes; and
- the release condition.
```

### Study objective

Avoid treating traceability, validation, and authorization as interchangeable.

---

## 16. High-stakes release gate

```text
Evaluate whether this output can be released for the stated use.

Record:
- intended audience and decision;
- consequence of error;
- authorized evidence set;
- source authority and currency;
- claim-level support status;
- calculation verification;
- unresolved uncertainty;
- required professional reviewer;
- required approval; and
- final disposition: release, edit, verify, escalate, or reject.

An AI-generated citation or self-review is not sufficient independent validation for a high-stakes claim.
```

### Study objective

Connect grounding to accountable release decisions.

---

## 17. Contract evidence extraction exercise

```text
Use only the supplied fictional agreement and amendments.

Question:
What notice is required to prevent automatic renewal?

Process:
1. Extract every term, renewal, termination, and notice provision.
2. Cite each document, section, and page.
3. Apply amendments in controlling order.
4. Identify conflicts and missing dates.
5. State the notice period only when supported.
6. Do not calculate a calendar deadline unless the current term-end date is supplied.

Return an evidence table, controlling interpretation, uncertainty statement, and reviewer note.
```

### Study objective

Practice quote-first document analysis and explicit unknowns.

---

## 18. Oral certification drill

Answer each in one or two sentences:

1. Why should uncertainty be permitted explicitly?
2. What is the difference between a citation and claim support?
3. Why is quote-first analysis useful?
4. What does Best-of-N comparison establish?
5. Why is a second model answer not independent evidence?
6. What is the difference between source restriction and authoritative validation?
7. Why do cell-level citations not prove a calculation is correct?
8. What should happen when a material claim cannot be supported?
9. Which verification level is required for a consequential decision?
10. What is the final responsibility of the human reviewer?

---

# Notebook completion record

Record one completed exercise:

| Field | Entry |
|---|---|
| Scenario | |
| Evidence boundary | |
| Authority hierarchy | |
| Unknown behavior | |
| Grounding method | |
| Citation format | |
| Independent validation | |
| Deterministic check | |
| Human reviewer | |
| Final disposition | |
| Remaining gap | |

The objective is not to produce the most elaborate verification process. It is to create the least complex evidence path that is strong enough for the consequence of error.
