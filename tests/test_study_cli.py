from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import study_cli


class StudyDataTests(unittest.TestCase):
    def test_question_counts(self) -> None:
        questions = study_cli.load_questions()
        self.assertEqual(len(questions), 56)
        for domain in range(1, 8):
            self.assertEqual(
                sum(1 for question in questions if question["domain"] == domain),
                8,
            )

    def test_flashcard_counts(self) -> None:
        cards = study_cli.load_flashcards()
        self.assertEqual(len(cards), 84)
        for domain in range(1, 8):
            self.assertEqual(
                sum(1 for card in cards if card["domain"] == domain),
                12,
            )

    def test_exams_are_balanced_and_disjoint(self) -> None:
        questions = study_cli.load_questions()
        exam_one = study_cli.exam_questions(questions, 1)
        exam_two = study_cli.exam_questions(questions, 2)

        self.assertEqual(len(exam_one), 28)
        self.assertEqual(len(exam_two), 28)
        self.assertFalse(
            {question["id"] for question in exam_one}
            & {question["id"] for question in exam_two}
        )

        for exam in (exam_one, exam_two):
            for domain in range(1, 8):
                self.assertEqual(
                    sum(1 for question in exam if question["domain"] == domain),
                    4,
                )

    def test_seeded_selection_is_repeatable(self) -> None:
        questions = study_cli.load_questions()
        first = study_cli.select_questions(questions, domain=3, count=4, seed=17)
        second = study_cli.select_questions(questions, domain=3, count=4, seed=17)
        self.assertEqual(
            [question["id"] for question in first],
            [question["id"] for question in second],
        )

    def test_normalize_answer(self) -> None:
        self.assertEqual(study_cli.normalize_answer(" a "), "A")
        with self.assertRaises(ValueError):
            study_cli.normalize_answer("E")

    def test_progress_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "progress.json"
            result = {
                "timestamp": "2026-07-14T00:00:00+00:00",
                "mode": "test",
                "correct": 1,
                "total": 1,
                "percentage": 100.0,
                "by_domain": {"1": {"correct": 1, "total": 1}},
                "responses": [
                    {
                        "question_id": "M1-Q01",
                        "domain": 1,
                        "selected": "A",
                        "correct_answer": "A",
                        "correct": True,
                    }
                ],
            }
            study_cli.append_progress(path, result)
            loaded = study_cli.load_progress(path)
            self.assertEqual(len(loaded["sessions"]), 1)
            self.assertEqual(loaded["sessions"][0]["percentage"], 100.0)

    def test_invalid_json_raises_study_data_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(study_cli.StudyDataError):
                study_cli.load_json(path)


if __name__ == "__main__":
    unittest.main()
