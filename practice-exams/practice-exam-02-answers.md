# Practice Exam 2: Answers and Rationales

Do not review this file until you have completed the exam.

## Answer string

`1B 2B 3B 4B 5C 6B 7C 8A 9D 10C 11A 12B 13A 14B 15C 16A 17A 18B 19A 20C 21D 22D 23C 24D 25C 26D 27D 28A`

## Detailed review

### 1. B | Platform & Model Foundations

**Question ID:** `M1-Q05`  
**Objective:** Model migration  
**Difficulty:** medium

**Why B is best:** A controlled comparison on the same cases isolates the model change and reveals regressions. Staging, monitoring, and rollback make the release operationally safe.

**Why the distractors are weaker:**

- **A:** Anecdotal review is not representative or measurable.
- **C:** Changing several components destroys attribution and complicates rollback.
- **D:** A newer release does not guarantee performance for this use case.

**Official reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 2. B | Prompting & Task Execution

**Question ID:** `M2-Q05`  
**Objective:** Structured output  
**Difficulty:** medium

**Why B is best:** Machine-consumed output requires a precise contract and independent validation. A generic request for JSON does not define semantics.

**Why the distractors are weaker:**

- **A:** Formatting does not constrain field semantics.
- **C:** Fuzzy parsing can silently accept incorrect data.
- **D:** Uncontrolled labels break downstream logic.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 3. B | Evaluating & Validating Output

**Question ID:** `M3-Q05`  
**Objective:** Representative evaluation sets  
**Difficulty:** medium

**Why B is best:** A representative evaluation set must reflect the real distribution and intentionally test edge and adversarial conditions.

**Why the distractors are weaker:**

- **A:** Paraphrases improve volume but not risk coverage.
- **C:** Prompt length is not a substitute for test diversity.
- **D:** Selecting only successful outputs creates severe bias.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 4. B | Workflow Integration & Solutions Design

**Question ID:** `M4-Q05`  
**Objective:** Observability  
**Difficulty:** medium

**Why B is best:** Stage-level telemetry is required to identify the bottleneck and choose the appropriate optimization.

**Why the distractors are weaker:**

- **A:** A longer prompt may increase latency and does not identify the cause.
- **C:** Duplicating responses does not isolate stages.
- **D:** Internal reasoning is neither necessary nor a reliable performance trace.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 5. C | Configuration & Knowledge Management

**Question ID:** `M5-Q05`  
**Objective:** Secret management  
**Difficulty:** easy

**Why C is best:** Credentials belong in a secret-management boundary and should be supplied only to the authorized service call.

**Why the distractors are weaker:**

- **A:** Prompt text may be logged or exposed and is not a secret store.
- **B:** Repository examples are public or broadly accessible.
- **D:** Outputting a credential is disclosure, regardless of warning.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 6. B | Governance, Risk & Responsible Use

**Question ID:** `M6-Q05`  
**Objective:** Change governance  
**Difficulty:** medium

**Why B is best:** A model change is a material system change. It requires evidence, approval, monitoring, and rollback proportional to the use-case risk.

**Why the distractors are weaker:**

- **A:** Release date is not evidence of use-case suitability.
- **C:** Multiple simultaneous changes prevent attribution.
- **D:** Permanent avoidance creates obsolescence and is not risk-based.

**Official reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 7. C | Troubleshooting & Optimization

**Question ID:** `M7-Q05`  
**Objective:** Latency profiling  
**Difficulty:** medium

**Why C is best:** Stage-level measurement identifies whether the bottleneck is retrieval, model generation, tools, validation, or approval. Optimization should preserve required quality and controls.

**Why the distractors are weaker:**

- **A:** Removing validation can create unacceptable risk and may not fix latency.
- **B:** A model change requires evaluation and may not address the bottleneck.
- **D:** More retries can increase latency and cost.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 8. A | Platform & Model Foundations

**Question ID:** `M1-Q06`  
**Objective:** Instruction placement  
**Difficulty:** medium

**Why A is best:** Durable behavior belongs in trusted configuration and must be supported by system controls. Retrieved documents remain evidence and cannot define their own authority.

**Why the distractors are weaker:**

- **B:** User wording is not a reliable place for mandatory application policy.
- **C:** A retrieved document is untrusted content and can contain prompt injection.
- **D:** A downstream field cannot reliably control model behavior or retrieval authority.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 9. D | Prompting & Task Execution

**Question ID:** `M2-Q06`  
**Objective:** Role prompting  
**Difficulty:** easy

**Why D is best:** A role can establish perspective, but it cannot replace the substantive task and evidence contract.

**Why the distractors are weaker:**

- **A:** Roles can help set perspective or vocabulary when used appropriately.
- **B:** A biography is not required and may be irrelevant.
- **C:** Roles can apply to many tasks, not only coding.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### 10. C | Evaluating & Validating Output

