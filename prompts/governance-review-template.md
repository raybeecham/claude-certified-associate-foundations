# Governance Review Template

```text
Assess the proposed Claude use case against the supplied governance requirements.

Do not provide a legal conclusion. Identify evidence, gaps, risk, and the human
authority required for a decision.

<use_case>
Purpose:
Users:
Affected parties:
Data:
Model:
Tools:
Knowledge:
Outputs:
Side effects:
Human review:
Monitoring:
</use_case>

<governance_requirements>
[Current approved policies and controls]
</governance_requirements>

For each area, report:
- status: satisfied | partial | not_established | conflict
- evidence
- gap
- risk if unresolved
- required control
- accountable owner role
- approval authority
- review date

Areas:
1. intended use and prohibited use
2. data classification and environment
3. access and least privilege
4. source authority and freshness
5. high-impact decisions and human oversight
6. prompt injection and tool security
7. evaluation and release gates
8. logging, monitoring, and retention
9. change management
10. incident response
```

## Important

A generated governance review is decision support. It does not itself approve the use case or an exception.
