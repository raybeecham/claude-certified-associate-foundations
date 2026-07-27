# Module 3 Prompt Notebook: Discernment — Accuracy and Completeness

These prompts are study aids and workflow starting points. They do not replace qualified review, authoritative evidence, professional standards, or independent validation.

Use fictional, generic, synthetic, public, or explicitly authorized material.

## 1. Plain-English evaluator

```text
Explain the difference between accuracy, completeness, and fitness for purpose in plain English.

Use:
- one short analogy;
- one practical workplace example;
- one sentence explaining why a polished answer can still fail; and
- a six-line recap.

Do not use specialist terminology unless you define it immediately.
```

## 2. Three-reference review planner

```text
I need to evaluate the following AI-assisted output.

Intended use:
[USE]

Audience:
[AUDIENCE]

Original requirements:
[REQUIREMENTS]

Authorized source material:
[SOURCES]

Applicable professional standards:
[STANDARDS]

Output to review:
[OUTPUT]

Build a review plan using these three references:
1. requirements;
2. source material; and
3. professional standards.

For each reference, identify:
- what must be checked;
- the evidence required;
- the likely failure modes; and
- the reviewer or tool best suited to perform the check.

Do not evaluate claims that cannot be checked from the supplied evidence. Mark them `requires external verification`.
```

## 3. Requirements traceability table

```text
Compare the output against the original request.

Original request:
[REQUEST]

Output:
[OUTPUT]

Create a table with:
- requirement;
- present in output?;
- correct?;
- evidence or location;
- defect;
- required action.

Use only these requirement statuses:
- met;
- partially met;
- missing;
- unclear.

Do not add requirements that were not part of the request or applicable standard.
```

## 4. Material-claim inventory

```text
Extract every material claim from the output below.

A material claim is one that could change a decision, create an external consequence, affect a comparison, or require evidence.

Output:
[OUTPUT]

Return a table with:
- claim ID;
- exact or closely paraphrased claim;
- claim type: fact / number / date / quotation / comparison / causal statement / recommendation input / compliance statement / other;
- consequence if wrong;
- source required;
- verification priority: high / medium / low.

Do not verify the claims yet.
```

## 5. Claim-to-source support check

```text
Evaluate each claim only against the supplied sources.

Claims:
[CLAIMS]

Sources:
[SOURCES]

For each claim, return:
- claim ID;
- source and location;
- support status: fully supported / partially supported / unsupported / conflicting;
- missing condition, exception, unit, date, or qualification;
- corrected wording when support is partial;
- follow-up action.

Do not use training memory or outside knowledge. If the sources do not support the claim, say so directly.
```

## 6. Accuracy review

```text
Review the output for accuracy.

Output:
[OUTPUT]

Evidence:
[EVIDENCE]

Check for:
- fabricated or unsupported facts;
- incorrect numbers or dates;
- misquotation or attribution;
- contradictions;
- incorrect calculations;
- conclusions that do not follow from the evidence;
- inference presented as fact; and
- overstated certainty.

Return:
1. accuracy defects;
2. supported content that should be preserved;
3. claims requiring independent verification; and
4. a provisional accuracy verdict.

Do not perform a completeness review in this pass.
```

## 7. Completeness review

```text
Review the output for completeness, separately from accuracy.

Intended purpose:
[PURPOSE]

Requirements or checklist:
[CHECKLIST]

Source coverage expectations:
[EXPECTED SOURCES OR CATEGORIES]

Output:
[OUTPUT]

Identify:
- required elements that are absent;
- missing options, risks, dependencies, exceptions, assumptions, or limitations;
- source categories not covered;
- missing units, denominators, dates, or decision conditions; and
- omissions that could change the intended decision.

Return a completeness table and a provisional completeness verdict.

Do not assume that correct visible statements make the output complete.
```

## 8. Professional-standards review scaffold

```text
Help a qualified reviewer evaluate this output against professional standards.

Domain:
[DOMAIN]

Applicable standards, policies, procedures, or review norms:
[STANDARDS]

Output:
[OUTPUT]

Create a checklist that asks whether the output includes the required:
- evidence;
- units and definitions;
- reasoning;
- qualifications;
- traceability;
- approvals;
- uncertainty handling;
- disclosures; and
- domain-specific controls.

Do not make a final professional determination. Identify where qualified human judgment or authoritative interpretation is required.
```

## 9. Stakes-calibration matrix

```text
Calibrate the required review depth for this AI-assisted output.

Use case:
[USE CASE]

Audience:
[AUDIENCE]

Decision or action supported:
[DECISION]

Potential harm if wrong:
[HARM]

Reversibility:
[REVERSIBILITY]

Evidence quality:
[EVIDENCE QUALITY]

Uncertainty:
[UNCERTAINTY]

Return:
1. stakes classification: low / material / high;
2. reasoning;
3. minimum review level;
4. required evidence;
5. required reviewer expertise and authority;
6. deterministic checks;
7. whether qualified human review is mandatory; and
8. release-blocking conditions.
```

