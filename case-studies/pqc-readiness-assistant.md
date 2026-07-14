# Case Study: PQC Readiness Assistant

## Mission

A federal technology organization wants an assistant that helps system owners assess post-quantum cryptography readiness. The assistant ingests approved architecture evidence, identifies likely cryptographic dependencies, maps evidence to an internal control framework, and drafts remediation actions.

## Constraints

- It must not make a final compliance determination.
- It must not claim that a system has implemented a control without evidence.
- It may use public standards, approved internal policy, vendor documentation, and authorized system evidence.
- Vendor documentation supports product claims but does not prove deployment.
- System evidence may contain confidential technical information.
- The assistant can create a draft remediation item but cannot assign an individual, approve funding, or modify production.
- A security architect remains accountable.

## Architecture questions

1. Which interaction pattern is appropriate for exploratory analysis versus repeatable assessments?
2. How will the application manage state across evidence collection, analysis, review, and revision?
3. Which tasks belong to Claude?
4. Which tasks require deterministic code?
5. Which tools are required, and what are their permissions?
6. Where is human approval required?
7. What evidence must be logged to reproduce a result?

## Prompting questions

1. Write a task contract for control mapping.
2. Define allowed status labels.
3. Define `insufficient_evidence`.
4. Explain how source authority and conflicts are represented.
5. Create a structured output schema.
6. Design behavior for prompt injection in uploaded evidence.

## Evaluation questions

Create at least 25 cases covering:

- known cryptographic inventory;
- incomplete inventory;
- ambiguous library names;
- vendor claim without deployment evidence;
- conflicting internal and public guidance;
- superseded policy;
- malicious document instruction;
- unauthorized repository request;
- long architecture document;
- unsupported migration date;
- duplicate system identifier; and
- high-severity gap.

Define:

- exact checks;
- model-assisted rubric dimensions;
- human review conditions;
- hard release gates;
- latency and cost measures; and
- regression process.

## Governance questions

1. What data classifications may appear?
2. Which environments are approved?
3. How is business-unit or system access isolated?
4. What is disclosed to system owners about AI involvement?
5. Who can approve the final assessment?
6. What logs are retained and for how long?
7. What triggers an incident?
8. How are model, prompt, tool, and policy changes approved?

## Deliverable

Produce:

- requirements matrix;
- architecture and trust-boundary diagram;
- responsibility matrix;
- source register;
- prompt and output schema;
- tool contracts;
- evaluation plan;
- threat model;
- incident response summary;
- ADR; and
- go/no-go recommendation.

## Strong-solution indicators

- Evidence and implementation status remain distinct.
- Authorization happens before retrieval.
- Source conflicts are traceable.
- Exact rules are deterministic.
- The draft tool is idempotent and has no approval capability.
- The architect sees evidence, uncertainty, and validation results.
- Critical grounding and privacy failures block release.
