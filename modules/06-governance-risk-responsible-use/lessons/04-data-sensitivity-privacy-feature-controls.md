# Lesson 4: Data Sensitivity, Privacy & Feature Controls

## Overview

Before data enters a chat, Project, connector, Memory, Skill, or code-execution workflow, classify it.

```text
Classify data
      ↓
Determine whether processing is allowed
      ↓
Minimize or redact when possible
      ↓
Choose the correct feature and persistence controls
      ↓
Review, monitor, delete, or escalate
```

> Feature controls do not make disallowed data safe. Permission to process the data comes first.

---

# Plain-English explanation

A useful feature can still be the wrong place for a particular dataset.

Incognito can keep a conversation out of ordinary chat history and Memory. A sandbox can isolate code execution. Memory controls can reduce persistence. None of those controls proves that regulated, confidential, or third-party data is permitted in the selected environment.

```text
Feature control applied
      ≠
Data approved for processing
```

---

# One analogy: airport security lanes

A different security lane may change how a bag is handled, but it does not change what items are legally allowed through the airport.

- **Data classification** determines whether the item may enter.
- **Redaction and minimization** reduce what must enter.
- **Feature controls** determine how the approved material is processed or retained.
- **Organizational policy** decides which lane and environment are authorized.

---

# Classify before upload

A practical three-tier model supports rapid decisions.

## Green — Safe to use

Typical examples:

- published material;
- anonymized or aggregated data;
- synthetic examples;
- internal material already cleared for broad sharing; and
- low-sensitivity reference content.

Green data still requires task relevance and source verification, but it usually does not require special privacy controls.

## Yellow — Review first

Typical examples:

- internal documents not intended for broad distribution;
- names, contact information, or employee details;
- confidential business drafts;
- unreleased product or transaction information;
- customer records with identifiers; and
- third-party information with unclear handling terms.

Yellow means pause long enough to confirm policy, environment, access, retention, and the minimum data required.

## Red — Keep out unless an approved path exists

Typical examples:

- regulated health, financial, government, or controlled data;
- credentials, keys, tokens, and secrets;
- legally privileged or contractually restricted material;
- protected personal data requiring an approved environment;
- export-controlled or similarly restricted information; and
- third-party confidential information whose processing has not been authorized.

```text
Uncertain classification
      ↓
Use the more sensitive tier
      ↓
Seek authorized clarification
```

---

# Necessity and minimization

Before applying a feature control, ask:

```text
Does the task need this data at all?
```

Possible reductions include:

- remove unused columns;
- use counts instead of raw records;
- replace names with stable pseudonyms;
- aggregate small groups where appropriate;
- truncate unnecessary dates or locations;
- omit credentials and secrets entirely;
- separate confidential context from the analytical dataset; and
- use synthetic or representative examples.

```text
Available data
      ≠
Necessary data
```

---

# Redaction and anonymization

Redaction is appropriate when sensitive identifiers are not required for the task.

Example:

```text
Original:
Jamie Rivera, account 483921, purchased Product X on 2026-06-14.

Minimized:
Customer 17 purchased Product X during the reporting period.
```

## Failure mode 1: Partial redaction

Removing a name may not prevent identification when other fields remain, such as:

- account numbers;
- email addresses;
- rare job titles;
- exact dates;
- precise locations;
- small-population attributes; or
- unique combinations of otherwise ordinary fields.

```text
Name removed
      ≠
Person de-identified
```

## Failure mode 2: Redaction breaks the task

If the task depends on the sensitive identifiers, stripping them may invalidate the analysis.

The correct response is not superficial redaction. Confirm an approved processing path or keep the data out.

> Redaction works when sensitivity and analytical necessity do not overlap.

---

# Feature-specific controls

## Code-execution sandbox

Current Claude guidance describes code execution and file creation as operating in a sandboxed computing environment. Uploaded files used for analysis may be processed through that environment.

Before running code:

- inspect the file;
- remove unnecessary sensitive fields;
- verify the approved environment;
- review network and package behavior where relevant;
- avoid secrets in files or prompts;
- check generated outputs for copied sensitive content; and
- delete or retain artifacts according to policy.

```text
Sandboxed
      ≠
Approved for every data class
```

## Memory persistence

Memory can preserve useful context across future work, but persistence may be inappropriate for sensitive information.

Review:

- whether the information should be retained;
- whether an authoritative source belongs elsewhere;
- whether the entry can become stale;
- who can view or export it;
- whether organizational retention applies; and
- how to edit, delete, pause, or reset it.

```text
Useful to remember
      ≠
Appropriate to persist
```

## Incognito chats

Current Claude guidance describes Incognito chats as temporary conversations that are not saved to ordinary chat history or Memory.

For Team and Enterprise accounts, Incognito chats still follow organizational retention rules and can be included in organizational data exports.

```text
Not in chat history or Memory
      ≠
Not retained by the organization
```

Incognito can be useful when approved Yellow data should not enter ordinary history or Memory. It does not authorize Red data.

## Organization and plan controls

