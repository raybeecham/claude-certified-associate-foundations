# Notes: Claude Platform & Model Foundations

## 1. Begin with the operating requirement

A platform decision should follow the task, not precede it. Ask:

- Is this a one-time, human-led task or a repeatable system?
- Does the user need an interactive conversation, an application integration, or a long-running managed process?
- Which data may be processed?
- Which actions, tools, and repositories must be accessed?
- What quality, latency, throughput, and cost thresholds apply?
- Who is accountable for the outcome?
- What must be logged and reproducible?

A simple interactive surface may be best for exploratory work. An API-backed application is more appropriate when requests, data, validation, and user experience must be controlled programmatically. A managed agent capability may fit long-running work, but only when its autonomy and infrastructure match the risk and governance requirements.

## 2. Select model characteristics, not prestige

Do not equate “best” with “largest” or “most capable.” Select against a measurable service profile.

| Requirement | What to test |
|---|---|
| Task quality | Accuracy, reasoning, instruction following, grounding |
| Latency | Time to first token and end-to-end time |
| Throughput | Concurrent requests and batch behavior |
| Cost | Input, output, caching, tooling, and operational costs |
| Context | Expected evidence and conversation size |
| Output | Required response length and structure |
| Tools | Tool selection and parameter reliability |
| Modality | Text, code, images, files, or other supported inputs |
| Governance | Region, provider, access, logging, retention, and policy |
| Stability | Version identifiers, deprecation path, and regression behavior |

A high-volume classification workflow may favor a faster, lower-cost model that meets a validated quality threshold. A complex cross-document analysis may require more reasoning capability and a larger context budget. Both decisions must be demonstrated on representative data.

## 3. Keep four concepts separate

### Context capacity

The context is the information available to the model for the current interaction. It may include trusted instructions, conversation turns, retrieved documents, tool results, and examples.

A larger context does not guarantee better answers. Irrelevant or conflicting content can reduce focus. Context must also obey data-access rules.

### Maximum output

The allowed generated response length is not the same as the context capacity. A request can fit within context and still be truncated because the output budget was too small or another stop condition occurred.

### Knowledge freshness

The model's pretrained knowledge has a boundary. Current facts can come from supplied documents or approved retrieval tools, but the model should not be assumed to know a newly issued policy simply because the prompt asks about “the latest.”

### Application state

API interactions are commonly stateless at the service boundary. The surrounding application stores and resends the conversation or the relevant compressed state. A developer must decide what to retain, summarize, redact, expire, and include.

Exam shortcut:

> Context is what the model can use now. State is what the application remembers and reconstructs. Freshness is where current evidence comes from. Output limit is how much can be generated.

## 4. Understand the request boundary

A robust request distinguishes:

- **trusted reusable instructions**, such as role, policy, and output requirements;
- **current user intent**, such as the task being requested;
- **task data**, which may be untrusted;
- **retrieved evidence**, which has source authority and freshness attributes;
- **tools**, which expose narrow actions through schemas; and
- **generation controls**, such as output budget and platform-supported settings.

Do not place secrets in any of these text fields. Use a secret manager and pass credentials through the surrounding application to the authorized integration.

### Instruction authority

Durable, trusted behavior belongs in the highest appropriate configuration layer. Task-specific inputs belong in the current request. Retrieved content and tool output are evidence, not a higher-priority authority merely because they contain imperative language.

## 5. Responses are structured events

A response is more than visible prose. Production systems should inspect:

- content blocks;
- tool requests;
- stop reason;
- input and output usage;
- errors and rate-limit metadata;
- request or trace identifiers; and
- model and API version identifiers.

A stop reason associated with a length limit means the system must handle possible truncation. A tool-use stop means the application must validate and execute or reject the requested tool call, then continue according to its workflow. A refusal or error requires a safe fallback, not blind retries.

## 6. Multi-turn interactions

Conversation history should be deliberate.

Questions to answer:

- Which turns remain relevant?
- Which sensitive content must be removed?
- Should older details be summarized?
- How is a summary validated?
- What happens when the context approaches its limit?
- How does the system prevent untrusted content from becoming durable instruction?
- How are user identity and authorization rechecked across turns?

Avoid the mental model that Claude independently remembers every conversation. Persistence is a product or application feature with its own scope and controls.

## 7. Versioning and migration

Model aliases and product behavior can change. A production integration should record explicit versions where appropriate and maintain a migration process.

### Minimum migration process

1. Freeze the current prompt, tools, source set, and evaluation data.
2. Run the baseline model and record metrics.
3. Run the candidate model on the same cases.
4. Compare quality, grounding, structured-output validity, tool behavior, latency, and cost.
5. Review high-severity failures individually.
6. Update prompts only when evidence shows the need.
7. Stage rollout with monitoring and rollback.
8. Update documentation and approval records.

Do not change the model, prompt, tool descriptions, and retrieval logic simultaneously. That destroys attribution.

## 8. Observability

At minimum, capture enough metadata to reconstruct a result without logging unnecessary sensitive content.

Recommended fields:

- timestamp and environment;
- use-case and workflow identifier;
- model and version;
- prompt/configuration version;
- source-set or knowledge version;
- tool definitions and tool-call results;
- input/output token counts;
- latency by stage;
- stop reason and error classification;
- validation results;
- human approval status; and
- final disposition.

Apply minimization, redaction, access control, and retention policy to logs.

## 9. Common misconceptions

| Misconception | Better mental model |
|---|---|
| “The model remembers prior calls.” | The product or application manages state and supplies relevant context. |
| “A larger context always improves quality.” | Relevance, authority, and organization matter as much as capacity. |
| “The strongest model is always safest.” | Safety depends on system controls, evidence, permissions, evaluation, and human accountability. |
| “A valid API response means the task succeeded.” | Validate content, schema, grounding, stop reason, and workflow outcome. |
| “A model migration is a drop-in upgrade.” | Treat it as a controlled change requiring regression tests. |
| “Current facts are part of the model.” | Supply or retrieve authoritative current evidence. |

## 10. Review questions

1. Why might a lower-cost model be the correct production choice?
2. How does application state differ from context?
3. What evidence would you collect when an answer ends abruptly?
4. Why should a model migration use the same evaluation set as the baseline?
5. Which platform decision factors are technical, and which are governance-related?
