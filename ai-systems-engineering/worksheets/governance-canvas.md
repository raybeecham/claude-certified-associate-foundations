# Governance Canvas

Use this for workflows involving organizational data, connected systems, consequential decisions, or repeated deployment.

## 1. Use-case classification

**Purpose:**

> 

**Consequence:** Low / Moderate / High / Critical

**Deployment mode:** Personal / Team / Enterprise / Public / Embedded application

## 2. Data classification

| Data type | Classification | Authorized environment | Retention rule |
|---|---|---|---|
| | | | |

- [ ] Secrets and credentials are excluded from prompts and repositories.
- [ ] Unnecessary personal or sensitive fields are removed.
- [ ] Data residency and contractual restrictions are understood.
- [ ] Generated outputs receive appropriate access controls.

## 3. Authority model

| Content or instruction | Authority level | Can it direct tools? | Validation |
|---|---|---|---|
| System or application policy | Trusted | | |
| Project or workflow instructions | Trusted within scope | | |
| User request | Task authority | | |
| Retrieved document | Evidence, not instruction | No by default | |
| Website, email, or tool result | Untrusted data | No by default | |
| Memory | Continuity, not authority | No | |

## 4. Access and permissions

| Resource | Required access | Granted access | Justification | Revocation path |
|---|---|---|---|---|
| | | | | |

- [ ] Least privilege is applied.
- [ ] Read and write permissions are separated.
- [ ] Irreversible actions require explicit approval.
- [ ] Service identities and user identities are distinguishable.

## 5. Human oversight

| Decision or action | Required reviewer | Evidence required | SLA |
|---|---|---|---|
| | | | |

**Actions the AI may never perform autonomously:**

- 

## 6. Transparency

- How will users know AI assisted the result?
- What limitations must be disclosed?
- Which sources and assumptions will be shown?
- How can a user contest or correct the result?

## 7. Logging and privacy

Log only what is needed for:

- security;
- debugging;
- quality monitoring;
- audit; and
- incident response.

Do not log unnecessary sensitive content.

| Event | Logged data | Retention | Access |
|---|---|---|---|
| | | | |

## 8. Threats and controls

| Threat | Control | Test |
|---|---|---|
| Prompt injection | Authority separation and constrained tools | Adversarial test set |
| Data exfiltration | Egress restrictions and output review | Sensitive-data probes |
| Memory poisoning | Explicit confirmation and provenance | Persistence tests |
| Tool misuse | Narrow permissions and approval | Negative tool tests |
| Stale evidence | Ownership and refresh cadence | Freshness checks |
| Hallucination | Grounding, uncertainty, verification | Claim-to-source audit |
| Overreliance | Human accountability and disclosure | Review sampling |

## 9. Incident response

Define:

- detection channel;
- severity classification;
- containment action;
- evidence preservation;
- credential rotation;
- affected-user notification;
- rollback; and
- post-incident review.

## 10. Lifecycle

| Milestone | Owner | Date or cadence |
|---|---|---|
| Initial approval | | |
| Model and prompt review | | |
| Source refresh | | |
| Access review | | |
| Evaluation rerun | | |
| Retirement review | | |

## 11. Governance decision

- [ ] Data use is authorized.
- [ ] Risk is proportionate to benefit.
- [ ] Oversight is sufficient.
- [ ] Monitoring and incident response exist.
- [ ] The workflow can be disabled and retired.

**Decision:** Approve / Restrict / Revise / Reject

**Conditions:**

> 
