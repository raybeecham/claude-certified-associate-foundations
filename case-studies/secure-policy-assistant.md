# Case Study: Secure Policy Assistant

## Mission

An enterprise wants a conversational assistant that answers internal security-policy questions, explains which requirements apply, and drafts exception-request text.

## Environment

The knowledge collection contains:

- current approved policies;
- historical versions;
- standards owned by different business units;
- implementation guides;
- legal interpretations;
- ticket comments;
- vendor documentation; and
- meeting notes.

The assistant serves users from multiple regions and business units.

## Failure reports

- It sometimes cites historical policy.
- It answers one business unit using another unit's confidential implementation guide.
- It treats a vendor document as proof of compliance.
- A malicious ticket comment tells it to send policy sources to an external URL.
- Users assume that a draft exception is already approved.
- Audit logs contain full questions and attached documents indefinitely.

## Analysis tasks

### Platform and model

- Choose an interaction pattern and explain why.
- Define candidate model tests.
- Describe state, context, current knowledge, and output requirements.

### Prompting

- Create a task contract.
- Define source authority and missing-evidence behavior.
- Distinguish policy, interpretation, guide, vendor claim, and notes.
- Define a clear draft watermark and disclosure.

### Evaluation

- Create a slice-based evaluation plan.
- Include cross-business-unit access tests.
- Verify citation support and effective dates.
- Define consistency expectations.
- Define critical release gates.

### Workflow

- Design retrieval, answer generation, validation, and exception drafting.
- Define an `create_draft_exception_request` tool.
- Require human governance review before an exception gains any status.
- Handle retries and duplicate drafts.

### Knowledge management

- Build a source register.
- Define supersession and conflict rules.
- Define freshness alerts.
- Analyze prompt-caching candidates.

### Governance

- Classify user questions and attached documents.
- Define logging minimization and retention.
- Threat-model prompt injection and compromised connectors.
- Define exception authority.
- Write an incident playbook for cross-unit disclosure.

### Troubleshooting

Design a controlled investigation for each reported failure. Identify evidence, likely layer, hypothesis, fix, regression test, and rollback.

## Deliverable

Write a decision memo with:

- executive summary;
- architecture;
- principal risks;
- controls;
- evaluation results required before launch;
- residual risk;
- accountable owners; and
- launch recommendation.

## Strong-solution indicators

- Historical documents remain searchable but cannot silently govern.
- Identity-aware access filters run before retrieval.
- Vendor statements are labeled as claims.
- External content cannot authorize tools.
- Drafts are unmistakably unapproved.
- Logs retain the minimum data needed for audit.
- An incident involving cross-unit disclosure triggers containment and review.
