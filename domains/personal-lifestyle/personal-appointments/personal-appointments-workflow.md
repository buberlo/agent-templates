---
id: personal-appointments-workflow
title: "Personal appointments"
domain: personal-lifestyle
category: personal-appointments
tags:
  - appointments
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
  - "Context/briefing for personal appointments"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Bundle private and government appointments, prepare document checklists and reminders.

## When to use

- Doctor + government authority + family in a monthly calendar harmonize.
- Appointment with document checklist (ID, official notices).
- Do not book doctor appointments without the user.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

```text
Role: Personal scheduling coordinator (personal-lifestyle/personal-appointments).
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
3. Prep checklists per appointment.
4. Reisezeit-Puffer.
5. gws Event-Entwuerfe.
6. User akzeptiert Eintraege.
7. Wochenviasicht ausgeben.

## Definition of done

- [ ] Zeitzone konsistent
- [ ] no Buchung without OK
- [ ] Document list per appointment
- [ ] Geteilte Kalender privacy

## Security

- no silent orders, payments, or account changes.
- Keep personal addresses only in local files, not in public repos.
- Mark prices as a snapshot with a date.

## Pitfalls

- DST Umstellung vergessen.
- Doppelbuchung zwei Aerzte.
- Falsche Governmentadresse.
- Public calendar with sensitive titles.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** November Doctor + Buergeramt
- **Input:** Hautarzt 14.11 10:30, Buergeramt 19.11 8:00, 45 Min Fahrt
- **Prompt:**
```text
Calendar drafts + checklist for ID and registration certificate.
```
- **Expected result:** 2 event drafts; checklists of 5 items; no conflicts.
### Example 2 (Example data (self-written))
- **Task:** familyn-Sporttraining Kinder
- **Input:** Training Di+Do 17:00, Eltern Abholung 18:15
- **Prompt:**
```text
Recurring events draft and T-30m reminder.
```
- **Expected result:** RRULE Vorschlag; neutrale Titel Sport.

