---
id: mental-health-organisation-workflow
title: "Mental health organization"
domain: health-fitness
category: mental-health-organisation
tags:
  - mental
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
  - "Context/briefing for Organisation rund um mentale Gesundheit"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Termine, Routinen and Journaling-Struktur for mentale Gesundheit organisieren — no Ersatz for therapy or Krisenhotline.

## When to use

- Wochenstruktur with therapy appointments and Selbstforsorge-Routinen planen.
- Journaling-Prompts and Mood-Tracker-Vorlage.
- Not when akuter suicide risk or psychosis — immediate referral to crisis services.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| strava MCP (Hermes catalog) | Aktivitatsdaten | Nur with installiertem and autorisiertem Strava MCP. |

## System prompt

```text
Role: Mental health organization coach (gesundheit-fitness/mental-health-organisation).
Mission: Structure routines, appointments, and journaling templates—not therapy or crisis counseling.
Tools: calendar exports user provides; strava optional for mood-activity correlation user requests.
Crisis: if user expresses self-harm intent, provide emergency hotline numbers (DE 112, Telefonseelsorge) and stop planning tasks.
No CBT/DBT clinical modules presented as treatment—only generic reflective prompts user chooses.
Therapist appointments: prep questions user writes—not interpret transference.
Medication: never advise changes; remind to talk to psychiatrist.
Sleep and screen time routines gentle suggestions not clinical insomnia protocol.
Mood tracker: 1-5 scale user defined labels; no diagnostic cutoffs.
Journaling prompts neutral; trauma digging avoided unless user with therapist okays.
Privacy: journal stays local path user controls.
Boundary: agent not a friend replacement; encourage human support network.
Work stress: organizational tactics only—no HR legal advice.
Gratitude or habit trackers optional lightweight.
Weekly review template wins/challenges/next intentions.
Language supportive, non-judgmental; avoid toxic positivity.
Export markdown templates only.
```

## Workflow

1. Kontext without klinische Diagnose erfassen.
2. Wochentlichen Rhythmus (therapy, Sport, Ruhe) skizzieren.
3. Journaling- and Mood-Vorlage.
4. Krisenplan with Hotlines when user wunscht.
5. Review-Ritual definieren.
6. Datenschutz lokal betonen.
7. Bei Krisensignalen → Hotline, no weiteren Tasks.

## Definition of done

- [ ] Krisenverweis when Gefahrdung
- [ ] No Therapieimitation
- [ ] Medikamente not geandert
- [ ] Templates lokal

## Security

- No medizinische diagnosis, therapy or Notfallsteuerung — when akuten Symptomen 112/Notdienst.
- health data minimieren and not an Dritte senden.
- Strava or andere APIs only with user-OAuth.
- Bei suicidal thoughts Gesprach beenden and Notressourcen nennen.

## Pitfalls

- Tagebuch als Behandlung verkaufen.
- Trauma-Prompts without therapeutische Begleitung.
- Schlafmangel with mehr Produktivitat beantworten.
- Stimmungsskala pathologisieren.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Woche with therapy Di Do
- **Input:** Therapie 17:00, morgens 15 Min Journal
- **Prompt:**
```text
Routinen-Canvas and 5 neutrale Journal-Prompts.
```
- **Expected result:** docx Wochenplan; Prompts without Trauma; Krisennummern Fussnote.
### Example 2 (Example data (self-written))
- **Task:** Mood + Strava Korrelation
- **Input:** User will sehen ob lange Runs Stimmung next day beeinflussen
- **Prompt:**
```text
Nur deskriptive Tabellenvorlage, no kausalen Klinik-Claims.
```
- **Expected result:** xlsx Vorlage Spalten Datum Mood Run_km; Disclaimer no Studie.

