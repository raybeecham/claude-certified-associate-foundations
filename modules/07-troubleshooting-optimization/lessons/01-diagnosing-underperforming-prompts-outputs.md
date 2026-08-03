# Lesson 1: Diagnosing Underperforming Prompts and Outputs

## Overview

When an output disappoints, avoid two weak defaults:

- concluding immediately that Claude cannot do the task; or
- changing several things at once until something appears to work.

Troubleshooting begins with diagnosis.

```text
Observe the symptom
      ↓
Read the timing and failure pattern
      ↓
Test the cheapest likely cause first
      ↓
Apply one bounded fix
      ↓
Verify the result
      ↓
Keep, revise, reshape, or revert
```

> Underperformance has findable root causes. Diagnose the responsible layer before changing the system.

---

# Plain-English explanation

Weak output does not automatically mean the prompt is bad, the model is weak, or the task is impossible.

The same visible problem can come from different causes:

- the task was never fully specified;
- the conversation became overloaded;
- the wrong feature or model was selected;
- a standing instruction, source, or Skill became stale; or
- the requested outcome was never realistically available.

The useful question is not:

> Why is Claude bad at this?

It is:

> Which layer is responsible, what evidence supports that diagnosis, and what is the smallest relevant fix?

---

# One analogy: diagnosing a vehicle problem

A vehicle that loses power could have a fuel problem, a battery problem, a sensor problem, or an unrealistic load.

Replacing every component at once may temporarily hide the symptom, but it does not establish the cause.

AI troubleshooting follows the same logic:

```text
Symptom
      ≠
Root cause
```

Read the pattern, test the likely cause, change one thing, and compare the result.

---

# Learning objectives

By the end of Module 7, you should be able to:

1. diagnose underperformance and trace it to under-specification, context overload, wrong feature or model, stale configuration, or expectation mismatch;
2. adjust the approach from observed feedback and convert recurring corrections into persistent fixes; and
3. optimize workflows by promoting stable context, format, procedure, and verification steps into the appropriate Project, Skill, instruction, or tool layer.

---

# Five diagnostic categories

## 1. Under-specification

### Symptom timing

The output is wrong or weak from the **first response**.

### Likely cause

The task contract omitted necessary:

- context;
- objective;
- constraints;
- evidence boundaries;
- success criteria;
- audience;
- examples; or
- output format.

### Fix

Add the missing information rather than rewriting everything.

```text
First response wrong
      →
Check specification first
```

### Example

> “The summary keeps missing key points.”

The prompt never defined what counts as important.

A targeted repair defines the criteria, such as decisions, risks, deadlines, owners, and unresolved questions.

---

## 2. Context overload

### Symptom timing

The session started well but **degraded over time**.

### Likely cause

The conversation accumulated too much material, irrelevant content, conflicting instructions, or compressed earlier details.

Current Claude guidance says that, when code execution is enabled, automatic context management can summarize earlier messages as a long conversation approaches its context limit. This allows the conversation to continue, but earlier detail may be represented more compactly.

### Fix

- restart from a clean summary;
- carry forward only authoritative constraints and decisions;
- remove irrelevant material;
- move stable instructions into the appropriate persistent layer; or
- split unrelated work into separate chats or Projects.

```text
Started right
+ degraded later
      →
Inspect context before rewriting prompt
```

### Example

> “It followed the format early in the conversation but stopped halfway through.”

A clean restart may solve the problem. If the format is a recurring rule, persist it in Project instructions or another suitable configuration layer rather than relying on a very long chat.

---

## 3. Wrong feature or model

### Symptom pattern

The failure is **specific and repeatable**.

Examples include:

- arithmetic or aggregation is subtly wrong;
- a deterministic transformation varies unnecessarily;
- a tool call uses the wrong schema or parameters;
- analysis is consistently too shallow for the task;
- the wrong entry point lacks required files or capabilities; or
- the selected model emphasizes speed where deeper reasoning is required.

### Fix

Use the right capability rather than compensating with more prose.

