# Skill Trust and Feature-Risk Pattern

## Problem

A Skill, connector, tool, integration, or execution feature is enabled because it is useful, internal, or easy to access, without a structured review of its source, effective reach, or proportionality to the task.

## Context

Use this pattern when a workflow introduces:

- a custom or shared Skill;
- organization-provisioned automation;
- executable scripts or dependencies;
- code execution;
- connector or file access;
- external actions;
- persistent memory or retained outputs; or
- a third-party integration.

## Recommended design

```text
Define the task and environment
      ↓
Establish source and ownership
      ↓
Inspect instructions, scripts, dependencies, and files
      ↓
Enumerate session permissions and effective reach
      ↓
Test proportionality and least privilege
      ↓
Assess data, actions, policy, and approval authority
      ↓
Enable / escalate / decline
      ↓
Monitor, re-review, disable, or retire
```

## Source review

Record:

- publisher;
- accountable owner;
- distribution path;
- version;
- approval evidence;
- update mechanism;
- support path;
- integrity or provenance evidence; and
- review date.

```text
Internal
      ≠
Vetted
```

## Effective reach

The relevant permission boundary is the environment in which the capability runs.

```text
Capability instructions
      ×
Available files, connectors, tools, and actions
      =
Effective reach
```

Enumerate read, write, execute, send, publish, modify, delete, persist, export, and network capabilities.

## Bundle inspection

Inspect:

- instructions;
- scripts;
- dependencies;
- bundled files;
- tool and connector references;
- external calls;
- file paths;
- retention and logging;
- error behavior; and
- behavior beyond the stated purpose.

## Appropriateness and proportionality

Ask whether the feature is the smallest capability that meets the approved need.

```text
Useful
      ≠
Necessary
      ≠
Proportionate
```

Narrow permissions, remove tools, isolate the environment, or select a simpler mechanism when possible.

## Outcomes

### Enable

Source, reach, task fit, policy, testing, monitoring, and disable paths are clear.

### Escalate

The capability may be useful, but specialist review or higher authority is required.

### Decline

The source cannot be established, access is disproportionate, policy conflicts exist, or review cannot make the use responsible.

## Controls

- least privilege;
- data minimization;
- approved environment;
- functional and security tests;
- boundary and adversarial tests;
- human approval before consequential actions;
- monitoring and logging;
- version pinning where appropriate;
- disable and rollback paths; and
- event-triggered re-review.

## Re-review triggers

- new version;
- changed publisher or owner;
- changed scripts or dependencies;
- added connector or tool;
- broader data classification;
- new external action;
- policy change;
- changed permissions;
- incident or unexpected behavior; or
- expansion to a new audience or use case.

## Failure modes

| Failure | Repair |
|---|---|
| Trust based only on name or publisher | Inspect bundle and current review evidence |
| Internal Skill treated as automatically safe | Require owner, scope, tests, and policy alignment |
| Permission review ignores session environment | Map effective reach across all available tools and data |
| Useful output treated as safety evidence | Test behavior, boundaries, side effects, and failure modes separately |
| User approves beyond authority | Escalate to the authorized owner or risk function |
| No containment path | Define disable, revoke, and rollback before enablement |
| Review never repeated | Trigger re-review after material changes |

## Compact decision rule

> Establish who provides the capability, inspect what it contains, map what it can reach in the real environment, confirm that reach is proportionate to the task, and choose enable, escalate, or decline under the correct authority.
