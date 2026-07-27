# Lesson 3: Hallucinations, Inconsistencies, and Bias

## Overview

AI-generated output can be fluent, organized, and persuasive whether it is well supported or wrong.

That means reviewers cannot wait for an error to *sound* suspicious. They need to recognize recurring failure signatures and check them deliberately.

This lesson focuses on four related risks:

1. **hallucinations** — content presented without adequate support;
2. **inconsistencies** — claims that conflict with one another or with the evidence;
3. **bias** — framing, selection, or emphasis that unfairly tilts the result; and
4. **silent omissions** — important material that is never discussed.

> Plausibility is a writing quality. Verification is an evidence quality.

## Plain-English explanation

Claude can sound certain even when it is guessing.

A beginner can review for the major failure types by asking:

```text
Did Claude add anything the evidence does not support?
                         ↓
Does one part of the answer disagree with another?
                         ↓
Does the answer lean toward one side without sufficient reason?
                         ↓
Did it skip an important source, option, exception, or risk?
```

The four questions map to four failure families:

| Question | Failure family |
|---|---|
| Did it invent or overstate something? | Hallucination |
| Does it disagree with itself or the sources? | Inconsistency |
| Does its framing unfairly favor one conclusion? | Bias |
| Did it leave out material information? | Completeness failure |

The answer does not need to contain an obvious absurdity to fail. The most dangerous defects are often ordinary-looking sentences that fit naturally into the rest of the response.

## One analogy: checking a road-trip map

Imagine that an AI assistant creates a route for a long road trip.

- A **hallucination** is a road that does not exist.
- An **inconsistency** is one page telling you to drive east while another says the destination is west.
- **Bias** is the route favoring scenic roads because your question sounded enthusiastic about scenery, even though you asked for the fastest trip.
- A **completeness failure** is leaving out a major road closure.
- A **capability hallucination** is the assistant claiming it already booked the hotel when no booking tool was available and no reservation exists.

The route can still look professional. It may include distances, turn-by-turn instructions, and estimated arrival times. None of that proves the roads, assumptions, or claimed actions are real.

The lesson is:

> Do not judge the map by how polished it looks. Check whether the route exists, agrees with itself, fits the real objective, includes material conditions, and produced any action it claims to have completed.

## Why failure signatures matter

Reading every sentence with equal suspicion is inefficient. A better method is to recognize the places where defects commonly hide.

```text
High-risk signature
        ↓
Targeted verification
        ↓
Documented finding
        ↓
Correct, qualify, escalate, or reject
```

A signature does not prove that a claim is wrong. It tells the reviewer where verification effort is most valuable.

## Failure-signature quick reference

| Signature | Possible failure | First check |
|---|---|---|
| Precise number with no source | Fabricated specific | Locate the number in authoritative evidence |
| Quotation with no page or location | Fabricated or altered quote | Compare the exact text with the source |
| Citation that looks formal but cannot be opened | Fabricated citation | Resolve the source and inspect support |
| Absolute answer to a date-sensitive question | Confidence masking uncertainty | Check currency, jurisdiction, scope, and authority |
| Same metric appears with two values | Internal inconsistency | Build a repeated-fact comparison table |
| Summary and appendix disagree | Cross-section inconsistency | Reconcile against the primary evidence |
| Response strongly confirms the prompt's preferred answer | Confirmation bias | Re-run the analysis with neutral criteria and counterevidence |
| Easy files are summarized but a difficult file is absent | Completeness failure | Create a source-coverage matrix |
| “Sent,” “saved,” “filed,” or “updated” without an action record | Capability hallucination | Confirm the tool call, receipt, artifact, or external state |
| Recommendation lacks risks or alternatives | Framing or omission bias | Require opposing considerations and decision criteria |

---

# Hallucination patterns

A hallucination is content stated as if it is supported when the available evidence does not justify it.

Hallucinations are not limited to bizarre facts. They often appear as reasonable completions of an incomplete pattern.

## Pattern 1: Plausible but unsupported claims

Example:

```text
Regional service providers are increasingly moving to consumption-based pricing because customers prefer predictable scaling.
```