```text
Specific repeatable error
      →
Check feature and model fit
```

Examples:

- move calculations into code execution;
- use a structured extraction path for machine-readable output;
- select a model that meets the task’s reasoning requirement;
- use a connector only when the required source is available and authorized; or
- choose a different entry point when the current one cannot perform the work.

A stronger model is not automatically the answer. Select the smallest capability that fixes the diagnosed limitation.

---

## 4. Stale configuration

### Symptom timing

The same workflow **used to work** but has quietly degraded.

### Likely cause

A maintained dependency drifted, such as:

- Project instructions;
- uploaded knowledge;
- source authority or version;
- a custom Skill;
- connector scope;
- Memory;
- a policy reference;
- a schema;
- examples or templates; or
- a human-review process.

### Fix

Run the Module 5 configuration-maintenance process:

```text
Inventory
      ↓
Compare with current reality
      ↓
Classify drift
      ↓
Edit / replace / disable / revoke / reset / retire
      ↓
Regression test
```

```text
Used to work
      →
Inspect configuration before rewriting prompt
```

---

## 5. Expectation mismatch

### Symptom pattern

The requested outcome remains unavailable after specification, context, feature, model, and configuration defects are ruled out.

### Likely cause

The task asks for something the system cannot responsibly provide, such as:

- an exact future event;
- certainty where evidence is incomplete;
- a final professional judgment without the qualified human owner;
- information that is not available in the provided or connected sources;
- guaranteed fairness or correctness without evaluation; or
- an external action that the selected feature cannot perform.

### Fix

Reshape the task.

```text
Impossible output request
      ↓
Convert to bounded analysis
```

Examples:

- replace an exact sales prediction with a scenario range and stated assumptions;
- replace certainty with confidence levels and evidence gaps;
- replace a final determination with a draft, checklist, or evidence summary for a qualified reviewer; or
- replace unsupported claims with questions that identify missing evidence.

Recognizing expectation mismatch is not failure. It prevents endless tuning for an output that was never realistically available.

---

# Read the symptom timing

| Symptom | Primary hypothesis | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract elements |
| Good initially, then degrades | Context overload | Restart or summarize cleanly |
| Specific repeatable error type | Wrong feature or model | Select the correct capability |
| Worked before, now performs poorly | Stale configuration | Inspect and maintain dependencies |
| Still impossible after other causes are ruled out | Expectation mismatch | Reshape the task |

The timing is evidence, not proof. Confirm the diagnosis with a controlled test.

---

# Cheapest-fix-first diagnostic sequence

Run the following in order:

## Step 1: Re-read the prompt

Check the five core task components:

```text
Objective
Context and evidence
Constraints
Output format
Success criteria
```

Ask:

- What did the user expect?
- What was actually specified?
- Which required detail was missing or ambiguous?

## Step 2: Inspect context

Ask:

- Did the session start correctly and later drift?
- Is the chat carrying unrelated material?
- Are old instructions competing with current ones?
- Has a summary compressed details that need to be restated?
- Should stable information move into a Project or other persistent mechanism?

## Step 3: Check feature and model fit

Ask:

- Does the task require code execution?
- Does it require a connector or uploaded file?
- Does it require structured output?
- Does the selected model meet the reasoning and quality requirement?
- Is the entry point capable of the requested action?

## Step 4: Inspect configuration

Review:

- Project instructions;
- knowledge and source versions;
- Skills and dependencies;
- connectors and permissions;
- Memory;
- schemas and templates;
- review gates; and
- policy or product changes.

## Step 5: Test task fit

Only after the cheaper causes are ruled out, ask:

- Is the requested result knowable?
- Is the required evidence available?
- Can the system perform the requested action?
- Does the task require non-transferable professional or organizational judgment?
- Should the task be reframed rather than optimized?

```text
Prompt
      ↓
Context
      ↓
Feature and model
      ↓
Configuration
      ↓
Task fit
```

This order prevents expensive overcorrection.

---

# Isolating the cause

