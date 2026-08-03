# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** In progress — Module 7 is the active module.

## Module thesis

> Troubleshooting is disciplined diagnosis: observe the failure, read its timing and pattern, localize the responsible layer, change the smallest relevant variable, and verify that the repair improves behavior without weakening governance or causing regressions.

```text
Observed underperformance
      ↓
Evidence and symptom timing
      ↓
Failure classification
      ↓
Cheapest relevant test
      ↓
Bounded repair
      ↓
Representative validation
```

---

# Course-aligned roadmap

- [x] [01. Diagnosing Underperforming Prompts & Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [ ] 02. Adjusting Approach from Feedback
- [ ] 03. Optimizing Workflows
- [ ] 04. Module 7 Quiz
  - [ ] Module 7 Quiz
  - [ ] Key Takeaways
- [ ] 05. Module Complete

No later section is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Module 6 to Module 7 bridge

Module 6 established whether a use case should proceed and under what data, feature, policy, ethical, and accountability boundaries.

Module 7 begins when an approved workflow underperforms.

```text
Governed workflow
      ↓
Unexpected or weak result
      ↓
Diagnose the responsible layer
      ↓
Apply the narrowest responsible repair
      ↓
Verify quality, safety, and operational impact
```

Governance remains active. Performance improvements must not weaken data controls, permissions, human-review gates, fairness, disclosure, recourse, or accountability.

---

# Lesson 1 foundation: diagnose before optimizing

Weak output has multiple possible causes.

```text
Output is weak
      ≠
Prompt is automatically the cause
```

The first lesson uses five diagnostic categories.

## 1. Under-specification

**Timing:** Wrong from the first response.

The prompt omitted required context, objective, constraints, evidence boundaries, format, examples, audience, or success criteria.

```text
First response wrong
      →
Check specification first
```

**First repair:** Add only the missing task-contract elements.

## 2. Context overload

**Timing:** The session began well and degraded over time.

The conversation may contain excessive, irrelevant, conflicting, or compressed earlier context. Current Claude guidance states that, when code execution is enabled, automatic context management can summarize earlier messages as a long conversation approaches its context limit.

```text
Started right
+ degraded later
      →
Inspect context before rewriting prompt
```

**First repair:** Restart from a verified summary, remove irrelevant material, and move recurring rules into the correct persistent layer.

## 3. Wrong feature or model

**Pattern:** A specific failure repeats.

Examples include subtle arithmetic errors, missing source access, malformed structured output, shallow analysis, or use of an entry point that lacks the required capability.

```text
Specific repeatable error
      →
Check feature and model fit
```

**First repair:** Use the smallest capability that directly addresses the limitation, such as code execution for deterministic calculations.

## 4. Stale configuration

**Timing:** The workflow used to work but now performs poorly.

Potential drift includes:

- Project instructions;
- knowledge and source versions;
- Skills and dependencies;
- connector scope;
- Memory;
- schemas and templates;
- policy references; and
- human-review processes.

```text
Used to work
      →
Inspect configuration before rewriting prompt
```

**First repair:** Run the Module 5 maintenance lifecycle and regression tests.

## 5. Expectation mismatch

**Pattern:** The requested result remains unavailable after cheaper causes are ruled out.

Examples include exact future predictions, certainty beyond evidence, unavailable source information, unsupported external actions, or final judgments that require non-transferable human authority.

```text
Unavailable requested outcome
      →
Reshape the task
```

**First repair:** Convert the request into a bounded analysis, scenario range, evidence summary, draft, checklist, or human-reviewed decision aid.

---

# Read symptom timing

| Symptom | Primary hypothesis | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract elements |
| Good initially, then degrades | Context overload | Restart or summarize cleanly |
| Specific repeatable error type | Wrong feature or model | Select the correct capability |
| Worked before, now performs poorly | Stale configuration | Inspect and maintain dependencies |
| Still unavailable after other causes are ruled out | Expectation mismatch | Reshape the task |

Timing is evidence, not proof. Confirm the diagnosis with a controlled test.

---

# Cheapest-fix-first diagnostic sequence

```text
1. Prompt specification
2. Conversation context
3. Feature and model fit
4. Maintained configuration
5. Task fit and expectation
```

## Step 1: Re-read the prompt

Check:

- objective;
- context and evidence;
- constraints;
- output format; and
- success criteria.

## Step 2: Inspect context

Check:

- session length and drift;
- irrelevant or conflicting material;
- compressed details that need restatement;
- clean restart requirements; and
- stable information that belongs in a Project, Skill, or instruction.

## Step 3: Check feature and model fit

Check whether the task requires:

- code execution;
- structured extraction;
- connected or uploaded sources;
- a different entry point;
- deeper reasoning; or
- a faster, less expensive route for a simpler stage.

## Step 4: Inspect configuration

Review instructions, knowledge, Skills, connectors, Memory, schemas, templates, review gates, policies, and product changes.

## Step 5: Test task fit

Ask whether the result is knowable, supported by available evidence, technically possible in the selected feature, and appropriate for AI assistance.

The order is deliberate: cheap and common causes come first; the expensive conclusion that the task is impossible comes last.

---

# Minimal reproducible diagnosis

Record:

- expected behavior;
- observed behavior;
- symptom timing;
- exact prompt;
- minimum relevant context;
- model and entry point;
- enabled tools and features;
- configuration version;
- source version;
- repeatability; and
- explicit pass/fail criteria.

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

Changing prompt, model, tools, context, and configuration simultaneously destroys causal evidence.

---

# Worked failure gallery

| Failure | Diagnosis | First repair |
|---|---|---|
| Summary misses key decisions from the first response | Under-specification | Define what counts as key |
| Format degrades during a long conversation | Context overload | Restart from a verified summary or persist the rule |
| Totals are subtly wrong | Wrong feature | Use code execution and deterministic validation |
| A reliable Project now uses outdated language | Stale configuration | Review sources, instructions, Skills, and dependencies |
| User requests next quarter’s exact sales number | Expectation mismatch | Produce ranges, assumptions, drivers, and sensitivity analysis |

---

# Diagnostic decision record

```text
Observed failure:
Expected behavior:
Symptom timing:
Primary hypothesis:
Alternate hypothesis:
Evidence:
Minimal test:
Result:
Selected repair:
Regression checks:
Governance checks:
Rollback condition:
Final disposition:
```

---

# Current module resources

## Course-aligned lesson

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)

