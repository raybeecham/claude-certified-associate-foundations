# Workflow Efficiency Audit and Promotion Pattern

## Problem

Recurring AI-assisted workflows often contain hidden friction:

- repeated context entry;
- recurring manual corrections;
- operator-dependent results;
- duplicated verification;
- unnecessary handoffs;
- avoidable reformatting; and
- fixes that remain personal instead of becoming shared infrastructure.

The problem is not merely wasted time. Repetition and variance can create inconsistent quality, missed controls, and growing maintenance cost.

## Context

Use this pattern when:

- a recurring workflow takes longer than expected;
- the same manual steps appear every cycle;
- several users perform the same work differently;
- output quality depends on personal workarounds;
- a validated fix should be promoted into shared configuration;
- optimization needs evidence and rollback; or
- a team must distinguish removable friction from required governance.

## Recommended design

```text
Observe one complete workflow cycle
      ↓
Record repetition, correction, and variance
      ↓
Identify root cause
      ↓
Classify fix as rule, reference, procedure, or deterministic control
      ↓
Place it in the narrowest correct layer
      ↓
Pilot against the baseline
      ↓
Measure target and guardrail metrics
      ↓
Adopt / revise / revert
      ↓
Monitor and review
```

## 1. Define the optimization objective

Select the primary reason for optimization:

- cycle time;
- revision reduction;
- consistency;
- verified accuracy;
- defect prevention;
- throughput;
- latency;
- cost;
- user effort; or
- governance reliability.

```text
Faster
      ≠
Better automatically
```

Pair the primary metric with guardrails for quality, safety, privacy, fairness, and accountability.

## 2. Instrument one full cycle

Record every manual step, including:

- repeated context;
- repeated correction;
- formatting;
- verification;
- handoff;
- waiting time;
- duplicate calculation or research;
- tool switching;
- approval; and
- rework.

Do not rely only on memory. Observe an actual representative cycle.

## 3. Classify the friction

### Repetition

The same content or instruction is re-entered every run.

### Correction

The same output defect is manually repaired every cycle.

### Variance

Different operators produce different results from the same intended workflow.

### Required control

The step exists to preserve approval, privacy, security, fairness, or accountability and should not be removed merely because it takes time.

```text
Visible effort
      ≠
Waste automatically
```

## 4. Apply the placement test

| Type | Correct home |
|---|---|
| Rule | Project or standing instruction |
| Reference | Governed knowledge or source |
| Procedure | Skill or workflow |
| Deterministic business logic | Code, query, schema, or technical control |
| One-time detail | Current prompt |

```text
Correct fix
+ wrong layer
=
fragile optimization
```

## 5. Consolidate carefully

Combine related steps only when:

- permissions are compatible;
- independent approval is not required;
- data boundaries are preserved;
- failure remains observable; and
- the combined stage can still be tested and rolled back.

Do not collapse human approval, independent verification, or segregation-of-duty boundaries into an automated convenience step.

## 6. Build the smallest shared change

Prefer one bounded intervention:

- add a standing rule;
- add or update one governed reference;
- create or revise one Skill;
- move one calculation into deterministic code;
- standardize one verification stage; or
- remove one redundant handoff.

Avoid changing model, prompt, tools, context, and workflow simultaneously.

## 7. Pilot with the baseline retained

The pilot should define:

- representative cases;
- participating users;
- number of cycles;
- baseline metrics;
- target metrics;
- quality and governance guardrails;
- edge cases;
- owner and approver;
- rollback conditions; and
- adopt, revise, or revert criteria.

```text
One successful run
      ≠
Validated optimization
```

## 8. Measure net improvement

Measure not only local speed but the full workflow effect.

Check whether the change:

- shifts effort to another role;
- creates hidden rework;
- increases maintenance;
- expands permissions;
- reduces accuracy;
- removes useful variation;
- weakens controls; or
- creates a new single point of failure.

## 9. Define stop conditions

Stop optimizing when:

- the target metric is met;
- further gains are marginal;
- added complexity exceeds benefit;
- maintenance cost grows faster than value;
- risk increases; or
- the next change no longer addresses a material problem.

## Controls

- workflow baseline;
- friction register;
- rule–reference–procedure classification;
- configuration owner;
- versioning;
- representative pilot;
- guardrail metrics;
- rollback plan;
- approval record;
- monitoring; and
- review cadence.

## Failure modes

### Optimizing without a baseline

No objective evidence shows whether the change helped.

### Promoting a local workaround too early

A narrow fix becomes a team-wide defect.

### Removing required governance

A control is misclassified as friction.

### Choosing the wrong configuration home

The optimization does not persist or creates bloat.

### Optimizing only for speed

Quality or reliability declines.

### Never stopping

Optimization itself becomes recurring waste.

## Decision record

```text
Workflow:
Owner:
Optimization objective:
Baseline:
Observed friction:
Friction type:
Root cause:
Proposed change:
Rule / reference / procedure / deterministic control:
Selected layer:
Pilot design:
Primary metric:
Guardrail metrics:
Results:
Governance impact:
Rollback condition:
Disposition:
Next review:
```

## Compact rule

> Observe one complete cycle, classify repetition, correction, and variance, place each fix as a rule, reference, procedure, or deterministic control, pilot against the baseline, and adopt only when the measured gain survives quality and governance checks.