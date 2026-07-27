# Module 3 Prompt Notebook: Hallucinations, Inconsistencies, and Bias

These prompts support deliberate review of AI-generated outputs. They are not substitutes for authoritative evidence, deterministic checks, qualified review, or confirmation in external systems.

Use fictional, generic, synthetic, public, or explicitly authorized material.

---

## 1. Beginner failure-pattern scan

```text
Review the output below for five possible failure types:

1. unsupported or invented claims;
2. contradictions;
3. biased framing;
4. important omissions; and
5. claimed actions that may not have occurred.

For each finding, explain it in plain English and quote the relevant sentence.

Do not decide whether a claim is true unless the supplied evidence supports that decision. Mark unsupported items as `needs verification`.

Output:
- Finding
- Failure type
- Why it matters
- Evidence needed
- Recommended next action

Output to review:
[OUTPUT]

Authorized evidence:
[EVIDENCE]
```

---

## 2. Claim inventory builder

```text
Create a complete inventory of material claims in the output.

Include:
- factual claims;
- numbers;
- dates;
- names;
- quotations;
- citations;
- comparisons;
- causal explanations;
- recommendations;
- assumptions;
- statements of certainty; and
- claims that an external action was completed.

Return a table with:
1. Claim ID
2. Exact claim
3. Claim type
4. Materiality: low / medium / high
5. Evidence cited in the output
6. Verification needed
7. Current status: verified / qualified / inference / assumption / unsupported / conflicting / action-unverified

Output:
[OUTPUT]
```

---

## 3. Fabricated-specifics audit

```text
Audit the output for precise details that require provenance.

Prioritize:
- percentages;
- dollar amounts;
- dates;
- names;
- quotations;
- report titles;
- page references;
- legal or policy provisions;
- benchmark results; and
- exact product capabilities.

For each precise claim:
1. identify the claim;
2. state what evidence would be required;
3. locate the supporting source when supplied;
4. preserve conditions, units, population, date, and methodology;
5. classify the claim as supported, qualified, unsupported, or conflicting.

Do not invent citations or source locations.

Output:
[OUTPUT]

Sources:
[SOURCES]
```

---

## 4. Citation-support checker

```text
Check whether each citation in the output supports the full claim attached to it.

For every cited claim, evaluate:
- source exists;
- source is accessible;
- source authority fits the question;
- citation points to the relevant passage;
- full claim is supported;
- date and scope are appropriate;
- qualifications and exceptions are preserved;
- quotation is verbatim when quotation marks are used.

Return:
| Claim | Citation | Exists? | Full support? | Scope/date issue | Qualification needed | Verdict |

If a source is missing or inaccessible, say `not verified` rather than guessing.

Output:
[OUTPUT]

Sources:
[SOURCES]
```

---

## 5. Certainty calibration review

```text
Review the output for language that is more certain than the evidence supports.

Identify words or constructions such as:
- definitely;
- clearly;
- proves;
- is;
- will;
- always;
- never;
- the cause was;
- the best option is; and
- no risk exists.

For each finding:
1. quote the statement;
2. summarize the available evidence;
3. classify the evidence strength;
4. determine whether the language is proportionate;
5. propose a qualified revision that preserves meaning without hiding uncertainty.

Do not weaken well-supported statements merely to sound cautious.

Output:
[OUTPUT]

Evidence:
[EVIDENCE]
```

---

## 6. Long-output consistency matrix

```text
Build a consistency matrix for the document.

Extract every repeated:
- number;
- date;
- name;
- option label;
- status;
- risk rating;
- total;
- baseline;
- assumption;
- conclusion; and
- recommendation.

Return:
| Fact or concept | Location 1 | Value 1 | Location 2 | Value 2 | Governing source | Conflict? | Resolution |

Also compare:
- executive summary against body;
- narrative against tables;
- tables against calculations;
- recommendations against unresolved risks;
- conclusions against appendices.

Do not resolve a conflict unless the governing source supports the resolution.

Document:
[DOCUMENT]

Sources:
[SOURCES]
```

---

## 7. Deterministic repeated-value checker

```text
Use code or a spreadsheet to extract and compare repeated quantitative values from the supplied document or dataset.

Tasks:
1. identify the selected metrics;
2. list every occurrence and location;
3. normalize formatting and units;
4. flag conflicting values;
5. recalculate totals and derived figures;
6. produce a reproducible exception report.

Do not infer which value is correct without the governing source.

Metrics:
[METRICS]

Files or data:
[INPUTS]
```

---

## 8. Confirmation-bias challenge

```text
Review the analysis for confirmation bias.

Original question:
[QUESTION]

Output:
[OUTPUT]

Approved criteria:
[CRITERIA]

Perform these checks:
1. identify any preferred conclusion implied by the question;
2. list evidence supporting the output's conclusion;
3. list evidence that weakens or complicates it;
4. identify alternatives that received less scrutiny;
5. compare whether each option was judged using the same criteria and evidence standard;
6. identify benefits, risks, dependencies, uncertainty, and trade-offs omitted from the favored option;
7. propose a neutral reframing of the task.

Return a bias-review memo. Do not manufacture opposition where the evidence is one-sided.
```

---

## 9. Framing-bias comparison

```text
Identify language choices that could tilt interpretation without changing the underlying facts.

For each finding:
1. quote the current wording;
2. identify the implied frame;
3. state the relevant baseline, target, time period, or comparator;
4. provide a neutral wording;
5. explain whether the original wording is supported, misleading, or merely rhetorical.

Output:
[OUTPUT]

Context and evidence:
[CONTEXT]
```

