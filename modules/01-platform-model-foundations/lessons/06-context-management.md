# Lesson 6: Context Management

## Overview

Model selection and capability configuration determine what Claude can do. Context management determines how long a session can remain coherent, efficient, and aligned with the task.

Every conversation has a finite working-memory budget. Messages, uploaded documents, images, tool definitions, tool results, instructions, and generated output all consume that budget. As a session grows, old information can become harder to retrieve accurately, irrelevant material can distract from the current task, and compressed summaries can lose detail.

The core operating principle is:

> Treat context as a managed budget, not an unlimited transcript.

This lesson focuses on four practical responsibilities:

1. detect context degradation;
2. choose whether to restart, summarize, or persist;
3. maintain conversation and Memory hygiene; and
4. plan around both context-length limits and usage limits.

## Learning objectives

After completing this lesson, you should be able to:

- explain what consumes a context window;
- distinguish a context or length limit from a usage limit;
- recognize signs that a conversation is losing earlier context;
- explain how automatic context management works in paid Claude chats;
- choose among restart, summarize, and persist;
- create a reliable handoff summary for a new conversation;
- decide what belongs in the current thread, a Project, Memory, or an external record;
- reduce unnecessary context from files, tools, duplicated instructions, and unrelated tasks;
- plan long work across multiple sessions without losing important decisions;
- manage Memory for freshness and scope;
- monitor session and weekly usage budgets; and
- preserve security, authority, and human review across context transitions.

## The context window in practical terms

The context window is the information Claude can reference while generating the next response.

It can include:

- system or product instructions;
- Project standing instructions;
- current and prior conversation turns;
- uploaded files, images, and document excerpts;
- retrieved Project knowledge;
- web-search or Research results;
- tool definitions;
- tool calls and tool results;
- examples and output schemas;
- extended-thinking content, depending on the model and product; and
- the response Claude is currently generating.

```text
Context window
   |
   +-- Trusted instructions
   +-- Conversation history
   +-- Current user request
   +-- Files and images
   +-- Retrieved evidence
   +-- Tool definitions and results
   +-- Generated output
```

A larger window permits more material, but more context is not automatically better. Relevant, authoritative, well-organized context is more useful than a larger collection of duplicated, stale, or conflicting material.

### Capacity versus usable quality

A session can degrade before it reaches a hard technical limit.

```text
Nominal context capacity
          !=
Guaranteed recall and reasoning quality
```

As context grows:

- early instructions compete with later content;
- irrelevant turns consume attention;
- conflicting decisions can remain active;
- tool output can dominate the thread;
- duplicated documents add noise;
- stale facts can remain available; and
- summaries can compress distinctions that once appeared explicitly.

Anthropic's current API documentation describes this degradation as **context rot**: accuracy and recall may decline as token count grows. The practical implication is that context should be curated for relevance, not filled merely because capacity exists.

## Automatic context management in Claude

As of July 14, 2026, Anthropic's Help Center states that paid Claude plans can automatically manage long conversations when Code Execution is enabled.

When a conversation approaches the context-window limit:

1. Claude summarizes earlier messages;
2. the compressed summary makes room for new content;
3. the full chat history remains preserved for reference; and
4. the conversation can usually continue without a hard interruption.

You may see Claude display a message indicating that it is organizing its thoughts while this occurs.

> [!IMPORTANT]
> Automatic context management extends a conversation. It does not guarantee that every early detail will retain the same prominence or precision after summarization.

### Why compression still requires deliberate management

A summary is a derived representation of earlier content. Compression can preserve the major storyline while weakening:

- exact wording;
- exceptions;
- negative constraints;
- source authority;
- unresolved disagreements;
- version identifiers;
- detailed acceptance criteria;
- distinctions between facts and assumptions; and
- instructions that appeared only once early in the session.

Therefore, critical state should not depend solely on implicit automatic summarization.

Use explicit checkpoints for decisions and constraints that must survive a long session.

## Signs a conversation needs intervention

Intervene when Claude:

- stops following instructions that worked earlier;
- omits required sections or formatting rules;
- focuses only on the latest exchange;
- contradicts an earlier accepted decision;
- forgets an important definition or constraint;
- reopens a question that was already resolved;
- treats an assumption as a confirmed fact;
- cites the wrong version of a source;
- loses track of open actions or owners;
- applies context from an unrelated subtask;
- produces answers consistent with missing early-session detail; or
- requires repeated correction of the same point.

### Context degradation is a diagnosis, not a certainty

Similar symptoms can also come from:

- ambiguous prompting;
- conflicting Project instructions;
- stale Project knowledge;
- an underpowered model;
- incorrect retrieval;
- tool failure;
- an output-length limit; or
- ordinary probabilistic variation.

Before restarting, ask whether the problem is truly context degradation or another workflow defect.

## The three responses: restart, summarize, persist

The course provides three actions for recovering or preserving context.

```text
Context problem
     |
     +-- Thread drifted or task changed? ------> Restart
     |
     +-- Thread state must transfer? ----------> Summarize
     |
     +-- Information should survive broadly? -> Persist
```

The three actions are complementary. A strong transition often uses all three:

1. summarize the current state;
2. persist the durable parts in the correct location; and
3. restart in a clean conversation with the approved handoff.

## Restart

Restart means opening a new conversation.

Within a Project, the new conversation inherits the Project's standing instructions and knowledge base. It does not automatically inherit the full conversational state of the prior thread.

### Restart when

- the current task is complete and a new task is beginning;
- unrelated work has accumulated in one thread;
- corrections and reversals have made the thread confusing;
- earlier assumptions are no longer valid;
- the session repeatedly ignores accepted instructions;
- the conversation has become difficult to audit;
- an experiment should be separated from approved work;
- source scope has materially changed; or
- the session is consuming excessive usage merely to preserve a bloated history.

### Restart is not failure

A new conversation can improve:

- focus;
- reproducibility;
- source control;
- instruction clarity;
- reviewability;
- usage efficiency; and
- separation of workstreams.

### Restart checklist

Before leaving the old thread:

1. identify completed work;
2. capture accepted decisions;
3. record open questions;
4. save or export any deliverables;
5. identify authoritative source versions;
6. remove secrets or unnecessary sensitive data from the handoff;
7. determine what should be persisted elsewhere;
8. create a validated state summary; and
9. state the objective of the new conversation.

## Summarize

Summarize means producing a compact handoff that preserves the state required by the next conversation.

A weak summary says:

> We discussed the report and need to finish it.

A useful summary preserves operational state.

### State-capsule structure

Use this structure:

```text
Objective
Scope
Accepted decisions
Authoritative sources and versions
Requirements and constraints
Definitions and terminology
Completed work
Work in progress
Open questions
Risks and uncertainties
Rejected approaches
Next actions
Required review and approval
```

### Example handoff prompt

```text
Create a state capsule for continuing this work in a new conversation.

Preserve:
- objective and scope;
- accepted decisions and their rationale;
- authoritative sources, versions, and dates;
- definitions and approved terminology;
- requirements, constraints, and prohibitions;
- completed work and current deliverables;
- open questions and unresolved evidence;
- risks, assumptions, and uncertainties;
- rejected options that should not be reconsidered without new evidence;
- owners and next actions; and
- required validation and human approval.

Separate confirmed facts from assumptions.
Do not add new conclusions.
Flag any conflict or detail that cannot be compressed safely.
```

### Validate the summary

Before using the summary in a new thread:

- compare it with the original decisions;
- verify source versions and dates;
- confirm all negative constraints survived;
- check that assumptions remain labeled;
- confirm open questions were not converted into answers;
- ensure sensitive information is still authorized;
- remove obsolete or duplicate details; and
- have an accountable person approve consequential state.

> [!WARNING]
> A summary can propagate an error more efficiently than the original conversation. Treat handoff summaries as reviewable artifacts.

## Persist

Persist means moving durable information out of the fragile session transcript and into the correct long-lived layer.

### Persistence placement model

| Information | Correct home |
|---|---|
| Stable workstream behavior | Project standing instructions |
| Curated reusable evidence | Project knowledge |
| General cross-session preference | Memory, when appropriate |
| Project-specific continuity | Project Memory or Project summary, when available |
| Current task facts | Current conversation |
| Accepted decision requiring traceability | Decision log or formal record |
| Current operational state | Authoritative external system |
| Repeatable procedure | Skill |
| Calculated result and audit trail | Code Execution output plus approved record |