This may be true in some markets. But without evidence, scope, or attribution, it is still unsupported.

### Signature

- sounds reasonable;
- fits common industry narratives;
- contains no source boundary;
- may use broad terms such as `increasingly`, `typically`, or `most`; and
- would be difficult to disprove through casual reading.

### Review action

Ask:

1. What source supports the claim?
2. What population and time period does it cover?
3. Is the statement fact, inference, or hypothesis?
4. Would the conclusion change if the claim were removed?

## Pattern 2: Fabricated specifics

Specificity feels authoritative. That is why invented details are persuasive.

Common fabricated specifics include:

- percentages;
- dollar amounts;
- dates;
- names;
- quotations;
- report titles;
- publication details;
- page references;
- legal provisions;
- product capabilities; and
- exact benchmark results.

Example:

```text
A 2025 industry survey found that 71% of regional hospitals had deployed an AI documentation assistant.
```

The figure may be plausible. The source may not exist.

### Precision-provenance rule

```text
More precision
      ↓
Higher expectation of provenance
```

A claim such as `many organizations are experimenting with AI` is vague and still requires care. A claim such as `71% adopted the technology in 2025` demands a traceable source, defined population, methodology, and date.

### Review action

For each precise claim, record:

| Claim | Source | Location | Scope | Status |
|---|---|---|---|---|
| 71% adoption | Not identified | — | Undefined | Unsupported |

## Pattern 3: Fabricated or weak citations

A citation is not proof merely because it has the appearance of a citation.

Citation failures include:

- a source that does not exist;
- a real source with an invented title;
- a valid link that does not support the claim;
- a source supporting only part of the statement;
- an outdated source used for a current claim;
- a secondary source cited when a controlling primary source exists; and
- a quotation that is paraphrased but placed inside quotation marks.

### Review action

Open the source and ask:

```text
Does the source exist?
        ↓
Is it authoritative for this question?
        ↓
Does it support the full claim?
        ↓
Are scope, date, conditions, and exceptions preserved?
```

## Pattern 4: Confidence masking uncertainty

AI systems do not reliably adjust tone in proportion to actual evidence strength.

A well-supported conclusion and an uncertain inference may both appear in direct, polished language.

Example:

```text
This grant expense is allowable under the award.
```

That conclusion may depend on:

- the current award terms;
- applicable cost principles;
- agency guidance;
- the expense category;
- documentation;
- timing;
- prior approval; and
- qualified grants-management review.

An unqualified sentence hides the missing analysis.

### Certainty-evidence check

| Language strength | Evidence expected |
|---|---|
| `may`, `could`, `appears` | Preliminary or incomplete support |
| `likely`, `generally` | Substantial but qualified support |
| `is`, `will`, `proves` | Strong, direct, authoritative support |

When language strength exceeds evidence strength, the output is overstated even if the underlying possibility is reasonable.

## Pattern 5: Unsupported causal explanations

Models may turn correlation, sequence, or coincidence into causation.

Example:

```text
Customer satisfaction improved because the new portal reduced support delays.
```

The evidence may show that satisfaction rose after the portal launch. That does not establish why it rose.

### Review action

Ask whether the source supports:

- correlation;
- temporal sequence;
- contributor language;
- a causal mechanism; or
- a controlled causal conclusion.

Repair by matching the wording to the evidence:

```text
Customer satisfaction increased after the portal launch. The available data does not isolate the portal's effect from staffing, seasonal, or process changes.
```

---

# Inconsistency patterns

An inconsistency occurs when parts of the output cannot all be correct at the same time, or when the output conflicts with the governing evidence.

## Pattern 1: Internal contradiction

Example:

```text
Executive summary: The addressable market is approximately $3.2 billion.

Financial model section: The forecast assumes a $3.8 billion addressable market.
```

Each sentence looks reasonable in isolation. Together they create an unresolved contradiction.

### Why long outputs are vulnerable

Long outputs distribute repeated facts across:

- executive summaries;
- tables;
- appendices;
- recommendations;
- charts;
- calculations; and
- conclusions.

