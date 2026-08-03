# Lesson 5: Maintaining Configurations

## Overview

Configurations are living assets. Instructions, Project knowledge, Skills, connectors, and Memory can all become stale, overbroad, duplicated, or inconsistent.

```text
Configured baseline
      ↓
Repeated use
      ↓
Process, source, access, and personnel changes
      ↓
Configuration drift
      ↓
Scheduled review, repair, rollback, or retirement
```

> Configuration maintenance is the work that keeps a reusable baseline accurate after the environment around it changes.

This lesson develops five capabilities:

1. setting a review cadence for active configurations;
2. detecting instruction, source, Skill, connector, and Memory drift;
3. versioning and testing changes;
4. choosing edit, replace, reset, rollback, or retire; and
5. diagnosing degraded output as a configuration problem rather than repeatedly rewriting prompts.

---

# Plain-English explanation

A Project may work well when first created and still degrade later without displaying an error.

Examples:

- an instruction references a renamed metric;
- Project knowledge contains both current and obsolete templates;
- a shared procedure changes but a personal copy does not;
- connector permissions remain after a user changes roles;
- Memory preserves a stakeholder or preference that is no longer valid; or
- a review gate remains in the instructions but no qualified reviewer is assigned.

```text
No visible error
      ≠
Configuration still correct
```

---

# One analogy: maintaining a navigation chart

A navigation chart can be perfectly drawn and still become unsafe when channels move, hazards change, or markers are replaced.

The fix is not to tell the navigator to “try harder.” The chart must be reviewed, corrected, versioned, and redistributed.

Claude configurations work the same way. Instructions, sources, procedures, access, and continuity must be checked against the current operating environment.

---

# Review cadence

Every active configuration should have an owner and scheduled review.

A practical default for an actively used Project is a monthly review, adjusted for the rate and consequence of change.

| Change profile | Example cadence |
|---|---|
| High-change or high-consequence | Weekly or event-triggered review |
| Active recurring Project | Monthly review |
| Stable reference workspace | Quarterly review |
| Archived or historical Project | Annual review or retirement |

Review immediately after material events such as:

- policy or process change;
- source replacement;
- Skill update;
- connector permission change;
- team or stakeholder change;
- model or product migration;
- repeated output regression;
- security or privacy incident; or
- expansion from personal helper to shared operational dependency.

```text
Scheduled cadence
+ event-triggered review
=
maintained configuration
```

---

# Configuration inventory

Maintain a register for each material configuration component.

| Component | Owner | Version | Effective date | Last review | Next review | Test set | Rollback or reset path |
|---|---|---|---|---|---|---|---|
| Project instructions | Project owner | PI-4 | 2026-07-01 | 2026-08-01 | 2026-09-01 | Instruction regression | Restore PI-3 |
| Knowledge source | Policy owner | v3.2 | 2026-07-15 | 2026-07-15 | On change | Source coverage | Replace with v3.1 |
| Skill | Process owner | SR-2.1 | 2026-07-20 | 2026-08-01 | 2026-09-01 | Golden outputs | Disable or restore prior package |
| Connector | System owner | C-5 | 2026-06-01 | 2026-08-01 | 2026-11-01 | Boundary tests | Revoke or disable |
| Memory | User or Project owner | Reviewed state | Continuous | 2026-08-01 | 2026-09-01 | Accuracy review | Edit, delete, pause, or reset |

---

# Maintaining instructions

Check whether standing instructions still match:

- current terminology;
- current process stages;
- current output format;
- current review and approval roles;
- current evidence rules;
- current connector capabilities; and
- current organizational policy.

Run the existing positive, missing-evidence, conflict, bypass, unrelated-task, and regression tests after any material instruction change.

```text
Instruction changed
      ↓
Version recorded
      ↓
Representative tests rerun
      ↓
Approval
      ↓
Release or rollback
```

---

# Maintaining knowledge

Review the knowledge base for:

- superseded documents;
- duplicates;
- missing owners;
- unclear authority;
- stale effective dates;
- out-of-scope material;
- excessive sensitivity;
- broken links or access;
- static uploads treated as live; and
- historical sources presented as current.

Use one controlling version when possible. Retain history only when the use case requires it and label it explicitly.

```text
New controlling source
      ↓
Remove or relabel prior source
      ↓
Update source register
      ↓
Run coverage and conflict tests
```

---

# Skills versioning

Skills may be maintained through different ownership paths.

- Anthropic-built Skills are maintained by Anthropic.
- Organization-provisioned Skills are maintained by organization owners.
- Skills shared directly with recipients can update automatically for those recipients when the owner updates the shared Skill.
- A personally uploaded custom Skill remains the owner's copy and must be edited, replaced, or re-uploaded by that owner when the procedure changes.

