# Prompt Library

These templates are study aids and starting points, not universal production prompts. Adapt them to the use case, current platform capabilities, data policy, tool design, and evaluation results.

## Templates

1. [Task brief](task-brief-template.md)
2. [Grounded analysis](grounded-analysis-template.md)
3. [Structured extraction](structured-extraction-template.md)
4. [Evaluator rubric](evaluator-rubric-template.md)
5. [Workflow orchestrator](workflow-orchestrator-template.md)
6. [Governance review](governance-review-template.md)
7. [Troubleshooting](troubleshooting-template.md)

## Usage discipline

Before using a template:

- define success criteria;
- identify authoritative and untrusted inputs;
- remove secrets and unauthorized data;
- choose a narrow output contract;
- define missing-data behavior;
- constrain and validate tools;
- create representative tests; and
- establish human review where the output is consequential.

A prompt cannot enforce identity, authorization, data isolation, or irreversible-action approval by itself.
