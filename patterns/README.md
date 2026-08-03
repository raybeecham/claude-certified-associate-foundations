# Claude Engineering Pattern Library

This directory converts certification concepts into reusable workflow-design patterns.

A pattern describes:

- the problem being solved;
- the context in which the problem appears;
- the recommended design;
- trade-offs and controls;
- common failure modes; and
- a compact decision rule.

The pattern library is an engineering reference, not a substitute for current official product documentation. Feature availability, model behavior, permissions, pricing, context limits, and plan details can change.

## Available patterns

- [Capability patterns](capability-patterns.md): Separate Project context, Skill procedures, Code Execution, and Memory continuity
- [Memory patterns](memory-patterns.md): Minimize, curate, scope, import, protect, and remediate persistent continuity
- [Model-selection patterns](model-selection-patterns.md): Select tiers, evaluate the minimum qualified model, route exceptions, and control migrations
- [Context-management patterns](context-management-patterns.md): Budget context, detect drift, restart cleanly, transfer state, persist correctly, and plan around usage limits
- [Task Specification Before Prompting](task-specification-before-prompting.md): Define objective, evidence, constraints, output, uncertainty, and success criteria before optimizing wording
- [Failure Localization Pattern](failure-localization-pattern.md): Observe, classify, localize, modify, validate, and decide without rewriting blindly
- [Task Strategy Fit Pattern](task-strategy-fit-pattern.md): Match control and creative latitude to analysis, research, drafting, brainstorming, and hybrid tasks
- [Prompt Calibration Pattern](prompt-calibration-pattern.md): Distinguish under-specification from over-specification and target the minimum sufficient task contract
- [Three-Reference Discernment Pattern](three-reference-discernment-pattern.md): Evaluate requirements, source support, professional standards, accuracy, completeness, stakes, and release disposition
- [Failure Signature Review Pattern](failure-signature-review-pattern.md): Detect hallucinations, contradictions, bias, silent omissions, and unverified capability claims through targeted evidence and system checks
- [Grounded Verification Pattern](grounded-verification-pattern.md): Define evidence boundaries, permit unknowns, map claims to sources, validate authoritatively, recompute deterministically, and record release disposition
- [Human Review Gate Pattern](human-review-gate-pattern.md): Precommit risk thresholds, define qualified reviewers, place approval before irreversible actions, and escalate when prompting reaches its limits
- [Audience Adaptation Pattern](audience-adaptation-pattern.md): Preserve verified invariants while adapting selection, depth, tone, order, format, and disclosure for the intended audience
- [Output Format and Reliability Pattern](output-format-reliability-pattern.md): Match inline, artifact, structured, and code-executed paths to consumer, reuse, machine-readability, computation, and release requirements
- [Requirements Traceability and Pressure-Test Pattern](requirements-traceability-pressure-test-pattern.md): Convert messy source material into atomic, traceable requirements, classify uncertainty, challenge completeness, and approve a baseline before workflow design
- [Verified Planning Workflow Pattern](verified-planning-workflow-pattern.md): Combine current research, executed quantitative analysis, explicit assumptions, scenario synthesis, human judgment, and process optimization into a defensible plan
- [Evidence-Driven Prototype Iteration Pattern](evidence-driven-prototype-iteration-pattern.md): Preserve stable design context, test bounded hypotheses, classify feedback, refine through controlled changes, and separate prototype success from production readiness
- [Delegation Boundary Mapping Pattern](delegation-boundary-mapping-pattern.md): Map atomic work, assess reversibility, stakes, and accountability, assign model/code/tool/storage/human ownership, and place review before consequence

## Planned pattern groups

- entry-point patterns;
- additional prompting patterns;
- additional evaluation patterns;
- integration patterns;
- governance patterns; and
- troubleshooting patterns.

## Usage rule

Use the least complex pattern that meets the requirement. Additional capabilities, stronger models, larger contexts, and longer sessions add setup, maintenance, usage, permission, validation, and governance obligations.

## Public-repository content rule

Patterns and examples must use fictional, generic, synthetic, or public information. Do not include client names, confidential information, proprietary workflows, credentials, or facts that identify a nonpublic engagement.
