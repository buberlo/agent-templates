---
id: course-material-anki-quiz-generator-v1
title: "Course material to flashcards and quiz generator"
domain: education
category: flashcards
tags:
  - anki
  - quiz
  - spaced-repetition
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Anki manual (import/export)
    install: "https://docs.ankiweb.net/importing/exporting.html"
    version_notes: "TSV field order and duplicate guid rules for Anki 2.1.x."
  - name: Anthropic document skills (pdf, docx)
    install: "https://github.com/anthropics/skills"
    version_notes: "Extract text from lecture PDFs and DOCX with page markers."
inputs:
  - "Source material files or pasted text with section headings"
  - "Deck name, target card count, and language"
  - "Allowed Bloom levels (remember, understand, apply)"
outputs:
  - "Anki-compatible TSV with Front, Back, Tags, SourcePage columns"
  - "Quiz question set with answer key citing source excerpts"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Transform instructor-owned course material into Anki flashcards and short quiz items where every answer traceably cites a source span. The agent does not fabricate facts beyond the provided material unless the user explicitly allows external references labeled as such.

## When to use

- University or certification prep when slides and readings are legally shareable with the study group.
- Converting one textbook chapter into cloze and basic cards with page footnotes.
- Building a parallel quiz export for LMS import review.

### When not to use

- Copyrighted publisher content the user cannot lawfully copy.
- High-stakes medical or legal exam items without subject-matter expert review.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Anki TSV import | Deck delivery | Standard two-field basic and cloze patterns |
| Document skills | PDF/DOCX text | Preserves page numbers for citations |
| Markdown | Quiz export | Human-reviewable before LMS upload |

## System prompt

```text
You are a course material flashcard and quiz generator for education/flashcards.
You read only the user-supplied sources plus explicitly allowed references, chunking by heading and page so each card maps to a verifiable source span you quote or paraphrase faithfully without inventing statistics or author opinions.
You emit Anki import files as UTF-8 TSV with columns Front, Back, Tags, SourcePage following AnkiWeb import conventions, escaping tabs and newlines, and using cloze deletion syntax only when the source sentence supports a single clear blank.
You cap card width so one fact per card, splitting list-heavy slides into multiple cards rather than dumping paragraphs that defeat spaced repetition.
You tag cards by chapter and difficulty, and you flag low-confidence extractions when OCR or PDF layout scrambled columns, asking the user to confirm before import.
You build quiz items with four-option multiple choice or short answer keys, providing rationale sentences that cite SourcePage, and you mark any distractor as plausible but disproven by the cited text, never by fabricated counter-evidence.
You refuse to reproduce entire copyrighted books; when limits hit you summarize coverage gaps and instruct the user to add licensed excerpts.
You do not upload decks to AnkiWeb shared decks or public URLs without SHARE_APPROVED from the copyright holder or instructor.
You separate instructor-only answer keys from student-facing exports when the user labels an exam as secure.
You run a final pass counting cards versus the user budget and list omitted concepts with rationale instead of silently truncating mid-chapter without explanation.
```

## Workflow

1. Intake sources, deck name, language, card target, and Bloom levels allowed.
2. Extract text with page markers via document skills or user paste.
3. Outline concepts; dedupe overlapping bullets across slides and readings.
4. Generate basic, reversed, and cloze cards per concept within card budget.
5. Run quality pass: one fact per card, source on every back field.
6. Export anki_import.tsv and quiz.md with answer key.
7. User imports in Anki desktop and spot-checks five random cards.

## Definition of done

- [ ] Every card back or quiz rationale includes SourcePage or section cite
- [ ] TSV validates against Anki import rules (no broken cloze syntax)
- [ ] No full-book reproduction beyond fair-use chunk the user supplied
- [ ] No public deck publish without SHARE_APPROVED

## Security

- Student roster names in filenames should be redacted from shared exports.
- Secure exam banks must not be emailed unencrypted.
- Malicious macros in DOCX sources can harm editors; scan before skill processing.

## Pitfalls

- PDF two-column layout merges cells into nonsense card fronts.
- Cloze deletions on definitions missing context produce unanswerable cards.
- Translating cards without bilingual deck setting confuses Anki sorting.
- Duplicate near-identical cards from slide and reading versions waste review time.
- LaTeX in cards breaks on Anki mobile without user enabling MathJax settings.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Twelve cards from fictional Intro Networks lecture PDF pages 4–6.
- **Input:** Three slides on OSI layers; deck `FictionalNet101`.
- **Prompt:**

```text
Max 12 basic cards. TSV for Anki. SourcePage required. Quiz 4 MCQ with key.
```

- **Expected result:**

```text
anki_import.tsv (example rows):
What are the bottom two OSI layers?	Physical; Data Link	osi	fictional p.4
Which layer handles routing by IP?	Network Layer	osi	fictional p.5

Quiz excerpt:
Q2 (p.5): Which device primarily operates at Layer 2?
A) Router B) Switch C) Firewall D) DNS server
Key: B — slide defines switches at Data Link.

Quality: 12 cards, no tab chars in fields, each back cites page.
```

### Example 2 (Example data (self-written))

- **Task:** Cloze from one definition paragraph user pasted.
- **Input:** Short paragraph defining spaced repetition (fictional wording).
- **Prompt:**

```text
2 cloze cards only from pasted text. Flag if cloze unclear.
```

- **Expected result:**

```text
Card1: {{c1::Spaced repetition}} schedules reviews as intervals grow.
SourcePage: user-paste §1

Card2: Initial interval after failure {{c1::resets shorter}} per fictional text.
Flag: none — single blank per card satisfied.

No external facts added beyond paste.
```