# Lesson 5A: Adapting Strategy by Task Type

## Overview

The same component stack applies to every meaningful prompt, but the emphasis changes with the task.

An analysis prompt should constrain judgment. A research prompt should control scope and sources. A drafting prompt should define the reader and communication shape while leaving room for phrasing. A brainstorming prompt should protect divergence rather than eliminate it prematurely.

> Prompt quality depends not only on what components are present, but on how tightly each component is specified for the task type.

This lesson focuses on four certification task types:

1. analysis;
2. research;
3. drafting; and
4. brainstorming.

## Learning objectives

After completing this lesson, you should be able to:

- identify the dominant task type in a request;
- decide where the prompt needs control and where it needs latitude;
- tighten criteria, sources, tone, format, or guardrails according to task type;
- recognize when one request contains several task types and should be decomposed;
- distinguish current-information research from analysis of supplied sources;
- specify citation and verification behavior for grounded research;
- preserve useful creative range during brainstorming; and
- diagnose task-strategy mismatch.

## The control-latitude dial

Prompting strategy is a design decision about **where the model must conform** and **where the model may explore**.

```text
More control                                      More latitude
|------------------------------------------------------------|
Analysis        Research          Drafting         Brainstorming
```

This is not an absolute ranking. A tightly regulated draft may require more control than a preliminary analysis. The diagram shows the normal starting posture.

### Control means

- explicit criteria;
- bounded scope;
- defined sources;
- required fields;
- prohibited assumptions;
- validation rules; and
- narrow uncertainty behavior.

### Latitude means

- freedom in phrasing;
- freedom in organization;
- multiple possible directions;
- range of ideas;
- alternative framing; and
- creative synthesis.

The design question is:

> Which parts must be reliable and repeatable, and which parts benefit from variation?

## Strategy quick reference

| Task type | Tighten | Loosen | Primary risk |
|---|---|---|---|
| Analysis | Criteria, standards, evidence, scope, ambiguity handling | Phrasing | Unsupported or inconsistent judgment |
| Research | Question, time boundary, source requirements, citations, uncertainty | Synthesis approach | Stale, weak, or unverifiable claims |
| Drafting | Audience, purpose, tone, length, structure, factual boundaries | Word choice and sentence construction | Polished but unusable communication |
| Brainstorming | Goal, hard guardrails, requested range | Quantity, direction, novelty | Premature convergence and repetitive ideas |

## Strategy 1: Analysis

Analysis converts evidence into structured judgment.

### Tighten

- the question being answered;
- evaluation criteria;
- comparison standard or baseline;
- evidence Claude may use;
- scope and exclusions;
- treatment of missing or conflicting evidence;
- output categories; and
- required rationale.

### Loosen

- prose style;
- wording of explanations; and
- organization within the required analytical structure.

### Recommended structure

```text
Objective
  + evidence set
  + analytical criteria
  + comparison standard
  + ambiguity behavior
  + output structure
  + validation requirement
```

### Mini-demo

```text
Compare the two supplied agreements on:
1. payment terms;
2. termination rights; and
3. liability caps.

Use only the supplied agreements.

For each criterion:
- identify the relevant clause in each agreement;
- explain the practical difference;
- state which position is more favorable to the buyer; and
- mark the result `unclear` when the documents do not support a conclusion.

Return a three-row table with columns for Criterion, Agreement A, Agreement B, Practical Difference, and Assessment.
```

### Why it works

The prompt defines what to compare, what evidence is permitted, how to handle ambiguity, and how to structure the result. It does not waste constraints on sentence-level phrasing.

### Analysis anti-patterns

- “Analyze this” with no analytical question;
- asking for a recommendation before criteria are agreed;
- allowing the model to invent missing facts;
- mixing extraction and judgment without separating them;
- using self-reported confidence as the only quality signal; and
- asking prose generation to perform consequential arithmetic.

## Strategy 2: Research

Research locates, evaluates, and synthesizes evidence that is not already fully supplied.

### Tighten

- the research question;
- date or currency boundary;
- geographic or organizational scope;
- source classes and authority hierarchy;
- inclusion and exclusion rules;
- citation requirements;
- treatment of conflicting sources; and
- missing-information behavior.

### Loosen

- the order in which sources are investigated;
- synthesis approach;
- follow-up query selection; and
- organization of evidence before the final output contract.

### Decide whether current retrieval is required

Ask:

1. Can the answer be supported entirely by supplied sources?
2. Does the question depend on events, prices, rules, releases, or facts that may have changed?
3. Is this a quick current-information lookup or a deep multi-source investigation?

Use supplied documents when they are the intended evidence set. Use web search for lighter current-information needs. Use Research when the task requires deeper, multi-step investigation across several sources or angles.

### Current product note, verified July 24, 2026

Anthropic's current Help Center describes web search as a live-web grounding feature that returns source citations and can gather information from multiple sources. It also describes Research as a paid-plan feature that performs deeper, multi-step investigation and requires web search to be enabled. Product availability and controls can change, so verify current documentation and workspace settings before relying on them.

### Mini-demo

