# Lesson 2: How Claude Behaves

## Overview

Claude is a generative AI system, not a database, search index, or traditional rule-based application. It produces responses from the instructions and information available in the current interaction. Because generation is probabilistic, a useful workflow must account for variation, uncertainty, finite context, knowledge boundaries, and the continued need for review.

This lesson introduces five behavioral properties that apply across Claude features and models:

1. Responses vary.
2. Fluent confidence is not evidence of accuracy.
3. Context is a budget.
4. Knowledge has a training boundary.
5. Configuration reduces variation but does not eliminate it.

> [!IMPORTANT]
> These properties are not defects that can be removed with one perfect prompt. They are operating characteristics that should shape the workflow around the model.

## Learning objectives

After completing this lesson, you should be able to:

- explain why identical requests may produce different acceptable outputs;
- separate writing fluency from factual reliability;
- treat context as a finite and managed resource;
- identify when current or authoritative evidence must be supplied;
- explain why Skills, templates, and standing instructions improve consistency without guaranteeing identical results; and
- design a review loop that matches the consequence of the task.

## A practical mental model

A typical interaction can be viewed as a pipeline:

```text
User task
    |
    v
Instructions + conversation + supplied evidence + tool results
    |
    v
Probabilistic generation
    |
    v
Candidate response
    |
    v
Validation, evidence check, and human review as required
    |
    v
Accepted, revised, or rejected output
```

The visible answer is a candidate output. Whether it is fit for use depends on the task's success criteria and the evidence supporting it.

---

## Property 1: Responses vary

### What the property means

Do not assume that the same prompt will always produce the same wording, organization, examples, or emphasis. Multiple continuations can satisfy the request, and Claude may select a different one on another run.

For an open-ended prompt such as:

```text
Explain zero trust to a nontechnical executive in one paragraph.
```

one response may lead with continuous verification, another may lead with the absence of implicit trust, and a third may emphasize identity and access controls. The responses can differ while still meeting the objective.

### What should remain stable

Variation is acceptable only inside the boundaries of the task. A well-designed workflow defines which properties may vary and which must not.

| May vary | Should remain controlled |
|---|---|
| Wording | Required facts |
| Examples | Output schema |
| Sentence order | Safety and policy constraints |
| Tone within an approved range | Required sections |
| Supporting explanation | Source restrictions |
| Creative options | Decision criteria |

### Workflow implication

Do not validate generative output with exact string matching unless the task truly requires an exact string. Evaluate against a rubric or contract instead:

- Did the response answer the requested question?
- Did it include every required field or section?
- Are factual claims supported?
- Did it follow the source and formatting constraints?
- Does it stay within the approved scope?

### Example prompt: observe controlled variation

```text
Create three executive summaries of the same source text.

Keep these elements invariant:
- factual claims;
- stated risks;
- recommendation priority; and
- maximum length of 150 words.

Vary only the organization and wording. After the summaries, explain whether any variation changed the meaning.
```

### Engineering rule

Design for semantic consistency, not identical prose.

---

## Property 2: Confident tone is not a signal of accuracy

### What the property means

Claude can state a correct fact, an unsupported inference, or a fabricated detail with similarly polished language. Style is visible. Factual grounding is a separate property that must be checked.

A professional tone may increase readability, but it does not provide evidence.

### Common failure pattern

```text
Plausible wording
    +
Specific-looking dates or statistics
    +
No authoritative source
    =
High risk of uncritical acceptance
```

### Verification hierarchy

Use the strongest evidence available for the task:

1. Authoritative source material supplied in the interaction.
2. Approved internal systems or connectors.
3. Current primary sources obtained through web search or Research.
4. Independent calculation or execution when the claim is computable.
5. Human subject-matter review for consequential judgments.

A model's self-critique can reveal possible weaknesses, but it is not independent verification. Asking Claude whether it is correct does not create a new source of truth.

### Example prompt: evidence-aware response

```text
Answer using only the supplied sources.

For each material claim, provide:
- the supporting source;
- the relevant section or page when available;
- whether the claim is explicit or inferred; and
- any uncertainty or missing evidence.

If the sources do not support an answer, state: "Insufficient evidence in the supplied material."
```

### Example prompt: publication review