## 10. Three-way triage

```text
Assign one verdict to the output:
- ready to use;
- needs revision; or
- needs human override.

Intended use:
[USE]

Stakes:
[STAKES]

Requirements result:
[RESULT]

Source-support result:
[RESULT]

Professional-standards result:
[RESULT]

Accuracy result:
[RESULT]

Completeness result:
[RESULT]

Unresolved uncertainty:
[UNCERTAINTY]

Return:
- verdict;
- scope of the verdict;
- three strongest reasons;
- unresolved issues;
- next action;
- who must own the next action; and
- what must be rechecked before release.

Do not use `ready to use` unless the review depth is proportionate to the stakes.
```

## 11. Decision-ready review record

```text
Create a concise evaluation record for the following output.

Output name and version:
[VERSION]

Prompt or task version:
[PROMPT VERSION]

Evidence-set version:
[EVIDENCE VERSION]

Intended use:
[USE]

Review findings:
[FINDINGS]

Return a table with:
- reviewed item;
- intended use;
- stakes;
- requirements result;
- source result;
- accuracy defects;
- completeness defects;
- professional-standard concerns;
- verdict;
- reviewer role;
- next action; and
- date or review version.

Use `none found through this review` rather than claiming that no defects exist.
```

## 12. Over-verification check

```text
Determine whether the proposed review plan is proportionate or excessive.

Use case:
[USE CASE]

Output status:
[PROVISIONAL / INTERNAL / EXTERNAL / FINAL]

Stakes:
[STAKES]

Proposed review steps:
[STEPS]

Assess:
- which steps are necessary;
- which steps add little value;
- which risks remain uncovered;
- whether the output's provisional limits are explicit; and
- the minimum sufficient review plan.

Do not recommend maximum review by default.
```

## 13. Human-override decision

```text
Determine whether qualified human override is required before this output can be used.

Output:
[OUTPUT]

Intended action:
[ACTION]

Available evidence:
[EVIDENCE]

Current reviewer qualifications and authority:
[REVIEWER]

Uncertainty and known defects:
[DEFECTS]

Potential consequence:
[CONSEQUENCE]

Identify:
- missing authority;
- missing expertise;
- missing evidence;
- severe or systemic defects;
- irreversible or high-impact consequences;
- required expert role; and
- whether the draft may be used only as input to expert review.

Clarify that human override requires substantive ownership, not a ceremonial approval click.
```

## 14. Practical status-summary drill

```text
Review this project-status summary using the three-reference protocol.

Requirements:
Leadership needs the current target date, material dependencies, open high-priority risks, and the next decision point.

Source notes:
- production target: September 9;
- target depends on privacy approval;
- one critical integration defect remains open;
- training begins September 2;
- go/no-go review is September 5.

Generated summary:
The project is on track for production on September 9. Training begins September 2, and final preparations are underway.

Return:
1. requirements result;
2. source-support result;
3. professional-standard result;
4. accuracy result;
5. completeness result;
6. stakes classification;
7. verdict; and
8. a corrected summary.
```

## 15. Accuracy-versus-completeness oral drill

```text
Give me eight short scenarios one at a time.

For each scenario, ask me to classify the dominant problem as:
- accuracy;
- completeness;
- both;
- professional-standard failure;
- review-depth failure; or
- no material defect for the stated use.

After I answer:
- tell me whether I am correct;
- explain the distinction in no more than five sentences;
- identify the three evaluation references; and
- ask the next scenario.

Use original professional scenarios. Do not reproduce proprietary course or exam questions.
```

## 16. Beginner recap generator

```text
Summarize the three-reference discernment protocol for a beginner.

Include exactly:
- one sentence defining discernment;
- the three references;
- the difference between accuracy and completeness;
- one sentence on stakes calibration;
- the three possible verdicts; and
- a six-line recap.

Use plain English and no unexplained jargon.
```

## 17. Reflection log

```text
Help me record what I learned from reviewing an AI-assisted output.

Task:
[TASK]

Output defect:
[DEFECT]

How it was detected:
[DETECTION]

Reference that exposed it:
Requirements / Source material / Professional standards

Quality dimension:
Accuracy / Completeness / Fitness / Review depth

Stakes:
[STAKES]

Verdict:
[VERDICT]

Create a short reflection with:
- what failed;
- why it was easy to miss;
- the control that would detect it earlier;
- whether the prompt, evidence, workflow, review, or authority should change; and
- one reusable rule.
```

## Study rule

> Review against requirements, sources, and professional standards; inspect accuracy and completeness separately; then choose a verdict and review depth based on the consequences of error.
