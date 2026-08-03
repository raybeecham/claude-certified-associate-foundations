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

Additional notebooks will be added as later course-aligned modules are completed.

## Usage discipline

Before using a template:

- define the business outcome and intended decision before selecting a capability;
- distinguish personal productivity from a repeatable workflow;
- inventory sources and establish the controlling-source hierarchy;
- convert broad needs into actors, triggers, inputs, outputs, owners, and acceptance criteria;
- extract atomic requirements into a structured register rather than a narrative summary;
- preserve exact source traceability;
- distinguish explicit, implied, ambiguous, missing, conflicting, assumed, and constrained requirements;
- pressure-test the first extraction for omissions, hidden conditions, conflicts, duplicates, and testability;
- preserve unresolved uncertainty instead of filling gaps with confident prose;
- distinguish a product capability from a viable use case with measurable value and human ownership;
- map workflow stages, owners, inputs, outputs, decisions, state, and side effects;
- separate task assistance from decision authority;
- classify responsibilities as AI-appropriate, human-retained, collaborative, deterministic, tool-owned, or storage-owned;
- identify authoritative and untrusted inputs;
- remove secrets and unauthorized data;
- permit explicit `unknown`, `not covered`, and `conflicting` outcomes;
- validate consequential claims and calculations independently;
- assess stakes, reversibility, audience, and governing obligations;
- place approval before irreversible actions;
- preserve human and organizational accountability;
- distinguish presentation format from computation method;
- persist long-running state outside the prompt;
- define retries, idempotency, fallback, rollback, escalation, and failure ownership;
- measure stage quality and business outcomes rather than prompt volume; and
- choose the smallest intervention and workflow that establish the required property.

A prompt cannot enforce source authority, requirement approval, identity, authorization, data isolation, legal authority, factual accuracy, correct code logic, durable state, meaningful human review, workflow authority, or irreversible-action approval by itself.

## Public-repository content rule

Do not place client names, nonpublic organizational details, confidential solicitations, proposal materials, proprietary workflows, credentials, system identifiers, full private conversation transcripts, remembered live-exam questions, or reconstructed proprietary course questions in these prompts. Use fictional, generic, synthetic, public, or sanitized descriptions.
