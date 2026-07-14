# Quiz: Claude Platform & Model Foundations

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. An analyst needs to compare two approved policy documents, explore several interpretations, and remain responsible for the final conclusions. There is no integration requirement and the task is occasional. Which approach is the best initial fit?

- **A.** Use an approved interactive Claude experience for human-led analysis.
- **B.** Build a fully autonomous agent with write access to the policy repository.
- **C.** Create a batch API service before the analyst has tested the workflow.
- **D.** Embed the documents in a public website so any model can access them.

### 2. A developer sends a second Messages API request containing only the text, “Now summarize the risks.” Claude does not appear to know the earlier discussion. What is the best explanation and corrective action?

- **A.** The model forgot because the temperature was too high; lower it.
- **B.** The application must preserve and resend the relevant conversation history or a validated state representation.
- **C.** The developer should add the word “remember” to the user message.
- **D.** The API can retain state only after a tool call.

### 3. A team must classify millions of short public documents into six routing categories. Several candidate models meet the required accuracy on a representative test set. Which selection rule is strongest?

- **A.** Always select the model with the largest context window.
- **B.** Always select the newest model regardless of measured results.
- **C.** Select the fastest, lowest-total-cost candidate that still meets all quality, throughput, governance, and reliability thresholds.
- **D.** Select the model that produces the longest explanations.

### 4. A request containing several documents is accepted, but the response stops midway through a required table. Which distinction should the team investigate first?

- **A.** The difference between a system prompt and a user prompt
- **B.** The difference between cached and uncached tokens
- **C.** The difference between training data and fine-tuning data
- **D.** The difference between available context capacity and the allowed generated output, including the reported stop reason

### 5. A production team plans to move to a new Claude model version. Which action provides the strongest basis for approval?

- **A.** Ask one developer whether the outputs look better.
- **B.** Run the candidate and baseline on the same representative evaluation set, compare severity-weighted results, latency, cost, and tool behavior, then stage rollout with rollback.
- **C.** Change the model, prompt, retrieval system, and schemas at the same time to maximize improvement.
- **D.** Rely on the model release date as evidence that the migration is safe.

### 6. A service must always cite approved evidence and must never treat retrieved documents as instructions. Where should this durable behavior be defined?

- **A.** In trusted, version-controlled system or application configuration, reinforced by retrieval and validation controls
- **B.** Only in the last sentence of every user's task
- **C.** Inside each retrieved document
- **D.** In a hidden field supplied by the downstream reader

### 7. A structured report is incomplete and the response metadata indicates generation ended because a token limit was reached. What does this most directly indicate?

- **A.** The source documents were necessarily false.
- **B.** The user's identity was invalid.
- **C.** The generated output was truncated and the workflow must adjust the output budget, reduce scope, or decompose the task.
- **D.** The model selected the wrong tool.

### 8. A user asks whether a system complies with a regulation issued last week. What is the best design response?

- **A.** Assume the model's pretrained knowledge includes the regulation.
- **B.** Ask Claude to be extra confident.
- **C.** Use a longer output budget.
- **D.** Supply or retrieve the current authoritative regulation, establish its effective scope, and validate the answer against that evidence.

<details>
<summary>Answer key and rationales</summary>

### 1. An analyst needs to compare two approved policy documents, explore several interpretations, and remain responsible for the final conclusions. There is no integration requirement and the task is occasional. Which approach is the best initial fit?

- **A.** Use an approved interactive Claude experience for human-led analysis.
- **B.** Build a fully autonomous agent with write access to the policy repository.
- **C.** Create a batch API service before the analyst has tested the workflow.
- **D.** Embed the documents in a public website so any model can access them.

**Answer: A**

**Rationale:** An approved interactive experience matches an occasional, exploratory, human-led task with no integration requirement. Environment and data controls still must be verified.

**Why the other options are weaker:**

- **B:** This adds unnecessary autonomy and overly broad write access.
- **C:** An API service may become useful later, but it adds engineering before the task is validated.
- **D:** Publishing internal evidence creates an unacceptable data-handling risk.

**Objective:** Product surface selection  
**Reference:** https://platform.claude.com/docs/en/intro

### 2. A developer sends a second Messages API request containing only the text, “Now summarize the risks.” Claude does not appear to know the earlier discussion. What is the best explanation and corrective action?

- **A.** The model forgot because the temperature was too high; lower it.
- **B.** The application must preserve and resend the relevant conversation history or a validated state representation.
- **C.** The developer should add the word “remember” to the user message.
- **D.** The API can retain state only after a tool call.

**Answer: B**

**Rationale:** The application is responsible for managing the relevant conversational state and supplying it with the request. State retention must also follow privacy and context-management rules.

**Why the other options are weaker:**

- **A:** Sampling settings do not restore missing conversation context.
- **C:** A request cannot reference information that was not supplied through the product or application state.
- **D:** Tool use is unrelated to whether the application includes prior turns.

