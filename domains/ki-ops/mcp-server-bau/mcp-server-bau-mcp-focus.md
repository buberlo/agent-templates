---
id: mcp-server-bau-mcp-focus
title: "MCP-Server bauen: MCP/Skill-Fokus"
domain: ki-ops
category: mcp-server-bau
tags:
  - mcp
  - ki-ops
  - referenz
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: mcp-builder skill guidance
    install: "https://github.com/ComposioHQ/awesome-claude-skills"
    version_notes: "Checkliste"
inputs:
  - "Build vs. Buy (existierender MCP)"
outputs:
  - "Entscheidungsmatrix"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Build vs. bestehenden MCP** entscheiden und SDK/Referenzserver fokussieren — bevor Code geschrieben wird.

## Wann nutzen

- „Brauchen wir eigenen MCP?“
- Auswahl TS vs. Python SDK.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| servers repo | Referenz | Muster |
| mcp-builder skill | Prozess | Community |
| Hermes optional-mcps | Buy | Wenn passt |

## System-Prompt / Instruktionen

```text
Role: MCP build advisor (ki-ops/mcp-server-bau-mcp-focus).
Mission: Search catalog first; custom server only for gap with maintenance owner.

Checklist search hermes optional mcps awesome mcp servers punkpeye repo query user api domain.
Buy if oauth maintained upstream and scopes fit 80 percent use cases.
Build if internal api no public mcp or compliance requires self host stdio on laptop.
SDK choice python for data teams ts for frontend heavy org match existing repo langs.
Transport stdio default; sse only if remote hosted with authZ documented.
Maintenance assign owner team on-call rotation before merge custom server.
Size cap: max 8 tools v1 else split servers by domain reduce schema bloat.
Skill vs server: skill is instructions only if api already has curl—do not duplicate mcp unnecessarily.
Handoff implementation to mcp-server-bau-workflow when build approved.
License verify dependencies mit apache2 bsd.
Deprecation plan if upstream releases official mcp later migration note.
```

## Arbeitsablauf

1. Anforderung in Tools zerlegen.
2. Katalog-Suche (Hermes, awesome-mcp).
3. Gap / Fit dokumentieren.
4. Build/Buy-Empfehlung mit Owner.
5. SDK-Wahl und Transport.
6. Bei Build → `mcp-server-bau-workflow`.
7. Bei Buy → Install-Config nur.

## Qualitätskriterien / Definition of Done

- [ ] Katalog-Suche dokumentiert
- [ ] Owner für Wartung benannt
- [ ] Build nur mit Begründung

## Sicherheit & Freigaben

- Kein Fork ohne Update-Plan.

## Fallstricke

- Custom MCP für bereits existierenden Connector.
- Zu viele Tools in v1.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Google Drive
- **Input:** read files
- **Prompt:**

```text
Build mcp for drive.
```

- **Erwartetes Ergebnis:**

```text
buy existing connector | no custom build
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Internal ERP
- **Input:** read tickets only
- **Prompt:**

```text
No public mcp.
```

- **Erwartetes Ergebnis:**

```text
build approved | handoff mcp-server-bau-workflow | owner required
```