# Claude Certified Associate Foundations + AI Systems Engineering Handbook

[![CI](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/ci.yml/badge.svg)](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/ci.yml)
[![Docs](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/docs.yml/badge.svg)](https://github.com/raybeecham/claude-certified-associate-foundations/actions/workflows/docs.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An independent, scenario-driven study repository for the **Claude Certified Associate - Foundations** certification, paired with a vendor-neutral **AI Systems Engineering Playbook** for applying the same principles to real professional workflows.

> **Core principle:** Prompts generate answers. Workflow design determines whether those answers are reliable, repeatable, efficient, secure, and trustworthy.

> [!IMPORTANT]
> This is an unofficial, community-maintained resource. It is not affiliated with, endorsed by, or sponsored by Anthropic. The repository contains original study material and does not reproduce proprietary course or exam questions. Treat the official preparation course, current Anthropic documentation, certification policies, and exam guide as authoritative.

## Choose your path

| Goal | Start here | What you will learn |
|---|---|---|
| Prepare for the certification | [Certification modules](modules/) | Claude platform selection, prompting, evaluation, integration, knowledge, governance, and troubleshooting |
| Design a real AI-assisted workflow | [AI Systems Engineering Playbook](ai-systems-engineering/) | A vendor-neutral method for defining the problem, selecting architecture, designing prompts, validating output, and assigning human responsibility |
| Review the material quickly | [Master cheat sheet](docs/master-cheat-sheet.md) | High-value distinctions, decision rules, controls, and troubleshooting mappings |
| Practice scenario judgment | [Practice exams](practice-exams/) | Timed, original scenario questions with detailed rationales |
| Start a new AI project | [AI Project Canvas](ai-systems-engineering/worksheets/ai-project-canvas.md) | Business objective, evidence, workspace, capabilities, model, context, validation, ownership, and go/no-go criteria |

## Two complementary tracks

### Track 1: Claude certification preparation

The seven study domains follow the Claude Certified Associate - Foundations preparation areas. Each domain includes original notes, labs, flashcards, quizzes, scenario exercises, and links to current official documentation.

### Track 2: AI Systems Engineering

The [AI Systems Engineering Playbook](ai-systems-engineering/) converts certification concepts into a practical operating method that can be applied across Claude, ChatGPT, Gemini, open-source models, and future platforms.

```text
Business problem
      ↓
Workspace and capabilities
      ↓
Model and context strategy
      ↓
Workflow and prompt
      ↓
Evaluation and human review
      ↓
Delivery, monitoring, and improvement
```

The certification teaches the platform concepts. The playbook turns them into a repeatable engineering practice.

## Official exam guide at a glance

The current official guide is **Version 1.0, effective July 2026**. Exam details and policies can change, so candidates should download and read the latest guide from the Anthropic Partner Academy before registering or scheduling.

### Exam format

| Field | Official guide |
|---|---|
| Credential | Claude Certified Associate - Foundations |
| Exam code | `CCAO-F` |
| Number of items | 60 |
| Item format | Multiple-choice and multiple-response; each item states how many responses to select |
| Time limit | 120 minutes |
| Delivery | Proctored online and/or at a test center, according to program policy |
| Passing score | Scaled score of 720 on a scale of 100-1,000 |
| Exam fee | $99 USD |
| Credential validity | 12 months from the award date |
| Result reporting | Pass/fail, scaled score, and percent correct by domain |

### Exam blueprint and repository crosswalk

The official domain numbering differs from this repository's learning order. In particular, the material we studied first as **Module 1** maps to **Official Domain 3: Product and Model Selection**.

| Official domain | Content domain | Weight | Repository coverage |
|---:|---|---:|---|
| 1 | Prompting and Task Execution | 14% | [Module 2](modules/02-prompting-task-execution/) |
| 2 | Output Evaluation and Validation | 21% | [Module 3](modules/03-evaluating-validating-output/) |
| 3 | Product and Model Selection | 12% | [Module 1](modules/01-platform-model-foundations/) |
| 4 | Workflow Integration and Solution Design | 16% | [Module 4](modules/04-workflow-integration-solutions-design/) |
| 5 | Configuration and Knowledge Management | 12% | [Module 5](modules/05-configuration-knowledge-management/) |
| 6 | Governance, Risk, and Responsible Use | 15% | [Module 6](modules/06-governance-risk-responsible-use/) |
| 7 | Troubleshooting and Optimization | 10% | [Module 7](modules/07-troubleshooting-optimization/) |
|  | **Total** | **100%** |  |

### What the weighting means for preparation

- **Output Evaluation and Validation is the largest domain at 21%.** Be able to detect hallucinations, inconsistencies, bias, incomplete work, and unsupported claims, then choose the appropriate validation or human-review response.
- **Workflow Integration and Solution Design is 16%.** Practice translating business requirements into useful Claude-supported workflows and communicating value and limitations to stakeholders.
- **Governance, Risk, and Responsible Use is 15%.** Data sensitivity, privacy, organizational policy, appropriate-use judgment, and escalation are major exam themes.
- **Prompting and Task Execution is 14%.** Know how to structure, decompose, iterate, and adapt prompts for different task types.
- **Product and Model Selection and Configuration and Knowledge Management are each 12%.** Know when to use Chat, Projects, Research, Artifacts, model tiers, context strategies, instructions, knowledge sources, and connectors.
- **Troubleshooting and Optimization is 10%.** Diagnose weak prompts and outputs, adjust the correct layer, and optimize for effectiveness and efficiency.

The exam is scored against a total scaled passing standard. Domain percentages on the score report are diagnostic; they do not independently determine pass or fail. Build balanced readiness rather than ignoring the smaller domains.

### Candidate and scope boundary

The minimally qualified candidate is a professional Claude productivity user who can translate business objectives into effective interactions, configure Projects, evaluate and adapt outputs, recognize limitations, and escalate when necessary. The associate exam does **not** require API development, enterprise-scale agentic architecture, machine-learning engineering, or advanced software integration.

The [AI Systems Engineering Playbook](ai-systems-engineering/) deliberately extends beyond the minimum exam scope. It is an optional applied track for readers who want to turn the certification concepts into a broader engineering practice.

## The AI Systems Engineering method

Before writing a substantial prompt, work through these decisions:

```text
1. Define the business problem
           ↓
2. Choose the workspace
           ↓
3. Select the required capabilities
           ↓
4. Choose the minimum qualified model
           ↓
5. Design the context strategy
           ↓
6. Design the workflow and prompt
           ↓
7. Validate the output
           ↓
8. Deliver, monitor, and improve
```

Always ask:

1. Where should this work live?
2. What capabilities are actually needed?
3. What is the minimum qualified model?
4. How will context stay focused and current?
5. How will the output be verified?
6. What remains under human responsibility?

## What makes this repository different

- **Scenario first:** Questions test judgment, not trivia alone.
- **Workflow over prompts:** The system is designed before the final prompt is optimized.
- **Evidence driven:** Success criteria and evaluation are defined before optimization.
- **Vendor neutral engineering:** The methodology applies beyond any one model or product.
- **Separation of concerns:** Context, procedure, computation, continuity, authority, validation, and approval are designed independently.
- **Security conscious:** Examples emphasize prompt injection, source integrity, least privilege, sensitive-data handling, and controlled tool use.
- **Governed deployment:** Human accountability, monitoring, rollback, incident response, and retirement are part of solution design.
- **Version aware:** Volatile model names, pricing, limits, defaults, and product behavior are treated as dated implementation details.
- **Public-safe examples:** Scenarios are fictional, generic, synthetic, or based on public information.

## What is included

| Resource | Count | Purpose |
|---|---:|---|
| Study domains | 7 | Coverage of the certification preparation areas |
| Scenario questions | 56 | Original multiple-choice questions with rationales |
| Flashcards | 84 | Fast recall and spaced-repetition practice |
| Practice exams | 2 | Balanced, 28-question exam simulations |
| Hands-on labs | 7 | Applied exercises with acceptance criteria |
| Case studies | 4 | Certification cases plus an end-to-end systems-engineering example |
| Prompt notebooks and templates | Growing | Reusable task, evaluation, orchestration, and review patterns |
| Engineering pattern library | Growing | Reusable workflow and architecture patterns |
| AI Systems Engineering Playbook | 1 | Methodology, canvases, checklists, mental models, and case studies |
| Study CLI | 1 | Offline quizzes, flashcards, practice exams, and local score tracking |

## Certification study domains

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
4. Apply the lesson to the [AI Systems Engineering Playbook](ai-systems-engineering/).
5. Complete the module lab before viewing the model solution.
6. Drill the flashcards until recall is consistent.
7. Take the module quiz and explain why each distractor is weaker.
8. Record weak areas in the [progress tracker](docs/progress-tracker.md).
9. Revisit the current official documentation linked from that module.

After all seven domains, complete both practice exams under timed, closed-note conditions.

## AI Systems Engineering quick start

For a new professional project:

1. Define the outcome in the [AI Project Canvas](ai-systems-engineering/worksheets/ai-project-canvas.md).
2. Map stages and responsibilities in the [Workflow Design Canvas](ai-systems-engineering/worksheets/workflow-design-canvas.md).
3. Build the task contract in the [Prompt Planning Canvas](ai-systems-engineering/worksheets/prompt-planning-canvas.md).
4. Set the quality floor in the [Evaluation Canvas](ai-systems-engineering/worksheets/evaluation-canvas.md).
5. Review risk, authority, and accountability in the [Governance Canvas](ai-systems-engineering/worksheets/governance-canvas.md).
6. Run [Before You Prompt](ai-systems-engineering/checklists/before-you-prompt.md).
7. Review the [public-source executive briefing case study](ai-systems-engineering/case-studies/01-public-source-executive-briefing.md).
8. Use the [postmortem worksheet](ai-systems-engineering/worksheets/postmortem.md) after a pilot, release, or significant failure.

For a small, low-consequence task, use the compressed path:

```text
Outcome → Evidence → Workspace → Model → Prompt → Review
```

## Repository map

```text
.
├── ai-systems-engineering/   # Vendor-neutral methodology and worksheets
├── modules/                  # Seven certification study domains
├── prompts/                  # Prompt notebooks and reusable templates
├── patterns/                 # Engineering patterns
├── case-studies/             # Applied certification scenarios
├── practice-exams/           # Two full exam simulations
├── docs/                     # Study plan, strategy, cheat sheet, glossary
├── data/                     # Machine-readable questions and flashcards
├── tools/                    # Offline study CLI
├── scripts/                  # Validation and publishing helpers
└── tests/                    # Automated repository checks
```

## Repository quick start

The Markdown content can be used directly in GitHub. Python is needed only for the optional study CLI and validation tools.

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
- Explain the correct answer and every distractor without relying on memorized wording.
- Complete all seven labs and document your design decisions.
- Resolve every miss involving privacy, grounding, human review, tool permissions, or high-impact use.
- Verify product-specific facts against current official documentation before the exam.

## Key resources

- [AI Systems Engineering Playbook](ai-systems-engineering/)
- [AI Project Canvas](ai-systems-engineering/worksheets/ai-project-canvas.md)
- [Before You Prompt checklist](ai-systems-engineering/checklists/before-you-prompt.md)
- [Certification overview](docs/certification-overview.md)
- [Four-week study plan](docs/study-plan.md)
- [Exam strategy](docs/exam-strategy.md)
- [Master cheat sheet](docs/master-cheat-sheet.md)
- [Glossary](docs/glossary.md)
- [Official resources](docs/official-resources.md)
- [Progress tracker](docs/progress-tracker.md)
- [Practice exams](practice-exams/)
- [Prompt library](prompts/)
- [Engineering pattern library](patterns/)

## Contributing

Corrections and improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Contributions must remain original and must not disclose remembered, reconstructed, or proprietary exam content.

## License

Code and original written material in this repository are licensed under the [MIT License](LICENSE), subject to the third-party rights and disclaimer described in [DISCLAIMER.md](DISCLAIMER.md).