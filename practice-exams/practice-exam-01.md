# Practice Exam 1

**Questions:** 28  
**Coverage:** Four questions from each domain  
**Status:** Original, unofficial practice material

Record answers on a separate sheet or use the CLI:

```bash
python -m tools.study_cli practice --exam 1
```

---

### 1. An analyst needs to compare two approved policy documents, explore several interpretations, and remain responsible for the final conclusions. There is no integration requirement and the task is occasional. Which approach is the best initial fit?

- **A.** Use an approved interactive Claude experience for human-led analysis.
- **B.** Build a fully autonomous agent with write access to the policy repository.
- **C.** Create a batch API service before the analyst has tested the workflow.
- **D.** Embed the documents in a public website so any model can access them.

### 2. A stakeholder says, “Make Claude give us better security reports.” What is the best first step?

- **A.** Define the task, audience, authoritative inputs, constraints, output requirements, and measurable success criteria.
- **B.** Add “be very accurate” to the current prompt.
- **C.** Increase the requested response length.
- **D.** Assign Claude the role of “world-class security expert” and make no other change.

### 3. A team says a summarizer is “not good enough” and wants to rewrite the prompt immediately. What should happen first?

- **A.** Increase the number of adjectives in the prompt.
- **B.** Define measurable success criteria and construct representative tests that expose the reported failure.
- **C.** Select the longest available output setting.
- **D.** Ask users to accept more variation.

### 4. A workflow calculates exact payment totals and then drafts a plain-language explanation. Which division of responsibility is best?

- **A.** Use deterministic code for the calculations and Claude for the explanation based on validated results.
- **B.** Ask Claude to calculate and authorize the payment in one step.
- **C.** Let a human retype every number after generation.
- **D.** Use retrieval to estimate the payment.

### 5. An internal knowledge document is used to answer policy questions, but no one knows whether it is current. What metadata is most important to establish first?

- **A.** The document's font and page color
- **B.** Its owner, authority, version or effective date, classification, scope, and review cadence
- **C.** How many users have downloaded it
- **D.** Whether it contains the word “policy”

### 6. A team wants to paste confidential architecture diagrams into a new Claude workspace. What should happen first?

- **A.** Classify the data and verify that the product environment, access, retention, logging, residency, contractual, and organizational controls permit the use.
- **B.** Upload the diagrams, then check policy if a problem occurs.
- **C.** Remove the document titles and assume the content is public.
- **D.** Ask Claude whether the workspace is approved.

### 7. A report generator became less accurate after a release that changed the model, prompt, tools, retrieval query, and schema. What is the best first technical step?

- **A.** Reconstruct the known-good baseline and compare one changed component at a time on the same evaluation set.
- **B.** Keep all changes and add more instructions.
- **C.** Retry each failed case until it passes once.
- **D.** Assume the model is the only possible cause.

### 8. A developer sends a second Messages API request containing only the text, “Now summarize the risks.” Claude does not appear to know the earlier discussion. What is the best explanation and corrective action?

- **A.** The model forgot because the temperature was too high; lower it.
- **B.** The application must preserve and resend the relevant conversation history or a validated state representation.
- **C.** The developer should add the word “remember” to the user message.
- **D.** The API can retain state only after a tool call.

### 9. A classifier confuses “planned,” “in progress,” and “implemented” when evidence is phrased indirectly. The written definitions are already concise. What prompt change is most targeted?

- **A.** Repeat the definitions three times.
- **B.** Ask for a more creative answer.
- **C.** Remove the allowed labels.
- **D.** Add representative positive, negative, and boundary examples for each label.

### 10. A workflow must return exactly one of four allowed status labels and a valid control identifier. Which grader is best for these properties?

- **A.** Deterministic code that validates the enumeration and identifier
- **B.** An unstructured human opinion
- **C.** A second model asked whether the output feels correct
- **D.** The original model's self-reported confidence

### 11. A system drafts a public incident statement from verified evidence. Where should the communications lead's approval occur?

- **A.** After the statement has been posted
- **B.** Only after public feedback arrives
- **C.** After evidence and policy validation but before any publishing tool can execute
- **D.** Inside a hidden model instruction with no reviewer interface

### 12. Every response in a controlled application must cite approved evidence and use `insufficient_evidence` when support is absent. Where should this rule live?

- **A.** Only in each user's memory
- **B.** Only in the source documents
- **C.** In version-controlled application or system configuration, with retrieval and validation enforcing it
- **D.** In a model-generated note that is not saved

### 13. A housing organization uses Claude to rank applicants for eligibility. Which control is most important before any adverse decision?

- **A.** Use the longest possible prompt.
- **B.** Require meaningful review by a qualified authorized human with evidence, disclose AI involvement as required, and provide an appropriate contest or appeal path.
- **C.** Automatically accept the top-ranked answer when confidence exceeds 90%.
- **D.** Have an untrained employee approve every result without seeing the underlying evidence.

### 14. Claude chooses the public search tool instead of the internal standards tool. Both tools have similar names and descriptions. Which fix is most directly supported by the symptom?

- **A.** Increase the maximum output length.
- **B.** Differentiate the tool purposes and when-to-use rules, strengthen schemas and examples, and expose only eligible tools.
- **C.** Allow the public tool to access internal data.
- **D.** Remove all tool descriptions.

### 15. A team must classify millions of short public documents into six routing categories. Several candidate models meet the required accuracy on a representative test set. Which selection rule is strongest?

