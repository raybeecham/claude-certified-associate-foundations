# Lesson 4: Fact-Checking and Grounding Techniques

## Overview

The strongest verification begins before the first draft exists.

A prompt can make an answer easier to audit by defining:

- what evidence Claude may use;
- what Claude should do when the evidence is silent;
- how each material claim must connect to a source;
- when direct quotations should be extracted before analysis;
- which calculations or claims require independent validation; and
- what must happen when support cannot be found.

> Grounding does not guarantee correctness. It makes the path from claim to evidence visible enough to inspect.

This lesson develops six techniques:

1. permit uncertainty;
2. restrict the evidence boundary;
3. require auditable citations;
4. quote first, then analyze;
5. use repeated runs to find instability rather than to vote on truth; and
6. validate consequential claims against authoritative evidence or deterministic checks.

---

# Plain-English explanation

Fact-checking asks:

```text
Is this claim actually true?
```

Grounding asks:

```text
What evidence is this claim based on, and can I inspect it?
```

A grounded answer should let you move backward:

```text
Conclusion
    ↓
Claim
    ↓
Citation or source location
    ↓
Exact supporting evidence
    ↓
Scope, date, conditions, and limitations
```

For a beginner, the central idea is simple:

> Do not ask Claude only for an answer. Ask it to show where the answer comes from and to admit when the evidence does not contain it.

A citation is useful only when:

- the source exists;
- the cited location can be opened or found;
- the source is authoritative enough for the question;
- the cited passage supports the full claim;
- relevant conditions and exceptions are preserved; and
- the source is current enough for the intended use.

---

# One analogy: an open-book exam

Imagine a student taking an open-book exam.

The student writes:

> The policy requires approval within 15 days.

The sentence may sound correct. But the instructor asks:

> Show me the page.

There are several possible outcomes:

- The student points to the exact section, and it says 15 days.
- The section says 15 **business** days, so the answer omitted an important condition.
- The section discusses a different process, so the citation is irrelevant.
- The book does not cover the question at all.
- The student cannot locate the source.

Grounding is the professional version of “show me the page.”

```text
Answer without evidence → plausible response
Answer with traceable support → auditable response
Answer with independent validation → stronger basis for action
```

The presence of a page number is not enough. The cited passage must actually support the claim.

---

# Build verifiability into the prompt

## Technique 1: Permit uncertainty

Models are often asked to be helpful, complete, and decisive. When the evidence is incomplete, that pressure can encourage the answer to fill gaps.

Explicitly allow outcomes such as:

- `unknown`;
- `not supported by the supplied materials`;
- `the sources conflict`;
- `additional evidence is required`; or
- `qualified review is needed`.

### Paste-ready prompt

```text
Use the supplied materials as the evidence boundary. If they do not support an answer, state `not covered by the supplied materials` rather than estimating or filling the gap from general knowledge.
```

### Why it helps

The prompt makes a supported non-answer preferable to an unsupported answer.

### What it does not do

Permission to say `unknown` reduces pressure to invent. It does not guarantee that Claude will recognize every unsupported claim. Material outputs still require review.

---

## Technique 2: Restrict the evidence boundary

For document analysis, decide whether the task is:

1. **closed-source analysis** — answer only from supplied documents; or
2. **open research** — use current external sources under a defined source hierarchy.

Do not leave this ambiguous.

### Closed-source prompt

```text
Answer using only the attached agreement and its amendments. Do not use general knowledge. Put any unanswered issue under `Not addressed in the supplied documents`.
```

### Open-research prompt

```text
Use current primary sources for material factual claims. Prefer official publications over summaries. Identify the publication date and event date, distinguish fact from inference, and list unresolved conflicts.
```

### Why source restriction matters

Without a source boundary, the output can silently combine:

- supplied documents;
- training-memory recall;
- current retrieved information;
- assumptions; and
- model-generated inference.

That mixture can be difficult to audit after the fact.

---

## Technique 3: Require auditable citations

A useful citation identifies a source and a location that a reviewer can inspect.

