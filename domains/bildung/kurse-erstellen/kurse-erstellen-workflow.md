---
id: kurse-erstellen-workflow
title: "Kurse erstellen"
domain: bildung
category: kurse-erstellen
tags:
  - kurse
  - bildung
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled-Katalog."
inputs:
  - "Thema, Zielgruppe, Dauer"
  - "Lernziele (messbar)"
  - "Quellen und Medien"
outputs:
  - "Curriculum-Outline"
  - "Lektionen (docx/md)"
  - "Folien (pptx)"
  - "Übungen mit Musterlösung (intern)"
risk_level: low
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Curriculum von messbaren Lernzielen bis zu Lektionen, Übungen und Folien**—mit Quellenpflicht und Office-Skills zur dateifertigen Auslieferung.

## Wann nutzen

- Neuer interner oder Kunden-Kurs (Workshop, E-Learning-Modul).
- Lernziele und Dauer sind bekannt.
- docx/pptx-Skills oder Hermes microsoft-office verfügbar.

**Wann nicht**

- Hochschul-Akreditierung ohne fachliche Freigabe.
- Urheberrechtlich geschützte Drittquellen ohne Lizenz.
- Prüfungsinhalte ohne Item-Review durch Fachexpert:in.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic pptx/docx | Präzise Office-Artefakte | Validatoren |
| Hermes microsoft-office | Offline python-docx/pptx | Kein Office nötig |
| youtube-content | Quellvideos → Outline | Transkript mit Quelle |

## System-Prompt / Instruktionen

```text
You build courses for bildung/kurse-erstellen.

Inputs: topic, audience, duration_hours, modality (live|self_paced), language DE, source_urls[], bloom_level target.

Pipeline:
1) Write measurable learning objectives (3-6), each with verb from Bloom taxonomy.
2) Curriculum outline: modules, lesson titles, time boxes, prerequisites.
3) For each lesson: concept explanation, activity, formative check question, optional homework.
4) Exercises: include instructor_solution separate file, not in student pack if assessment.
5) Slides: one pptx deck per module, speaker notes, max 6 bullets per slide.
6) Cite all external facts with source_urls; mark UNSOURCED if missing.
7) Run office validate script on pptx when Anthropic skill available.

Do not plagiarize courseware sites verbatim.
Deliver: outline.md, lessons/*.md, slides/module-*.pptx paths, sources.bib.
```

## Arbeitsablauf

1. Lernziele mit Nutzer abstimmen (SMART).
2. `outline.md` mit Modulen und Zeiten.
3. Lektionstexte pro Modul als Markdown.
4. Übungen + `instructor_solutions.md` ablegen.
5. pptx pro Modul erzeugen; `validate.py` wenn verfügbar.
6. Quellenliste `sources.bib` vervollständigen.
7. Paket `output/course-<topic>/` zur Review.

## Qualitätskriterien / Definition of Done

- [ ] Jedes Lernziel einer Lektion/Übung zugeordnet
- [ ] pptx validiert oder manuell gegengelesen
- [ ] Quellen für externe Fakten
- [ ] Assessments getrennt von Teilnehmermaterial

## Sicherheit & Freigaben

- Keine personenbezogenen Beispieldaten ohne Einwilligung.
- Vorschulpädagogik/Medizin: menschliche Fachexpertise Pflicht.
- Publish in LMS nur nach Freigabe.

## Fallstricke

- Folien voller Text statt Unterricht.
- Übungen ohne Lösbarkeitstest.
- YouTube-Zusammenfassung ohne Zeitcode-Check.
- pptx-Validator ignoriert → kaputte Layouts.
- Lernziele nicht messbar.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 2h Workshop „API-Grundlagen“.
- **Input:** Entwickler Einsteiger, DE.
- **Prompt:**

```text
Create outline + 3 lessons + 10-slide deck with speaker notes, cite REST docs only from provided URLs.
```

- **Erwartetes Ergebnis:**

```text
Objectives: 4 (z. B. "REST-Verb benennen", "JSON-Fehler lesen")
Files: outline.md, lessons/L1-L3.md, slides/module-1.pptx (10 slides)
sources.bib: 2 URLs
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende Zielgruppe.
- **Input:** Nur Thema "Kubernetes".
- **Prompt:**

```text
Build full course package.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: audience and duration_hours required.
Nachfrage: Rolle (Dev/Ops)? Dauer? Prüfung ja/nein?
Keine pptx erzeugt.
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Kurzes Briefing-Deck mit Anthropic-pptx-Skill validieren.
- **Input:** Tutorial-Briefing als PowerPoint.
- **Prompt:**

```text
pptxgenjs 4.0.1, skills/pptx/scripts/office/validate.py, python-pptx zum Gegenlesen.
```

- **Erwartetes Ergebnis:**

```text
Datei briefing.pptx — Validator: All validations PASSED
3 Folien 16x9, Text + Speaker Notes
Quelle: https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
```