**Question ID:** `M3-Q06`  
**Objective:** Severity-based release gates  
**Difficulty:** hard

**Why C is best:** Unauthorized disclosure is a critical failure and must be a hard release gate. Aggregate quality cannot offset it.

**Why the distractors are weaker:**

- **A:** An average hides severity and does not make the disclosure acceptable.
- **B:** Privacy should not be diluted by unrelated low-severity metrics.
- **D:** A warning does not prevent unauthorized access.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 11. A | Workflow Integration & Solutions Design

**Question ID:** `M4-Q06`  
**Objective:** Durable state  
**Difficulty:** medium

**Why A is best:** Long-running workflows need durable external state and validated state transitions. Model context is not a reliable workflow database.

**Why the distractors are weaker:**

- **B:** The model does not independently preserve application state across service restarts.
- **C:** A browser tab is fragile, unauditable, and not a system of record.
- **D:** Repeating completed side effects can create duplicates.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/working-with-messages

### 12. B | Configuration & Knowledge Management

**Question ID:** `M5-Q06`  
**Objective:** Least-privilege retrieval  
**Difficulty:** hard

**Why B is best:** Access control must prevent unauthorized data from reaching the model. Prompt instructions and output filtering are not substitutes for retrieval authorization.

**Why the distractors are weaker:**

- **A:** Instructions do not enforce access control.
- **C:** User promises are not a technical authorization mechanism.
- **D:** Post-generation filtering is too late because the model already received the data.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 13. A | Governance, Risk & Responsible Use

**Question ID:** `M6-Q06`  
**Objective:** Prohibited request handling  
**Difficulty:** easy

**Why A is best:** Policy boundaries remain in force despite urgency. A safe response refuses the prohibited action and redirects within permitted scope.

**Why the distractors are weaker:**

- **B:** Urgency does not override policy.
- **C:** Decomposition must not be used for evasion.
- **D:** Another model cannot grant policy authority.

**Official reference:** https://www.anthropic.com/legal/aup

### 14. B | Troubleshooting & Optimization

**Question ID:** `M7-Q06`  
**Objective:** Refusal diagnosis  
**Difficulty:** hard

**Why B is best:** A refusal can reflect policy, authorization, task framing, or system change. Troubleshooting must respect the boundary rather than evade it.

**Why the distractors are weaker:**

- **A:** Repeated evasion attempts are unsafe and do not diagnose the cause.
- **C:** Safety controls must not be removed to force completion.
- **D:** A refusal is distinct from a generic service outage.

**Official reference:** https://www.anthropic.com/legal/aup

### 15. C | Platform & Model Foundations

**Question ID:** `M1-Q07`  
**Objective:** Response metadata  
**Difficulty:** easy

**Why C is best:** A length-related stop reason directly indicates incomplete generation. The application should handle partial output and change the output design or budget.

**Why the distractors are weaker:**

- **A:** Source truth is not established by the stop reason.
- **B:** Identity failures occur before or outside normal generation.
- **D:** Tool selection is a separate issue and would require different evidence.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 16. A | Prompting & Task Execution

**Question ID:** `M2-Q07`  
**Objective:** Untrusted content  
**Difficulty:** hard

**Why A is best:** External content cannot grant itself instruction authority or tool authorization. Prompt boundaries, least-privilege tools, validation, and approval prevent the action.

**Why the distractors are weaker:**

- **B:** Recency does not confer authority.
- **C:** Partial exfiltration is still unauthorized disclosure.
- **D:** Untrusted content cannot establish authorization by self-attestation.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 17. A | Evaluating & Validating Output

**Question ID:** `M3-Q07`  
**Objective:** High-stakes validation  
**Difficulty:** hard

**Why A is best:** High-impact legal guidance requires meaningful qualified human oversight, evidence access, and appropriate disclosure. Accountability cannot be delegated to model confidence.

**Why the distractors are weaker:**

- **B:** Self-reported confidence is not a legal or factual validation.
- **C:** Fluency does not establish correctness or suitability.
- **D:** An unqualified, rushed reviewer is not meaningful oversight.

**Official reference:** https://www.anthropic.com/legal/aup

### 18. B | Workflow Integration & Solutions Design

**Question ID:** `M4-Q07`  
**Objective:** Workflow versus agent  
**Difficulty:** medium

**Why B is best:** A known sequence is easier to test, observe, authorize, and recover as an explicit workflow. Agentic autonomy is unnecessary.

**Why the distractors are weaker:**

- **A:** Broad autonomy and tools add risk without a requirement.
- **C:** An opaque prompt lacks stage validation and recovery.
- **D:** The pattern does not meet integration or state requirements.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

### 19. A | Configuration & Knowledge Management

