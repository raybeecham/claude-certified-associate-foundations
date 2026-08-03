# Lesson 3: Skill Trust and Feature-Level Risk

## Overview

A Skill is a software-like capability package. It can contain instructions, scripts, and supporting resources, and it may execute within a session that already has access to files, connectors, tools, and data.

That means the relevant governance question is not merely:

```text
Do I trust Skills in general?
```

It is:

```text
Do I understand this Skill,
what it can reach in this environment,
and whether that reach is proportionate to the task?
```

> The practical response to feature risk is neither blind trust nor blanket prohibition. It is a repeatable source, reach, and appropriateness review before enablement.

---

# Plain-English explanation

A Skill can improve consistency and speed by giving Claude a repeatable procedure. That same mechanism can introduce risk when the Skill includes unreviewed instructions, executable scripts, unnecessary dependencies, or behavior that reaches beyond its stated purpose.

A Skill does not become trustworthy merely because:

- it has a useful name;
- it came from another internal team;
- it worked once in a low-risk test;
- it is easy to enable; or
- its output looks polished.

```text
Available
      ≠
Approved
      ≠
Vetted
      ≠
Appropriate for this task
```

---

# One analogy: installing workplace software

Before installing software on a work machine, a responsible user asks:

- Who published it?
- What does it install?
- What data or systems can it access?
- Does it need that access?
- Is it approved for this environment?
- How can it be disabled or removed?

A Skill should receive the same treatment.

```text
Skill bundle        → software package
Session access      → runtime permissions
Task purpose        → business justification
Enablement decision → software approval decision
```

---

# Why untrusted Skills create risk

Skills may include:

- instructions that redirect Claude's behavior;
- scripts such as Python, shell, or JavaScript;
- bundled templates and files;
- dependencies;
- procedures that invoke available tools;
- assumptions about data handling; and
- hidden or outdated workflow rules.

A malicious or poorly designed Skill could:

- mishandle sensitive data;
- inspect more files than necessary;
- use connectors beyond the stated task;
- execute unsafe or unnecessary code;
- produce outputs based on obsolete policy;
- create unintended external actions;
- increase prompt-injection exposure; or
- undermine existing instructions and controls.

```text
Helpful procedure
      +
Broad runtime reach
      =
Potentially large blast radius
```

---

# The three trust checks

## 1. Source

Ask:

- Who created or published the Skill?
- Is the publisher identifiable?
- Is the Skill Anthropic-provided, organization-provisioned, team-shared, personally uploaded, or third-party?
- Has an authorized reviewer approved it?
- Is there a named owner and support path?
- Is the version current?
- Can the source and integrity of the bundle be established?

### Lower-risk starting points

- Anthropic-provided Skills for their documented purpose;
- organization-provisioned Skills reviewed by authorized owners; and
- internally developed Skills with a clear owner, review record, and current tests.

These are not automatically risk-free. They begin from a stronger provenance position.

### Higher-scrutiny cases

- unknown third-party publisher;
- copied Skill with no owner;
- internal Skill from another team with no review evidence;
- old or abandoned bundle;
- unverifiable version or source; and
- Skill whose description is inconsistent with its contents.

```text
Internal
      ≠
Vetted
```

## 2. Reach

The course frames reach as what the Skill could touch in the sessions where it runs.

Review the environment in which the Skill will operate:

- files and directories;
- uploaded knowledge;
- connectors;
- code execution;
- external tools;
- credentials exposed to the runtime;
- network access, where applicable;
- write, send, publish, modify, or delete capabilities;
- retained logs and outputs; and
- sensitive or regulated data.

A Skill may not present a separate permission prompt for every action. Its practical reach depends on the tools and access already available in the session or agent environment.

```text
Skill scope
      ×
Session permissions
      =
Effective reach
```

### Audit the bundle

Inspect:

- `SKILL.md` or equivalent instructions;
- scripts;
- dependency declarations;
- bundled files and templates;
- tool references;
- external calls;
- file paths;
- data-retention behavior;
- error handling;
- update behavior; and
- actions that exceed the stated purpose.

