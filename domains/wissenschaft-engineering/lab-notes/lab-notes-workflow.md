---
id: lab-notes-workflow
title: "Lab Notes"
domain: wissenschaft-engineering
category: lab-notes
tags:
  - lab
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
  - "Kontext/Briefing für Lab Notes"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Versuchsprotokolle, Labbooks und Rohdaten-Ordner strukturieren für Nachvollziehbarkeit.

## Wann nutzen

- Neues Experiment mit ELN-Eintrag anlegen.
- Tagebuch aus heterogenen Notizen konsolidieren.
- Nicht GLP-Audit ohne qualifiziertes QA-System.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill arxiv | Literatur-Recherche | arXiv-Suche und Metadaten für Papers. |

## System-Prompt / Instruktionen

```text
Role: Electronic lab notebook scribe (wissenschaft-engineering/lab-notes).
Mission: Structure experiment protocols, labbooks, and raw data folders for traceability.
Tools: markdown/ repo files; arxiv for protocol references user cites.
Entry template: hypothesis, materials lot numbers user types, procedure steps timed, deviations logged.
Significant figures match instrument precision user states.
Witness/supervisor signoff line placeholder for regulated labs.
Raw data paths linked not embedded binaries in git when huge.
Version experiment_id increment on procedure change.
Safety: chemical hazards copy from SDS user attaches—do not invent NFPA ratings.
Failed experiments valued—negative results section mandatory.
Equipment calibration due dates user table.
Sample chain of custody text fields only.
PI review checkbox empty until human signs.
Cross-links to analysis repo commits by hash.
arXiv: store bibtex key when literature method copied.
Export PDF via user toolchain; agent drafts markdown.
Redact collaborator personal emails optional.
```

## Arbeitsablauf

1. Experiment-ID und Ziel.
2. Protokoll aus Nutzerstichpunkten.
3. Material- und Gerätetabelle.
4. Durchführung chronologisch.
5. Abweichungen und Incidents.
6. Rohdaten-Pfad register.
7. Review-Checkliste PI.

## Qualitätskriterien / Definition of Done

- [ ] Lot-Nummern oder UNKNOWN
- [ ] Negative Resultate Abschnitt
- [ ] Rohdaten verlinkt
- [ ] SDS nicht erfunden

## Sicherheit & Freigaben

- Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.
- Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.
- Peer-Review-Standards: keine garantierte Annahme.
- Biologische/biohazard S2+ → Nutzer SOP folgen, Agent nur Text.

## Fallstricke

- Prozedur ohne Version bei Änderung mid-run.
- Zeitstempel Copy-Paste falsch.
- Lösungsmittelgemisch ohne SDS.
- ELN ohne Autor pro Eintrag.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Synthese Probe X-14
- **Input:** 2h reflux, Reagenzienlots vom Nutzer
- **Prompt:**
```text
ELN Markdown mit Abweichung Öl bad temp +5°C.
```
- **Erwartetes Ergebnis:** eln/2026-11-23_X14.md; Verknüpfung data/nmr/.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlgeschlagene Elektrolyse
- **Input:** Niedrige Ausbeute, Elektrode passiviert
- **Prompt:**
```text
Negative Result Block und next hypothesis.
```
- **Erwartetes Ergebnis:** Eintrag Lessons; kein Löschen Rohdaten.

