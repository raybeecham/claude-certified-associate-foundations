# Core Entry Points: Worked Comparison

## Overview

This worked example demonstrates why entry-point selection affects efficiency even when the final output quality remains unchanged.

The central lesson is simple:

> Repeated context-loading is a workflow-design problem, not a prompting problem.

A user may receive a good result from Chat every time and still be using the wrong entry point. When the same task recurs with stable background information and a consistent output structure, a Project can remove the recurring setup burden.

## Scenario

A project coordinator prepares a team status report every Monday.

The report requires the same foundational information each week:

- project purpose;
- team structure;
- stakeholder roles;
- report format;
- escalation thresholds; and
- unresolved items carried forward from the previous reporting period.

Only the current week's updates change substantially.

## Wrong entry point: rebuilding context in Chat

Each Monday, the coordinator opens a new Chat and reconstructs the same operating context.

```text
New Chat
   |
   +-- Re-enter project background
   +-- Re-enter team structure
   +-- Re-enter stakeholder list
   +-- Re-enter report format
   +-- Re-enter escalation rules
   +-- Re-enter prior open items
   +-- Add current weekly updates
   +-- Generate report
```

Claude produces a useful report, but the workflow includes a recurring setup tax.

### Example timing

| Activity | Approximate time |
|---|---:|
| Reconstruct background and instructions | 12 minutes |
| Add weekly updates and clarify issues | 18 minutes |
| Review and revise report | 10 minutes |
| **Total** | **40 minutes** |

The problem is not poor prompting. The problem is that durable information is being treated as temporary conversation input.

### Why the workflow is inefficient

The coordinator repeatedly performs work that could have been persisted:

- stable context is rewritten;
- the same files may be uploaded again;
- formatting rules are restated;
- terminology can drift between weeks;
- prior decisions are reconstructed manually; and
- time is spent proving the same context to Claude before useful work begins.

The output can still be correct, but the process is unnecessarily expensive.

## Right entry point: persist stable context in a Project

The coordinator creates a Project and separates durable information from weekly inputs.

### Project knowledge base

The knowledge base contains reusable reference material:

- project background;
- team structure;
- stakeholder directory;
- approved terminology;
- reporting calendar; and
- any stable reference documents authorized for reuse.

### Project standing instructions

The Project instructions define the recurring procedure:

- required report sections;
- tone and intended audience;
- escalation thresholds;
- issue-priority definitions;
- evidence and uncertainty rules;
- formatting requirements; and
- review expectations.

### Weekly conversation input

Each Monday, the coordinator supplies only what changed:

- completed work;
- current status;
- new risks;
- blocked items;
- decisions needed;
- changed deadlines; and
- updates to prior open items.

```text
Project
   |
   +-- Persistent knowledge
   |      +-- Background
   |      +-- Team and stakeholders
   |      +-- Stable references
   |
   +-- Standing instructions
   |      +-- Report structure
   |      +-- Escalation thresholds
   |      +-- Tone and review rules
   |
   +-- Weekly conversation
          +-- Current updates
          +-- Changed risks
          +-- New decisions
          +-- Generate report
```

### Example timing after setup

| Activity | Approximate time |
|---|---:|
| Add weekly updates | 10 minutes |
| Clarify current issues | 5 minutes |
| Review and revise report | 10 minutes |
| **Total** | **25 minutes** |

The report quality may remain comparable. The improvement is operational: the entry-point choice removes approximately 15 minutes of avoidable work each week.

## The weekly setup tax

A setup tax is time repeatedly spent reconstructing information that is stable enough to persist.

It commonly appears as:

- repeated background paragraphs;
- repeated file uploads;
- repeated output-format instructions;
- repeated corrections to terminology;
- repeated explanation of stakeholder roles;
- repeated policy or process reminders; and
- repeated searches for prior decisions.

A setup tax is a signal that the workflow may have outgrown Chat.

## The three-question Project test

Ask:

1. **Does the task recur?**
2. **Is the background context substantially the same across sessions?**
3. **Is the output format consistent?**

If the answer is **yes to two or more**, creating a Project is usually justified.

| Recurs | Stable context | Consistent format | Initial recommendation |
|---|---|---|---|
| No | No | No | Remain in Chat |
| Yes | No | No | Usually Chat, unless coordination needs justify a Project |
| No | Yes | Yes | Consider a Project if the task will be revisited or shared |
| Yes | Yes | No | Build a Project for persistent context |
| Yes | No | Yes | Consider a Project for reusable procedure and templates |
| No | Yes | No | Chat may be sufficient for a one-time task |
| Yes | Yes | Yes | Strong Project candidate |

This is a heuristic, not an absolute rule. Data sensitivity, collaboration, governance, maintenance burden, and feature availability can change the answer.

## Break-even reasoning

A Project has an initial setup cost. The decision becomes worthwhile when recurring savings exceed that cost.

### Simple model

```text
Break-even sessions = Project setup time / Time saved per session
```

Example:

```text
Project setup time: 30 minutes
Time saved each week: 15 minutes
Break-even point: 2 sessions
```

After the second recurring session, the setup investment has been recovered. Every later session produces net time savings, assuming the Project remains maintained and useful.

## What belongs where

A useful Project separates durable, reusable information from volatile weekly input.

| Information | Best location | Reason |
|---|---|---|
| Project purpose | Project instructions or knowledge | Stable across sessions |
| Team structure | Project knowledge | Reused regularly |
| Stakeholder list | Project knowledge | Reused regularly, subject to maintenance |
| Report format | Project instructions | Defines recurring output behavior |
| Escalation thresholds | Project instructions | Durable procedure |
| This week's updates | Current conversation | Changes each session |
| Temporary draft comments | Current conversation | Not durable policy |
| Sensitive data without authorization | Do not upload | Access and data-handling control |
| Superseded reference document | Remove or archive | Prevent stale guidance |

## Worked prompt: weekly report inside the Project

```text
Using the Project instructions and approved Project knowledge, prepare this week's status report from the updates below.

Weekly updates:
[PASTE CURRENT UPDATES]

Requirements:
- follow the standing report structure;
- carry forward unresolved items only when still supported by current information;
- apply the documented escalation thresholds;
- distinguish facts, risks, assumptions, and decisions needed;
- flag missing information instead of inventing it; and
- identify any Project knowledge that appears stale or inconsistent with this week's updates.

Before finalizing, verify that every required section is present.
```

## Worked prompt: migrate a recurring Chat into a Project

```text
Analyze the recurring workflow described below and produce a migration plan from repeated Chat setup to a maintained Project.

Current workflow:
[DESCRIBE THE RECURRING CHAT WORKFLOW]

Identify:
1. stable background that belongs in Project knowledge;
2. durable procedure that belongs in standing instructions;
3. information that should remain session-specific;
4. data that should not be persisted;
5. recurring setup steps that can be eliminated;
6. Project maintenance responsibilities;
7. estimated setup effort;
8. estimated time saved per session; and
9. estimated break-even point.

Return a proposed Project structure and a first-session checklist.
```

## Common mistakes

### Mistake 1: Uploading everything into Project knowledge

Persistence is not a reason to store every file. Curate the knowledge base and remove stale, duplicative, irrelevant, or unauthorized material.

### Mistake 2: Putting weekly updates into standing instructions

Standing instructions should describe durable behavior. Temporary status belongs in the current conversation or an appropriately managed record.

### Mistake 3: Assuming all Project conversations share full thread history

Project conversations share the Project's instructions and knowledge base, but a decision made only in one conversation should be persisted deliberately if another conversation needs it.

### Mistake 4: Treating setup savings as proof of output quality

The worked example improves efficiency. The report still requires review for completeness, factual grounding, appropriate escalation, and audience fit.

### Mistake 5: Never maintaining the Project

