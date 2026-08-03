# Module 4 Notebook: Analyzing Requirements and Use Cases

Use these study prompts to convert messy source material into traceable requirements and viable use cases. Do not replace authorized interpretation or approval.

## 1. Business-need decomposition

```text
Translate this business need into candidate task definitions:
[NEED]

For each task define actor, purpose, trigger, authorized inputs, work, output, audience, timing, constraints, owner, approver, acceptance criteria, and escalation behavior.
Mark absent decisions `clarification required`.
```

## 2. Source-package inventory

```text
Inventory each supplied source by name, type, date/version, role, authority, duplicate status, conflicts, missing metadata, and Include/Exclude/Replace/Clarify decision.
Then state the proposed source hierarchy. Do not silently choose a controlling source when authority is unclear.
```

## 3. Atomic requirement extraction

```text
Use only the supplied sources. Extract one independently trackable requirement per row.
Return ID, label, full text, class, source, exact location, conditions, status, owner, and acceptance criterion.
Classes: explicit, implied, ambiguous, missing, conflicting, assumption, constraint, acceptance criterion.
Do not convert inference into an explicit requirement. Use `not found` when unsupported.
```

## 4. RFP requirement register

```text
Create a traceability register from the solicitation package and internal response material.
For each requirement include source location, explicit/implied status, answer coverage, internal evidence, ambiguity, owner, deadline if stated, and completion criterion.
Add separate lists for source conflicts, clarification questions, missing evidence, and possible implied requirements.
```

## 5. Answer-coverage review

```text
Compare each requirement with existing response material.
Classify coverage as Complete, Partial, Absent, Conflicting, Unsupported, or Not Applicable Pending Approval.
Cite exact response evidence and explain what remains unanswered.
```

## 6. Ambiguity and implication review

```text
Identify undefined terms, vague quantities, unclear actors or dates, multiple plausible meanings, hidden subordinate conditions, cross-references, examples mistaken for mandates, and requirements implied by evaluation criteria.
For each item provide evidence, competing interpretations, risk, and a clarification question.
Never present an implication as explicit.
```

## 7. Pressure-test pass

```text
Pressure-test the candidate register against the complete source package.
Find omissions, incorrect splitting or merging, duplicates, superseded language, amendment conflicts, missing conditions, assumptions presented as facts, weak internal answers, and untestable requirements.
Return affected IDs, evidence, severity, and repair action.
```

## 8. Requirement-quality audit

```text
Audit each requirement for necessity, traceability, clarity, atomicity, feasibility, testability, bounded scope, ownership, authorization, and currency.
Classify Pass, Fail, or Needs Clarification and recommend the smallest source-faithful correction.
```

## 9. Acceptance-criteria builder

```text
For each approved requirement define observable result, test, threshold or controlled status, evidence, reviewer, and blocking conditions.
Mark criteria provisional when interpretation is unresolved.
```

## 10. Clarification register

```text
Convert ambiguous, missing, conflicting, and implied items into questions.
Include requirement ID, question, why it matters, affected decision, temporary assumption, assumption risk, owner, and response deadline.
```

## 11. Source-authority reconciliation

```text
Compare base documents, amendments, instructions, internal notes, and examples.
For every conflict state both positions, dates/versions, proposed controlling source, authority rule, and whether human approval is still required.
```

## 12. Change-impact analysis

```text
For this changed requirement, identify effects on dependent requirements, workflow stages, data, tools, deterministic rules, roles, deliverables, tests, schedule, risk, documentation, and approval.
Preserve requirement IDs.
```

## 13. Use-case viability test

```text
Evaluate this proposed Claude use case for measurable outcome, user, current process pain, repeatability, authorized inputs, bounded AI contribution, retained human judgment, deterministic needs, tools, state, acceptance criteria, error consequence, reversibility, governing obligations, escalation, and minimum workflow complexity.
Return Viable, Viable With Constraints, Needs Clarification, or Unsuitable for AI Delegation.
```

## 14. Capability-to-use-case repair

```text
Rewrite this capability-first idea into a use case with business outcome, affected user, current process, repeatable task, authorized evidence, bounded Claude role, retained authority, validation, success measures, risks, and stopping conditions:
[IDEA]
```

## 15. Project-fit assessment

```text
Decide whether this work belongs in a Project, one-off conversation, or managed workflow.
Separate project knowledge, project instructions, reusable procedural Skill, source updates, collaboration, sensitivity, versioning, approval, and downstream actions.
```

## 16. Requirements-to-workflow handoff

```text
Convert the approved requirements into a preliminary workflow map.
For each requirement identify stage, input, actor/component, work, output, validation, human review, tool interaction, state recorded, acceptance test, and failure path.
Keep requirement IDs for traceability.
```

## 17. Oral certification drill

Explain: business need versus requirement; table versus narrative; explicit versus implied; traceability; pressure-testing; source conflicts; testability; viable use cases; Project fit; and who approves interpretation.

## Compact card

```text
OUTCOME → SOURCE HIERARCHY → ATOMIC REQUIREMENTS → CLASSIFICATION → PRESSURE TEST → CLARIFICATION → ACCEPTANCE → APPROVED USE CASE
```
