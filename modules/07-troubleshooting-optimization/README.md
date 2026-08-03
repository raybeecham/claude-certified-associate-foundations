# Module 7: Troubleshooting & Optimization

Associate Persona · Official Exam Domain 7

> **Status:** In progress — lessons 1 and 2 are complete.

## Module thesis

> Troubleshooting is disciplined diagnosis and controlled learning: identify the responsible layer, translate feedback into a specific adjustment, validate the smallest relevant change, and promote recurring fixes into durable configuration without weakening governance.

```text
Observed underperformance
      ↓
Evidence and diagnosis
      ↓
Feedback translated into instruction
      ↓
Bounded adjustment
      ↓
Representative validation
      ↓
Durable promotion and monitoring
```

---

# Course-aligned roadmap

- [x] [01. Diagnosing Underperforming Prompts & Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [x] [02. Adjusting Approach from Feedback](lessons/02-adjusting-approach-from-feedback.md)
- [ ] 03. Optimizing Workflows
- [ ] 04. Module 7 Quiz
  - [ ] Module 7 Quiz
  - [ ] Key Takeaways
- [ ] 05. Module Complete

No later section is marked complete until its preparation-course material is supplied and converted into original public-safe study content.

---

# Foundation 1: diagnose before editing

Weak output has multiple possible causes.

```text
Output is weak
      ≠
Prompt is automatically the cause
```

| Symptom pattern | Likely cause | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract details |
| Started well, then degraded | Context overload | Restart from a verified summary |
| Specific repeatable error | Wrong feature or model | Select the correct capability |
| Used to work, now performs poorly | Stale configuration | Review maintained dependencies |
| Unavailable after cheaper causes are ruled out | Expectation mismatch | Reshape the task |

Timing is evidence, not proof. Confirm the diagnosis through a controlled test.

## Cheapest-fix-first sequence

```text
1. Prompt specification
2. Conversation context
3. Feature and model fit
4. Maintained configuration
5. Task fit and expectation
```

## Controlled diagnosis

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

A repair should pass the original failing case, representative cases, edge cases, and governance checks.

---

# Foundation 2: adjust from feedback

A disappointing output is diagnostic data about the setup that produced it.

```text
Output critique
      ↓
Observable defect
      ↓
Missing condition
      ↓
Controlling lever
      ↓
Testable adjustment
      ↓
Validation and promotion
```

## Reaction versus instruction

A reaction describes how an output feels:

- too generic;
- wrong tone;
- missed the point;
- too long;
- incomplete.

An instruction defines what must change:

- name the audience and required action;
- add a tone rule and example;
- state the single question first;
- impose section or length limits;
- require the missing field.

```text
Reaction
      ≠
Instruction
```

If the controlling lever cannot be named, the next attempt remains a guess.

## Feedback translation table

| Reaction | Specific adjustment | Lever |
|---|---|---|
| Too generic | State the audience and desired action | Prompt context or Project instruction |
| Wrong tone | Define observable tone constraints | Standing instruction |
| Missed the point | Put the required question first | Prompt objective |
| Same field missing repeatedly | Add it to the maintained template or Skill | Configuration |
| Test records included | Add deterministic exclusion and verification | Code, query, or workflow control |

## Choose the correct lever

| Cause | Correct home |
|---|---|
| One-time detail | Current prompt |
| Reusable facts | Project knowledge or approved source |
| Recurring behavior or format | Project, user, or organization instruction |
| Multi-step repeatable procedure | Skill |
| Exact calculation or filtering | Code, query, schema, or workflow control |
| Long-session drift | Clean restart or transfer summary |
| Outdated rule or dependency | Configuration maintenance |
| Missing approval | Human workflow gate |

```text
Correct correction
+ wrong layer
=
fragile repair
```

## Promotion test

Ask:

```text
Will this same correction be needed again
by me, another person, or another cycle?
```

- **No:** keep the change local.
- **Yes:** validate it, then promote it to the narrowest durable layer.

Before promotion, confirm scope, ownership, approval, representative tests, conflicts, rollback, and review triggers.

## Memory versus deliberate configuration

Memory can support personal continuity, but recurring shared corrections belong in deliberate configuration that can be reviewed, shared, versioned, tested, and maintained.

Current Claude guidance describes:

- Project instructions as guidance applied across chats in a Project;
- Project knowledge as reusable context across Project chats;
- Skills as task-specific repeatable workflows using instructions, scripts, and resources; and
- organization instructions, where available, as standards applied across an organization.

```text
May be remembered personally
      ≠
Authoritative shared control
```

---

# Worked feedback examples

## Campaign briefs

Recurring defects:

- target segment omitted;
- call to action buried.

Validated standing instructions:

```text
Always state the target segment in the first line.
Place the call to action in a separate closing section.
```

Because these are recurring Project-specific behavior rules, they belong in Project instructions after representative testing.

## Monthly report test accounts

A repeated conversational reminder to exclude internal test accounts is insufficient.

The durable repair is:

```text
Authoritative exclusion rule
+ deterministic filter
+ verification count
+ shared documentation
```

Exact business logic belongs in code or query configuration, not only in natural-language prompting.

---

# Feedback-adjustment protocol

```text
1. Capture the output and critique
2. Describe the observable defect
3. Identify the missing or incorrect condition
4. Select the controlling lever
5. State one testable hypothesis
6. Make one bounded adjustment
7. Re-run the failing case
8. Test representative and edge cases
9. Check quality, cost, latency, and governance
10. Keep, revise, or revert
11. Decide whether the fix should remain local or be promoted
12. Version, approve, monitor, and review durable changes
```

---

# Current module resources

## Course-aligned lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)

## Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)

## Engineering patterns

- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Feedback-to-Configuration Promotion Pattern](../../patterns/feedback-to-configuration-promotion-pattern.md)

## Existing extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

---

# Exam lens

```text
Wrong on first response                 → inspect specification
Started well, then drifted              → inspect context
Specific quantitative failure          → inspect feature fit
Used to work                            → inspect configuration
Exact unavailable outcome               → reshape the task
Same correction every cycle             → validate and promote
Feedback says `too generic`             → identify audience and action
Recurring format requirement            → standing instruction
Multi-step recurring procedure          → Skill
Exact exclusion or calculation          → deterministic control
One improved example                    → run regression tests
Memory may retain a pattern              → deliberate configuration is the shared home
```

---

# Completion criteria

- [x] I completed Diagnosing Underperforming Prompts & Outputs.
- [x] I completed Adjusting Approach from Feedback.
- [ ] I completed Optimizing Workflows.
- [ ] I can classify under-specification, context overload, wrong feature or model, stale configuration, and expectation mismatch.
- [ ] I can convert a vague reaction into an observable defect and testable instruction.
- [ ] I can identify the lever that controls a recurring defect.
- [ ] I can distinguish local prompt edits from Project instructions, knowledge, Skills, deterministic controls, and human gates.
- [ ] I can validate one bounded adjustment against representative cases.
- [ ] I can decide when a correction should be promoted into configuration.
- [ ] I can preserve governance while troubleshooting and promoting fixes.
- [ ] I completed the Module 7 quiz and Key Takeaways.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

---

# Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private prompts or outputs, confidential incidents, proprietary logs, credentials, internal configuration, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.

## Product-verification note

Product behavior changes. The placement guidance in this module was checked against official Claude Help Center material available on August 3, 2026. Current official documentation and authorized organizational guidance control implementation-specific decisions.