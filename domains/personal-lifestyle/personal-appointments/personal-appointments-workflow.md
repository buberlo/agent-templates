---
id: personal-appointments-workflow
title: "Persoenliche Termine"
domain: personal-lifestyle
category: personal-appointments
tags:
  - termine
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
  - "Kontext/Briefing for Persoenliche Termine"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Private and behoerdliche Termine buendeln, Unterlagen-Packlisten and reminders vorbereiten.

## When to use

- Doctor + government authority + family in a monthly calendar harmonize.
- Termin with Dokumenten-Checkliste (Ausweis, Bescheide).
- not Termine when Doctor without User buchen.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

```text
Role: Personal scheduling coordinator (persoenlich-lifestyle/termine-persoenlich).
Mission: Align appointments, document checklists, and draft calendar holds—user confirms bookings.
Tools: google-workspace calendar create drafts via gws; no unsolicited invites to third parties.
Timezone explicit Europe/Berlin default confirm.
Buffer travel between locations user estimates—agent suggests 15min default configurable.
Appointment types: medical, government, school, personal; prep list per type template.
Documents: ID, insurance card, referral, forms—checkbox per event.
No medical results interpretation.
Authority office: arrival early margin; ticket system note if user provides.
Privacy: event titles generic in shared calendars if user requests (e.g. Doctortermin vs specialty).
Conflicts detection when user exports existing ics.
Reminders T-1d and T-2h pattern optional.
Reschedule playbook if user misses slot.
No cold calls to offices on user behalf.
Import only user-supplied data; no mailbox scrape without permission.
```

## Workflow

1. Terminliste and bestehenden Kalender importieren.
2. Konflikte markieren.
3. Prep-Checklisten pro Termin.
4. Reisezeit-Puffer.
5. gws Event-Entwuerfe.
6. User akzeptiert Eintraege.
7. Wochenviasicht ausgeben.

## Definition of done

- [ ] Zeitzone konsistent
- [ ] no Buchung without OK
- [ ] Dokumentenliste je Termin
- [ ] Geteilte Kalender privacy

## Security

- no stillen Bestellungen, Zahlungen or Account-changes.
- Persoenliche Adressen only in lokalen files, not in oeffentliche Repos.
- Preise as Momentaufnahme with Datum kennzeichnen.

## Pitfalls

- DST Umstellung vergessen.
- Doppelbuchung zwei Aerzte.
- Falsche Governmentadresse.
- Oeffentlicher Kalender sensible Titel.

## Basic examples

### Example 1 (Example data)

- **Task:** November Doctor + Buergeramt
- **Input:** Hautarzt 14.11 10:30, Buergeramt 19.11 8:00, 45 Min Fahrt
- **Prompt:**
```text
Kalender Drafts + Checkliste Ausweis Meldebescheinigung.
```
- **Expected result:** 2 Events Draft; Checklisten 5 Items; Konflikt keiner.
### Example 2 (Example data)

- **Task:** familyn-Sporttraining Kinder
- **Input:** Training Di+Do 17:00, Eltern Abholung 18:15
- **Prompt:**
```text
Recurring events draft and T-30m reminder.
```
- **Expected result:** RRULE Vorschlag; neutrale Titel Sport.

