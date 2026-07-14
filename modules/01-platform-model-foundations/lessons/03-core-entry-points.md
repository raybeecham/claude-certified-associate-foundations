# Lesson 3: Core Entry Points

## Overview

Claude may appear to be one conversational interface, but the work can begin from four different operating patterns:

1. **Chat** for one-off or exploratory work.
2. **Projects** for recurring work with stable context.
3. **Artifacts** for outputs that should become editable deliverables.
4. **Research** for deeper, multi-source investigation and synthesis.

Choosing the entry point before writing the first prompt determines how much setup the task requires, how context is organized, how reusable the work becomes, and whether the result is delivered as a conversation or a work product.

> [!NOTE]
> The four options are composable, not mutually exclusive. A recurring investigation may live in a Project, use Research to gather current evidence, and produce an Artifact as the final deliverable.

## Learning objectives

After completing this lesson, you should be able to:

- select Chat, Projects, Artifacts, or Research based on the work pattern;
- identify when a recurring workflow has outgrown an ordinary Chat;
- explain the three core components of a Project;
- distinguish a conversational response from an Artifact deliverable;
- distinguish targeted web search from deeper Research;
- combine entry points into a coherent professional workflow; and
- account for persistence, source quality, access, and review requirements.

## The entry-point decision

Use this first-pass selection logic:

| Work pattern | Primary entry point | Reason |
|---|---|---|
| One-off question or quick task | Chat | Lowest setup cost |
| Recurring work with stable background | Project | Persistent instructions and curated knowledge |
| Output is a deliverable | Artifact | Separate, editable work product |
| Deep investigation across multiple sources | Research | Multi-step search and synthesis |

This is a starting point, not a rule that prevents combinations.

```text
Task
  |
  +-- One-off and conversational? ----------> Chat
  |
  +-- Recurring with stable context? -------> Project
  |
  +-- Recipient will open and use output? --> Artifact
  |
  +-- Deep multi-source investigation? -----> Research
```

## Entry points are workflow choices

The entry-point question is not simply, "Which feature is available?" It is:

> Where should this work live, how should context persist, and what form should the result take?

A prompt can be well written and still sit inside the wrong workflow. Repeatedly pasting the same background into new Chats creates avoidable setup. Producing a long report only as inline prose makes revision and handoff harder. Using Research for a simple lookup can add unnecessary time and complexity.

---

## Chat

### What Chat is

Chat is the default, flexible conversation surface. It is appropriate when the work begins and ends in one thread or when you are still exploring the task.

Common uses include:

- one-off questions;
- quick drafts;
- brainstorming;
- explanations;
- lightweight document review;
- targeted current-information lookup with web search, when available; and
- testing a prompt before deciding whether the workflow should become persistent.

A normal Chat can be saved to history and reopened, subject to account and workspace settings. Memory or past-chat search may also carry selected context into later work when those features are enabled. These forms of continuity are not the same as a Project's deliberate standing instructions and curated knowledge base.

### Strengths

- minimal setup;
- fast iteration;
- flexible conversation;
- useful for ambiguous or exploratory tasks; and
- easy to abandon when the task is complete.

### Limitations

- background may need to be reconstructed in a new thread;
- stable instructions can become scattered across conversation turns;
- source files may need to be supplied again outside a persistent workspace;
- a long thread can accumulate irrelevant or conflicting context; and
- it is easy to mix unrelated workstreams.

### Signals that work has outgrown Chat

Move toward a Project when you repeatedly:

- paste the same background paragraph;
- upload the same source files;
- restate the same role, tone, or output format;
- recreate the same checklist;
- correct the same terminology;
- search old conversations for the latest decision; or
- expect the workstream to continue over days or weeks.

### Example prompt: one-off analysis

```text
Summarize the attached public advisory for a nontechnical leadership audience.

Return:
- three key facts;
- affected systems;
- immediate actions;
- uncertainties; and
- source references.

Do not add details that are not supported by the advisory.
```

### Best mental model

Chat is a workbench. It is ideal for quick, flexible work, but it is not automatically a durable operating environment.

---

## Projects

### What a Project is

A Project is a persistent workspace for a defined workstream. It typically brings together three layers:

1. **Standing instructions:** durable guidance about role, process, terminology, source use, tone, and output expectations.
2. **Knowledge base:** curated documents, policies, references, examples, or other files supplied once for reuse.
3. **Project conversation list:** separate conversations that inherit the Project's instructions and knowledge.

```text
Project
  |
  +-- Standing instructions
  |
  +-- Curated knowledge base
  |
  +-- Conversation A: planning
  |
  +-- Conversation B: analysis
  |
  +-- Conversation C: deliverable review
```

### Important context boundary