Reviewers often read locally rather than comparing every repeated statement.

### Repeated-fact consistency table

| Fact or metric | Location 1 | Location 2 | Governing source | Resolution |
|---|---|---|---|---|
| Market size | $3.2B | $3.8B | Source report: $3.2B | Correct model section |

## Pattern 2: Summary-detail mismatch

A summary may present a stronger or simpler conclusion than the details justify.

Example:

```text
Summary: All critical readiness items are complete.

Readiness table: Identity testing remains open and is rated critical.
```

The table may be correct while the summary is not.

### Review action

Compare conclusions against:

- tables;
- appendices;
- source notes;
- unresolved-item lists;
- calculations; and
- exceptions.

## Pattern 3: Source contradiction

The output may be internally consistent but consistently wrong relative to the source.

Example:

A policy summary repeatedly states that records must be retained for six years, while the supplied policy specifies seven years.

Repetition does not increase truth. It may only propagate one initial misreading.

## Pattern 4: Temporal inconsistency

An output may combine facts from different dates as if they describe one current state.

Example:

- employee count from a 2024 report;
- revenue from a 2025 filing;
- product availability from a 2026 webpage; and
- a conclusion describing all three as `current`.

### Review action

Attach an `as of` date to material claims and flag mixed-period comparisons.

## Pattern 5: Arithmetic inconsistency

The prose, table, and calculation may disagree.

Example:

- table values total $840,000;
- narrative states $810,000;
- recommendation uses $900,000.

Exact arithmetic should be recalculated with code, a spreadsheet, or another deterministic method.

---

# Bias patterns

Bias in AI output often appears through framing, selection, omission, or unequal scrutiny rather than openly prejudicial language.

## Pattern 1: Confirmation bias

If a prompt contains a preferred conclusion, the response may organize evidence around that preference.

Prompt:

```text
Explain why we should accelerate the migration this quarter.
```

The task already assumes acceleration is the correct answer.

The resulting analysis may emphasize:

- opportunity;
- urgency;
- competitor movement; and
- benefits;

while minimizing:

- readiness gaps;
- dependencies;
- cost uncertainty;
- operational risk; and
- credible alternatives.

### Neutralization repair

```text
Evaluate whether the migration should be accelerated, delayed, or phased. Use the approved criteria for readiness, cost, operational risk, dependencies, and strategic value. Present evidence for and against each option before recommending.
```

## Pattern 2: Selection bias

The response may use only the evidence that is easy to locate or aligns with the emerging narrative.

Examples:

- using three favorable customer comments and ignoring twelve negative ones;
- summarizing the shortest reports but omitting the complex appendix;
- selecting recent sources while excluding an authoritative older standard still in force; and
- comparing vendors only on criteria where one vendor performs well.

### Review action

Create a coverage matrix:

| Required source or population | Reviewed? | Represented in output? | Material omission? |
|---|---|---|---|
| Document A | Yes | Yes | No |
| Document B | Yes | Yes | No |
| Document C — critical appendix | No | No | Yes |

## Pattern 3: Framing bias

Word choice can tilt interpretation without changing the underlying facts.

Compare:

```text
The pilot achieved only 62% adoption.
```

with:

```text
The pilot reached 62% adoption during its first phase.
```

Neither framing is automatically correct. The reviewer must ask which wording best reflects the baseline, target, time period, and decision context.

## Pattern 4: Unequal scrutiny

One option may receive detailed criticism while another is described only through benefits.

A fair comparison applies the same:

- criteria;
- evidence standards;
- time periods;
- uncertainty rules;
- scoring scales; and
- level of skepticism.

## Pattern 5: False balance

Bias control does not mean treating every position as equally supported.

If one conclusion has strong evidence and another has none, presenting them as equally credible is also misleading.

The objective is evidence-proportionate treatment, not automatic symmetry.

---

# The silent completeness failure

A response can list many valid findings and still miss the most important one.

This pattern is dangerous because visible detail creates an impression of thoroughness.

## Original field-style example

