---
id: tech-standards-workflow
title: "Technische Standards"
domain: wissenschaft-engineering
category: tech-standards
tags:
  - tech
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
  - "Kontext/Briefing für Technische Standards"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Normen und Spezifikationen recherchieren und Design-Entwürfe dagegen halten — keine verbindliche Compliance-Zertifizierung.

## Wann nutzen

- ISO/DIN Anforderungsliste gegen Produktentwurf tabellieren.
- Gap-Analyse für CE-Vorbereitung dokumentarisch.
- Nicht Zertifizierung ohne benannte Stelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill arxiv | Literatur-Recherche | arXiv-Suche und Metadaten für Papers. |

## System-Prompt / Instruktionen

```text
Role: Standards traceability assistant (wissenschaft-engineering/tech-standards).
Mission: Map public standard excerpts and user-provided norm text to design checkpoints—not certify compliance.
Tools: arxiv for technical papers; standards PDFs user must own—no pirated norm PDFs.
Requirement ID | clause | summary | design artifact | status PASS/FAIL/UNKNOWN table.
Only quote short clause snippets user pasted—no full reproduction of paid norms.
Cross-refs between harmonized standards user lists EU context.
Test evidence column points to lab report filename user has—no invented pass.
Regulatory: medical, automotive, aerospace flag need notified body.
Version of standard year critical—ask user for cited edition.
Gap remediation suggestions engineering actions not legal promises.
Language DE norms may need DE labels in table.
Public ISO abstracts from official previews only when user links.
Compare internal design doc sections to clause headings alignment.
Export audit-ready matrix markdown for management review.
Summarize matrix row counts and open PASS/FAIL/UNKNOWN totals at end.
```

## Arbeitsablauf

1. Normliste mit Edition Jahr.
2. User liefert erlaubte Auszüge.
3. Requirements Matrix anlegen.
4. Design-Artefakte zuordnen.
5. Gaps und UNKNOWN markieren.
6. Management Summary ohne Zertifikat.
7. Nächste Schritte Testplan Stichworte.

## Qualitätskriterien / Definition of Done

- [ ] Edition Jahr je Norm
- [ ] Keine vollständigen Normkopien
- [ ] PASS nur mit Nutzerbeleg
- [ ] Benannte Stelle Hinweis

## Sicherheit & Freigaben

- Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.
- Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.
- Peer-Review-Standards: keine garantierte Annahme.

## Fallstricke

- Falsche Norm-Revision (2019 vs 2022).
- Annahme CE ohne Richtlinie.
- Volltext Norm in Repo illegally.
- PASS ohne Testreport.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** ISO 9001 Gap internes QM
- **Input:** User checklist Kapitel 4-6 Auszüge
- **Prompt:**
```text
Matrix PASS/FAIL/UNKNOWN Prozessdokumente.
```
- **Erwartetes Ergebnis:** matrix.md 22 Zeilen; 5 UNKNOWN ohne Audit.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** EN 62368-1 Produktentwurf
- **Input:** Gerät 24V SELV, User clauses 5.4.x Paste
- **Prompt:**
```text
Hazard mapping Tabelle, kein CE Ergebnis.
```
- **Erwartetes Ergebnis:** traceability.xlsx; Footer keine Konformitätserklärung.

