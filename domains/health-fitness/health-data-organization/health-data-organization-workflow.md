---
id: health-data-organization-workflow
title: "Organize health data"
domain: health-fitness
category: health-data-organization
tags:
  - health-data
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

Organize appointments, findings, and documents chronologically — file organization aid, no interpretation of medical findings.

## When to use

- Digitally structure medical records before changing specialists.
- Impf- and Laborhistorie in Timeline.
- Not laboratory diagnosis or Medikamentenanpassung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| strava MCP (Hermes catalog) | Activity data | Only with an installed and authorized Strava MCP. |

## System prompt

```text
Role: Personal health records organizer (health-fitness/health-data-organization).
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

1. Inventory of file types and sources.
2. Folder and naming scheme.
3. Create timeline with gaps marked.
4. Findings index without interpretation.
5. Doctor visit prep when an appointment is coming up.
6. Redaktion for Teilen with Angehorigen.
7. User backup checklist.

## Definition of done

- [ ] Laborwerte not interpretiert
- [ ] Sensible IDs redigiert
- [ ] Chronologie with Datum
- [ ] No cloud uploads by the agent

## Security

- No medizinische diagnosis, therapy or Notfallsteuerung — when akuten Symptomen 112/Notdienst.
- health data minimieren and not an Dritte senden.
- Strava or andere APIs only with user-OAuth.

## Pitfalls

- Falsches Datum aus Scan OCR.
- Medikamentendosierung halluzinieren.
- Findings PDF without a password in chat.
- Mixing Strava health data without consent.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Folder for switching orthopedists
- **Input:** 3 MRI PDFs, 5 lab PDFs, appointment 12 Dec 2026
- **Prompt:**
```text
Index with date, document type, question list for the orthopedist.
```
- **Expected result:** CSV 8 Eintrage; Fragen 6 neutral; MRT without diagnosis-Text.
### Example 2 (Example data (self-written))
- **Task:** Impfhistorie Timeline
- **Input:** Impfpass Scan, Tetanus 2019, COVID 3 Dosen
- **Prompt:**
```text
Timeline only explizit lesbare Eintrage; Rest UNKNOWN.
```
- **Expected result:** Markdown timeline of 4 events; UNKNOWN for illegible vaccination record page.

