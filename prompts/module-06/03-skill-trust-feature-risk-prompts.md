# Module 6 Prompt Notebook: Skill Trust and Feature-Level Risk

Use fictional, synthetic, public, or explicitly authorized descriptions. Do not include proprietary Skill bundles, confidential code, credentials, private connector identifiers, or restricted data.

## 1. Source check

```text
Evaluate the source trust of this Skill:
[Skill description]

Identify:
- publisher;
- owner;
- distribution path;
- current version;
- approval evidence;
- update path;
- support path;
- unresolved provenance questions; and
- preliminary trust level.

Do not treat `internal` as equivalent to `vetted`.
```

## 2. Bundle audit

```text
Review this Skill bundle inventory:
[instructions, scripts, dependencies, files]

Flag:
- executable code;
- external calls;
- unnecessary dependencies;
- tool references;
- file access;
- actions beyond the stated purpose;
- hidden retention or logging;
- obsolete policy assumptions;
- prompt-injection exposure; and
- items requiring specialist review.
```

## 3. Effective reach map

```text
The Skill will run in this environment:
[files, connectors, tools, code execution, data, actions]

Create an effective-reach map covering:
- readable data;
- writable data;
- executable code;
- external systems;
- create/update/send/publish/delete actions;
- retained outputs;
- secrets exposure;
- sensitive-data categories;
- likely blast radius; and
- access that is unnecessary for the task.
```

## 4. Proportionality test

```text
Task:
[task]

Skill capability and access:
[capability]

Determine whether the Skill's reach is proportionate.
Recommend:
- retain current design;
- narrow permissions;
- remove connectors;
- replace with instructions;
- replace with a smaller Skill or tool;
- isolate in a lower-trust environment; or
- decline.
```

## 5. Enable, escalate, or decline

```text
Classify this Skill decision as:
- Enable;
- Escalate; or
- Decline.

Evaluate:
1. Source
2. Reach
3. Appropriateness
4. Data sensitivity
5. External actions
6. User approval authority
7. Testing evidence
8. Monitoring and disable path

Name the load-bearing concern and provide a concise decision rationale.
```

## 6. Internal Skill review

```text
A Skill was built by another internal team:
[description]

Create a sister-team software review covering:
- owner;
- purpose;
- exact access;
- justification for access;
- scripts and dependencies;
- current policy basis;
- tests;
- known limitations;
- distribution and update behavior;
- rollback;
- requested changes before use; and
- review owner.
```

## 7. Skill trust register

```text
Create a Skill trust register with:
- Skill ID;
- version;
- publisher;
- owner;
- distribution path;
- purpose;
- bundle contents;
- runtime requirements;
- effective reach;
- data classification;
- external actions;
- review status;
- tests;
- limitations;
- monitoring;
- disable or rollback path;
- approval authority; and
- next review date.
```

## 8. Feature-risk generalization

```text
Apply the same source, reach, and appropriateness review to this feature:
[connector, tool, integration, code execution, Memory, or external action]

Determine:
- provider;
- access;
- execution;
- persistence;
- data movement;
- side effects;
- approval boundary;
- monitoring;
- revocation; and
- enable/escalate/decline outcome.
```

## 9. Boundary test suite

```text
Create tests for this Skill:
[Skill and environment]

Include:
- expected task;
- irrelevant task;
- denied file;
- sensitive file;
- missing connector;
- unexpected tool call;
- attempted external action;
- malicious source instruction;
- stale dependency;
- changed policy;
- revoked access; and
- disable/rollback verification.
```

## 10. Least-privilege redesign

```text
Redesign this Skill deployment for least privilege:
[current design]

Reduce:
- files;
- directories;
- connectors;
- write permissions;
- external actions;
- retained outputs;
- enabled audience; and
- runtime duration.

Preserve only what is necessary for the approved task.
```

## 11. Trust claim audit

```text
Audit these claims:
[claims such as `internal`, `approved`, `safe`, `read-only`, `no data leaves`]

For each claim, identify:
- evidence required;
- evidence present;
- unsupported assumptions;
- verification owner; and
- corrected wording.
```

## 12. Worked two-Skill comparison

```text
Compare:
A. A documented first-party formatter with task-matched access.
B. An unknown analytics Skill with scripts and broad session reach.

For each, assess source, reach, appropriateness, data risk, tests, approval authority, and outcome.
```

## 13. Governance decision record

```text
Write a decision record for this Skill review:
[review evidence]

Include:
- proposed use;
- data and environment;
- source findings;
- bundle findings;
- effective reach;
- proportionality;
- residual risk;
- outcome;
- required conditions;
- approver;
- monitoring;
- rollback; and
- re-review triggers.
```

## 14. Oral certification drill

```text
Give me six brief scenarios involving:
- first-party Skill;
- unknown third-party Skill;
- unvetted internal Skill;
- excessive connector reach;
- user without approval authority; and
- feature that is more capable than necessary.

Ask me to choose Enable, Escalate, or Decline and identify the load-bearing trust concern. Grade each answer.
```
