---
id: health-data-organization-workflow
title: "Organize health data"
domain: health-fitness
category: health-data-organization
tags:
  - gesundheitsdaten
  - health-fitness
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: strava MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Context/briefing for health data organisieren"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Termine, Befunde and Unterlagen chronologisch organisieren — Aktenhulfe, no Befundinterpretation.

## When to use

- Arztordner digital strukturieren vor Facharztwechsel.
- Impf- and Laborhistorie in Timeline.
- Not laboratory diagnosis or Medikamentenanpassung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| strava MCP (Hermes catalog) | Aktivitatsdaten | Nur with installiertem and autorisiertem Strava MCP. |

## System prompt

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

## Workflow

1. Bestandsaufnahme Dateitypen and Quellen.
2. Ordner- and Benennungsschema.
3. Timeline anlegen with Lucken markiert.
4. Befundindex without Interpretation.
5. Arztbesuch-Prep wenn Termin nahe.
6. Redaktion for Teilen with Angehorigen.
7. Backup-Checkliste User.

## Definition of done

- [ ] Laborwerte not interpretiert
- [ ] Sensible IDs redigiert
- [ ] Chronologie with Datum
- [ ] No Cloud-Uploads durch agent

## Security

- No medizinische diagnosis, therapy or Notfallsteuerung — when akuten Symptomen 112/Notdienst.
- health data minimieren and not an Dritte senden.
- Strava or andere APIs only with user-OAuth.

## Pitfalls

- Falsches Datum aus Scan OCR.
- Medikamentendosierung halluzinieren.
- Befund PDF without Passwort in Chat.
- Strava Gesundheitsdaten vermischen without Consent.

## Basic examples

### Example 1 (Example data)

- **Task:** Ordner for Orthopadie-Wechsel
- **Input:** 3 MRT PDFs, 5 Labor PDFs, Termin 12.12.2026
- **Prompt:**
```text
Index with Datum, Dokumenttyp, Fragenliste orthopedist.
```
- **Expected result:** CSV 8 Eintrage; Fragen 6 neutral; MRT without diagnosis-Text.
### Example 2 (Example data)

- **Task:** Impfhistorie Timeline
- **Input:** Impfpass Scan, Tetanus 2019, COVID 3 Dosen
- **Prompt:**
```text
Timeline only explizit lesbare Eintrage; Rest UNKNOWN.
```
- **Expected result:** Markdown Timeline 4 Events; UNKNOWN bei unleserlicher Seite Impfpass.

