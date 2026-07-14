# Contributing

Thank you for helping improve this independent study resource.

## Acceptable contributions

- Factual corrections supported by current official documentation
- Clearer explanations and examples
- New original scenario questions
- New original labs or case studies
- Accessibility and navigation improvements
- CLI, test, or automation improvements
- Broken-link and formatting fixes

## Prohibited contributions

Do not submit:

- recalled, reconstructed, leaked, purchased, or copied certification questions;
- proprietary preparation-course text, screenshots, transcripts, or answer keys;
- content that represents itself as an official exam blueprint without a public source;
- credentials, secrets, personal data, controlled data, or confidential organizational material; or
- unlicensed third-party content.

## Question quality standard

A strong multiple-choice question:

1. tests one primary objective;
2. uses a realistic scenario;
3. has one defensible best answer;
4. uses plausible distractors;
5. avoids trivia that becomes obsolete quickly;
6. explains why the correct answer is best;
7. explains why every distractor is weaker; and
8. cites an official source when the rationale depends on current product behavior.

See [docs/question-writing-guide.md](docs/question-writing-guide.md).

## Workflow

1. Create a focused branch.
2. Make the smallest coherent change.
3. Run:

   ```bash
   python scripts/check_content.py
   python -m unittest discover -s tests -v
   ```

4. Open a pull request with:
   - the problem being solved;
   - a summary of the change;
   - validation performed; and
   - source links for factual updates.

## Style

- Use clear Markdown headings.
- Prefer concise sentences and concrete examples.
- Distinguish stable concepts from current product details.
- Use “Claude” and “Anthropic” accurately.
- Avoid promotional claims.
- Avoid em dashes.
- Do not imply official endorsement.