Conversations inside the same Project share the Project's instructions and knowledge base. They do **not** automatically share the full conversational context of every other thread.

This means:

- stable background belongs in Project instructions or knowledge;
- decisions that must carry forward should be recorded deliberately;
- a detail mentioned only in Conversation A should not be assumed to appear in Conversation B; and
- each thread should have a clear purpose.

### When a Project is worth building

Evaluate three conditions:

| Condition | Question |
|---|---|
| Recurrence | Will this task or workstream happen again? |
| Stable background | Will the same policies, references, terminology, or constraints apply? |
| Consistent output | Will the deliverables follow a repeatable structure or quality standard? |

A useful course heuristic is to build a Project when at least two conditions are true.

### Project design checklist

Before adding files, define:

- purpose and boundaries;
- intended users;
- standing instructions;
- authoritative sources;
- source owners and versions;
- approved terminology;
- expected outputs;
- review and approval requirements;
- data handling restrictions;
- refresh cadence; and
- archive or deletion criteria.

### Knowledge-base discipline

A Project knowledge base should be curated, not treated as a file dump.

Include:

- authoritative and relevant documents;
- current versions;
- approved examples;
- source metadata; and
- clear distinctions between policy, guidance, evidence, and draft material.

Avoid:

- obsolete versions without labels;
- duplicate documents;
- unauthorized sensitive data;
- credentials or secrets;
- unrelated material; and
- drafts that could be mistaken for approved policy.

A Project is not a substitute for identity, authorization, retention, or data-governance controls.

### Example: recurring security assessment

A team performs recurring reviews of cryptographic inventories. The background framework, terminology, assessment rubric, and output structure remain stable. A Project can hold the approved methodology, glossary, public standards, and report template. Separate conversations can handle intake, evidence review, risk analysis, and final editing.

### Example standing-instructions prompt

```text
Help me design standing instructions for a recurring assessment Project.

The instructions must define:
- scope;
- source authority;
- approved terminology;
- analysis procedure;
- required output sections;
- missing-evidence behavior;
- prohibited assumptions;
- review checkpoints; and
- escalation conditions.

Keep task-specific facts out of the standing instructions.
```

### Best mental model

A Project is a deliberately configured workspace, not simply a folder of old chats.

---

## Artifacts

### What an Artifact is

An Artifact is appropriate when the result should exist as a work product rather than only as a conversational reply. It appears in a dedicated working area where the output can be viewed, edited, and iterated separately from the chat.

Common Artifact types include:

- reports;
- policies and procedures;
- decision memos;
- tables;
- code;
- diagrams;
- prototypes;
- visualizations; and
- structured reference material.

### Conversation versus deliverable

| Use an inline response when | Use an Artifact when |
|---|---|
| The answer supports the next conversational step | The output will be opened, edited, shared, or handed off |
| The content is short-lived | The content has a document-like lifecycle |
| You need a quick explanation | You need structured revision |
| The user will act immediately in the thread | A recipient will consume the result outside the immediate exchange |

### Artifact design questions

Before requesting an Artifact, define:

- intended recipient;
- purpose;
- format;
- required sections;
- source and citation expectations;
- editability requirements;
- acceptance criteria; and
- whether the result must remain inside an approved environment.

### Example prompt: decision memo Artifact

```text
Create the result as an editable decision-memo Artifact.

Audience: senior technical leadership
Purpose: select between three implementation approaches

Required sections:
1. Decision requested
2. Background
3. Evaluation criteria
4. Options
5. Trade-offs
6. Recommendation
7. Risks and mitigations
8. Open questions
9. Source notes

Clearly distinguish facts, assumptions, and recommendations.
```

### Important limitation

Creating an Artifact does not, by itself, make the content authoritative, verified, persistent project knowledge, or approved for distribution. The Artifact still needs the appropriate evidence checks and review.

### Best mental model

An Artifact is an output surface and collaboration object, not a truth guarantee.

---

## Research

### What Research is

Research is intended for deeper investigation across multiple sources. It can perform a sequence of searches, follow emerging questions, examine different angles, and synthesize the results into a cited response.

Research is a stronger fit when the task requires:

- a multi-source literature or market review;
- synthesis of recent information;
- comparison across organizations or standards;
- investigation that will generate follow-up questions;
- reconciliation of conflicting sources; or
- a briefing that needs a traceable source base.

### Web search versus Research

| Need | Targeted web search in Chat | Research |
|---|---|---|
| Confirm one current fact | Strong fit | Usually unnecessary |
| Locate one official page | Strong fit | Usually unnecessary |
| Answer a narrow current question | Strong fit | Possible but heavier |
| Investigate a broad issue | Limited | Strong fit |
| Run multiple linked searches | Limited | Strong fit |
| Compare many sources | Possible with manual prompting | Strong fit |
| Produce a synthesized research briefing | Possible for a small source set | Strong fit |

