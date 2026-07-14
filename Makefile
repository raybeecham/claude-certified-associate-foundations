.PHONY: check test quiz flashcards docs

check:
	python scripts/check_content.py

test:
	python -m unittest discover -s tests -v

quiz:
	python -m tools.study_cli quiz --questions 10

flashcards:
	python -m tools.study_cli flashcards --limit 10

docs:
	mkdocs serve
