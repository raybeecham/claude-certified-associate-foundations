# Lesson 6A: Module 5 Quiz

## Result

```text
Full marks — 5 of 5
```

This public study quiz uses original fictional scenarios to test the same Module 5 competencies without reproducing proprietary course questions.

The assessed areas are:

1. selecting the correct configuration mechanism;
2. separating sensitive workstreams and continuity;
3. respecting connector capability boundaries;
4. writing precise, testable persistent instructions; and
5. diagnosing configuration drift.

---

# Question 1: Procedure or instruction?

A program-management team wants every monthly steering-committee update to follow the same eight-step preparation method, including data checks, section order, risk formatting, and a final quality checklist.

Which mechanism is the best primary home?

A. Project instructions containing the complete eight-step method  
B. A reusable Skill containing the procedure and quality checks  
C. A prior report uploaded to Project knowledge  
D. A Project Memory entry describing the last report

## Correct answer: B

A repeatable multi-step method belongs in a Skill. Project instructions can define workspace behavior, such as tone, citation rules, and review expectations. Project knowledge supplies facts and reference material. Memory preserves selected continuity.

```text
Behavior → instructions
Facts → knowledge
Procedure → Skill
Continuity → Memory
```

---

# Question 2: Separate sensitive workstreams

A research group analyzes two unrelated acquisition candidates. Each analysis uses confidential assumptions, stakeholder preferences, and evolving decisions that must not influence the other workstream.

Which setup is most appropriate?

A. One shared Project with careful wording in each chat  
B. Separate bounded Projects, each with its own approved knowledge, instructions, access, and scoped continuity  
C. One Project with a stronger model for the more sensitive candidate  
D. Disable all continuity and place both candidates in one knowledge base

## Correct answer: B

Separate bounded Projects reduce contextual mixing and allow each workstream to have its own sources, instructions, membership, and continuity. The Project boundary does not replace identity, permissions, disclosure review, or systems of record, but it is the appropriate configuration structure.

```text
Different sensitive purpose, sources, and audience
      ↓
Separate bounded Project configuration
```

---

# Question 3: Connector capability boundary

A connector can search a mailbox, read messages, and create drafts. A workflow designer expects it to send an approved response automatically, but no send tool is enabled.

What is the most accurate diagnosis?

A. The connector is defective  
B. The model tier is too weak  
C. Sending is outside the enabled capability contract; the workflow must stop at draft or use a separately authorized send action  
D. Reconnect every available mail integration

## Correct answer: C

Connector capabilities are tool- and permission-specific. Search, read, draft, approve, and send are separate stages. An unsupported action is not automatically a product defect.

```text
Connector name
      ≠
Universal connector capability
```

---

# Question 4: Instruction precision

A Project produces meeting records. Which standing instruction is most likely to create consistent, reviewable output?

A. Capture the discussion professionally  
B. Write thorough notes  
C. Record each decision as a separate bullet; list every action as `owner — due date — status`; label missing owners `owner TBD`; list unresolved questions in a final section  
D. Summarize the meeting as clearly as possible

## Correct answer: C

Option C defines observable behavior and can be interpreted consistently by two competent readers. The other options are aspirations without a testable output contract.

```text
Vague intention
      ≠
Operational instruction
```

---

# Question 5: Configuration drift

A recurring financial-performance Project begins using last year's metric labels even though users have not changed their prompts.

The current configuration contains:

- Project instruction: `Use the FY25 scorecard labels and compare results with FY25 targets.`
- Project knowledge: the approved FY26 scorecard and FY26 targets.
- Custom Skill: the current FY26 report structure.
- Memory: `The active reporting year is FY25.`

What is the correct diagnosis and repair?

A. Delete the FY26 knowledge because it conflicts with the instructions  
B. Replace the custom Skill even though it already uses FY26  
C. Update and test the stale Project instruction and Memory entry so they align with the current approved FY26 sources  
D. Move to a stronger model

## Correct answer: C

The knowledge and procedure are current. The persistent instruction and Memory entry are stale and continue to direct the output toward FY25. The repair is configuration maintenance, followed by representative regression tests.

```text
Output drift without prompt change
      ↓
Inspect instructions, knowledge, Skills, connectors, and Memory
```

---

# Five-question synthesis

| Scenario | Controlling judgment |
|---|---|
| Repeatable multi-step method | Skill |
| Distinct sensitive workstream | Separate bounded Project plus access controls |
| Unsupported connector action | Respect capability boundary |
| Vague standing rule | Replace with precise observable instruction |
| Quietly outdated output | Inspect and repair stale configuration |

## Quiz shortcut

```text
Behavior rule                  → Project instructions
Workspace facts                → Project knowledge
Reusable multi-step procedure  → Skill
Selected continuity            → scoped Memory
External access                → connector contract
Exact authority                → technical and human controls
Quiet output regression        → configuration maintenance
```

---

# Why common distractors fail

## Stronger-model distractor

Changing the model does not repair stale instructions, crossed workstream boundaries, excessive access, or unsupported connector tools.

## Prompt-more-carefully distractor

Repeatedly correcting the current chat does not repair the persistent baseline that causes the problem in every conversation.

## Connect-everything distractor

More connectors broaden access and overhead without establishing relevance, authority, or missing capabilities.

## Disable-all-continuity distractor

Eliminating continuity can avoid one risk while discarding legitimate Project value. The better design is bounded continuity plus authoritative records and access controls.

---

# Exam reasoning sequence

```text
1. Identify the configuration concern
2. Select the correct layer or component
3. Check authority, scope, precision, and capability
4. Identify what remains uncontrolled or stale
5. Choose the smallest responsible repair
6. Reject model-tier and one-time-prompt distractors
```

---

# Remediation map

| Missed concept | Review |
|---|---|
| Procedure versus behavior | Configuring Projects and Project Configuration Slot Selection Pattern |
| Workstream separation | Project charter, sharing, permissions, and Memory boundaries |
| Connector boundaries | Connector and Knowledge Boundary Pattern |
| Instruction precision | Persistent Instruction Precision Pattern |
| Configuration drift | Configuration Maintenance Lifecycle Pattern |

---

# Completion record

```text
Module 5 teaching sections: Complete
Module 5 quiz:              Full marks — 5 of 5
Key takeaways:              Open
Module complete:            Open
```

## Educational-use notice

This is an unofficial educational assessment using original fictional scenarios. It does not reproduce live certification questions or proprietary course wording. Product behavior and terminology can change; current official documentation controls.