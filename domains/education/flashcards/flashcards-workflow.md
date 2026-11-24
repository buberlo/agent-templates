---
id: flashcards-workflow
title: "Lernkarten"
domain: education
category: flashcards
tags:
  - lernkarten
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
  - "Quelltext (PDF, docx, YouTube-URL)"
  - "Anki Deck Name and Language"
  - "Kartenlimit pro Abschnitt"
outputs:
  - "TSV / CSV for Anki-Import"
  - "Quality notes (duplicates, too wide cards)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Create **concise educational cards** (Anki format) from lectures, scripts or videos—one question per card, with **sources**.

## When to use

- Test preparation with limited material body.
- Transkript or docx liegt vor.
- Export as a tab-separated file for Anki.

**When not to use**

- Raw material without copyright clearance.
- Medizinrechtliche Merkhilfen without Fachreview.
- Riesige PDFs without Chunking → Kontext-Overflow.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| youtube-content | Transcript | Timestamp as source |
| microsoft-office | docx lesen | Vorlesungsskript |
| TSV | Anki-Import | Standardformat |

## System prompt

```text
You create flashcards for education/lernkarten.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: source (file path|youtube url), deck_name, language, max_cards, card_style (basic|cloze), source_tag_prefix.
Rules:
- One fact per card; question answerable without long context.
- Cloze: max 2 deletions per card.
- Back side: short answer + source (page, timestamp, or heading).
- No copyrighted exam item banks copied verbatim.
- Deduplicate near-identical cards; list removed_duplicates[].
- After generation, sample 5 cards for leak (answer in question).
Output: anki_import.tsv columns: Front, Back, Tags
Tag format: source_tag_prefix::chapter
If youtube: fetch transcript via skill; cite mm:ss.
Deliver: anki_import.tsv, quality_notes.md, card_count.```

## Workflow

1. Download source (docx or YouTube transcript).
2. Chunken in sections (max ~2k words per pass).
3. Pro Abschnitt Karten generieren bis `max_cards`.
4. Remove duplicates; Check Cloze cards.
5. `anki_import.tsv` schreiben (UTF-8, Tabs).
6. `quality notes.md` with sample 5 cards.
7. Users imported into Anki; Agent does not send cloud syncs.

## Definition of done

- [ ] A card = a verifiable fact
- [ ] Source on the back
- [ ] No Antwort in Frage versteckt (Stichprobe)
TSV valid for Anki Desktop Import

## Security

- No🙂 Personal a's data on the back of the card.
Explorers.
- Exam leak: only self-formulated questions.

## Pitfalls

- Karten zu lang → schlechte Retention.
- Cloze zu komplex.
- Falsche Zeitstempel bei Transkript-Sync.
- Tag-Overflow in Anki.
- Import-Kodierung falsch (Komma statt Tab).

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30 Karten aus Vorlesung docx Kap. 2.
- **Input:** `lecture2.docx`, DE, basic.
- **Prompt:**

```text
Max 30 cards, tag prefix BIO101::ch2, export anki_import.tsv.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.card_count: 30
Sample front: "Was ist Mitose?"
Sample back: "Zellteilung … — Source: Kap. 2 §Mitose"
quality_notes: 2 duplicates removed
```

### Example 2 (Example data (self-written))
- **Task:** YouTube without URL.
- **Input:** Nur Thema "Photosynthese".
- **Prompt:**

```text
Make flashcards from YouTube.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abbruch: source_url required for youtube path.
Alternative: paste transcript text or provide docx.
No TSV written.
```