```text
Review the draft as a quality-assurance analyst.

Classify each factual statement as:
1. directly supported by the supplied evidence;
2. a reasonable inference that requires review;
3. unsupported; or
4. dependent on current external information.

Do not invent citations. Return a verification checklist before revising the draft.
```

### Engineering rule

Treat fluency as a presentation characteristic, not a confidence score.

---

## Property 3: Context is a budget

### What the property means

Claude can use only the information available within the effective context of the current interaction. Context may include:

- trusted or standing instructions;
- current user messages;
- prior conversation turns;
- uploaded or retrieved documents;
- examples;
- tool definitions and tool results; and
- summaries of earlier material.

Context is finite. More context is not automatically better context. Irrelevant, duplicated, outdated, or conflicting material can make the task harder.

### Compression is not perfect persistence

In some Claude app configurations, earlier conversation content may be summarized as a thread grows. Summarization allows work to continue, but it compresses detail. Fine-grained constraints, exceptions, and exact wording can lose influence if they are not preserved deliberately.

Product behavior and plan availability can change. Verify current details in the official Claude Help Center rather than treating plan-specific behavior as permanent.

### Symptoms of context degradation

- Claude repeats questions already answered.
- An early constraint is no longer followed.
- Terminology changes unexpectedly.
- A previously rejected assumption returns.
- The response mixes unrelated workstreams.
- Citations or source boundaries become less precise.

### Context-management responses

| Situation | Recommended response |
|---|---|
| A long thread remains coherent | Continue and monitor |
| Important details are scattered | Create a structured checkpoint summary |
| Earlier instructions are losing force | Restate the authoritative constraints |
| The task has shifted substantially | Start a new conversation |
| The work recurs with stable background | Move it into a Project |
| The source set is too broad | Curate, partition, or retrieve only relevant evidence |

### Example prompt: context checkpoint

```text
Create a continuation brief for this workstream.

Preserve exactly:
- objective;
- approved scope;
- authoritative sources;
- decisions already made;
- constraints and exceptions;
- unresolved questions;
- rejected assumptions;
- required output format; and
- next actions.

Separate confirmed information from inference. Do not add new decisions.
```

### Security perspective

Do not allow untrusted content to become durable instruction merely because it appeared earlier in the conversation. Keep source material, user requests, and trusted configuration conceptually separate. Revalidate identity, authorization, and data access outside the prompt when a workflow spans multiple turns.

### Engineering rule

Optimize context for relevance, authority, and structure, not maximum size.

---

## Property 4: Knowledge has a training boundary

### What the property means

A model's pretrained knowledge has a cutoff. It should not be assumed to know a newly issued regulation, current market price, recent vulnerability, current office-holder, updated product feature, or today's event unless current evidence is available in the interaction.

Current information can be supplied through:

- uploaded documents;
- approved connectors or enterprise sources;
- web search for targeted current lookups; or
- Research for deeper multi-source investigation and synthesis.

### Stable knowledge versus current evidence

| Task | Likely source strategy |
|---|---|
| Explain a stable technical concept | Model knowledge may be sufficient, with normal review |
| Interpret a newly issued policy | Supply or retrieve the policy |
| Report a current statistic | Use a current primary source |
| Compare current vendor capabilities | Retrieve current vendor documentation |
| Analyze an internal procedure | Supply the approved internal version |
| Summarize breaking news | Use current sources and verify publication dates |

### Example prompt: current-information boundary

```text
Answer as of [YYYY-MM-DD].

Use only current, authoritative sources. Prefer primary sources over summaries.
For every time-sensitive claim, cite the source and publication or effective date.
If current evidence is unavailable, say so explicitly rather than relying on pretrained knowledge.
```

### Example prompt: supplied-source boundary

```text
Use the attached policy as the sole authority for policy requirements.
You may use general knowledge only to explain terminology, not to add requirements.
If the policy is silent on a question, label the issue as a gap.
```

### Engineering rule

When freshness matters, connect evidence. Do not prompt harder for facts the model cannot reliably know.

---

## Property 5: Configured procedures still produce varied outputs

### What the property means

Standing instructions, Skills, templates, examples, and output schemas can reduce variance. They make the procedure more explicit and can improve repeatability. They do not turn generation into a guaranteed deterministic process.

