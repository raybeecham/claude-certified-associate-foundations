# Lesson 1: Module Introduction

## Overview

Most people begin using Claude by learning one or two tasks it performs well, such as drafting an email, summarizing a document, or answering questions. That approach can work for simple, one-time requests.

Professional work is different. Recurring workflows, team projects, and deliverables that must survive review depend on decisions made before the first prompt is written. Those choices establish the quality ceiling for the session.

This module introduces four foundational decisions:

1. **Entry point:** Where should Claude be used?
2. **Capability layer:** Which features should support the task?
3. **Model selection:** Which model best fits the required quality, speed, and volume?
4. **Context management:** How should information be organized and carried across the session or project?

These decisions determine whether Claude can build efficiently on prior work or whether the user must repeatedly reconstruct the task, requirements, and source material.

## Why this matters

Prompting is only one layer of a Claude workflow. A well-written prompt cannot fully compensate for:

- using the wrong product surface;
- omitting a needed capability;
- choosing a model that does not fit the task;
- overloading the session with irrelevant context; or
- failing to preserve continuity across recurring work.

A useful analogy is software architecture. Writing a prompt is like writing a function. Before writing the function, an engineer still decides which environment, tools, runtime, data sources, controls, and persistence model the system requires.

Claude should be approached the same way.

## Learning objectives

By the end of this module, you should be able to:

1. Select the appropriate Claude entry point and feature set for a professional task.
2. Differentiate Haiku, Sonnet, and Opus by capability characteristics and task fit.
3. Match model selection to quality, speed, cost, and volume requirements.
4. Manage context limitations and use continuity features appropriately across sessions.

## The four foundational decisions

| Decision | Core question | Why it matters |
|---|---|---|
| **Entry point** | Where should I use Claude? | Determines available interaction patterns, collaboration options, integrations, and controls. |
| **Capability layer** | Which features should I activate? | Determines whether the task can use capabilities such as Skills, code execution, files, or memory. |
| **Model selection** | Which model fits the task? | Balances quality, reasoning depth, latency, throughput, and cost. |
| **Context management** | What information should Claude have now, and what should persist? | Preserves continuity while limiting repetition, distraction, stale information, and context overload. |

## A practical decision flow

```text
Professional task
       |
       v
Choose an entry point
       |
       v
Select needed capabilities
       |
       v
Choose the appropriate model
       |
       v
Organize and manage context
       |
       v
Write the prompt
       |
       v
Evaluate the result
```

The sequence is important. Prompt wording comes after the environment, capabilities, model, and context strategy are understood.

## Real-world examples

### Example 1: One-time email draft

**Task:** Draft a follow-up email after a meeting.

**Likely design:**

- Entry point: Interactive Claude application
- Capability layer: No special capabilities required
- Model: A fast general-purpose model that meets the quality need
- Context: The current conversation and meeting notes

This is a simple, human-led task. A lightweight setup is sufficient.

### Example 2: Repository review

**Task:** Review a Python repository for maintainability and security issues.

**Likely design:**

- Entry point: An interactive coding surface or an API-backed workflow
- Capability layer: Repository access, files, and possibly code execution
- Model: A model with strong coding and reasoning performance
- Context: Relevant source files, architecture notes, constraints, and review criteria

The quality of the result now depends heavily on tool access, model fit, and context organization.

### Example 3: Federal compliance assessment

**Task:** Analyze policy, architecture, inventory, and evidence files over several weeks and produce an executive briefing.

**Likely design:**

- Entry point: A persistent project or controlled application workflow
- Capability layer: File handling, reusable instructions, structured knowledge, and code execution where appropriate
- Model: Selected through representative evaluation against quality and latency requirements
- Context: Curated authoritative sources, engagement-specific instructions, decision logs, and validated summaries

Here, workflow design matters more than any single prompt.

### Example 4: Cryptographic inventory triage

**Task:** Review a cryptographic bill of materials and identify systems likely to require post-quantum migration.

**Likely design:**

- Entry point: API or controlled project workspace
- Capability layer: File analysis and code execution for structured data
- Model: A model that meets the required accuracy on cryptographic classification tasks
- Context: Approved algorithms, agency policy, system metadata, risk criteria, and exception rules

