---
id: powerpoint-pptx-workflow
title: "PowerPoint-Praesentationen from Briefing"
domain: office-documents
category: powerpoint-pptx
tags:
  - pptx
  - slides
  - deck
target_agents:
  - hermes
  - claude-code
  - generic
required_tools:
  - name: Anthropic document skills (pptx)
    install: "https://github.com/anthropics/skills"
    version_notes: "pptx validate"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "python-pptx"
  - name: LibreOffice
    install: "optional impress export"
    version_notes: "PDF Deck review"
inputs:
  - "Outline and slide count"
  - "CI-Farben and Logo-path"
outputs:
  - "deck.pptx"
  - "Optional deck.pdf"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Build structured **slide decks** from briefing—title, content, speaker notes—with validator and PDF review.

## When to use

- Sales-Pitch, Status-Review, Workshop-Intro.
- 10–40 slides, consistent layout.
- no Animations-Heavy-Design required.

**When not to use**

- Broadcast Motion Graphics (→ media).
- Template with komplexen Slide Masters without Vorlage-file.
- Automatischer Upload to SlideShare without approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic pptx-Skill | generation | Validate |
| Hermes pptx CLI | Alternative | Offline |
| LibreOffice Impress | PDF-Export | QA |
| python-pptx | Layout-Checks | Programmatisch |

## System prompt

```text
You build pptx decks from an outline—one message per slide, readable font sizes, speaker notes when requested.

Inputs: title, audience, outline (slide title + bullets max 5 per slide), brand colors hex optional, logo path, output deck.pptx, notes yes/no.

Rules:
- Title slide: event name, date, speaker.
- Avoid walls of text; split overflow to new slides.
- Charts only when data series provided—no invented metrics.
- Alt text on images when accessibility flag set.

After build: run pptx validate from skill if available; export PDF via soffice for visual pass.
Check: no placeholder "Lorem", consistent heading sizes, footer page numbers if template includes.

Speaker notes: expand bullets to sentences user can speak; do not duplicate slide text verbatim.

Approvals: present externally, upload cloud, or email deck requires user yes.

Output: pptx path, slide count, validation status, pdf qa path.

Do not embed video files without codec check.
Keep 16:9 layout unless 4:3 requested.

If user supplies pptx template, clone masters—do not rebuild brand from scratch.

Document slide count vs outline count mismatch.

Use high-contrast text on brand backgrounds.
```

## Workflow

1. Verify outline in slide list with strict character limits.
2. Skill/CLI Deck generieren.
3. Validator laufen.
4. PDF-Export for visuelle QA.
5. Spot-check 3 slides (title, chart, closing).
6. Sprechernotizen re-checked.
7. approval for externe Nutzung einholen.

## Definition of done

- [ ] Slide count = outline
- [ ] Validator OK or Abweichungen dokumentiert
- [ ] no invented KPIs in Charts
- [ ] PDF QA on brand slides
- [ ] approval before Versand

## Security

- Do not share confidential strategy slides publicly.
- Kundennamen only with approval.
- Skills minimal enable.

## Pitfalls

- python-pptx ignoriert manche Master-Layouts.
- to kleine Schrift in PDF-Review unsichtbar in Editor.
- Logo PNG to gross → langsame file.
- Tabellen breiter as Slide.
- Speaker notes with confidential details in public PDF.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 12-slide status deck.
- **Input:** Outline 12 Punkte, CI #003366.
- **Prompt:**

```text
Build status_nov.pptx from outline; speaker notes; validate; export status_nov.pdf.
```

- **Expected result:**

```text
status_nov.pptx 12 slides; validation PASS; pdf for QA attached path.
```

### Example 2 (Example data (self-written))
- **Task:** Chart without Daten ablehnen.
- **Input:** Outline verlangt Umsatz-Chart without CSV.
- **Prompt:**

```text
Stop and request data series before adding chart slide.
```

- **Expected result:**

```text
No chart slide; deck without slide 7 or placeholder TEXT ONLY pending data.
```