**Objective:** Application-managed state  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/working-with-messages

### 3. A team must classify millions of short public documents into six routing categories. Several candidate models meet the required accuracy on a representative test set. Which selection rule is strongest?

- **A.** Always select the model with the largest context window.
- **B.** Always select the newest model regardless of measured results.
- **C.** Select the fastest, lowest-total-cost candidate that still meets all quality, throughput, governance, and reliability thresholds.
- **D.** Select the model that produces the longest explanations.

**Answer: C**

**Rationale:** Once hard requirements are met, model selection should optimize the full operational profile, including latency, throughput, cost, governance, and reliability.

**Why the other options are weaker:**

- **A:** The task uses short documents, so maximum context may not be decision-relevant.
- **B:** Recency does not prove fit for the validated use case.
- **D:** Long explanations may increase cost and are not the required output.

**Objective:** Model selection  
**Reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 4. A request containing several documents is accepted, but the response stops midway through a required table. Which distinction should the team investigate first?

- **A.** The difference between a system prompt and a user prompt
- **B.** The difference between cached and uncached tokens
- **C.** The difference between training data and fine-tuning data
- **D.** The difference between available context capacity and the allowed generated output, including the reported stop reason

**Answer: D**

**Rationale:** A request can fit within context yet still end because generation reached an output limit or another stop condition. The response metadata is critical evidence.

**Why the other options are weaker:**

- **A:** Prompt roles may affect behavior but do not explain the abrupt ending by themselves.
- **B:** Caching can affect performance and cost, not usually the logical completion boundary.
- **C:** Training methodology is not the immediate operational diagnostic.

**Objective:** Context and output limits  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 5. A production team plans to move to a new Claude model version. Which action provides the strongest basis for approval?

- **A.** Ask one developer whether the outputs look better.
- **B.** Run the candidate and baseline on the same representative evaluation set, compare severity-weighted results, latency, cost, and tool behavior, then stage rollout with rollback.
- **C.** Change the model, prompt, retrieval system, and schemas at the same time to maximize improvement.
- **D.** Rely on the model release date as evidence that the migration is safe.

**Answer: B**

**Rationale:** A controlled comparison on the same cases isolates the model change and reveals regressions. Staging, monitoring, and rollback make the release operationally safe.

**Why the other options are weaker:**

- **A:** Anecdotal review is not representative or measurable.
- **C:** Changing several components destroys attribution and complicates rollback.
- **D:** A newer release does not guarantee performance for this use case.

**Objective:** Model migration  
**Reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 6. A service must always cite approved evidence and must never treat retrieved documents as instructions. Where should this durable behavior be defined?

- **A.** In trusted, version-controlled system or application configuration, reinforced by retrieval and validation controls
- **B.** Only in the last sentence of every user's task
- **C.** Inside each retrieved document
- **D.** In a hidden field supplied by the downstream reader

**Answer: A**

**Rationale:** Durable behavior belongs in trusted configuration and must be supported by system controls. Retrieved documents remain evidence and cannot define their own authority.

**Why the other options are weaker:**

- **B:** User wording is not a reliable place for mandatory application policy.
- **C:** A retrieved document is untrusted content and can contain prompt injection.
- **D:** A downstream field cannot reliably control model behavior or retrieval authority.

**Objective:** Instruction placement  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 7. A structured report is incomplete and the response metadata indicates generation ended because a token limit was reached. What does this most directly indicate?

- **A.** The source documents were necessarily false.
- **B.** The user's identity was invalid.
- **C.** The generated output was truncated and the workflow must adjust the output budget, reduce scope, or decompose the task.
- **D.** The model selected the wrong tool.

**Answer: C**

**Rationale:** A length-related stop reason directly indicates incomplete generation. The application should handle partial output and change the output design or budget.

**Why the other options are weaker:**

- **A:** Source truth is not established by the stop reason.
- **B:** Identity failures occur before or outside normal generation.
- **D:** Tool selection is a separate issue and would require different evidence.

**Objective:** Response metadata  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 8. A user asks whether a system complies with a regulation issued last week. What is the best design response?

- **A.** Assume the model's pretrained knowledge includes the regulation.
- **B.** Ask Claude to be extra confident.
- **C.** Use a longer output budget.
- **D.** Supply or retrieve the current authoritative regulation, establish its effective scope, and validate the answer against that evidence.

**Answer: D**

**Rationale:** Current legal or policy claims require current authoritative evidence. The system must distinguish model knowledge from evidence supplied in the interaction.

**Why the other options are weaker:**

- **A:** Training knowledge should not be assumed current enough for a regulation issued last week.
- **B:** Confidence wording does not create evidence.
- **C:** More output does not improve source freshness.

**Objective:** Knowledge freshness  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

</details>
