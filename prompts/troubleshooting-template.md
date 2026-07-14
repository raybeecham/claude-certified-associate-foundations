# Troubleshooting Template

```text
You are assisting with a controlled troubleshooting investigation.

<symptom>
[Precise observed behavior]
</symptom>

<impact>
[Users, systems, severity, frequency]
</impact>

<known_good_baseline>
[Model, prompt, tools, sources, schema, and date]
</known_good_baseline>

<evidence>
[Logs, stop reason, tool calls, retrieval results, metrics, versions]
</evidence>

Tasks:
1. Classify the likely failure layer.
2. List hypotheses in priority order.
3. For each hypothesis, identify supporting evidence and a falsifying test.
4. Propose the minimum controlled experiment that changes one variable.
5. Define pass criteria and regression tests.
6. Define rollback and monitoring.
7. Do not claim a root cause until evidence supports it.

Output:
- symptom restatement
- layer classification
- evidence gaps
- hypothesis table
- experiment plan
- safety constraints
- decision criteria
```

## Use with caution

Do not include credentials or unrestricted production logs. Redact sensitive content and preserve the authoritative evidence outside the prompt.
