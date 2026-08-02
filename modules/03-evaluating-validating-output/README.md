# Module 3: Evaluating & Validating Claude's Output

Associate Persona · Official Exam Domain 2 · **21% of the exam blueprint**

> **Status:** In progress — Module 3 is the active module.

## Why this domain matters

A plausible output is not evidence of a reliable result. Evaluation determines whether an answer is accurate, complete, grounded, internally consistent, appropriately framed, suitable for its audience, and safe to use.

Module 2 focused on specifying intended behavior. Module 3 focuses on inspecting observed behavior and deciding whether it may be released.

```text
Prompt specification
        ↓
Candidate output
        ↓
Discernment
        ↓
Verification and grounding
        ↓
Diligence and human-review gate
        ↓
Edit, release, escalate, or reject
```

> **Module thesis:** Fluency is not proof. An output must be evaluated against requirements, evidence, internal consistency, audience needs, governing obligations, and the consequences of error.

## Course-aligned lesson map

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Discernment: Accuracy & Completeness](lessons/02-discernment-accuracy-completeness.md)
- [x] [03. Hallucinations, Inconsistencies & Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [x] [04. Fact-Checking & Grounding](lessons/04-fact-checking-grounding.md)
- [x] [05. Diligence: When Review Is Non-Negotiable](lessons/05-diligence-human-review.md)
- [ ] 06. Editing & Adapting for Audience
- [ ] 07. Choosing Output Formats
- [ ] 08. Exercise: Triage the Output Set
  - [ ] Exercise
  - [ ] Self-Assessment
- [ ] 09. Module 3 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 10. Module Complete

## Learning progression

```text
Inspect accuracy and completeness
              ↓
Detect hallucinations, inconsistencies, and bias
              ↓
Verify claims against authoritative evidence
              ↓
Determine when qualified human review is mandatory
              ↓
Adapt the content for its actual audience
              ↓
Choose a usable output format
              ↓
Triage: release, edit, verify, escalate, or reject
```

---

# Introduction foundation

Professional AI use contains an accountability asymmetry:

```text
Immediate, visible benefit
          ↓
Faster drafting and synthesis

Delayed, less visible risk
          ↓
Rework, poor decisions, credibility loss, or harm
```

A polished output can contain one plausible unsupported claim among many correct statements. The reviewer must evaluate evidence and consequence rather than rely on tone, confidence, or surface coherence.

The module is anchored in two AI Fluency competencies:

```text
Discernment → How should this output be evaluated?
Diligence   → What responsibility must be satisfied before it is used?
```

It also introduces **verification debt**: unresolved validation work that accumulates when generation exceeds review capacity.

---

# Accuracy and completeness foundation

Discernment begins with three stable references:

```text
Requirements
    +
Source material
    +
Professional standards
    ↓
Accuracy review
    +
Completeness review
    ↓
Stakes-calibrated verdict
```

## Beginner version

```text
Did it do what I asked?
        ↓
Does it match the evidence?
        ↓
Would it be acceptable in the real setting where it will be used?
```

Then separate:

```text
Accuracy     → Is what is present correct?
Completeness → Is anything material missing?
```

An output can be accurate but incomplete. A correct target date may still mislead when the approval dependency is omitted.

## Three-way verdict

```text
Ready to use
Needs revision
Needs human override
```

The verdict is always scoped to a specific use. An internal discussion starter may not be ready for a client, regulator, executive decision, or production action.

---

# Failure-pattern foundation

Plausible language does not reveal whether a claim is supported, the document is consistent, the framing is fair, the evidence set is complete, or a claimed action occurred.

```text
Precise but uncited       → verify provenance
Confident but conditional → calibrate uncertainty
Repeated fact disagrees   → consistency check
Preferred answer echoed   → bias challenge
Important source absent   → coverage check
Action claimed complete   → tool and external-state verification
```

Failure families include:

| Failure family | Meaning |
|---|---|
| Hallucination | A claim is presented with more support than the evidence justifies |
| Inconsistency | Parts of the output, or the output and evidence, cannot all be correct |
| Bias | Selection, framing, emphasis, or scrutiny is uneven relative to criteria and evidence |
| Completeness failure | A material source, requirement, option, condition, or risk is absent |
| Capability hallucination | An external action is claimed without verified execution and external-state confirmation |

Claude capabilities vary by product surface, connected tools, permissions, and approvals. A conversational statement is not an action receipt.

---

# Fact-checking and grounding foundation

The strongest verification is designed before generation.

```text
Purpose and stakes
        ↓
Evidence boundary
        ↓
Permission for unknown
        ↓
Evidence extraction or retrieval
        ↓
Claim-to-source mapping
        ↓
Support classification
        ↓
Independent validation
        ↓
Deterministic checks and qualified review
        ↓
Release disposition
```

## Beginner version

```text
Where did this claim come from?
        ↓
Can I find the cited location?
        ↓
Does it support the full statement?
        ↓
Is the source authoritative, current, and applicable?
        ↓
What still needs independent verification?
```

```text
Citation present
      ≠
Claim supported
```

## Grounding ladder

| Level | Method | What it establishes |
|---|---|---|
| 0 | Fluent output only | Generated text |
| 1 | Self-review or repeated runs | Possible instability or defects |
| 2 | Claim-to-source citations | Traceability to the selected evidence set |
| 3 | Quote-first, section-level, or cell-level grounding | More inspectable support |
| 4 | Independent authoritative validation | Stronger factual basis |
| 5 | Deterministic tests and qualified human review | Consequential release basis |

```text
Self-consistency is not source support.
Source support is not independent validation.
Independent validation is not authorization to release.
```

---

# Diligence foundation

Diligence decides when review is mandatory and places the gate before release or action.

## Four thresholds

```text
Stakes              → What happens if it is wrong?
Reversibility       → Can the action be undone?
Audience            → Who will see or rely on it?
Regulatory exposure → What law, contract, policy, standard, or duty governs it?
```

| Posture | Typical conditions | Review action |
|---|---|---|
| **Green** | Low stakes, reversible, internal, unregulated | Proportionate self-review or peer check |
| **Yellow** | Material decision support or management/external use | Structured evidence review and identified approver |
| **Red** | High stakes, hard to reverse, external or regulated | Qualified human review is mandatory |

> The most severe credible threshold controls the minimum review requirement.

## Fixed do-not-ship gates

At minimum, require human review for:

- final client or external deliverables;
- audit-critical or financially material calculations;
- regulated, confidential, privileged, or highly sensitive work;
- public, legal, regulatory, or incident communications;
- consequential decisions affecting rights, access, safety, employment, benefits, or eligibility; and
- irreversible external or production actions.

## Meaningful human review

```text
Expertise
  + Authority
  + Context
  + Evidence access
  + Time
  + Independence
  + Intervention rights
  = Meaningful human review
```

A person merely present in the workflow does not satisfy the gate.

## Iteration versus escalation

```text
Prompt problem     → targeted iteration
Evidence problem   → obtain evidence
Tool problem       → repair workflow
Authority problem  → escalate
Judgment problem   → qualified human review
```

Stop prompting when improvement has plateaued or the remaining gap requires unavailable evidence, authority, expertise, or accountable professional judgment.

## Accountability

```text
Model assists
      ↓
Human validates and approves
      ↓
Organization releases and owns the consequences
```

AI origin does not transfer accountability away from the releasing human or organization.

---

# Four durable capabilities

## 1. Discernment

Evaluate what the output says, what it contradicts, and what it leaves out.

```text
Define purpose and stakes
          ↓
Check requirements and coverage
          ↓
Inventory material claims and actions
          ↓
Check source support and professional standards
          ↓
Review accuracy and completeness
          ↓
Scan failure signatures
          ↓
Compare repeated facts
          ↓
Challenge favored conclusions
          ↓
Confirm external actions
          ↓
Assign and document a disposition
```

## 2. Grounding

Trace material claims to evidence.

```text
Claim
  ↓
Source
  ↓
Exact support
  ↓
Scope, date, and conditions
  ↓
Supported, qualified, unsupported, conflicting, or not covered
```

## 3. Diligence

Match review depth to consequence and ensure required human ownership.

```text
Low consequence      → proportionate review
Material consequence → stronger validation
High consequence     → qualified human review is non-negotiable
```

## 4. Adaptation and triage

A factually sound output may still be unusable because of audience, framing, format, uncertainty, or authority.

```text
Release
Edit
Verify
Escalate
Reject
```

---

# Learning objectives

By the end of this module, you should be able to:

- distinguish fluent output from verified output;
- assess accuracy and completeness against an explicit purpose;
- evaluate requirements, source material, and professional standards;
- detect hallucinations, contradictions, omissions, and biased framing;
- calibrate certainty to evidence strength;
- verify source and requirement coverage;
- verify claimed external actions using tool and system records;
- permit explicit uncertainty when evidence is insufficient;
- distinguish closed-source analysis from open research;
- require precise, auditable claim-to-source locations;
- use quote-first analysis for consequential sources;
- distinguish citation presence from semantic support;
- use repeated runs to identify instability without treating agreement as proof;
- validate material claims against authoritative sources;
- recompute material calculations deterministically;
- assess stakes, reversibility, audience, and regulatory exposure;
- identify automatic do-not-ship review gates;
- distinguish meaningful human review from ceremonial approval;
- decide when iteration has reached diminishing returns;
- place approval before irreversible actions;
- preserve accountability with the releasing human or organization;
- adapt accurate content for different audiences without changing meaning;
- choose formats that make outputs easier to inspect and use;
- triage outputs into release, edit, verify, escalate, or reject;
- construct representative evaluation sets; and
- justify code-based, human, and model-assisted grading methods.

---

# Current module resources

## Lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Discernment: Accuracy and Completeness](lessons/02-discernment-accuracy-completeness.md)
- [Hallucinations, Inconsistencies, and Bias](lessons/03-hallucinations-inconsistencies-bias.md)
- [Fact-Checking and Grounding Techniques](lessons/04-fact-checking-grounding.md)
- [Diligence: When Human Review Is Non-Negotiable](lessons/05-diligence-human-review.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-03/01-module-introduction-prompts.md)
- [Accuracy and Completeness prompts](../../prompts/module-03/02-discernment-accuracy-completeness-prompts.md)
- [Failure Patterns prompts](../../prompts/module-03/03-hallucinations-inconsistencies-bias-prompts.md)
- [Fact-Checking and Grounding prompts](../../prompts/module-03/04-fact-checking-grounding-prompts.md)
- [Diligence and Human Review prompts](../../prompts/module-03/05-diligence-human-review-prompts.md)

## Engineering patterns

- [Three-Reference Discernment Pattern](../../patterns/three-reference-discernment-pattern.md)
- [Failure Signature Review Pattern](../../patterns/failure-signature-review-pattern.md)
- [Grounded Verification Pattern](../../patterns/grounded-verification-pattern.md)
- [Human Review Gate Pattern](../../patterns/human-review-gate-pattern.md)

## Existing module files

- [notes.md](notes.md): Exam-focused evaluation concepts and decision rules
- [lab.md](lab.md): Applied evaluation exercise with acceptance criteria
- [flashcards.md](flashcards.md): Baseline active-recall cards
- [quiz.md](quiz.md): Extended original scenario quiz

---

# Exam shortcuts

## Accuracy and completeness

```text
Requirements           → Did it do all requested work?
Source material        → Does evidence support each material claim?
Professional standards → Is the result fit for real use?
Accuracy               → Is what is present correct?
Completeness           → Is anything material missing?
Stakes                 → How much review is required?
```

## Failure patterns

```text
Precise number with no source        → fabricated-specific risk
Citation exists but mismatches       → claim-support failure
Absolute answer in conditional domain → certainty mismatch
Repeated fact has two values         → inconsistency
Prompt assumes conclusion            → confirmation-bias risk
Required file absent                 → completeness failure
Action claimed without receipt       → capability hallucination
```

## Fact-checking and grounding

```text
Evidence is silent         → permit unknown or not covered
Fixed document set         → restrict sources
Long or consequential text → quote first
Material claim             → precise citation
Citation present           → inspect actual support
Runs disagree              → investigate instability
Runs agree                 → still verify material claims
Calculation matters        → recompute deterministically
High-stakes conclusion     → authoritative source + qualified review
```

## Diligence and review gates

```text
Low-stakes internal draft         → proportionate review
Final client deliverable          → qualified review
Audit-critical calculation        → deterministic verification + finance review
Regulated or sensitive content    → policy controls + authorized review
Public or legal communication     → qualified review before release
Iteration improvement has stalled → fresh human judgment
Irreversible action               → approval gate before execution
```

Do not confuse precision, confidence, repetition, citations, agreement, human presence, or polished appearance with proof or approval.

---

# Exam lens

For scenario questions:

1. identify the property that needs evaluation;
2. determine purpose, stakes, reversibility, audience, and governing obligations;
3. define the evidence boundary and authority hierarchy;
4. permit explicit unknowns when evidence is silent;
5. check requirements, sources, professional standards, and coverage;
6. distinguish accuracy, completeness, consistency, bias, audience fit, and format;
7. inspect whether citations support the full claim;
8. use deterministic checks for exact values and calculations;
9. identify automatic human-review gates;
10. ensure the reviewer has expertise, authority, evidence, time, and intervention rights;
11. place review before irreversible action;
12. stop iterating when evidence, authority, or judgment is the real blocker; and
13. choose release, edit, verify, escalate, or reject.

---

# Completion criteria

- [x] I completed the Module 3 introduction.
- [x] I completed the Accuracy and Completeness lesson.
- [x] I completed the Hallucinations, Inconsistencies, and Bias lesson.
- [x] I completed the Fact-Checking and Grounding lesson.
- [x] I completed the Diligence and Human Review lesson.
- [ ] I can explain the accountability asymmetry and verification debt.
- [ ] I can apply the three evaluation references.
- [ ] I can review accuracy and completeness separately.
- [ ] I can identify hallucinations, contradictions, omissions, and biased framing.
- [ ] I can build a claim-evidence ledger and consistency matrix.
- [ ] I can verify source and requirement coverage.
- [ ] I can distinguish citation presence from actual support.
- [ ] I can use repeated runs as an instability detector rather than proof.
- [ ] I can validate material claims and calculations independently.
- [ ] I can apply the four Diligence thresholds.
- [ ] I can identify automatic do-not-ship categories.
- [ ] I can define meaningful human-review qualifications.
- [ ] I can determine when iteration should stop and escalation begin.
- [ ] I can place a review gate before an irreversible action.
- [ ] I can preserve human and organizational accountability.
- [ ] I can adapt output for an audience without distorting meaning.
- [ ] I can choose a format that supports inspection and use.
- [ ] I can triage an output into release, edit, verify, escalate, or reject.
- [ ] I completed the preparation-course exercise, quiz, and takeaways.
- [ ] I completed the repository evaluation lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not contribute confidential data, proprietary work products, credentials, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource and does not constitute legal, financial, medical, compliance, or other professional advice. Product behavior, interfaces, policies, and documentation can change. Current authoritative terms, policies, documentation, and organizational requirements control when conflicts exist.

## Official reading

Verify current official guidance before relying on implementation-specific details.

- [AI Fluency Framework overview](https://www.anthropic.com/ai-fluency/overview)
- [AI Fluency: Discernment](https://www.anthropic.com/ai-fluency/discernment)
- [AI Fluency: Diligence](https://www.anthropic.com/ai-fluency/due-dilligence)
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