---

## 10. Source-coverage and omission matrix

```text
Determine whether the output covers the full required evidence set.

Expected sources:
[EXPECTED SOURCES]

Output:
[OUTPUT]

For each source, file, chapter, option, criterion, or stakeholder group, record:
- expected identifier;
- accessible to the workflow?;
- reviewed?;
- represented in the output?;
- depth of treatment;
- material findings;
- omissions;
- parsing or access problems;
- follow-up action.

Return a coverage matrix and highlight any high-risk source that received no or unusually little attention.
```

---

## 11. Hardest-source check

```text
Identify which input was likely hardest to process and determine whether it received proportionate attention.

Consider:
- length;
- poor formatting;
- scanned or image-heavy content;
- tables;
- conflicting sections;
- technical complexity;
- unusual terminology;
- missing metadata; and
- high consequence.

Compare the difficult input with its treatment in the final output.

Return:
1. hardest source;
2. why it is difficult;
3. evidence it was processed;
4. material content omitted;
5. required corrective review.

Inputs:
[INPUTS]

Output:
[OUTPUT]
```

---

## 12. Capability-action verifier

```text
Review every statement claiming that an external action was completed.

Examples:
- email sent;
- draft created;
- file saved;
- event scheduled;
- ticket filed;
- record updated;
- team notified;
- form submitted.

For each claimed action, verify:
1. required tool or integration;
2. tool availability in the environment;
3. invocation evidence;
4. required approval or permission;
5. tool result;
6. returned identifier or artifact;
7. external-system confirmation;
8. final status: verified / failed / not performed / unclear.

A conversational statement is not proof of action.

Conversation and tool records:
[RECORDS]
```

---

## 13. Action read-back prompt

```text
After an external update, read the affected record back from the authoritative system and compare it with the requested state.

Requested change:
[REQUEST]

Tool result:
[TOOL RESULT]

Read-back result:
[READ-BACK]

Return:
- requested state;
- observed state;
- exact match?;
- discrepancies;
- duplicate or partial-action risk;
- safe next step.
```

---

## 14. Vendor-comparison failure audit

```text
Audit the vendor comparison for:
- unsupported features;
- conflicting prices or dates;
- missing approved criteria;
- unequal scrutiny;
- biased recommendation language;
- hidden uncertainty;
- arithmetic errors; and
- claimed actions without receipts.

Build:
1. requirement coverage table;
2. vendor-by-criterion evidence table;
3. repeated-fact consistency table;
4. missing-evidence list;
5. neutral trade-off summary;
6. disposition: release / edit / verify / escalate / reject.

Approved criteria:
[CRITERIA]

Proposals:
[PROPOSALS]

Draft comparison:
[DRAFT]
```

---

## 15. Causal-claim audit

```text
Identify every causal claim in the output.

For each:
1. quote the causal statement;
2. identify whether the evidence establishes correlation, timing, contribution, mechanism, or causation;
3. list alternative explanations;
4. determine whether a deterministic or statistical analysis is required;
5. revise the wording to match the evidence strength.

Output:
[OUTPUT]

Evidence:
[EVIDENCE]
```

---

## 16. Failure-pattern triage memo

```text
Prepare a concise triage memo for the output.

Sections:
1. Intended use and stakes
2. Material hallucination risks
3. Internal or source inconsistencies
4. Bias and framing concerns
5. Coverage and completeness gaps
6. Capability-action claims
7. Required verification
8. Required human review
9. Disposition: release / edit / verify / escalate / reject
10. Conditions for reconsideration

Every finding must cite the relevant sentence, source, tool record, or missing requirement. Mark unknowns explicitly.

Output:
[OUTPUT]

Requirements:
[REQUIREMENTS]

Sources and tool records:
[EVIDENCE]
```

---

## 17. Model-assisted self-review with boundaries

```text
Review your prior response for possible defects, but do not treat your self-review as independent verification.

Perform:
1. claim inventory;
2. unsupported-specific scan;
3. contradiction scan;
4. missing-source coverage check;
5. counterargument generation;
6. capability-action check;
7. list of items requiring external verification.

For every item, state whether the finding came from:
- supplied evidence;
- comparison within the output;
- inference;
- missing information; or
- external verification still required.

Prior response:
[OUTPUT]
```

---

## 18. Oral certification drill

```text
Give me one short scenario at a time about hallucinations, inconsistencies, bias, completeness failures, or capability hallucinations.

Ask me to identify:
1. the visible signature;
2. the failure family;
3. the evidence or record needed;
4. the safest immediate action; and
5. the correct disposition.

After I answer:
- score the reasoning;
- explain the strongest answer;
- identify the closest distractor;
- give one transfer variation.

Use only original fictional scenarios.
```

---

## 19. Short reflection log

```text
Help me record a failure-pattern review.

Fields:
- Date
- Output type
- Intended use
- Stakes
- Failure signature noticed
- Failure family
- Evidence checked
- Defect confirmed?
- Correction
- Human reviewer
- Final disposition
- Workflow change to prevent recurrence
- Retest date
```

---

## Compact recall card

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → tool and external-state verification
```

## Usage rule

Model-assisted review can organize evidence and identify candidate defects. Material claims, calculations, external actions, high-stakes conclusions, and release decisions still require appropriate source checks, deterministic validation, system confirmation, or qualified human review.
