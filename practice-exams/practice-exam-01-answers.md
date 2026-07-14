# Practice Exam 1: Answers and Rationales

Do not review this file until you have completed the exam.

## Answer string

`1A 2A 3B 4A 5B 6A 7A 8B 9D 10A 11C 12C 13B 14B 15C 16B 17C 18B 19A 20C 21C 22D 23C 24D 25D 26D 27D 28A`

## Detailed review

### 1. A | Platform & Model Foundations

**Question ID:** `M1-Q01`  
**Objective:** Product surface selection  
**Difficulty:** easy

**Why A is best:** An approved interactive experience matches an occasional, exploratory, human-led task with no integration requirement. Environment and data controls still must be verified.

**Why the distractors are weaker:**

- **B:** This adds unnecessary autonomy and overly broad write access.
- **C:** An API service may become useful later, but it adds engineering before the task is validated.
- **D:** Publishing internal evidence creates an unacceptable data-handling risk.

**Official reference:** https://platform.claude.com/docs/en/intro

### 2. A | Prompting & Task Execution

**Question ID:** `M2-Q01`  
**Objective:** Task definition  
**Difficulty:** easy

**Why A is best:** Prompt improvement begins with a clear definition of success and an empirical way to test it. The task contract makes later changes measurable.

**Why the distractors are weaker:**

- **B:** Accuracy must be defined through evidence and tests, not an adjective.
- **C:** Longer output does not establish correctness or usefulness.
- **D:** A role alone does not provide evidence, constraints, or completion criteria.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

### 3. B | Evaluating & Validating Output

**Question ID:** `M3-Q01`  
**Objective:** Evaluation-first development  
**Difficulty:** easy

**Why B is best:** The team must define what acceptable performance means and how it will be measured before prompt changes can be evaluated.

**Why the distractors are weaker:**

- **A:** Wording changes without criteria cannot be assessed objectively.
- **C:** Output length may be unrelated to the actual failure.
- **D:** Changing expectations without understanding the use case is not evaluation.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 4. A | Workflow Integration & Solutions Design

**Question ID:** `M4-Q01`  
**Objective:** Responsibility partitioning  
**Difficulty:** easy

**Why A is best:** Exact arithmetic and authorization belong in deterministic components. Claude can explain the validated results without controlling the financial action.

**Why the distractors are weaker:**

- **B:** This combines probabilistic calculation with a consequential side effect.
- **C:** Manual retyping adds error and does not improve the architecture.
- **D:** Retrieval is unrelated to exact arithmetic.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 5. B | Configuration & Knowledge Management

**Question ID:** `M5-Q01`  
**Objective:** Source governance  
**Difficulty:** easy

**Why B is best:** A governed source needs accountability, authority, freshness, scope, and data-handling metadata before it can reliably support answers.

**Why the distractors are weaker:**

- **A:** Formatting does not establish governance or freshness.
- **C:** Popularity is not authority.
- **D:** A keyword does not prove the document governs the use case.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 6. A | Governance, Risk & Responsible Use

**Question ID:** `M6-Q01`  
**Objective:** Data classification  
**Difficulty:** easy

**Why A is best:** Data handling and environment approval must precede processing. The model cannot determine organizational authorization.

**Why the distractors are weaker:**

- **B:** Governance after disclosure is too late.
- **C:** Removing a title does not declassify the technical content.
- **D:** Approval comes from authoritative policy and accountable humans, not model judgment.

**Official reference:** https://www.anthropic.com/legal/aup

### 7. A | Troubleshooting & Optimization

**Question ID:** `M7-Q01`  
**Objective:** Baseline comparison  
**Difficulty:** easy

**Why A is best:** A known-good baseline and controlled variable isolation are required to attribute the regression.

**Why the distractors are weaker:**

- **B:** Additional uncontrolled change makes attribution harder.
- **C:** A single pass can hide intermittent or systematic failure.
- **D:** Any of the changed components could be responsible.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 8. B | Platform & Model Foundations

**Question ID:** `M1-Q02`  
**Objective:** Application-managed state  
**Difficulty:** medium

**Why B is best:** The application is responsible for managing the relevant conversational state and supplying it with the request. State retention must also follow privacy and context-management rules.

**Why the distractors are weaker:**

- **A:** Sampling settings do not restore missing conversation context.
- **C:** A request cannot reference information that was not supplied through the product or application state.
- **D:** Tool use is unrelated to whether the application includes prior turns.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/working-with-messages

### 9. D | Prompting & Task Execution

**Question ID:** `M2-Q02`  
**Objective:** Few-shot examples  
**Difficulty:** medium

**Why D is best:** Examples efficiently clarify ambiguous category boundaries and show how indirect evidence maps to the allowed labels.

**Why the distractors are weaker:**

- **A:** Repetition adds tokens without resolving the boundary.
- **B:** Creativity is contrary to stable classification.
- **C:** Removing labels increases ambiguity.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 10. A | Evaluating & Validating Output

