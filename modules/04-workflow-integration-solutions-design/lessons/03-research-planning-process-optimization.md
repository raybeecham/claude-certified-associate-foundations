# Lesson 3: Research, Planning, and Process Optimization

## Overview

Planning work often combines three different kinds of responsibility:

1. **Research and synthesis** — gathering current evidence, organizing considerations, comparing options, and explaining trade-offs.
2. **Computation and analysis** — calculating trends, rates, forecasts, scenarios, and resource requirements from actual data.
3. **Human judgment** — deciding how much risk to accept, which trade-off is politically or operationally realistic, and whether the organization should act.

Claude can contribute strongly to the first two categories, but the workflow must use different controls for each.

```text
Research evidence
      +
Executed analysis
      +
Human constraints and judgment
      ↓
Defensible plan
```

> A plan is only as trustworthy as the evidence, calculations, assumptions, and decision authority beneath it.

This lesson develops five capabilities:

- selecting web search, deeper research, source files, or internal evidence for the research stage;
- separating synthesis from exact calculation;
- using code execution for trend analysis, forecasting inputs, charts, and processed files;
- identifying which workflow stages benefit from Claude and which decisions remain human; and
- improving a current process by targeting bottlenecks rather than automating every step.

---

# Plain-English explanation

A planning request might sound simple:

```text
How many people will we need next quarter?
```

But the answer may depend on:

- historical workload;
- growth rate;
- worker throughput;
- seasonality;
- service targets;
- planned leave;
- backlog;
- hiring lead time;
- budget limits;
- policy constraints; and
- leadership risk tolerance.

Claude can help organize these considerations and calculate values from supplied data. It cannot independently know every budget freeze, political concern, labor constraint, or unrecorded organizational priority.

A reliable workflow therefore separates:

```text
What the evidence shows
      ↓
What the calculations produce
      ↓
What assumptions connect the numbers to a forecast
      ↓
What decision an authorized person makes
```

---

# One analogy: planning a road trip

A trip plan requires several kinds of work.

- **Research** identifies roads, closures, weather, lodging, and fuel availability.
- **Calculation** determines distance, travel time, fuel consumption, and cost.
- **Judgment** decides whether the travelers accept the weather risk, prefer a scenic route, or postpone the trip.

A travel guide can summarize options. A calculator can compute mileage. Neither should decide the travelers' risk tolerance without their input.

Workflow planning follows the same pattern:

```text
Current information → research tools and verified sources
Exact numbers       → code execution or deterministic analysis
Risk and priorities → human owner
```

> Use Claude to make the decision better informed, not to erase the decision-maker.

---

# Research and synthesis

Claude is useful when a planner must combine many sources and considerations into a coherent decision structure.

Research tasks may include:

- identifying current practices or market conditions;
- summarizing policies, standards, or public guidance;
- comparing options;
- identifying risks and dependencies;
- organizing stakeholder considerations;
- extracting planning assumptions;
- building scenario narratives; and
- drafting a recommendation based on verified evidence.

## Select the research path by depth

| Need | Appropriate path |
|---|---|
| One or two current facts | Web search |
| Multi-source, deeper investigation | Research |
| Analysis of supplied documents | Closed-source document analysis |
| Internal operational truth | Approved internal systems and records |
| Exact values from uploaded data | Code execution |

Current official Claude guidance describes web search as suitable for straightforward current factual queries and Research as a deeper approach for more comprehensive investigation. Product availability and behavior can change.

## Research output should remain auditable

For each material finding, preserve:

- source;
- date;
- scope;
- relevant passage or data point;
- uncertainty;
- conflicts with other sources; and
- how the finding affects the plan.

```text
Research summary
      ≠
Verified planning assumption
```

A research finding becomes a planning assumption only after its authority, currency, scope, and applicability are reviewed.

---

# Synthesis is not calculation

Claude can describe a numerical method correctly while generating an incorrect result.

Examples of planning values that should be executed rather than produced as prose include:

- workload growth;
- utilization;
- throughput;
- average handling time;
- backlog burn rate;
- required headcount;
- cost totals;
- budget variance;
- capacity by time period;
- scenario ranges;
- confidence intervals; and
- chart values.

```text
Plausible number in prose
      ≠
Computed result
```

Use code execution or another deterministic system when the plan depends materially on the number.

---

# Code execution for verified analysis

Code execution can:

- inspect uploaded datasets;
- filter and transform records;
- calculate trends and ratios;
- aggregate by time period, team, or category;
- create visualizations;
- process files;
- generate structured output; and
- preserve reusable calculation logic.

Current Anthropic documentation describes the code execution tool as a sandboxed environment for Python and Bash code, data analysis, calculations, visualizations, and file processing.

## What execution establishes

Code execution adds:

- an explicit method;
- a repeatable calculation;
- visible inputs and parameters;
- inspectable intermediate results; and
- the ability to rerun the analysis.

## What execution does not establish

The code may still use:

- the wrong date field;
- an incorrect filter;
- a mistaken business rule;
- an invalid denominator;
- duplicate records;
- incomplete data;
- the wrong unit;
- an inappropriate forecasting method; or
- an unsupported assumption.

Therefore:

```text
Code executed
      ≠
Logic correct
      ≠
Data complete
      ≠
Forecast valid
      ≠
Decision approved
```

## Analysis verification chain

```text
Inspect data and schema
      ↓
Define business rules and assumptions
      ↓
Review calculation logic
      ↓
Execute
      ↓
Inspect intermediate and final results
      ↓
Reconcile with control totals or an independent method
      ↓
Use results in the planning synthesis
      ↓
Apply qualified human judgment and approval
```

---

# Worked example: a capacity plan

## Business question

An operations lead must estimate next-quarter staffing while maintaining the current resolution-time target.

## Input package

The fictional planning package contains:

- four quarters of ticket data;
- ticket status and close dates;
- analyst identifiers;
- analyst availability by quarter;
- backlog counts;
- service-level targets;
- approved leave assumptions; and
- known hiring constraints.

## Workflow

```text
Curate the data
      ↓
Execute historical analysis
      ↓
Calculate workload growth and throughput
      ↓
Build transparent scenarios
      ↓
Claude synthesizes recommendation and trade-offs
      ↓
Operations lead weighs budget and hiring realities
      ↓
Authorized staffing decision
```

## Analysis prompt

```text
Using code execution on the attached ticket and staffing data:

1. inspect the schema and report missing or ambiguous fields;
2. define the quarter boundaries and inclusion rules;
3. calculate ticket volume by quarter;
4. calculate quarter-over-quarter growth;
5. calculate tickets resolved per available analyst;
6. report backlog and resolution-time trends;
7. estimate next-quarter staffing under baseline, conservative, and stress scenarios;
8. show every assumption and formula;
9. produce a result table and charts from the computed data; and
10. identify which decisions still require management judgment.

Do not invent a business rule or missing value. Mark unresolved items as assumptions or blockers.
```

## Example formulas

A simplified throughput measure might be:

```text
Quarterly throughput per analyst
=
Resolved tickets
÷
Average available analysts
```

A simplified staffing estimate might be:

```text
Required analysts
=
Forecast ticket volume
÷
Expected tickets resolved per analyst
```

Real planning may also require:

- productivity ramp for new hires;
- planned absence;
- case complexity;
- service-level buffers;
- backlog reduction target;
- attrition;
- seasonality; and
- confidence ranges.

## Illustrative computed evidence

| Measure | Q1 | Q2 | Q3 | Q4 |
|---|---:|---:|---:|---:|
| Ticket volume | 18,400 | 19,150 | 20,600 | 21,900 |
| Resolved tickets | 18,050 | 18,900 | 20,100 | 21,300 |
| Available analysts | 24.0 | 24.5 | 25.0 | 25.0 |
| Resolved per analyst | 752 | 771 | 804 | 852 |

These values are fictional and illustrate the method only.

## Planning synthesis

Claude may then summarize:

- historical growth;
- productivity trend;
- baseline forecast;
- range of staffing scenarios;
- backlog risk;
- sensitivity to throughput assumptions;
- operational dependencies; and
- actions that preserve options.

## Human-retained decision

The operations lead must still weigh:

- approved budget;
- hiring freeze;
- overtime tolerance;
- service-risk appetite;
- labor-market conditions;
- internal transfers;
- planned technology changes; and
- political or leadership priorities unavailable to Claude.

```text
Claude supports the staffing recommendation
      ≠
Claude authorizes hiring
```

---

# Where AI insight changes the plan

Not every workflow stage benefits equally from Claude.

## High-leverage AI stages

Claude often adds value where the work requires:

- synthesizing many sources;
- identifying themes and dependencies;
- organizing alternatives;
- translating analysis into scenarios;
- explaining trade-offs;
- drafting options;
- identifying missing considerations; and
- communicating a plan to different audiences.

## Deterministic stages

Use code or fixed logic for:

- calculations;
- date boundaries;
- filtering;
- aggregation;
- business-rule enforcement;
- schema validation;
- authorization checks; and
- reproducible chart data.

## Human-retained stages

Retain people for:

- risk appetite;
- political reality;
- professional judgment;
- acceptance of uncertainty;
- prioritization among legitimate values;
- budget approval;
- commitments to stakeholders; and
- consequential decisions.

## Planning-stage map