Availability, controls, and administrator settings can vary by plan and workspace. Check the current Claude Help Center before treating feature access as permanent.

### Research does not remove verification

A Research response can still:

- select weak sources;
- miss a relevant source;
- misunderstand a source;
- cite a passage that does not fully support the claim;
- combine facts from different dates; or
- present a synthesis more confidently than the evidence permits.

Review source authority, publication date, claim-to-citation alignment, conflicting evidence, and missing perspectives.

### Example prompt: research plan

```text
Research the current state of post-quantum cryptography migration guidance for large enterprises.

Before searching, define:
- research questions;
- inclusion and exclusion criteria;
- preferred primary sources;
- date range;
- comparison dimensions; and
- evidence-quality rules.

Then return:
1. executive summary;
2. findings by research question;
3. comparison table;
4. areas of agreement;
5. unresolved differences;
6. source-quality notes; and
7. claims that require further verification.
```

### Best mental model

Research is an investigation workflow, not merely a longer answer.

---

## Combining entry points

Professional work often uses several entry points together.

| Pattern | Workflow | Example |
|---|---|---|
| Quick answer | Chat | Explain a stable concept |
| Current lookup | Chat + web search | Confirm the current version of a public standard |
| Recurring analysis | Project | Apply the same rubric to new evidence |
| Deliverable production | Chat or Project + Artifact | Draft and revise a report |
| Deep current investigation | Research | Compare recent public guidance |
| Recurring research deliverable | Project + Research + Artifact | Maintain a periodic landscape briefing |

### Pattern: recurring research deliverable

```text
Project
  |
  +-- Standing methodology and source rules
  +-- Stable knowledge and templates
  |
  v
Research
  |
  +-- Current multi-source evidence
  |
  v
Artifact
  |
  +-- Editable briefing or report
  |
  v
Validation and accountable review
```

## Selection matrix

| Scenario | Recommended entry point or combination | Rationale |
|---|---|---|
| Ask a one-time conceptual question | Chat | No persistence requirement |
| Draft a quick email | Chat | Lightweight and conversational |
| Maintain a multi-week study workstream | Project | Stable instructions and reusable material |
| Produce an executive-ready report | Artifact | Deliverable lifecycle and editing |
| Compare current public guidance from several authorities | Research | Multi-source investigation and synthesis |
| Produce a monthly evidence-based briefing | Project + Research + Artifact | Persistence, current evidence, and deliverable output |
| Explore whether a workflow should be automated | Chat first, then Project if recurring | Start with low setup, persist after the pattern stabilizes |

## Common mistakes

### Using Chat for recurring work

**Symptom:** Repeatedly rebuilding background and uploading the same files.

**Better choice:** Create a Project with curated knowledge and standing instructions.

### Treating a Project as shared conversational memory

**Symptom:** Assuming every new Project conversation knows every detail from every other thread.

**Better choice:** Store stable context in Project configuration and preserve cross-thread decisions explicitly.

### Treating an Artifact as automatically final

**Symptom:** Sharing a polished-looking output without source or approval checks.

**Better choice:** Apply the same validation and review required for any deliverable.

### Using Research for a simple lookup

**Symptom:** A narrow question becomes a large, slower investigation.

**Better choice:** Use targeted web search in Chat when one current fact or official page is sufficient.

### Using web search without source discipline

**Symptom:** Recent but low-authority pages are treated as definitive.

**Better choice:** Prefer primary sources and verify that each citation supports the claim.

### Putting everything into one Project

**Symptom:** Unrelated workstreams, conflicting instructions, and excessive knowledge compete for attention.

**Better choice:** Give each Project a coherent purpose and boundary.

## Think like an AI solutions architect

Entry-point selection should follow requirements:

1. **Recurrence:** Will this happen again?
2. **Persistence:** What context must carry forward deliberately?
3. **Deliverable:** Is the output a work product or a conversational answer?
4. **Freshness:** Does the task require current evidence?
5. **Depth:** Is one lookup enough, or is multi-step investigation required?
6. **Governance:** Which data, sources, users, and review controls are allowed?
7. **Handoff:** Who will use the output, and in what form?

The feature choice follows these questions. It should not be driven by novelty.

## Hands-on lab: Select and compose entry points

### Objective

Choose the lowest-complexity entry point that still satisfies the workflow requirements.

### Instructions

For each scenario, record:

- primary entry point;
- optional secondary entry point;
- persistence requirement;
- source strategy;
- output form;
- review requirement; and
- why a simpler choice would be insufficient.

### Scenarios

