# Module 3: Evaluating & Validating Claude's Output

## Why this domain matters

A plausible output is not evidence of a reliable system. Evaluation connects business requirements to measurable behavior, exposes edge cases, prevents regressions, and determines whether an output is safe to release.

## Learning objectives

By the end of this module, you should be able to:

- define specific, measurable, achievable, and relevant success criteria;
- construct representative test sets with normal, edge, conflicting, missing, and adversarial cases;
- select code-based, human, and model-assisted grading methods;
- evaluate grounding and citation support;
- measure consistency and regression;
- distinguish average performance from release-blocking failures;
- calibrate rubrics and reviewers; and
- design validation for high-stakes outputs.

## Files

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

The strongest answer usually establishes criteria and tests before changing the prompt. Match the grader to the property being measured. Exact labels favor deterministic checks, while nuanced policy or high-impact judgment requires qualified human review.

## Completion criteria

- [ ] I can define multidimensional success criteria.
- [ ] I can build a representative evaluation set.
- [ ] I can justify the selected grader.
- [ ] I can verify claim-to-source support.
- [ ] I completed the evaluation lab and scored at least 80% on the quiz.

## Official reading

- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
