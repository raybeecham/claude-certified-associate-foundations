# Notes: Governance, Risk & Responsible Use

## 1. Governance begins with the use case

Document:

- intended purpose;
- users and affected parties;
- data categories;
- decision impact;
- model and tool capabilities;
- action authority;
- applicable policies and laws;
- human roles;
- monitoring;
- incident ownership; and
- prohibited uses.

A general-purpose model does not make every downstream use acceptable.

## 2. Classify data before processing

Identify whether the task contains:

- public information;
- internal business data;
- confidential information;
- personal data;
- sensitive personal data;
- regulated records;
- credentials;
- controlled technical data;
- classified or national-security information; or
- other organization-defined categories.

Then verify:

- approved environment and provider;
- contractual terms;
- access controls;
- data residency;
- retention and deletion;
- logging;
- training or data-use settings;
- encryption;
- incident obligations; and
- authorized users.

Do not paste data into a product and investigate controls afterward.

## 3. High-impact uses

High-impact domains can affect rights, opportunities, health, finances, legal position, education, employment, housing, insurance, or access to essential services.

Controls may include:

- qualified human review;
- disclosure that AI is involved;
- evidence and citation access;
- ability to contest or appeal;
- bias and performance evaluation;
- monitoring by subgroup and case type;
- restrictions on automated decisions;
- documented accountability; and
- legal or policy approval.

The human must have meaningful authority. Rubber-stamping is not oversight.

## 4. Human accountability

A strong review design answers:

- Who reviews?
- What qualifications are required?
- Which evidence is visible?
- What uncertainty and conflicts are shown?
- What decision can the reviewer make?
- Can the reviewer reject or modify?
- When must the reviewer escalate?
- How is the decision recorded?
- What time pressure or automation bias could impair review?

Keep consequential authority with the accountable organization and person.

## 5. Prompt injection threat model

### Assets

- confidential data;
- credentials;
- tool permissions;
- source integrity;
- system instructions;
- user identity;
- workflow state; and
- external side effects.

### Attack paths

- malicious uploaded document;
- web page instruction;
- poisoned knowledge source;
- email or ticket content;
- tool output containing commands;
- compromised third-party skill or connector;
- encoded or obfuscated instruction; and
- multi-turn social engineering.

### Controls

- treat external content as untrusted;
- separate instruction authority from evidence;
- retrieve from approved sources;
- constrain tools and schemas;
- validate parameters;
- sandbox execution;
- require approval before sensitive actions;
- minimize accessible data;
- monitor anomalous behavior;
- test adversarial cases; and
- preserve a safe failure path.

Prompt text alone cannot enforce authorization.

## 6. Third-party integrations and skills

Review before use:

- publisher and provenance;
- source code where available;
- requested permissions;
- network destinations;
- file-system scope;
- tool calls;
- executable code;
- credential handling;
- update mechanism;
- data retention;
- dependency chain; and
- incident support.

Risk indicators include hardcoded credentials, broad file access, hidden network calls, instructions to bypass controls, or ambiguous tool behavior.

Use allowlists and formal approval for enterprise deployment.

## 7. Logging and privacy

Logs are useful for audit and troubleshooting but can become a secondary sensitive-data store.

Apply:

- collection minimization;
- field redaction;
- tokenization or pseudonymization;
- role-based access;
- encryption;
- retention limits;
- separate security audit trails;
- tamper evidence;
- access monitoring; and
- secure deletion.

Log identifiers and validation outcomes when full content is unnecessary.

## 8. Policy and refusal

Current provider policy, product terms, law, and organization policy all apply.

When a request is prohibited or unsafe:

1. do not perform the disallowed action;
2. explain the boundary clearly enough to be useful;
3. avoid exposing internal safeguards;
4. offer a safe, permitted alternative when appropriate;
5. log or escalate according to policy; and
6. do not repeatedly rephrase the request to evade the restriction.

Policies change. Verify the current authoritative text.

## 9. Change management

Review material changes to:

- model or provider;
- prompt or system instructions;
- tools and permissions;
- data sources;
- retrieval logic;
- user population;
- use case;
- output distribution;
- human review process;
- retention;
- policy; and
- monitoring thresholds.

A release record should include evaluation results, risk review, approver, rollback, and monitoring plan.

## 10. Exceptions

An exception process needs:

- named authority;
- documented scope;
- business justification;
- risk assessment;
- compensating controls;
- start and expiration dates;
- monitoring;
- revocation conditions; and
- audit trail.

The model cannot authorize an exception to governance policy.

## 11. Incident response

Potential incidents include:

- sensitive-data disclosure;
- unauthorized tool action;
- credential exposure;
- prompt injection success;
- poisoned knowledge;
- harmful high-impact recommendation;
- policy violation;
- unexplained model behavior; and
- audit-log compromise.

### Response sequence

1. Contain the affected workflow or permission.
2. Preserve relevant evidence.
3. Assess scope and affected parties.
4. Rotate credentials or revoke access where needed.
5. Notify the appropriate security, privacy, legal, product, and business owners.
6. Meet contractual or regulatory reporting obligations.
7. Remove or correct affected data and outputs.
8. Remediate the root cause.
9. Revalidate before restoration.
10. Document lessons and update controls.

Do not destroy evidence while attempting a quick fix.

## 12. Responsible-use review template

```text
Use case:
Affected users:
Decision impact:
Data classification:
Approved environment:
Model and tools:
Permissions:
Knowledge sources:
Human reviewer and authority:
Disclosure:
Evaluation:
Monitoring:
Incident owner:
Prohibited behavior:
Residual risk:
Approval:
Review date:
```

## 13. Common mistakes

| Mistake | Better approach |
|---|---|
| Review governance after prototype deployment | Design controls before data and tool access |
| Human sees only final answer | Show evidence, uncertainty, and action |
| Broad tool permissions for convenience | Least privilege and approval |
| Log everything indefinitely | Minimize, redact, restrict, expire |
| Treat provider policy as the only control | Apply all provider, legal, and organizational obligations |
| Let model approve exceptions | Named human governance authority |
| Retry after suspected exfiltration | Contain, preserve evidence, assess, and rotate |
| Assume external content is benign | Threat-model injection and poisoned sources |

## 14. Review questions

1. What makes human review meaningful?
2. Which controls prevent data from reaching the model?
3. How should a third-party integration be assessed?
4. What should happen first after suspected credential exfiltration?
5. Why must governance changes be regression tested?
