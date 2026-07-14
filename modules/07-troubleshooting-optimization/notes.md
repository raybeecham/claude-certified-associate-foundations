# Notes: Troubleshooting & Optimization

## 1. Use a disciplined troubleshooting loop

1. Define the symptom precisely.
2. Establish scope and severity.
3. Reproduce with a minimal case.
4. Collect evidence.
5. Compare with a known-good baseline.
6. Form one falsifiable hypothesis.
7. Change one variable.
8. Retest the minimal case and full evaluation set.
9. Monitor for regression.
10. Document the cause, fix, and rollback.

Avoid random prompt edits. They can mask the issue and create new failures.

## 2. Classify the layer

| Layer | Example symptoms |
|---|---|
| Input | Missing, malformed, oversized, or unauthorized data |
| Instructions | Ambiguity, conflicts, poor examples, wrong priority |
| Model | Capability mismatch, version change, refusal behavior |
| Context/retrieval | Irrelevant, stale, conflicting, or inaccessible sources |
| Tool selection | Wrong tool or no tool |
| Tool parameters | Invalid types, invented fields, missing required values |
| Tool execution | Timeout, permissions, side-effect ambiguity |
| Output | Invalid schema, unsupported claim, truncation |
| Evaluation | Wrong metric, biased test set, grader drift |
| Workflow | State loss, duplicate action, missing approval |
| Platform/operations | Rate limit, outage, latency, cache miss |
| Governance | Policy, access, retention, or prohibited-use conflict |

The layer classification determines the likely evidence and fix.

## 3. Collect diagnostic evidence

Capture:

- exact input, with approved redaction;
- trusted instructions;
- prompt/template version;
- model and API version;
- parameters;
- source IDs and retrieved passages;
- tool definitions;
- requested and executed tool calls;
- response content;
- stop reason;
- token and latency data;
- error codes;
- authorization context;
- validation results;
- baseline result; and
- timestamp and environment.

A screenshot of the final answer is rarely enough.

## 4. Wrong tool selection

Symptoms:

- a similar but inappropriate tool is selected;
- the model does not select a required tool;
- the model invokes multiple tools unnecessarily; or
- the model requests a tool outside the task.

Likely causes:

- ambiguous names;
- overlapping descriptions;
- missing “when to use” guidance;
- missing negative guidance;
- too many tools in context;
- insufficient examples;
- incorrect workflow state; or
- tool unavailable or unauthorized.

Fixes:

- differentiate tool names;
- rewrite purpose and selection boundaries;
- add representative examples;
- expose only relevant tools;
- enforce workflow eligibility;
- test confusing pairs; and
- validate authorization outside the model.

## 5. Bad tool parameters

Symptoms:

- wrong type;
- missing required field;
- invented identifier;
- unsupported enumeration;
- unsafe broad scope; or
- malformed nested object.

Fixes:

- strict schemas;
- descriptive field names;
- enum constraints;
- formats and ranges;
- examples;
- application-side validation;
- lookup of authoritative IDs;
- explicit missing-data behavior; and
- rejection before execution.

Do not coerce dangerous or ambiguous parameters silently.

## 6. Hallucination and unsupported claims

Investigate:

- whether the task was grounded;
- whether relevant evidence was retrieved;
- source authority and conflict;
- whether the prompt forced an answer;
- citation requirements;
- whether claims add specificity beyond evidence;
- context overload;
- validator coverage; and
- model or prompt changes.

Fix at the responsible layer:

- improve retrieval;
- restrict allowed sources;
- permit unknown;
- require quotations or citations;
- validate claims;
- decompose extraction and synthesis;
- change the model only if capability evidence supports it.

## 7. Truncation and incomplete output

Check:

- stop reason;
- requested output budget;
- prompt and retrieved context size;
- structured-output behavior;
- network or client streaming;
- application timeout;
- tool loop limit; and
- whether the task is too large for one response.

Fixes:

- reserve more output budget;
- reduce irrelevant context;
- paginate;
- decompose;
- request a concise schema;
- resume from a validated checkpoint; or
- handle partial output explicitly.

Do not concatenate partial machine-readable output without validation.

## 8. Refusals

First determine whether the request conflicts with provider policy, organizational policy, permissions, or safety requirements.

Then:

- respect a legitimate refusal;
- redesign the task only within allowed boundaries;
- remove unnecessary sensitive or disallowed content;
- separate allowed analytical work from prohibited action;
- provide human escalation;
- inspect stop or refusal metadata when available; and
- avoid repeated evasion attempts.

A refusal is not always a model-quality defect.

## 9. Prompt caching misses

Inspect:

- whether the cached prefix is identical;
- content ordering;
- cache breakpoint placement;
- changed tool definitions;
- changed system instructions;
- minimum eligibility requirements;
- expiration;
- request routing and supported behavior; and
- cache diagnostics or usage fields.

Small dynamic fields inserted early can invalidate a large reusable prefix. Place stable reusable content first when the platform's caching semantics support that design and policy permits it.

## 10. Latency

Measure before optimizing.

Break down:

- client and network;
- authentication;
- input validation;
- retrieval;
- queueing;
- model time to first token;
- generation time;
- tool selection;
- tool execution;
- validation;
- human review; and
- final side effect.

Possible improvements:

- choose a model that meets the quality threshold at lower latency;
- reduce unnecessary context;
- cache stable prefixes;
- parallelize independent retrieval or tools;
- stream user-visible output;
- reduce output length;
- use batch processing where appropriate;
- eliminate redundant calls;
- precompute static data; and
- tune retries and timeouts.

Do not reduce validation or governance controls without a risk decision.

## 11. Cost

Measure cost per successful task, not merely per request.

Include:

- input and output usage;
- retries;
- failed tool calls;
- duplicated side effects;
- retrieval and infrastructure;
- human correction;
- incident and audit burden; and
- cache performance.

A cheaper request that doubles the correction rate can be a more expensive workflow.

## 12. Controlled experiments

Use an experiment table:

| Run | Model | Prompt | Sources | Tools | Variable changed | Quality | Latency | Cost | Notes |
|---|---|---|---|---|---|---:|---:|---:|---|

Change one material variable. Preserve the baseline and rollback.

For stochastic behavior, run enough repeats to observe the distribution rather than relying on one result.

## 13. Troubleshooting report

```text
Incident/symptom:
Impact:
Scope:
First observed:
Known-good baseline:
Evidence:
Layer classification:
Hypotheses:
Experiment:
Root cause:
Fix:
Regression results:
Rollback:
Monitoring:
Owner:
```

## 14. Common mistakes

| Mistake | Better approach |
|---|---|
| Edit prompt immediately | Classify and collect evidence |
| Change model and prompt together | One variable at a time |
| Retry a side effect blindly | Check status and idempotency |
| Treat every refusal as a bug | Verify policy and authorization |
| Optimize average latency only | Profile percentiles and stages |
| Assume cache based on prompt length | Inspect prefix identity and diagnostics |
| Accept repaired JSON without validation | Validate against schema |
| Close issue after one successful run | Run regression and monitor |

## 15. Review questions

1. What is the minimum evidence needed to diagnose a wrong tool call?
2. Why can a cache miss be caused by a tool-definition change?
3. How do you distinguish truncation from application timeout?
4. What metric best captures the total cost of an AI workflow?
5. Why should a fix be tested on both the minimal case and the full evaluation set?
