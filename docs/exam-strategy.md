# Exam Strategy

## Read the scenario before the options

Identify five elements:

1. **Objective:** What outcome is required?
2. **Failure:** What is going wrong?
3. **Constraint:** What cannot change?
4. **Risk:** What harm must be prevented?
5. **Decision layer:** Is the best fix in the prompt, data, model choice, workflow, tool contract, evaluation, governance, or operations?

This prevents plausible but irrelevant options from controlling your interpretation.

## Use the lowest appropriate control layer

A recurring decision pattern is to fix the problem at the layer that actually owns it.

| Problem | Strong first control |
|---|---|
| Vague task | Clear instructions and success criteria |
| Inconsistent category boundaries | Representative examples and evaluation |
| Invalid JSON | Structured output or schema validation |
| Exact arithmetic | Deterministic code or calculator |
| Unsupported claims | Source restriction, citations, and validation |
| Wrong tool | Better tool descriptions and schemas |
| Excessive access | Least privilege and authorization boundaries |
| Stale knowledge | Source register, authority, and refresh process |
| High-impact decision | Qualified human review and disclosure |
| Latency regression | Stage-level measurement before optimization |

Do not choose a larger architecture change when a more direct control solves the stated issue.

## Recognize attractive distractors

### “Use the most capable model”

Model capability can help, but it does not replace clear task definition, trusted evidence, validation, or workflow controls. Choose models against measurable quality, latency, and cost requirements.

### “Add more instructions”

More instructions can make prompts harder to follow. Prefer prioritized, non-conflicting instructions with clear data boundaries and examples.

### “Let the model decide everything”

Models are useful for language and judgment under uncertainty. Deterministic code is usually better for exact calculations, hard business rules, validation, authorization, and irreversible side effects.

### “Add a human somewhere”

Human review is meaningful only when the reviewer is qualified, sees the right evidence, has decision authority, and occurs before the consequential action.

### “Retry the request”

Retries may help transient failures. They do not fix malformed schemas, ambiguous tools, stale knowledge, policy conflicts, prompt injection, or systematic evaluation failures.

## Elimination sequence

When uncertain, eliminate options that:

- ignore the stated constraint;
- solve a different problem;
- grant unnecessary access;
- remove traceability;
- hide uncertainty;
- rely on unverified model output for a high-impact action;
- bypass current policy; or
- add complexity without a measurable need.

## Time management

- Make a first pass on clear questions.
- Mark questions requiring comparison of two plausible controls.
- On review, restate the scenario in one sentence.
- Change an answer only when you can name the overlooked fact or principle.
- Do not infer hidden requirements that are absent from the scenario.

## Post-practice review

For every missed question, write:

- the clue you missed;
- why your selected option was attractive;
- the rule that makes the best option superior;
- a real-world example; and
- one new variation that would change the answer.
