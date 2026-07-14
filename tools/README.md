# Study CLI

The CLI is intentionally offline and uses only the Python standard library.

## Commands

```bash
python -m tools.study_cli domains
python -m tools.study_cli quiz --domain 2 --questions 8
python -m tools.study_cli quiz --questions 14 --seed 42
python -m tools.study_cli flashcards --domain 6 --limit 12
python -m tools.study_cli practice --exam 1
python -m tools.study_cli stats
```

## Progress data

By default, progress is stored in:

```text
.study-progress.json
```

The file is excluded from Git. It contains quiz responses and the latest recorded flashcard rating. It does not call an external service.

Use a different file:

```bash
python -m tools.study_cli --progress ~/private/claude-study.json stats
```

Global options such as `--progress` appear before the subcommand.

## Exit codes

- `0`: success
- `2`: invalid input or study data
- `130`: cancelled with Ctrl+C
