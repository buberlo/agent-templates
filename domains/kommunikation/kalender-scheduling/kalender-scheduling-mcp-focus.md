---
id: kalender-scheduling-mcp-focus
title: "Kalender und Scheduling: MCP/Skill-Fokus"
domain: kommunikation
category: kalender-scheduling
tags:
  - kalender
  - kommunikation
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
  - name: calendly MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kalender-Backends (Google, Calendly, Outlook)"
  - "Schreib-Rechte ja/nein"
outputs:
  - "Aktivierungsplan für Kalender-Tools"
  - "Free/busy Smoke-Test"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Kalender-Anbindungen sauber wählen**: gws vs. Calendly MCP vs. Grok Plugin—inkl. Schreib-Rechten, Zeitzonen-Defaults und minimalem MCP-Set.

## Wann nutzen

- Agent-Setup für Scheduling; mehrere Kalender-Optionen im Katalog.
- Read-only Availability-Check vor Produktiv-Einladungen.
- Dokumentation für Ops/Security (welche Tokens, welche Scopes).

**Wann nicht**

- Konkrete Meeting-Einladung mit Teilnehmern → `kalender-scheduling-workflow`.
- Outlook ohne angebundenen MCP/Skill.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| gws calendar | Google Workspace | CLI + bundled Skill |
| Calendly MCP | Externe Buchung | Hermes optional-mcps |
| Grok Google Calendar | OAuth im Chat | Schnelltest Free/Busy |

## System-Prompt / Instruktionen

```text
You configure calendar tooling for kommunikation/kalender-scheduling.

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

## Arbeitsablauf

1. Backends inventarisieren (Google primär? Calendly öffentlich?).
2. Schreib-Recht policy klären (`write_allowed`).
3. `hermes mcp install` bzw. `gws auth login` Status prüfen.
4. Smoke-Test: nächste 2 Events listen (Titel, Start, TZ).
5. Schreib-Tools aus Session entfernen wenn read-only.
6. `output/calendar-tooling.md` mit Scopes und Befehlen.
7. Nutzer bestätigt vor Scheduling-Workflow.

## Qualitätskriterien / Definition of Done

- [ ] Source of truth für Creates benannt
- [ ] Smoke-Test erfolgreich oder Fehler mit Remediation
- [ ] Default-Zeitzone dokumentiert
- [ ] Write-Tools gated

## Sicherheit & Freigaben

- OAuth nur über offizielle Flows.
- Calendly API-Keys nicht in Git.
- Grok-Plugin erbt Nutzerrechte—keine Eskalation.

## Fallstricke

- gws ohne Workspace-Admin → falsche Kalender-ID.
- Calendly MCP aktiv, aber Google für Creates → doppelte Events.
- Readonly-Scope, aber Workflow versucht insert → opaque 403.
- TZ nicht gesetzt in gws Config.
- Vergessene Calendly-Webhook vs. manuelle Slots.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Read-only Google.
- **Input:** `write_allowed=false`, gws.
- **Prompt:**

```text
Configure calendar tools read-only, smoke test next 2 events.
```

- **Erwartetes Ergebnis:**

```text
Read: gws calendar events.list
Write: disabled
Smoke: "Standup" 2026-11-24T09:00+01:00; "1:1" 2026-11-24T14:00+01:00
File: output/calendar-tooling.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Calendly + Google schreiben.
- **Input:** Public booking + internal calendar.
- **Prompt:**

```text
Document dual backend: Calendly for external, gws for internal creates.
```

- **Erwartetes Ergebnis:**

```text
Source of truth creates: gws (internal), Calendly links read-only in agent
Calendly MCP: availability only
Warning: do not events.insert on behalf of Calendly bookings
```