1. A user needs a plain-language explanation of a stable technical term.
2. A team performs the same document review every month using an approved rubric.
3. An analyst needs a polished risk register that leadership will edit and circulate.
4. A researcher must compare current guidance across several public authorities.
5. A recurring research program produces a quarterly executive briefing.
6. A user wants to test several ways to phrase a short announcement.
7. A team has ten related chats but keeps losing decisions between threads.
8. A user needs one current product-support statement from the vendor's official documentation.

### Suggested answers

| Scenario | Recommended choice |
|---|---|
| 1 | Chat |
| 2 | Project |
| 3 | Artifact, possibly inside a Project |
| 4 | Research |
| 5 | Project + Research + Artifact |
| 6 | Chat |
| 7 | Project plus an explicit decision log or continuation brief |
| 8 | Chat with targeted web search |

## Certification lens

Expect scenario questions in which more than one feature could technically work. Choose the option that best matches persistence, depth, output, and reuse requirements.

Use this diagnostic sequence:

1. Is the task one-off or recurring?
2. Is the background stable enough to persist?
3. Is the requested result a deliverable?
4. Does the task need a quick current lookup or a deep investigation?
5. Would combining entry points create a better workflow?

A common exam trap is choosing the most advanced feature rather than the simplest feature that satisfies the requirements.

## Knowledge check

1. What is the strongest signal that a workflow has outgrown Chat?
2. What three components make a Project useful for recurring work?
3. Do conversations inside a Project automatically share their complete thread history?
4. When should an output become an Artifact?
5. How does targeted web search differ from Research?
6. Why might a monthly briefing use Project, Research, and Artifact together?
7. Does a Project replace authorization and data-governance controls?
8. Why is Research output still subject to source verification?

### Answer guide

1. The same background, files, instructions, or format are repeatedly reconstructed.
2. Standing instructions, curated knowledge, and a Project-specific conversation list.
3. No. They inherit Project instructions and knowledge, but each conversation has its own thread context.
4. When the result has a deliverable lifecycle and should be viewed, edited, shared, or handed off separately from the conversation.
5. Web search is suited to narrow current lookups; Research performs deeper, multi-step, multi-source investigation and synthesis.
6. The Project preserves the recurring methodology, Research gathers current evidence, and the Artifact provides the editable deliverable.
7. No. Those controls must be enforced by the product, organization, and surrounding process.
8. Research can still choose weak sources, miss evidence, or misalign claims and citations.

## Flashcards

**Q:** What are the four core entry points in this course framework?

**A:** Chat, Projects, Artifacts, and Research.

**Q:** What is Chat best for?

**A:** One-off, exploratory, or lightweight tasks that do not require deliberate persistence.

**Q:** What indicates that a task has outgrown Chat?

**A:** Repeatedly reconstructing the same background, files, instructions, or output format.

**Q:** What does a Project persist?

**A:** Standing instructions, curated knowledge, and an organized set of Project conversations.

**Q:** Do all conversations in a Project share full context?

**A:** No. They share Project instructions and knowledge, but each conversation retains its own thread context.

**Q:** When is a Project usually worth building?

**A:** When at least two are true: the task recurs, the background is stable, and the output format is consistent.

**Q:** What is the primary purpose of an Artifact?

**A:** To create a separate, editable work product rather than only an inline conversational response.

**Q:** What is Research best for?

**A:** Deep, multi-step investigation and synthesis across multiple current or connected sources.

**Q:** Can the entry points be combined?

**A:** Yes. A Project can use Research and produce an Artifact.

**Q:** What is the simplest-entry-point principle?

**A:** Choose the least complex option that fully satisfies persistence, source, output, and governance requirements.

## Key takeaways

- Use Chat for work that starts and ends in a lightweight conversation.
- Move recurring work with stable context into a Project.
- Use Artifacts when the output is a deliverable.
- Use Research when the task requires deep multi-source investigation, not merely one current lookup.
- Project conversations share configuration and knowledge, not every detail from other threads.
- Entry points can be composed into a complete workflow.
- Feature availability can change, so verify current plan and workspace behavior in official documentation.
- No entry point removes the need for evidence validation, access control, or accountable review.

## Related repository material

- [Lesson 1: Module Introduction](01-module-introduction.md)
- [Lesson 2: How Claude Behaves](02-how-claude-behaves.md)
- [Entry-point prompt notebook](../../../prompts/module-01/03-core-entry-points-prompts.md)
- [Broader platform notes](../notes.md)

## Official reading

Feature access and administrator controls change over time. Treat these pages as the current authority.

- [Claude Help Center](https://support.claude.com/en/)
- [Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)
- [Artifacts are now generally available](https://www.anthropic.com/news/artifacts)
- [Claude takes research to new places](https://www.anthropic.com/news/research)
