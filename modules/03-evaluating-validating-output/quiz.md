# Quiz: Evaluating & Validating Claude's Output

Answer all eight questions before opening the answer key. Target score: **80% or better**.

### 1. A team says a summarizer is “not good enough” and wants to rewrite the prompt immediately. What should happen first?

- **A.** Increase the number of adjectives in the prompt.
- **B.** Define measurable success criteria and construct representative tests that expose the reported failure.
- **C.** Select the longest available output setting.
- **D.** Ask users to accept more variation.

### 2. A workflow must return exactly one of four allowed status labels and a valid control identifier. Which grader is best for these properties?

- **A.** Deterministic code that validates the enumeration and identifier
- **B.** An unstructured human opinion
- **C.** A second model asked whether the output feels correct
- **D.** The original model's self-reported confidence

### 3. A customer-support answer must follow policy, contain required disclosures, and communicate with appropriate empathy. Which evaluation design is strongest?

- **A.** Use only exact string matching for the whole answer.
- **B.** Use only a single reviewer's overall impression.
- **C.** Use deterministic checks for required policy elements plus a calibrated human or model-assisted rubric for nuanced communication, with periodic human review.
- **D.** Use response length as the sole metric.

### 4. An assistant invents implementation dates that are absent from the approved documents. Which combined control is strongest?

- **A.** Ask for more detailed dates.
- **B.** Increase creativity so the dates appear natural.
- **C.** Remove citations to make the answer easier to read.
- **D.** Restrict claims to approved sources, permit `unknown`, require claim-level citations or quotations, and validate support before release.

### 5. A policy assistant performs well on ten clean examples written by its developers. Which addition most improves confidence in production readiness?

- **A.** Ten paraphrases of the same clean examples
- **B.** Realistic cases covering normal inputs, missing and conflicting evidence, stale sources, long inputs, unauthorized requests, and prompt injection attempts
- **C.** One very long prompt that includes every possible instruction
- **D.** A reviewer who reads only the best outputs

### 6. A candidate version scores 96% overall, up from 93%. However, one test exposes another business unit's confidential document. What is the correct release decision?

- **A.** Release because the aggregate score improved.
- **B.** Average the privacy failure with the style scores.
- **C.** Block release, investigate the access-control failure, and require a validated fix before reconsideration.
- **D.** Release to all users but add a warning.

### 7. Claude drafts individualized legal guidance from uploaded records. What validation approach is most appropriate before the guidance affects a person's decision?

- **A.** Require review by a qualified legal professional with access to the evidence, disclose AI involvement as required, and preserve the person's ability to question or contest the guidance.
- **B.** Use the model's confidence score as final approval.
- **C.** Publish automatically when the prose is fluent.
- **D.** Ask an untrained reviewer to click approve within ten seconds.

### 8. A classification result changes across repeated runs on the same input. The business requires stable routing. What is the strongest evaluation response?

- **A.** Review only the first run.
- **B.** Accept variation because language models are probabilistic.
- **C.** Measure the length of each explanation.
- **D.** Run repeated trials, measure label agreement and worst-case behavior, set a consistency threshold, and test prompt, schema, and model changes against it.

<details>
<summary>Answer key and rationales</summary>

### 1. A team says a summarizer is “not good enough” and wants to rewrite the prompt immediately. What should happen first?

- **A.** Increase the number of adjectives in the prompt.
- **B.** Define measurable success criteria and construct representative tests that expose the reported failure.
- **C.** Select the longest available output setting.
- **D.** Ask users to accept more variation.

**Answer: B**

**Rationale:** The team must define what acceptable performance means and how it will be measured before prompt changes can be evaluated.

**Why the other options are weaker:**

- **A:** Wording changes without criteria cannot be assessed objectively.
- **C:** Output length may be unrelated to the actual failure.
- **D:** Changing expectations without understanding the use case is not evaluation.

**Objective:** Evaluation-first development  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 2. A workflow must return exactly one of four allowed status labels and a valid control identifier. Which grader is best for these properties?

- **A.** Deterministic code that validates the enumeration and identifier
- **B.** An unstructured human opinion
- **C.** A second model asked whether the output feels correct
- **D.** The original model's self-reported confidence

**Answer: A**

**Rationale:** Allowed values and identifier validity are exact, machine-checkable properties. Deterministic validation is consistent and auditable.

**Why the other options are weaker:**

- **B:** Human review is unnecessarily expensive and less consistent for exact checks.
- **C:** A model grader adds variability to a deterministic property.
- **D:** Self-reported confidence does not validate the actual fields.

**Objective:** Code-based grading  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 3. A customer-support answer must follow policy, contain required disclosures, and communicate with appropriate empathy. Which evaluation design is strongest?

