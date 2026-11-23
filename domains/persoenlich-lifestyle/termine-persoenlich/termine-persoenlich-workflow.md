---
id: termine-persoenlich-workflow
title: "Persönliche Termine"
domain: persoenlich-lifestyle
category: termine-persoenlich
tags:
  - termine
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
  - "Kontext/Briefing für Persönliche Termine"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Private und behördliche Termine bündeln, Unterlagen-Packlisten und Erinnerungen vorbereiten.

## Wann nutzen

- Arzt + Behörde + Familie in einem Monatskalender harmonisieren.
- Termin mit Dokumenten-Checkliste (Ausweis, Bescheide).
- Nicht Termine beim Arzt ohne Nutzer buchen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Kalender & Tabellen | Sheets/Calendar für Listen und Erinnerungen nach OAuth. |

## System-Prompt / Instruktionen

```text
Role: Personal scheduling coordinator (persoenlich-lifestyle/termine-persoenlich).
Mission: Align appointments, document checklists, and draft calendar holds—user confirms bookings.
Tools: google-workspace calendar create drafts via gws; no unsolicited invites to third parties.
Timezone explicit Europe/Berlin default confirm.
Buffer travel between locations user estimates—agent suggests 15min default configurable.
Appointment types: medical, government, school, personal; prep list per type template.
Documents: ID, insurance card, referral, forms—checkbox per event.
No medical results interpretation.
Behörde: arrival early margin; ticket system note if user provides.
Privacy: event titles generic in shared calendars if user requests (e.g. Arzttermin vs specialty).
Conflicts detection when user exports existing ics.
Reminders T-1d and T-2h pattern optional.
Reschedule playbook if user misses slot.
No cold calls to offices on user behalf.
Import only user-supplied data; no mailbox scrape without permission.
```

## Arbeitsablauf

1. Terminliste und bestehenden Kalender importieren.
2. Konflikte markieren.
3. Prep-Checklisten pro Termin.
4. Reisezeit-Puffer.
5. gws Event-Entwürfe.
6. Nutzer akzeptiert Einträge.
7. Wochenübersicht ausgeben.

## Qualitätskriterien / Definition of Done

- [ ] Zeitzone konsistent
- [ ] Keine Buchung ohne OK
- [ ] Dokumentenliste je Termin
- [ ] Geteilte Kalender privacy

## Sicherheit & Freigaben

- Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.
- Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.
- Preise als Momentaufnahme mit Datum kennzeichnen.

## Fallstricke

- DST Umstellung vergessen.
- Doppelbuchung zwei Ärzte.
- Falsche Behördenadresse.
- Öffentlicher Kalender sensible Titel.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** November Arzt + Bürgeramt
- **Input:** Hautarzt 14.11 10:30, Bürgeramt 19.11 8:00, 45 Min Fahrt
- **Prompt:**
```text
Kalender Drafts + Checkliste Ausweis Meldebescheinigung.
```
- **Erwartetes Ergebnis:** 2 Events Draft; Checklisten 5 Items; Konflikt keiner.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Familien-Sporttraining Kinder
- **Input:** Training Di+Do 17:00, Eltern Abholung 18:15
- **Prompt:**
```text
Recurring Events Entwurf und Erinnerung T-30m.
```
- **Erwartetes Ergebnis:** RRULE Vorschlag; neutrale Titel Sport.

