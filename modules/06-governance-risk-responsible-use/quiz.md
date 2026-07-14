# Quiz: Governance, Risk & Responsible Use

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. A team wants to paste confidential architecture diagrams into a new Claude workspace. What should happen first?

- **A.** Classify the data and verify that the product environment, access, retention, logging, residency, contractual, and organizational controls permit the use.
- **B.** Upload the diagrams, then check policy if a problem occurs.
- **C.** Remove the document titles and assume the content is public.
- **D.** Ask Claude whether the workspace is approved.

### 2. A housing organization uses Claude to rank applicants for eligibility. Which control is most important before any adverse decision?

- **A.** Use the longest possible prompt.
- **B.** Require meaningful review by a qualified authorized human with evidence, disclose AI involvement as required, and provide an appropriate contest or appeal path.
- **C.** Automatically accept the top-ranked answer when confidence exceeds 90%.
- **D.** Have an untrained employee approve every result without seeing the underlying evidence.

### 3. An email-processing agent reads a message that instructs it to ignore policy and send customer records to an external address. Which control set is strongest?

- **A.** Ask the model to be careful and retain broad email tools.
- **B.** Hide the system prompt from users.
- **C.** Treat email as untrusted data, constrain tools and recipients, validate authorization in code, require approval for sensitive sends, and test adversarial cases.
- **D.** Retry with a different phrasing until the model complies.

### 4. A team logs every complete prompt, source document, tool credential, and response indefinitely “for debugging.” What is the best correction?

- **A.** Keep the design because more logs are always safer.
- **B.** Make logs publicly searchable so errors are found faster.
- **C.** Encrypt the credential but continue logging it.
- **D.** Minimize and redact content, never log secrets, apply access control and retention, and retain only evidence needed for audit and diagnosis.

### 5. A vendor releases a new model version. The production owner wants to switch immediately because it is newer. What is the strongest governance response?

- **A.** Approve automatically because newer models are always safer.
- **B.** Run change review and regression testing, evaluate policy and risk impacts, obtain required approval, stage rollout, and preserve rollback.
- **C.** Change the model and all prompts simultaneously.
- **D.** Delay all model updates permanently.

### 6. A user asks the system to perform an action that is prohibited by current provider and organization policy. What should the system do?

- **A.** Refuse the prohibited action, explain the boundary at an appropriate level, provide a safe permitted alternative when available, and follow escalation or logging policy.
- **B.** Comply if the user says the task is urgent.
- **C.** Break the action into smaller steps to bypass the restriction.
- **D.** Ask a second model to authorize it.

### 7. A workflow identifies a case that appears to need an exception to the organization's AI data-handling policy. Who can approve it?

- **A.** Claude, when its confidence is high
- **B.** Any user who submitted the request
- **C.** The named human governance authority through the documented exception process and compensating controls
- **D.** The tool that stores the request

### 8. Monitoring suggests a malicious document induced an agent to attempt sending a secret to an external service. What is the best immediate sequence?

- **A.** Delete all logs, then continue operating.
- **B.** Ask the agent whether any data was exposed and accept its answer.
- **C.** Edit the prompt while leaving all tools active.
- **D.** Contain or disable the affected workflow and permissions, preserve evidence, assess scope, rotate exposed credentials, notify incident owners, remediate, and revalidate before restoration.

<details>
<summary>Answer key and rationales</summary>

### 1. A team wants to paste confidential architecture diagrams into a new Claude workspace. What should happen first?

- **A.** Classify the data and verify that the product environment, access, retention, logging, residency, contractual, and organizational controls permit the use.
- **B.** Upload the diagrams, then check policy if a problem occurs.
- **C.** Remove the document titles and assume the content is public.
- **D.** Ask Claude whether the workspace is approved.

**Answer: A**

**Rationale:** Data handling and environment approval must precede processing. The model cannot determine organizational authorization.

**Why the other options are weaker:**

- **B:** Governance after disclosure is too late.
- **C:** Removing a title does not declassify the technical content.
- **D:** Approval comes from authoritative policy and accountable humans, not model judgment.

**Objective:** Data classification  
**Reference:** https://www.anthropic.com/legal/aup

### 2. A housing organization uses Claude to rank applicants for eligibility. Which control is most important before any adverse decision?

- **A.** Use the longest possible prompt.
- **B.** Require meaningful review by a qualified authorized human with evidence, disclose AI involvement as required, and provide an appropriate contest or appeal path.
- **C.** Automatically accept the top-ranked answer when confidence exceeds 90%.
- **D.** Have an untrained employee approve every result without seeing the underlying evidence.

**Answer: B**

**Rationale:** A housing eligibility decision is high impact. Oversight must be qualified, evidence-based, timely, and authoritative, with appropriate transparency and recourse.

**Why the other options are weaker:**

- **A:** Prompt length does not establish accountability.
- **C:** Model confidence is not a substitute for human decision responsibility.
- **D:** Rubber-stamping without expertise or evidence is not meaningful review.