### Persist selectively

Do not persist information merely because it might be useful someday.

Persist only when the information is:

- expected to recur;
- stable enough to remain valid;
- authorized for retention;
- placed in the correct scope;
- assigned an owner or source;
- reviewable and correctable; and
- subject to a refresh or deletion rule.

### When not to persist

Avoid persisting:

- temporary debugging details;
- superseded decisions;
- raw untrusted instructions;
- credentials or secrets;
- one-time personal or contractual details;
- unresolved claims;
- current incident facts that belong in an incident system;
- full documents when a controlled repository should remain authoritative; or
- context that applies to only one task instance.

## Conversation hygiene

Conversation hygiene keeps the active context focused before degradation becomes visible.

### 1. Give each thread a clear purpose

Prefer:

```text
Conversation A: source review
Conversation B: analytical decisions
Conversation C: deliverable drafting
Conversation D: final validation
```

Avoid one thread that mixes research, brainstorming, coding, policy review, unrelated questions, and final publication.

### 2. Front-load the task contract

At the beginning of a conversation, state:

- objective;
- audience;
- source scope;
- required output;
- acceptance criteria;
- prohibited assumptions;
- escalation rules; and
- review requirements.

### 3. Use checkpoints after major decisions

After a milestone, ask Claude to restate:

- what was decided;
- what evidence supports it;
- what changed;
- what remains unresolved; and
- what must carry forward.

### 4. Avoid unnecessary duplication

Do not repeatedly:

- upload the same file inside one conversation;
- paste identical background paragraphs;
- restate every prior turn;
- include multiple copies of the same policy; or
- keep obsolete drafts in active context.

### 5. Keep Project instructions concise

Project instructions should contain durable guidance, not every temporary task detail. Overly long instructions consume context and make conflicts harder to detect.

### 6. Curate Project knowledge

Regularly remove:

- superseded documents;
- duplicates;
- unauthorized files;
- irrelevant material;
- drafts that should not be treated as approved; and
- sources without clear dates or ownership.

### 7. Disable unused tools and connectors

Tool definitions and results can consume substantial context. Enable only the tools required for the current task.

### 8. Separate evidence from discussion

Use a source ledger or evidence table so that authoritative material does not disappear inside conversational prose.

## Source and decision ledgers

Long-running work benefits from two compact artifacts.

### Source ledger

| Source | Authority | Version or date | Scope | Status |
|---|---|---|---|---|
| Public policy | Primary | YYYY-MM-DD | Governing requirement | Current |
| Internal procedure | Approved | v2.1 | Implementation | Current |
| Draft memo | Informational | Draft | Background only | Not authoritative |

### Decision ledger

| Decision | Rationale | Evidence | Owner | Date | Revisit trigger |
|---|---|---|---|---|---|
| Use option B | Meets constraints | Sources 1 and 2 | Reviewer | YYYY-MM-DD | New requirement |

These ledgers make restart and summary transitions more reliable.

## Memory management within context management

Memory supports continuity, but stale Memory can repeatedly contaminate otherwise clean conversations.

For active users, the course recommends reviewing Memory at least monthly.

During review:

1. list stored entries;
2. confirm accuracy;
3. verify scope;
4. update changed facts;
5. remove expired entries;
6. move Project-specific material into the relevant Project;
7. remove sensitive or unauthorized information;
8. verify that remembered facts do not replace authoritative evidence; and
9. record a next-review date when governance requires it.

The goal is not maximum Memory volume.

> The accuracy and relevance of stored Memory matter more than the amount stored.

## Context length versus usage limits

Claude has two different resource constraints.

### Length or context limit

A length limit controls how much information can be active in one conversation or request.

It is affected by:

- model context-window size;
- conversation history;
- files and images;
- tool definitions and results;
- extended thinking;
- Project instructions and retrieved knowledge; and
- output reservation.

### Usage limit

A usage limit controls how much Claude can be used over time across conversations and product surfaces.

It is affected by:

- plan;
- message length;
- file size;
- current conversation length;
- model choice;
- effort level;
- tools such as Research or web search;
- Artifact creation; and
- overall capacity policies.

```text
Context limit = depth of one conversation
Usage limit   = quantity of use over time
```

Hitting one does not necessarily mean hitting the other.

## Current usage behavior, dated July 14, 2026

Anthropic's current Help Center states that paid plan users can view:

- a rolling five-hour session budget;
- weekly limits for Opus; and
- a separate weekly pool for all other models.

The exact allowances vary by plan, model, feature, effort level, message length, attachment size, current capacity, and product changes.

Usage across Claude product surfaces can count toward the same allowance. Usage-based Enterprise plans may instead be billed by consumption rather than operate under the same fixed progress bars.

> [!NOTE]
> Memorize the planning principle, not a permanent number. Check **Settings > Usage** and the current Help Center before relying on plan-specific limits.

## Usage-aware work planning

For intensive work:

1. inspect current session and weekly usage before starting;
2. define the deliverable and acceptance criteria upfront;
3. choose the minimum qualified model;
4. disable unnecessary tools and high effort;
5. place reusable files in a Project;
6. divide the work into coherent stages;
7. create an interim deliverable after each stage;
8. record decisions and open questions;
9. generate a handoff before the session becomes constrained; and
10. restart from the approved handoff rather than extending one thread indefinitely.

### Example segmentation

```text
Session 1: Source collection and scope
Session 2: Analysis and decision ledger
Session 3: Draft deliverable
Session 4: Verification and revision
Session 5: Final approval
```

Each session begins from Project context plus the latest approved state capsule.

## Projects and context efficiency

Projects improve context and usage efficiency in several ways:

- durable instructions do not need to be retyped;
- reusable documents can be cached;
- retrieval can load relevant Project content rather than every document at once;
- separate conversations can isolate tasks; and
- Project summaries and Memory can support continuity.

Projects do not remove the need to:

- curate documents;
- keep instructions concise;
- label versions;
- record cross-thread decisions;
- restart degraded conversations; or
- verify that retrieved evidence is current and authoritative.

## Context management for API and agent workflows

In API workflows, the surrounding application controls what history is sent back to the model.

The application must decide:

- which turns remain relevant;
- what to summarize;
- what to redact;
- which tool results can be removed;
- how to track token usage;
- when to use server-side compaction;
- when to clear old tool or thinking blocks;
- what state belongs in a durable store; and
- how a new session reconstructs authorized state.

Current Anthropic API documentation provides server-side compaction for supported models and context-editing controls for specialized workflows. These product details are version-sensitive, but the durable design principle is stable:

> The application should reconstruct the smallest authoritative context required for the next action.

## Security and integrity considerations

Context is an attack surface as well as a resource budget.

### Prompt injection persistence

Untrusted documents, websites, tool results, and emails may contain instructions that should not become durable context.

Do not automatically move untrusted content into:

- Project standing instructions;
- Project knowledge;
- Memory;
- Skills; or
- state summaries.

Require source review and explicit authorization.

### Summary poisoning

A malicious or incorrect statement can become harder to detect after it is compressed into a trusted-looking summary.

Control this by:

- labeling source provenance;
- separating facts from instructions;
- validating summaries;
- retaining links to original evidence;
- recording unresolved conflicts; and
- requiring review before persistence.

### Cross-workstream leakage

Do not combine unrelated confidential workstreams in one thread or one Project. Keep context within the smallest authorized scope.

### Data minimization

A large context window is not permission to upload more data. Include only the information necessary and authorized for the task.

## Common mistakes

### Extending one conversation indefinitely

Automatic context management helps continuity but does not make an endlessly growing thread the best architecture.

### Treating the transcript as the source of truth

Important decisions and current facts should live in controlled records, not only in chat history.

### Summarizing without validation

A handoff can omit constraints or convert uncertainty into certainty.

### Persisting everything

Excess persistence creates staleness, privacy, and contamination risks.

### Starting over without a handoff

A clean conversation is useful only if the required state is preserved deliberately.

### Mixing unrelated tasks

Context from one task can distract or contaminate another.

### Ignoring usage limits

A technically valid long session can still exhaust the user's rolling or weekly budget.