A formatting Skill that searches unrelated repositories or invokes broad analytics is a red flag.

## 3. Appropriateness

Ask whether the Skill is the smallest capability that meets the need.

Evaluate:

- Does the task genuinely require a Skill?
- Is the procedure aligned to the approved workflow?
- Is the Skill more capable than necessary?
- Are simpler instructions or a narrower tool sufficient?
- Is its access proportional to the task?
- Does it preserve human review and approval boundaries?
- Is the data appropriate for the environment?
- Does the Skill comply with current policy?

```text
Useful capability
      ≠
Necessary capability
```

The principle is least privilege: enable the narrowest capability and access scope that can complete the approved work.

---

# Trust is contextual

A Skill may be acceptable in one environment and inappropriate in another.

```text
Document formatter
+ public sample content
+ no external connectors
→ lower-risk use

Same formatter
+ restricted client records
+ broad Drive and email access
→ materially different risk
```

The Skill did not change. Its data, environment, and effective reach changed.

> Trust belongs to the Skill-environment-use-case combination, not to the Skill name alone.

---

# Internal does not mean vetted

An internally created Skill may still contain:

- permissions chosen for another team's convenience;
- assumptions based on outdated policy;
- stale templates;
- dependencies not approved for your environment;
- broad connector access;
- scripts that were never security-reviewed; or
- behavior that does not fit your task.

Treat an internal Skill from outside your team like software from a sister department.

Confirm with the owner:

- what it does;
- what it accesses;
- why it needs that access;
- which version is current;
- how it was tested;
- what policy it implements;
- how updates are distributed;
- what failures are known; and
- how it can be disabled or rolled back.

```text
Known colleague
      ≠
Known software behavior
```

---

# Three trust outcomes

## Enable

Use when:

- the source is established;
- the bundle has been reviewed to the required level;
- the effective reach is understood;
- access is proportionate;
- the task is appropriate;
- policy and data conditions are satisfied;
- tests pass; and
- disable and monitoring paths exist.

## Escalate

Use when the Skill may be valuable but:

- the publisher is unknown or insufficiently verified;
- scripts or dependencies require specialist review;
- effective reach is broad;
- sensitive data is involved;
- write or external-action tools are available;
- organizational policy is unclear;
- the Skill comes from another team without current review evidence; or
- you lack authority to approve the risk.

Escalation routes may include organization owners, security, privacy, legal or compliance, platform administration, procurement, third-party risk, or the Skill's accountable publisher.

## Decline

Use when:

- the source cannot be established;
- the bundle cannot be inspected sufficiently;
- access is clearly disproportionate;
- the Skill conflicts with policy;
- the task is inappropriate;
- the Skill performs unnecessary external actions;
- no credible owner or remediation path exists; or
- review would not make the use acceptable.

```text
Trust check failed
      ≠
Always permanent ban
```

It means the current user should not enable the Skill under the current conditions and authority.

---

# Worked examples

## Example 1: Anthropic-provided document formatter

- **Source:** Anthropic-provided and maintained.
- **Reach:** Document creation and code execution required for the documented task; no unrelated connector access.
- **Appropriateness:** Formatting an approved, non-sensitive document.

```text
Enable within the approved environment.
```

Retain normal output review and data-handling controls.

## Example 2: Unknown analytics booster

A third-party Skill promises faster analytics but includes scripts, broad file access, and connector references unrelated to its description.

- **Source:** Unknown publisher and no review record.
- **Reach:** Potentially broad access to data, files, and tools.
- **Appropriateness:** Disproportionate capability for the stated task.

```text
Do not enable under personal authority.
Escalate for security and administrator review,
or decline if the source and access cannot be justified.
```

## Example 3: Skill from another internal team

The Skill creates recurring status reports but also reads a shared repository and uses an old policy template.

- **Source:** Internal owner is known, but no current approval exists for your workstream.
- **Reach:** Repository access exceeds what your Project requires.
- **Appropriateness:** The reporting procedure is useful, but the current bundle and access are not proportionate.

```text
Escalate and request a narrower reviewed version.
```

Internal provenance improves traceability, not automatic approval.

