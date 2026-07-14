# Notes: Configuration & Knowledge Management

## 1. Configuration is a governed dependency

Reusable instructions, project guidance, tool definitions, output schemas, source-selection rules, and safety constraints determine system behavior. Treat them like code:

- version them;
- review changes;
- test them;
- document ownership;
- control access;
- stage rollout; and
- preserve rollback.

Do not let durable behavior emerge from copied ad hoc prompts that no one owns.

## 2. Establish instruction authority

A system should define which instruction source wins when guidance conflicts.

A practical hierarchy may include:

1. provider and platform controls;
2. organization policy;
3. application system configuration;
4. workflow-specific developer instructions;
5. authorized user request;
6. retrieved or uploaded content as evidence;
7. tool output as data.

The exact implementation varies, but untrusted documents should never gain authority merely by containing commands.

### Conflict behavior

Specify whether the system should:

- follow the higher-authority instruction;
- report the conflict;
- ask for clarification;
- deny the action; or
- route to a human.

Silent conflict resolution can create hidden risk.

## 3. Build a knowledge-source register

Each approved source should have metadata.

| Field | Purpose |
|---|---|
| Source ID | Stable reference |
| Title | Human-readable name |
| Owner | Accountable maintainer |
| Authority | Official, approved internal, advisory, or unverified |
| Version | Applicable revision |
| Effective date | When the source governs |
| Review date | Freshness check |
| Classification | Data handling |
| Audience/scope | Where it applies |
| Supersedes | Prior source relationship |
| Retrieval location | Controlled access path |
| Refresh cadence | Update expectation |
| Citation format | Traceability |
| Notes | Conflicts and limitations |

A file with no owner, date, or authority may still be useful, but it should not silently govern a high-stakes answer.

## 4. Retrieval is selection, not accumulation

The goal is the smallest relevant, permitted, authoritative evidence set.

Excess context can introduce:

- conflicting instructions;
- stale versions;
- irrelevant details;
- higher cost and latency;
- access violations;
- prompt injection; and
- reduced focus.

A retrieval pipeline may use:

1. identity and authorization filter;
2. scope and classification filter;
3. authority and version filter;
4. semantic or keyword retrieval;
5. reranking;
6. deduplication;
7. context-budget selection; and
8. provenance attachment.

Enforce access controls before retrieval results reach the model. Post-generation filtering is too late.

## 5. Resolve source conflicts explicitly

When sources disagree:

1. identify the exact conflict;
2. compare authority, scope, version, and effective date;
3. apply documented precedence;
4. do not merge incompatible claims into a false consensus;
5. cite both when the conflict remains unresolved;
6. state the operational consequence; and
7. route to an accountable owner when needed.

### Example

An approved internal standard may add requirements beyond a public baseline. The answer should identify which standard governs the organization rather than selecting whichever text is newer or easier to retrieve.

## 6. Freshness management

Freshness is a process, not a prompt phrase such as “use the latest.”

Controls include:

- source owners;
- scheduled review dates;
- automated ingestion checks;
- version and effective-date metadata;
- invalidation when a source is superseded;
- link and retrieval health checks;
- stale-source warnings; and
- evaluation cases for changed requirements.

For current claims, include the source date in the output when it affects interpretation.

## 7. Context budgeting

Allocate context intentionally among:

- trusted instructions;
- examples;
- current task;
- retrieved evidence;
- prior conversation;
- tool output; and
- requested generation.

Strategies:

- retrieve fewer, higher-quality passages;
- remove duplicate boilerplate;
- summarize only with validation;
- persist structured state instead of replaying all prose;
- separate stages;
- use source identifiers instead of repeated metadata; and
- reserve enough output budget.

Compaction or summarization can lose obligations or caveats. Test it.

## 8. Prompt caching

Caching can reduce repeated processing of stable prompt prefixes, improving cost or latency for eligible patterns.

Good candidates may include:

- stable system instructions;
- a long, reused reference corpus;
- tool definitions;
- consistent examples; and
- other unchanged prefixes.

Poor candidates include:

- rapidly changing user data;
- secrets;
- content that policy does not permit to be cached;
- prefixes with frequent small changes; and
- data whose invalidation requirements cannot be met.

Cache performance depends on stable ordering and prefix reuse. Measure actual cache hits and misses rather than assuming benefits.

## 9. Secrets and credentials

Never store credentials in:

- system prompts;
- examples;
- knowledge documents;
- repository files;
- logs;
- model outputs; or
- user-visible error messages.

Use a secret manager. The application should inject a credential only into the authorized service call and should expose neither the value nor broad access to the model.

Rotate credentials after suspected exposure and preserve evidence according to incident procedures.

## 10. Least privilege for knowledge and connectors

A model should only receive the sources and capabilities necessary for the current authorized task.

Controls:

- identity-aware retrieval;
- per-source access control;
- business-unit or project isolation;
- row- and field-level filters;
- tool allowlists;
- scoped service accounts;
- time-limited credentials;
- read-only access by default;
- approval for writes; and
- audit logging.

Do not rely on instructions such as “do not reveal confidential data” to enforce access. Prevent the data from entering the context.

## 11. Configuration testing

Test:

- instruction conflicts;
- missing configuration;
- malformed templates;
- unauthorized source requests;
- stale sources;
- source supersession;
- excessive context;
- cache invalidation;
- secret patterns;
- prompt injection inside documents;
- cross-tenant isolation; and
- output citation provenance.

Record configuration and source versions with each evaluation run.

## 12. Common mistakes

| Mistake | Better approach |
|---|---|
| Put all documents in context | Retrieve the smallest relevant authoritative set |
| “Latest” with no source process | Track source version and freshness |
| Secret in system prompt | Use a secret manager and application boundary |
| Conflicting sources silently merged | Apply authority rules and surface unresolved conflict |
| Access filter after generation | Enforce before retrieval |
| Cache every long prompt | Cache only stable, permitted, reused prefixes |
| Durable rule copied into user prompt | Put it in governed configuration |
| No owner or review date | Maintain a source register |

## 13. Review questions

1. Why is retrieval an authorization decision?
2. What makes a source authoritative for a particular answer?
3. How should unresolved source conflict appear in the output?
4. Which prompt sections are good caching candidates?
5. Why can summarization create a configuration risk?