A configured workflow can standardize:

- the sequence of analysis;
- required inputs;
- output sections;
- terminology;
- formatting;
- source restrictions;
- escalation rules; and
- review criteria.

It cannot, by configuration alone, guarantee:

- factual correctness;
- identical wording;
- complete extraction from every input;
- correct judgment in ambiguous cases;
- safe tool execution; or
- compliance with controls enforced only in natural language.

### Example output contract

```text
Return exactly these sections:
1. Scope
2. Evidence reviewed
3. Findings
4. Uncertainties
5. Recommendations
6. Required human decisions

For every finding, include:
- severity;
- evidence;
- rationale; and
- confidence basis.

Do not assign a final approval decision.
```

### Repeatability pattern

```text
Configured procedure
        |
        v
Generated candidate output
        |
        v
Schema and rule validation
        |
        v
Evidence validation
        |
        v
Human review when consequence requires it
```

### Engineering rule

Configuration narrows the solution space. Evaluation determines whether the result is acceptable.

---

## The five-property operating table

| Property | Incorrect expectation | Better workflow response |
|---|---|---|
| Responses vary | The same prompt should produce one canonical answer | Define invariants and evaluate against a rubric |
| Confidence is not accuracy | Polished language means the claim is reliable | Require evidence and verification |
| Context is a budget | Claude will retain every detail indefinitely | Curate, checkpoint, restart, or persist deliberately |
| Knowledge has a boundary | Claude automatically knows the latest facts | Connect current authoritative sources |
| Configuration does not eliminate variance | A Skill guarantees a perfect repeatable result | Validate every run and review consequential outputs |

## Think like an AI engineer

Before accepting a Claude output, classify the task:

| Task type | Primary concern | Minimum control |
|---|---|---|
| Creative and reversible | Usefulness | User review |
| Structured and repetitive | Consistency | Output contract and tests |
| Factual | Grounding | Source verification |
| Current-information dependent | Freshness | Current authoritative retrieval |
| High-impact or irreversible | Consequence | Strong validation and accountable human approval |

The right review loop depends on consequence, not merely on how impressive the response sounds.

## Practical examples

### Example 1: Security briefing

A security team asks Claude to summarize a public advisory for executives. Different summaries may use different wording, but the affected products, severity, dates, and recommended actions must remain aligned with the advisory. The workflow should restrict the answer to the source, require citations, and include human review before distribution.

### Example 2: Recurring policy analysis

A team uses a configured procedure to map policies to a control framework. The template can standardize the sections and mapping method. Review is still required because ambiguous policy language may produce different interpretations across runs.

### Example 3: Code review

Claude may identify different maintainability issues on repeated reviews of the same repository. A reliable process combines a defined rubric, automated tests and static analysis, traceable findings, and engineer review instead of relying on one generated pass.

## Hands-on lab: Observe and control model behavior

### Objective

Observe the five behavioral properties and document which workflow controls reduce risk.

### Exercise 1: Response variation

Run this prompt three times in separate conversations:

```text
Explain zero trust to a nontechnical executive in 120 words or fewer.
Include one analogy and three practical implications.
```

Record:

- what stayed constant;
- what varied;
- whether any variation changed the meaning; and
- which rubric would determine acceptance.

### Exercise 2: Confidence versus evidence

Provide Claude with one authoritative public document and ask for a five-point briefing. Then request an evidence table mapping each point to the source. Identify any claim that is not directly supported.

### Exercise 3: Context checkpoint

Use a multi-step planning conversation. After several turns, create a continuation brief with the checkpoint prompt in this lesson. Start a new conversation using only that brief and compare which details survived.

### Exercise 4: Configured procedure

Create a reusable review template with required sections and run it twice against the same short document. Compare:

- structural consistency;
- factual consistency;
- differences in prioritization;
- unsupported claims; and
- the review effort still required.

### Observation worksheet

| Exercise | Variation observed | Risk created | Control applied | Residual review needed |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

## Common misconceptions

