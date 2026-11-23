---
id: powerpoint-pptx-workflow
domain: office-dokumente
title: "PowerPoint-Präsentationen aus Briefing"
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
  - "Gliederung und Folienanzahl"
  - "CI-Farben und Logo-Pfad"
outputs:
  - "deck.pptx"
  - "Optional deck.pdf"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Folien-Decks** aus Briefing strukturiert bauen—Titel, Inhalt, Sprechernotizen—mit Validator und PDF-Review.

## Wann nutzen

- Sales-Pitch, Status-Review, Workshop-Intro.
- 10–40 Folien, konsistentes Layout.
- Kein Animations-Heavy-Design nötig.

**Wann nicht**

- Broadcast Motion Graphics (→ medien).
- Template mit komplexen Slide Masters ohne Vorlage-Datei.
- Automatischer Upload zu SlideShare ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic pptx-Skill | Erzeugung | Validate |
| Hermes pptx CLI | Alternative | Offline |
| LibreOffice Impress | PDF-Export | QA |
| python-pptx | Layout-Checks | Programmatisch |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Outline in Folienliste mit harter Zeichenanzahl prüfen.
2. Skill/CLI Deck generieren.
3. Validator laufen.
4. PDF-Export für visuelle QA.
5. Stichprobe 3 Folien (Titel, Chart, Abschluss).
6. Sprechernotizen gegenlesen.
7. Freigabe für externe Nutzung einholen.

## Qualitätskriterien / Definition of Done

- [ ] Folienanzahl = Outline
- [ ] Validator OK oder Abweichungen dokumentiert
- [ ] Keine erfundenen KPIs in Charts
- [ ] PDF-QA bei Brand-Folien
- [ ] Freigabe vor Versand

## Sicherheit & Freigaben

- Vertrauliche Strategie-Folien nicht öffentlich teilen.
- Kundennamen nur mit Freigabe.
- Skills minimal aktivieren.

## Fallstricke

- python-pptx ignoriert manche Master-Layouts.
- Zu kleine Schrift in PDF-Review unsichtbar in Editor.
- Logo PNG zu groß → langsame Datei.
- Tabellen breiter als Slide.
- Notizen mit vertraulichen Details bei öffentlicher PDF.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 12-Folien Status-Deck.
- **Input:** Outline 12 Punkte, CI #003366.
- **Prompt:**

```text
Build status_nov.pptx from outline; speaker notes; validate; export status_nov.pdf.
```

- **Erwartetes Ergebnis:**

```text
status_nov.pptx 12 slides; validation PASS; pdf for QA attached path.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Chart ohne Daten ablehnen.
- **Input:** Outline verlangt Umsatz-Chart ohne CSV.
- **Prompt:**

```text
Stop and request data series before adding chart slide.
```

- **Erwartetes Ergebnis:**

```text
No chart slide; deck without slide 7 or placeholder TEXT ONLY pending data.
```