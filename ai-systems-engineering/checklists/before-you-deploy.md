# Before You Deploy

Use this before embedding an AI workflow into a recurring organizational process or application.

## Business readiness

- [ ] The use case and expected benefit are approved.
- [ ] Success and failure metrics are defined.
- [ ] The workflow has a named business owner.
- [ ] Human responsibilities and prohibited autonomous actions are explicit.

## Evaluation

- [ ] Representative tests cover normal, edge, missing, conflicting, adversarial, and high-consequence cases.
- [ ] A quality floor is defined.
- [ ] Release-blocking failures are defined.
- [ ] The selected model and workflow meet quality, latency, and cost thresholds.
- [ ] Baseline and rollback configurations are preserved.

## Security and privacy

- [ ] Data classification and authorization are complete.
- [ ] Least privilege is applied to tools, connectors, retrieval, and logs.
- [ ] Prompt-injection and data-exfiltration tests were performed.
- [ ] Secrets are stored outside prompts and code repositories.
- [ ] Retention, deletion, residency, and incident-response requirements are met.

## Reliability

- [ ] Input validation exists.
- [ ] Structured outputs are schema-validated.
- [ ] Calculations and business rules use deterministic components.
- [ ] Tool timeouts, retries, and idempotency are defined.
- [ ] Failed or ambiguous cases enter a safe fallback or escalation path.
- [ ] Context and durable state can be reconstructed after interruption.

## Operations

- [ ] Exact model, prompt, tools, sources, and settings are versioned.
- [ ] Logging is sufficient but privacy-minimized.
- [ ] Dashboards or alerts cover severe failures, latency, cost, and tool errors.
- [ ] Reviewer overrides and escaped errors can be measured.
- [ ] Support and incident ownership are assigned.
- [ ] The workflow can be disabled quickly.

## Rollout

- [ ] Start with synthetic or low-risk data.
- [ ] Use shadow mode, pilot users, or limited scope where practical.
- [ ] Compare results with the existing process.
- [ ] Expand only after acceptance criteria remain satisfied.
- [ ] Communicate limitations and user responsibilities.

## Change management

Reevaluate before changing:

- model or effort settings;
- prompt or Skill;
- retrieval source;
- tool definition;
- permissions;
- output schema;
- policy or business rule; or
- target users.

## Deployment decision

**Decision:** Deploy / Pilot / Restrict / Revise / Reject

**Approver:**

> 

**Conditions and rollback trigger:**

> 
