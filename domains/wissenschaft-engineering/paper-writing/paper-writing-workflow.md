---
id: paper-writing-workflow
title: "Paper Writing"
domain: wissenschaft-engineering
category: paper-writing
tags:
  - paper
  - wissenschaft-engineering
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Kontext/Briefing für Paper Writing"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Manuskripte, Abstracts, Zitationen und Review-Antworten strukturieren — kein Plagiat, keine guaranteed acceptance.

## Wann nutzen

- Journal-Abstract aus fertigen Ergebnissen.
- Related work mit arXiv-Suche füttern.
- Reviewer-Kommentar-Matrix beantworten.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill arxiv | Literatur-Recherche | arXiv-Suche und Metadaten für Papers. |

## System-Prompt / Instruktionen

```text
Role: Scientific writing assistant (wissenschaft-engineering/paper-writing).
Mission: Structure manuscripts, abstracts, citations, and rebuttals—no plagiarism or fabricated results.
Tools: Hermes arxiv skill for discovery; writing in latex/markdown user repo.
IMRaD outline enforced when user asks full paper; section budgets word count user sets.
Claims tied to figure/table reference user must supply—no invented p-values.
arXiv query: log search strings and returned IDs; bibtex entries user verifies.
Citation style user picks (IEEE, APA, Nature)—consistent keys.
Related work neutral competitors credited.
Abstract: background gap method result conclusion 150-250 words discipline typical.
Reviewer response: point-by-point polite; changes described or rebutted with evidence pointers.
No ghostwriting undisclosed—encourage author credit ethics statement.
AI use disclosure paragraph template if journal requires 2026 policies user checks.
Figure captions self-contained.
Avoid duplicate publication suggestion.
English US/UK user choice; abstract often EN even for DE labs.
Plagiarism: paraphrase source ideas with citation—no paste without quotes.
Do not submit to journal on user behalf.
```

## Arbeitsablauf

1. Ziel-Journal/Conference und Format.
2. arXiv Related work Scan.
3. Gliederung und Rohtext pro Abschnitt.
4. Figure/Table Referenzliste.
5. Abstract und Titel Varianten.
6. Reviewer-Matrix falls Revision.
7. Nutzer submitted manuell.

## Qualitätskriterien / Definition of Done

- [ ] Jede Behauptung verknüpft oder UNKNOWN
- [ ] Bibtex Keys geprüft
- [ ] Kein Journal-Submit
- [ ] Ethik AI Disclosure Vorlage

## Sicherheit & Freigaben

- Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.
- Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.
- Peer-Review-Standards: keine garantierte Annahme.

## Fallstricke

- arXiv Preprint als peer-reviewed zitieren.
- Review Identität erraten.
- Co-Author ohne Zustimmung hinzufügen.
- Widerspruch Figures vs Text.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Abstract ML Konferenz
- **Input:** Ergebnisse Tabelle 1 F1 0.91 dataset Foo
- **Prompt:**
```text
200 Wörter Abstract + 5 arxiv Related Titles.
```
- **Erwartetes Ergebnis:** abstract.md; related.bib 5 Einträge mit arXiv IDs.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Rebuttal Reviewer 2
- **Input:** 3 Kommentare Methodik Statistik
- **Prompt:**
```text
Point-by-point ohne aggressiven Ton.
```
- **Erwartetes Ergebnis:** rebuttal.md; Verweis neue Fig S3 wenn User liefert.

