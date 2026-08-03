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

## Course-aligned roadmap

- [x] [01. Diagnosing Underperforming Prompts & Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [x] [02. Adjusting Approach from Feedback](lessons/02-adjusting-approach-from-feedback.md)
- [ ] 03. Optimizing Workflows
- [ ] 04. Module 7 Quiz
  - [ ] Module 7 Quiz
  - [ ] Key Takeaways
- [ ] 05. Module Complete

## Diagnostic foundation

| Symptom pattern | Likely cause | First repair |
|---|---|---|
| Wrong from the first response | Under-specification | Add missing task-contract details |
| Started well, then degraded | Context overload | Restart from a verified summary |
| Specific repeatable error | Wrong feature or model | Select the correct capability |
| Used to work, now performs poorly | Stale configuration | Review maintained dependencies |
| Unavailable after cheaper causes are ruled out | Expectation mismatch | Reshape the task |

```text
One hypothesis
      ↓
One bounded change
      ↓
One controlled comparison
      ↓
Keep / revise / revert
```

## Feedback-adjustment foundation

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

A reaction describes how an output feels. An instruction defines what must change.

```text
Reaction
      ≠
Instruction
```

| Reaction | Specific adjustment | Lever |
|---|---|---|
| Too generic | State the audience and desired action | Prompt context or Project instruction |
| Wrong tone | Define observable tone constraints | Standing instruction |
| Missed the point | Put the required question first | Prompt objective |
| Same field missing repeatedly | Add it to the maintained template or Skill | Configuration |
| Test records included | Add deterministic exclusion and verification | Code, query, or workflow control |

## Correct placement

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

```text
Will this same correction be needed again
by me, another person, or another cycle?
```

- **No:** keep the change local.
- **Yes:** validate it, then promote it to the narrowest durable layer.

Memory can support personal continuity, but shared recurring corrections belong in deliberate configuration that can be reviewed, versioned, tested, shared, and maintained.

## Worked examples

### Campaign briefs

Recurring defects:

- target segment omitted;
- call to action buried.

Validated Project instructions:

```text
Always state the target segment in the first line.
Place the call to action in a separate closing section.
```

### Monthly test-account exclusion

A recurring conversational reminder is insufficient.

```text
Authoritative exclusion rule
+ deterministic filter
+ verification count
+ shared documentation
```

Exact business logic belongs in code or query configuration, not only in prompting.

## Feedback-adjustment protocol

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
11. Decide whether the fix remains local or is promoted
12. Version, approve, monitor, and review durable changes
```

## Current module resources

### Lessons

- [Diagnosing Underperforming Prompts and Outputs](lessons/01-diagnosing-underperforming-prompts-outputs.md)
- [Adjusting Approach from Feedback and Results](lessons/02-adjusting-approach-from-feedback.md)

### Prompt notebooks

- [Diagnosing Underperformance prompts](../../prompts/module-07/01-diagnosing-underperformance-prompts.md)
- [Adjusting Approach from Feedback prompts](../../prompts/module-07/02-adjusting-approach-from-feedback-prompts.md)

### Engineering patterns

- [Failure Localization Pattern](../../patterns/failure-localization-pattern.md)
- [Feedback-to-Configuration Promotion Pattern](../../patterns/feedback-to-configuration-promotion-pattern.md)

### Extended practice

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

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

## Completion criteria

- [x] I completed Diagnosing Underperforming Prompts & Outputs.
- [x] I completed Adjusting Approach from Feedback.
- [ ] I completed Optimizing Workflows.
- [ ] I can classify the five common underperformance causes.
- [ ] I can convert a vague reaction into an observable defect and testable instruction.
- [ ] I can identify the lever that controls a recurring defect.
- [ ] I can distinguish prompt edits, instructions, knowledge, Skills, deterministic controls, and human gates.
- [ ] I can validate a bounded adjustment against representative cases.
- [ ] I can decide when a correction should be promoted into configuration.
- [ ] I can preserve governance while troubleshooting and promoting fixes.
- [ ] I completed the Module 7 quiz and Key Takeaways.
- [ ] I completed the troubleshooting lab and scored at least 80% on the extended quiz.

## Public-repository scenario policy

Examples must be fictional, generic, synthetic, public, or explicitly authorized. Do not include client data, private prompts or outputs, confidential incidents, proprietary logs, credentials, internal configuration, nonpublic performance results, remembered live-exam questions, or reconstructed proprietary course content.

## Educational-use notice

This repository is an unofficial educational resource. It does not constitute operational, security, reliability, legal, privacy, compliance, or production-engineering advice.

## Product-verification note

Product behavior changes. The placement guidance in this module was checked against official Claude Help Center material available on August 3, 2026. Current official documentation and authorized organizational guidance control implementation-specific decisions.