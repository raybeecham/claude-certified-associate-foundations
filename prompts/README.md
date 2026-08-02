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

Additional notebooks will be added as later course-aligned modules are completed.

## Usage discipline

Before using a template:

- define success criteria and intended use;
- identify authoritative and untrusted inputs;
- remove secrets and unauthorized data;
- define missing-data and uncertainty behavior;
- evaluate requirements, source material, and professional standards;
- review accuracy and completeness separately;
- scan precise claims for provenance;
- compare repeated facts for inconsistency;
- challenge preferred conclusions and unequal scrutiny;
- verify source and requirement coverage;
- permit explicit `unknown`, `not covered`, and `conflicting` outcomes;
- require precise, auditable claim-to-source locations;
- validate consequential claims against authoritative sources;
- recompute material calculations deterministically;
- assess stakes, reversibility, audience, and governing obligations;
- identify automatic do-not-ship review gates;
- place approval before irreversible actions;
- preserve human and organizational accountability for release;
- define the audience contract and preserve factual invariants;
- distinguish presentation format from computation method;
- use code execution for material calculations and review the logic;
- validate structure separately from semantic correctness;
- de-duplicate, label, and prune inputs before processing;
- retain code, parameters, source versions, row counts, reconciliation, review, and approval evidence;
- distinguish output condition from intended-use risk;
- choose release, edit, verify, escalate, or reject;
- state the controlling reason and required next action;
- review your own Discernment and Diligence behavior after meaningful tasks;
- identify what property remains unproven in each scenario;
- choose the smallest intervention that establishes that property; and
- reject distractors based only on confidence, polish, repetition, model tier, formatting, or schema validity.

A prompt cannot enforce identity, authorization, data isolation, legal authority, factual accuracy, professional approval, disclosure authorization, correct code logic, meaningful human review, reflective judgment, or irreversible-action approval by itself.

## Public-repository content rule

Do not place client names, nonpublic organizational details, proprietary work products, confidential data, credentials, engagement-identifying examples, full private conversation transcripts, remembered live-exam questions, or reconstructed proprietary course questions in these prompts. Use fictional, generic, synthetic, public, or sanitized descriptions.
