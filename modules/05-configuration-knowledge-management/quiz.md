# Quiz: Configuration & Knowledge Management

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. An internal knowledge document is used to answer policy questions, but no one knows whether it is current. What metadata is most important to establish first?

- **A.** The document's font and page color
- **B.** Its owner, authority, version or effective date, classification, scope, and review cadence
- **C.** How many users have downloaded it
- **D.** Whether it contains the word “policy”

### 2. Every response in a controlled application must cite approved evidence and use `insufficient_evidence` when support is absent. Where should this rule live?

- **A.** Only in each user's memory
- **B.** Only in the source documents
- **C.** In version-controlled application or system configuration, with retrieval and validation enforcing it
- **D.** In a model-generated note that is not saved

### 3. A service repeatedly sends the same long system instructions, tool definitions, and approved reference text, followed by a different short user task. Data policy permits caching. What optimization is most relevant?

- **A.** Place the stable reusable content in a consistent prompt prefix and use the platform's prompt-caching behavior, then measure actual hits.
- **B.** Move a changing timestamp to the beginning of the prompt.
- **C.** Store the API credential in the cached text.
- **D.** Randomize the order of tool definitions on each request.

### 4. A policy assistant retrieves fifty documents for every question. Answers are slow and sometimes combine conflicting versions. What is the best redesign?

- **A.** Increase the response length so all documents are discussed.
- **B.** Tell Claude to ignore conflict without identifying it.
- **C.** Remove authorization filters so retrieval is faster.
- **D.** Retrieve the smallest relevant, permitted, authoritative, current set and attach provenance and conflict metadata.

### 5. A prompt needs to call an internal search service that requires a credential. Where should the credential be stored?

- **A.** In the system prompt so Claude can copy it into the tool call
- **B.** In an example inside the repository
- **C.** In an approved secret manager, used by the application or connector without exposing the value to the model
- **D.** In the generated output with a warning

### 6. Users in Business Unit A can retrieve confidential documents from Business Unit B because the model is instructed not to reveal them. What is the correct control?

- **A.** Make the non-disclosure instruction more forceful.
- **B.** Enforce identity-aware authorization before retrieval so unauthorized documents never enter the model context.
- **C.** Ask users to promise not to request other units' data.
- **D.** Filter the final answer after the model has processed all documents.

### 7. A knowledge file has a recent upload timestamp but contains an older policy with no owner or review date. What is the primary risk?

- **A.** The system may treat stale or superseded content as authoritative because file metadata does not establish content freshness.
- **B.** The file will necessarily exceed the context window.
- **C.** The model will always refuse to read it.
- **D.** The document cannot contain any useful information.

### 8. A current public standard and a current approved internal standard give different minimum requirements. The internal standard applies to the organization and is stricter. What should the assistant do?

- **A.** Choose the shorter document.
- **B.** Blend the requirements and omit the difference.
- **C.** Select the public standard because it is public.
- **D.** Apply the documented authority and scope rules, cite both where useful, and state that the stricter internal standard governs the organization.

<details>
<summary>Answer key and rationales</summary>

### 1. An internal knowledge document is used to answer policy questions, but no one knows whether it is current. What metadata is most important to establish first?

- **A.** The document's font and page color
- **B.** Its owner, authority, version or effective date, classification, scope, and review cadence
- **C.** How many users have downloaded it
- **D.** Whether it contains the word “policy”

**Answer: B**

**Rationale:** A governed source needs accountability, authority, freshness, scope, and data-handling metadata before it can reliably support answers.

**Why the other options are weaker:**

- **A:** Formatting does not establish governance or freshness.
- **C:** Popularity is not authority.
- **D:** A keyword does not prove the document governs the use case.

**Objective:** Source governance  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 2. Every response in a controlled application must cite approved evidence and use `insufficient_evidence` when support is absent. Where should this rule live?

- **A.** Only in each user's memory
- **B.** Only in the source documents
- **C.** In version-controlled application or system configuration, with retrieval and validation enforcing it
- **D.** In a model-generated note that is not saved

**Answer: C**

**Rationale:** Durable application behavior should be governed, versioned, reviewed, and tested rather than repeated informally by each user.

**Why the other options are weaker:**

- **A:** User memory is not enforceable or auditable.
- **B:** Sources are evidence, not trusted behavioral configuration.
- **D:** An unsaved note cannot establish repeatable system behavior.

**Objective:** Reusable configuration  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 3. A service repeatedly sends the same long system instructions, tool definitions, and approved reference text, followed by a different short user task. Data policy permits caching. What optimization is most relevant?

