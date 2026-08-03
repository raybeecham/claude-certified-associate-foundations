# Prompt Library

These templates are study aids and starting points, not universal production prompts. Adapt them to the use case, current platform capabilities, data policy, tool design, and evaluation results.

## General templates

1. [Task brief](task-brief-template.md)
2. [Grounded analysis](grounded-analysis-template.md)
3. [Structured extraction](structured-extraction-template.md)
4. [Evaluator rubric](evaluator-rubric-template.md)
5. [Workflow orchestrator](workflow-orchestrator-template.md)
6. [Governance review](governance-review-template.md)
7. [Troubleshooting](troubleshooting-template.md)

## Module study notebooks

### Module 1: Claude Platform & Model Foundations

1. [Workflow foundation prompts](module-01/01-workflow-foundation-prompts.md)
2. [How Claude Behaves prompts](module-01/02-how-claude-behaves-prompts.md)
3. [Core Entry Points prompts](module-01/03-core-entry-points-prompts.md)
4. [Core Entry Points worked-example prompts](module-01/03a-core-entry-points-worked-example-prompts.md)
5. [Capability Layer, Skills and Code Execution prompts](module-01/04-capability-layer-skills-code-execution-prompts.md)
6. [Capability Layer, Memory prompts](module-01/04a-capability-layer-memory-prompts.md)
7. [Capability Layer scenario prompts](module-01/04b-capability-layer-scenario-prompts.md)
8. [Capability Layer checkpoint prompts](module-01/04c-capability-layer-checkpoint-prompts.md)
9. [Choosing Models prompts](module-01/05-choosing-models-prompts.md)
10. [Context Management prompts](module-01/06-context-management-prompts.md)
11. [Platform Selection Exercise prompts](module-01/07-platform-selection-exercise-prompts.md)
12. [Module 1 quiz and remediation prompts](module-01/08-module-1-quiz-prompts.md)
13. [Module 1 Key Takeaways prompts](module-01/09-key-takeaways-prompts.md)

### Module 2: Prompting & Task Execution

1. [Module Introduction prompts](module-02/01-module-introduction-prompts.md)
2. [Component Stack prompts](module-02/02a-component-stack-prompts.md)
3. [Worked Build prompts](module-02/02b-worked-build-prompts.md)
4. [Task Decomposition prompts](module-02/03a-decomposition-prompts.md)
5. [Parallel Case prompts](module-02/03b-parallel-case-prompts.md)
6. [Iterating to Improve Output prompts](module-02/04-iterating-to-improve-output-prompts.md)
7. [Strategy by Task Type prompts](module-02/05a-strategy-by-task-type-prompts.md)
8. [Strategy Checkpoint prompts](module-02/05b-strategy-checkpoint-prompts.md)
9. [Repair-the-Prompt prompts](module-02/06-repair-the-prompt-prompts.md)
10. [Module 2 quiz and remediation prompts](module-02/07a-module-2-quiz-prompts.md)
11. [Module 2 Key Takeaways prompts](module-02/07b-key-takeaways-prompts.md)
12. [Module 2 completion and transition prompts](module-02/08-module-complete-prompts.md)

### Module 3: Evaluating & Validating Claude's Output

1. [Module Introduction prompts](module-03/01-module-introduction-prompts.md)
2. [Discernment: Accuracy and Completeness prompts](module-03/02-discernment-accuracy-completeness-prompts.md)
3. [Hallucinations, Inconsistencies, and Bias prompts](module-03/03-hallucinations-inconsistencies-bias-prompts.md)
4. [Fact-Checking and Grounding prompts](module-03/04-fact-checking-grounding-prompts.md)
5. [Diligence and Human Review prompts](module-03/05-diligence-human-review-prompts.md)
6. [Editing and Audience Adaptation prompts](module-03/06-editing-adapting-audience-prompts.md)
7. [Choosing Output Formats prompts](module-03/07-choosing-output-formats-prompts.md)
8. [Triage the Output Set prompts](module-03/08a-triage-output-set-prompts.md)
9. [Self-Assessment prompts](module-03/08b-self-assessment-prompts.md)
10. [Module 3 quiz and remediation prompts](module-03/09a-module-3-quiz-prompts.md)
11. [Module 3 Key Takeaways prompts](module-03/09b-key-takeaways-prompts.md)
12. [Module 3 completion and transition prompts](module-03/10-module-complete-prompts.md)

