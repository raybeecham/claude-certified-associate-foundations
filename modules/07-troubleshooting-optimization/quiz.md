# Quiz: Troubleshooting & Optimization

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. A report generator became less accurate after a release that changed the model, prompt, tools, retrieval query, and schema. What is the best first technical step?

- **A.** Reconstruct the known-good baseline and compare one changed component at a time on the same evaluation set.
- **B.** Keep all changes and add more instructions.
- **C.** Retry each failed case until it passes once.
- **D.** Assume the model is the only possible cause.

### 2. Claude chooses the public search tool instead of the internal standards tool. Both tools have similar names and descriptions. Which fix is most directly supported by the symptom?

- **A.** Increase the maximum output length.
- **B.** Differentiate the tool purposes and when-to-use rules, strengthen schemas and examples, and expose only eligible tools.
- **C.** Allow the public tool to access internal data.
- **D.** Remove all tool descriptions.

### 3. A tool call contains an invented field named `system_owner_email`, which is neither required nor authorized. What is the strongest fix?

- **A.** Silently accept the field when it looks plausible.
- **B.** Ask Claude to spell the email more carefully.
- **C.** Use a strict schema that forbids extra fields, validate all parameters in the application, and require authoritative lookup for any identifier.
- **D.** Send the email to test whether it exists.

### 4. Prompt-cache hit rates collapse after a release even though the long reference text did not change. Which item should the team inspect first?

- **A.** Whether any content, ordering, tool definitions, or cache breakpoint in the reusable prefix changed
- **B.** Whether the final user answer used more adjectives
- **C.** Whether reviewers liked the output tone
- **D.** Whether the model's pretrained knowledge changed

### 5. P95 end-to-end latency rose by 50%. The workflow includes retrieval, two model calls, a database tool, validation, and human approval. What should the team do first?

- **A.** Remove validation immediately.
- **B.** Switch to the smallest model without testing quality.
- **C.** Measure latency and queueing for every stage, then optimize the actual bottleneck against quality and risk thresholds.
- **D.** Increase the retry count.

### 6. A previously allowed analytical task now receives a refusal. What is the strongest troubleshooting approach?

- **A.** Keep rephrasing until a guardrail is bypassed.
- **B.** Inspect the exact task, current policy and permissions, refusal or stop metadata, and recent changes, then redesign only the permitted portion or escalate.
- **C.** Disable all safety controls.
- **D.** Assume every refusal is a service outage.

### 7. A report repeatedly ends at the same point, and the stop reason indicates the maximum generation length. What is the best remediation?

- **A.** Assume the missing content was not important.
- **B.** Retry indefinitely with the same budget.
- **C.** Remove the output schema.
- **D.** Increase the output budget when appropriate, reduce irrelevant context or requested verbosity, decompose or paginate the task, and validate partial output.

### 8. Which change process produces the most trustworthy optimization result?

- **A.** Record a baseline, change one material variable, rerun representative tests and operational metrics, document the result, and preserve rollback.
- **B.** Change every component and judge one attractive output.
- **C.** Optimize only for cost and ignore quality.
- **D.** Deploy directly to all users without monitoring.

<details>
<summary>Answer key and rationales</summary>

### 1. A report generator became less accurate after a release that changed the model, prompt, tools, retrieval query, and schema. What is the best first technical step?

- **A.** Reconstruct the known-good baseline and compare one changed component at a time on the same evaluation set.
- **B.** Keep all changes and add more instructions.
- **C.** Retry each failed case until it passes once.
- **D.** Assume the model is the only possible cause.

**Answer: A**

**Rationale:** A known-good baseline and controlled variable isolation are required to attribute the regression.

**Why the other options are weaker:**

- **B:** Additional uncontrolled change makes attribution harder.
- **C:** A single pass can hide intermittent or systematic failure.
- **D:** Any of the changed components could be responsible.

**Objective:** Baseline comparison  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 2. Claude chooses the public search tool instead of the internal standards tool. Both tools have similar names and descriptions. Which fix is most directly supported by the symptom?

- **A.** Increase the maximum output length.
- **B.** Differentiate the tool purposes and when-to-use rules, strengthen schemas and examples, and expose only eligible tools.
- **C.** Allow the public tool to access internal data.
- **D.** Remove all tool descriptions.

**Answer: B**

**Rationale:** Ambiguous tool descriptions and selection boundaries are a common cause of wrong-tool behavior. Narrow exposure also reduces confusion and privilege.

**Why the other options are weaker:**

- **A:** Output length does not control tool selection.
- **C:** Broadening access creates security risk.
- **D:** Descriptions are necessary for informed selection.

**Objective:** Wrong tool diagnosis  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use

