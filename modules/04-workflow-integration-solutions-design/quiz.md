# Quiz: Workflow Integration & Solutions Design

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. A workflow calculates exact payment totals and then drafts a plain-language explanation. Which division of responsibility is best?

- **A.** Use deterministic code for the calculations and Claude for the explanation based on validated results.
- **B.** Ask Claude to calculate and authorize the payment in one step.
- **C.** Let a human retype every number after generation.
- **D.** Use retrieval to estimate the payment.

### 2. A system drafts a public incident statement from verified evidence. Where should the communications lead's approval occur?

- **A.** After the statement has been posted
- **B.** Only after public feedback arrives
- **C.** After evidence and policy validation but before any publishing tool can execute
- **D.** Inside a hidden model instruction with no reviewer interface

### 3. A payment tool times out after submission. The client does not know whether the payment completed. What is the safest next action?

- **A.** Immediately submit the same payment again with a new identifier.
- **B.** Use the original idempotency key or transaction identifier to check status before any retry.
- **C.** Ask Claude whether it thinks the payment succeeded.
- **D.** Ignore the timeout and mark the workflow complete.

### 4. Which tool definition is most reliable for model-guided use?

- **A.** `manage_data`: Does data things.
- **B.** `run_action`: Use whenever needed; accepts any object.
- **C.** `admin`: Full system access for convenience.
- **D.** `create_draft_exception_request`: Creates a non-approved draft only, lists when it applies, requires typed fields and authorization, defines errors, and has no execution capability.

### 5. End-to-end latency increased, but the team logs only the total request duration. What is the key missing capability?

- **A.** A longer system prompt
- **B.** Stage-level timing and outcome data for retrieval, model generation, tools, validation, and human review
- **C.** A second copy of every response
- **D.** A model-generated explanation of its internal reasoning

### 6. A workflow pauses for two days while awaiting approval, then resumes after a service restart. Which design is required?

- **A.** Persist validated workflow state, completed steps, versions, and pending approval outside the prompt.
- **B.** Assume the model will remember the workflow after restart.
- **C.** Keep the only state in a developer's browser tab.
- **D.** Restart the entire workflow and repeat all side effects.

### 7. A process always follows the same five steps with fixed validation and one approval gate. Which architecture is usually safest?

- **A.** An unconstrained autonomous agent with every enterprise tool
- **B.** An explicit workflow with bounded model calls and deterministic transitions
- **C.** A single prompt that silently performs all steps
- **D.** A public chatbot with no state store

### 8. A team proposes a multi-agent system for a one-time, human-reviewed summary of two documents. What is the best design principle?

- **A.** More agents always improve factual accuracy.
- **B.** Every document task requires a workflow engine.
- **C.** Choose the simplest architecture that meets the quality, integration, control, and risk requirements.
- **D.** Use the architecture with the most components because it is easier to audit.

<details>
<summary>Answer key and rationales</summary>

### 1. A workflow calculates exact payment totals and then drafts a plain-language explanation. Which division of responsibility is best?

- **A.** Use deterministic code for the calculations and Claude for the explanation based on validated results.
- **B.** Ask Claude to calculate and authorize the payment in one step.
- **C.** Let a human retype every number after generation.
- **D.** Use retrieval to estimate the payment.

**Answer: A**

**Rationale:** Exact arithmetic and authorization belong in deterministic components. Claude can explain the validated results without controlling the financial action.

**Why the other options are weaker:**

- **B:** This combines probabilistic calculation with a consequential side effect.
- **C:** Manual retyping adds error and does not improve the architecture.
- **D:** Retrieval is unrelated to exact arithmetic.

**Objective:** Responsibility partitioning  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 2. A system drafts a public incident statement from verified evidence. Where should the communications lead's approval occur?

- **A.** After the statement has been posted
- **B.** Only after public feedback arrives
- **C.** After evidence and policy validation but before any publishing tool can execute
- **D.** Inside a hidden model instruction with no reviewer interface

**Answer: C**

**Rationale:** Meaningful approval must occur before the consequential side effect and should present the evidence, uncertainty, and proposed action to an authorized reviewer.

**Why the other options are weaker:**

- **A:** Post-execution review cannot prevent harm.
- **B:** Public feedback is not a substitute for prepublication authorization.
- **D:** A model instruction does not create human accountability.

**Objective:** Human approval placement  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 3. A payment tool times out after submission. The client does not know whether the payment completed. What is the safest next action?

