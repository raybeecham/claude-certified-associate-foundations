# Module 7 Quiz: Troubleshooting & Optimization

## Result

```text
Full marks — 5 of 5
```

This public study quiz uses original scenarios to test the same Module 7 competencies without reproducing proprietary course wording.

## Instructions

For each scenario, choose the response that best applies the troubleshooting and optimization framework.

---

## Question 1 — First-response failure

A procurement specialist opens a new conversation and asks for a renewal-risk memo. The first draft is generic and omits two contractual obligations that were never included in the request.

What is the most likely cause?

A. Context overload

B. Stale configuration

C. Under-specification

D. Missing code execution

### Correct answer: C — Under-specification

The failure appears in the first response, and the required contractual details were absent from the task specification.

```text
First response wrong
      →
Inspect specification first
```

The narrow repair is to add the missing obligations, audience, decision purpose, and output requirements. A longer conversation, stronger model, or code execution does not supply facts that were never provided.

---

## Question 2 — Capability mismatch

A researcher repeatedly receives shallow strategic analysis while using a model selected primarily for speed. The task is well specified, the context is current, and the same lack of depth appears across several fresh conversations.

What is the best next action?

A. Continue adding more context

B. Test a model suited to deeper analysis against the same evaluation cases

C. Restart the conversation again

D. Replace the Project knowledge base

### Correct answer: B — Test a better-fitting model

The repeatable defect is aligned with the selected model's capability profile rather than missing instructions or session drift.

The change should still be controlled:

1. preserve the same task and evidence;
2. change only the model;
3. compare against explicit depth and quality criteria; and
4. measure latency and cost as guardrails.

```text
Model mismatch suspected
      ≠
Upgrade blindly
```

---

## Question 3 — Diagnostic sequence

A report output is disappointing, but the cause is not yet known.

Which approach is strongest before concluding that the task is unsuitable for Claude?

A. Switch immediately to the most capable model

B. Check specification, context, feature or model fit, and maintained configuration in that order

C. Rewrite the entire prompt several times

D. Abandon the workflow and complete it manually

### Correct answer: B — Run the diagnostic sequence

The sequence checks common and inexpensive causes before reaching the costly conclusion that the task is a poor fit.

```text
1. Specification
2. Context
3. Feature and model fit
4. Configuration
5. Task fit
```

This preserves causal evidence and avoids random prompt thrashing.

---

## Question 4 — Recurring correction

A weekly operations brief always requires the same manual correction: the owner and due date must be moved into a closing action table.

What is the most durable response after validating the change?

A. Continue fixing it manually

B. Capture the requirement in the appropriate standing instruction or repeatable procedure

C. Change models every week

D. Start a fresh chat and retype the reminder

### Correct answer: B — Promote the validated fix

The correction is recurring, observable, and shareable. It belongs in deliberate configuration rather than a one-off conversation.

Placement depends on the requirement:

- persistent output rule → instruction;
- ordered report-generation method → Skill or workflow;
- exact transformation → deterministic control.

```text
Recurring correction
      ↓
Validated repair
      ↓
Durable promotion
```

---

## Question 5 — Target the measured bottleneck

A monthly financial close workflow produces reliable numbers, but three analysts format their sections differently. A reviewer spends substantial time reconciling styles. The explicit optimization objective is to reduce reconciliation time without changing the calculations.

Which intervention most directly targets the bottleneck?

A. Upgrade the drafting model for faster prose generation

B. Use one governed shared procedure that formats every section to the same approved template

C. Ask analysts to start earlier

D. Add another reviewer

### Correct answer: B — Standardize the procedure at the source

The measured bottleneck is formatting variance, not drafting speed or reviewer capacity.

```text
Variance across operators
      →
Shared procedure and validation
```

The optimized version should be piloted against the baseline and measured for:

- reconciliation time;
- template compliance;
- accuracy;
- revision rounds; and
- governance integrity.

Adding another reviewer divides the waste rather than removing it.

---

# Competency summary

| Question | Competency |
|---|---|
| 1 | Distinguish under-specification from context and configuration problems |
| 2 | Diagnose model or feature mismatch through controlled comparison |
| 3 | Apply the cheapest-fix-first diagnostic sequence |
| 4 | Promote recurring corrections into durable configuration |
| 5 | Optimize the measured bottleneck rather than general speed |

## Exam shortcuts

```text
Wrong on the first response
→ inspect specification

Persistently shallow on a speed-oriented route
→ test model fit

Cause unknown
→ run the diagnostic sequence

Same manual correction every cycle
→ validate and promote

Measured bottleneck is variance
→ standardize the procedure
```

## Common distractors

### Stronger model as universal repair

A stronger model does not repair missing facts, stale sources, incorrect permissions, exact business logic, or a bottleneck located elsewhere.

### More context by default

More context can increase noise and does not supply missing task clarity automatically.

### Manual work as safety

Manual correction is not a durable control when the same defect can be prevented through reviewed configuration or deterministic logic.

### Adding capacity instead of removing waste

Adding reviewers or starting earlier may shift work without fixing its source.

## Public-repository note

These scenarios are fictional and original. They assess concepts from the supplied Module 7 material without reproducing remembered or proprietary quiz wording.