# Workflow Design Canvas

Map the end-to-end process before writing the final prompt.

## 1. Trigger

What event starts the workflow?

> 

Who or what is authorized to start it?

> 

## 2. Inputs

| Input | Source | Required? | Sensitivity | Validation |
|---|---|---|---|---|
| | | | | |

## 3. Processing stages

| Stage | Purpose | Component | Input | Output | Owner |
|---|---|---|---|---|---|
| 1 | | Human / Model / Code / Tool / System | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

## 4. Separation of concerns

| Concern | Where it belongs |
|---|---|
| Durable instructions | |
| Reusable knowledge | |
| Current-cycle evidence | |
| Generative analysis | |
| Deterministic calculation | |
| Current operational state | |
| Approval | |
| Audit record | |

## 5. Tool and connector design

| Tool or connector | Purpose | Read or write | Permission scope | Failure behavior |
|---|---|---|---|---|
| | | | | |

- [ ] Permissions follow least privilege.
- [ ] Destructive or irreversible actions require approval.
- [ ] Untrusted tool results are treated as data, not instructions.
- [ ] Timeouts, retries, and duplicate-action protection are defined.

## 6. Human decision points

| Decision | Human role | Evidence required | Possible outcomes |
|---|---|---|---|
| | | | Accept / Revise / Escalate / Reject |

## 7. Failure modes

| Failure mode | Detection | Containment | Recovery | Owner |
|---|---|---|---|---|
| Missing input | | | | |
| Stale source | | | | |
| Unsupported claim | | | | |
| Invalid calculation | | | | |
| Tool failure | | | | |
| Unauthorized action | | | | |
| Context loss | | | | |
| Invalid output format | | | | |

## 8. State and handoff

What state must survive between stages or sessions?

- 

Where is it stored?

- 

How is it validated before reuse?

- 

## 9. Observability

Record at minimum:

- workflow version;
- model identifier and settings;
- prompt version;
- input and source versions;
- tool calls and outcomes;
- validation results;
- latency and usage;
- reviewer decision; and
- final disposition.

## 10. Target-state diagram

```text
[Trigger]
   ↓
[Authorization and input checks]
   ↓
[Evidence collection]
   ↓
[Generative task]
   ↓
[Deterministic checks]
   ↓
[Human review]
   ↓
[Delivery or controlled action]
   ↓
[Logging, monitoring, and improvement]
```

Modify the diagram to match the actual workflow.

## 11. Simplification review

- What can be removed?
- What can remain manual?
- What can use a lower model tier?
- What should never be autonomous?
- Which stages can share a validated state artifact?

**Simplifications selected:**

- 