A reviewer asks Claude to compare six incident reports and identify material differences.

The output provides a detailed comparison of five reports. It does not discuss the sixth report, which contains the only event classified as critical severity.

Nothing in the prose is necessarily false.

The failure is coverage.

```text
Five easy files summarized thoroughly
                  +
One difficult, decision-critical file omitted
                  =
Confident but incomplete analysis
```

### Coverage checks

Before accepting a batch analysis, verify:

- expected number of files;
- actual number processed;
- file names or identifiers;
- page or section coverage;
- parsing or access failures;
- empty or unreadable inputs;
- unusually short treatment of complex sources; and
- whether the highest-risk source received explicit attention.

> A long list of findings does not prove that the full evidence set was reviewed.

---

# Capability hallucination

A capability hallucination occurs when Claude claims to have completed an action that was not actually performed.

Examples include:

- `I sent the email.`
- `I filed the ticket.`
- `I updated the calendar.`
- `I saved the document to the shared drive.`
- `I submitted the form.`
- `I notified the team.`

## Current capability boundary

Claude's available actions vary by product surface, plan, connected apps, tools, permissions, and user approvals.

The durable rule is not `Claude can never take actions.` The durable rule is:

> An external action is verified only when the required capability was available, the action was actually invoked, and the resulting external state or receipt confirms success.

## Action verification chain

```text
Requested action
      ↓
Required tool or integration available?
      ↓
Correct tool invoked?
      ↓
Permission or approval granted?
      ↓
Tool returned success?
      ↓
External state, receipt, draft, event, file, or ticket confirmed?
```

A conversational sentence claiming success is not an action receipt.

## Practical checks

| Claimed action | Evidence of completion |
|---|---|
| Email sent | Sent-message record, provider receipt, or confirmed thread state |
| Draft created | Draft appears in the connected mailbox |
| File saved | File exists at the confirmed destination |
| Calendar event created | Event appears with expected time and attendees |
| Ticket filed | Ticket identifier and accessible record |
| Data updated | Read-back confirms the new value |

Official Anthropic guidance notes that Claude can hallucinate capabilities and does not have access to tools that are not explicitly integrated. Current Claude products may support connectors, file creation, code execution, and computer-use features, so reviewers should verify the actual capability and result rather than rely on a universal assumption.

---

# One practical example: vendor recommendation

## The request

A team asks Claude to compare two service proposals and recommend one for a one-year pilot.

The approved criteria are:

- annual cost;
- implementation time;
- support coverage;
- data residency;
- termination flexibility; and
- operational risk.

## Generated output

```text
Vendor North is the stronger choice. It costs $84,000 annually, offers 24/7 support, can be implemented in six weeks, and carries lower operational risk.

Vendor South costs $96,000 annually and provides business-hours support. Although South has stronger termination terms, North's lower cost and superior support make it the clear recommendation.

I saved the final comparison to the procurement workspace.
```

The appendix later lists Vendor North's annual cost as `$91,000`.

## Failure-pattern review

### Hallucination

The proposal does not state that Vendor North offers 24/7 support. The output converted an unanswered support questionnaire item into a positive capability.

**Status:** Unsupported claim.

### Inconsistency

The narrative says `$84,000`; the appendix says `$91,000`.

**Status:** Internal contradiction requiring source reconciliation.

### Bias

The recommendation emphasizes North's cost and support while giving little attention to:

- unresolved data-residency evidence;
- implementation dependencies;
- South's stronger termination flexibility; and
- the uncertainty around North's support model.

The phrase `clear recommendation` exceeds the evidence.

**Status:** Confirmation and framing bias.

### Completeness

Data residency was an approved criterion but is not evaluated.

**Status:** Material omission.

### Capability hallucination

No procurement-workspace tool was available and no saved artifact or location was returned.

**Status:** Claimed external action is unverified.

## Verdict

**Reject the recommendation as currently written and reconstruct the comparison from the proposals.**

This is not a one-sentence revision. Multiple interacting defects affect the evidence, score, and claimed action.

## Safer next step

