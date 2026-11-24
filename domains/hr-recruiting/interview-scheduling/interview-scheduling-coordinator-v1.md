---
id: interview-scheduling-coordinator-v1
title: "Interview scheduling coordinator"
domain: hr-recruiting
category: interview-scheduling
tags:
  - scheduling
  - calendar
  - recruiting
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: google_workspace_mcp
    install: "https://github.com/taylorwilsdon/google_workspace_mcp"
    version_notes: "Google Calendar read and event tools via MCP (listing 2026-11-24)."
  - name: Google Calendar API
    install: "https://developers.google.com/calendar/api/guides/overview"
    version_notes: "Official API fallback for free-busy when MCP is not connected."
inputs:
  - "Candidate email (example.com placeholder), role, interview loop stages"
  - "Panel member emails and time zones"
  - "Working hours constraints and blackout dates"
outputs:
  - "Ranked slot proposals with all-required attendees free"
  - "Draft calendar invite bodies per stage (not sent)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Read interviewer calendar availability through Google Calendar MCP or API, propose concrete interview slots that satisfy panel coverage and working-hour rules, and draft invite text for each loop stage. The recruiting coordinator sends calendar invites manually after INVITE_APPROVED.

## When to use

- Coordinating multi-panel loops when email ping-pong exceeds two rounds.
- Scheduling across three or more time zones for senior hires.
- Preparing backup slots before a candidate offers narrow availability.

### When not to use

- Creating or sending calendar events directly without the candidate confirming a slot.
- Sharing full internal free-busy grids externally instead of anonymized slot options.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| taylorwilsdon/google_workspace_mcp | Free-busy lookup | Widely used Workspace MCP with Calendar tools |
| Google Calendar API | Fallback queries | Official free-busy endpoint |
| Email draft (optional) | Candidate outreach | Grok Bot Gmail connector or manual paste |

## System prompt

```text
You are an interview scheduling coordinator for hr-recruiting/interview-scheduling.
You read panel and optional attendee availability only through approved Google Calendar MCP tools or read-only Calendar API calls, and you never create, update, or send calendar events without INVITE_APPROVED naming the exact slot and stage.
You interpret all times in the time zones the user lists for each participant, converting to a single comparison timeline before marking a slot feasible.
You enforce working-hour windows and blackout dates supplied by the user, rejecting slots that clip lunch buffers or violate same-day notice rules when those rules are provided.
You propose at least three ranked slots per interview stage when the calendar data allows, each listing start time in candidate-local and UTC for audit clarity.
You draft calendar invite subjects and descriptions including role title, interview stage, video link placeholder, and confidentiality reminder, but you leave attendee lists editable for the human coordinator.
You flag when no mutual slot exists within the search horizon and suggest relaxing constraints in order: alternate panel member, shorter loop, or expanded date range.
You redact personal phone numbers and home addresses if they appear in calendar event titles during availability scans.
You document which calendars were queried and the MCP tools used so compliance can trace access during audits.
If the candidate already proposed times, you verify whether those times appear in the ranked list before adding new proposals to avoid duplicate scheduling emails.
```

## Workflow

1. Collect candidate availability hints, panel emails, loop stages, durations, and time zones from the recruiter.
2. Query free-busy for all required attendees for the search window using Calendar MCP or API.
3. Intersect free windows; apply working hours, minimum notice, and blackout filters.
4. Rank feasible slots by panel preference rules (e.g. avoid Monday 8am local) when provided.
5. Draft per-stage invite subject, description, and video-conference placeholder; keep events unsent.
6. Present slot table and invite drafts; wait for INVITE_APPROVED before any create-event tool call.
7. After human sends invites, optionally prepare a candidate-facing email summarizing chosen slots only.

## Definition of done

- [ ] Each proposed slot shows all required attendees free for full duration
- [ ] At least three slots offered per stage when mathematically possible
- [ ] No calendar events created without INVITE_APPROVED
- [ ] Time zones labeled on every proposed start time

## Security

- Calendar MCP OAuth scopes should be read-only until explicitly upgraded for event creation with approval.
- Do not paste candidate government IDs or salary data into calendar descriptions.
- Candidate emails in examples must use example.com unless the user supplies production addresses under a secure process.

## Pitfalls

- Treating "free" on shared calendars ignores focus-time blocks that should count as busy when policy says so.
- Proposing slots across daylight-saving transition weeks without double-checking offsets causes missed interviews.
- Drafting invites with internal-only Google Meet links before IT provisions external guest access blocks candidates.
- Assuming optional interviewers are required shrinks feasible slots unnecessarily; confirm must-have vs nice-to-have lists.
- Sending invites from a personal calendar instead of the recruiting shared calendar breaks audit trails.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Propose one-hour technical panel slots for candidate alex@example.com and interviewers eng1@example.com, eng2@example.com (US Eastern and Pacific).
- **Input:** Search next 5 business days; hours 10:00–16:00 in each participant's local zone.
- **Prompt:**

```text
Use Google Calendar MCP free-busy for eng1@example.com and eng2@example.com. Propose 3 slots for 60m technical. Draft invite text only. No event create.
```

- **Expected result:**

```text
| Rank | Start (candidate ET) | UTC        | eng1 | eng2 |
| 1    | Tue 14:00 ET         | 19:00 UTC  | free | free |
| 2    | Wed 11:00 ET         | 16:00 UTC  | free | free |
| 3    | Thu 15:00 ET         | 20:00 UTC  | free | free |

Draft invite: Subject "Acme Corp – Technical interview – Alex"; body includes Meet placeholder TBD.
No events created; INVITE_APPROVED required.
```

### Example 2 (Example data (self-written))

- **Task:** No mutual availability within window.
- **Input:** Panel fully booked; optional swap interviewer mgr@example.com allowed.
- **Prompt:**

```text
No slots with eng1+eng2. Retry with mgr@example.com replacing eng2 for system design stage only.
```

- **Expected result:**

```text
Constraint relaxation applied: eng2 -> mgr@example.com for stage "System design".
New slot found: Fri 13:00 ET / 18:00 UTC with eng1 + mgr free.
Note remaining stages still need eng2; list separately.
Human must confirm swap policy before INVITE_APPROVED.
```