- **A.** Place the stable reusable content in a consistent prompt prefix and use the platform's prompt-caching behavior, then measure actual hits.
- **B.** Move a changing timestamp to the beginning of the prompt.
- **C.** Store the API credential in the cached text.
- **D.** Randomize the order of tool definitions on each request.

**Answer: A**

**Rationale:** Prompt caching is designed for stable, repeatedly reused prefixes. The design must follow current platform semantics and data policy and should be verified with usage diagnostics.

**Why the other options are weaker:**

- **B:** A changing early field can invalidate the reusable prefix.
- **C:** Credentials must never be stored in prompt text or cache.
- **D:** Changing order prevents prefix reuse.

**Objective:** Prompt caching  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching

### 4. A policy assistant retrieves fifty documents for every question. Answers are slow and sometimes combine conflicting versions. What is the best redesign?

- **A.** Increase the response length so all documents are discussed.
- **B.** Tell Claude to ignore conflict without identifying it.
- **C.** Remove authorization filters so retrieval is faster.
- **D.** Retrieve the smallest relevant, permitted, authoritative, current set and attach provenance and conflict metadata.

**Answer: D**

**Rationale:** Retrieval should select high-quality evidence, not maximize volume. Authority, freshness, relevance, and access belong in the retrieval pipeline.

**Why the other options are weaker:**

- **A:** More generated text does not resolve noisy or conflicting evidence.
- **B:** Conflict must be resolved by documented authority or surfaced.
- **C:** Removing authorization creates a data exposure risk.

**Objective:** Context selection  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 5. A prompt needs to call an internal search service that requires a credential. Where should the credential be stored?

- **A.** In the system prompt so Claude can copy it into the tool call
- **B.** In an example inside the repository
- **C.** In an approved secret manager, used by the application or connector without exposing the value to the model
- **D.** In the generated output with a warning

**Answer: C**

**Rationale:** Credentials belong in a secret-management boundary and should be supplied only to the authorized service call.

**Why the other options are weaker:**

- **A:** Prompt text may be logged or exposed and is not a secret store.
- **B:** Repository examples are public or broadly accessible.
- **D:** Outputting a credential is disclosure, regardless of warning.

**Objective:** Secret management  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 6. Users in Business Unit A can retrieve confidential documents from Business Unit B because the model is instructed not to reveal them. What is the correct control?

- **A.** Make the non-disclosure instruction more forceful.
- **B.** Enforce identity-aware authorization before retrieval so unauthorized documents never enter the model context.
- **C.** Ask users to promise not to request other units' data.
- **D.** Filter the final answer after the model has processed all documents.

**Answer: B**

**Rationale:** Access control must prevent unauthorized data from reaching the model. Prompt instructions and output filtering are not substitutes for retrieval authorization.

**Why the other options are weaker:**

- **A:** Instructions do not enforce access control.
- **C:** User promises are not a technical authorization mechanism.
- **D:** Post-generation filtering is too late because the model already received the data.

**Objective:** Least-privilege retrieval  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 7. A knowledge file has a recent upload timestamp but contains an older policy with no owner or review date. What is the primary risk?

- **A.** The system may treat stale or superseded content as authoritative because file metadata does not establish content freshness.
- **B.** The file will necessarily exceed the context window.
- **C.** The model will always refuse to read it.
- **D.** The document cannot contain any useful information.

**Answer: A**

**Rationale:** Upload or modification time is not sufficient evidence of policy currency. Content version, effective date, authority, and ownership are needed.

**Why the other options are weaker:**

- **B:** File age does not determine context size.
- **C:** A stale document is not inherently unreadable.
- **D:** It may still be useful as historical or advisory evidence if labeled correctly.

**Objective:** Freshness risk  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 8. A current public standard and a current approved internal standard give different minimum requirements. The internal standard applies to the organization and is stricter. What should the assistant do?

- **A.** Choose the shorter document.
- **B.** Blend the requirements and omit the difference.
- **C.** Select the public standard because it is public.
- **D.** Apply the documented authority and scope rules, cite both where useful, and state that the stricter internal standard governs the organization.

**Answer: D**

**Rationale:** Source resolution depends on authority and scope, not convenience. The conflict and governing rule should remain traceable.

**Why the other options are weaker:**

- **A:** Length has no relationship to authority.
- **B:** Blending hides a material difference.
- **C:** Public availability does not override an approved internal requirement within scope.

**Objective:** Source conflict  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

</details>
