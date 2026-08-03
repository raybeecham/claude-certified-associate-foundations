# Connector and Knowledge Boundary Pattern

## Problem

Teams connect Claude to external systems or upload files without defining what the source can be used for, what actions the connector supports, or how stale and conflicting material is handled.

This creates three recurring errors:

1. access is mistaken for authority;
2. connector names are mistaken for capability contracts; and
3. uploaded knowledge becomes an unmanaged collection of duplicate or superseded files.

## Context

Use this pattern when a workflow depends on:

- email, calendar, cloud storage, repositories, or enterprise systems;
- Model Context Protocol connectors;
- uploaded Project files;
- synced external documents;
- connector-assisted drafting or external actions; or
- maintained knowledge that changes over time.

## Forces

The design must balance:

- useful access;
- least privilege;
- source authority;
- freshness;
- capability differences;
- user identity and permissions;
- workflow speed;
- human approval;
- change management; and
- troubleshootability.

## Recommended design

```text
Define purpose
      ↓
Select minimum sources and connectors
      ↓
Record identity, scope, and capabilities
      ↓
Classify source authority and refresh behavior
      ↓
Separate retrieve, draft, approve, and execute
      ↓
Test boundaries and failure modes
      ↓
Monitor, update, revoke, or retire
```

## 1. Connector contract

For each connector, record:

- approved business purpose;
- owner;
- connected identity;
- permitted accounts, tenants, folders, repositories, or mailboxes;
- read capabilities;
- draft capabilities;
- write and external-action capabilities;
- unsupported actions;
- administrator dependencies;
- data sensitivity;
- approval boundaries;
- logging and retention;
- review date; and
- revocation process.

```text
Connector installed
      ≠
Connector enabled
      ≠
User authenticated
      ≠
Source accessible
      ≠
Action authorized
```

## 2. Source contract

For every connected or uploaded source, record:

- source ID;
- owner;
- authority;
- effective date;
- review or expiration date;
- scope;
- sensitivity;
- version;
- refresh type;
- conflicts;
- replacement; and
- permitted use.

```text
Accessible source
      ≠
Authorized source
      ≠
Controlling source
      ≠
Current source
```

## 3. Stage separation

Expose consequential transitions as separate stages.

```text
Retrieve
  ↓
Read
  ↓
Analyze
  ↓
Draft
  ↓
Human review
  ↓
Approval
  ↓
Controlled execution, if supported
```

A connector may support only a subset of these stages. Do not redesign the boundary through optimistic prompting.

## 4. Capability-aware troubleshooting

Classify failures in this order:

1. installation or organization enablement;
2. authentication;
3. permission;
4. source scope;
5. tool loading;
6. unsupported capability;
7. stale or missing source;
8. external-system failure; and
9. product defect.

Do not route an unsupported action as a software bug.

## 5. Uploaded-knowledge maintenance

For static uploads:

- assign an owner;
- record the effective version;
- establish a replacement trigger;
- remove or archive superseded copies;
- run regression questions after change; and
- retain historical material only when its status is explicit.

For synced sources:

- monitor upstream changes;
- verify that the upstream source remains controlling;
- review access changes; and
- retest material workflows after significant updates.

## 6. Least privilege

Use only the connector and source scope required by the workflow.

Separate:

- read access;
- draft creation;
- write or update access;
- send or publish authority;
- deletion rights; and
- administrative control.

Human approval should precede consequential or irreversible actions.

## Controls

- connector capability register;
- source register;
- source-authority order;
- duplicate and supersession checks;
- permission review;
- approved installation path;
- successful and denied test cases;
- external-action approval;
- audit evidence;
- offboarding and revocation; and
- configuration review cadence.

## Failure modes

### Capability by association

The workflow assumes every mail connector can send or every storage connector can update.

**Repair:** document exact tools and permissions.

### Access equals authority

Retrieved content is accepted without checking ownership, version, or scope.

**Repair:** classify the source before using it.

### File accumulation

Project knowledge contains several unlabeled versions of the same document.

**Repair:** maintain one controlling version and explicitly archive history.

### Everything connected

All available connectors are loaded for convenience.

**Repair:** select the minimum relevant set and review tool overhead and access.

### Boundary failure mislabeled

An unsupported action is treated as a defect.

**Repair:** run the capability-aware troubleshooting sequence.

### Approval collapsed into execution

A draft or recommendation directly triggers an external side effect.

**Repair:** add a qualified human gate before the controlled action.

## Trade-offs

A smaller connector and source set may require more deliberate selection, but it reduces permission exposure, retrieval noise, context overhead, and ambiguity.

Maintaining capability and source registers adds governance work, but makes failures easier to diagnose and workflows easier to audit.

## Compact decision rule

> Connect only what the workflow needs, document exactly what each connector can do, classify every source by authority and freshness, and place approval before external consequence.

## Review checklist

- Is the connector approved?
- Is the correct identity connected?
- Is the permission scope minimal?
- Are read, draft, write, send, and delete capabilities explicit?
- Are unsupported actions documented?
- Are sources current, authoritative, and in scope?
- Are duplicate and superseded files removed or labeled?
- Are synced and static sources maintained differently?
- Are human approvals placed before consequential actions?
- Are failure routing, revocation, and review cadence defined?