Feature availability, Memory controls, retention, exports, role-based permissions, and administrator capabilities can differ by plan and organizational configuration.

Before processing sensitive information, confirm:

- which account and organization are active;
- the plan and approved configuration;
- who controls Memory and retention;
- whether data exports or compliance access apply;
- whether the feature is enabled for the organization;
- whether the environment is approved for the data class; and
- which owner or administrator can clarify the boundary.

Do not rely on a remembered plan distinction when current organizational settings can be checked.

---

# Persistence and processing are separate controls

```text
Question 1:
May this data be processed here?

Question 2:
If yes, how may it be retained, remembered, exported, or deleted?
```

Answer Question 1 before Question 2.

This prevents the common mistake:

```text
Incognito enabled
      ↓
Assume regulated data is safe
```

The correct sequence is:

```text
Classify data
      ↓
Confirm approved environment
      ↓
Minimize data
      ↓
Select persistence and feature controls
```

---

# Worked examples

## 1. Anonymized survey trends

**Classification:** Green

- no direct identifiers;
- aggregated analysis;
- code execution appropriate for verified counts;
- confirm small groups do not permit re-identification.

## 2. Confidential acquisition draft

**Classification:** Yellow pending policy review

- confidential and not publicly announced;
- confirm that the selected account, Project, and entry point are approved;
- minimize unnecessary deal details;
- use Incognito only if processing is permitted and ordinary history or Memory should be avoided;
- organizational retention still applies.

## 3. Customer spreadsheet with personal identifiers

**Classification:** Yellow or Red depending on policy and data class

- remove names, contact details, account numbers, and unnecessary dates when the task permits;
- test for indirect identification;
- if identifiers are necessary, use only an approved processing path;
- otherwise stop and escalate.

## 4. Patient records

**Classification:** Red unless an approved compliant environment and workflow are confirmed

```text
First question:
Is this environment approved for protected health information?

Not:
Should I turn on Incognito?
```

If the organization has not confirmed the approved path, do not upload the records.

---

# Common failure modes

| Failure | Why it fails | Repair |
|---|---|---|
| Upload first, classify later | Sensitive data may already be exposed | Classify before entry |
| Incognito treated as compliance | It changes history and Memory, not authorization | Confirm approved environment first |
| Name-only redaction | Indirect identifiers remain | Review all identifying fields and combinations |
| Redaction destroys analytical validity | Required context is removed | Use an approved environment or redesign the task |
| Sandbox treated as permission | Isolation does not establish policy approval | Verify data class and environment |
| Memory used for sensitive authoritative records | Persistence, staleness, and export risks remain | Use approved systems of record and minimize Memory |
| Green/Yellow/Red treated as universal law | Organizational classifications may differ | Map the quick tiers to current policy |

---

# Data and feature-control protocol

```text
1. Define the task and minimum required data
2. Identify the data owner and affected people
3. Classify the data under current organizational policy
4. When uncertain, use the more sensitive category
5. Check legal, contractual, regulatory, and third-party restrictions
6. Confirm the approved account, environment, and entry point
7. Minimize, redact, anonymize, aggregate, or synthesize where valid
8. Select feature controls for execution, Memory, history, access, retention, and export
9. Test redaction for re-identification and analytical validity
10. Define review, deletion, revocation, incident, and escalation paths
11. Record the decision and approval
12. Stop when no approved path exists
```

---

# Exam lens

```text
Published or approved public data       → usually Green
Confidential internal draft             → Yellow; review first
Regulated data or credentials           → Red without approved path
Incognito                               → history and Memory control, not permission
Sandbox                                 → execution isolation, not data authorization
Name removed but unique details remain  → incomplete redaction
Sensitive identifiers unnecessary       → minimize or redact
Sensitive identifiers required          → approved environment or stop
Unsure between tiers                    → choose the more sensitive tier
```

For data-sensitivity scenarios:

1. classify before upload;
2. identify the minimum necessary data;
3. map the quick tier to current policy;
4. separate processing approval from persistence controls;
5. distinguish direct and indirect identifiers;
6. test whether redaction preserves task validity;
7. use Incognito only within an approved processing boundary;
8. understand sandbox and Memory limitations;
9. verify plan and organization settings; and
10. escalate when an approved path is not established.

---

# Short recap

```text
1. Classify before data enters a feature.
2. Green, Yellow, and Red support rapid screening.
3. Uncertainty moves data to the more sensitive tier.
4. Minimize before relying on controls.
5. Redaction must remove indirect identifiers too.
6. Redaction is invalid when it breaks the task.
7. Sandboxing does not authorize sensitive data.
8. Incognito excludes ordinary history and Memory, not organizational retention.
9. Memory persistence and processing permission are separate.
10. Regulated data stays out until an approved path is confirmed.
```

## Educational-use notice

This lesson is an unofficial educational resource. Data classifications, privacy requirements, retention rules, regulatory obligations, and feature availability vary by organization, jurisdiction, plan, and configuration. Current policy, contract terms, qualified privacy or legal guidance, and official product documentation control real decisions.