Depending on the source, location may mean:

- page number;
- section or clause number;
- paragraph or heading;
- table and row;
- spreadsheet tab and cell;
- email or thread;
- document link; or
- timestamp and record identifier.

### Paste-ready prompt

```text
For every material factual claim, provide the source title and the most precise available location, such as section, clause, page, table, or cell. If a claim cannot be traced, label it `unsupported` and do not use it in the recommendation.
```

### Citation-status vocabulary

Use a small controlled set:

| Status | Meaning |
|---|---|
| **Supported** | The source directly supports the full claim |
| **Qualified** | The source supports the claim only with conditions or narrower wording |
| **Unsupported** | No adequate support was located |
| **Conflicting** | Relevant sources disagree |
| **Not covered** | The evidence set does not address the issue |

### Important distinction

```text
Citation present
      ≠
Claim supported
```

A citation can be real and still fail because it:

- points to the wrong section;
- supports only part of the claim;
- omits an exception;
- uses an outdated version;
- refers to a weak secondary source when a primary source is required; or
- does not support the conclusion drawn from it.

---

## Technique 4: Quote first, then analyze

For long or high-stakes documents, separate evidence extraction from interpretation.

```text
Source document
      ↓
Extract exact passages
      ↓
Validate coverage and quotations
      ↓
Analyze only the validated evidence
      ↓
State conclusion and uncertainty
```

### Paste-ready prompt

```text
Before analyzing, extract the exact passages that bear on the question. Include the source location for each passage. Then analyze only those passages. If the passages are insufficient or conflict, state that before giving any conclusion.
```

### Why it helps

Quote-first work makes several defects easier to see:

- the source does not contain the claimed fact;
- the quote was altered;
- a condition was dropped;
- the analysis exceeds the evidence;
- a relevant passage was omitted; or
- two passages conflict.

### Quote-first is not quote-only

A quotation does not interpret itself. The reviewer still needs to check:

- whether the quote is representative;
- whether surrounding context changes its meaning;
- whether another provision controls;
- whether the source is authoritative and current; and
- whether professional judgment is required.

---

## Technique 5: Verify claims after generation

A second pass can require the output to prove its own material claims.

### Paste-ready prompt

```text
Create a claim-evidence table for the draft. For each material claim, provide the exact supporting quotation and source location. If adequate support cannot be located, retract or qualify the claim rather than defending it.
```

### Claim-evidence table

| Claim | Source | Exact support | Scope or condition | Status | Action |
|---|---|---|---|---|---|
| Material statement | Document and location | Quotation or cell | Limitation | Supported / Qualified / Unsupported / Conflicting | Keep / Rewrite / Remove / Escalate |

This turns review into a visible reconciliation process rather than a general request to “double-check.”

---

# Grounding techniques beyond one prompt

## Best-of-N comparison: use disagreement as a warning signal

Run the same bounded request more than once and compare the outputs.

```text
Run 1
Run 2
Run 3
  ↓
Agreement and divergence map
```

Useful signals include:

- different numbers;
- different source selections;
- different conclusions;
- changing levels of certainty;
- different omitted conditions; and
- different recommendations from the same evidence.

### Correct interpretation

```text
Runs disagree → the area is unstable and needs review
Runs agree    → the answer may be stable, but is not thereby proven true
```

Agreement among model runs is **not independent evidence**. Several runs can reproduce the same unsupported pattern.

### Paste-ready comparison prompt

```text
Compare these three responses against the same requirements and evidence set. List every material agreement, disagreement, omitted condition, and difference in certainty. Do not decide correctness by majority vote; identify which points require source verification.
```

---

## Validate against authoritative sources

For consequential claims, verify against a source that has authority for the question.

Examples:

| Claim type | Stronger validation source |
|---|---|
| Contract term | Executed agreement and controlling amendments |
| Regulation | Current official regulatory text and applicable guidance |
| Company policy | Current approved policy repository |
| Financial figure | Governing ledger, workbook inputs, or audited report |
| Product capability | Current official product documentation |
| Schedule or event | Authoritative system of record |
| Scientific claim | Relevant primary research and qualified expert review |

