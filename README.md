# Claude Certified Associate - Foundations Study Guide

[![CI](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/ci.yml/badge.svg)](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/ci.yml)
[![Docs](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/docs.yml/badge.svg)](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An independent, scenario-driven study repository for the **Claude Certified Associate - Foundations** certification.

> [!IMPORTANT]
> This is an unofficial, community-maintained resource. It is not affiliated with, endorsed by, or sponsored by Anthropic. It contains original study material and does not reproduce proprietary course or exam questions. Always treat the official preparation course, current Anthropic documentation, certification policies, and exam guide as authoritative.

## What is included

| Resource | Count | Purpose |
|---|---:|---|
| Study domains | 7 | Complete coverage of the course areas listed below |
| Scenario questions | 56 | Original multiple-choice questions with rationales |
| Flashcards | 84 | Fast recall and spaced-repetition prompts |
| Practice exams | 2 | Balanced, 28-question exam simulations |
| Hands-on labs | 7 | Applied exercises with acceptance criteria |
| Case studies | 3 | Security, governance, and workflow design practice |
| Prompt templates | 7 | Reusable task, evaluation, orchestration, and review patterns |
| Engineering pattern library | Growing | Reusable Claude workflow and architecture patterns |
| Study CLI | 1 | Offline quizzes, flashcards, practice exams, and local score tracking |

## Study domains

1. [Claude Platform & Model Foundations](modules/01-platform-model-foundations/)
2. [Prompting & Task Execution](modules/02-prompting-task-execution/)
3. [Evaluating & Validating Claude's Output](modules/03-evaluating-validating-output/)
4. [Workflow Integration & Solutions Design](modules/04-workflow-integration-solutions-design/)
5. [Configuration & Knowledge Management](modules/05-configuration-knowledge-management/)
6. [Governance, Risk & Responsible Use](modules/06-governance-risk-responsible-use/)
7. [Troubleshooting & Optimization](modules/07-troubleshooting-optimization/)

## Recommended study loop

For each domain:

1. Read the module overview and learning objectives.
2. Work through `notes.md` and the course-aligned lessons.
3. Practice with the module prompt notebooks and engineering patterns.
4. Complete the module lab before viewing the model solution.
5. Drill the flashcards until recall is consistent.
6. Take the module quiz and explain why each distractor is wrong.
7. Record weak areas in [the progress tracker](docs/progress-tracker.md).
8. Revisit the official documentation linked from that module.

After all seven domains, complete both practice exams under timed, closed-note conditions.

## Quick start

The repository is useful as plain Markdown. Python is only needed for the optional study CLI and checks.

```bash
git clone https://github.com/raybeecham/claude-certified-associate-foundations.git
cd claude-certified-associate-foundations

python -m tools.study_cli domains
python -m tools.study_cli quiz --domain 2 --questions 8
python -m tools.study_cli flashcards --domain 6 --limit 12
python -m tools.study_cli practice --exam 1
python -m tools.study_cli stats
```

Run the validation suite:

```bash
python scripts/check_content.py
python -m unittest discover -s tests -v
```

Build the documentation site locally:

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## Suggested readiness standard

These are study recommendations, not official passing requirements:

- Score at least **80%** on every module quiz.
- Score at least **80%** on both practice exams on separate attempts.
- Explain the correct answer and each distractor without relying on memorized wording.
- Complete all seven labs and document your design decisions.
- Resolve every miss involving privacy, grounding, human review, tool permissions, or high-impact use.
- Verify product-specific facts against current official documentation before the exam.

## Repository design principles

- **Original content:** No exam dumps or copied proprietary questions.
- **Scenario first:** Questions test judgment, not trivia alone.
- **Evidence driven:** Prompt design starts with success criteria and evaluation.
- **Version aware:** Volatile model names, limits, pricing, and product behavior are not treated as permanent facts.
- **Governed deployment:** Data handling, least privilege, human oversight, logging, and incident response are part of solution design.
- **Security conscious:** Examples emphasize adversarial input, prompt injection, source integrity, and controlled tool use.
- **Separation of concerns:** Context, procedure, computation, continuity, and authoritative records are designed independently.
- **Public-safe examples:** Scenarios use fictional, generic, synthetic, or public information rather than identifiable nonpublic work.

## Documentation map

- [Certification overview](docs/certification-overview.md)
- [Four-week study plan](docs/study-plan.md)
- [Exam strategy](docs/exam-strategy.md)
- [Master cheat sheet](docs/master-cheat-sheet.md)
- [Glossary](docs/glossary.md)
- [Official resources](docs/official-resources.md)
- [Progress tracker](docs/progress-tracker.md)
- [Question-writing guide](docs/question-writing-guide.md)
- [Practice exams](practice-exams/)
- [Prompt library](prompts/)
- [Engineering pattern library](patterns/)
- [Case studies](case-studies/)

## Contributing

Corrections and improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Contributions must remain original and must not disclose remembered, reconstructed, or proprietary exam content.

## License

Code and original written material in this repository are licensed under the [MIT License](LICENSE), subject to the third-party rights and disclaimer described in [DISCLAIMER.md](DISCLAIMER.md).