# Module 1 Prompt Library: Workflow Foundations

These prompts support the **Module Introduction** lesson in Claude Platform & Model Foundations. Replace bracketed fields with task-specific information.

## 1. Workflow orientation

```text
I am beginning a new Claude-assisted project.

Before performing the task, recommend:

1. The most appropriate Claude entry point.
2. The capabilities or features the workflow should use.
3. The model characteristics required for the task.
4. A context-management strategy for both the current session and recurring work.

For each recommendation, explain the requirement that drives the choice. Identify any assumptions that need validation.

Project:
[Describe the project, users, data, deliverables, frequency, and constraints.]
```

## 2. AI solutions architecture review

```text
Act as an AI solutions architect.

Evaluate the following proposed Claude workflow across four dimensions:

- Entry point
- Capability layer
- Model selection
- Context management

For each dimension:

1. State whether the current choice fits the task.
2. Identify risks or limitations.
3. Recommend a better option when needed.
4. Define how the recommendation should be tested.

Workflow description:
[Insert the proposed workflow.]
```

## 3. Professional task intake

```text
Help me design a Claude workflow for the task below.

Do not begin the task yet. First produce a concise intake table covering:

- Task objective
- Users and reviewers
- Frequency and volume
- Data sensitivity
- Required tools or files
- Quality threshold
- Latency requirement
- Need for continuity across sessions
- Human approval requirements

Then recommend the entry point, capabilities, model profile, and context strategy.

Task:
[Insert task.]
```

## 4. Workflow self-assessment

```text
Review how I used Claude for this project.

Assess whether I selected:

- The correct entry point
- The necessary capabilities
- An appropriate model
- An effective context-management strategy

Separate problems caused by workflow design from problems caused by prompt wording. Rank improvements by expected impact and explain how I should validate each one.

Project summary:
[Insert summary.]
```

## 5. Federal and security workflow intake

```text
Act as a security-conscious AI workflow architect.

Design a Claude-assisted workflow for the use case below. Address:

- Appropriate Claude entry point
- Required capabilities and tools
- Model-selection criteria
- Authoritative source material
- Context and continuity strategy
- Data classification and handling constraints
- Least-privilege access
- Human review and approval points
- Logging and reproducibility requirements
- Evaluation criteria before operational use

Do not assume that pretrained model knowledge is current or authoritative when policy or technical standards can be supplied directly.

Use case:
[Insert the federal, cybersecurity, cloud, or cryptographic use case.]
```

## Suggested use

Use these prompts to practice separating **workflow architecture** from **prompt wording**. A good answer should trace every recommendation back to a concrete task requirement rather than defaulting to the most powerful model or largest feature set.
