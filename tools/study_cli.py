"""Offline study CLI for the Claude Foundations study guide.

No third-party dependencies are required. Progress is stored locally in
.study-progress.json and is excluded from Git by default.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
DEFAULT_PROGRESS_PATH = REPO_ROOT / ".study-progress.json"

DOMAIN_NAMES = {
    1: "Claude Platform & Model Foundations",
    2: "Prompting & Task Execution",
    3: "Evaluating & Validating Claude's Output",
    4: "Workflow Integration & Solutions Design",
    5: "Configuration & Knowledge Management",
    6: "Governance, Risk & Responsible Use",
    7: "Troubleshooting & Optimization",
}


class StudyDataError(RuntimeError):
    """Raised when repository study data is missing or invalid."""


def load_json(path: Path) -> list[dict[str, Any]]:
    """Load a JSON list and provide an actionable error on failure."""
    try:
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except FileNotFoundError as exc:
        raise StudyDataError(f"Study data file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise StudyDataError(f"Invalid JSON in {path}: {exc}") from exc

    if not isinstance(data, list):
        raise StudyDataError(f"Expected a JSON list in {path}")
    return data


def load_questions() -> list[dict[str, Any]]:
    return load_json(DATA_DIR / "questions.json")


def load_flashcards() -> list[dict[str, Any]]:
    return load_json(DATA_DIR / "flashcards.json")


def parse_domain(value: str) -> int:
    """Argparse validator for domain numbers."""
    try:
        domain = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("domain must be an integer from 1 to 7") from exc
    if domain not in DOMAIN_NAMES:
        raise argparse.ArgumentTypeError("domain must be an integer from 1 to 7")
    return domain


def select_questions(
    questions: Sequence[dict[str, Any]],
    domain: int | None,
    count: int,
    seed: int | None = None,
) -> list[dict[str, Any]]:
    """Filter and sample questions without modifying the source list."""
    pool = [q for q in questions if domain is None or q.get("domain") == domain]
    if not pool:
        raise StudyDataError("No questions matched the selected domain.")
    if count <= 0:
        raise ValueError("Question count must be greater than zero.")

    rng = random.Random(seed)
    count = min(count, len(pool))
    return rng.sample(pool, count)


def exam_questions(
    questions: Sequence[dict[str, Any]], exam_number: int
) -> list[dict[str, Any]]:
    """Return the same balanced question set used by the Markdown exams."""
    if exam_number not in (1, 2):
        raise ValueError("Practice exam must be 1 or 2.")

    selected: list[dict[str, Any]] = []
    start = 0 if exam_number == 1 else 4
    for offset in range(start, start + 4):
        for domain in range(1, 8):
            domain_questions = sorted(
                (q for q in questions if q.get("domain") == domain),
                key=lambda item: str(item.get("id", "")),
            )
            if len(domain_questions) != 8:
                raise StudyDataError(
                    f"Domain {domain} must contain exactly 8 questions; "
                    f"found {len(domain_questions)}."
                )
            selected.append(domain_questions[offset])
    return selected


def normalize_answer(value: str) -> str:
    """Normalize one multiple-choice answer."""
    answer = value.strip().upper()
    if answer not in {"A", "B", "C", "D"}:
        raise ValueError("Enter A, B, C, or D.")
    return answer


def prompt_answer() -> str:
    while True:
        try:
            return normalize_answer(input("Your answer [A-D]: "))
        except ValueError as exc:
            print(exc)


def print_question(question: dict[str, Any], number: int, total: int) -> None:
    print(f"\n[{number}/{total}] {question['scenario']}\n")
    for letter in "ABCD":
        print(f"  {letter}. {question['options'][letter]}")


def run_question_session(
    selected: Sequence[dict[str, Any]],
    mode: str,
    progress_path: Path,
    save: bool = True,
) -> dict[str, Any]:
    """Run an interactive question session and return a result record."""
    correct = 0
    by_domain: dict[int, dict[str, int]] = defaultdict(
        lambda: {"correct": 0, "total": 0}
    )
    responses: list[dict[str, Any]] = []

    for index, question in enumerate(selected, 1):
        print_question(question, index, len(selected))
        answer = prompt_answer()
        expected = str(question["answer"]).upper()
        is_correct = answer == expected

        domain = int(question["domain"])
        by_domain[domain]["total"] += 1
        if is_correct:
            correct += 1
            by_domain[domain]["correct"] += 1
            print("\nCorrect.")
        else:
            print(f"\nIncorrect. Correct answer: {expected}")

        print(f"Rationale: {question['rationale']}")
        if not is_correct:
            selected_reason = question["distractor_rationales"].get(answer)
            if selected_reason:
                print(f"Why {answer} is weaker: {selected_reason}")

        responses.append(
            {
                "question_id": question["id"],
                "domain": domain,
                "selected": answer,
                "correct_answer": expected,
                "correct": is_correct,
            }
        )

    percentage = round((correct / len(selected)) * 100, 1)
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "correct": correct,
        "total": len(selected),
        "percentage": percentage,
        "by_domain": {
            str(domain): values for domain, values in sorted(by_domain.items())
        },
        "responses": responses,
    }

    print("\n" + "=" * 64)
    print(f"Score: {correct}/{len(selected)} ({percentage:.1f}%)")
    for domain, values in sorted(by_domain.items()):
        domain_pct = (values["correct"] / values["total"]) * 100
        print(
            f"  Domain {domain}: {values['correct']}/{values['total']} "
            f"({domain_pct:.1f}%) | {DOMAIN_NAMES[domain]}"
        )

    if save:
        append_progress(progress_path, result)
        print(f"\nSaved locally to: {progress_path}")

    return result


def load_progress(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "sessions": [], "flashcards": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StudyDataError(f"Invalid progress file {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise StudyDataError(f"Invalid progress structure in {path}")
    data.setdefault("version", 1)
    data.setdefault("sessions", [])
    data.setdefault("flashcards", {})
    return data


def save_progress(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    temp_path.replace(path)


def append_progress(path: Path, result: dict[str, Any]) -> None:
    data = load_progress(path)
    sessions = data.setdefault("sessions", [])
    if not isinstance(sessions, list):
        raise StudyDataError("Progress file sessions field must be a list.")
    sessions.append(result)
    save_progress(path, data)


def command_domains(_: argparse.Namespace) -> int:
    questions = load_questions()
    cards = load_flashcards()
    print("Claude Foundations study domains\n")
    for domain, name in DOMAIN_NAMES.items():
        q_count = sum(1 for q in questions if q.get("domain") == domain)
        c_count = sum(1 for c in cards if c.get("domain") == domain)
        print(f"{domain}. {name}")
        print(f"   {q_count} questions | {c_count} flashcards")
    return 0


def command_quiz(args: argparse.Namespace) -> int:
    questions = load_questions()
    selected = select_questions(
        questions, domain=args.domain, count=args.questions, seed=args.seed
    )
    mode = f"quiz-domain-{args.domain}" if args.domain else "quiz-mixed"
    run_question_session(
        selected, mode=mode, progress_path=args.progress, save=not args.no_save
    )
    return 0


def command_practice(args: argparse.Namespace) -> int:
    selected = exam_questions(load_questions(), args.exam)
    print(
        f"Practice Exam {args.exam}: {len(selected)} questions, "
        "four from each domain."
    )
    run_question_session(
        selected,
        mode=f"practice-exam-{args.exam}",
        progress_path=args.progress,
        save=not args.no_save,
    )
    return 0


def select_cards(
    cards: Sequence[dict[str, Any]],
    domain: int | None,
    limit: int,
    seed: int | None,
) -> list[dict[str, Any]]:
    pool = [card for card in cards if domain is None or card.get("domain") == domain]
    if not pool:
        raise StudyDataError("No flashcards matched the selected domain.")
    if limit <= 0:
        raise ValueError("Flashcard limit must be greater than zero.")
    rng = random.Random(seed)
    return rng.sample(pool, min(limit, len(pool)))


def command_flashcards(args: argparse.Namespace) -> int:
    cards = select_cards(
        load_flashcards(), domain=args.domain, limit=args.limit, seed=args.seed
    )
    data = load_progress(args.progress)
    ratings = data.setdefault("flashcards", {})
    if not isinstance(ratings, dict):
        raise StudyDataError("Progress file flashcards field must be an object.")

    for index, card in enumerate(cards, 1):
        print("\n" + "=" * 64)
        print(
            f"[{index}/{len(cards)}] {card['id']} | "
            f"Domain {card['domain']}: {DOMAIN_NAMES[int(card['domain'])]}"
        )
        print(f"\nFront: {card['front']}")
        if not args.show_answers:
            input("\nPress Enter to reveal the answer...")
        print(f"\nBack: {card['back']}")

        if not args.no_save:
            while True:
                rating = input(
                    "\nRate recall: 0=missed, 1=hard, 2=good, 3=easy "
                    "(Enter to skip): "
                ).strip()
                if rating == "":
                    break
                if rating in {"0", "1", "2", "3"}:
                    ratings[card["id"]] = {
                        "rating": int(rating),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    }
                    break
                print("Enter 0, 1, 2, 3, or press Enter to skip.")

    if not args.no_save:
        save_progress(args.progress, data)
        print(f"\nSaved locally to: {args.progress}")
    return 0


def weighted_domain_stats(
    sessions: Iterable[dict[str, Any]],
) -> dict[int, dict[str, int]]:
    totals: dict[int, dict[str, int]] = defaultdict(
        lambda: {"correct": 0, "total": 0}
    )
    for session in sessions:
        for response in session.get("responses", []):
            try:
                domain = int(response["domain"])
            except (KeyError, TypeError, ValueError):
                continue
            totals[domain]["total"] += 1
            if response.get("correct") is True:
                totals[domain]["correct"] += 1
    return totals


def command_stats(args: argparse.Namespace) -> int:
    data = load_progress(args.progress)
    sessions = data.get("sessions", [])
    if not sessions:
        print(f"No saved quiz sessions found in {args.progress}")
    else:
        print(f"Saved sessions: {len(sessions)}")
        for session in sessions[-10:]:
            print(
                f"- {session.get('timestamp', 'unknown')} | "
                f"{session.get('mode', 'unknown')} | "
                f"{session.get('correct', 0)}/{session.get('total', 0)} "
                f"({session.get('percentage', 0)}%)"
            )

        print("\nCumulative performance by domain:")
        totals = weighted_domain_stats(sessions)
        for domain in range(1, 8):
            values = totals.get(domain, {"correct": 0, "total": 0})
            if values["total"]:
                percentage = (values["correct"] / values["total"]) * 100
                score = f"{values['correct']}/{values['total']} ({percentage:.1f}%)"
            else:
                score = "No attempts"
            print(f"{domain}. {DOMAIN_NAMES[domain]}: {score}")

    flashcards = data.get("flashcards", {})
    if flashcards:
        counts = defaultdict(int)
        for record in flashcards.values():
            if isinstance(record, dict):
                counts[int(record.get("rating", -1))] += 1
        print("\nLatest flashcard ratings:")
        print(f"  Missed: {counts[0]}")
        print(f"  Hard:   {counts[1]}")
        print(f"  Good:   {counts[2]}")
        print(f"  Easy:   {counts[3]}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="claude-study",
        description="Offline study CLI for the Claude Foundations guide.",
    )
    parser.add_argument(
        "--progress",
        type=Path,
        default=DEFAULT_PROGRESS_PATH,
        help=f"Local progress file (default: {DEFAULT_PROGRESS_PATH})",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    domains_parser = subparsers.add_parser("domains", help="List study domains")
    domains_parser.set_defaults(func=command_domains)

    quiz_parser = subparsers.add_parser("quiz", help="Run a module or mixed quiz")
    quiz_parser.add_argument("--domain", type=parse_domain)
    quiz_parser.add_argument("--questions", type=int, default=10)
    quiz_parser.add_argument("--seed", type=int)
    quiz_parser.add_argument("--no-save", action="store_true")
    quiz_parser.set_defaults(func=command_quiz)

    practice_parser = subparsers.add_parser(
        "practice", help="Run a balanced 28-question practice exam"
    )
    practice_parser.add_argument("--exam", type=int, choices=(1, 2), required=True)
    practice_parser.add_argument("--no-save", action="store_true")
    practice_parser.set_defaults(func=command_practice)

    flashcard_parser = subparsers.add_parser(
        "flashcards", help="Review flashcards"
    )
    flashcard_parser.add_argument("--domain", type=parse_domain)
    flashcard_parser.add_argument("--limit", type=int, default=10)
    flashcard_parser.add_argument("--seed", type=int)
    flashcard_parser.add_argument("--show-answers", action="store_true")
    flashcard_parser.add_argument("--no-save", action="store_true")
    flashcard_parser.set_defaults(func=command_flashcards)

    stats_parser = subparsers.add_parser("stats", help="Show local progress")
    stats_parser.set_defaults(func=command_stats)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (StudyDataError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nSession cancelled.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
