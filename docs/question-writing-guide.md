# Question-Writing Guide

Use this guide for community contributions and personal practice.

## Anatomy of a strong question

### 1. Objective

Name the single concept being tested.

Example: Select the best first step when a grounded summarization system invents unsupported claims.

### 2. Scenario

Provide enough context to make the decision meaningful:

- intended outcome;
- available evidence;
- operational constraint;
- observed failure; and
- relevant risk.

Avoid irrelevant story details.

### 3. Options

Create four options:

- one best answer;
- one technically possible but incomplete answer;
- one answer aimed at the wrong layer;
- one answer that creates a risk or unnecessary complexity.

Do not use joke answers.

### 4. Rationale

Explain:

- why the correct answer directly addresses the scenario;
- why each distractor is weaker;
- which facts would change the answer; and
- which stable principle the question tests.

### 5. Metadata

Each JSON question contains:

```json
{
  "id": "M3-Q01",
  "domain": 3,
  "objective": "Evaluation design",
  "difficulty": "medium",
  "scenario": "Question text",
  "options": {
    "A": "Option A",
    "B": "Option B",
    "C": "Option C",
    "D": "Option D"
  },
  "answer": "B",
  "rationale": "Why B is best",
  "distractor_rationales": {
    "A": "Why A is weaker",
    "C": "Why C is weaker",
    "D": "Why D is weaker"
  },
  "source": "Official public documentation URL"
}
```

## Avoiding accidental exam dumps

Do not contribute a question because it resembles one seen on a live exam. Build from public learning objectives and your own scenario.

Red flags include:

- “I remember this exact wording”;
- unusual names, numbers, or option order from an exam;
- reconstructed answer choices;
- screenshots or notes taken during a test; and
- claims that a question is “guaranteed to appear.”

Replace such material with a new scenario that tests the underlying public concept.

## Review checklist

- [ ] One primary objective
- [ ] One defensible best answer
- [ ] Plausible distractors
- [ ] No volatile trivia unless explicitly sourced
- [ ] Complete rationale
- [ ] No proprietary material
- [ ] Appropriate data and security handling
- [ ] Clear grammar and accessible wording