A second Claude answer is not a substitute for a controlling source.

### Authority hierarchy

```text
Controlling primary source
          ↓
Official interpretation or guidance
          ↓
Reliable independent analysis
          ↓
Informal summary
          ↓
Training-memory recall or unsupported assertion
```

The exact hierarchy depends on the domain. The reviewer must define it before the research begins.

---

## Validate calculations deterministically

Grounded prose can still contain bad arithmetic.

For calculations:

1. identify the inputs;
2. identify the formula or rule;
3. compute with code or the authoritative application;
4. retain a reproducible result;
5. compare the narrative to the computed value; and
6. investigate discrepancies.

```text
Source inputs
      ↓
Deterministic calculation
      ↓
Reproducible result
      ↓
Narrative explanation
```

Do not treat a citation to the input values as proof that the calculation is correct.

---

# Practical example: renewal notice in an agreement

## Question

A manager asks:

```text
How much notice do we need to prevent the service agreement from renewing automatically?
```

The evidence package contains:

- the original agreement;
- Amendment 1; and
- Amendment 2.

## Weak request

```text
Read the contract and tell me when we need to cancel.
```

## Weak answer

```text
You should provide written notice at least 30 days before the renewal date.
```

The answer is clear, but no evidence is shown.

## Grounded request

```text
Use only the supplied agreement and amendments.

First, extract every provision that addresses term, renewal, termination, or notice. Quote the relevant language exactly and cite the document, section, and page.

Then determine the notice period for preventing automatic renewal. Apply amendments in controlling order. If the documents conflict or do not resolve the issue, state that explicitly. Do not use general contract knowledge.

Return:
1. evidence table;
2. controlling interpretation;
3. unresolved uncertainty; and
4. action date only if the effective renewal date is supplied.
```

## Evidence extracted

| Source | Location | Extracted support |
|---|---|---|
| Original agreement | Section 8.2 | Automatic renewal unless notice is received 60 days before the end of the current term |
| Amendment 1 | Section 3 | Changes payment timing; does not change renewal notice |
| Amendment 2 | Section 2 | Changes renewal term from one year to six months; does not change notice period |

## Grounded conclusion

```text
The supplied documents require notice at least 60 days before the current term ends. Amendment 2 changes the length of the renewal term but does not change the 60-day notice requirement. The exact notice deadline cannot be calculated unless the current term-end date is confirmed.
```

## Why this is stronger

- the evidence boundary is explicit;
- relevant passages are extracted first;
- amendments are checked;
- the notice period is traceable;
- the missing term-end date remains unknown; and
- the output does not invent a calendar deadline.

This is still an educational example, not legal advice. Consequential contract interpretation requires qualified review.

---

# In-product grounding aids

Product features can make evidence easier to inspect, but they do not eliminate review.

## Claude for Excel

As of August 1, 2026, Anthropic's Help Center describes Claude for Excel as providing direct citations to referenced workbook cells when explaining calculations. It also states that the product is not recommended for final client deliverables without human review or for audit-critical calculations without verification.

Use cell-level citations to answer:

- Which cells support this figure?
- Which formula produces the result?
- Which assumptions affect it?
- Which tab contains the source input?

Then independently check:

- the formula;
- the units;
- the date range;
- hidden assumptions;
- dependency integrity; and
- whether the cited cells are themselves authoritative.

```text
Cell citation → traceability
Recalculation → verification
Qualified review → release decision
```

## Document and connector citations

Current Claude product surfaces may provide clickable citations to document sections, emails, calendar events, Drive files, or other connected records. These citations improve navigation and auditability.

They still require the reviewer to confirm:

- the correct source was selected;
- the citation supports the claim;
- the source is current and authoritative;
- access or parsing was complete; and
- relevant conflicting evidence was not omitted.

> Product citation features reduce the cost of checking. They do not transfer accountability away from the reviewer.

---

# A grounding ladder