### Module 4: Workflow Integration & Solution Design

1. [Module Introduction prompts](module-04/01-module-introduction-prompts.md)
2. [Analyzing Requirements and Use Cases prompts](module-04/02-analyzing-requirements-use-cases-prompts.md)
3. [Research, Planning, and Process Optimization prompts](module-04/03-research-planning-process-optimization-prompts.md)
4. [Solution Design, Development, and Iteration prompts](module-04/04-solution-design-development-iteration-prompts.md)
5. [Delegation Mapping prompts](module-04/05-delegation-mapping-prompts.md)
6. [Communicating Value and Limitations prompts](module-04/06-communicating-value-limitations-prompts.md)
7. [Redesign a Workflow prompts](module-04/07-redesign-a-workflow-prompts.md)
8. [Module 4 quiz and remediation prompts](module-04/08a-module-4-quiz-prompts.md)
9. [Module 4 Key Takeaways prompts](module-04/08b-key-takeaways-prompts.md)

### Module 5: Configuration & Knowledge Management

1. [Module Introduction prompts](module-05/01-module-introduction-prompts.md)
2. [Configuring Projects prompts](module-05/02-configuring-projects-prompts.md)
3. [Connectors and Uploaded Knowledge prompts](module-05/03-connectors-uploaded-knowledge-prompts.md)
4. [System-Level Instructions prompts](module-05/04-system-level-instructions-prompts.md)
5. [Maintaining Configurations prompts](module-05/05-maintaining-configurations-prompts.md)
6. [Module 5 quiz and remediation prompts](module-05/06a-module-5-quiz-prompts.md)
7. [Module 5 Key Takeaways prompts](module-05/06b-key-takeaways-prompts.md)

Additional notebooks will be added as later course-aligned sections are completed.

## Usage discipline

Before using a template:

- distinguish a one-time prompt from a maintained operating baseline;
- place behavior, facts, procedures, continuity, access, exact controls, and durable state in the correct layer;
- assign one authoritative home and pair mechanisms without duplicating authority;
- separate sensitive workstreams when purpose, users, sources, disclosure boundaries, or continuity materially differ;
- treat Project separation as context scoping rather than a replacement for identity, permissions, or data controls;
- treat connector availability as access, not authority;
- document connector identity, scope, capabilities, unsupported actions, and approval boundaries;
- apply least privilege and separate retrieve, draft, approve, execute, and record-state stages;
- curate sources by owner, authority, effective date, review date, scope, sensitivity, version, refresh type, conflicts, and replacement;
- remove or label duplicate and superseded sources;
- define persistent instructions with trigger, required behavior, evidence boundary, failure behavior, and observable output;
- apply the two-reader test and pair consequential guidance with enforceable controls;
- inventory instructions, knowledge, Skills, connectors, and Memory as versioned operational assets;
- schedule recurring and event-triggered reviews;
- inspect the full configured baseline when output drifts without a prompt change;
- distinguish Anthropic, organization-provisioned, shared, directory-installed, and personal Skill distribution paths;
- update or re-upload owner-managed personal Skills when procedures change;
- review Memory for accuracy, relevance, and appropriate authority placement;
- export approved context before destructive Memory changes where appropriate;
- treat reset as irreversible and use it only when selective repair is insufficient;
- recertify connector identity, permissions, tools, business need, offboarding, and revocation;
- choose edit, replace, disable, revoke, reset, rollback, or retirement according to the defect;
- rerun representative and adversarial tests after material change;
- reject distractors based only on stronger models, more careful one-time prompting, or connecting more sources;
- preserve rollback paths and release evidence;
- keep secrets outside prompts, instructions, repositories, files, knowledge, Skills, Memory, and connector configuration; and
- preserve Module 4 disciplines for requirements, calculations, delegation, review, and stakeholder communication.

A prompt or configuration cannot by itself enforce source authority, identity, authorization, data isolation, connector permissions, secret handling, factual accuracy, correct business rules, professional approval, durable state, confidentiality, or irreversible-action authorization.

## Public-repository content rule

Do not place client names, nonpublic organizational details, confidential instructions, emails, files, connector identifiers, credentials, internal policies, Skill packages, Memory exports, production dependencies, private transcripts, remembered live-exam questions, or reconstructed proprietary course questions in these prompts. Use fictional, generic, synthetic, public, or sanitized descriptions.