# Repository Manifest

Generated: **July 14, 2026**

## Build summary

| Item | Value |
|---|---:|
| Study domains | 7 |
| Original scenario questions | 56 |
| Flashcards | 84 |
| Practice exams | 2 |
| Applied labs | 7 |
| Case studies | 3 |
| Prompt templates | 7 |
| Markdown files before this manifest | 76 |
| Approximate Markdown words | 45,070 |
| Files before this manifest | 101 |

## Top-level structure

```text
.
├── README.md
├── docs/                    # Study plan, strategy, cheat sheet, glossary
├── modules/                 # Seven domains, each with notes, lab, cards, quiz
├── practice-exams/          # Two balanced exams and detailed rationales
├── prompts/                 # Reusable prompt and workflow templates
├── case-studies/            # PQC, policy, and incident-triage scenarios
├── data/                    # Machine-readable questions and flashcards
├── tools/                   # Offline study CLI
├── scripts/                 # Validation and GitHub publishing
├── tests/                   # Standard-library unit tests
└── .github/                 # CI, documentation, issue, and PR automation
```

## Validation performed

```bash
python scripts/check_content.py
python -m unittest discover -s tests -v
python -m compileall -q tools scripts tests
bash -n scripts/publish.sh
mkdocs build --strict
python -m pip install -e . --no-deps --no-build-isolation
claude-study domains
```

Validated results:

- content checker passed;
- all seven unit tests passed;
- Python compilation passed;
- Bash publishing script syntax passed;
- documentation build passed;
- editable package installation passed; and
- CLI smoke test passed.

## Publication target

```text
https://github.com/raybeecham/claude-certified-associate-foundations
```

Use either publishing script after installing and authenticating the GitHub CLI:

```bash
./scripts/publish.sh
```

```powershell
.\scripts\publish.ps1
```

## Content status

The material is independent and unofficial. Product-specific facts should be rechecked against current official documentation. No proprietary course or live-exam content is included.