### Assuming a larger model solves context problems

A stronger model does not repair stale, conflicting, unauthorized, or irrelevant context.

## Worked examples

### Example 1: Instruction drift

A writer gave detailed style rules at the start of a long session. Later responses repeatedly ignore two negative constraints.

**Action:** Create a state capsule, validate the constraints, restart the drafting thread, and persist truly durable style rules in Project instructions or Memory as appropriate.

### Example 2: New task in the same Project

A research conversation is complete, and the user is ready to draft the final deliverable.

**Action:** Open a new Project conversation for drafting, using the approved source and decision ledgers rather than the entire exploratory thread.

### Example 3: Temporary detail

A current incident status changes hourly.

**Action:** Keep it in the current conversation and authoritative incident system. Do not persist it in general Memory.

### Example 4: Reused reference set

A recurring analysis uses the same approved public standards every month.

**Action:** Place current versions in Project knowledge, label authority and date, and remove superseded versions.

### Example 5: Usage budget risk

A user plans a long Opus session with many attachments, Research, and high effort while near the weekly limit.

**Action:** Segment the workflow, use the minimum qualified model at each stage, disable unnecessary features, save interim state, and monitor Settings > Usage.

## Hands-on lab

### Objective

Practice detecting context degradation and transferring work safely into a clean session.

### Exercise 1: Context-health audit

Review a long conversation and identify:

- repeated information;
- stale assumptions;
- conflicting instructions;
- unrelated tasks;
- tool results that no longer matter;
- decisions that should be persisted; and
- symptoms of degraded recall.

### Exercise 2: Create a state capsule

Produce a handoff using the state-capsule structure. Compare it against the source conversation and document omissions.

### Exercise 3: Classify persistence

For each item, select:

- current conversation;
- Project instructions;
- Project knowledge;
- Memory;
- Skill;
- external source of record; or
- do not retain.

### Exercise 4: Usage-aware plan

Design a four-session plan for a large analytical deliverable. Specify model, tools, outputs, checkpoints, and handoffs for each session.

### Acceptance criteria

The lab is complete when:

- the new conversation can resume without reading the old transcript;
- accepted decisions and constraints are preserved;
- assumptions remain labeled;
- authoritative sources remain traceable;
- temporary and sensitive details are not over-persisted;
- the plan accounts for usage limits; and
- an accountable reviewer can audit the transition.

## Knowledge check

### Question 1

Claude stops following an instruction that appeared near the start of a very long conversation. What is the best first response?

A. Upgrade every request to the highest model tier.

B. Continue correcting Claude inside the same thread indefinitely.

C. Diagnose whether context has degraded, create a validated state summary, and restart if necessary.

D. Store the entire transcript in Memory.

**Answer:** C.

### Question 2

Which item is the best candidate for persistence in Project knowledge?

A. A temporary deadline for today's task.

B. The current approved version of a standard used repeatedly by the workstream.

C. An unverified claim copied from a webpage.

D. A password required by a connector.

**Answer:** B.

### Question 3

What is the main difference between a usage limit and a context-length limit?

A. Usage limits apply only to free plans.

B. Usage limits control quantity over time; context limits control the depth of an individual conversation.

C. Context limits apply only to uploaded documents.

D. There is no meaningful difference.

**Answer:** B.

### Question 4

What should a handoff summary preserve?

A. Only the latest response.

B. Every sentence verbatim.

C. Decisions, constraints, sources, assumptions, open questions, work state, and next actions.

D. Only information Claude believes is important.

**Answer:** C.

### Question 5

A user reaches a clean task boundary inside a Project. What is usually appropriate?

A. Continue the same thread because the Project requires one conversation.

B. Start a focused new Project conversation and provide the required state handoff.

C. Delete the Project knowledge base.

D. Save the entire transcript as a Skill.

**Answer:** B.

### Question 6

Automatic context management means:

A. all details remain equally prominent forever;

B. Code Execution calculates the context window;

C. earlier material may be summarized so a long conversation can continue;

D. usage limits no longer apply.

**Answer:** C.

## Flashcards

**Q:** What is a context window?

**A:** The finite working set of instructions, conversation history, files, tool information, retrieved evidence, and generated output that Claude can reference for a response.

