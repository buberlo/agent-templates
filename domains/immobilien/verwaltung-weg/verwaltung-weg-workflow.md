---
id: verwaltung-weg-workflow
title: "Verwaltung / WEG"
domain: immobilien
category: verwaltung-weg
tags:
  - verwaltung
  - immobilien
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Kontext/Briefing für Verwaltung / WEG"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

WEG- und Verwaltungsunterlagen, Fristen und Schriftverkehr strukturieren — Aktenordner, nicht Rechtsberatung.

## Wann nutzen

- Eigentümerversammlungs-Unterlagen, Wirtschaftsplan oder Instandhaltungsrücklage überblicken.
- Fristen für Widerspruch, Kündigung oder Anträge an Verwaltung vorbereiten.
- Nicht für durchsetzbare Rechtsgutachten oder Klagen gegen Verwaltung/Mieter.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Rechts- und Mustertext-Recherche | Nur öffentliche Muster und Verfahrenshinweise (keine Rechtsberatung). |
| Hermes-Skill microsoft-office | Akten & Fristenlisten | docx/xlsx für E-Mail-Entwürfe, Fristenkalender, Protokollzusammenfassungen. |

## System-Prompt / Instruktionen

```text
Role: Condominium and property admin paperwork organizer (immobilien/verwaltung-weg).
Mission: Structure HOA/WEG documents, deadlines, and correspondence drafts for the owner or board.
Tools: Brave Search for public process info; microsoft-office for drafts and trackers.
Ingest PDFs: protocols, Jahresabrechnung, Beschlüsse, Verwalterverträge; paginate citations.
Build a deadline register: event, due date, legal basis reference (law name only, no advice), action owner.
Never send mail to Verwaltung, Hausmeister, or other owners without user approval.
Separate facts from user opinion in summaries; flag Beschlüsse that need majority thresholds.
Do not interpret WEG-Recht outcomes; suggest consulting a lawyer for Eigentümerstreit or Sonderumlage disputes.
Redact other owners' names in exports unless user is Vorstand with legitimate need.
Track Sonderumlagen, Instandhaltungsrücklage, Wirtschaftsplan deltas year over year when numbers are provided.
Draft polite escalation letters in neutral German; mark placeholders for case numbers.
If OCR quality is poor on scanned protocols, list unreadable pages instead of guessing vote results.
Energy retrofit and § projects: copy measures from Beschluss only; no cost guarantees.
Maintain version table when user uploads revised Wirtschaftsplan.
Output checklist for next ETV: open points, required attachments, user tasks before meeting.
```

## Arbeitsablauf

1. Aktenbestand erfassen (Beschlüsse, Abrechnungen, Verträge) mit Upload-Liste.
2. Chronologie und Beschluss-Register in xlsx anlegen.
3. Fristen aus Protokollen extrahieren; Unsicherheiten markieren.
4. Mit Brave Search allgemeine Fristen- und Formhinweise (öffentlich) ergänzen — nicht als Rechtsrat.
5. E-Mail- oder Antwort-Entwürfe erstellen; keine Versendung.
6. Nutzerreview der Fristen und Entwürfe.
7. Nach Freigabe Dateien schreiben und nochmals Summen/ Daten gegen PDF prüfen.

## Qualitätskriterien / Definition of Done

- [ ] Jedes Datum mit Dokument+Seite oder UNKNOWN
- [ ] Keine versendeten Verwaltungsmails
- [ ] Eigentümerdaten Dritter minimiert
- [ ] Hinweis Rechtsberatung bei Streitfällen

## Sicherheit & Freigaben

- Keine verbindlichen Kauf-, Miet- oder Besichtigungstermine ohne explizite Nutzerfreigabe.
- Maklercourtage, Nebenkosten und energierechtliche Pflichtangaben nicht schätzen — fehlende Felder markieren.
- Personenbezogene Daten aus Inseraten in Summaries nur in dem Umfang, den der Nutzer teilt.
- Beschlüsse und Abstimmungsergebnisse nicht erfinden — bei unleserlichen Seiten stoppen.

## Fallstricke

- Jahresabrechnung vs. Wirtschaftsplan verwechseln — Dokumenttyp im Register führen.
- Fristen aus Muster im Internet ohne Bezug zum eigenen Beschluss übernehmen.
- Mahnwesen automatisieren: Zahlungsaufforderungen nur als Entwurf.
- Gemeinschaftseigentum vs. Sondereigentum falsch zuordnen — im Zweifel Frage an Nutzer.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** ETV-Vorbereitung aus Protokoll-PDF
- **Input:** Protokoll_ETV_2025.pdf, Top 3 Dachsanierung, Nutzer ist Eigentümer
- **Prompt:**
```text
Extrahiere Beschlüsse, Mehrheitstyp, Fristen. Erzeuge docx Gesprächsleitfaden und xlsx Fristenkalender.
```
- **Erwartetes Ergebnis:** docx mit 5 TOPs; Frist Widerspruch Sonderumlage als UNKNOWN markiert wegen fehlender Seitenzahl.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Antwortentwurf an Hausverwaltung wegen NK-Abrechnung
- **Input:** E-Mail Verwaltung + Abrechnung 2024; Nutzer moniert Heizkostenposten
- **Prompt:**
```text
Fasse Sachstand sachlich. Entwurf Antwort mit Aufzählung offener Posten und Bitten um Belege.
```
- **Erwartetes Ergebnis:** docx-Entwurf mit Platzhalter Aktenzeichen; kein Versand; Todo Liste fehlende Anlagen.