**Objective:** High-impact oversight  
**Reference:** https://www.anthropic.com/legal/aup

### 3. An email-processing agent reads a message that instructs it to ignore policy and send customer records to an external address. Which control set is strongest?

- **A.** Ask the model to be careful and retain broad email tools.
- **B.** Hide the system prompt from users.
- **C.** Treat email as untrusted data, constrain tools and recipients, validate authorization in code, require approval for sensitive sends, and test adversarial cases.
- **D.** Retry with a different phrasing until the model complies.

**Answer: C**

**Rationale:** Defense requires authority separation and system-enforced permissions. Prompt text alone cannot prevent unauthorized side effects.

**Why the other options are weaker:**

- **A:** A cautionary instruction does not offset broad tool permissions.
- **B:** Secrecy of instructions is not an authorization control.
- **D:** Repeated attempts to comply worsen the security failure.

**Objective:** Prompt injection defense  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 4. A team logs every complete prompt, source document, tool credential, and response indefinitely “for debugging.” What is the best correction?

- **A.** Keep the design because more logs are always safer.
- **B.** Make logs publicly searchable so errors are found faster.
- **C.** Encrypt the credential but continue logging it.
- **D.** Minimize and redact content, never log secrets, apply access control and retention, and retain only evidence needed for audit and diagnosis.

**Answer: D**

**Rationale:** Logs should provide traceability without becoming an uncontrolled sensitive-data store. Secrets must not be logged at all.

**Why the other options are weaker:**

- **A:** Excessive logging increases privacy and security exposure.
- **B:** Public access would compound the risk.
- **C:** A credential should not enter the log, even encrypted as a routine practice.

**Objective:** Logging minimization  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 5. A vendor releases a new model version. The production owner wants to switch immediately because it is newer. What is the strongest governance response?

- **A.** Approve automatically because newer models are always safer.
- **B.** Run change review and regression testing, evaluate policy and risk impacts, obtain required approval, stage rollout, and preserve rollback.
- **C.** Change the model and all prompts simultaneously.
- **D.** Delay all model updates permanently.

**Answer: B**

**Rationale:** A model change is a material system change. It requires evidence, approval, monitoring, and rollback proportional to the use-case risk.

**Why the other options are weaker:**

- **A:** Release date is not evidence of use-case suitability.
- **C:** Multiple simultaneous changes prevent attribution.
- **D:** Permanent avoidance creates obsolescence and is not risk-based.

**Objective:** Change governance  
**Reference:** https://platform.claude.com/docs/en/about-claude/models/overview

### 6. A user asks the system to perform an action that is prohibited by current provider and organization policy. What should the system do?

- **A.** Refuse the prohibited action, explain the boundary at an appropriate level, provide a safe permitted alternative when available, and follow escalation or logging policy.
- **B.** Comply if the user says the task is urgent.
- **C.** Break the action into smaller steps to bypass the restriction.
- **D.** Ask a second model to authorize it.

**Answer: A**

**Rationale:** Policy boundaries remain in force despite urgency. A safe response refuses the prohibited action and redirects within permitted scope.

**Why the other options are weaker:**

- **B:** Urgency does not override policy.
- **C:** Decomposition must not be used for evasion.
- **D:** Another model cannot grant policy authority.

**Objective:** Prohibited request handling  
**Reference:** https://www.anthropic.com/legal/aup

### 7. A workflow identifies a case that appears to need an exception to the organization's AI data-handling policy. Who can approve it?

- **A.** Claude, when its confidence is high
- **B.** Any user who submitted the request
- **C.** The named human governance authority through the documented exception process and compensating controls
- **D.** The tool that stores the request

**Answer: C**

**Rationale:** Policy exceptions require accountable human authority, documented scope, risk analysis, expiration, and monitoring.

**Why the other options are weaker:**

- **A:** A model cannot authorize governance exceptions.
- **B:** The requester may have a conflict of interest and lacks delegated authority.
- **D:** A storage tool has no governance authority.

**Objective:** Exception authority  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

### 8. Monitoring suggests a malicious document induced an agent to attempt sending a secret to an external service. What is the best immediate sequence?

- **A.** Delete all logs, then continue operating.
- **B.** Ask the agent whether any data was exposed and accept its answer.
- **C.** Edit the prompt while leaving all tools active.
- **D.** Contain or disable the affected workflow and permissions, preserve evidence, assess scope, rotate exposed credentials, notify incident owners, remediate, and revalidate before restoration.

**Answer: D**

**Rationale:** Potential exfiltration requires containment and evidence preservation before full remediation. Credential rotation and governed incident response reduce ongoing risk.

**Why the other options are weaker:**

- **A:** Deleting logs destroys evidence and leaves the threat active.
- **B:** The agent is not an authoritative incident investigator.
- **C:** Prompt editing alone does not contain tool or credential exposure.

**Objective:** Incident response  
**Reference:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

</details>