---

**Q:** Why is more context not automatically better?

**A:** Irrelevant, duplicated, stale, or conflicting content can reduce recall and focus even before the hard limit is reached.

---

**Q:** What are the three responses to context degradation?

**A:** Restart, summarize, and persist.

---

**Q:** When should you restart?

**A:** When the task changes, the thread drifts, corrections accumulate, context becomes unreliable, or a clean boundary improves focus and auditability.

---

**Q:** What should a state capsule contain?

**A:** Objective, scope, decisions, sources, constraints, definitions, completed work, open questions, risks, next actions, and approval requirements.

---

**Q:** What does persist mean?

**A:** Move durable information into the correct long-lived layer, such as Project instructions, Project knowledge, Memory, a Skill, or an external record.

---

**Q:** What is the difference between context limits and usage limits?

**A:** Context limits control how much one conversation can actively contain; usage limits control how much Claude can be used over time.

---

**Q:** Does automatic summarization eliminate the need for context management?

**A:** No. Critical details can lose prominence or precision, so explicit checkpoints, summaries, and clean restarts remain useful.

---

**Q:** Why validate a handoff summary?

**A:** Compression can omit constraints, misstate decisions, or turn assumptions into apparent facts.

---

**Q:** What is the best Memory strategy?

**A:** Keep the smallest accurate, recurring, authorized set and review it regularly.

---

**Q:** How can Projects improve usage efficiency?

**A:** Reusable documents can be cached and retrieved as needed instead of being re-uploaded and fully reprocessed in every session.

---

**Q:** What is the central context-engineering rule?

**A:** Reconstruct the smallest authoritative context required for the next action.

## Certification lens

The exam is likely to test whether you recognize the correct intervention for a long or drifting session.

Use this reasoning:

```text
Session drifted beyond recovery? -> Restart
State must move to a new thread? -> Summarize
Information should survive future sessions? -> Persist
```

Also remember:

- automatic context management does not make context unlimited;
- Memory should be curated, not accumulated;
- Projects carry durable context, but threads remain distinct;
- context limits and usage limits are separate; and
- planning and checkpointing are more reliable than extending one session indefinitely.

## Engineering perspective

Context management is state architecture.

A mature workflow does not ask the model to remember everything. It defines:

- which state is active;
- which state is durable;
- which source is authoritative;
- which information is temporary;
- which data is authorized;
- how state is summarized;
- how state is validated;
- when a session ends; and
- how the next session recovers.

```text
Authoritative sources
        |
        v
Curated active context
        |
        v
Model work
        |
        v
Validated decisions and artifacts
        |
        +-- Persist durable state
        +-- Discard temporary state
        +-- Create next-session handoff
```

## Key takeaways

- Context is finite and quality can degrade before the hard limit.
- Automatic summarization extends long paid-plan chats when Code Execution is enabled, but critical state still requires explicit management.
- Restart at clean task boundaries or when drift becomes costly.
- Summarize operational state, then validate the summary.
- Persist only durable, authorized information in the correct layer.
- Keep Projects, Memory, tools, documents, and conversations curated.
- Distinguish context-length limits from rolling and weekly usage limits.
- Plan intensive work as stages with interim artifacts and handoffs.
- Treat summaries and persistent state as security- and integrity-sensitive artifacts.
- The best context is the smallest authoritative context needed for the next action.

## Related material

- [How Claude Behaves](02-how-claude-behaves.md)
- [Core Entry Points](03-core-entry-points.md)
- [Capability Layer, Memory](04a-capability-layer-memory.md)
- [Choosing Models](05-choosing-models.md)
- [Context Management prompts](../../../prompts/module-01/06-context-management-prompts.md)
- [Context Management patterns](../../../patterns/context-management-patterns.md)

## Official reading

Product behavior, context-window sizes, and plan limits change. Verify current documentation before relying on specific numbers.

- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- [Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)

## Version-awareness note

Context-window sizes, automatic context management, Code Execution dependencies, Project retrieval, Memory behavior, chat search, session windows, weekly pools, usage credits, effort controls, and Enterprise billing can change. Treat the current Claude Help Center, Platform documentation, product settings, and organization policy as authoritative.