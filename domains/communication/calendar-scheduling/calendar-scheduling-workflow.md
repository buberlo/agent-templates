---
id: calendar-scheduling-workflow
title: "Calendar and scheduling"
domain: communication
category: calendar-scheduling
tags:
  - calendar
  - communication
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled catalog."
  - name: calendly MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
  - name: Grok Bot Google Calendar
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Product documentation."
inputs:
  - "Time zone and search window"
  - "Attendees and duration"
  - "Title/agenda draft"
outputs:
  - "Slot proposals"
  - "Calendar invite (after approval)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Find open times**, propose options, and **create invites** (Google Calendar, Calendly)—with a fixed time zone and no double bookings across calendars.

## When to use

- Meeting with 2–8 attendees in the next two weeks.
- gws, Calendly MCP, or Grok Calendar connected.
- Invite copy and attendee list approved by the user.

**When not to use**

- Redesigning recurring rules for an entire organization.
- Rooms/resources without a bound resource calendar.
- Appointments in time zones without an explicit IANA identifier.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| gws calendar | Free/busy, events.insert | Native Workspace |
| Calendly MCP | Booking links, availability | External booking |
| Grok Google Calendar | Chat OAuth | Fast slot search |

## System prompt

```text
You schedule meetings for communication/calendar-scheduling using gws, Calendly MCP, or Grok Calendar.

Inputs: timezone (default Europe/Vienna), window start/end ISO, duration minutes, attendee emails, title, agenda bullets, location (meet link or room), calendars_to_check[], create_event (yes only after approval).

Process:
1) Query freebusy for all attendees; intersect availability.
2) Propose 3 slots in local timezone with weekday names in German if user locale DE.
3) Show draft invitation body (HTML/plain) including agenda and conferencing link placeholder.
4) On "CREATE EVENT", call events.insert with sendUpdates=none unless user requests email invites.
5) Detect conflicts on organizer calendar; flag if hard conflict exists.

Never delete events without confirmation.
Use IANA timezone in API calls, not abbreviations like CET.
Log event_id after create.
```

## Workflow

1. Set time zone `Europe/Vienna` and window (e.g. next 5 business days).
2. Run `gws calendar freebusy` for all attendee emails.
3. Compute three mutual slots and print a table.
4. User picks a slot; finalize title and agenda.
5. Show invite draft (attendees, Zoom/Meet link).
6. After `CREATE`: `events.insert` with chosen slot.
7. Save `event_id` and ICS link in `output/scheduling.md`.

## Definition of done

- [ ] All times include offset/IANA
- [ ] No invite without confirmed slot and attendee list
- [ ] Organizer calendar conflicts checked
- [ ] event_id documented

## Security

- Do not put attendee emails in public logs.
- Share Calendly links only when booking policy allows it.
- Delete or move events only on explicit instruction.

## Pitfalls

- Daylight saving time calculated incorrectly.
- Organizer has multiple calendars not queried → double booking.
- `sendUpdates=all` without review → wrong invite sent.
- Calendly vs. Google: two parallel bookings for the same slot.
- Only UTC used internally → user sees wrong local time.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30-minute sync with two colleagues.
- **Input:** `alice@firma.example`, `bob@firma.example`, Mon–Fri 09–17 Europe/Vienna.
- **Prompt:**

```text
Find 3 free 30-min slots next week, draft invite title "API Review", do not create until I pick.
```

- **Expected result:**

```text
1) Tue 25.11. 10:00–10:30 CET
2) Wed 26.11. 14:00–14:30 CET
3) Thu 27.11. 11:30–12:00 CET
Draft title: API Review | Attendees: alice, bob
Create: pending
```

### Example 2 (Example data (self-written))
- **Task:** Hard conflict.
- **Input:** Organizer blocked 14:00–15:00; desired slot 14:30.
- **Prompt:**

```text
Create event at 14:30 Tuesday.
```

- **Expected result:**

```text
Conflict: existing event "Board prep" 14:00–15:00.
No events.insert executed.
Suggest alternate slot 15:00 or explicit user override.
```