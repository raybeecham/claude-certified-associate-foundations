# Failure Localization Pattern

## Problem

An AI-assisted workflow underperforms, and the operator responds by rewriting the entire prompt. The output may change, but the team cannot determine what fixed the problem, what regressed, or whether the root cause was prompt wording at all.

## Context

Use this pattern when:

- a prompt produces output that is close but not usable;
- a recurring workflow shows inconsistent quality;
- one section fails while others pass;
- several possible causes exist; or
- prompt, evidence, model, context, tool, and evaluation failures could be confused.

## Recommended design

```text
Observe
   ↓
Classify the symptom
   ↓
Localize the responsible layer
   ↓
Modify the smallest responsible component
   ↓
Validate improvement and regression
   ↓
Continue, accept, edit, escalate, or stop
```

### 1. Observe

Describe the failure in testable terms.

Weak observation:

> The answer is bad.

Useful observation:

> The executive summary exceeds 300 words, uses technical terminology, and omits the requested decision.

### 2. Classify

Common quality dimensions include:

- accuracy;
- completeness;
- grounding;
- relevance;
- audience fit;
- tone;
- structure;
- schema validity;
- consistency;
- latency;
- cost;
- safety; and
- escalation quality.

### 3. Localize

| Layer | Example failure |
|---|---|
| Role | Wrong professional lens |
| Context | Generic or misaligned output |
| Task | Wrong action performed |
| Constraints | Wrong length, tone, or scope |
| Output contract | Missing sections or invalid structure |
| Evidence | Unsupported or stale claims |
| Decomposition | Competing objectives and shallow work |
| Model | Insufficient capability for task complexity |
| Context management | Drift, stale state, or contradiction |
| Deterministic execution | Incorrect arithmetic or transformation |
| Tool design | Invalid parameters, permissions, or side effects |
| Evaluation | Defects were not detected before release |
| Governance | Authority or review responsibility is unclear |

### 4. Modify

Apply the smallest intervention supported by the diagnosis. Preserve validated content and controls.

### 5. Validate

Check both:

- **improvement:** did the failed dimension improve?;
- **regression:** did any previously passing dimension degrade?

### 6. Decide

Choose one:

- continue iterating;
- accept;
- perform a manual edit;
- escalate to a qualified reviewer;
- change the workflow architecture; or
- stop the task.

## Controls

- Define acceptance criteria before comparing versions.
- Change one significant variable at a time when practical.
- Version prompts and outputs for recurring workflows.
- Record the symptom, diagnosis, change, and result.
- Do not use model self-confidence as evidence of correctness.
- Preserve human approval for consequential decisions.

## Trade-offs

Targeted iteration may be slower than a wholesale rewrite for a severely underspecified first prompt. It produces more reliable learning, traceability, and maintainability for recurring or consequential work.

## Common failure modes

- changing several components without tracking them;
- confusing fluent wording with corrected substance;
- fixing tone while losing required facts;
- continuing to prompt when evidence or permissions are missing;
- optimizing beyond the point of practical value;
- failing to test for regression; and
- treating a human-authority boundary as a prompt problem.

## Decision rule

> Change the prompt when the failure is instructional. Change the system when the failure is architectural.

## Public-repository rule

Use fictional, synthetic, public, or explicitly authorized examples. Do not include confidential data, proprietary workflows, credentials, or facts that identify a nonpublic engagement.