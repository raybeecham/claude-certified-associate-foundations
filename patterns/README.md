# Claude Engineering Pattern Library

This directory converts certification concepts into reusable workflow-design patterns.

A pattern describes the problem, context, recommended design, controls, failure modes, and a compact decision rule.

The pattern library is an engineering reference, not a substitute for current official product documentation. Feature availability, permissions, pricing, context limits, and plan details can change.

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
- [Capability, Value, and Limitation Communication Pattern](capability-value-limitation-communication-pattern.md): Describe bounded AI tasks, support value claims with scoped evidence, preserve material limitations across audiences, and operationalize human oversight
- [Project Configuration Slot Selection Pattern](project-configuration-slot-selection-pattern.md): Place behavior, facts, procedures, continuity, access, exact controls, and durable state in the correct configuration layer, then pair mechanisms without duplicating authority
- [Connector and Knowledge Boundary Pattern](connector-and-knowledge-boundary-pattern.md): Connect only required sources, document exact connector capabilities, classify source authority and freshness, curate uploads, and place approval before external consequence
- [Persistent Instruction Precision Pattern](persistent-instruction-precision-pattern.md): Convert recurring behavioral requirements into precise, observable, tested instructions with evidence, failure, conflict, and enforcement boundaries

## Planned pattern groups

- entry-point patterns;
- additional prompting patterns;
- additional evaluation patterns;
- integration patterns;
- governance patterns; and
- troubleshooting patterns.

## Usage rule

Use the least complex pattern that meets the requirement. Additional capabilities, stronger models, larger contexts, and longer sessions add setup, maintenance, permission, validation, and governance obligations.

## Public-repository content rule

Patterns and examples must use fictional, generic, synthetic, or public information. Do not include client names, confidential information, proprietary workflows, credentials, or facts that identify a nonpublic engagement.
