# Verified Planning Workflow Pattern

## Purpose

Use this pattern when a plan depends on both qualitative synthesis and quantitative analysis.

> Use research to establish current evidence, code to establish material numbers, and accountable people to make the decision.

---

## Problem

Planning workflows often blur several different activities:

- gathering current information;
- synthesizing considerations;
- calculating trends or forecasts;
- making assumptions;
- weighing risk and feasibility; and
- authorizing action.

When these responsibilities are not separated, a plan may contain:

- stale research;
- unsupported claims;
- prose-generated numbers;
- hidden assumptions;
- deterministic code using the wrong rule;
- recommendations that exceed the evidence; or
- organizational decisions made without accountable authority.

---

## Core model

```text
Current evidence
      +
Executed quantitative analysis
      +
Visible assumptions and sensitivity
      +
Human constraints and judgment
      ↓
Defensible planning recommendation
      ↓
Authorized decision
```

---

## Responsibility split

| Responsibility | Best owner |
|---|---|
| Straightforward current lookup | Web search with source review |
| Deeper multi-source investigation | Research with source review |
| Internal operational facts | Approved internal systems |
| Exact calculation and transformation | Code execution or deterministic analytics |
| Scenario and trade-off synthesis | Claude with verified evidence |
| Risk appetite and feasibility | Human owner |
| Budget, policy, or staffing approval | Authorized human or governance body |
| External action | Controlled tool after approval |
| Durable planning state | System of record |

---

## Recommended workflow

```text
Define planning decision
      ↓
Map evidence, data, constraints, and owners
      ↓
Select research depth
      ↓
Curate inputs
      ↓
Separate synthesis from calculation
      ↓
Execute material analysis
      ↓
Reconcile and validate
      ↓
Build assumptions and scenarios
      ↓
Synthesize recommendation
      ↓
Human evaluates feasibility and risk
      ↓
Approve, revise, defer, or reject
      ↓
Monitor outcomes and update assumptions
```

---

## Step 1: Define the decision

Record:

- decision to be made;
- accountable owner;
- deadline;
- affected stakeholders;
- intended action;
- consequence of error;
- reversibility;
- required approvals; and
- success criteria.

A planning workflow should not begin with `research this topic` without identifying the decision the research must support.

---

## Step 2: Build the evidence map

Classify each planning input as:

- current public evidence;
- approved internal fact;
- computed metric;
- assumption;
- constraint;
- stakeholder preference;
- policy or authority boundary; or
- unresolved unknown.

For research findings, retain source, date, scope, support location, conflicts, and applicability.

---

## Step 3: Select the research path

```text
Quick current fact          → web search
Deep multi-source inquiry   → Research
Supplied-document question  → closed-source analysis
Internal operational truth  → approved system of record
Material numeric question   → code execution
Missing organizational fact → human clarification
```

Research depth should match the consequence and complexity of the decision.

---

## Step 4: Curate inputs

Before analysis:

- remove duplicates;
- identify authoritative versions;
- label raw, processed, approved, draft, and superseded inputs;
- check schema, units, dates, and identifiers;
- remove irrelevant material;
- restrict unauthorized sensitive content; and
- document missing evidence.

---

## Step 5: Separate synthesis from computation

Create a stage map:

| Stage | Type | Owner | Validation |
|---|---|---|---|
| Gather market data | Research | Search/Research + reviewer | Source authority and currency |
| Calculate growth | Computation | Code | Logic review and reconciliation |
| Build scenarios | Collaborative synthesis | Claude + planner | Assumption and sensitivity review |
| Set risk tolerance | Human judgment | Decision owner | Governance and approval |
| Execute approved action | Tool | Controlled system | Authorization and receipt |

---

## Step 6: Execute material calculations

For each material calculation, define:

- source file and version;
- data schema;
- inclusion and exclusion rules;
- date boundaries;
- units and currency;
- duplicate handling;
- missing-value behavior;
- formula or method;
- assumptions;
- intermediate outputs; and
- reconciliation target.

```text
Executed successfully
      ≠
Correct business rule
      ≠
Complete data
      ≠
Valid forecast
```

---

## Step 7: Maintain an assumption register

