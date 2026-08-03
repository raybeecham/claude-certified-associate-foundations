# Lesson 2: Adjusting Approach from Feedback and Results

## Overview

A disappointing output is not only a result to repair. It is evidence about the system that produced it.

```text
Output critique
      ↓
Specific missing condition
      ↓
Controlling lever
      ↓
Bounded adjustment
      ↓
Validation
      ↓
Promote recurring fix
```

> The goal is to convert a reaction into an instruction, test the change, and place recurring corrections in the configuration layer where they will persist.

---

# Plain-English explanation

A reaction describes how an output feels:

- too generic;
- wrong tone;
- missed the point;
- too long;
- inconsistent;
- missing the same item again.

A useful instruction states what must change:

- name the intended audience and required action;
- add a tone constraint;
- state the single question the output must answer;
- define a word or section limit;
- provide a stable format;
- exclude a known class of records.

```text
Reaction
      ≠
Instruction
```

If the controlling lever cannot be named, the next attempt is still a guess.

---

# One analogy: correcting a production line

If the same product defect appears every week, repeatedly fixing the finished item is expensive. The better response is to identify which station creates the defect and repair that station.

- **Output critique** identifies the defect.
- **Root-cause analysis** identifies the station.
- **A specific adjustment** changes the station.
- **Validation** confirms the defect is gone.
- **Configuration promotion** keeps the repair in place for future runs.

---

# Build feedback loops into recurring work

After each recurring task, ask:

1. What was correct?
2. What required correction?
3. Has this correction appeared before?
4. What specifically was missing or wrong?
5. Which part of the setup controls it?
6. What is the smallest change that should fix it?
7. Did the change improve representative cases?
8. Should the successful fix be promoted into configuration?

```text
Recurring manual correction
      =
Evidence of a missing persistent control
```

One isolated correction may remain local. A correction that recurs across cycles, users, or similar tasks should be treated as a system defect.

---

# Translate critique into a specific adjustment

Use this translation sequence:

```text
Reaction
      ↓
Observable defect
      ↓
Missing condition
      ↓
Controlling lever
      ↓
Testable instruction
```

## Examples

| Reaction | Observable defect | Specific adjustment | Lever |
|---|---|---|---|
| Too generic | Output lacks audience-specific priorities | State the audience and required action | Prompt context or Project instruction |
| Wrong tone | Language is too casual for the recipient | Add an observable tone constraint and example | Project or organization instruction |
| Missed the point | Output answers several issues but not the central question | Put the single required question first | Prompt objective |
| Too long | Output regularly exceeds the usable length | Add section and word limits | Prompt or standing format rule |
| Missing the same field | A recurring report omits one required item | Add the field to the maintained template or Skill | Configuration |
| Includes test records | Report logic does not exclude known test accounts | Add a deterministic filter and verification check | Code, query, or workflow control |

The instruction should be observable enough to test. `Make it better` is not testable. `State the target segment in the first line` is.

---

# Identify the controlling lever

A correction belongs where the cause lives.

| Cause | Likely lever |
|---|---|
| Missing one-time detail | Current prompt |
| Missing reusable background | Project knowledge or approved source |
| Recurring behavior or format | Project, user, or organization instruction |
| Multi-step repeatable procedure | Skill |
| Deterministic calculation or filtering | Code or query logic |
| Long-session drift | Clean restart or context transfer |
| Outdated source or rule | Configuration maintenance |
| Wrong capability | Entry point, feature, tool, or model selection |
| Human decision or approval defect | Workflow gate and accountable role |

```text
Correct instruction
+ wrong configuration layer
=
fragile repair
```

Do not place facts in behavioral instructions, do not use Memory as an authoritative shared control, and do not encode deterministic business logic only in natural-language prompting.

---

# Validate the adjustment

Before promoting a fix:

1. preserve the original failing case;
2. state the hypothesis;
3. change one relevant variable;
4. rerun the failing case;
5. test representative normal cases;
6. inspect edge cases;
7. check quality, latency, cost, and governance effects;
8. keep, revise, or revert.

```text
One improved output
      ≠
Validated recurring fix
```

A correction that helps one example but damages other cases should not be promoted unchanged.

---

# Promote what works

Use the narrowest durable home that matches the correction.

## Current prompt

Use for:

- one-time facts;
- temporary constraints;
- unique audience details;
- a single task exception.

## Project instructions

Use for recurring Project-specific behavior, such as:

- required tone;
- output structure;
- audience rules;
- recurring exclusions;
- evidence and uncertainty requirements.

Current Claude documentation states that Project instructions apply across chats within that Project.

## Project knowledge

