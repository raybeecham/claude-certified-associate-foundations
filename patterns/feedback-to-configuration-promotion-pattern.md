# Feedback-to-Configuration Promotion Pattern

## Problem

Teams often discover the right correction but leave it inside a one-off conversation. The same defect then returns in later cycles, for other users, or after ownership changes.

Common symptoms include:

- the same manual edit is repeated every week;
- different users rediscover the same instruction;
- a colleague misses an undocumented correction;
- Memory is assumed to be a shared control;
- exact business logic exists only in prompt wording;
- a successful fix is promoted after one example without regression testing.

## Context

Use this pattern when:

- recurring output needs the same correction;
- stakeholder feedback repeats across cycles;
- a prompt improvement should persist across Project chats;
- a multi-step repair may belong in a Skill;
- deterministic logic should move out of natural-language prompting;
- a team needs a shared, reviewable improvement rather than personal memory.

## Recommended design

```text
Capture feedback
      ↓
Translate reaction into observable defect
      ↓
Identify missing condition
      ↓
Select controlling lever
      ↓
Make one bounded change
      ↓
Validate representative cases
      ↓
Promote to the correct layer
      ↓
Version, monitor, and review
```

## 1. Capture the feedback precisely

Record:

- task and expected outcome;
- observed output;
- reviewer reaction;
- concrete defect;
- affected users or cycles;
- consequence if repeated.

```text
`Not quite right`
      ≠
Actionable feedback
```

## 2. Convert reaction into instruction

Ask:

- What specifically would need to be present for the output to be correct?
- What should be absent?
- Where should it appear?
- How can a reviewer observe compliance?

Examples:

- `Too generic` → name the audience and required action.
- `Wrong tone` → define tone, prohibited language, and an example.
- `Missed the point` → state the single question first.
- `Keeps including test data` → implement and verify an exclusion rule.

## 3. Identify the controlling lever

| Defect source | Durable lever |
|---|---|
| One-time missing detail | Current prompt |
| Reusable facts | Project knowledge or approved source |
| Recurring behavior or format | Project, user, or organization instruction |
| Repeatable multi-step method | Skill |
| Exact filtering or calculation | Code, query, schema, or workflow control |
| Long-session degradation | Clean restart or context transfer |
| Outdated dependency | Configuration maintenance |
| Missing approval | Human workflow gate |

```text
Correct correction
+ wrong layer
=
fragile repair
```

## 4. Test one change

Preserve the baseline and change one relevant variable.

Test:

- original failing case;
- representative normal cases;
- edge cases;
- conflicting-instruction cases;
- quality and completeness;
- latency and cost;
- governance controls.

## 5. Decide whether to promote

Use this trigger:

```text
Will the same correction be needed again
by this user, another user, or another cycle?
```

If no, keep it local.

If yes, promote only after validation.

## 6. Choose the narrowest durable home

- **Project instruction:** recurring behavior within one Project.
- **Project knowledge:** shared factual background or maintained templates.
- **Skill:** specialized repeatable procedure.
- **Organization instruction:** organization-wide behavior where available and authorized.
- **Code or workflow control:** exact rules, filters, calculations, schemas, approvals, and release gates.
- **Memory:** personal continuity only; not the authoritative shared home for material controls.

## 7. Govern the promoted fix

Record:

- owner;
- scope;
- approval;
- version;
- effective date;
- representative tests;
- conflicts;
- rollback path;
- review trigger;
- retirement condition.

## Failure modes

### Manual correction forever

The team knows the fix but never changes the system.

### Vague promotion

A reaction such as `be more strategic` becomes a standing instruction without observable criteria.

### Premature promotion

One successful output is treated as proof.

### Overbroad scope

A rule useful in one workflow is applied everywhere.

### Wrong mechanism

A deterministic exclusion is stored only in natural language.

### Memory as authority

Personal best-effort continuity is mistaken for a shared, versioned control.

## Compact decision rule

> Translate recurring feedback into an observable instruction, locate the lever that controls the defect, validate one bounded change, and promote the fix to the narrowest shared configuration layer that can be reviewed, tested, versioned, and rolled back.

## Public-repository rule

Use fictional, synthetic, public, or sanitized examples. Do not include private outputs, confidential prompts, production logs, client information, credentials, internal corrections, or proprietary workflows.