```text
Research how the following three named competitors positioned product launches announced between April 1 and June 30, 2026.

Requirements:
- use current web sources;
- prioritize official company announcements and primary materials;
- use reputable independent reporting to add context;
- separate product claims from independently supported observations;
- cite every material claim;
- note publication date and event date when they differ;
- flag any statement that cannot be verified; and
- summarize common themes, differences, and strategic implications.

Return:
1. a source table;
2. one section per competitor;
3. a cross-competitor comparison; and
4. a verification-gaps section.
```

### Citation discipline

Citations are useful only when they point to actual grounded sources that support the claim.

```text
Grounded source citation -> inspectable evidence
Citation generated from memory alone -> plausible text, not proof
```

For consequential work:

- open the cited source;
- confirm the claim is supported;
- check date, scope, and authority;
- distinguish primary from secondary sources; and
- record unresolved conflicts.

### Research anti-patterns

- relying on training memory for recent facts;
- asking for “citations” without providing or retrieving sources;
- treating every search result as equally authoritative;
- ignoring event dates and publication dates;
- silently combining conflicting sources;
- presenting inference as fact; and
- using deep Research for a question that one authoritative source answers directly.

## Strategy 3: Drafting

Drafting translates known content into communication for a specific audience and purpose.

### Tighten

- audience;
- communication purpose;
- decision or action expected from the reader;
- factual inputs;
- tone;
- length;
- format;
- required points;
- prohibited claims; and
- approval or disclosure language when needed.

### Loosen

- word choice;
- sentence rhythm;
- transitions;
- rhetorical framing; and
- exact phrasing, unless policy or legal language must be preserved.

### Mini-demo

```text
Draft a 150-word LinkedIn post announcing the new reporting feature.

Audience:
Operations managers responsible for month-end reporting.

Purpose:
Explain the practical benefit and encourage readers to view the product update.

Required facts:
- the feature consolidates reporting status in one view;
- it reduces manual follow-up; and
- it is available now.

Tone:
Confident and practical, not salesy.

Format:
- opening sentence that names the problem;
- two short paragraphs;
- one closing call to action;
- no hashtags; and
- no unsupported performance claims.
```

### Why it works

The prompt controls what must be communicated and how the reader should experience it, while leaving Claude room to find natural language.

### Drafting anti-patterns

- specifying tone without naming the audience;
- asking for “professional” without defining purpose;
- providing no factual boundary;
- over-prescribing every sentence;
- mixing brainstorming, fact-finding, and final drafting in one step; and
- polishing language before the underlying content is approved.

## Strategy 4: Brainstorming

Brainstorming generates range before selection.

### Tighten

- the goal;
- the problem space;
- non-negotiable boundaries;
- prohibited or inappropriate directions;
- requested number of ideas; and
- dimensions of variety.

### Loosen

- direction;
- originality;
- framing;
- combinations;
- examples; and
- preliminary feasibility, unless an idea violates a hard constraint.

### Diverge before converging

```text
Phase 1: Generate range
          ↓
Phase 2: Group and inspect
          ↓
Phase 3: Apply criteria
          ↓
Phase 4: Select and develop
```

Do not ask Claude to generate, criticize, rank, and eliminate ideas in the same first pass. Early evaluation encourages safe, repetitive answers.

### Mini-demo

```text
Generate 20 distinct campaign angles around faster month-end close.

Goal:
Create a broad pool of concepts for an operations audience.

Guardrails:
- do not make numerical performance claims;
- avoid fear-based messaging; and
- keep every idea relevant to finance or operations teams.

Range requirements:
Include ideas based on time savings, visibility, reduced follow-up, team coordination, confidence, and executive reporting.

For this round, do not rank, reject, or refine the ideas. Return a numbered list with a one-sentence explanation for each.
```

### Why it works

The prompt protects the creative phase from premature convergence while still keeping the ideas inside useful boundaries.

### Brainstorming anti-patterns

- specifying too many evaluation criteria before ideation;
- asking for only three ideas and expecting variety;
- asking the model to self-edit immediately;
- accepting twenty paraphrases as twenty distinct concepts;
- omitting hard safety, brand, or scope boundaries; and
- treating brainstormed ideas as validated recommendations.

## Hybrid tasks need decomposition

Many professional requests contain several task types.

Example:

```text
Research the market, analyze the findings, brainstorm options, and draft a recommendation.
```

This should normally become:

```text
Stage 1: Research and build an evidence set
          ↓
Stage 2: Validate and analyze the evidence
          ↓
Stage 3: Brainstorm options within approved constraints
          ↓
Stage 4: Evaluate the options against criteria
          ↓
Stage 5: Draft the recommendation for the audience
```

Each stage uses a different control-latitude strategy.

| Stage | Dominant task type | Primary control |
|---|---|---|
| Find evidence | Research | Sources and scope |
| Interpret evidence | Analysis | Criteria and ambiguity handling |
| Generate options | Brainstorming | Goal and guardrails |
| Communicate decision | Drafting | Audience, tone, and format |

## Diagnosing task-strategy mismatch

