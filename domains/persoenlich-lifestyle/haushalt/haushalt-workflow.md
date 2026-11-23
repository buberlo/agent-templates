---
id: haushalt-workflow
title: "Haushalt"
domain: persoenlich-lifestyle
category: haushalt
tags:
  - haushalt
  - persoenlich-lifestyle
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
inputs:
  - "Kontext/Briefing für Haushalt"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Haushaltsaufgaben, Wartungsintervalle und Inventar mit Erinnerungen strukturieren.

## Wann nutzen

- Saisonale Wartung (Heizung, Rauchmelder, Filter) planen.
- Putzrotation in Mehrpersonenhaushalt.
- Nicht für Gas/ Elektro-Reparaturen ohne Fachbetrieb.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Kalender & Tabellen | Sheets/Calendar für Listen und Erinnerungen nach OAuth. |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Haushaltgröße und Räume.
2. Wartungskalender jährlich.
3. Wochenputz-Rotation.
4. Inventar Verbrauch.
5. Kalender-Events Entwurf gws.
6. Nutzer bestätigt Termine.
7. Quartalsreview Vorlage.

## Qualitätskriterien / Definition of Done

- [ ] Gefährliche Reparaturen ausgeschlossen
- [ ] Erinnerungen nur nach Freigabe
- [ ] Inventar ohne Auto-Bestellung
- [ ] Rotation dokumentiert

## Sicherheit & Freigaben

- Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.
- Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.
- Preise als Momentaufnahme mit Datum kennzeichnen.
- Gasgeruch → Notruf, keine DIY-Fortsetzung.

## Fallstricke

- Rauchmelder Batterie vergessen.
- Filtergröße halluziniert.
- Kalender Zeitzone falsch.
- Chemikalienmischung gefährlich vorschlagen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** WG Putzplan 4 Personen
- **Input:** Bad Küche Flur rotierend
- **Prompt:**
```text
4 Wochen Matrix und Fairness Regeln.
```
- **Erwartetes Ergebnis:** Sheet Rotation; docx an Tür Aushang Stil.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Wartung Eigentumswohnung
- **Input:** Fußbodenheizung jährlich, Rauchmelder, Fensterdichtung Herbst
- **Prompt:**
```text
Jahreskalender Events Entwurf.
```
- **Erwartetes Ergebnis:** 6 Events gws Draft; Disclaimer Sanitär Fachfirma.