| Field | Purpose |
|---|---|
| Assumption ID | Stable reference |
| Statement | What is being assumed |
| Rationale or source | Why it is used |
| Owner | Who validates it |
| Sensitivity | How much the plan changes |
| Status | Proposed / Approved / Rejected / Expired |
| Review date | When it must be revisited |
| Failure action | What happens if disproven |

Assumptions should never be hidden inside a precise forecast.

---

## Step 8: Build scenarios

At minimum, consider:

- baseline;
- conservative; and
- stress scenarios.

Each scenario should identify:

- fixed evidence;
- changed assumptions;
- computed outcome;
- operational effect;
- risk;
- early warning indicator;
- reversible response; and
- required decision.

---

## Step 9: Synthesize without overclaiming

The recommendation should distinguish:

```text
Verified fact
Computed result
Research finding
Assumption
Inference
Human constraint
Recommendation
Decision
```

Do not present a model-generated recommendation as an approved organizational decision.

---

## Step 10: Retain human authority

Human owners decide:

- acceptable risk;
- political or stakeholder feasibility;
- budget and resource commitment;
- exceptions;
- policy interpretation;
- timing trade-offs; and
- final approval.

```text
Claude recommends
      ≠
Organization authorizes
```

---

## Process-optimization branch

When improving an existing process, first map:

- trigger;
- stages;
- owners;
- inputs and outputs;
- waiting time;
- calculations;
- handoffs;
- rework;
- review burden;
- state;
- approvals;
- exceptions; and
- failure paths.

Then classify the primary constraint:

```text
Retrieval bottleneck
Synthesis bottleneck
Calculation bottleneck
Handoff bottleneck
Review bottleneck
State bottleneck
Authority bottleneck
```

Target the controlling bottleneck rather than placing Claude across the entire workflow.

---

## Measures

### Stage measures

- source coverage;
- retrieval time;
- calculation reconciliation rate;
- assumption resolution rate;
- review time;
- defect rate;
- rework;
- escalation frequency;
- scenario accuracy; and
- plan refresh time.

### Business measures

- forecast error;
- service performance;
- resource utilization;
- cost variance;
- decision cycle time;
- avoided backlog; and
- stakeholder outcome.

---

## Failure modes

### Research-only plan

The plan summarizes current information but lacks verified internal data and calculations.

**Control:** Add approved internal evidence and executed analysis.

### Prose arithmetic

Material values are generated as fluent text.

**Control:** Execute and retain the calculation.

### Code certainty

Successful execution is treated as proof of valid assumptions.

**Control:** Review data, rules, assumptions, and reconciliation.

### Hidden constraints

Budget, policy, or political realities are absent from the model context.

**Control:** Make them explicit human-owned planning inputs.

### Over-delegated decision

The recommendation triggers action without authorized approval.

**Control:** Separate recommendation, approval, and execution.

### Automation without process analysis

The team automates an unnecessary or defective stage.

**Control:** Map the current process and identify the controlling bottleneck first.

---

## Implementation checklist

- [ ] Decision and owner are defined.
- [ ] Research path matches the question.
- [ ] Sources are current and traceable.
- [ ] Internal data is authorized and curated.
- [ ] Synthesis and calculation are separated.
- [ ] Material calculations are executed.
- [ ] Logic and control totals are reviewed.
- [ ] Assumptions are visible and owned.
- [ ] Scenarios include sensitivity.
- [ ] Human constraints are represented.
- [ ] Approval remains human-controlled.
- [ ] External action follows authorization.
- [ ] Workflow and business outcomes are measured.

---

## Decision rule

```text
Use Claude where evidence must be synthesized,
use deterministic analysis where numbers must be established,
and retain accountable human judgment where risk and authority determine the decision.
```

---

## Related material

- [Research, Planning, and Process Optimization](../modules/04-workflow-integration-solutions-design/lessons/03-research-planning-process-optimization.md)
- [Requirements Traceability and Pressure-Test Pattern](requirements-traceability-pressure-test-pattern.md)
- [Output Format and Reliability Pattern](output-format-reliability-pattern.md)
- [Human Review Gate Pattern](human-review-gate-pattern.md)
