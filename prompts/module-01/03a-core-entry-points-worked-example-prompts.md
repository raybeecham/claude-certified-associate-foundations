# Module 1 Prompt Notebook: Core Entry Points Worked Example

These prompts support the worked comparison between repeatedly rebuilding context in Chat and creating a Project for recurring work.

Use only fictional, public, or authorized information. Do not place confidential, client-identifying, proprietary, or unauthorized data into a public example or Project.

## 1. Three-question Project test

### Use when

You need a quick decision on whether recurring work has outgrown Chat.

```text
Evaluate whether the workflow below should become a Claude Project.

Workflow:
[DESCRIBE WORKFLOW]

Answer these three questions:
1. Does the task recur?
2. Is the background context substantially the same across sessions?
3. Is the output format consistent?

For each answer, provide supporting evidence from the workflow description.

Decision rule:
- 0 yes answers: remain in Chat unless another requirement justifies persistence;
- 1 yes answer: usually remain in Chat, but identify any special considerations;
- 2 or 3 yes answers: recommend a Project unless governance, data handling, or maintenance concerns outweigh the benefit.

Return:
- result for each question;
- recommendation;
- rationale;
- information that should persist;
- information that should remain session-specific; and
- risks or conditions that could change the recommendation.
```

## 2. Setup-tax calculator

### Use when

You want to quantify time lost to repeated context loading.

```text
Analyze the recurring setup tax in this workflow.

Workflow frequency:
[FREQUENCY]

Repeated setup activities and time:
[LIST EACH ACTIVITY AND MINUTES]

Estimated Project setup time:
[MINUTES]

For each recurring setup activity, classify it as:
- durable Project instruction;
- reusable Project knowledge;
- current-session input;
- unnecessary duplication;
- sensitive or unauthorized information that should not persist; or
- requires human decision.

Calculate:
1. total repeated setup time per session;
2. projected time saved per session after Project setup;
3. break-even number of sessions;
4. projected time saved after 4, 12, and 26 sessions; and
5. maintenance effort that should be subtracted from gross savings.

State all assumptions and do not invent missing numbers.
```

## 3. Chat-to-Project migration planner

### Use when

A recurring Chat workflow should be reorganized into a durable workspace.

```text
Create a migration plan from repeated standalone Chats to a Claude Project.

Current workflow:
[DESCRIBE CURRENT WORKFLOW]

Repeated background:
[BACKGROUND]

Repeated files or sources:
[SOURCES]

Repeated output requirements:
[OUTPUT REQUIREMENTS]

Current-session inputs:
[VARIABLE INPUTS]

Produce:
1. proposed Project purpose;
2. draft standing instructions;
3. curated knowledge-base inventory;
4. information that must remain conversation-specific;
5. information that should not be uploaded or retained;
6. proposed conversation structure;
7. first-session checklist;
8. maintenance and refresh schedule;
9. review controls; and
10. measurable success criteria.

Keep durable configuration separate from temporary status information.
```

## 4. Durable versus temporary context sorter

### Use when

You need to decide where each piece of information belongs.

```text
Classify the following information for a recurring Claude workflow.

Items:
[LIST ITEMS]

Use these destinations:
- Project standing instructions;
- Project knowledge base;
- current conversation only;
- external system of record;
- archive or remove;
- do not upload;
- owner review required.

For each item, explain:
- why it belongs there;
- expected lifetime;
- owner;
- refresh trigger;
- sensitivity;
- conflict risk; and
- what happens if it becomes stale.

Then identify any missing durable context required for the workflow.
```

## 5. Weekly status-report intake

### Use when

A Project is already configured and only current updates should be supplied.

```text
Using the Project's standing instructions and approved knowledge, prepare the current status report from the updates below.

Reporting period:
[DATE RANGE]

Current updates:
[UPDATES]

Before drafting:
1. separate completed work, active work, risks, blockers, decisions needed, and changed dates;
2. identify missing or contradictory information;
3. determine which prior open items remain active based only on available evidence; and
4. flag any Project knowledge that appears stale.

Draft the report using the standing format.

Do not:
- invent status;
- carry forward an issue without current support;
- silently resolve a contradiction;
- treat old Project knowledge as current when the updates supersede it; or
- expose sensitive information outside the approved audience.

End with a validation checklist.
```

## 6. Project break-even review

### Use when

You want to determine whether a newly created Project is actually delivering value.

```text
Evaluate whether this Claude Project has reached its intended break-even point.

Original setup effort:
[HOURS OR MINUTES]

Number of sessions completed:
[COUNT]

Baseline time per session before the Project:
[MINUTES]

Current time per session:
[MINUTES]

Maintenance effort to date:
[MINUTES]

Quality and review observations:
[OBSERVATIONS]

Calculate:
- gross time saved;
- maintenance-adjusted time saved;
- whether setup cost has been recovered;
- projected annual savings at the current cadence; and
- whether quality, continuity, or governance improved, declined, or stayed constant.

Recommend:
- continue as designed;
- revise instructions;
- refresh knowledge;
- split the Project;
- return the workflow to Chat; or
- retire the Project.

State assumptions and distinguish measured results from estimates.
```

## 7. Repeated-setup audit

### Use when

A team suspects that it is recreating the same context across Claude sessions.

```text
Audit the workflow below for repeated setup.

Workflow description:
[DESCRIPTION]

Identify every repeated action involving:
- background explanation;
- file upload;
- terminology correction;
- stakeholder description;
- role definition;
- output structure;
- policy reminder;
- prior-decision reconstruction; and
- formatting correction.

For each action, estimate:
- frequency;
- time cost;
- error or drift risk;
- whether persistence is appropriate; and
- the best corrective action.

Return a prioritized setup-tax reduction plan.
```

## Suggested study exercise

Apply prompts 1 and 2 to the project-coordinator scenario in the worked example. Then change one assumption at a time:

- the report happens only once;
- the background changes every week;
- the output format is different each session;
- the source data is too sensitive to persist;
- three team members collaborate in the Project; or
- maintaining the Project takes ten minutes every week.

Explain how each change affects the recommendation.

## Related material

- [Core Entry Points worked example](../../modules/01-platform-model-foundations/lessons/03a-core-entry-points-worked-example.md)
- [Core Entry Points lesson](../../modules/01-platform-model-foundations/lessons/03-core-entry-points.md)
- [Core Entry Points prompt notebook](03-core-entry-points-prompts.md)
