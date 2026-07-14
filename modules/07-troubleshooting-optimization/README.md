# Module 7: Troubleshooting & Optimization

## Why this domain matters

Uncontrolled prompt tweaking produces fragile systems. Effective troubleshooting begins with evidence, reproduction, a baseline, one hypothesis, one change, and a regression test.

## Learning objectives

By the end of this module, you should be able to:

- classify failures by layer;
- collect the minimum diagnostic evidence;
- reproduce problems with a minimal case;
- compare behavior to a known-good baseline;
- diagnose wrong tools, bad parameters, truncation, refusals, cache misses, and latency;
- change one variable at a time;
- validate fixes against a representative evaluation set; and
- document rollback and monitoring.

## Files

- [notes.md](notes.md)
- [lab.md](lab.md)
- [flashcards.md](flashcards.md)
- [quiz.md](quiz.md)

## Exam lens

Prefer measurement before optimization. A model change is not the first response to every quality or latency issue. Diagnose the responsible stage and apply the narrowest fix that survives regression testing.

## Completion criteria

- [ ] I can classify a failure without immediately editing the prompt.
- [ ] I can diagnose tool-selection and schema failures.
- [ ] I can interpret stop behavior and cache patterns.
- [ ] I can profile latency by stage.
- [ ] I completed the troubleshooting lab and scored at least 80% on the quiz.

## Official reading

- [Troubleshooting tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)
- [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Reducing latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