Stakeholder lists, reference documents, thresholds, and templates can become stale. Persistence creates a maintenance obligation.

## Engineering perspective

This scenario is a basic form of state and configuration separation.

```text
Durable configuration
   +
Curated reusable knowledge
   +
Current session input
   =
Repeatable workflow
```

The same design principle appears in production AI systems:

- configuration is versioned;
- reusable knowledge is curated;
- current input remains request-specific;
- outputs are validated; and
- stale state is refreshed or retired.

The goal is not merely to save keystrokes. It is to place each type of information in the correct lifecycle.

## Certification lens

For a scenario involving repeated setup, look for these signals:

- the task happens regularly;
- the same background is repeatedly supplied;
- the same documents are reused;
- the same output structure is requested;
- the user spends meaningful time reconstructing context; or
- multiple conversations need the same stable operating rules.

These signals favor a Project over repeatedly starting a new Chat.

The expected reasoning is not that Projects inherently produce better prose. The key benefit in this example is persistence and efficiency.

## Knowledge check

### Question 1

A coordinator spends ten minutes every week re-entering the same team structure and report format before adding new updates. What is the clearest workflow problem?

A. The model is not capable enough  
B. The prompt needs more adjectives  
C. Stable context is being reconstructed as temporary Chat input  
D. Research should be enabled

**Answer:** C

### Question 2

Which item belongs most naturally in Project standing instructions?

A. This week's completed tasks  
B. The permanent report structure and escalation rules  
C. A one-time draft comment  
D. An unapproved sensitive attachment

**Answer:** B

### Question 3

True or false: Moving the workflow into a Project removes the need to review the weekly report.

**Answer:** False. The Project reduces repeated setup but does not guarantee factual accuracy, completeness, or appropriate judgment.

### Question 4

A task recurs and uses a consistent output format, but the source material changes every time. Does it satisfy the course heuristic for considering a Project?

**Answer:** Yes. Two of the three conditions are met. The Project can preserve the procedure and format while each conversation supplies current source material.

### Question 5

What is the approximate break-even point for a Project requiring 45 minutes to configure when it saves 15 minutes per recurring session?

**Answer:** Three sessions.

## Flashcards

**Q:** What three questions test whether a Project is worth building?  
**A:** Does the task recur, is the background context stable, and is the output format consistent?

**Q:** What is the course heuristic?  
**A:** If two or more of the three Project conditions are true, build or strongly consider a Project.

**Q:** What is a setup tax?  
**A:** Repeated time spent reconstructing stable context, files, instructions, terminology, or formats.

**Q:** Does moving work into a Project necessarily improve report quality?  
**A:** Not necessarily. It may preserve quality while improving efficiency and continuity.

**Q:** What belongs in Project knowledge?  
**A:** Curated, reusable background and reference material authorized for persistent use.

**Q:** What belongs in Project instructions?  
**A:** Durable process, role, format, source, escalation, and review requirements.

**Q:** What belongs in the weekly conversation?  
**A:** Current updates, changed risks, new decisions, and other session-specific information.

**Q:** Why must a Project be maintained?  
**A:** Persistent instructions and knowledge can become stale, conflicting, unnecessary, or unauthorized.

## Key takeaways

- A good result does not prove the entry point is efficient.
- Repeated context-loading is a sign that stable information may belong in a Project.
- Projects separate durable instructions and reusable knowledge from current-session updates.
- If recurrence, stable background, and consistent format are true in at least two cases, a Project is usually worth considering.
- Break-even analysis turns the entry-point decision into a measurable workflow choice.
- Persistence reduces setup effort but does not eliminate validation, review, or maintenance.

## Related material

- [Core Entry Points](03-core-entry-points.md)
- [Module Introduction](01-module-introduction.md)
- [Core Entry Points prompt notebook](../../../prompts/module-01/03-core-entry-points-prompts.md)
- [Worked comparison prompts](../../../prompts/module-01/03a-core-entry-points-worked-example-prompts.md)
