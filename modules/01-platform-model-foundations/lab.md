# Lab: Platform and Model Selection Matrix

## Scenario

A federal cybersecurity program is considering Claude for three workloads:

1. **Ad hoc policy analysis:** Analysts compare a new public memorandum with an internal implementation plan. The work is exploratory and always human-reviewed.
2. **Control mapping service:** An application maps system evidence to a fixed control taxonomy, returns structured results, and integrates with an existing dashboard.
3. **High-volume document triage:** A service classifies large numbers of public documents into a small set of routing categories. Speed and unit cost matter.

You have not been given model names, prices, or limits. Your design must remain valid as those facts change.

## Objectives

- Select the appropriate interaction pattern.
- Define measurable model-selection criteria.
- Distinguish context, output, current knowledge, and state requirements.
- Define observability and migration controls.

## Tasks

### Task 1: Requirements matrix

Complete:

| Requirement | Ad hoc policy analysis | Control mapping service | Document triage |
|---|---|---|---|
| Primary user | | | |
| Interaction pattern | | | |
| Integration required | | | |
| Evidence source | | | |
| Structured output | | | |
| State | | | |
| Human review | | | |
| Quality threshold | | | |
| Latency target | | | |
| Cost/throughput target | | | |
| Governance constraint | | | |

### Task 2: Model selection test

For each workload, define:

- five representative test cases;
- at least two edge cases;
- quality metrics;
- latency metric;
- cost metric;
- one hard release gate; and
- the rule for selecting among candidate models.

Do not write “use the most capable model.”

### Task 3: Request and response flow

Draw or describe the flow for the control mapping service. Include:

- identity and authorization;
- trusted instructions;
- current task;
- evidence retrieval;
- model request;
- response and stop handling;
- schema validation;
- human review or escalation;
- persistence; and
- logging.

### Task 4: Migration plan

Assume the selected model version will be retired. Write an eight-step migration plan with rollback.

## Deliverable

Create `platform-selection-matrix.md` containing:

1. completed requirements matrix;
2. selection tests;
3. request/response flow;
4. migration plan; and
5. residual risks.

## Acceptance criteria

- [ ] Each interaction pattern is justified by requirements.
- [ ] Model selection uses measurable thresholds.
- [ ] State is explicitly managed by the product or application.
- [ ] Current policy claims require authoritative current evidence.
- [ ] Stop reasons and schema failures have defined handling.
- [ ] Migration changes one major variable at a time.
- [ ] Logs are sufficient for reproduction but minimize sensitive content.

<details>
<summary>Model solution outline</summary>

### Likely pattern choices

- Ad hoc analysis: interactive Claude experience, assuming the environment is approved for the data and analysts remain accountable.
- Control mapping: API-backed application with versioned prompts, retrieval, structured output, validation, and dashboard integration.
- Document triage: API or batch-oriented service using the least expensive and fastest candidate that meets a validated quality threshold.

### Model selection rule

A defensible rule is: eliminate candidates that fail hard gates, then select the lowest total operational cost candidate that meets quality, latency, throughput, governance, and tool/structure requirements on the representative evaluation set.

### Migration

Freeze the current stack, run baseline, test candidate on identical cases, compare by severity and slices, investigate regressions, stage deployment, monitor, preserve rollback, and update records.

</details>
