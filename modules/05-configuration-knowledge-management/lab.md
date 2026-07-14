# Lab: Knowledge-Source Register and Retrieval Policy

## Scenario

A policy assistant has access to:

- public federal memoranda;
- organization cryptography standards;
- NIST publications;
- vendor product documentation;
- internal implementation evidence; and
- analyst notes.

Users complain about stale answers and conflicting recommendations. Some users can retrieve documents from another business unit.

## Objectives

- Establish source authority, freshness, and scope.
- Define retrieval and access policy.
- Handle conflicts.
- Select safe caching candidates.
- Test knowledge behavior.

## Tasks

### Task 1: Source register

Create at least eight entries using:

| Source ID | Owner | Authority | Version/date | Classification | Scope | Refresh | Supersedes | Citation |
|---|---|---|---|---|---|---|---|---|

### Task 2: Precedence rules

Write rules for:

- public baseline versus approved internal standard;
- older versus newer versions;
- vendor claims versus independent validation;
- analyst notes versus approved policy;
- unresolved conflict; and
- out-of-scope source.

### Task 3: Retrieval policy

Design the order of:

1. identity check;
2. authorization filter;
3. classification filter;
4. scope filter;
5. current-version filter;
6. relevance retrieval;
7. reranking;
8. context-budget selection; and
9. provenance attachment.

Explain why access filters must occur before model context construction.

### Task 4: Caching analysis

Classify each as a good, conditional, or poor caching candidate:

- stable system instructions;
- tool definitions;
- a current public standard;
- user-specific access token;
- frequently changed case evidence;
- reusable examples;
- internal source corpus; and
- current date inserted near the start of the prompt.

Include policy and invalidation requirements.

### Task 5: Test plan

Create cases for:

- stale source;
- superseded source;
- conflicting source;
- unauthorized source;
- missing owner;
- prompt injection in a vendor document;
- context overflow; and
- cache miss after a tool-definition update.

## Deliverable

Create `knowledge-governance.md` with the register, rules, retrieval policy, caching analysis, and tests.

## Acceptance criteria

- [ ] Every governing source has authority, owner, version, and scope.
- [ ] Authorization occurs before retrieval reaches Claude.
- [ ] Unresolved conflicts are surfaced.
- [ ] Secrets are excluded from prompt and cache.
- [ ] Caching applies only to stable, permitted, reusable prefixes.
- [ ] Stale or superseded content triggers a defined behavior.
- [ ] Cross-business-unit retrieval is prevented by system controls.

<details>
<summary>Model solution outline</summary>

Approved internal standards govern the organization within scope and may add obligations beyond public baselines. Public standards remain authoritative for their own claims. Vendor documents support product assertions but do not prove implementation. Analyst notes are leads, not governing evidence. Access control is enforced before retrieval. Stable instructions and tool definitions may be cache candidates, while credentials and rapidly changing case data are not.

</details>
