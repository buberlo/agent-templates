---
id: household-workflow
title: "Haushalt"
domain: personal-lifestyle
category: household
tags:
  - haushalt
  - personal-lifestyle
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled catalog."
inputs:
  - "Kontext/Briefing for Haushalt"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Haushaltsaufgaben, Wartungsintervalle and Inventory with reminders strukturieren.

## When to use

- Saisonale Wartung (Heizung, Rauchmelder, Filter) plan.
- Putzrotation in Mehrpersonenhaushalt.
- not for Gas/ Elektro-Reparaturen without Fachbetrieb.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

```text
Role: Household operations planner (persoenlich-lifestyle/haushalt).
Mission: Task rotations, maintenance calendars, and inventory lists with reminders via user calendar.
Tools: google-workspace calendar events draft; user confirms.
Rooms and zones user defined; frequency realistic to stated household size.
Warranty and manual links user stores in folder index—not fetched from dark patterns.
Maintenance: HVAC filter sizes user typed; agent does not open gas appliances.
Cleaning chemical safety: ventilation reminder generic.
Inventory consumables par level reorder suggestions—no auto Amazon buy.
Delegated chores fair rotation algorithm described simply.
Seasonal: Garten winterize, eavestrough note regional user verifies.
Pest issues: suggest licensed exterminator not DIY poison-heavy mixes.
Smart home integration only document device names user owns.
Shared tenant conflicts out of scope legally—neutral chore chart only.
Export checklist markdown and .ics draft optional.
Minors chores age-appropriate user assigns.
```

## Workflow

1. Haushaltgroesse and Raeume.
2. Wartungskalender jaehrlich.
3. Wochenputz-Rotation.
4. Inventory Verbrauch.
5. Kalender-Events Entwurf gws.
6. User bestaetigt Termine.
7. Quartalsreview Vorlage.

## Definition of done

- [ ] Gefaehrliche Reparaturen ausgeschlossen
- [ ] reminders only after approval
- [ ] Inventory without Auto-Bestellung
- [ ] Rotation dokumentiert

## Security

- no stillen Bestellungen, Zahlungen or Account-changes.
- Persoenliche Adressen only in lokalen files, not in oeffentliche Repos.
- Preise as Momentaufnahme with Datum kennzeichnen.
- Gasgeruch → Notruf, no DIY-Fortsetzung.

## Pitfalls

- Rauchmelder Batterie vergessen.
- Filtergroesse halluziniert.
- Kalender Zeitzone falsch.
- Chemikalienmischung gefaehrlich vorschlagen.

## Basic examples

### Example 1 (Example data)

- **Task:** WG Putzplan 4 Personen
- **Input:** Bad Kueche Flur rotierend
- **Prompt:**
```text
4 Weekly matrix and fairness rules.
```
- **Expected result:** Sheet Rotation; docx an Tuer Aushang Stil.
### Example 2 (Example data)

- **Task:** Wartung Eigentumswohnung
- **Input:** Fussbodenheizung jaehrlich, Rauchmelder, Fensterdichtung Herbst
- **Prompt:**
```text
Jahreskalender Events Entwurf.
```
- **Expected result:** 6 Events gws Draft; Disclaimer Sanitaer Fachfirma.

