# Configuration Maintenance Lifecycle Pattern

## Problem

A configured workspace may continue running after its instructions, sources, Skills, connector permissions, or Memory no longer match the current operating environment.

Because configuration drift often produces plausible output rather than a clear error, teams may keep rewriting prompts instead of repairing the reusable baseline.

## Context

Use this pattern when work depends on:

- Project instructions;
- Project knowledge;
- custom or shared Skills;
- connectors and external permissions;
- Memory or Project continuity;
- recurring templates and procedures; or
- a configured helper that has become an operational dependency.

## Recommended design

```text
Inventory
  ↓
Assign ownership and cadence
  ↓
Review current state against operating reality
  ↓
Classify drift and consequence
  ↓
Edit / replace / disable / revoke / reset / roll back / retire
  ↓
Regression-test
  ↓
Approve and release
  ↓
Monitor and schedule next review
```

## 1. Configuration register

For every material component, record:

- component ID and type;
- purpose;
- owner;
- current version;
- effective date;
- distribution or access model;
- last and next review dates;
- test suite;
- known limitations;
- dependencies;
- rollback, reset, disable, revocation, or retirement path; and
- approval evidence.

## 2. Cadence and event triggers

Use a recurring cadence proportional to change rate and consequence. Add event-triggered reviews after:

- process or policy changes;
- source replacement;
- Skill updates;
- connector or permission changes;
- team turnover;
- product or model changes;
- repeated output regression;
- incidents; or
- growth into shared infrastructure.

## 3. Component-specific review

### Instructions

Check terminology, process, format, evidence behavior, reviewers, and conflicts.

### Knowledge

Check authority, effective dates, duplicates, supersession, scope, sensitivity, and refresh type.

### Skills

Check owner, distribution method, version, trigger description, dependencies, enabled audience, and golden-output tests.

### Connectors

Check identity, source scope, tools, permission level, administrator approval, usage need, failures, offboarding, and revocation.

### Memory

Check accuracy, relevance, scope, sensitivity, and whether material information belongs in knowledge, instructions, or a system of record instead.

## 4. Maintenance action selection

| Condition | Action |
|---|---|
| Small isolated defect | Edit and retest |
| Source replaced | Replace, relabel history, and rerun coverage tests |
| Procedure changed | Update Skill, version, and regression-test |
| Access excessive or unused | Reduce scope, disable, or revoke |
| Memory entry stale | Correct or delete |
| Memory broadly misleading | Preserve approved context, then consider reset |
| New version regresses | Roll back |
| Workspace no longer needed | Retire and revoke dependencies |

## 5. Destructive-action safeguard

Before reset, deletion, revocation, or retirement:

1. identify approved information or evidence that must be retained;
2. export or archive it through an approved path;
3. confirm owner approval;
4. document irreversibility and downstream effects;
5. execute the change; and
6. validate the resulting state.

```text
Reset available
      ≠
Reset appropriate
```

## 6. Regression verification

After material changes, test:

- normal cases;
- missing and conflicting evidence;
- current terminology and output format;
- superseded-source exclusion;
- Skill triggering and golden outputs;
- permitted and denied connector actions;
- stale-Memory removal;
- bypass attempts;
- rollback behavior; and
- retirement or revocation effects.

## Controls

- configuration register;
- owner and approver;
- recurring and event-triggered review;
- source and capability registers;
- version history;
- representative and adversarial tests;
- rollback and reset safeguards;
- access recertification;
- release evidence;
- monitoring; and
- retirement process.

## Failure modes

### Prompt churn

A team repeatedly changes prompts while the persistent configuration remains stale.

**Repair:** inspect the reusable baseline before changing one-time wording.

### Unversioned repair

A configuration is edited directly without recording the prior state.

**Repair:** version material changes and preserve a rollback path.

### Silent Skill divergence

Different users run different copies or versions of a procedure.

**Repair:** document distribution method, current version, and enabled audience.

### Memory accumulation

More continuity is retained than can be reliably reviewed.

**Repair:** curate entries and move authoritative information to the correct system.

### Ceremonial review

A monthly review is scheduled but no result, owner, or remediation is recorded.

**Repair:** require a completed checklist, disposition, evidence, and next review date.

## Compact decision rule

> Treat every configuration as a versioned operational asset: review it on cadence and after material events, repair the smallest affected component, preserve approved information before destructive changes, regression-test the result, and retire what no longer serves the workflow.

## Review checklist

- Is every component owned and versioned?
- Do instructions match the current process?
- Is knowledge current, authoritative, and deduplicated?
- Are Skills on the intended version and distribution path?
- Are connector permissions still required and minimal?
- Is Memory accurate, relevant, and appropriately scoped?
- Are reset, rollback, revocation, and retirement paths documented?
- Were destructive changes preceded by preservation and approval?
- Did regression tests pass?
- Is the next review scheduled?