Create a minimal reproducible case.

Record:

- expected behavior;
- observed behavior;
- exact prompt;
- relevant context;
- model and entry point;
- enabled tools and features;
- configuration version;
- data and source versions;
- time and environment;
- repeatability; and
- the smallest case that still reproduces the failure.

Then test one hypothesis at a time.

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

Do not change the prompt, model, tools, context, and configuration simultaneously. That may improve the result, but it destroys causal evidence.

---

# Worked failure gallery

## Failure 1: Missing key points

**Symptom:** Wrong from the first response.

**Diagnosis:** Under-specification.

**Repair:** Define which points matter and the required output structure.

## Failure 2: Format degrades in a long session

**Symptom:** Started correctly, then drifted.

**Diagnosis:** Context overload or competing context.

**Repair:** Restart from a verified summary. Persist recurring format rules in the correct instruction layer.

## Failure 3: Numbers are subtly wrong

**Symptom:** Repeatable quantitative errors.

**Diagnosis:** Wrong feature.

**Repair:** Use code execution, validate inputs, and compare results with a deterministic check.

## Failure 4: Workflow worked last month

**Symptom:** Same setup now produces weaker results.

**Diagnosis:** Stale configuration.

**Repair:** Review instructions, source versions, Skills, connectors, schemas, and policy dependencies.

## Failure 5: Exact future sales prediction

**Symptom:** No repair produces reliable precision.

**Diagnosis:** Expectation mismatch.

**Repair:** Ask for a scenario model, range, assumptions, drivers, and sensitivity analysis rather than an exact future fact.

---

# Diagnostic decision record

```text
Observed failure:
[what happened]

Expected behavior:
[what should have happened]

Symptom timing:
[first response / degraded over time / specific error / used to work / persistent mismatch]

Primary hypothesis:
[under-specification / context / feature-model / configuration / expectation]

Evidence:
[why this hypothesis fits]

Minimal test:
[one bounded change]

Result:
[improved / unchanged / worse]

Decision:
[keep / revise / revert / reshape task]

Regression checks:
[representative cases and governance controls]
```

---

# Governance remains active

Troubleshooting must not remove controls merely to improve output.

Do not weaken:

- data-classification boundaries;
- Skill or connector review;
- least privilege;
- review gates;
- fairness checks;
- disclosure requirements;
- explanation and recourse;
- logging and monitoring; or
- escalation authority.

```text
Performance improved
      ≠
Workflow approved
```

A repair is acceptable only when it improves the target behavior without creating a material regression in quality, safety, privacy, fairness, or accountability.

---

# Practical example

A team reports that a recurring executive summary has become generic.

A weak response is to switch immediately to the most capable model and rewrite the entire prompt.

A disciplined diagnosis asks:

1. Was the summary generic on the first run, or did it degrade over time?
2. Does the prompt define which decisions, risks, metrics, and actions matter?
3. Is the session carrying unrelated history?
4. Is the source document or Project knowledge current?
5. Did a standing instruction or template change?
6. Does the selected model meet the required depth?
7. Can a minimal test reproduce the problem?

The answer may be a one-line specification repair, a clean restart, a refreshed source, a corrected instruction, or a model change. The evidence determines which.

---

# Recap

- Weak output has multiple possible causes.
- Read symptom timing before editing anything.
- Check the prompt first because under-specification is common and cheap to fix.
- Check context when a session degrades over time.
- Use the correct feature or model for specific repeatable limitations.
- Inspect stale configuration when a workflow used to work.
- Treat task mismatch as the final conclusion, not the first assumption.
- Test one hypothesis and one bounded change at a time.
- Preserve governance while troubleshooting.

```text
Diagnose before optimizing.
```

---

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute legal, financial, security, compliance, medical, employment, or other professional advice.

## Product-verification note

Product behavior changes. Current Claude Help Center guidance available on August 3, 2026 states that automatic context management can summarize earlier messages in long conversations when code execution is enabled. Current official documentation controls if product behavior differs from this lesson.