## Prompt notebook

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)

## Existing engineering pattern

- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Wrong on first response                  → inspect specification
Started well, then drifted               → inspect context
Specific quantitative or schema failure  → inspect feature or tool fit
Used to work                             → inspect configuration
Exact unavailable outcome                → reshape the task
Strongest model suggested first          → rule out cheaper causes
Many variables changed together          → attribution is lost
Performance fix weakens controls          → reject or redesign
```

For diagnostic scenarios:

1. define expected versus observed behavior;
2. read symptom timing;
3. classify the most likely cause;
4. state the cheapest controlled test;
5. change one variable;
6. compare with a baseline;
7. preserve governance;
8. test representative cases; and
9. keep, revise, revert, or reshape.

---

# Completion criteria

- [x] I completed Diagnosing Underperforming Prompts & Outputs.
- [ ] I completed Adjusting Approach from Feedback.
- [ ] I completed Optimizing Workflows.
- [ ] I can distinguish first-response, degraded-over-time, specific-error, used-to-work, and expectation-mismatch patterns.
- [ ] I can audit a prompt against objective, evidence, constraints, format, and success criteria.
- [ ] I can identify when context needs a clean restart or persistent instruction.
- [ ] I can distinguish feature and model fit from prompt quality.
- [ ] I can inspect stale configuration when a workflow used to work.
- [ ] I can reshape an unrealistic task rather than endlessly tune it.
- [ ] I can create a minimal reproducible case and change one variable at a time.
- [ ] I can validate a repair without weakening governance.
- [ ] I completed the Module 7 quiz and Key Takeaways.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private production prompts, confidential incidents, proprietary logs, credentials, internal connector identifiers, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.

## Product-verification note

Product behavior changes. Current Claude Help Center guidance available on August 3, 2026 states that automatic context management can summarize earlier messages in long conversations when code execution is enabled. Current official documentation controls if product behavior differs from this module.