Use the least complex level that fits the consequence of error.

| Level | Method | What it establishes |
|---|---|---|
| 0 | Fluent answer only | Nothing beyond generated text |
| 1 | Self-review or repeated runs | Possible instability, omissions, or contradictions |
| 2 | Claim-to-source citations | Traceability to the selected evidence set |
| 3 | Quote-first or cell-level grounding | More inspectable source support |
| 4 | Independent authoritative validation | Stronger factual basis |
| 5 | Deterministic testing and qualified human review | Release readiness for consequential use |

Do not confuse a lower level with a higher one.

```text
Self-consistency is not source support.
Source support is not independent validation.
Independent validation is not authorization to release.
```

---

# Verification checklist

Before relying on a material output, ask:

## Prompt design

- [ ] Did the prompt allow `unknown` or `not covered`?
- [ ] Is the evidence boundary explicit?
- [ ] Is the source hierarchy defined?
- [ ] Are citations required at a checkable location?
- [ ] Should evidence be extracted before analysis?
- [ ] Is unsupported content supposed to be retracted or qualified?

## Output review

- [ ] Can every material claim be traced?
- [ ] Does each citation support the full claim?
- [ ] Were conditions, exceptions, units, dates, and scope preserved?
- [ ] Are fact, inference, assumption, and uncertainty separated?
- [ ] Were all required sources and sections covered?
- [ ] Were conflicting sources disclosed?

## Independent validation

- [ ] Were high-stakes claims checked against authoritative sources?
- [ ] Were calculations recomputed deterministically?
- [ ] Were unstable points identified through comparison or testing?
- [ ] Did a qualified reviewer examine consequential conclusions?
- [ ] Is the final release decision documented?

---

# Common anti-patterns

## Anti-pattern 1: “Add citations” with no evidence source

**Failure:** The prompt requests citation-shaped text without supplying or retrieving evidence.

**Repair:** Provide or retrieve the evidence and require precise claim-to-source locations.

## Anti-pattern 2: Treating any citation as proof

**Failure:** The cited source exists but does not support the full statement.

**Repair:** Compare the claim with the exact passage and classify support.

## Anti-pattern 3: Majority vote across model runs

**Failure:** Three similar outputs are treated as three independent confirmations.

**Repair:** Use disagreement to locate instability; use authoritative evidence to decide correctness.

## Anti-pattern 4: Quote extraction without coverage checks

**Failure:** The extracted quotes are accurate, but important sections or documents were never reviewed.

**Repair:** Pair quote-first analysis with a source-coverage matrix.

## Anti-pattern 5: Restricting to sources that cannot answer the question

**Failure:** The evidence boundary is too narrow, but the output is still expected to decide.

**Repair:** Permit `not covered`, expand the authorized evidence set, or escalate.

## Anti-pattern 6: Grounded inputs, unverified calculation

**Failure:** The numbers are cited, but the arithmetic is wrong.

**Repair:** Recompute deterministically and reconcile the narrative.

## Anti-pattern 7: Using an authoritative source that is stale or out of scope

**Failure:** The source is official but applies to a different date, jurisdiction, version, population, or product.

**Repair:** Check authority, currency, scope, and applicability—not authority alone.

---

# Exam reasoning pattern

For fact-checking and grounding scenarios:

1. identify the material claim or decision;
2. define the permitted evidence set and authority hierarchy;
3. allow explicit uncertainty;
4. prefer direct quotations or precise locations for important claims;
5. check that citations support the full statement;
6. distinguish source grounding from independent validation;
7. use repeated runs to find instability, not to prove truth;
8. route arithmetic and exact checks to deterministic methods;
9. require qualified human review when consequences or authority demand it; and
10. release, edit, verify, escalate, or reject.

```text
No source boundary       → define one
Evidence is silent       → say unknown or not covered
Long source              → quote first
Claim has citation       → inspect actual support
Runs disagree            → investigate instability
Runs agree               → still verify material claims
Calculation matters      → recompute deterministically
High-stakes conclusion   → authoritative source + qualified review
```

