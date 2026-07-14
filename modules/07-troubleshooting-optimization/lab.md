# Lab: Controlled Troubleshooting Investigation

## Scenario

A previously stable workflow now has four symptoms:

1. It sometimes selects `search_public_policy` instead of `search_internal_standard`.
2. Tool calls occasionally contain an invented `system_owner_email`.
3. The generated report ends halfway through a table.
4. P95 latency increased by 60% after a release.

The release changed the model version, prompt, tool descriptions, retrieval query, and output schema at the same time.

## Objectives

- Reconstruct a baseline.
- Classify failures by layer.
- Design controlled experiments.
- Validate fixes and rollback.

## Tasks

### Task 1: Incident record

Document impact, scope, first observed time, changed components, known-good version, and severity.

### Task 2: Evidence request

List the exact artifacts needed, including prompt/configuration versions, source results, tool definitions, stop reasons, usage, latency stages, and validation logs.

### Task 3: Hypotheses

For each symptom, write at least three plausible causes and one falsifying test.

### Task 4: Experiment plan

Restore the known-good stack, then test one change at a time:

| Run | Model | Prompt | Tools | Retrieval | Schema | Expected insight |
|---|---|---|---|---|---|---|
| Baseline | old | old | old | old | old | |
| 1 | new | old | old | old | old | |
| 2 | old | new | old | old | old | |
| 3 | old | old | new | old | old | |
| 4 | old | old | old | new | old | |
| 5 | old | old | old | old | new | |

Run the representative evaluation set and enough repeats to observe intermittent behavior.

### Task 5: Targeted fixes

Propose:

- clearer tool selection descriptions;
- strict schema that removes or rejects invented fields;
- stop-reason handling and output decomposition;
- stage-level latency profiling; and
- rollback criteria.

### Task 6: Post-fix validation

Define pass thresholds and monitoring for 7, 30, and 90 days.

## Deliverable

Create `troubleshooting-report.md` containing the evidence, experiment table, root cause, fix, regression results, and rollback.

## Acceptance criteria

- [ ] The initial response is not random prompt editing.
- [ ] Each symptom is classified by likely layer.
- [ ] One material variable changes per run.
- [ ] Wrong-tool fixes clarify when each tool applies.
- [ ] Invented parameters are rejected by schema and application validation.
- [ ] Truncation investigation uses stop reason and output budget.
- [ ] Latency is measured by stage.
- [ ] Fixes are tested against the full evaluation set.

<details>
<summary>Model solution outline</summary>

Because five components changed together, attribution is impossible without reconstructing the baseline. The tool confusion likely requires differentiated descriptions and examples. The invented email should be impossible under a strict schema and should fail application validation. The partial report requires stop-reason and client-timeout evidence. Latency must be decomposed into retrieval, model, tool, and validation stages before optimization.

</details>