| Symptom | Likely mismatch | Repair |
|---|---|---|
| Analysis is vague and opinionated | Too much latitude | Add criteria, evidence, and ambiguity rules |
| Research is current but unreliable | Source discipline is weak | Define authority, citations, dates, and verification |
| Draft is stiff or unnatural | Too much phrasing control | Preserve facts and structure, loosen word choice |
| Brainstorm is repetitive | Too many early constraints or too little requested range | Increase volume and diversity dimensions |
| Brainstorm is unusable | Too little guardrail control | Add scope, audience, safety, or feasibility boundaries |
| One prompt produces shallow work across several modes | Hybrid task was not decomposed | Separate research, analysis, ideation, and drafting stages |

## A reusable strategy-selection sequence

Before prompting, ask:

1. What is the dominant task type?
2. What must be controlled for the result to be valid?
3. Where would variation improve the result?
4. What evidence is required?
5. What should Claude do when evidence is missing?
6. Does the request combine task types that should be decomposed?
7. How will the output be evaluated?

## Knowledge check

### Question 1

A team wants 30 distinct ideas before deciding what is feasible. Which strategy is strongest?

- A. Specify ten evaluation criteria and ask Claude to rank ideas while generating them.
- B. Define the goal and hard guardrails, request volume and range, and defer ranking.
- C. Ask for the single most practical idea.
- D. Use a rigid three-row table.

**Answer:** B. Brainstorming needs protected divergence before convergence.

### Question 2

A user asks for an analysis of two reports, but the response makes unsupported judgments. What is the best first repair?

- A. Ask for a more confident answer.
- B. Add a creative role.
- C. Define the criteria, evidence boundary, and ambiguity behavior.
- D. Increase the word count.

**Answer:** C. Analysis quality depends on explicit criteria and evidence discipline.

### Question 3

A question depends on announcements from the last 30 days. What should the prompt establish?

- A. Current-source retrieval, time boundaries, authority preferences, and citations.
- B. A fictional expert role only.
- C. A longer response.
- D. No source requirements so synthesis remains creative.

**Answer:** A. Currency and source discipline are core research requirements.

### Question 4

A draft contains every required fact but reads mechanically. What is the most targeted repair?

- A. Replace the entire workflow.
- B. Preserve the facts, audience, tone, and format, but loosen sentence-level phrasing constraints.
- C. Add five more required sections.
- D. Convert the task into Research.

**Answer:** B. Drafting often benefits from controlled shape and flexible wording.

## Flashcards

### Flashcard 1

**Q:** What changes across analysis, research, drafting, and brainstorming if the component stack remains the same?

**A:** The balance between control and creative latitude.

### Flashcard 2

**Q:** What should be tightest in an analysis prompt?

**A:** Criteria, standards, evidence, scope, and ambiguity handling.

### Flashcard 3

**Q:** What should be tightest in a research prompt?

**A:** The research question, source discipline, time boundary, citations, and uncertainty behavior.

### Flashcard 4

**Q:** What should a drafting prompt control while leaving room for Claude?

**A:** Control audience, purpose, tone, facts, length, and format; leave room for word choice and phrasing.

### Flashcard 5

**Q:** What is the core brainstorming sequence?

**A:** Diverge, group, evaluate, then converge.

### Flashcard 6

**Q:** What should happen when one request includes research, analysis, brainstorming, and drafting?

**A:** Decompose it into stages and apply the appropriate strategy to each stage.

## Applied exercise

For each request below:

1. identify the dominant task type;
2. list what should be tightened;
3. list what should remain flexible;
4. identify the evidence requirement;
5. define missing-information behavior; and
6. decide whether decomposition is needed.

### Request A

“Tell me which of these two implementation plans is stronger.”

### Request B

“Find recent changes in three competitors' public messaging.”

### Request C

“Write an internal announcement about the new policy.”

### Request D

“Give us some ideas for improving employee adoption.”

### Request E

“Research the issue, identify options, recommend one, and write an executive memo.”

## Certification lens

The exam is testing whether you can match prompt design to task characteristics.

Use this shortcut:

```text
Analysis      -> criteria and standards
Research      -> scope, sources, currency, citations
Drafting      -> audience, tone, purpose, format
Brainstorming -> goal, guardrails, volume, range
```

Do not choose the prompt with the most detail automatically. Choose the prompt that places detail where control is required and preserves latitude where variation creates value.

## Engineering takeaway

> Tighten what determines validity. Loosen what benefits from variation.

## Current official reading

Product capabilities can change. Verify current feature availability and workspace controls before relying on implementation-specific behavior.

- [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)
- [Claude features and capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

## Related material

- [Component Stack](02a-component-stack.md)
- [Task Decomposition](03a-decomposition.md)
- [Parallel Case](03b-parallel-case.md)
- [Iterating to Improve Output](04-iterating-to-improve-output.md)
- [Task Strategy prompt notebook](../../../prompts/module-02/05a-strategy-by-task-type-prompts.md)
- [Task Strategy Fit Pattern](../../../patterns/task-strategy-fit-pattern.md)
