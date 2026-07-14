# Study Data

Machine-readable study content used by the offline CLI.

## Files

- `questions.json`: 56 original multiple-choice questions, eight per domain
- `flashcards.json`: 84 flashcards, twelve per domain

## Stability

Question IDs and flashcard IDs are intended to remain stable. Corrections should update content without reusing an ID for a different objective.

## Data integrity

Run:

```bash
python scripts/check_content.py
```

The checker validates counts, IDs, answer keys, distractor rationales, module structure, and local Markdown links.

## Licensing and exam integrity

The records are original educational material under the repository license. Do not add proprietary course text or recalled live-exam questions.
