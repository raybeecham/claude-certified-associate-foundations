# Glossary

**Agent:** A system in which a model selects and performs actions through tools, usually across multiple steps and with bounded autonomy.

**Application state:** Conversation history, workflow status, user data, tool results, and other information maintained by the surrounding application.

**Authority:** The precedence assigned to an instruction or knowledge source when information conflicts.

**Cache breakpoint:** A designated boundary after which a stable prompt prefix may be reused according to the platform's caching behavior.

**Citation accuracy:** The degree to which a citation actually supports the claim attached to it.

**Context window:** The amount of input and generated content that a model can process within a request or conversation under the applicable platform behavior.

**Deterministic control:** Logic that should produce the same result for the same input, such as schema validation, arithmetic, authorization, or a business rule.

**Evaluation set:** A collection of representative test cases used to measure system behavior.

**Grounding:** Constraining an answer to supplied or retrieved evidence and maintaining traceability from claims to sources.

**Hallucination:** A confident-looking statement that is unsupported, fabricated, or inconsistent with the governing evidence.

**High-impact decision:** A decision or recommendation that can materially affect a person's rights, access, opportunities, safety, finances, health, or legal position.

**Human in the loop:** A control in which a qualified person reviews evidence and retains meaningful authority before a consequential action.

**Idempotency:** The property that repeating an operation does not create unintended duplicate effects.

**Instruction hierarchy:** The precedence relationship among platform, system, developer, user, retrieved, and tool-provided instructions.

**Jailbreak:** An attempt to bypass model or application safeguards.

**Knowledge cutoff:** The boundary of information represented in a model's training, distinct from information supplied in the current context or retrieved through tools.

**Least privilege:** Granting only the data and action permissions necessary for the current task.

**Model-assisted grader:** A model used to score another model's output against a rubric. It requires calibration and monitoring.

**Prompt injection:** Untrusted content designed to alter model behavior, override instructions, or induce unauthorized actions.

**Prompt chaining:** Decomposing a task into multiple model calls with explicit intermediate outputs and checks.

**Regression test:** A test used to determine whether a prompt, model, tool, data, or configuration change degraded established behavior.

**Retrieval:** Selecting relevant source material from a knowledge collection for inclusion in the model context.

**Schema:** A formal definition of required fields, types, values, and constraints for structured input or output.

**Stop reason:** Metadata describing why generation ended, such as completion, a limit, a tool request, or another platform-defined condition.

**Structured output:** Output constrained to a machine-readable format and schema.

**Success criteria:** Specific and measurable conditions that define acceptable performance.

**Tool contract:** The tool's purpose, authorization, input schema, output schema, errors, side effects, and conditions for use.

**Traceability:** The ability to reconstruct which model, prompt, sources, tools, configuration, and approvals produced an outcome.

**Workflow:** A designed sequence of steps with explicit control flow, state, validation, and responsibility.
