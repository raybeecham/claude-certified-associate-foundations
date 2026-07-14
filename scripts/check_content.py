"""Validate repository study content and local Markdown links."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUESTION_PATH = ROOT / "data" / "questions.json"
FLASHCARD_PATH = ROOT / "data" / "flashcards.json"

EXPECTED_MODULES = [
    "01-platform-model-foundations",
    "02-prompting-task-execution",
    "03-evaluating-validating-output",
    "04-workflow-integration-solutions-design",
    "05-configuration-knowledge-management",
    "06-governance-risk-responsible-use",
    "07-troubleshooting-optimization",
]

REQUIRED_MODULE_FILES = {
    "README.md",
    "notes.md",
    "lab.md",
    "quiz.md",
    "flashcards.md",
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def load_list(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise AssertionError(f"{path} must contain a JSON list")
    return data


def validate_questions(questions: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if len(questions) != 56:
        errors.append(f"Expected 56 questions, found {len(questions)}")

    ids = [str(question.get("id", "")) for question in questions]
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate question IDs: {duplicates}")

    counts = Counter(question.get("domain") for question in questions)
    for domain in range(1, 8):
        if counts[domain] != 8:
            errors.append(
                f"Domain {domain} must have 8 questions, found {counts[domain]}"
            )

    required = {
        "id",
        "domain",
        "objective",
        "difficulty",
        "scenario",
        "options",
        "answer",
        "rationale",
        "distractor_rationales",
        "source",
    }
    for question in questions:
        qid = question.get("id", "<missing>")
        missing = required - set(question)
        if missing:
            errors.append(f"{qid}: missing fields {sorted(missing)}")
            continue

        if set(question["options"]) != {"A", "B", "C", "D"}:
            errors.append(f"{qid}: options must be A, B, C, and D")
        if question["answer"] not in {"A", "B", "C", "D"}:
            errors.append(f"{qid}: invalid answer {question['answer']}")
        expected_distractors = {"A", "B", "C", "D"} - {question["answer"]}
        if set(question["distractor_rationales"]) != expected_distractors:
            errors.append(f"{qid}: distractor rationale keys do not match")
        if not str(question["source"]).startswith("https://"):
            errors.append(f"{qid}: source must be an HTTPS URL")
    return errors


def validate_flashcards(cards: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if len(cards) != 84:
        errors.append(f"Expected 84 flashcards, found {len(cards)}")

    ids = [str(card.get("id", "")) for card in cards]
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate flashcard IDs: {duplicates}")

    counts = Counter(card.get("domain") for card in cards)
    for domain in range(1, 8):
        if counts[domain] != 12:
            errors.append(
                f"Domain {domain} must have 12 flashcards, found {counts[domain]}"
            )

    for card in cards:
        for field in ("id", "domain", "front", "back"):
            if not card.get(field):
                errors.append(f"{card.get('id', '<missing>')}: missing {field}")
    return errors


def validate_modules() -> list[str]:
    errors: list[str] = []
    module_root = ROOT / "modules"
    for module in EXPECTED_MODULES:
        path = module_root / module
        if not path.is_dir():
            errors.append(f"Missing module directory: {path.relative_to(ROOT)}")
            continue
        files = {item.name for item in path.iterdir() if item.is_file()}
        missing = REQUIRED_MODULE_FILES - files
        if missing:
            errors.append(
                f"{path.relative_to(ROOT)} missing files: {sorted(missing)}"
            )
    return errors


def clean_link_target(target: str) -> str:
    target = target.strip().split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.split("#", 1)[0].split("?", 1)[0]


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = clean_link_target(raw_target)
            if not target:
                continue
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            if target.startswith("/"):
                errors.append(
                    f"{markdown.relative_to(ROOT)}: absolute local link {target}"
                )
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{markdown.relative_to(ROOT)}: link leaves repository: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{markdown.relative_to(ROOT)}: missing link target {target}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        questions = load_list(QUESTION_PATH)
        cards = load_list(FLASHCARD_PATH)
    except (OSError, json.JSONDecodeError, AssertionError) as exc:
        print(f"Content validation failed: {exc}", file=sys.stderr)
        return 1

    errors.extend(validate_questions(questions))
    errors.extend(validate_flashcards(cards))
    errors.extend(validate_modules())
    errors.extend(validate_local_links())

    if errors:
        print("Content validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Content validation passed.")
    print("- 7 modules")
    print("- 56 questions")
    print("- 84 flashcards")
    print("- local Markdown links resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
