# Lesson 4: System-Level Instructions That Stick

## Overview

Persistent instructions let a team define recurring behavior once instead of rebuilding the same guardrails in every conversation.

They are useful for verification habits, evidence boundaries, uncertainty behavior, tone, output structure, terminology, review reminders, and escalation rules.

```text
Recurring behavioral requirement
      ↓
Precise standing instruction
      ↓
Representative tests
      ↓
Consistent Project baseline
```

> A standing instruction is effective only when it is specific enough to produce observable behavior and narrow enough to avoid unintended interference.

---

# Plain-English explanation

A vague instruction such as:

```text
Be professional and accurate.
```

sounds reasonable, but it does not define what professional or accurate means.

A stronger instruction says:

```text
Use a formal register.
Define each acronym on first use.
Keep paragraphs under four sentences.
Cite the supplied source location for every material factual claim.
If the supplied sources do not support a claim, label it unverified rather than guessing.
```

```text
Vague intention
      ≠
Operational behavior
```

---

# One analogy: a flight checklist

A checklist does not say `fly safely`. It defines observable steps, thresholds, and responses.

Standing instructions should likewise define what behavior is expected, what evidence is required, and what Claude should do when the requirement cannot be satisfied.

> Good instructions replace interpretation with observable operating rules where possible.

---

# What belongs in persistent instructions

Appropriate categories include:

## Verification behavior

```text
Cite the supplied source document and location for material factual claims.
Do not infer a fact when the sources are silent.
Label conflicting evidence and identify the competing sources.
```

## Uncertainty behavior

```text
When evidence is insufficient, say what is missing.
Use `unknown`, `not supported`, or `requires clarification` rather than filling the gap.
```

## Format defaults

```text
Lead each report with a one-sentence headline.
Use the required section order.
Return action items with owner, due date, and status.
```

## Tone and terminology

```text
Use a formal register.
Define acronyms on first use.
Use the approved terminology glossary where supplied.
```

## Review and escalation

```text
Flag material assumptions for reviewer confirmation.
Do not present draft content as approved.
Escalate unresolved source conflicts to the named owner.
```

---

# What belongs elsewhere

| Need | Appropriate home |
|---|---|
| Current policy text | Project knowledge |
| Standard multi-step report procedure | Skill |
| Prior Project decisions | Scoped Memory or authoritative record |
| Exact authorization rule | Deterministic control |
| Credentials or secrets | Approved secret-management mechanism |
| Current task exception | Current request |

```text
Behavior rule → instruction
Reference evidence → knowledge
Reusable procedure → Skill
Authority or exact rule → deterministic control
```

---

# Instruction anatomy

A durable instruction should answer five questions.

| Element | Question |
|---|---|
| Trigger | When does the rule apply? |
| Required behavior | What should Claude do? |
| Evidence boundary | What may it rely on? |
| Failure behavior | What happens when the rule cannot be satisfied? |
| Observable output | How can a reviewer tell it was followed? |

Example:

```text
When producing a report from supplied data:
- state the source for every figure;
- use only supplied or reviewed calculated figures;
- label unsupported figures `unverified`;
- lead with a one-sentence headline; and
- list unresolved data gaps.
```

---

# The two-reader test

Ask:

> Would two different people interpret this instruction the same way?

If not, add defined terms, thresholds, named formats, source boundaries, examples, failure behavior, or precedence rules.

| Weak | Stronger |
|---|---|
| Be concise | Limit the executive summary to five bullets and 150 words |
| Be professional | Use a formal register, no slang, and define acronyms on first use |
| Verify facts | Cite the supplied source and location for each material claim |
| Do not hallucinate | Mark unsupported claims `not supported by supplied sources` |
| Flag risks | List likelihood, impact, owner, and mitigation |

---

# Worked example

## Before

```text
Make the reports good and accurate.
```

This fails because `good` is undefined, `accurate` has no evidence rule, no format is specified, and no missing-data behavior exists.

## After

```text
For every report:
1. Lead with a one-sentence headline.
2. Use Summary, Evidence, Risks, Decisions, and Actions.
3. Cite the supplied source and location for every material factual claim.
4. State the source or reviewed calculation method for every figure.
5. Label unsupported figures `unverified`.
6. List unresolved evidence gaps before the recommendation.
7. Do not describe a draft as approved.
```

Observable tests check the headline, section order, citations, figure support, evidence gaps, and approval status.

---

# Instruction conflicts and precedence

Persistent instructions interact with the current request, Project knowledge, Skills, organizational policy, tool permissions, deterministic controls, and platform rules.

```text
Instruction present
      ≠
Instruction highest authority
      ≠
Instruction technically enforceable
```

When maintained instructions conflict:

1. identify the exact conflict;
2. compare scope, owner, version, and authority;
3. determine supersession;
4. preserve unresolved conflict;
5. obtain owner resolution; and
6. update tests and version history.

---

# Instructions are not security controls

Persistent instructions do not independently enforce identity, authorization, data isolation, source permissions, secrets handling, professional authority, external-action approval, or deterministic business rules.

```text
Instruction says `do not send`
      ≠
Send capability technically disabled
```

Pair consequential instructions with least-privilege permissions, deterministic validation, controlled tools, human review, approval gates, logging, and systems of record.

---

# Testing persistent instructions

Use positive, boundary, adversarial, and regression tests.

Test cases should include:

- supported factual claims;
- missing evidence;
- conflicting sources;
- a request to skip citations;
- a task-specific format exception;
- a draft that could be mistaken for approved output; and
- unrelated tasks that should not be distorted by the standing rule.

After changes, confirm intended behavior improved without damaging unrelated outputs or approval boundaries.

---

# Common failure modes

| Failure | Repair |
|---|---|
| Vague aspiration | Define evidence, uncertainty, and observable behavior |
| Instruction overload | Move facts, procedures, state, and exact controls elsewhere |
| No failure behavior | Define unknown, unverified, clarification, or escalation behavior |
| Untested guardrail | Add positive, boundary, and adversarial tests |
| Conflicting rules | Assign authority, owner, version, and resolution path |
| Natural-language-only restriction | Add technical, tool, review, and approval controls |

---

# Durable-instruction protocol

```text
1. Identify behavior users repeatedly retype
2. Separate behavior from facts, procedures, state, access, and authority
3. Define trigger, behavior, evidence boundary, failure behavior, and observable output
4. Apply the two-reader test
5. Add examples where ambiguity remains
6. Document precedence and conflict behavior
7. Pair consequential rules with enforceable controls
8. Create representative and adversarial tests
9. Version, approve, and release
10. Monitor and refine without broadening scope unnecessarily
```

---

# Exam lens

```text
Always cite supplied sources          → persistent Project instruction
Current policy text                   → Project knowledge
Standard multi-step report method     → Skill
Be professional                       → too vague
Unsupported claim                     → label unknown or unverified
Two instructions conflict             → resolve authority and version
Instruction says no external action   → still require technical controls
Instruction changed                   → rerun regression tests
```

---

# Short recap

```text
1. Persistent instructions define recurring behavior.
2. High-value rules are the ones users otherwise retype.
3. Vague instructions fail silently.
4. Precise instructions define observable behavior.
5. Evidence and missing-data behavior matter.
6. The two-reader test exposes ambiguity.
7. Facts belong in knowledge; procedures belong in Skills.
8. Instructions cannot replace permissions or approvals.
9. Standing instructions require tests and versioning.
10. Maintain them as the workflow changes.
```

## Educational-use notice

This lesson is an unofficial educational resource. Product behavior and configuration interfaces can change. Verify current official documentation and organizational policy before relying on implementation-specific behavior.
