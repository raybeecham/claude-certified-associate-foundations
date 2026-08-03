# Module 5 Prompt Notebook: Key Takeaways

Use fictional, synthetic, public, or explicitly authorized descriptions. Do not include credentials, private connector identifiers, confidential knowledge, proprietary instructions, or Memory exports.

## 1. Configuration leverage assessment

```text
Review this recurring workflow:
[workflow]

Identify:
- what users currently rebuild every conversation;
- which requirements are stable enough to configure;
- what must remain task-specific;
- the expected consistency benefit;
- new maintenance obligations; and
- signs that configuration is becoming an operational dependency.
```

## 2. Mechanism classification drill

```text
Classify each item as:
- current request;
- Project instruction;
- Project knowledge;
- Skill;
- scoped Memory;
- connector;
- deterministic control; or
- system of record.

Items:
[list]

Explain the choice and identify any item that requires paired mechanisms.
```

## 3. Authoritative-home audit

```text
Review this Project configuration:
[configuration]

Identify:
- duplicated rules;
- facts stored in instructions;
- procedures stored only in knowledge;
- stable references stored only in Memory;
- exact controls expressed only as prose; and
- missing authoritative homes.

Return a corrected configuration map.
```

## 4. Connector boundary review

```text
Create a capability contract for this connector:
[connector description]

Separate:
- identity;
- source scope;
- search;
- read;
- draft;
- create;
- update;
- send or publish;
- delete;
- unsupported actions;
- approval gates;
- owner;
- review date; and
- revocation path.

Do not infer capabilities that are not documented.
```

## 5. Connector failure diagnosis

```text
A connector failed in this scenario:
[scenario]

Classify the likely failure as:
- installation or enablement;
- authentication;
- permission;
- source scope;
- tool loading;
- unsupported capability;
- stale or missing source;
- external-system failure; or
- probable product defect.

State the next verification step and the correct escalation owner.
```

## 6. Vague-instruction repair

```text
Rewrite these standing instructions as observable operating rules:
[instructions]

For each rule define:
- trigger;
- required behavior;
- evidence boundary;
- failure behavior; and
- observable output.

Apply the two-reader test and explain what ambiguity was removed.
```

## 7. Instruction enforcement audit

```text
Review these persistent guardrails:
[guardrails]

Separate:
- behavior Claude can be instructed to follow;
- technical permissions required;
- deterministic validations required;
- human approvals required;
- audit evidence required; and
- claims the instruction cannot enforce by itself.
```

## 8. Configuration maintenance review

```text
Review this Project inventory:
[inventory]

Check:
- standing-instruction drift;
- stale or duplicate knowledge;
- Skill version and distribution;
- connector identity and permissions;
- Memory accuracy;
- missing owners;
- missing review dates;
- absent rollback paths; and
- unsupported operational dependency.

Recommend edit, replace, disable, revoke, reset, rollback, or retirement for each defect.
```

## 9. Review cadence design

```text
Design a maintenance cadence for this configured workspace:
[workspace]

Include:
- recurring review frequency;
- event-triggered reviews;
- component owners;
- test suites;
- release evidence;
- rollback criteria;
- revocation criteria; and
- retirement criteria.
```

## 10. Memory lifecycle decision

```text
Review this fictional Memory inventory:
[memory entries]

Classify each entry as:
- retain;
- correct;
- move to Project knowledge;
- move to a system of record;
- delete;
- export before migration; or
- evidence that a full reset may be necessary.

Treat reset as destructive and justify it only when selective repair is insufficient.
```

## 11. Quiet-quality-decay investigation

```text
A recurring workflow produces subtly worse output with no prompt change:
[symptoms and configuration]

Investigate:
- instructions;
- knowledge;
- Skills;
- connectors;
- Memory;
- permissions;
- reviewer availability; and
- product or model changes.

Identify the smallest sufficient repair and regression tests.
```

## 12. Five-takeaway recall drill

```text
Without looking at notes, explain:
1. why configuration is leverage;
2. how to choose the correct mechanism;
3. why connector boundaries matter;
4. what makes an instruction precise; and
5. why configurations require maintenance.

For each, provide one correct example and one failure mode.
```

## 13. Integrated Project review

```text
Evaluate this configured Project end to end:
[Project description]

Answer:
1. Is the purpose bounded?
2. Are needs in the correct mechanisms?
3. Are sources current and authoritative?
4. Are connector capabilities explicit?
5. Are instructions observable and testable?
6. Are high-stakes rules technically enforced?
7. Are Memory and Skills current?
8. Are ownership and review cadence defined?
9. Is rollback or retirement possible?
10. What is the overall release disposition?
```

## 14. Oral certification drill

```text
Ask me one Module 5 scenario at a time.
Cover mechanism selection, Project separation, connector capability, instruction precision, and maintenance drift.
After each answer:
- score it;
- explain the controlling principle;
- identify the distractor pattern; and
- ask a harder follow-up.
```

## Review discipline

A correct Module 5 answer usually:

1. identifies the configuration responsibility;
2. places it in the smallest correct mechanism;
3. distinguishes access, authority, and action;
4. converts vague behavior into observable rules;
5. pairs guidance with enforceable controls;
6. checks version, freshness, permissions, and ownership;
7. chooses the smallest sufficient maintenance action; and
8. preserves rollback, revocation, reset safeguards, and retirement.