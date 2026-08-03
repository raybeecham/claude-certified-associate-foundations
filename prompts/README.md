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

Additional notebooks will be added as later course-aligned modules are completed.

## Usage discipline

Before using a template:

- define the business outcome and workflow boundary;
- map atomic work steps before selecting Skills, tools, or integrations;
- identify the source of truth, work type, output, side effect, and exception path for every step;
- assess reversibility, stakes, accountability, and propagation risk independently for each step;
- separate task preparation from decision authority;
- classify work as AI-appropriate, AI with code execution, collaborative, human-retained, deterministic, tool-owned, or storage-owned;
- route exact calculations, transformations, and reconciliation to code execution or deterministic logic;
- use Skills for repeatable procedures only after the step is judged AI-appropriate;
- make collaborative review real by naming a qualified reviewer with evidence, time, criteria, authority, and intervention rights;
- expose send, sign, file, pay, publish, and system-update actions as separate stages;
- place authorized approval before consequential or irreversible side effects;
- define exception ownership, escalation, stopping rules, and audit evidence;
- check for halo delegation and AI approval of its own work;
- preserve approved requirements, data definitions, constraints, decisions, and version history;
- generate bounded options and prototypes, classify feedback, and regression-test changes;
- distinguish prototype acceptance from production readiness;
- separate research, computation, synthesis, assumptions, and human judgment;
- execute material calculations over actual data and reconcile results;
- preserve requirements traceability and pressure-test the first extraction;
- persist long-running workflow state outside the prompt; and
- measure stage quality and business outcomes rather than prompt volume.

A prompt cannot enforce requirement approval, source authority, correct business rules, complete data, valid assumptions, stable state, production security, meaningful human review, legal or employment authority, workflow accountability, or irreversible-action approval by itself.

## Public-repository content rule

Do not place client names, nonpublic organizational details, confidential contracts, employment records, compensation data, requirements, datasets, prototypes, internal systems, credentials, system identifiers, full private conversation transcripts, remembered live-exam questions, or reconstructed proprietary course questions in these prompts. Use fictional, generic, synthetic, public, or sanitized descriptions.
