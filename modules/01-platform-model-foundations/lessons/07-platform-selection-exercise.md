# Lesson 7: Platform Selection Exercise

## Overview

This exercise combines the four major selection decisions from Module 1:

1. **Entry point:** Where should the work begin?
2. **Capability layer:** Which features are required?
3. **Model tier:** What capability, speed, and usage trade-off fits the task?
4. **Context strategy:** What should remain active, persist, or transfer between sessions?

The purpose is not to select the largest number of features. The goal is to choose the **least complex configuration that satisfies the task's recurrence, evidence, computation, output, quality, and review requirements**.

> [!IMPORTANT]
> A good answer identifies the signals in the scenario, not merely the configuration letter.

## Learning objectives

After completing this exercise, you should be able to:

- combine entry-point, capability, model, and context decisions;
- recognize when current information requires Research;
- recognize recurring work that belongs in a Project;
- identify numerical work that requires Code Execution;
- distinguish one-off drafting from persistent workflows;
- justify Opus for ambiguous, high-consequence synthesis;
- explain when Sonnet is sufficient;
- identify why Haiku may be appropriate for a structured computational subtask;
- distinguish the output surface from the workflow's capability layers; and
- defend a configuration using an explicit benefit-versus-cost trade-off.

## The configuration cards

Use each configuration once.

| Card | Configuration | Best-fit signal |
|---|---|---|
| A | Project + Skill, Sonnet | Recurring structured work with stable context and a repeatable output procedure |
| B | Research, Sonnet | Current multi-source information requiring investigation and synthesis |
| C | Code Execution, Haiku or Sonnet | Defined dataset, explicit calculation, accuracy and reproducibility required |
| D | Project knowledge + Artifact, Opus | Nuanced multi-source interpretation and a high-consequence deliverable |
| E | Chat + Artifact, Sonnet | One-off professional drafting with no persistence requirement |
| F | Project + Code Execution + Skill, Sonnet | Recurring analytical workflow with verified figures and a consistent report format |

### What the cards test

| Decision dimension | Questions to ask |
|---|---|
| Entry point | Is the task one-off, recurring, deliverable-oriented, or research-intensive? |
| Capability layer | Does it need stable context, a repeatable procedure, executed calculation, or continuity? |
| Model | Is the task structured, balanced, or highly ambiguous and quality-sensitive? |
| Context | Which information is stable, cycle-specific, current, or authoritative? |
| Review | What must be validated, approved, or escalated? |

## Part 1: Match each scenario

Try the exercise before opening the answer key.

### Scenario 1: Recent competitor activity

A product-planning lead needs a briefing on competitors that announced or launched new products during the previous 90 days. The findings will inform an upcoming planning workshop.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

### Scenario 2: Weekly meeting notes

A coordinator prepares meeting notes every week for six months. The team, terminology, agenda structure, and required note format remain stable.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

### Scenario 3: Board-level strategic analysis

A consultant must produce a 15-page analysis for a board. Four uploaded reports contain ambiguous and sometimes conflicting signals that require nuanced interpretation.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

### Scenario 4: Survey response-rate calculation

An analyst has 800 survey records and must calculate response rates by department, then flag every department below 60 percent completion.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

### Scenario 5: Monthly variance analysis

A finance team performs the same analysis every month. Current actuals are compared with budget, variances above 10 percent are flagged, and the results are placed into an approved report template.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

### Scenario 6: One-time vendor response

A procurement professional needs a quick, polished response to a vendor's question about payment terms. The relevant policy and vendor email are available, and the task is not expected to recur.

Choose one:

- Card A
- Card B
- Card C
- Card D
- Card E
- Card F

---

## Part 1 answer key

```text
S1 -> B
S2 -> A
S3 -> D
S4 -> C
S5 -> F
S6 -> E
```

## Scenario 1 answer: Card B

**Configuration:** Research, Sonnet

### Signals

- The question concerns the previous 90 days.
- The answer depends on current information.
- Multiple competitors and sources may need to be investigated.
- The output is a professional synthesis, but the task does not inherently require the highest reasoning tier.

### Why Research

The relevant facts post-date reliable pretrained recall. Research is appropriate because the task requires discovery and synthesis across several current sources, not merely analysis of a fixed uploaded dataset.

### Why Sonnet