---

# Knowledge check

## Question 1

Why is permission to say `I don't know` useful?

**Answer:** It makes a supported non-answer acceptable when the evidence is insufficient, reducing pressure to fill the gap with unsupported content.

## Question 2

What is the difference between source restriction and authoritative validation?

**Answer:** Source restriction limits what evidence the model may use. Authoritative validation independently checks whether a material claim is correct using the controlling or most trustworthy source.

## Question 3

Does agreement across three model runs prove the answer is true?

**Answer:** No. Agreement may indicate stability, but the runs are not independent evidence and can reproduce the same unsupported claim.

## Question 4

Why extract quotes before analysis?

**Answer:** It exposes the evidence basis, conditions, omissions, and conflicts before interpretation is added.

## Question 5

What makes a citation auditable?

**Answer:** The source can be accessed, the location can be found, and the cited content supports the full claim within the relevant scope and date.

## Question 6

What does a cell-level citation establish in a spreadsheet?

**Answer:** It improves traceability to workbook inputs or formulas. It does not by itself prove that the formula, assumptions, units, or resulting calculation are correct.

## Question 7

What should happen when a post-generation citation audit cannot find support for a claim?

**Answer:** The claim should be retracted, narrowed, marked unsupported, or escalated—not defended through additional unsupported explanation.

---

# Flashcards

## Flashcard 1

**Q:** What is grounding?

**A:** Connecting material claims to inspectable evidence with enough location, scope, and context to evaluate support.

## Flashcard 2

**Q:** What is the safest response when supplied sources do not answer the question?

**A:** State that the issue is not covered or remains unknown rather than estimating.

## Flashcard 3

**Q:** What is quote-first analysis?

**A:** Extracting and locating exact supporting passages before drawing conclusions from them.

## Flashcard 4

**Q:** What is the correct use of Best-of-N comparison?

**A:** Detecting instability and soft spots that require verification, not deciding truth by majority vote.

## Flashcard 5

**Q:** What is the difference between a citation and support?

**A:** A citation points to a source; support means the cited content actually justifies the full claim.

## Flashcard 6

**Q:** What should verify consequential calculations?

**A:** Reproducible deterministic computation using authoritative inputs, followed by appropriate review.

## Flashcard 7

**Q:** What do cell-level citations provide?

**A:** Traceability to workbook cells; they do not replace formula, assumption, or human review.

## Flashcard 8

**Q:** What is the grounding ladder's key warning?

**A:** Self-consistency is not source support, source support is not independent validation, and validation is not authorization to release.

---

# Short recap

```text
1. Permit uncertainty.
2. Define the evidence boundary.
3. Require checkable claim-to-source locations.
4. Extract evidence before analysis when the source is long or consequential.
5. Audit claims after generation and retract unsupported ones.
6. Use repeated runs to find instability, not to vote on truth.
7. Validate important claims against authoritative sources.
8. Recompute calculations deterministically.
9. Treat product citations as traceability aids, not proof.
10. Document the release decision.
```

The central rule is:

> Build the evidence path before the answer, then inspect that path before relying on the result.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, medical, compliance, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was dated June 2026. Product-specific statements were rechecked against official Anthropic sources on **August 1, 2026**.

Official references:

- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)

Product features, citation behavior, plan availability, interfaces, and review guidance can change. Verify the current official documentation and the actual tool surface before relying on implementation-specific claims.

## Related material

- [Hallucinations, Inconsistencies, and Bias](03-hallucinations-inconsistencies-bias.md)
- [Discernment: Accuracy and Completeness](02-discernment-accuracy-completeness.md)
- [Module 3 overview](../README.md)
- [Fact-Checking and Grounding prompt notebook](../../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Grounded Verification Pattern](../../../patterns/grounded-verification-pattern.md)
- [Failure Signature Review Pattern](../../../patterns/failure-signature-review-pattern.md)
- [Evaluation Canvas](../../../ai-systems-engineering/worksheets/evaluation-canvas.md)