**Question ID:** `M3-Q02`  
**Objective:** Code-based grading  
**Difficulty:** easy

**Why A is best:** Allowed values and identifier validity are exact, machine-checkable properties. Deterministic validation is consistent and auditable.

**Why the distractors are weaker:**

- **B:** Human review is unnecessarily expensive and less consistent for exact checks.
- **C:** A model grader adds variability to a deterministic property.
- **D:** Self-reported confidence does not validate the actual fields.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 11. C | Workflow Integration & Solutions Design

**Question ID:** `M4-Q02`  
**Objective:** Human approval placement  
**Difficulty:** medium

**Why C is best:** Meaningful approval must occur before the consequential side effect and should present the evidence, uncertainty, and proposed action to an authorized reviewer.

**Why the distractors are weaker:**

- **A:** Post-execution review cannot prevent harm.
- **B:** Public feedback is not a substitute for prepublication authorization.
- **D:** A model instruction does not create human accountability.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 12. C | Configuration & Knowledge Management

**Question ID:** `M5-Q02`  
**Objective:** Reusable configuration  
**Difficulty:** medium

**Why C is best:** Durable application behavior should be governed, versioned, reviewed, and tested rather than repeated informally by each user.

**Why the distractors are weaker:**

- **A:** User memory is not enforceable or auditable.
- **B:** Sources are evidence, not trusted behavioral configuration.
- **D:** An unsaved note cannot establish repeatable system behavior.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 13. B | Governance, Risk & Responsible Use

**Question ID:** `M6-Q02`  
**Objective:** High-impact oversight  
**Difficulty:** hard

**Why B is best:** A housing eligibility decision is high impact. Oversight must be qualified, evidence-based, timely, and authoritative, with appropriate transparency and recourse.

**Why the distractors are weaker:**

- **A:** Prompt length does not establish accountability.
- **C:** Model confidence is not a substitute for human decision responsibility.
- **D:** Rubber-stamping without expertise or evidence is not meaningful review.

**Official reference:** https://www.anthropic.com/legal/aup

### 14. B | Troubleshooting & Optimization

**Question ID:** `M7-Q02`  
**Objective:** Wrong tool diagnosis  
**Difficulty:** medium

**Why B is best:** Ambiguous tool descriptions and selection boundaries are a common cause of wrong-tool behavior. Narrow exposure also reduces confusion and privilege.

**Why the distractors are weaker:**

- **A:** Output length does not control tool selection.
- **C:** Broadening access creates security risk.
- **D:** Descriptions are necessary for informed selection.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use

### 15. C | Platform & Model Foundations

**Question ID:** `M1-Q03`  
**Objective:** Model selection  
**Difficulty:** medium

**Why C is best:** Once hard requirements are met, model selection should optimize the full operational profile, including latency, throughput, cost, governance, and reliability.

**Why the distractors are weaker:**

- **A:** The task uses short documents, so maximum context may not be decision-relevant.
- **B:** Recency does not prove fit for the validated use case.
- **D:** Long explanations may increase cost and are not the required output.

**Official reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 16. B | Prompting & Task Execution

**Question ID:** `M2-Q03`  
**Objective:** Prompt structure  
**Difficulty:** easy

**Why B is best:** Clear structure helps distinguish instruction from data. It should be combined with system-enforced permissions and validation.

**Why the distractors are weaker:**

- **A:** Adjectives do not create authority boundaries.
- **C:** Combining all content increases ambiguity.
- **D:** Removing the boundary weakens the design.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 17. C | Evaluating & Validating Output

**Question ID:** `M3-Q03`  
**Objective:** Mixed-method grading  
**Difficulty:** medium

**Why C is best:** Different properties require different graders. Exact requirements can be automated, while nuanced tone needs a calibrated semantic judgment process.

**Why the distractors are weaker:**

- **A:** Exact matching cannot reliably score nuanced communication.
- **B:** One uncalibrated impression is subjective and difficult to reproduce.
- **D:** Length does not measure policy fidelity or empathy.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 18. B | Workflow Integration & Solutions Design

**Question ID:** `M4-Q03`  
**Objective:** Idempotency  
**Difficulty:** medium

**Why B is best:** A status check tied to a stable idempotency key prevents duplicate side effects when the result of the first request is uncertain.

**Why the distractors are weaker:**

- **A:** A new identifier can create a duplicate payment.
- **C:** The model cannot determine an external transaction state without authoritative evidence.
- **D:** Ignoring the result leaves the workflow inconsistent.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

### 19. A | Configuration & Knowledge Management

**Question ID:** `M5-Q03`  
**Objective:** Prompt caching  
**Difficulty:** medium

**Why A is best:** Prompt caching is designed for stable, repeatedly reused prefixes. The design must follow current platform semantics and data policy and should be verified with usage diagnostics.

**Why the distractors are weaker:**

- **B:** A changing early field can invalidate the reusable prefix.
- **C:** Credentials must never be stored in prompt text or cache.
- **D:** Changing order prevents prefix reuse.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching

### 20. C | Governance, Risk & Responsible Use

**Question ID:** `M6-Q03`  
**Objective:** Prompt injection defense  
**Difficulty:** hard

**Why C is best:** Defense requires authority separation and system-enforced permissions. Prompt text alone cannot prevent unauthorized side effects.

**Why the distractors are weaker:**

- **A:** A cautionary instruction does not offset broad tool permissions.
- **B:** Secrecy of instructions is not an authorization control.
- **D:** Repeated attempts to comply worsen the security failure.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 21. C | Troubleshooting & Optimization

**Question ID:** `M7-Q03`  
**Objective:** Tool parameter validation  
**Difficulty:** medium

**Why C is best:** The tool boundary must reject fields outside the contract and prevent model-invented identifiers from causing action.

**Why the distractors are weaker:**

- **A:** Silent coercion hides errors and can create unauthorized behavior.
- **B:** Spelling does not establish authority or provenance.
- **D:** Testing an invented address can itself create an unauthorized side effect.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use

### 22. D | Platform & Model Foundations

**Question ID:** `M1-Q04`  
**Objective:** Context and output limits  
**Difficulty:** medium

**Why D is best:** A request can fit within context yet still end because generation reached an output limit or another stop condition. The response metadata is critical evidence.

**Why the distractors are weaker:**

- **A:** Prompt roles may affect behavior but do not explain the abrupt ending by themselves.
- **B:** Caching can affect performance and cost, not usually the logical completion boundary.
- **C:** Training methodology is not the immediate operational diagnostic.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 23. C | Prompting & Task Execution

**Question ID:** `M2-Q04`  
**Objective:** Prompt decomposition  
**Difficulty:** medium

**Why C is best:** Stages with different evidence, validation, and side effects should be separated. This improves inspectability, recovery, and control.

**Why the distractors are weaker:**

- **A:** Length does not create stage-level visibility.
- **B:** Skipping validation weakens the core requirement.
- **D:** Retries do not correct systematic design ambiguity and may duplicate actions.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 24. D | Evaluating & Validating Output

**Question ID:** `M3-Q04`  
**Objective:** Grounding controls  
**Difficulty:** medium

**Why D is best:** The system should make unsupported specificity unnecessary and detectable by grounding every claim and permitting abstention.

**Why the distractors are weaker:**

- **A:** Requesting more detail can increase fabrication when evidence is absent.
- **B:** Creativity is contrary to evidence-bound reporting.
- **C:** Removing citations reduces traceability.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

### 25. D | Workflow Integration & Solutions Design

**Question ID:** `M4-Q04`  
**Objective:** Tool contracts  
**Difficulty:** medium

**Why D is best:** A purpose-specific, narrow, typed, and non-ambiguous contract supports correct selection and least privilege.

**Why the distractors are weaker:**

- **A:** The purpose and selection boundary are undefined.
- **B:** An unconstrained object and broad use guidance are unsafe.
- **C:** Full administrative access violates least privilege.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

### 26. D | Configuration & Knowledge Management

**Question ID:** `M5-Q04`  
**Objective:** Context selection  
**Difficulty:** medium

**Why D is best:** Retrieval should select high-quality evidence, not maximize volume. Authority, freshness, relevance, and access belong in the retrieval pipeline.

**Why the distractors are weaker:**

- **A:** More generated text does not resolve noisy or conflicting evidence.
- **B:** Conflict must be resolved by documented authority or surfaced.
- **C:** Removing authorization creates a data exposure risk.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 27. D | Governance, Risk & Responsible Use

**Question ID:** `M6-Q04`  
**Objective:** Logging minimization  
**Difficulty:** medium

**Why D is best:** Logs should provide traceability without becoming an uncontrolled sensitive-data store. Secrets must not be logged at all.

**Why the distractors are weaker:**

- **A:** Excessive logging increases privacy and security exposure.
- **B:** Public access would compound the risk.
- **C:** A credential should not enter the log, even encrypted as a routine practice.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 28. A | Troubleshooting & Optimization

**Question ID:** `M7-Q04`  
**Objective:** Cache diagnostics  
**Difficulty:** medium

**Why A is best:** Cache reuse depends on the applicable stable prefix and platform semantics. Seemingly small early changes or reordered tools can invalidate reuse.

**Why the distractors are weaker:**

- **B:** Generated answer wording does not determine the input prefix match.
- **C:** Tone review is unrelated to cache identity.
- **D:** Pretrained knowledge is not the direct cache key.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching

## Score review

| Domain | Correct | Total | Notes |
|---|---:|---:|---|
| 1. Platform & Model Foundations | | 4 | |
| 2. Prompting & Task Execution | | 4 | |
| 3. Evaluating & Validating Output | | 4 | |
| 4. Workflow Integration & Solutions Design | | 4 | |
| 5. Configuration & Knowledge Management | | 4 | |
| 6. Governance, Risk & Responsible Use | | 4 | |
| 7. Troubleshooting & Optimization | | 4 | |
