# Module 5 Prompt Notebook: Completion and Transition

Use fictional, synthetic, public, or explicitly authorized examples. Do not include confidential configurations, credentials, private connector identifiers, Memory exports, or proprietary policies.

## 1. Explain configuration leverage

```text
Explain the difference between using Claude for one conversation and operating a maintained Claude environment.

Include:
- what is configured once;
- what remains task-specific;
- how team consistency improves;
- what configuration cannot guarantee; and
- why maintenance is part of the design.
```

## 2. Mechanism-selection review

```text
Classify each recurring need into its primary home:
- current request;
- Project instructions;
- Project knowledge;
- Skill;
- Project-scoped Memory;
- connector;
- deterministic control; or
- system of record.

Needs:
[list]

For each, explain the selection and identify any required pairing with another mechanism.
```

## 3. Project-boundary review

```text
Review this proposed Project boundary:
[description]

Assess:
- purpose;
- users;
- source set;
- permissions;
- sensitivity;
- disclosure boundaries;
- continuity needs;
- reasons to split into separate Projects; and
- controls Project separation does not replace.
```

## 4. Connector and source contract

```text
Create a combined connector and knowledge contract for:
[workflow]

Include:
- connected identity;
- source scope;
- read, draft, write, and unsupported actions;
- approval boundary;
- source authority;
- freshness and refresh behavior;
- conflicts and supersession;
- owner;
- review date; and
- revocation path.
```

## 5. Persistent-instruction certification drill

```text
Repair these vague standing instructions:
[instructions]

For each replacement, define:
- trigger;
- required behavior;
- evidence boundary;
- failure behavior;
- observable output; and
- one positive and one adversarial test.

Apply the two-reader test.
```

## 6. Configuration-maintenance audit

```text
Audit this configured workspace:
[configuration inventory]

Check:
- instruction drift;
- stale, duplicate, or superseded knowledge;
- Skill ownership and version;
- connector permissions and current need;
- Memory accuracy and authority placement;
- missing owners or review dates;
- missing tests;
- rollback and reset safeguards; and
- retirement conditions.

Recommend the smallest sufficient maintenance actions.
```

## 7. Quiet-drift investigation

```text
A recurring workflow is producing subtly worse output even though user prompts have not changed.

Configuration:
[details]

Investigate the reusable baseline before recommending prompt changes.
Classify each possible defect as:
- instruction;
- knowledge;
- Skill;
- connector;
- Memory;
- permission;
- product change;
- test gap; or
- workflow ownership.
```

## 8. Module 5 retention check

```text
Ask me ten short scenario questions covering:
- configuration leverage;
- mechanism selection;
- Project boundaries;
- connector capability;
- source authority;
- precise instructions;
- instruction enforcement limits;
- maintenance cadence;
- Memory lifecycle; and
- rollback or retirement.

Wait for my answer after each question, then explain the reasoning.
```

## 9. Transition to Governance

```text
Given this configured AI-assisted workflow:
[workflow]

Identify the governance questions that Module 6 should evaluate next.
Separate:
- use-case appropriateness;
- data sensitivity and permitted use;
- policy obligations;
- affected people;
- decision authority;
- fairness and ethics concerns;
- monitoring and accountability; and
- conditions for approval, restriction, escalation, or rejection.

Do not assume configuration quality proves governance acceptability.
```

## 10. Oral certification summary

```text
Give a two-minute spoken explanation of Module 5.

Cover:
1. using versus operating Claude;
2. instructions, knowledge, Skills, and Memory;
3. connector capability boundaries;
4. precise persistent instructions;
5. configuration maintenance; and
6. the transition from configuration to governance.

Use plain language and one practical example.
```

## Compact recall card

```text
Behavior → instructions
Facts → knowledge
Procedure → Skill
Continuity → Memory
Access → connector
Authority → human and deterministic controls
State → system of record

Access ≠ authority
Instruction ≠ enforcement
No error ≠ no drift
Configured ≠ governed
```