Do not assume every enabled Skill is on the same version.

For each Skill, track:

- owner;
- purpose;
- current version;
- distribution method;
- enabled audience;
- trigger description;
- dependencies;
- golden-output tests;
- last successful test;
- known limitations; and
- rollback or disable path.

```text
Output drifts slightly every run
      ≠
Prompting problem by default
```

It may indicate an outdated Skill, changed dependency, poor trigger description, or conflicting configuration.

---

# Memory lifecycle

Treat Memory as reviewed continuity, not an unquestioned archive.

Maintenance actions include:

- review entries;
- add missing stable context explicitly;
- correct inaccurate entries;
- delete stale or inappropriate entries;
- export Memory before major migration or reset;
- pause Memory when continuity should temporarily stop; and
- reset Memory when accumulated state is materially misleading and selective repair is not sufficient.

Current product behavior may differ by plan and rollout. Memory reset is destructive and cannot be undone, so export or otherwise preserve approved information before resetting when appropriate.

```text
More remembered context
      ≠
Better continuity
```

Accuracy, relevance, scope, and permission matter more than volume.

Memory should not be the sole location for a material constraint, approved decision, or required workflow state. Stable authoritative content belongs in Project knowledge, instructions, or a system of record as appropriate.

---

# Connectors and access maintenance

Review:

- connected identity;
- enabled tools;
- source scope;
- read and write permissions;
- administrator approval;
- usage need;
- offboarding status;
- unsupported actions;
- failure trends; and
- revocation path.

Remove access that is no longer required. Revalidate capabilities after connector, plan, administrator, or permission changes.

---

# Worked example: degraded report Project

A recurring reporting Project begins producing subtly incorrect output.

The review finds:

1. a standing instruction still uses the old metric name;
2. Project knowledge contains two versions of the report template;
3. a custom Skill still formats the retired section order; and
4. Memory includes a stakeholder who has left the program.

The repair is:

```text
Update and version the instruction
      ↓
Remove or archive the obsolete template
      ↓
Replace and regression-test the Skill
      ↓
Delete the stale Memory entry
      ↓
Rerun representative reports
```

The team does not need a more elaborate one-time prompt. It needs a corrected operating baseline.

---

# Maintenance decision model

| Condition | Appropriate action |
|---|---|
| Minor isolated error | Edit and retest |
| Controlling source replaced | Replace source and rerun coverage tests |
| Skill procedure changed | Update or re-upload, version, and regression-test |
| Access no longer needed | Revoke or disable connector |
| Memory entry stale | Edit or delete |
| Memory broadly misleading | Export approved context, then reset if justified |
| Change causes regression | Roll back to last approved version |
| Workspace no longer needed | Retire and revoke access |

---

# Configuration maintenance protocol

```text
1. Inventory instructions, knowledge, Skills, connectors, and Memory
2. Assign owners, versions, review dates, and tests
3. Review on cadence and after material events
4. Compare configuration with current process, sources, people, and access
5. Classify drift and downstream impact
6. Edit, replace, disable, revoke, reset, roll back, or retire
7. Rerun representative and adversarial tests
8. Obtain approval for material changes
9. Release and monitor
10. Record the result and next review date
```

---

# Exam lens

```text
Output degrades without prompt change     → inspect configuration drift
Old metric remains in every report        → update standing instruction
Two template versions conflict            → retain one controlling source
Personal Skill uses old procedure          → update or re-upload and retest
Shared Skill owner publishes an update     → recipients receive updated shared version
Former stakeholder persists in Memory      → edit or delete stale entry
Memory broadly misleads future work        → export, then consider irreversible reset
Unused connector remains authorized        → revoke or disable
Change breaks known cases                  → roll back to approved version
```

For maintenance scenarios:

1. identify the configuration component;
2. determine ownership and distribution model;
3. compare it with the current operating reality;
4. inspect source, permission, and version drift;
5. choose the smallest sufficient repair;
6. preserve approved information before destructive actions;
7. rerun regression tests;
8. document approval and release;
9. monitor for recurrence; and
10. define the next review date.

---

# Short recap

```text
1. Configurations silently decay.
2. Active Projects need recurring and event-triggered reviews.
3. Instructions must follow current process and terminology.
4. Knowledge must be current, authoritative, and deduplicated.
5. Skill maintenance depends on ownership and distribution method.
6. Personal custom Skills require owner-managed updates.
7. Memory should be reviewed, corrected, exported, or reset when justified.
8. Least privilege requires connector review and revocation.
9. Material changes require versioning and regression tests.
10. Degraded output may require maintenance, not a better prompt.
```

## Educational-use notice

This lesson is an unofficial educational resource. Product behavior and availability can change. Verify current official Anthropic documentation and organizational policy before relying on implementation-specific behavior.