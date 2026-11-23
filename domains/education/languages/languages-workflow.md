---
id: languages-workflow
title: "Sprachen"
domain: education
category: languages
tags:
  - sprachen
  - education
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled catalog."
inputs:
  - "Source and Target Language"
  - "Text or Audiostream"
  - "Register (du/Sie, formal/informell)"
outputs:
  - "Translation or corrected text"
  - "Grammatics Explanations"
  - "mini-exercise dialogue"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Language learning, translation and corrections** with register specifications, error categorization and short practice dialogues—no certification as a substitute for reviewers:in.

## When to use

- Translation or error analysis of a user text (DE↔EN or similar).
- Sprachniveau (A2–C1) angegeben.
- Tonality (business, casual) is known.

**When not to use**

- Certified translations.
- Legal / contractual texts without specialist translators:in.
- Identity fraud in language examinations.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| LLM + explicit rules | translation / correction | core |
| microsoft-office | Glossar docx | Terminologie |
| youtube-content | Immersion clips | Optional with transcript |

## System prompt

```text
You teach and translate languages for education/sprachen.

Inputs: source_lang, target_lang, text, task (translate|correct|dialog_drill), cefr_level, register, glossary path optional.

Translate:
- Prefer sense-for-sense; flag untranslatable idioms with explanation in target_lang.
- Use glossary terms exactly when file provided.

Correct:
- Mark errors with category (grammar|word_choice|register|spelling).
- Provide corrected sentence and one-sentence rule DE if user UI DE.

Dialog drill:
- 6-turn mini dialog at cefr_level; bold new vocabulary; no toxic content.

Do not claim certified translation.
For exams: if user requests answer key for live test, refuse.

Output: result.md with sections per task; table of corrections if correct mode.
```

## Workflow

1. Sprachen, Niveau, Register festlegen.
2. Optional Glossar `glossary.docx` laden.
3. Perform task (translate/correct/drill).
4. Error in table with category.
5. In the case of translation: Mark inquiry in case of ambiguity.
6. Mini-dialogue if `dialog drill` is desired.
7. `output/lang-session.md` archivieren.

## Definition of done

- [ ] Register konsistent
- [ ] Glossar-Begriffe eingehalten
- [ ] Corrections with category
- [ ] No Zertifizierungsbehauptung

## Security

- Do not externally log sensitive content into input text.
- For minors appropriate content.
- Do not reinforce hate speech in corrections.

## Pitfalls

Overlooked incorrect gender/numerus congruence.
- Sie/du vermischt.
- Fachterminologie without Glossar erfunden.
Idiom translated literally.
- CEFR level too heavy → Overwhelming.

## Basic examples

### Example 1 (Example data)

- **Task:** EN→DE Business-Mail Korrektur.
- **Input:** B1, register formal Sie.
- **Prompt:**

```text
Correct this email in German business register, table of errors.
```

- **Expected result:**

```text
| # | Original | Fix | Category |
| 1 | "I wanted to ask" | "I want to ask you" | register |
Corrected body: Dear Mrs. Mueller, ...
```

### Example 2 (Example data)

- **Task:** Certified translation.
- **Input:** Vertrag EN→DE beglaubigt.
- **Prompt:**

```text
Provide sworn translation for court.
```

- **Expected result:**

```text
Abgelehnt: certified_translation_not_offered.
Hinweis: qualifizierte beeidete Dolmetscher:in anfragen.
Optional: rough draft only as a learning aid with disclaimer, possible after approval.
```