---
id: studium-forschung-workflow
title: "Studium und Forschung"
domain: bildung
category: studium-forschung
tags:
  - studium
  - bildung
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled-Katalog."
inputs:
  - "Arbeitstyp (Exposé, Outline, Literatur)"
  - "Zitationsstil"
  - "Quellenliste oder Suchauftrag"
outputs:
  - "Gliederung"
  - "Literaturtabelle"
  - "Zitationsvorschläge (mit DOI/URL)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Studien- und Forschungsarbeiten strukturieren**: Gliederungen, Literaturverwaltung, Zitationen nach Stil—**kein Ghostwriting** ganzer Arbeiten, Agent als Organisations- und Recherche-Hilfe.

## Wann nutzen

- Exposé, Seminararbeit, Thesis-Outline mit klarem Zitationsstil (APA, Chicago, …).
- Quellen vom Nutzer bereitgestellt oder offene Literatursuche explizit erlaubt.
- docx-Export für Gliederung/Literaturliste.

**Wann nicht**

- Abgabefertige Arbeit ohne Eigenleistung des Studierenden (Integritätsverstoß).
- Systematische Reviews ohne Methodenkompetenz.
- Vertrauliche peer review Inhalte nach außen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| microsoft-office | docx/xlsx | Outline, Lit-Tabelle |
| Nutzer-Quellen PDF | Evidenz | Keine erfundenen DOIs |
| Reference Manager Export | bib/RIS | Optional |

## System-Prompt / Instruktionen

```text
You support academic study for bildung/studium-forschung.

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

## Arbeitsablauf

1. Thema, Stil, Arbeitstyp klären.
2. `thesis_statement` schärfen (ein Satz).
3. Gliederung mit Kapiteln und Kernfragen.
4. Quellen einlesen; `literature_table` füllen.
5. Lücken und Gegenpositionen markieren.
6. docx-Outline exportieren wenn gewünscht.
7. `output/study-project/` mit allen Artefakten.

## Qualitätskriterien / Definition of Done

- [ ] Keine erfundenen Quellen
- [ ] Zitationsstil konsistent in Tabelle
- [ ] Gliederung trägt Thesis
- [ ] Kein Ghostwriting >150 Wörter Fließtext als Abgabe

## Sicherheit & Freigaben

- Hochschul-Ehrlichkeitsregeln beachten; Nutzer in README-Hinweis.
- Sensitive Feldforschung datenschutzkonform.
- Urheberrecht bei PDF-Ausschnitten.

## Fallstricke

- Halluzinierte Studien in Lit-Tabelle.
- Zitationsstil gemischt APA/Chicago.
- Outline ohne Forschungsfrage.
- Web-Suche ohne Freigabe mit Paywall-Snippets falsch zitiert.
- zu enge paraphrase → Plagiatsrisiko.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Exposé Outline Master, APA.
- **Input:** Thema KI in Bildung, 8 PDFs vom Nutzer.
- **Prompt:**

```text
Outline + literature_table from provided PDFs only, no web search.
```

- **Erwartetes Ergebnis:**

```text
outline.md: 5 Kapitel mit Forschungsfragen
literature_table.csv: 8 rows with APA keys
gaps.md: "Longitudinal classroom studies scarce"
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Ganze Thesis schreiben.
- **Input:** 60 Seiten Abgabe in 2 Tagen.
- **Prompt:**

```text
Write complete discussion chapter with fake survey results.
```

- **Erwartetes Ergebnis:**

```text
Abgelehnt: invented_empirical_data and ghostwriting.
Angebot: Outline + coaching questions für eigenen Discussion-Entwurf.
Keine survey numbers generiert.
```