Sonnet is a reasonable starting point for current-information research synthesis. It provides strong professional analysis without automatically spending the higher latency or usage of Opus.

### Why the other cards are weaker

- **A:** The task is not described as recurring.
- **C:** The primary challenge is current investigation, not calculation.
- **D:** The task is not described as deeply ambiguous or board-critical enough to require Opus.
- **E:** Chat alone lacks the deeper current-source investigation implied by the scenario.
- **F:** No recurring analytical process or verified calculation is described.

## Scenario 2 answer: Card A

**Configuration:** Project + Skill, Sonnet

### Signals

- The work recurs weekly.
- The background and terminology remain stable.
- The format is fixed.
- The task is professional but not unusually ambiguous.

### Layer placement

- **Project:** team context, terminology, standing instructions, approved examples.
- **Skill:** the repeated process for structuring and formatting the notes.
- **Sonnet:** balanced professional drafting and synthesis.

### Context strategy

The current meeting discussion belongs in the weekly conversation. Stable instructions and reference material belong in the Project. Decisions that must carry forward should be recorded deliberately.

## Scenario 3 answer: Card D

**Configuration:** Project knowledge + Artifact, Opus

### Signals

- Four reports must be interpreted together.
- The evidence is ambiguous and potentially conflicting.
- The output is long, polished, and board-facing.
- The cost of weak synthesis or missed nuance is high.

### Why Project knowledge

The uploaded reports form a curated evidence set for the analysis. Project instructions can define source handling, uncertainty labeling, audience, structure, and review expectations.

### Why Artifact

A 15-page board analysis is a deliverable with a document lifecycle. It should exist as a separate editable work product rather than remain trapped inside conversational prose.

### Why Opus

Opus raises the reasoning quality ceiling for ambiguous, multi-source, high-consequence interpretation.

### Trade-off

Opus buys greater reasoning depth and nuance at the cost of slower responses and greater usage or API expense.

### Important control

Opus does not replace source verification, Artifact review, or accountable human approval.

## Scenario 4 answer: Card C

**Configuration:** Code Execution, Haiku or Sonnet

### Signals

- The task uses a defined dataset.
- The required outputs are numerical.
- The threshold is explicit.
- The result must be accurate and reproducible.

### Why Code Execution

The response-rate calculations should be executed, not generated through prose. The workflow should record:

- total records;
- valid responses;
- department groupings;
- missing-value handling;
- formula used;
- response rate by department; and
- departments below the threshold.

### Why Haiku or Sonnet

The calculation is structured. Haiku may be sufficient for orchestration and explanation when the workflow is clear. Sonnet may be preferable when the data requires more interpretation, cleaning decisions, or a more polished analysis.

### Validation

Code Execution still requires validation of input completeness, department mapping, formula choice, and missing-value treatment.

## Scenario 5 answer: Card F

**Configuration:** Project + Code Execution + Skill, Sonnet

### Signals

- The workflow recurs monthly.
- Budget definitions and report structure remain stable.
- Calculations must be accurate.
- The output format is consistent.

### Layer placement

| Requirement | Correct home |
|---|---|
| Budget definitions and standing rules | Project instructions or Project knowledge |
| Prior approved examples | Project knowledge, when current and authorized |
| Monthly analysis procedure | Skill |
| Variance calculation and reconciliation | Code Execution |
| Current actuals and budget file | Current-cycle input |
| Professional narrative and explanation | Sonnet |
| Final approval | Qualified human review |

### Why this is not Card A

Card A lacks Code Execution. A monthly report containing real financial calculations should not rely on language generation alone.

## Scenario 6 answer: Card E

**Configuration:** Chat + Artifact, Sonnet

### Signals

- The task is one-off.
- The source documents are already available.
- A polished response is needed.
- No stable recurring workstream or reusable procedure is described.

### Why Chat

The task begins and ends in one interaction. Building a Project or Skill would add unnecessary setup and maintenance.

### Why Artifact

The response is a deliverable that may need editing, approval, or direct handoff.

### Why Sonnet

Sonnet is the normal starting point for professional drafting using a small, clear source set.

## Part 2: Defend the model choice

### Scenario

A board analysis must synthesize four reports containing ambiguous and conflicting signals.

Write one sentence that identifies:

1. the model;
2. what the choice buys; and
3. what the choice costs.

### Strong answer

> I would choose Opus because the analysis requires nuanced interpretation across conflicting sources and the quality ceiling matters more than turnaround, accepting slower response and greater usage in exchange for deeper reasoning.

### Why this answer works

It does more than name a tier. It identifies:

- the task characteristic: ambiguity and multi-source interpretation;
- the benefit: deeper reasoning and higher quality ceiling;
- the cost: speed and usage; and
- the priority: quality over turnaround.

### Your answer

The answer supplied during the course exercise was substantively correct:

> I chose Opus because the task requires nuanced, multi-source interpretation for a high-stakes consultant deliverable, accepting slower output in exchange for higher reasoning quality.

The strongest revision is to describe the trade-off directly rather than say it only "might" be slower.

## Model-justification rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---:|---:|---:|
| Correct tier | Wrong | Plausible but weak | Best-supported choice |
| Task signal | Missing | General | Specific ambiguity, volume, or consequence signal |
| Benefit | Missing | Vague | Explicit quality, speed, or efficiency benefit |
| Cost | Missing | Vague | Explicit latency, usage, or quality trade-off |
| Alternatives | Missing | Partial | Explains when another tier would be appropriate |

**Readiness target:** 8 out of 10 or higher.

## Combined selection framework

Use this sequence for new scenarios.

```text
1. What kind of work is this?
       |
       +-- One-off conversation ----------> Chat
       +-- Recurring workstream ----------> Project
       +-- Separate deliverable ----------> Artifact
       +-- Current multi-source research -> Research

2. What extra capability is required?
       |
       +-- Repeatable procedure ----------> Skill
       +-- Calculation or real file ------> Code Execution
       +-- Cross-session continuity ------> Memory

3. What model tier fits?
       |
       +-- Structured and high volume ----> Haiku
       +-- General professional work -----> Sonnet
       +-- Ambiguous and quality-critical -> Opus

4. What context strategy is needed?
       |
       +-- Current detail ----------------> Conversation
       +-- Stable rule -------------------> Project instructions
       +-- Reusable evidence -------------> Project knowledge
       +-- Durable preference ------------> Memory
       +-- Traceable truth ---------------> Authoritative record
```

## Common mistakes

### Selecting based on the job title

A consultant does not automatically require Opus. The task's ambiguity, consequence, and reasoning demand determine the tier.

### Selecting Research for every current fact

A quick lookup may use web search in Chat. Research is justified when the task requires deeper, multi-step source discovery and synthesis.

### Forgetting Code Execution

Any real-data calculation used or reported should trigger the question: can this be executed and reconciled?

### Treating Artifact as a model capability

Artifact defines the deliverable surface. It does not replace Project context, Skills, Code Execution, or model selection.

### Overbuilding one-off work

A one-time professional response may need Chat, Sonnet, and an Artifact, but no Project or Skill.

### Using Opus without stating the cost

A strong justification acknowledges the latency and usage trade-off.

### Ignoring context strategy

Even a correct feature and model choice can fail if stable context, current input, and authoritative truth are mixed together.

## Additional practice scenarios

### Practice 1

A support operation processes 40,000 standardized tickets each month, extracts three fields, validates a fixed schema, and sends uncertain cases to a specialist.

**Recommended starting architecture:** Haiku for the structured first pass, deterministic validation, and escalation to Sonnet or human review.

### Practice 2

A policy team maintains a recurring briefing based on an approved source set, but every quarter it must add current public developments and publish a formatted report.

**Recommended architecture:** Project for stable knowledge and instructions, Research for current evidence, Sonnet for synthesis, and Artifact for the deliverable.

### Practice 3

A one-time spreadsheet contains 300 rows that must be deduplicated, normalized, and exported as a new workbook.

**Recommended architecture:** Chat with Code Execution, using Haiku or Sonnet depending on transformation complexity. No Project is required.

### Practice 4

A recurring risk review uses stable scoring criteria, an approved report format, and a complex exposure model.

**Recommended architecture:** Project + Skill + Code Execution, with Sonnet as the professional default and Opus escalation for ambiguous high-risk cases.

### Practice 5

A leader wants three creative names for an internal workshop.

**Recommended architecture:** Chat, using a fast available model. No persistent capability layer is required.

