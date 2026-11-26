---
id: calendar-scheduling-mcp-focus
title: "Calendar and scheduling: MCP/skill focus"
domain: communication
category: calendar-scheduling
tags:
  - kalender
  - communication
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
  - name: calendly MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Kalender-Backends (Google, Calendly, Outlook)"
  - "Schreib-Rechte ja/nein"
outputs:
  - "Activation plan for calendar tools"
  - "Free/busy Smoke-Test"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Choose Calendar Connections Clean: gws vs. Calendly MCP vs. Grok Plugin Write privileges, time zone defaults and minimum MCP set.

## When to use

- Agent setup for scheduling; Multiple calendar options in the catalog.
- Read-only availability check before production invitations.
Documentation for Ops/Security (which tokens, which scopes).

**When not to use**

Concrete meeting invitation with participants → `calendar-scheduling-workflow`.
- Outlook without angebundenen MCP/Skill.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| gws calendar | Google Workspace | CLI + bundled Skill |
| Calendly MCP | Externe Buchung | Hermes optional-mcps |
| Grok Google Calendar | OAuth in chat | Quick free/busy test |

## System prompt

```text
You configure calendar tooling for communication/calendar-scheduling.

Inputs: primary_backend (google | calendly | grok_plugin), write_allowed bool, default_tz, hermes mcp list, credentials location.

Deliver calendar-tooling.md:
- Chosen read tool and optional write tool (only if write_allowed)
- Install: hermes mcp install calendly OR gws auth status command
- Scopes documented (calendar.readonly vs calendar.events)
- Smoke test: list next 2 events on primary calendar, titles only
- Disable events.insert and calendly cancel if write_allowed=false

Conflict policy: if multiple backends, designate single source of truth for creates.

Never paste refresh tokens. Note Europe/Vienna as display default.
```

## Workflow

1. Inventory backends (Google primary? Calendly public?).
2. Write-right policy (`write allowed`).
3. Check hermes mcp install or gws auth login status.
4. Smoke test: next 2 events list (title, start, TZ).
5. Remove write tools from session when read-only.
6. `output/calendar-tooling.md` with scopes and commands.
7. User confirmed before scheduling workflow.

## Definition of done

- [ ] Source of truth named for Creates
Smoke test successful or error with remediation
- [ ] Default-Zeitzone dokumentiert
- [ ] Write-Tools gated

## Security

enested in the gaunting in the en-a-reichen in Plus in the f  traders in the a possible in the gaunting in the gaunting in the gaunting in the gaunting in the
- Calendly API keys not in Git.
- Grok plugin inherits user permissions—no escalation.

## Pitfalls

- gws without Workspace-Admin → falsche Kalender-ID.
- Calendly MCP active, but Google for Creates → double events.
- Readonly-Scope, aber Workflow versucht insert → opaque 403.
- TZ not set in gws config.
- Vergessene Calendly-Webhook vs. manuelle Slots.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Read-only Google.
- **Input:** `write_allowed=false`, gws.
- **Prompt:**

```text
Configure calendar tools read-only, smoke test next 2 events.
```

- **Expected result:**

```text
Read: gws calendar events.list
Write: disabled
Smoke: "Standup" 2026-11-24T09:00+01:00; "1:1" 2026-11-24T14:00+01:00
File: output/calendar-tooling.md
```

### Example 2 (Example data (self-written))
- **Task:** Write to Calendly + Google.
- **Input:** Public booking + internal calendar.
- **Prompt:**

```text
Document dual backend: Calendly for external, gws for internal creates.
```

- **Expected result:**

```text
Source of truth creates: gws (internal), Calendly links read-only in agent
Calendly MCP: availability only
Warning: do not events.insert on behalf of Calendly bookings
```