### 3. A tool call contains an invented field named `system_owner_email`, which is neither required nor authorized. What is the strongest fix?

- **A.** Silently accept the field when it looks plausible.
- **B.** Ask Claude to spell the email more carefully.
- **C.** Use a strict schema that forbids extra fields, validate all parameters in the application, and require authoritative lookup for any identifier.
- **D.** Send the email to test whether it exists.

**Answer: C**

**Rationale:** The tool boundary must reject fields outside the contract and prevent model-invented identifiers from causing action.

**Why the other options are weaker:**

- **A:** Silent coercion hides errors and can create unauthorized behavior.
- **B:** Spelling does not establish authority or provenance.
- **D:** Testing an invented address can itself create an unauthorized side effect.

**Objective:** Tool parameter validation  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use

### 4. Prompt-cache hit rates collapse after a release even though the long reference text did not change. Which item should the team inspect first?

- **A.** Whether any content, ordering, tool definitions, or cache breakpoint in the reusable prefix changed
- **B.** Whether the final user answer used more adjectives
- **C.** Whether reviewers liked the output tone
- **D.** Whether the model's pretrained knowledge changed

**Answer: A**

**Rationale:** Cache reuse depends on the applicable stable prefix and platform semantics. Seemingly small early changes or reordered tools can invalidate reuse.

**Why the other options are weaker:**

- **B:** Generated answer wording does not determine the input prefix match.
- **C:** Tone review is unrelated to cache identity.
- **D:** Pretrained knowledge is not the direct cache key.

**Objective:** Cache diagnostics  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching

### 5. P95 end-to-end latency rose by 50%. The workflow includes retrieval, two model calls, a database tool, validation, and human approval. What should the team do first?

- **A.** Remove validation immediately.
- **B.** Switch to the smallest model without testing quality.
- **C.** Measure latency and queueing for every stage, then optimize the actual bottleneck against quality and risk thresholds.
- **D.** Increase the retry count.

**Answer: C**

**Rationale:** Stage-level measurement identifies whether the bottleneck is retrieval, model generation, tools, validation, or approval. Optimization should preserve required quality and controls.

**Why the other options are weaker:**

- **A:** Removing validation can create unacceptable risk and may not fix latency.
- **B:** A model change requires evaluation and may not address the bottleneck.
- **D:** More retries can increase latency and cost.

**Objective:** Latency profiling  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 6. A previously allowed analytical task now receives a refusal. What is the strongest troubleshooting approach?

- **A.** Keep rephrasing until a guardrail is bypassed.
- **B.** Inspect the exact task, current policy and permissions, refusal or stop metadata, and recent changes, then redesign only the permitted portion or escalate.
- **C.** Disable all safety controls.
- **D.** Assume every refusal is a service outage.

**Answer: B**

**Rationale:** A refusal can reflect policy, authorization, task framing, or system change. Troubleshooting must respect the boundary rather than evade it.

**Why the other options are weaker:**

- **A:** Repeated evasion attempts are unsafe and do not diagnose the cause.
- **C:** Safety controls must not be removed to force completion.
- **D:** A refusal is distinct from a generic service outage.

**Objective:** Refusal diagnosis  
**Reference:** https://www.anthropic.com/legal/aup

### 7. A report repeatedly ends at the same point, and the stop reason indicates the maximum generation length. What is the best remediation?

- **A.** Assume the missing content was not important.
- **B.** Retry indefinitely with the same budget.
- **C.** Remove the output schema.
- **D.** Increase the output budget when appropriate, reduce irrelevant context or requested verbosity, decompose or paginate the task, and validate partial output.

**Answer: D**

**Rationale:** The evidence identifies a generation-length problem. The design should allocate budget or split the work and explicitly handle incomplete output.

**Why the other options are weaker:**

- **A:** The required report is incomplete.
- **B:** Identical retries preserve the same limit and add cost.
- **C:** Removing structure can make partial output harder to detect and integrate.

**Objective:** Truncation remediation  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 8. Which change process produces the most trustworthy optimization result?

- **A.** Record a baseline, change one material variable, rerun representative tests and operational metrics, document the result, and preserve rollback.
- **B.** Change every component and judge one attractive output.
- **C.** Optimize only for cost and ignore quality.
- **D.** Deploy directly to all users without monitoring.

**Answer: A**

**Rationale:** Controlled experimentation enables attribution, regression detection, and safe reversal.

**Why the other options are weaker:**

- **B:** One attractive output is not representative, and multiple changes obscure causality.
- **C:** Optimization must respect quality, safety, and mission requirements.
- **D:** Unmonitored full deployment creates avoidable risk.

**Objective:** Controlled optimization  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

</details>
