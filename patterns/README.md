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

## Planned pattern groups

- entry-point patterns;
- additional prompting patterns;
- evaluation patterns;
- integration patterns;
- governance patterns; and
- troubleshooting patterns.

## Usage rule

Use the least complex pattern that meets the requirement. Additional capabilities, stronger models, larger contexts, and longer sessions add setup, maintenance, usage, permission, validation, and governance obligations.

## Public-repository content rule

Patterns and examples must use fictional, generic, synthetic, or public information. Do not include client names, confidential information, proprietary workflows, credentials, or facts that identify a nonpublic engagement.