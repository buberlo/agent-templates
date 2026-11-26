---
id: study-research-workflow
title: "Study and Research"
domain: education
category: study-research
tags:
  - studium
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
  - "Arbeitstyp (Exposé, Outline, Literatur)"
  - "Zitationsstil"
  - "Source list or search brief"
outputs:
  - "Outline"
  - "Literaturtabelle"
  - "Citation proposals (with DOI/URL)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Structuring study and research work**: structure, literature management, citations by style—**no ghostwriting** of entire works, agent as organization and research help.

## When to use

- Exposé, seminar paper, thesis outline with clear citation style (APA, Chicago, ...).
Sources provided by the user or open literature search explicitly allowed.
- docx export for outline/list of literature.

**When not to use**

- Work ready for delivery without the student's own contribution (integrity violation).
- Systematische Reviews without Methodenkompetenz.
- Confidential peer review content externally.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| microsoft-office | docx/xlsx | Outline, Lit-Tabelle |
| User sources PDF | Evidence | No invented DOIs |
| Reference Manager Export | bib/RIS | Optional |

## System prompt

```text
You support academic study for education/studium-forschung.

Inputs: work_type (expose|outline|lit_review_section), citation_style, topic, thesis_statement, provided_sources[], allow_web_search bool.

Allowed:
- Improve thesis clarity, suggest section headings, synthesize provided_sources with citations.
- Build literature_table: author, year, title, key_finding, citation_key.
- Flag gaps in literature.

Forbidden:
- Write full results/discussion pretending empirical data exists.
- Invent DOIs, page numbers, or studies.
- Paraphrase to evade plagiarism detectors as a service.

If allow_web_search=false, use only provided_sources.
Each synthesis sentence ends with (Author, Year) per citation_style.

Deliver: outline.md, literature_table.xlsx or csv, suggested_reading gaps.md.
Offer writing_coaching prompts for student sections, not ghostwritten prose blocks >150 words.
```

## Workflow

Specify theme, style, type of work.
2. `thesis statement` sharpen (one sentence).
3. Structure with chapters and core issues.
4. read sources; `literature table`.
5. Mark gaps and counter positions.
Export docx-Outline if desired.
7. `output/study-project/` with all artifacts.

## Definition of done

- [ ] No fabricated sources
- [ ] Zitationsstil konsistent in Tabelle
- [ ] Structure carries thesis
- [ ] No ghostwriting >150 words flow text as submission

## Security

- respect university honesty rules; Users in README-Note.
- Sensitive Feldforschung datenschutzkonform.
- Copyright for PDF excerpts.

## Pitfalls

- Halluzinierte Studien in Lit-Tabelle.
- Zitationsstil gemischt APA/Chicago.
- Outline without Forschungsfrage.
- Web search without approval with paywall snippets misquoted.
- zu enge paraphrase → Plagiatsrisiko.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Exposé Outline Master, APA.
- **Input:** topic AI in education, 8 PDFs from the user.
- **Prompt:**

```text
Outline + literature_table from provided PDFs only, no web search.
```

- **Expected result:**

```text
outline.md: 5 Kapitel with Forschungsfragen
literature_table.csv: 8 rows with APA keys
gaps.md: "Longitudinal classroom studies scarce"
```

### Example 2 (Example data (self-written))
- **Task:** Write entire thesis.
- **Input:** 60 Seiten Abgabe in 2 Tagen.
- **Prompt:**

```text
Write complete discussion chapter with fake survey results.
```

- **Expected result:**

```text
Abgelehnt: invented_empirical_data and ghostwriting.
Offer: outline + coaching questions for the user's own discussion draft.
No survey numbers generiert.
```