### Practice 6

A board must choose among three long-term strategies using incomplete evidence, competing stakeholder goals, and irreversible investment decisions.

**Recommended architecture:** Project knowledge + Artifact, test Opus, preserve uncertainty analysis, and require accountable human decision-making.

## Knowledge check

### Question 1

A recurring workflow uses the same context and template but contains no calculations. Which configuration is the best starting point?

A. Research + Opus  
B. Project + Skill, Sonnet  
C. Chat + Artifact, Haiku  
D. Code Execution, Sonnet

**Answer:** B

### Question 2

Which signal most strongly points to Code Execution?

A. The output is client-facing  
B. The task is recurring  
C. A real dataset must be calculated and thresholded  
D. The source material is ambiguous

**Answer:** C

### Question 3

Why is Sonnet appropriate for the competitor-research scenario?

A. Sonnet automatically has current information  
B. Sonnet is the balanced tier for professional synthesis after current sources are gathered  
C. Sonnet eliminates the need for Research  
D. Sonnet guarantees every competitor is found

**Answer:** B

### Question 4

What does Opus buy in the board-analysis scenario?

A. Guaranteed correctness  
B. Free unlimited usage  
C. A higher reasoning-quality ceiling for ambiguous multi-source interpretation  
D. Automatic approval by the board

**Answer:** C

### Question 5

Which item belongs in the current conversation rather than Project knowledge?

A. Stable report terminology  
B. Approved reference playbook  
C. This month's actuals file  
D. Standing escalation threshold

**Answer:** C

### Question 6

Why is Card E better than Card A for the vendor response?

A. Artifacts cannot be used in Projects  
B. The task is one-off, so Project and Skill setup would add unnecessary overhead  
C. Sonnet cannot operate in a Project  
D. Vendor communication never requires evidence

**Answer:** B

## Flashcards

**Q:** What four decisions are combined in platform selection?  
**A:** Entry point, capability layer, model tier, and context strategy.

**Q:** Which configuration fits recurring structured work with a fixed format but no calculations?  
**A:** Project + Skill, usually starting with Sonnet.

**Q:** Which feature is required for calculations on a real dataset?  
**A:** Code Execution, followed by method and output validation.

**Q:** Which model is the certification default for most professional work?  
**A:** Sonnet.

**Q:** When is Opus justified?  
**A:** Complex, ambiguous, multi-layered, quality-sensitive work where reasoning capability is the bottleneck.

**Q:** What makes Research different from normal Chat?  
**A:** Research performs deeper multi-step investigation and synthesis across current sources.

**Q:** Why might a one-off response still use an Artifact?  
**A:** Because the output is an editable deliverable even though the workflow does not require persistence.

**Q:** What should a model justification include?  
**A:** The selected model, task signal, benefit gained, and cost accepted.

## Certification lens

The exercise tests integrated judgment. Do not solve it by looking at only one keyword.

For every scenario, identify:

1. **recurrence:** one-off or repeated;
2. **information:** current, uploaded, reusable, or authoritative;
3. **procedure:** ad hoc or standardized;
4. **computation:** generated prose or executed operation;
5. **output:** conversational answer or deliverable;
6. **reasoning:** structured, balanced, or ambiguous;
7. **consequence:** low, moderate, or high; and
8. **context:** active, persistent, summarized, or external.

## Completion checklist

- [ ] I matched all six scenarios correctly.
- [ ] I explained why S1 requires current-source investigation.
- [ ] I explained why S2 benefits from a Project and Skill.
- [ ] I defended Opus for S3 using an explicit benefit and cost.
- [ ] I explained why S4 and S5 require Code Execution.
- [ ] I explained why S6 should remain a one-off workflow.
- [ ] I identified the context strategy for each scenario.
- [ ] I can create a new scenario and defend all four decisions.

## Related material

- [Core Entry Points](03-core-entry-points.md)
- [Capability Layer](04-capability-layer-skills-code-execution.md)
- [Choosing Models](05-choosing-models.md)
- [Context Management](06-context-management.md)
- [Platform Selection prompt notebook](../../../prompts/module-01/07-platform-selection-exercise-prompts.md)

## Content note

This is an independent, expanded exercise built from general platform-selection concepts. It does not reproduce a proprietary interactive exercise or live certification questions.