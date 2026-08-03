# Module 7 — Adjusting Approach from Feedback Prompts

Use these prompts to turn output critique into specific, testable, durable improvements.

## 1. Reaction-to-instruction translator

```text
Review this critique and convert it into an actionable adjustment.

Task:
[describe the task]

Output:
[paste or summarize output]

Reaction:
[too generic / wrong tone / missed the point / other]

Return:
1. Observable defect
2. Missing or incorrect condition
3. Controlling lever
4. Specific testable instruction
5. Validation case
6. Whether the fix should remain local or be promoted
```

## 2. Controlling-lever classifier

```text
Classify the correct repair location for this recurring output problem.

Problem:
[describe recurring defect]

Possible levers:
- current prompt
- context or source material
- Project instruction
- Project knowledge
- Skill
- code or query logic
- workflow gate
- feature or model choice
- configuration maintenance

Explain why the chosen lever controls the defect and why the alternatives are weaker.
```

## 3. Recurrence detector

```text
Determine whether this correction is a one-time edit or evidence of a recurring system defect.

Correction history:
[list occurrences, users, dates, or task variants]

Assess:
- recurrence frequency
- cross-user impact
- business consequence
- whether the correction is stable
- whether it belongs in configuration
- recommended owner and review cadence
```

## 4. Project-instruction candidate

```text
Convert this validated recurring correction into a precise Project instruction.

Correction:
[describe correction]

Write the instruction with:
- trigger
- required behavior
- evidence boundary
- failure behavior
- observable output

Then apply the two-reader test and identify any conflicts with existing instructions.
```

## 5. Skill promotion test

```text
Assess whether this successful multi-step fix should become a Skill.

Procedure:
[list steps]

Evaluate:
- repetition frequency
- procedural complexity
- need for examples, scripts, or resources
- activation conditions
- scope
- governance or permission implications
- tests required before release

Return: keep local / Project instruction / Skill / deterministic workflow control.
```

## 6. Deterministic-control check

```text
Review this proposed natural-language instruction and identify any requirement that should instead be enforced with code, query logic, schema validation, or a release gate.

Instruction:
[paste instruction]

Separate:
- judgment suitable for instructions
- facts suitable for maintained knowledge
- procedure suitable for a Skill
- exact logic suitable for deterministic control
- approval suitable for a human workflow gate
```

## 7. One-variable validation plan

```text
Design a controlled test for this feedback-driven adjustment.

Original defect:
[describe]

Hypothesis:
[describe]

Proposed change:
[one change]

Create:
- original failing case
- control case
- representative normal cases
- edge cases
- success criteria
- regression risks
- governance checks
- keep / revise / revert decision rule
```

## 8. Promotion decision record

```text
Create a promotion decision record for a validated correction.

Include:
- task or workflow
- recurring defect
- source of feedback
- root cause
- tested adjustment
- validation evidence
- chosen configuration layer
- scope
- owner
- approval
- version
- rollback
- review trigger
- residual risk
```

## 9. Lost-fix audit

```text
Audit this recurring workflow for fixes that users repeatedly rediscover but have not captured.

Workflow:
[describe]

Manual corrections:
[list corrections]

For each correction, identify:
- frequency
- current informal workaround
- correct durable home
- risk if omitted
- validation needed
- owner
- migration step
```

## 10. Feedback-quality critique

```text
Evaluate whether each feedback statement is specific enough to drive a controlled adjustment.

Feedback statements:
[list]

For each:
- reaction or instruction?
- observable defect?
- missing condition?
- controlling lever identifiable?
- improved wording
```

## 11. Campaign-brief exercise

```text
A recurring campaign brief omits the target segment and buries the call to action.

Develop:
- diagnosis
- two precise standing instructions
- validation set
- promotion decision
- conflict check
- rollback rule
```

## 12. Test-account exclusion exercise

```text
A monthly report repeatedly includes internal test accounts unless the analyst manually reminds Claude to exclude them.

Explain why a conversation reminder is insufficient.
Design a durable repair using:
- authoritative business rule
- deterministic filter
- verification check
- shared documentation
- owner and review trigger
```

## 13. Memory versus configuration

```text
Compare Memory with deliberate configuration for this recurring correction.

Correction:
[describe]

Assess:
- scope
- sharing
- authority
- versioning
- testability
- reviewability
- reliability

Recommend the correct home and explain why.
```

## 14. Oral certification drill

```text
Ask me five scenario questions about adjusting an AI workflow from feedback.
Require me to:
- convert a reaction into an instruction
- identify the controlling lever
- choose a durable configuration layer
- define validation
- distinguish a local fix from a promoted fix

After each answer, grade the reasoning and explain the strongest alternative.
```

## 15. Full feedback-loop synthesis

```text
For this recurring workflow, build an end-to-end feedback improvement loop:

Workflow:
[describe]

Include:
1. output review
2. critique capture
3. reaction-to-instruction translation
4. root-cause and lever selection
5. bounded change
6. validation
7. promotion decision
8. versioning and approval
9. monitoring
10. rollback and re-review
```

## Public-repository rule

Use fictional, synthetic, public, or sanitized scenarios. Do not include confidential prompts, private outputs, production logs, client data, credentials, internal review records, or reconstructed proprietary course questions.