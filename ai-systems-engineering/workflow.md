# Standard Workflow

Use this sequence before beginning any substantial AI task.

## Step 1: Define the problem

Document:

- business objective;
- audience and decision supported;
- current process and pain point;
- required deliverable;
- success measures;
- consequence of failure; and
- constraints.

**Gate:** Do not proceed until the objective can be stated without mentioning a model or prompt.

## Step 2: Choose the workspace

Ask whether the work is:

- one-off;
- recurring;
- research-intensive;
- deliverable-oriented;
- collaborative; or
- integrated into software.

Select the simplest suitable environment. Record why other plausible surfaces are unnecessary.

## Step 3: Select capabilities

Separate the workflow into:

| Need | Typical solution |
|---|---|
| Stable background and rules | Persistent workspace or Project |
| Repeatable procedure | Skill or workflow template |
| Calculation or transformation | Code Execution or deterministic service |
| Current evidence | Search, retrieval, connector, supplied source |
| Editable output | Artifact or file-generation tool |
| Cross-session preference | Memory or profile, when appropriate |
| Current operational truth | External authoritative system |

**Gate:** Every capability must map to a requirement.

## Step 4: Select the model

Evaluate:

- structure and ambiguity;
- reasoning depth;
- input length and source diversity;
- consequence of failure;
- volume and latency;
- cost or usage; and
- available validation.

Define the minimum quality floor, then test candidate models on representative cases.

## Step 5: Design context

Classify information as:

- durable instruction;
- reusable knowledge;
- current task input;
- temporary working state;
- external source of truth;
- persistent preference; or
- exclude.

Create a plan for checkpoints, summaries, clean restarts, versioning, and deletion.

## Step 6: Design the workflow

Map the sequence:

```text
Input
  ↓
Precondition and authorization checks
  ↓
Retrieval or evidence collection
  ↓
Generative analysis
  ↓
Deterministic operations
  ↓
Validation
  ↓
Human review or approval
  ↓
Delivery or controlled action
  ↓
Logging and monitoring
```

For each stage define owner, input, output, failure mode, retry, escalation, and rollback.

## Step 7: Design the prompt

Only after the system is defined, write the prompt using:

- objective;
- audience;
- authorized inputs;
- source hierarchy;
- constraints;
- required process;
- output contract;
- uncertainty behavior;
- tool rules; and
- success criteria.

## Step 8: Evaluate

Build representative cases covering:

- normal inputs;
- edge cases;
- missing information;
- conflicting information;
- adversarial or untrusted content;
- prohibited actions;
- tool failures; and
- high-consequence failures.

Measure accuracy, grounding, completeness, schema validity, safety, latency, cost, revision burden, and escalation quality.

## Step 9: Release and operate

Before use:

- confirm authorization and data policy;
- pin versions;
- establish logging and monitoring;
- define human ownership;
- stage rollout;
- preserve rollback; and
- set review and retirement dates.

## Step 10: Improve

After each meaningful use, record:

- what succeeded;
- what failed;
- which assumptions were wrong;
- which controls caught errors;
- which errors escaped;
- how much review was required; and
- what should change next.

## Fast path

For low-consequence one-off work, use the same logic in compressed form:

```text
Outcome → evidence → workspace → model → prompt → review
```

The method scales down. It should not disappear.
