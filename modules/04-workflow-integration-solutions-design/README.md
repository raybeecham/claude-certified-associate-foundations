# Module 4: Workflow Integration & Solution Design

Associate Persona · Official Exam Domain 4 · **16% of the exam blueprint**

> **Status:** In progress — Module 4 is the active module.

## Module thesis

> Workflow value comes from deciding what to delegate—not from automating everything.

```text
Business need
      ↓
Traceable requirements and viable use case
      ↓
Verified research and executed analysis
      ↓
Process planning and optimization
      ↓
Solution design and iteration
      ↓
Delegation mapping
      ↓
Value and limitation communication
      ↓
Validated workflow
```

---

# Course-aligned roadmap

- [x] [01. Module Introduction](lessons/01-module-introduction.md)
- [x] [02. Analyzing Requirements & Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [x] [03. Research, Planning & Process Optimization](lessons/03-research-planning-process-optimization.md)
- [ ] 04. Solution Design, Development & Iteration
- [ ] 05. Delegation Mapping
- [ ] 06. Communicating Value & Limitations
- [ ] 07. Exercise: Redesign a Workflow
- [ ] 08. Module 4 Quiz
  - [ ] Quiz
  - [ ] Takeaways
- [ ] 09. Module Complete

No later lesson is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: Personal use versus workflow integration

```text
I use Claude
      ↓
One person supplies context, reviews, and adapts

Our workflow uses Claude
      ↓
A team follows repeatable stages with defined
inputs, controls, ownership, state, and outcomes
```

```text
Repeated prompting
      ≠
Designed workflow
```

## Delegation modes

| Mode | Appropriate responsibility |
|---|---|
| AI-appropriate | Interpretation, classification, synthesis, drafting, and options under bounded criteria |
| Human-retained | Authority, accountability, professional judgment, exceptions, and approval |
| Collaborative | Claude prepares or analyzes while a human evaluates and decides |
| Deterministic | Exact calculations, schemas, fixed rules, routing, and authorization checks |
| Tool-owned | Controlled retrieval, transformation, external actions, and system interaction |
| Storage-owned | Authoritative records, durable state, checkpoints, logs, and version history |

```text
Generate recommendation
      ≠
Authorize action
```

---

# Foundation 2: Requirements and use-case analysis

```text
Messy inputs
      ↓
Candidate requirements
      ↓
Traceability and classification
      ↓
Pressure-test
      ↓
Human clarification and approval
      ↓
Requirement baseline
```

## Requirement classes

| Class | Meaning |
|---|---|
| Explicit | Directly stated in the source |
| Implied | Inferred from criteria, dependencies, or cross-references |
| Ambiguous | Supports multiple material interpretations |
| Missing | Needed for a buildable or testable task but absent |
| Conflicting | Relevant sources disagree |
| Assumption | Temporary premise pending confirmation |
| Constraint | Limits the solution or method |
| Acceptance criterion | Defines observable completion |

```text
Extracted fact
      ≠
Implied requirement
      ≠
Analyst assumption
```

Every material requirement should have an exact source location, owner, status, and completion test.

## Use-case viability

```text
Measurable business outcome
+ user and current process
+ repeatable task
+ authorized inputs
+ bounded AI contribution
+ retained human authority
+ deterministic controls
+ acceptance criteria
+ risk and escalation
```

---

# Foundation 3: Research, planning, and process optimization

Planning combines three responsibilities that require different controls.

```text
Research and synthesis
      +
Executed computation
      +
Human judgment and authority
      ↓
Defensible plan
```

## Research-path selection

| Need | Preferred path |
|---|---|
| Straightforward current fact | Web search |
| Deeper multi-source investigation | Research |
| Supplied-document question | Closed-source analysis |
| Internal operational truth | Approved internal system |
| Exact metric or transformation | Code execution |
| Missing organizational constraint | Human clarification |

Current official Claude guidance describes web search as suited to straightforward current lookups and Research as the deeper path for more comprehensive investigation. Product availability can change.

## Synthesis versus calculation

```text
Evidence and trade-off synthesis → Claude with verified sources
Material calculation             → code execution or deterministic analytics
Risk appetite and approval       → accountable human
```

```text
Plausible number in prose
      ≠
Computed result
```

Material planning values such as growth, throughput, utilization, backlog burn rate, cost, and headcount should be calculated over actual data.

## Code-execution trust boundary

```text
Inspect data and schema
      ↓
Define rules and assumptions
      ↓
Review critical logic
      ↓
Execute
      ↓
Inspect intermediate results
      ↓
Reconcile
      ↓
Synthesize scenarios
      ↓
Human decision and approval
```

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

## Capacity-planning example

```text
Curate four quarters of workload and staffing data
      ↓
Compute volume growth and throughput
      ↓
Build baseline, conservative, and stress scenarios
      ↓
Claude synthesizes recommendation and trade-offs
      ↓
Operations lead weighs budget, hiring, and risk
      ↓
Authorized staffing decision
```

Claude may improve the analysis and recommendation. It does not authorize hiring.

## Process optimization

Map the current process before adding automation:

- triggers;
- inputs;
- stages;
- owners;
- waiting time;
- calculations;
- handoffs;
- rework;
- state;
- approvals;
- exceptions; and
- failure paths.

Then identify the controlling bottleneck:

```text
Retrieval
Synthesis
Calculation
Handoff
Review
State
Authority
```

```text
Automating a broken process
      =
Producing defects faster
```

Target the actual bottleneck and measure the business outcome.

---

# Integrated planning protocol

```text
1. Define the decision and accountable owner
2. Establish the requirement baseline
3. Map evidence, data, constraints, and stakeholders
4. Select web search, Research, closed-source, internal, or code path
5. Curate and label inputs
6. Separate synthesis questions from calculation questions
7. Execute and reconcile material analysis
8. Record assumptions and sensitivity
9. Build scenarios and trade-offs
10. Retain human judgment for feasibility, risk, and approval
11. Optimize the controlling process bottleneck
12. Measure stage performance and business outcomes
```

## Planning evidence table

| Planning input | Type | Source or method | Validation | Sensitivity | Decision impact |
|---|---|---|---|---|---|
| Workload growth | Computed | Code-executed analysis | Reconcile | Medium | Capacity forecast |
| Budget ceiling | Human constraint | Approved budget | Owner confirmation | High | Feasible scenario |
| Productivity ramp | Assumption | Historical cohorts | Sensitivity review | High | Staffing timing |
| Market availability | Research finding | Current sources | Scope and currency | Medium | Hiring risk |

This makes facts, calculations, assumptions, and human constraints visible.

---

# Current module resources

## Course-aligned lessons

- [Module Introduction](lessons/01-module-introduction.md)
- [Analyzing Requirements and Use Cases](lessons/02-analyzing-requirements-use-cases.md)
- [Research, Planning, and Process Optimization](lessons/03-research-planning-process-optimization.md)

## Prompt notebooks

- [Module Introduction prompts](../../prompts/module-04/01-module-introduction-prompts.md)
- [Requirements Analysis prompts](../../prompts/module-04/02-analyzing-requirements-use-cases-prompts.md)
- [Research, Planning, and Process Optimization prompts](../../prompts/module-04/03-research-planning-process-optimization-prompts.md)

## Engineering patterns

- [Requirements Traceability and Pressure-Test Pattern](../../patterns/requirements-traceability-pressure-test-pattern.md)
- [Verified Planning Workflow Pattern](../../patterns/verified-planning-workflow-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Quick current lookup        → web search
Deep multi-source inquiry   → Research
Exact trend or forecast     → code execution
Trade-off synthesis         → Claude + verified evidence
Risk, budget, or approval   → human
Messy current process       → map before automating
```

For planning scenarios:

1. identify the decision and owner;
2. distinguish research, supplied evidence, computation, synthesis, and judgment;
3. match research depth to the question;
4. preserve source authority, scope, and currency;
5. execute material calculations over actual data;
6. review logic, data, assumptions, and reconciliation;
7. use Claude for synthesis, scenarios, and trade-offs;
8. retain human authority for feasibility and approval;
9. identify the real process bottleneck; and
10. choose the least complex improvement that changes the outcome.

---

# Completion criteria

- [x] I completed the Module 4 introduction.
- [x] I completed Analyzing Requirements and Use Cases.
- [x] I completed Research, Planning, and Process Optimization.
- [ ] I can distinguish personal use from workflow integration.
- [ ] I can explain Delegation and its responsibility modes.
- [ ] I can build and pressure-test a traceable requirement register.
- [ ] I can distinguish web search, Research, source analysis, code execution, and human clarification.
- [ ] I can separate synthesis from material calculation.
- [ ] I can define a reproducible planning analysis.
- [ ] I can create an assumption register and sensitivity scenarios.
- [ ] I can map a current process and identify the controlling bottleneck.
- [ ] I can retain human ownership of risk, feasibility, and approval.
- [ ] I can create a component responsibility matrix.
- [ ] I can design tool, state, validation, and approval boundaries.
- [ ] I can communicate value and limitations without overclaiming.
- [ ] I completed the workflow-redesign exercise.
- [ ] I completed the Module 4 quiz and takeaways.
- [ ] I completed the workflow lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include confidential planning data, workforce records, internal budgets, proprietary processes, credentials, system identifiers, engagement-identifying facts, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute workforce, financial, operational, architecture, legal, compliance, or other professional advice.

## Official reading

- [When to use web search, extended thinking, and research](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)
- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
