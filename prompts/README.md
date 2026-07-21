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
2. [Worked Build prompts](module-02/02b-worked-build-prompts.md)

Additional notebooks will be added as the course-aligned lessons are completed.

## Usage discipline

Before using a template:

- define success criteria;
- identify authoritative and untrusted inputs;
- remove secrets and unauthorized data;
- choose a narrow output contract;
- define missing-data behavior;
- constrain and validate tools;
- create representative tests;
- establish human review where the output is consequential;
- define how context will be checkpointed, summarized, persisted, or discarded;
- justify the selected entry point, capability layers, model tier, and context strategy; and
- analyze why plausible alternatives are weaker rather than memorizing answer wording.

A prompt cannot enforce identity, authorization, data isolation, persistent-state integrity, legal authority, correct model selection, reliable context transfer, factual accuracy, or irreversible-action approval by itself.

## Public-repository content rule

Do not place client names, nonpublic organizational details, proprietary work products, confidential data, credentials, engagement-identifying examples, remembered live-exam questions, or reconstructed proprietary course questions in these prompts. Use fictional, generic, synthetic, or public scenarios.
