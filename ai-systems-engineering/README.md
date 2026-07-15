# AI Systems Engineering Playbook

A vendor-neutral methodology for designing AI-assisted workflows that are useful, reliable, repeatable, efficient, secure, and accountable.

> **Core principle:** Prompts generate answers. Workflow design determines whether those answers are reliable, repeatable, efficient, and trustworthy.

## Why this exists

Prompting is only one layer of an AI system. A strong prompt cannot compensate for:

- an unclear business problem;
- the wrong workspace or product surface;
- missing or unauthorized evidence;
- an unsuitable model;
- a calculation performed through prose;
- uncontrolled tools or permissions;
- degraded context;
- absent validation; or
- unclear human accountability.

This playbook turns those concerns into a repeatable engineering method.

## The eight-step method

```text
1. Define the business problem
           ↓
2. Choose the workspace
           ↓
3. Select capabilities
           ↓
4. Choose the model
           ↓
5. Design the context strategy
           ↓
6. Design the workflow and prompt
           ↓
7. Validate the output
           ↓
8. Deliver, monitor, and improve
```

## The six questions to ask every time

1. Where should this work live?
2. What capabilities are actually needed?
3. What is the minimum qualified model?
4. How will context stay focused and current?
5. How will the output be verified?
6. What remains under human responsibility?

## Start here

1. Read [Philosophy](philosophy.md).
2. Use the [Workflow](workflow.md) as the standard operating procedure.
3. Complete the [AI Project Canvas](worksheets/ai-project-canvas.md).
4. Complete the [Workflow Design Canvas](worksheets/workflow-design-canvas.md).
5. Complete the [Prompt Planning Canvas](worksheets/prompt-planning-canvas.md).
6. Define acceptance criteria in the [Evaluation Canvas](worksheets/evaluation-canvas.md).
7. Review risk and accountability in the [Governance Canvas](worksheets/governance-canvas.md).
8. Run the appropriate checklist before prompting, publishing, or deploying.

## Repository structure

```text
ai-systems-engineering/
├── README.md
├── philosophy.md
├── workflow.md
├── worksheets/
│   ├── ai-project-canvas.md
│   ├── workflow-design-canvas.md
│   ├── prompt-planning-canvas.md
│   ├── evaluation-canvas.md
│   └── governance-canvas.md
├── checklists/
│   ├── before-you-prompt.md
│   ├── before-you-publish.md
│   └── before-you-deploy.md
├── mental-models/
│   ├── README.md
│   ├── workflow-over-prompts.md
│   ├── deterministic-vs-generative.md
│   └── context-as-working-memory.md
└── case-studies/
    ├── README.md
    └── case-study-template.md
```

## Design principles

### Problem first

Describe the business outcome before describing the prompt.

### Minimum sufficient architecture

Use the least complex configuration that meets the requirement. Every added model, tool, connector, memory layer, or autonomous action creates maintenance and risk.

### Separation of concerns

Separate:

- durable instructions;
- reusable knowledge;
- current task inputs;
- generative reasoning;
- deterministic computation;
- external authoritative state;
- validation; and
- human approval.

### Evidence over fluency

Professional tone is not proof. Require evidence, calculation, validation, and accountable review based on consequence.

### Evaluation before optimization

Define the quality floor before optimizing speed, model tier, or cost.

### Human responsibility remains explicit

AI may assist analysis, drafting, classification, and planning. People and authorized systems retain accountability for consequential decisions and actions.

## Vendor-neutral mapping

The method applies across Claude, ChatGPT, Gemini, open-source models, and future platforms.

| Engineering concern | Example implementation |
|---|---|
| Persistent workstream context | Project, workspace, repository, knowledge base |
| Reusable procedure | Skill, agent instruction, workflow template |
| Executed computation | Code interpreter, sandbox, deterministic service |
| Current evidence | Search, retrieval, connectors, supplied sources |
| Deliverable | Artifact, document, spreadsheet, slide deck, code repository |
| Long-term continuity | Memory, profile, durable state store |
| Validation | Tests, evaluators, source checks, human review |

## Public-repository rule

Use fictional, synthetic, public, or explicitly authorized examples. Do not include client names, confidential data, credentials, proprietary procedures, or facts that identify a nonpublic engagement.