- **A.** Always select the model with the largest context window.
- **B.** Always select the newest model regardless of measured results.
- **C.** Select the fastest, lowest-total-cost candidate that still meets all quality, throughput, governance, and reliability thresholds.
- **D.** Select the model that produces the longest explanations.

### 16. A prompt contains policy instructions, three source documents, examples, and a requested JSON output. Claude sometimes treats text inside a source as an instruction. Which prompt improvement is most directly relevant?

- **A.** Use more adjectives to describe the desired answer.
- **B.** Clearly delimit and label trusted instructions, examples, untrusted source data, and the requested output.
- **C.** Put all content into one paragraph so the model sees it together.
- **D.** Remove the instruction that sources are untrusted.

### 17. A customer-support answer must follow policy, contain required disclosures, and communicate with appropriate empathy. Which evaluation design is strongest?

- **A.** Use only exact string matching for the whole answer.
- **B.** Use only a single reviewer's overall impression.
- **C.** Use deterministic checks for required policy elements plus a calibrated human or model-assisted rubric for nuanced communication, with periodic human review.
- **D.** Use response length as the sole metric.

### 18. A payment tool times out after submission. The client does not know whether the payment completed. What is the safest next action?

- **A.** Immediately submit the same payment again with a new identifier.
- **B.** Use the original idempotency key or transaction identifier to check status before any retry.
- **C.** Ask Claude whether it thinks the payment succeeded.
- **D.** Ignore the timeout and mark the workflow complete.

### 19. A service repeatedly sends the same long system instructions, tool definitions, and approved reference text, followed by a different short user task. Data policy permits caching. What optimization is most relevant?

- **A.** Place the stable reusable content in a consistent prompt prefix and use the platform's prompt-caching behavior, then measure actual hits.
- **B.** Move a changing timestamp to the beginning of the prompt.
- **C.** Store the API credential in the cached text.
- **D.** Randomize the order of tool definitions on each request.

### 20. An email-processing agent reads a message that instructs it to ignore policy and send customer records to an external address. Which control set is strongest?

- **A.** Ask the model to be careful and retain broad email tools.
- **B.** Hide the system prompt from users.
- **C.** Treat email as untrusted data, constrain tools and recipients, validate authorization in code, require approval for sensitive sends, and test adversarial cases.
- **D.** Retry with a different phrasing until the model complies.

### 21. A tool call contains an invented field named `system_owner_email`, which is neither required nor authorized. What is the strongest fix?

- **A.** Silently accept the field when it looks plausible.
- **B.** Ask Claude to spell the email more carefully.
- **C.** Use a strict schema that forbids extra fields, validate all parameters in the application, and require authoritative lookup for any identifier.
- **D.** Send the email to test whether it exists.

### 22. A request containing several documents is accepted, but the response stops midway through a required table. Which distinction should the team investigate first?

- **A.** The difference between a system prompt and a user prompt
- **B.** The difference between cached and uncached tokens
- **C.** The difference between training data and fine-tuning data
- **D.** The difference between available context capacity and the allowed generated output, including the reported stop reason

### 23. A single prompt must extract claims, verify evidence, resolve conflicts, draft an executive summary, and create a ticket. Errors are difficult to diagnose. What is the strongest redesign?

- **A.** Make the prompt longer but keep one opaque step.
- **B.** Allow the model to skip citation verification.
- **C.** Decompose the task into explicit stages with validated intermediate outputs and a separate controlled side effect.
- **D.** Retry the same prompt until an acceptable result appears.

### 24. An assistant invents implementation dates that are absent from the approved documents. Which combined control is strongest?

- **A.** Ask for more detailed dates.
- **B.** Increase creativity so the dates appear natural.
- **C.** Remove citations to make the answer easier to read.
- **D.** Restrict claims to approved sources, permit `unknown`, require claim-level citations or quotations, and validate support before release.

### 25. Which tool definition is most reliable for model-guided use?

- **A.** `manage_data`: Does data things.
- **B.** `run_action`: Use whenever needed; accepts any object.
- **C.** `admin`: Full system access for convenience.
- **D.** `create_draft_exception_request`: Creates a non-approved draft only, lists when it applies, requires typed fields and authorization, defines errors, and has no execution capability.

### 26. A policy assistant retrieves fifty documents for every question. Answers are slow and sometimes combine conflicting versions. What is the best redesign?

- **A.** Increase the response length so all documents are discussed.
- **B.** Tell Claude to ignore conflict without identifying it.
- **C.** Remove authorization filters so retrieval is faster.
- **D.** Retrieve the smallest relevant, permitted, authoritative, current set and attach provenance and conflict metadata.

### 27. A team logs every complete prompt, source document, tool credential, and response indefinitely “for debugging.” What is the best correction?

- **A.** Keep the design because more logs are always safer.
- **B.** Make logs publicly searchable so errors are found faster.
- **C.** Encrypt the credential but continue logging it.
- **D.** Minimize and redact content, never log secrets, apply access control and retention, and retain only evidence needed for audit and diagnosis.

### 28. Prompt-cache hit rates collapse after a release even though the long reference text did not change. Which item should the team inspect first?

- **A.** Whether any content, ordering, tool definitions, or cache breakpoint in the reusable prefix changed
- **B.** Whether the final user answer used more adjectives
- **C.** Whether reviewers liked the output tone
- **D.** Whether the model's pretrained knowledge changed