- **A.** Use only exact string matching for the whole answer.
- **B.** Use only a single reviewer's overall impression.
- **C.** Use deterministic checks for required policy elements plus a calibrated human or model-assisted rubric for nuanced communication, with periodic human review.
- **D.** Use response length as the sole metric.

**Answer: C**

**Rationale:** Different properties require different graders. Exact requirements can be automated, while nuanced tone needs a calibrated semantic judgment process.

**Why the other options are weaker:**

- **A:** Exact matching cannot reliably score nuanced communication.
- **B:** One uncalibrated impression is subjective and difficult to reproduce.
- **D:** Length does not measure policy fidelity or empathy.

**Objective:** Mixed-method grading  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 4. An assistant invents implementation dates that are absent from the approved documents. Which combined control is strongest?

- **A.** Ask for more detailed dates.
- **B.** Increase creativity so the dates appear natural.
- **C.** Remove citations to make the answer easier to read.
- **D.** Restrict claims to approved sources, permit `unknown`, require claim-level citations or quotations, and validate support before release.

**Answer: D**

**Rationale:** The system should make unsupported specificity unnecessary and detectable by grounding every claim and permitting abstention.

**Why the other options are weaker:**

- **A:** Requesting more detail can increase fabrication when evidence is absent.
- **B:** Creativity is contrary to evidence-bound reporting.
- **C:** Removing citations reduces traceability.

**Objective:** Grounding controls  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

### 5. A policy assistant performs well on ten clean examples written by its developers. Which addition most improves confidence in production readiness?

- **A.** Ten paraphrases of the same clean examples
- **B.** Realistic cases covering normal inputs, missing and conflicting evidence, stale sources, long inputs, unauthorized requests, and prompt injection attempts
- **C.** One very long prompt that includes every possible instruction
- **D.** A reviewer who reads only the best outputs

**Answer: B**

**Rationale:** A representative evaluation set must reflect the real distribution and intentionally test edge and adversarial conditions.

**Why the other options are weaker:**

- **A:** Paraphrases improve volume but not risk coverage.
- **C:** Prompt length is not a substitute for test diversity.
- **D:** Selecting only successful outputs creates severe bias.

**Objective:** Representative evaluation sets  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 6. A candidate version scores 96% overall, up from 93%. However, one test exposes another business unit's confidential document. What is the correct release decision?

- **A.** Release because the aggregate score improved.
- **B.** Average the privacy failure with the style scores.
- **C.** Block release, investigate the access-control failure, and require a validated fix before reconsideration.
- **D.** Release to all users but add a warning.

**Answer: C**

**Rationale:** Unauthorized disclosure is a critical failure and must be a hard release gate. Aggregate quality cannot offset it.

**Why the other options are weaker:**

- **A:** An average hides severity and does not make the disclosure acceptable.
- **B:** Privacy should not be diluted by unrelated low-severity metrics.
- **D:** A warning does not prevent unauthorized access.

**Objective:** Severity-based release gates  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

### 7. Claude drafts individualized legal guidance from uploaded records. What validation approach is most appropriate before the guidance affects a person's decision?

- **A.** Require review by a qualified legal professional with access to the evidence, disclose AI involvement as required, and preserve the person's ability to question or contest the guidance.
- **B.** Use the model's confidence score as final approval.
- **C.** Publish automatically when the prose is fluent.
- **D.** Ask an untrained reviewer to click approve within ten seconds.

**Answer: A**

**Rationale:** High-impact legal guidance requires meaningful qualified human oversight, evidence access, and appropriate disclosure. Accountability cannot be delegated to model confidence.

**Why the other options are weaker:**

- **B:** Self-reported confidence is not a legal or factual validation.
- **C:** Fluency does not establish correctness or suitability.
- **D:** An unqualified, rushed reviewer is not meaningful oversight.

**Objective:** High-stakes validation  
**Reference:** https://www.anthropic.com/legal/aup

### 8. A classification result changes across repeated runs on the same input. The business requires stable routing. What is the strongest evaluation response?

- **A.** Review only the first run.
- **B.** Accept variation because language models are probabilistic.
- **C.** Measure the length of each explanation.
- **D.** Run repeated trials, measure label agreement and worst-case behavior, set a consistency threshold, and test prompt, schema, and model changes against it.

**Answer: D**

**Rationale:** When stability is a requirement, the evaluation must measure output variance at the level that matters and enforce a threshold.

**Why the other options are weaker:**

- **A:** A single run cannot reveal instability.
- **B:** Probabilistic behavior does not remove the business requirement.
- **C:** Explanation length is not label consistency.

**Objective:** Consistency evaluation  
**Reference:** https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

</details>
