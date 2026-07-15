# Prompt Planning Canvas

Use this only after the project and workflow decisions are defined.

## 1. Objective

What should the model accomplish in this step?

> 

What is explicitly outside scope?

- 

## 2. Audience and use

**Audience:**

> 

**How the output will be used:**

> 

**Decision or next stage supported:**

> 

## 3. Inputs

| Input | Authority | Trust level | How it is delimited |
|---|---|---|---|
| | | Trusted / Untrusted / Mixed | |

## 4. Instruction hierarchy

| Instruction type | Content |
|---|---|
| Durable system or Project rules | |
| Task-specific user instruction | |
| Tool-use rules | |
| Source hierarchy | |
| Prohibited behavior | |

## 5. Required process

List the steps Claude should follow.

1. 
2. 
3. 
4. 

Which steps must be performed by code, tools, or a human instead of the model?

- 

## 6. Output contract

**Format:** Markdown / JSON / Table / Memo / Email / Code / Other

**Required sections or fields:**

- 

**Length or level of detail:**

- 

**Citation or evidence requirements:**

- 

## 7. Uncertainty behavior

Claude should:

- [ ] identify missing information;
- [ ] distinguish fact from inference;
- [ ] state assumptions;
- [ ] use `unknown` when evidence is insufficient;
- [ ] ask for clarification when safe and necessary;
- [ ] escalate high-risk ambiguity; and
- [ ] avoid inventing data.

## 8. Examples

Provide examples only when they clarify ambiguous boundaries or output structure.

**Positive example:**

> 

**Negative example:**

> 

## 9. Tool rules

| Tool | When to use | When not to use | Validation |
|---|---|---|---|
| | | | |

## 10. Acceptance criteria

The output passes when:

- 

The output fails when:

- 

## 11. Review requirements

- Deterministic checks: 
- Source checks: 
- Human reviewer: 
- Approval required before: 

## 12. Final prompt skeleton

```text
Role or operating context:
[ONLY WHEN USEFUL]

Objective:
[OBJECTIVE]

Audience and use:
[AUDIENCE AND DECISION]

Authorized inputs:
[INPUTS]

Source hierarchy:
[AUTHORITATIVE SOURCES AND CONFLICT RULES]

Constraints:
[BOUNDARIES, PROHIBITED ACTIONS, DATA RULES]

Required process:
[ORDERED STEPS]

Tools:
[WHEN AND HOW TO USE TOOLS]

Output contract:
[FORMAT, FIELDS, LENGTH, CITATIONS]

Uncertainty behavior:
[UNKNOWN, ASSUMPTIONS, ESCALATION]

Success criteria:
[ACCEPTANCE TESTS]
```

## 13. Prompt review

- [ ] The objective is specific.
- [ ] The source hierarchy is explicit.
- [ ] Untrusted content cannot redefine authority.
- [ ] The model is not asked to perform deterministic work through prose.
- [ ] Missing-data behavior is defined.
- [ ] The output can be validated.
- [ ] The prompt does not claim to enforce permissions or policy by itself.
