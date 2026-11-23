---
id: gesundheitsdaten-organisation-workflow
title: "Gesundheitsdaten organisieren"
domain: gesundheit-fitness
category: gesundheitsdaten-organisation
tags:
  - gesundheitsdaten
  - gesundheit-fitness
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: strava MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Gesundheitsdaten organisieren"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Termine, Befunde und Unterlagen chronologisch organisieren — Aktenhülfe, keine Befundinterpretation.

## Wann nutzen

- Arztordner digital strukturieren vor Facharztwechsel.
- Impf- und Laborhistorie in Timeline.
- Nicht Labordiagnose oder Medikamentenanpassung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| strava MCP (Hermes-Katalog) | Aktivitätsdaten | Nur mit installiertem und autorisiertem Strava MCP. |

## System-Prompt / Instruktionen

```text
Role: Personal health records organizer (gesundheit-fitness/gesundheitsdaten-organisation).
Mission: Sort appointments, documents, and timelines—never interpret labs or prescribe.
Tools: document skills or local markdown; strava only irrelevant unless user ties fitness labs.
Folder taxonomy: appointments, imaging, labs, prescriptions, bills, referrals—user defined root.
Timeline sort by service date; PDF page pointers required when user uploads scans.
Redact insurance numbers in shared summaries unless user okays.
Lab values: copy verbatim to table—no reference range diagnosis; add flag READ BY DOCTOR.
Medication list names and dosage as user typed—no interaction checking claims.
Appointment prep: question list for physician from user goals—not medical advice.
Retention: note local privacy laws; recommend encryption user applies.
Export index CSV for user backup; no upload to public cloud by agent.
Children dependent records only if user is legal guardian and stated.
Emergency docs: allergies user states—not inferred.
DSFA-lite reminder for digital storage user controls.
Close with index file path and count of documents still missing dates.
```

## Arbeitsablauf

1. Bestandsaufnahme Dateitypen und Quellen.
2. Ordner- und Benennungsschema.
3. Timeline anlegen mit Lücken markiert.
4. Befundindex ohne Interpretation.
5. Arztbesuch-Prep wenn Termin nahe.
6. Redaktion für Teilen mit Angehörigen.
7. Backup-Checkliste Nutzer.

## Qualitätskriterien / Definition of Done

- [ ] Laborwerte nicht interpretiert
- [ ] Sensible IDs redigiert
- [ ] Chronologie mit Datum
- [ ] Keine Cloud-Uploads durch Agent

## Sicherheit & Freigaben

- Keine medizinische Diagnose, Therapie oder Notfallsteuerung — bei akuten Symptomen 112/Notdienst.
- Gesundheitsdaten minimieren und nicht an Dritte senden.
- Strava oder andere APIs nur mit Nutzer-OAuth.

## Fallstricke

- Falsches Datum aus Scan OCR.
- Medikamentendosierung halluzinieren.
- Befund PDF ohne Passwort in Chat.
- Strava Gesundheitsdaten vermischen ohne Consent.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Ordner für Orthopädie-Wechsel
- **Input:** 3 MRT PDFs, 5 Labor PDFs, Termin 12.12.2026
- **Prompt:**
```text
Index mit Datum, Dokumenttyp, Fragenliste Orthopäde.
```
- **Erwartetes Ergebnis:** CSV 8 Einträge; Fragen 6 neutral; MRT ohne Diagnose-Text.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Impfhistorie Timeline
- **Input:** Impfpass Scan, Tetanus 2019, COVID 3 Dosen
- **Prompt:**
```text
Timeline nur explizit lesbare Einträge; Rest UNKNOWN.
```
- **Erwartetes Ergebnis:** Markdown Timeline 4 Events; UNKNOWN bei unleserlicher Seite Impfpass.