| Stage | Best owner | Reason |
|---|---|---|
| Gather current public evidence | Web search or Research, with human review | Current-source retrieval and synthesis |
| Analyze internal dataset | Code execution or deterministic analytics | Exact, reproducible calculation |
| Generate scenarios | Collaborative | Model organizes options; human validates assumptions |
| Evaluate political feasibility | Human | Context and accountability are not fully captured in data |
| Approve budget or hiring | Human authority | Consequential organizational decision |
| Publish approved plan | Controlled workflow | Version, disclosure, review, and release controls |

---

# Process optimization

Planning should improve the workflow, not merely produce a document.

## Current-state process review

Map:

- trigger;
- inputs;
- actors;
- stages;
- handoffs;
- waiting time;
- rework;
- calculations;
- decisions;
- approvals;
- systems of record;
- outputs;
- exceptions; and
- failure paths.

## Bottleneck categories

| Bottleneck | Example |
|---|---|
| Information retrieval | Analysts repeatedly search for the same approved source |
| Manual synthesis | Staff combine many documents into similar summaries |
| Repeated calculation | Teams rebuild the same spreadsheet logic each cycle |
| Waiting for clarification | Requirements lack owners or acceptance criteria |
| Handoff failure | Output arrives in the wrong format or without evidence |
| Review overload | Qualified reviewers spend time fixing preventable drafting issues |
| Uncontrolled variation | Each person follows a different process |
| Missing state | Work is restarted because prior decisions are not persisted |

## Optimization questions

Ask:

```text
Which stage creates the delay?
Which stage creates the defect?
Which stage requires synthesis?
Which stage requires exact computation?
Which stage requires authority?
Which steps can be standardized?
Which exceptions must stay human?
What evidence will show that the redesign improved the outcome?
```

## Do not optimize the wrong step

A faster summary is not useful if the source package is incomplete.

A faster calculation is not useful if the business rule is unresolved.

A fully automated recommendation is not useful if no authorized person can accept its risk.

```text
Automating a broken process
      =
Producing defects faster
```

---

# Planning workflow protocol

```text
1. Define the planning decision and success criteria
2. Map evidence, data, constraints, and decision owners
3. Select current-source research path
4. Curate internal and external inputs
5. Separate synthesis questions from calculation questions
6. Execute material calculations with visible assumptions
7. Reconcile and validate the results
8. Generate scenarios and trade-offs
9. Identify where AI insight materially affects the plan
10. Retain human judgment for risk, feasibility, and approval
11. Document assumptions, limitations, and sensitivity
12. Measure the resulting workflow and business outcome
```

---

# Planning evidence table

| Claim or planning input | Type | Source or method | Verified? | Assumption | Sensitivity | Decision impact |
|---|---|---|---|---|---|---|
| Ticket growth | Computed | Executed dataset analysis | Yes/No | Quarter definition | Medium | Headcount forecast |
| Hiring lead time | Internal fact | Approved HR data | Yes/No | None | High | Start date |
| Productivity ramp | Assumption | Historical cohorts | Yes/No | Training duration | High | First-quarter capacity |
| Budget ceiling | Human constraint | Approved budget | Yes/No | None | High | Feasible scenario |
| Market availability | Research finding | Current labor data | Yes/No | Local comparability | Medium | Hiring risk |

The table makes clear which parts of the recommendation are facts, computations, assumptions, and human constraints.

---

# Common anti-patterns

## Anti-pattern 1: Research without source discipline

**Failure:** A polished synthesis contains stale, weak, or unverifiable claims.

**Repair:** Preserve citations, dates, scope, conflicts, and source hierarchy.

## Anti-pattern 2: Prose-generated planning numbers

**Failure:** The recommendation depends on a figure that was never actually calculated.

**Repair:** Execute the analysis and retain the method.

## Anti-pattern 3: Code-execution overconfidence

**Failure:** Successful execution is treated as proof of valid logic and complete data.

**Repair:** Review business rules, inputs, intermediate outputs, and reconciliation.

## Anti-pattern 4: Hidden assumptions

**Failure:** A forecast appears precise while its productivity, seasonality, or availability assumptions are invisible.

**Repair:** Create an assumption register and sensitivity analysis.

## Anti-pattern 5: Claude makes the organizational decision

**Failure:** A synthesized recommendation becomes an approved hiring, budget, policy, or risk decision without authorized ownership.

**Repair:** Keep consequential judgment and approval human-retained.

## Anti-pattern 6: AI everywhere

**Failure:** Claude is added to stages that already have reliable deterministic logic or require human authority.

**Repair:** Target synthesis-heavy and interpretation-heavy stages where bounded assistance adds value.

## Anti-pattern 7: Optimizing output instead of process

**Failure:** The report improves while bottlenecks, handoffs, missing state, and review burden remain unchanged.

**Repair:** Measure stage-level cycle time, defects, rework, and business outcomes.

---

# Exam reasoning pattern

For research, planning, and process-optimization scenarios:

1. define the planning decision;
2. distinguish current research, supplied evidence, calculation, synthesis, and human judgment;
3. use web search for straightforward current facts and Research for deeper multi-source investigation;
4. require source traceability and currency;
5. execute material calculations over actual data;
6. inspect business rules, data quality, and assumptions;
7. use Claude to structure scenarios and trade-offs;
8. retain human ownership of risk, feasibility, commitments, and approval;
9. identify which workflow stage actually creates the bottleneck or defect;
10. optimize the stage rather than automating the entire process; and
11. measure both workflow performance and business outcome.

```text
Current factual lookup      → web search
Deeper multi-source inquiry → Research
Exact trend or forecast     → code execution
Trade-off synthesis         → Claude + verified evidence
Risk appetite or approval   → human
Broken current process      → map before automating
```

---

# Knowledge check

## Question 1

Why should synthesis and calculation be separated?

**Answer:** They require different reliability controls. Synthesis organizes evidence and trade-offs; material calculations should be executed and reviewed.

## Question 2

When is web search more appropriate than Research?

**Answer:** For straightforward current facts or quick lookups that require only limited searching.

## Question 3

What does code execution add to a capacity plan?

**Answer:** An explicit, rerunnable analysis of actual workload and staffing data, including formulas, intermediate results, tables, and charts.

## Question 4

What remains unproven after code runs successfully?

**Answer:** Data completeness, business-rule correctness, assumption validity, forecast suitability, and release approval.

## Question 5

Why must assumptions be visible?

**Answer:** Forecasts can change materially when productivity, demand, availability, or policy assumptions change.

## Question 6

Where does Claude often add the most planning value?

**Answer:** In synthesizing many considerations, generating scenarios, organizing trade-offs, and explaining options.

## Question 7

Which planning decisions should remain human?

**Answer:** Decisions involving risk appetite, budget authority, political reality, commitments, and consequential organizational judgment.

## Question 8

Why map the current process before optimizing it?

**Answer:** Otherwise the team may automate an unnecessary, defective, or poorly controlled stage rather than fixing the real bottleneck.

---

# Flashcards

## Flashcard 1

**Q:** What are the three planning responsibility types?

**A:** Research and synthesis, deterministic computation, and human judgment.

## Flashcard 2

**Q:** What is the quick research-path rule?

**A:** Web search for straightforward current lookups; Research for deeper multi-source investigation.

## Flashcard 3

**Q:** What should calculate material planning numbers?

**A:** Code execution or another deterministic analytical system using actual data.

## Flashcard 4

**Q:** Does code execution guarantee a valid plan?

**A:** No. Logic, data, assumptions, interpretation, and approval still require validation.

## Flashcard 5

**Q:** Where is Claude strongest in planning?

**A:** Synthesis, scenario organization, trade-off explanation, and identifying considerations.

## Flashcard 6

**Q:** What must stay human-retained?

**A:** Risk appetite, feasibility judgment, authority, commitments, and consequential approval.

## Flashcard 7

**Q:** What is an assumption register?

**A:** A record of planning assumptions, owners, evidence, sensitivity, and resolution status.

## Flashcard 8

**Q:** What is the process-optimization rule?

**A:** Identify and improve the actual bottleneck or defect source instead of automating every stage.

---

# Short recap

```text
1. Define the planning decision.
2. Select the right research depth.
3. Keep sources, dates, and scope visible.
4. Separate synthesis from calculation.
5. Execute material numbers over actual data.
6. Review logic, data, and assumptions.
7. Use Claude to structure scenarios and trade-offs.
8. Retain human judgment and approval.
9. Map the current process before redesigning it.
10. Optimize the real bottleneck and measure the outcome.
```

> Use Claude to synthesize the plan, code to establish the numbers, and accountable people to make the decision.

## Educational-use notice

This repository is an unofficial educational resource. Examples are fictional, generic, synthetic, public, or explicitly authorized. The material does not constitute operational, workforce, financial, research, or other professional advice.

## Source and currency note

The preparation-course material supplied for this lesson was received on August 3, 2026. Product-specific statements were rechecked against official Anthropic sources on August 3, 2026.

Official references:

- [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)
- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)

## Related material

- [Analyzing Requirements and Use Cases](02-analyzing-requirements-use-cases.md)
- [Module 4 overview](../README.md)
- [Research, Planning, and Process Optimization prompts](../../../prompts/module-04/03-research-planning-process-optimization-prompts.md)
- [Verified Planning Workflow Pattern](../../../patterns/verified-planning-workflow-pattern.md)
- [Requirements Traceability and Pressure-Test Pattern](../../../patterns/requirements-traceability-pressure-test-pattern.md)
- [Output Format and Reliability Pattern](../../../patterns/output-format-reliability-pattern.md)