---

# Feature-level risk generalization

The same evaluation applies beyond Skills.

Before enabling a connector, tool, integration, code-execution feature, Memory setting, or external action, ask:

```text
Who provides it?
What can it access or change?
Is that reach proportionate to the approved task?
```

Additional questions include:

- What persists?
- What is logged?
- What can execute?
- What can leave the environment?
- What requires human confirmation?
- How is it monitored?
- How is it disabled or revoked?

```text
Feature enabled
      ≠
Feature governed
```

---

# Skill trust register

| Field | Purpose |
|---|---|
| Skill ID and version | Stable identification |
| Publisher and owner | Provenance and accountability |
| Distribution path | Anthropic, organization, shared, personal, third-party |
| Stated purpose | Intended task |
| Bundle contents | Instructions, scripts, files, dependencies |
| Required environment | Code execution, connectors, file access, network |
| Effective reach | Data and tools accessible in use |
| Data classification | Information exposed to the Skill |
| External actions | Create, update, send, publish, delete |
| Review status | Approved, conditional, pending, rejected |
| Tests | Functional, security, boundary, regression |
| Known limitations | Residual risk |
| Disable or rollback | Containment path |
| Review date | Revalidation schedule |

---

# Trust evaluation protocol

```text
1. Define the task and approved environment
2. Identify the Skill, publisher, owner, and version
3. Inspect instructions, scripts, dependencies, and bundled files
4. Enumerate the session's files, connectors, tools, data, and actions
5. Calculate effective reach
6. Compare reach with task necessity and policy
7. Check data sensitivity and human approval boundaries
8. Run functional, security, boundary, and regression tests
9. Record residual risk, monitoring, and disable path
10. Enable, escalate, or decline
```

---

# Common failure modes

| Failure | Repair |
|---|---|
| Trusting a Skill because it is internal | Require current owner, review evidence, and proportional access |
| Reviewing description but not bundle | Inspect instructions, scripts, dependencies, and files |
| Treating Skill reach as isolated | Evaluate the full session environment and available tools |
| Enabling broad access for convenience | Apply least privilege and narrow the environment |
| Assuming useful output proves safety | Test security, boundaries, and side effects separately |
| User approves beyond their authority | Escalate to the appropriate owner or risk function |
| No disable path | Define containment and rollback before enablement |
| Feature approved once, never revisited | Reassess after version, policy, data, or permission changes |

---

# Exam lens

```text
Anthropic-provided Skill for matching task → lower-risk starting point, still use normal controls
Unknown publisher with broad reach         → escalate or decline
Internal Skill with no review evidence     → internal is not automatically vetted
Skill description narrower than contents   → red flag; inspect and escalate
Skill inherits broad session environment   → reduce effective reach
Capability exceeds task need               → choose narrower feature or decline
User lacks approval authority              → escalate
Source, reach, and appropriateness clear    → enable with monitoring
```

For Skill and feature-risk scenarios:

1. identify the exact feature and version;
2. establish publisher and owner;
3. inspect the bundle rather than relying on the name;
4. enumerate the session's effective reach;
5. compare access with the approved task;
6. apply least privilege;
7. classify data and external actions;
8. confirm approval authority;
9. define tests, monitoring, and disable paths; and
10. choose enable, escalate, or decline.

---

# Short recap

```text
1. A Skill is a software-like package, not merely a prompt.
2. Review source, reach, and appropriateness before enablement.
3. Internal does not automatically mean vetted.
4. Inspect instructions, scripts, dependencies, and bundled files.
5. Effective reach depends on the session environment.
6. Access must be proportional to the task.
7. Least privilege applies to Skills and every other feature.
8. The three outcomes are enable, escalate, and decline.
9. Useful output does not prove safe behavior.
10. Reassess trust after versions, permissions, data, or policy change.
```

## Educational-use notice

This lesson is an unofficial educational resource. Skills, connectors, code execution, permissions, and product interfaces can change. Verify current official documentation and organizational policy before enabling capabilities in a work environment. Examples are fictional and do not constitute security, privacy, legal, compliance, procurement, or operational advice.
