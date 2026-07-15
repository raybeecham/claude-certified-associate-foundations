# Deterministic vs. Generative

## Two kinds of work

AI systems combine components that behave differently.

### Generative components

Useful for:

- drafting;
- synthesis;
- interpretation;
- classification;
- explanation;
- planning; and
- producing options.

Characteristics:

- outputs may vary;
- wording can be fluent but wrong;
- behavior depends on context;
- edge cases require evaluation; and
- uncertainty must be managed.

### Deterministic components

Useful for:

- calculations;
- exact business rules;
- schema validation;
- identity and authorization;
- database state;
- side effects;
- limits and thresholds;
- audit logging; and
- release gates.

Characteristics:

- the same inputs and method should produce the same result;
- rules can be inspected and tested;
- failures can often be detected automatically; and
- correctness still depends on valid inputs and logic.

## Architecture rule

```text
Generative model proposes, interprets, or explains.
Deterministic system calculates, constrains, validates, or acts.
Human or authorized policy owns consequential judgment.
```

## Examples

| Task | Correct component |
|---|---|
| Summarize a policy | Generative model |
| Determine whether a citation exists | Deterministic check plus source review |
| Calculate financial exposure | Code |
| Explain the exposure | Generative model |
| Enforce a spending limit | Application rule |
| Recommend an exception | Generative analysis |
| Approve the exception | Authorized human or policy system |

## Common error

Do not replace deterministic controls with stronger wording.

“Always calculate correctly” is not a calculation control.

“Never access unauthorized data” is not an authorization system.

“Only take safe actions” is not an approval gate.

## Validation equation

```text
Valid input
   +
Valid method
   +
Successful execution
   +
Validated interpretation
   =
Usable result
```

## Decision rule

> If the requirement can be expressed as an exact rule, calculation, permission, or state transition, prefer a deterministic component.