- **A.** Immediately submit the same payment again with a new identifier.
- **B.** Use the original idempotency key or transaction identifier to check status before any retry.
- **C.** Ask Claude whether it thinks the payment succeeded.
- **D.** Ignore the timeout and mark the workflow complete.

**Answer: B**

**Rationale:** A status check tied to a stable idempotency key prevents duplicate side effects when the result of the first request is uncertain.

**Why the other options are weaker:**

- **A:** A new identifier can create a duplicate payment.
- **C:** The model cannot determine an external transaction state without authoritative evidence.
- **D:** Ignoring the result leaves the workflow inconsistent.

**Objective:** Idempotency  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

### 4. Which tool definition is most reliable for model-guided use?

- **A.** `manage_data`: Does data things.
- **B.** `run_action`: Use whenever needed; accepts any object.
- **C.** `admin`: Full system access for convenience.
- **D.** `create_draft_exception_request`: Creates a non-approved draft only, lists when it applies, requires typed fields and authorization, defines errors, and has no execution capability.

**Answer: D**

**Rationale:** A purpose-specific, narrow, typed, and non-ambiguous contract supports correct selection and least privilege.

**Why the other options are weaker:**

- **A:** The purpose and selection boundary are undefined.
- **B:** An unconstrained object and broad use guidance are unsafe.
- **C:** Full administrative access violates least privilege.

**Objective:** Tool contracts  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

### 5. End-to-end latency increased, but the team logs only the total request duration. What is the key missing capability?

- **A.** A longer system prompt
- **B.** Stage-level timing and outcome data for retrieval, model generation, tools, validation, and human review
- **C.** A second copy of every response
- **D.** A model-generated explanation of its internal reasoning

**Answer: B**

**Rationale:** Stage-level telemetry is required to identify the bottleneck and choose the appropriate optimization.

**Why the other options are weaker:**

- **A:** A longer prompt may increase latency and does not identify the cause.
- **C:** Duplicating responses does not isolate stages.
- **D:** Internal reasoning is neither necessary nor a reliable performance trace.

**Objective:** Observability  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 6. A workflow pauses for two days while awaiting approval, then resumes after a service restart. Which design is required?

- **A.** Persist validated workflow state, completed steps, versions, and pending approval outside the prompt.
- **B.** Assume the model will remember the workflow after restart.
- **C.** Keep the only state in a developer's browser tab.
- **D.** Restart the entire workflow and repeat all side effects.

**Answer: A**

**Rationale:** Long-running workflows need durable external state and validated state transitions. Model context is not a reliable workflow database.

**Why the other options are weaker:**

- **B:** The model does not independently preserve application state across service restarts.
- **C:** A browser tab is fragile, unauditable, and not a system of record.
- **D:** Repeating completed side effects can create duplicates.

**Objective:** Durable state  
**Reference:** https://platform.claude.com/docs/en/build-with-claude/working-with-messages

### 7. A process always follows the same five steps with fixed validation and one approval gate. Which architecture is usually safest?

- **A.** An unconstrained autonomous agent with every enterprise tool
- **B.** An explicit workflow with bounded model calls and deterministic transitions
- **C.** A single prompt that silently performs all steps
- **D.** A public chatbot with no state store

**Answer: B**

**Rationale:** A known sequence is easier to test, observe, authorize, and recover as an explicit workflow. Agentic autonomy is unnecessary.

**Why the other options are weaker:**

- **A:** Broad autonomy and tools add risk without a requirement.
- **C:** An opaque prompt lacks stage validation and recovery.
- **D:** The pattern does not meet integration or state requirements.

**Objective:** Workflow versus agent  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 8. A team proposes a multi-agent system for a one-time, human-reviewed summary of two documents. What is the best design principle?

- **A.** More agents always improve factual accuracy.
- **B.** Every document task requires a workflow engine.
- **C.** Choose the simplest architecture that meets the quality, integration, control, and risk requirements.
- **D.** Use the architecture with the most components because it is easier to audit.

**Answer: C**

**Rationale:** Complexity should be justified by requirements. A simple human-led interaction may be more appropriate and easier to govern.

**Why the other options are weaker:**

- **A:** More model calls can add new failure modes.
- **B:** A workflow engine is not necessary for every task.
- **D:** More components generally increase the audit surface.

**Objective:** Architecture selection  
**Reference:** https://platform.claude.com/docs/en/intro

</details>