Use for maintained background facts, approved references, templates, and source material that should be available across Project chats.

## Skill

Use for a specialized repeatable procedure, especially when the correction requires several ordered steps, examples, scripts, or reusable resources.

Current Claude documentation describes Skills as repeatable task-specific workflows made from instructions, scripts, and resources.

## Organization instructions

Where available and authorized, use for organization-wide standards that should apply across conversations, such as approved communication or compliance guidance.

## Code or workflow control

Use for exact filters, calculations, schema validation, release gates, and other deterministic requirements.

## Memory

Memory can support personal continuity, but it is not the preferred authoritative home for a shared recurring correction. Deliberate configuration is easier to review, share, version, and test.

---

# Promotion test

Ask:

```text
Will this same correction be needed again
by me or someone else?
```

If **no**, keep it local.

If **yes**, consider promotion.

Before promotion, confirm:

- the correction is validated;
- its scope is known;
- the correct owner approves it;
- it does not conflict with policy or other instructions;
- representative and edge cases pass;
- rollback is possible;
- a review date or trigger exists.

---

# Worked example: campaign briefs

A fictional marketing team sees the same two defects every week:

- the target segment is omitted;
- the call to action is buried.

## Reaction

`The brief is incomplete and unfocused.`

## Translation

- Observable defect 1: no target segment appears near the start.
- Adjustment 1: `State the target segment in the first line.`
- Observable defect 2: the call to action is difficult to locate.
- Adjustment 2: `Place the call to action in a separate closing section.`

## Lever

Both are recurring Project-specific output rules, so they belong in the briefs Project instructions.

## Validation

Test:

- the original campaign;
- a different audience segment;
- a campaign with multiple possible actions;
- a short-form brief;
- a case where the call to action is unknown.

## Result

After validation, the correction is promoted into Project instructions and no longer depends on a user remembering it every week.

---

# Worked contrast: uncaptured filtering rule

An analyst repeatedly reminds Claude to exclude internal test accounts from a monthly report.

Leaving the instruction in one conversation creates several risks:

- the analyst must remember it every month;
- a colleague covering the task may not know it;
- the rule is not versioned or reviewed;
- there is no deterministic verification;
- the report may ship with test records.

The correct repair is stronger than a recurring reminder:

```text
Maintained exclusion rule
+ deterministic filter
+ verification count
+ shared documentation
```

This places exact logic in code or query configuration and records the business rule where the team can review it.

---

# Feedback-adjustment record

```text
Task or workflow:

Observed output defect:

Reaction received:

Specific missing or incorrect condition:

Controlling lever:
Prompt / Context / Project instruction / Knowledge / Skill / Code / Workflow / Model / Other

Hypothesis:

Bounded adjustment:

Validation cases:

Result:
Keep / Revise / Revert

Promotion decision:
Local / Project instruction / Knowledge / Skill / Organization instruction / Code / Workflow

Owner:

Rollback path:

Review trigger:
```

---

# Common failure modes

## Repeating the correction manually

The fix is known but never captured.

## Converting a reaction into vague wording

`Be more strategic` does not define observable behavior.

## Promoting before validation

A correction becomes a standing rule after one successful example.

## Choosing the wrong layer

Exact filtering logic is placed only in a natural-language instruction.

## Overgeneralizing

A correction useful for one report is applied to every workflow.

## Conflicting instructions

A new standing rule contradicts an existing Project, user, or organization instruction.

## Treating Memory as shared governance

A personal best-effort continuity mechanism is assumed to be a reviewed team control.

---

# Exam lens

```text
Same correction every cycle          → promote after validation
Feedback says `too generic`          → identify audience and required action
Feedback remains emotional or vague  → translate into observable defect
Fix belongs to one task only         → keep it in the current prompt
Recurring format requirement         → Project or standing instruction
Multi-step recurring method          → Skill
Exact exclusion or calculation       → deterministic code or workflow control
One example improves                 → run representative regression tests
Memory may remember a pattern        → deliberate configuration is the reliable shared home
```

---

# Recap

1. Treat disappointing output as diagnostic evidence.
2. Translate reactions into observable defects and specific instructions.
3. Identify the lever that controls the defect.
4. Test one bounded adjustment.
5. Validate beyond the original example.
6. Promote recurring fixes into the correct configuration layer.
7. Version, review, monitor, and roll back durable changes.

> A fix becomes an improvement only when it is specific, validated, and captured where future work will actually use it.

---

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, privacy, legal, compliance, or production-engineering advice.

## Product-verification note

Product behavior and feature availability can change. Current official Claude documentation should control implementation-specific decisions about Projects, instructions, Skills, Memory, and organization features.