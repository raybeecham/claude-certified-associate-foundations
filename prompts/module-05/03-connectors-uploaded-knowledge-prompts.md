# Module 5 Prompt Notebook: Connectors and Uploaded Knowledge

Use fictional, synthetic, public, or explicitly authorized source descriptions. Do not place credentials, private connector identifiers, confidential files, or nonpublic records in this notebook.

## 1. Connector purpose contract

```text
I am considering a connector for this recurring workflow:
[workflow]

Create a connector purpose contract with:
- business purpose;
- intended users;
- required source systems;
- minimum read capabilities;
- any required draft or write capabilities;
- prohibited actions;
- data sensitivity;
- human approval gates;
- owner;
- review cadence; and
- revocation conditions.

Prefer the least-privileged design.
```

## 2. Capability register

```text
For the following connector description, create a capability register:
[description]

Separate:
- search;
- read;
- attachment access;
- draft;
- create;
- update;
- send or publish;
- delete;
- unsupported or unknown actions;
- permission dependencies; and
- required human approval.

Do not infer capabilities that are not stated.
```

## 3. Access versus authority

```text
Review these retrieved sources:
[source list]

For each, classify:
- accessible;
- permitted for this task;
- authoritative, advisory, historical, draft, or superseded;
- current or stale;
- within scope or outside scope;
- safe to cite or requires clarification.

Explain why access alone does not establish authority.
```

## 4. Read-draft-approve-execute map

```text
Map this connector-assisted workflow into atomic stages:
[workflow]

Use these stage types:
- retrieve;
- read;
- analyze;
- draft;
- review;
- approve;
- execute external action;
- record state.

For each stage, name:
- owner;
- connector/tool capability;
- evidence;
- validation;
- approval boundary; and
- failure route.
```

## 5. Connector troubleshooting classifier

```text
A connector did not produce the expected result:
[symptoms]

Classify the most likely failure category:
- installation or enablement;
- authentication;
- permission;
- source scope;
- unsupported capability;
- connector not loaded in the conversation;
- missing or stale source;
- probable product defect.

List the minimum checks needed before escalation.
```

## 6. Approved installation-path review

```text
Design an installation-path checklist for a managed organization.

Include:
- approved connector directory or catalog;
- administrator enablement;
- vendor and connector identity verification;
- requested permissions;
- organization account versus personal account;
- test user;
- owner;
- rollback or disable path; and
- evidence of approval.
```

## 7. Uploaded knowledge register

```text
Create a knowledge-source register for these uploaded files:
[file descriptions]

Include:
- source ID;
- title;
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
```

## 8. Duplicate-version audit

```text
The Project contains these versions of a policy:
[version list]

Determine:
- which version appears controlling;
- which are duplicates;
- which are historical or superseded;
- what authority is still unclear;
- what should be removed, archived, or relabeled; and
- which regression questions should be rerun.

Do not silently choose a controlling source when the evidence is insufficient.
```

## 9. Synced versus static source plan

```text
Classify each source as:
- synced external document;
- static upload;
- live connector retrieval;
- historical archive.

For each, define:
- freshness check;
- owner;
- review cadence;
- replacement or invalidation method;
- failure signal; and
- downstream tests after change.
```

## 10. Least-privilege connector design

```text
Given this workflow and candidate connector set:
[workflow and connectors]

Recommend the minimum connector set and permission scope.
Identify:
- unnecessary connectors;
- excessive read scope;
- write permissions that are not required;
- sensitive data exposure;
- approval gates; and
- revocation triggers.
```

## 11. Conflict-handling design

```text
Two connected or uploaded sources disagree:
[source A]
[source B]

Create a conflict record with:
- exact conflicting claims;
- authority;
- scope;
- effective date;
- version;
- likely supersession;
- current decision impact;
- owner for resolution; and
- interim uncertainty statement.
```

## 12. Connector boundary test suite

```text
Create representative and adversarial tests for this connector:
[connector contract]

Include:
- successful search;
- permitted read;
- denied record;
- out-of-scope source;
- unsupported action;
- stale or missing item;
- conflicting sources;
- wrong account;
- disconnected connector;
- revoked access; and
- attempted external action without approval.
```

## 13. Uploaded-knowledge maintenance review

```text
Run a maintenance review of this Project knowledge inventory:
[inventory]

Check for:
- stale files;
- missing owners;
- duplicate versions;
- superseded documents;
- unclear authority;
- excessive sensitivity;
- unrelated sources;
- static files assumed to be live;
- missing review dates; and
- missing regression tests.
```

## 14. Operational failure routing

```text
Create a routing table for connector failures.

Distinguish issues owned by:
- user configuration;
- organization administrator;
- source-system owner;
- identity and access team;
- connector provider;
- Claude product support; and
- workflow owner.

State the evidence required before routing each issue.
```

## 15. Oral certification drill

```text
Ask me ten short scenario questions about connectors and uploaded knowledge.

Test whether I can:
- distinguish access from authority;
- identify connector capability boundaries;
- separate read, draft, approve, and execute;
- apply least privilege;
- diagnose connector failures;
- curate uploaded knowledge;
- handle duplicates and superseded sources;
- distinguish synced from static sources;
- retain human approval; and
- define maintenance ownership.

After each answer, give a concise correction and the governing rule.
```