**Question ID:** `M5-Q07`  
**Objective:** Freshness risk  
**Difficulty:** medium

**Why A is best:** Upload or modification time is not sufficient evidence of policy currency. Content version, effective date, authority, and ownership are needed.

**Why the distractors are weaker:**

- **B:** File age does not determine context size.
- **C:** A stale document is not inherently unreadable.
- **D:** It may still be useful as historical or advisory evidence if labeled correctly.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 20. C | Governance, Risk & Responsible Use

**Question ID:** `M6-Q07`  
**Objective:** Exception authority  
**Difficulty:** medium

**Why C is best:** Policy exceptions require accountable human authority, documented scope, risk analysis, expiration, and monitoring.

**Why the distractors are weaker:**

- **A:** A model cannot authorize governance exceptions.
- **B:** The requester may have a conflict of interest and lacks delegated authority.
- **D:** A storage tool has no governance authority.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 21. D | Troubleshooting & Optimization

**Question ID:** `M7-Q07`  
**Objective:** Truncation remediation  
**Difficulty:** medium

**Why D is best:** The evidence identifies a generation-length problem. The design should allocate budget or split the work and explicitly handle incomplete output.

**Why the distractors are weaker:**

- **A:** The required report is incomplete.
- **B:** Identical retries preserve the same limit and add cost.
- **C:** Removing structure can make partial output harder to detect and integrate.

**Official reference:** https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons

### 22. D | Platform & Model Foundations

**Question ID:** `M1-Q08`  
**Objective:** Knowledge freshness  
**Difficulty:** medium

**Why D is best:** Current legal or policy claims require current authoritative evidence. The system must distinguish model knowledge from evidence supplied in the interaction.

**Why the distractors are weaker:**

- **A:** Training knowledge should not be assumed current enough for a regulation issued last week.
- **B:** Confidence wording does not create evidence.
- **C:** More output does not improve source freshness.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

### 23. C | Prompting & Task Execution

**Question ID:** `M2-Q08`  
**Objective:** Tool descriptions  
**Difficulty:** medium

**Why C is best:** Wrong-tool errors often result from overlapping purposes. Clear selection boundaries and examples improve tool choice while preserving narrow access.

**Why the distractors are weaker:**

- **A:** A shared generic name increases ambiguity.
- **B:** Broader access violates least privilege and does not clarify selection.
- **D:** Schemas help constrain safe tool parameters.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use

### 24. D | Evaluating & Validating Output

**Question ID:** `M3-Q08`  
**Objective:** Consistency evaluation  
**Difficulty:** medium

**Why D is best:** When stability is a requirement, the evaluation must measure output variance at the level that matters and enforce a threshold.

**Why the distractors are weaker:**

- **A:** A single run cannot reveal instability.
- **B:** Probabilistic behavior does not remove the business requirement.
- **C:** Explanation length is not label consistency.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 25. C | Workflow Integration & Solutions Design

**Question ID:** `M4-Q08`  
**Objective:** Architecture selection  
**Difficulty:** easy

**Why C is best:** Complexity should be justified by requirements. A simple human-led interaction may be more appropriate and easier to govern.

**Why the distractors are weaker:**

- **A:** More model calls can add new failure modes.
- **B:** A workflow engine is not necessary for every task.
- **D:** More components generally increase the audit surface.

**Official reference:** https://platform.claude.com/docs/en/intro

### 26. D | Configuration & Knowledge Management

**Question ID:** `M5-Q08`  
**Objective:** Source conflict  
**Difficulty:** hard

**Why D is best:** Source resolution depends on authority and scope, not convenience. The conflict and governing rule should remain traceable.

**Why the distractors are weaker:**

- **A:** Length has no relationship to authority.
- **B:** Blending hides a material difference.
- **C:** Public availability does not override an approved internal requirement within scope.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 27. D | Governance, Risk & Responsible Use

**Question ID:** `M6-Q08`  
**Objective:** Incident response  
**Difficulty:** hard

**Why D is best:** Potential exfiltration requires containment and evidence preservation before full remediation. Credential rotation and governed incident response reduce ongoing risk.

**Why the distractors are weaker:**

- **A:** Deleting logs destroys evidence and leaves the threat active.
- **B:** The agent is not an authoritative incident investigator.
- **C:** Prompt editing alone does not contain tool or credential exposure.

**Official reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 28. A | Troubleshooting & Optimization

**Question ID:** `M7-Q08`  
**Objective:** Controlled optimization  
**Difficulty:** easy

**Why A is best:** Controlled experimentation enables attribution, regression detection, and safe reversal.

**Why the distractors are weaker:**

- **B:** One attractive output is not representative, and multiple changes obscure causality.
- **C:** Optimization must respect quality, safety, and mission requirements.
- **D:** Unmonitored full deployment creates avoidable risk.

**Official reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

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
