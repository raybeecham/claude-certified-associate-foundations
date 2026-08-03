# Module 5 Prompt Notebook: Maintaining Configurations

Use fictional, synthetic, public, or explicitly authorized configuration descriptions. Do not place credentials, private connector identifiers, confidential sources, or personal Memory exports in this notebook.

## 1. Configuration inventory

```text
Create a maintenance inventory for this configured workspace:
[description]

For each Project instruction, knowledge source, Skill, connector, and Memory category, record:
- owner;
- purpose;
- version;
- effective date;
- last review;
- next review;
- tests;
- known limitations;
- rollback, reset, disable, revocation, or retirement path.
```

## 2. Review-cadence design

```text
Recommend a recurring and event-triggered maintenance cadence for:
[configuration]

Consider:
- rate of process change;
- stakes;
- source update frequency;
- connector permissions;
- Skill distribution;
- team turnover;
- operational dependency; and
- consequence of silent drift.
```

## 3. Instruction-drift audit

```text
Compare these standing instructions with the current process:
[instructions]
[current process]

Identify:
- obsolete terminology;
- renamed metrics;
- changed output formats;
- outdated reviewers;
- missing evidence rules;
- conflicts;
- instructions that belong elsewhere; and
- regression tests to run after repair.
```

## 4. Knowledge-maintenance review

```text
Review this Project knowledge inventory:
[inventory]

Flag:
- superseded documents;
- duplicates;
- missing owners;
- unclear authority;
- stale dates;
- out-of-scope sources;
- static snapshots assumed to be live;
- historical sources presented as current; and
- missing replacement triggers.
```

## 5. Skill-version review

```text
Create a Skill maintenance record for:
[Skill description]

Include:
- owner;
- distribution method: Anthropic, organization-provisioned, directly shared, directory-installed, or personal upload;
- current version;
- enabled audience;
- trigger description;
- dependencies;
- golden-output tests;
- observed drift;
- update method;
- rollback or disable path.
```

## 6. Prompting problem or maintenance problem?

```text
A recurring workflow is producing this regression:
[problem]

Classify likely causes across:
- current request;
- persistent instructions;
- Project knowledge;
- Skill version or trigger;
- connector capability or access;
- Memory;
- deterministic rule;
- model or product change.

Recommend the smallest diagnostic sequence before changing the prompt.
```

## 7. Memory lifecycle review

```text
Review these fictional Memory categories:
[entries or categories]

Classify each as:
- retain;
- correct;
- delete;
- move to Project knowledge;
- move to standing instructions;
- move to a system of record;
- export before change;
- candidate for reset only if selective repair is insufficient.

Explain the authority and staleness risk.
```

## 8. Reset decision

```text
Assess whether this Memory state should be selectively repaired or fully reset:
[description]

Consider:
- number of stale entries;
- ability to identify them reliably;
- downstream risk;
- approved information that must be preserved;
- export or backup plan;
- irreversibility of reset; and
- validation after rebuilding.
```

## 9. Connector access recertification

```text
Review this connector inventory:
[inventory]

Check:
- connected identity;
- business need;
- read, draft, write, send, update, and delete tools;
- source scope;
- administrator approval;
- role changes;
- unused access;
- offboarding;
- revocation path; and
- boundary tests.
```

## 10. Degraded Project investigation

```text
A recurring report Project now has:
- an old metric name in instructions;
- two template versions;
- a Skill using an old section order;
- a stale stakeholder Memory entry.

Create:
1. root-cause table;
2. repair sequence;
3. affected tests;
4. rollback options;
5. release evidence; and
6. next review date.
```

## 11. Configuration change record

```text
Write a configuration change record for:
[change]

Include:
- change ID;
- component;
- old and new version;
- reason;
- affected workflows;
- source or access changes;
- test results;
- reviewer and approver;
- rollout date;
- rollback path;
- limitations; and
- next review.
```

## 12. Maintenance test suite

```text
Create representative and adversarial tests for this configuration:
[configuration]

Cover:
- normal task;
- missing evidence;
- conflicting sources;
- obsolete terminology;
- superseded file retrieval;
- Skill trigger and output;
- revoked connector access;
- stale Memory;
- attempted bypass;
- rollback verification; and
- retirement behavior.
```

## 13. Retirement plan

```text
Create a retirement plan for this unused or replaced Project:
[description]

Include:
- owner approval;
- final data and source disposition;
- connector revocation;
- Skill dependencies;
- Memory or continuity handling;
- access removal;
- archive labeling;
- audit evidence; and
- user communication.
```

## 14. Oral certification drill

```text
Give me five short scenarios about configuration drift.
For each, ask me to identify:
- affected component;
- likely cause;
- maintenance action;
- destructive-action safeguard;
- required tests; and
- owner.

Do not reveal the answers until I respond.
```