The model should not be asked to infer current policy from memory when authoritative policy can be supplied directly.

## Example prompts

### Prompt 1: Workflow orientation

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

### Prompt 2: AI solutions architecture review

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

### Prompt 3: Professional task intake

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

### Prompt 4: Workflow self-assessment

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

## Engineering perspective

An experienced Claude user does not begin with, "What prompt should I write?"

They begin with questions such as:

- Is this a one-time human task or a repeatable system?
- Does the work require an interactive surface, an API, or a persistent workspace?
- Which capabilities are necessary, and which would add unnecessary complexity?
- What quality, latency, throughput, and cost requirements apply?
- Which information is authoritative, current, sensitive, or untrusted?
- What must be retained, summarized, redacted, or revalidated?
- Who is accountable for the final output?

This systems-oriented mindset produces workflows that are more reliable, reviewable, and maintainable.

## Common misconceptions

| Misconception | Better mental model |
|---|---|
| "A better prompt solves every problem." | Some problems require a different entry point, capability, model, or context strategy. |
| "The most capable model is always the right choice." | The correct model is the least costly and fastest option that reliably meets the validated requirement. |
| "Claude automatically remembers everything." | Continuity depends on the product feature or surrounding application and has defined scope and controls. |
| "More context always improves the answer." | Relevant, authoritative, and well-organized context is more useful than maximum context volume. |
| "A successful response means the workflow is well designed." | The result must still be evaluated for correctness, grounding, completeness, and repeatability. |

## Certification lens

Expect scenario-based questions that ask you to select the most appropriate workflow rather than merely identify a feature definition.

Use this four-question checklist:

1. Am I using the right entry point?
2. Am I activating the right capabilities?
3. Does the model fit the task's quality, speed, and volume requirements?
4. Is context being managed deliberately?

The best answer usually follows from the task requirements, not from choosing the most powerful option by default.

## Knowledge check

### 1. Which decision most directly controls the trade-off among quality, speed, and volume?

A. Entry point  
B. Capability layer  
C. Model selection  
D. File naming

**Answer:** C. Model selection.

### 2. True or false: Prompt engineering is the first and most important decision in every professional Claude workflow.

**Answer:** False. Entry point, capabilities, model fit, and context strategy can establish constraints before prompting begins.

### 3. A team repeatedly rebuilds the same background information at the start of every session. Which foundational area is weakest?

A. Output formatting  
B. Context management  
C. Temperature selection  
D. Writing style

**Answer:** B. Context management.

### 4. A high-volume classification task has a validated 98% accuracy requirement and a strict latency target. What is the best model-selection principle?

A. Always choose Opus  
B. Choose the newest model without testing  
C. Choose the fastest model that reliably meets the validated requirement  
D. Choose the model with the longest name

**Answer:** C. Model choice should follow representative evaluation and service requirements.

## Flashcards

**Q:** What four decisions establish the foundation of a Claude session?  
**A:** Entry point, capability layer, model selection, and context management.

**Q:** Why is prompt engineering alone insufficient for recurring professional work?  
**A:** Because environment, features, model fit, and context strategy also determine quality, continuity, and scalability.

**Q:** Which decision determines whether work can build efficiently across sessions?  
**A:** Context management, supported by the relevant product or application features.

**Q:** What should drive model selection?  
**A:** Measurable task requirements such as quality, reasoning depth, latency, throughput, cost, tools, and governance.

**Q:** What is the quality ceiling?  
**A:** The highest dependable result the chosen workflow design can support before prompt-level refinements are considered.

## Key takeaways

- Claude should be treated as a platform and workflow component, not only as a chatbot.
- Four decisions shape every session: entry point, capability layer, model, and context.
- These choices should follow the task's actual requirements.
- Prompting begins after the workflow foundation is established.
- Professional use requires evaluating the full system, not just the visible response.

## Connections to the rest of Module 1

- **How Claude Behaves** explains the behavioral characteristics that affect expectations and review.
- **Core Entry Points** compares where Claude can be used.
- **Capability Layer** explains Skills, code execution, memory, and related features.
- **Choosing Models** examines Haiku, Sonnet, and Opus trade-offs.
- **Context Management** explains continuity, limits, relevance, and session design.