```text
1. Rebuild a criterion-by-criterion evidence table from the proposals.
2. Mark unanswered items as unknown.
3. Recalculate annual cost using a deterministic method.
4. Apply equal scrutiny to both vendors.
5. Produce a qualified recommendation only after material gaps are resolved.
6. Save or transmit the result only through an available tool and verify the external record.
```

---

# Failure-pattern gallery

The examples below are original and illustrate what the signatures look like in practice.

## Gallery 1: Fabricated specific

**Prompt**

```text
How common was AI-assisted forecasting among regional manufacturers in 2025?
```

**Output**

```text
Approximately 68% of regional manufacturers used AI-assisted forecasting in 2025, up from 44% in 2024.
```

**Signature**

- precise percentages;
- year-over-year comparison;
- no population definition;
- no source; and
- no methodology.

**Review verdict:** Unsupported until a credible source is located and shown to support the full claim.

## Gallery 2: Confidence masking uncertainty

**Prompt**

```text
Can the organization charge this expense to the grant?
```

**Output**

```text
Yes. The expense is allowable and can be charged directly to the award.
```

**Signature**

The answer ignores award terms, cost principles, documentation, approval conditions, and qualified review.

**Review verdict:** Needs human override. Use the answer only as a question list for a grants professional.

## Gallery 3: Internal contradiction

**Output section 1**

```text
The program serves approximately 18,400 users.
```

**Output section 6**

```text
Assuming a current user base of 21,000, annual savings would total $1.26 million.
```

**Signature**

A repeated baseline changes without explanation.

**Review verdict:** Needs revision and recalculation against the governing source.

## Gallery 4: Confirmation bias

**Prompt**

```text
Build the case for consolidating all support operations immediately.
```

**Output**

The response lists cost savings and management simplicity but omits transition risk, service continuity, local expertise, contractual constraints, and phased alternatives.

**Signature**

The prompt asks for advocacy rather than evaluation, and the response mirrors that preference.

**Review verdict:** Reframe the task neutrally before treating the result as analysis.

## Gallery 5: Capability hallucination

**Output**

```text
I created the incident ticket and notified the response team.
```

**Observed environment**

No ticketing or messaging tool was available, and no ticket number or notification record exists.

**Review verdict:** The claimed actions did not occur. Create them through authorized tools or perform them manually.

---

# A repeatable failure-signature review protocol

Use this protocol for material outputs.

```text
1. Define purpose, stakes, and evidence boundary
                 ↓
2. Build a claim and action inventory
                 ↓
3. Scan precise claims for provenance
                 ↓
4. Compare certainty with evidence strength
                 ↓
5. Check repeated facts for consistency
                 ↓
6. Challenge the favored conclusion
                 ↓
7. Verify coverage and omissions
                 ↓
8. Confirm claimed external actions
                 ↓
9. Document defects and disposition
```

## Step 1: Define purpose, stakes, and evidence boundary

Record:

- intended audience;
- decision or action supported;
- consequence if wrong;
- approved sources;
- required current information;
- required reviewer expertise; and
- acceptable uncertainty.

## Step 2: Build a claim and action inventory

Mark:

- factual claims;
- numbers;
- dates;
- quotations;
- citations;
- comparisons;
- causal explanations;
- recommendations;
- assumptions;
- external-action claims; and
- major omissions suspected from the requirements.

## Step 3: Scan precise claims for provenance

Prioritize:

- percentages;
- dollar amounts;
- dates;
- names;
- titles;
- quotations;
- source references;
- legal or policy provisions; and
- benchmark values.

## Step 4: Compare certainty with evidence strength

Classify each material statement:

| Statement class | Meaning |
|---|---|
| Verified fact | Directly supported by appropriate evidence |
| Qualified fact | Supported, but conditions or limits apply |
| Inference | Reasoned interpretation rather than direct source content |
| Assumption | Working premise not established by evidence |
| Unsupported | No adequate basis identified |
| Conflicting | Relevant sources or sections disagree |

The language should reveal the class rather than hide it.

## Step 5: Check repeated facts for consistency

Search or extract repeated:

- numbers;
- dates;
- names;
- option labels;
- ratings;
- totals;
- assumptions; and
- recommendations.

Use code or a spreadsheet when the output is long or contains many repeated values.

## Step 6: Challenge the favored conclusion

Ask:

1. What evidence would weaken this conclusion?
2. Which alternatives received less scrutiny?
3. Did the prompt imply a preferred answer?
4. Were the same criteria applied to all options?
5. Are risks and benefits represented proportionately?
6. Is uncertainty treated consistently?

## Step 7: Verify coverage and omissions

Compare:

- expected files versus processed files;
- required sections versus output sections;
- known options versus discussed options;
- required criteria versus evaluated criteria;
- source chapters versus summarized chapters; and
- high-risk inputs versus attention received.

## Step 8: Confirm claimed external actions

Do not rely on prose alone.

Verify:

- the correct tool existed;
- it was invoked;
- authorization was granted;
- the response indicated success;
- an identifier or artifact was returned; and
- the external system reflects the expected state.

## Step 9: Document defects and disposition

Use the wider Module 3 triage:

| Disposition | Use when |
|---|---|
| **Release** | No material defect remains for the stated use |
| **Edit** | Presentation or a bounded non-evidentiary issue needs correction |
| **Verify** | Material claims or calculations need additional checking |
| **Escalate** | Qualified authority or expertise is required |
| **Reject** | The output is materially unreliable, biased, contradictory, incomplete, or falsely claims completed actions |

---

# Model self-review: useful but not independent proof

Claude can help identify possible contradictions, unsupported claims, or missing coverage in its own output.

Useful prompts include:

```text
List every quantitative claim and identify its source.
```

```text
Build a table of repeated facts and flag conflicting values.
```

```text
Identify evidence that would weaken your recommendation.
```

```text
List every required source and state where it is represented in the output.
```

This can improve review efficiency, but it does not create independent verification.

The same system may:

- miss the same defect again;
- invent a source during self-review;
- rationalize its earlier conclusion;
- overlook omitted material it never processed; or
- claim that an action succeeded without external confirmation.

Use model-assisted review to organize inspection, then validate material findings through sources, deterministic checks, system records, or qualified human review.

---

# Common anti-patterns

## Anti-pattern 1: Trusting confident tone

**Failure:** Assurance is treated as evidence.

**Repair:** Require provenance and uncertainty classification.

## Anti-pattern 2: Checking only suspicious-looking claims

**Failure:** Plausible fabricated details survive because they do not look unusual.

**Repair:** Scan all material specifics and decision-critical claims.

## Anti-pattern 3: Reading a long output only from top to bottom

**Failure:** Contradictory repeated facts are never compared.

**Repair:** Build a cross-document consistency matrix.

## Anti-pattern 4: Asking the model whether it is biased

**Failure:** A general self-assessment replaces criterion-level review.

**Repair:** Apply equal criteria, test counterevidence, and inspect selection and framing.

## Anti-pattern 5: Assuming many findings imply complete coverage

**Failure:** Visible volume masks omitted sources or requirements.

**Repair:** Use a source and requirement coverage matrix.

## Anti-pattern 6: Treating a claimed action as completed

**Failure:** Conversational confirmation substitutes for a tool receipt or external record.

**Repair:** Verify capability, invocation, response, identifier, and external state.

---

# Exam reasoning pattern

For hallucination, inconsistency, and bias scenarios:

1. identify the visible signature;
2. determine whether the problem is support, consistency, framing, coverage, or capability;
3. locate the authoritative evidence or system record;
4. avoid treating confidence, precision, or citations as proof;
5. use deterministic checks for repeated facts and calculations;
6. neutralize prompts that imply a preferred conclusion;
7. verify that every required source and criterion was covered;
8. require qualified human review when stakes or domain authority demand it; and
9. select release, edit, verify, escalate, or reject.

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → tool and external-state verification
```

---

# Knowledge check

## Question 1

Why is a precise percentage without a source a high-risk signature?

**Answer:** Precision creates an appearance of authority. A specific percentage requires traceable evidence defining the population, method, date, and scope.

## Question 2

A report uses the same incorrect number in five places. Is it internally consistent?

**Answer:** It may be internally consistent but still conflict with the source. Consistency does not prove accuracy.

## Question 3

How can a prompt create confirmation bias?

**Answer:** By assuming or advocating a preferred conclusion instead of asking for neutral evaluation against common criteria and counterevidence.

## Question 4

Why can a detailed document comparison still fail completeness?

**Answer:** It may thoroughly discuss some sources while omitting a required or decision-critical source. Volume is not proof of coverage.

## Question 5

What evidence verifies that an external action occurred?

**Answer:** Availability and invocation of the correct tool, required approval, a successful tool result, and confirmation in the external system or resulting artifact.

## Question 6

Can Claude help review its own output?

**Answer:** Yes, it can organize claims, identify possible contradictions, and surface counterarguments, but its self-review is not independent proof and must be validated for material use.

## Question 7

What is the difference between bias control and false balance?

**Answer:** Bias control applies fair criteria and evidence standards. False balance presents weak and strong positions as equally supported even when the evidence differs materially.

---

# Flashcards

## Flashcard 1

**Q:** What is a hallucination?

**A:** Content presented as supported or factual when the available evidence does not justify it.

## Flashcard 2

**Q:** What is the precision-provenance rule?

**A:** The more precise a claim is, the stronger and more traceable its evidence should be.

## Flashcard 3

**Q:** Why are long outputs vulnerable to inconsistency?

**A:** Repeated facts are distributed across summaries, tables, appendices, calculations, and conclusions that reviewers may not compare directly.

## Flashcard 4

**Q:** What is confirmation bias in an AI-assisted analysis?

**A:** The output organizes or emphasizes evidence to support a preferred conclusion implied by the prompt or reviewer.

## Flashcard 5

**Q:** What is a silent completeness failure?

**A:** A materially required source, issue, option, or condition is omitted while the visible output still appears thorough.

## Flashcard 6

**Q:** What is a capability hallucination?

**A:** A claim that an external action was completed when the required tool, invocation, permission, or resulting state does not verify it.

## Flashcard 7

**Q:** Does internal consistency prove factual accuracy?

**A:** No. A response can repeat the same unsupported or incorrect claim consistently.

## Flashcard 8

**Q:** What should a reviewer do when language strength exceeds evidence strength?

**A:** Qualify the statement, obtain stronger evidence, or withhold the conclusion.

---

# Short recap

```text
1. Plausible is not verified.
2. Treat precise unsupported details as high-risk.
3. Compare repeated facts across the full output.
4. Challenge conclusions that mirror the prompt's preference.
5. Check coverage, especially difficult or high-risk sources.
6. Verify external actions through tools and system records.
7. Use model self-review as assistance, not independent proof.
8. Release, edit, verify, escalate, or reject explicitly.
```

The central rule is:

> Look for the signature, trace it to evidence, and verify the result. Do not wait for a fluent failure to look obviously wrong.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute legal, financial, medical, compliance, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was dated June 2026. Product-capability statements were rechecked against official Claude Help Center materials on **July 26, 2026**.

Official references:

- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Claude can falsely claim it sent emails or produced external documents](https://support.claude.com/en/articles/8241188-claude-is-producing-links-that-don-t-work-and-falsely-claiming-that-it-has-sent-emails-or-produced-external-documents-what-s-going-on)
- [Manage Claude's tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)

Capabilities, integrations, plans, interfaces, and approval requirements can change. Verify the current tool surface and external result before relying on a claimed action.

## Related material

- [Discernment: Accuracy and Completeness](02-discernment-accuracy-completeness.md)
- [Module 3 overview](../README.md)
- [Failure Patterns prompt notebook](../../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Failure Signature Review Pattern](../../../patterns/failure-signature-review-pattern.md)
- [Three-Reference Discernment Pattern](../../../patterns/three-reference-discernment-pattern.md)
- [Evaluation Canvas](../../../ai-systems-engineering/worksheets/evaluation-canvas.md)