| Misconception | Better mental model |
|---|---|
| "Different wording means one answer is wrong." | Multiple responses can satisfy the same semantic requirements. |
| "Claude sounds certain, so the answer is verified." | Tone and factual support are independent. |
| "The conversation history is permanent memory." | Context, product memory, and application state are different mechanisms. |
| "A larger context always improves the answer." | Irrelevant or conflicting context can reduce quality. |
| "Web access makes every answer current and correct." | Current sources still require authority, date, and claim-level verification. |
| "A Skill removes the need for review." | Configuration improves consistency but does not guarantee correctness. |
| "Claude can reliably grade its own answer." | Self-review is useful, but it is not independent evidence. |

## Certification lens

Scenario questions may describe a disappointing output without naming the underlying property. Diagnose the behavior before selecting a solution.

Ask:

1. Is normal response variation being mistaken for failure?
2. Is a fluent statement being accepted without evidence?
3. Has the session's effective context become overloaded or compressed?
4. Does the task require information newer than the model's reliable knowledge?
5. Is a configured workflow being treated as a substitute for validation?

The best answer usually adds the appropriate workflow control rather than promising that one revised prompt will remove the behavior entirely.

## Knowledge check

1. Why can two answers to the same prompt both be acceptable?
2. Why is a model's confident tone not a usable accuracy metric?
3. What is the difference between context capacity and durable memory?
4. Why can automated summarization affect instructions from early in a session?
5. What should you do when a task depends on a newly issued regulation?
6. What does a Skill standardize, and what does it not guarantee?
7. Why is exact string matching usually a poor test for open-ended generation?
8. When is human approval required even if automated validation passes?

### Answer guide

1. Generative systems can produce multiple semantically valid continuations.
2. Fluency is a presentation property and does not establish factual support.
3. Context is information available now; durable memory is a product or application mechanism that carries selected information forward.
4. Summaries are compressed representations and may omit fine-grained constraints or exceptions.
5. Supply or retrieve the current authoritative source and verify claims against it.
6. It can standardize process, structure, and constraints; it does not guarantee factual correctness or identical output.
7. It penalizes harmless wording changes and does not directly test meaning, evidence, or compliance.
8. When the output is consequential, high-impact, ambiguous, or capable of causing an irreversible action.

## Flashcards

**Q:** Why may Claude answer the same prompt differently?

**A:** It generates responses probabilistically, and multiple continuations may satisfy the request.

**Q:** What should a repeatable workflow hold invariant?

**A:** Required facts, constraints, sources, structure, safety rules, and acceptance criteria.

**Q:** Does fluent writing indicate factual accuracy?

**A:** No. Fluency and factual grounding must be evaluated separately.

**Q:** Is asking Claude to check itself independent verification?

**A:** No. Self-critique may identify issues, but independent evidence is still required.

**Q:** What does "context is a budget" mean?

**A:** The model can use only a finite amount of relevant information in the current interaction, so context must be curated and managed.

**Q:** Why can a long conversation lose important detail?

**A:** Earlier content may receive less influence or be compressed into a summary that omits fine-grained information.

**Q:** How should current facts be handled?

**A:** Retrieve or supply current authoritative evidence and verify time-sensitive claims.

**Q:** What does configuration do to output variance?

**A:** It reduces and channels variance, but does not eliminate it.

**Q:** What is the appropriate validation target for an open-ended answer?

**A:** Semantic requirements, evidence, constraints, and a task-specific rubric, not identical wording.

**Q:** What determines the strength of the review process?

**A:** The consequence, reversibility, and uncertainty of the task.

## Key takeaways

- Variation is expected. Define what may vary and what must remain fixed.
- Confidence is not evidence. Verify important claims independently.
- Context is finite. Curate, checkpoint, partition, and restart deliberately.
- Current information requires current sources.
- Configuration improves consistency but never removes the need for evaluation.
- Claude should be one component in a controlled workflow, not the sole authority for consequential decisions.

## Related repository material

- [Module introduction](01-module-introduction.md)
- [Broader platform notes](../notes.md)
- [Behavior prompt notebook](../../../prompts/module-01/02-how-claude-behaves-prompts.md)
- [Grounded analysis template](../../../prompts/grounded-analysis-template.md)
- [Evaluator rubric template](../../../prompts/evaluator-rubric-template.md)

## Official reading

Product capabilities and availability can change. Verify current behavior before relying on plan-specific details.

- [Claude Help Center](https://support.claude.com/en/)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
