---
id: mcp-server-bau-workflow
title: "MCP-Server bauen"
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
  - name: MCP TypeScript/Python SDK
    install: "https://github.com/modelcontextprotocol/sdk"
    version_notes: "stdio transport default"
  - name: modelcontextprotocol/servers
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "Referenzmuster"
inputs:
  - "API oder Datenquelle, gewünschte Tools"
  - "Auth-Muster (env, OAuth)"
outputs:
  - "MCP-Server Repo-Skeleton"
  - "mcp.json Client-Config"
  - "Tool-Schema-Review"
risk_level: medium
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Eigenen MCP-Server** bauen: stdio, klare Tool-Schemas, Secrets aus argv fernhalten — an modelcontextprotocol/servers orientiert.

## Wann nutzen

- Interne API soll agentenfähig werden.
- Wrapper um CLI mit strukturierten Tools.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| @modelcontextprotocol/sdk | Implementierung | Offiziell |
| Referenzserver | Muster | filesystem, fetch |
| mcp-inspector | Debug | Lokal testen |

## System-Prompt / Instruktionen

```text
Role: MCP server engineer (ki-ops/mcp-server-bau).
Mission: Ship minimal read-only server first; no secrets in argv or tool descriptions.

Scaffold ts: npm create from sdk sample or clone pattern from servers repo fetch filesystem.
Tools: one tool one responsibility; json schema input strict additionalProperties false.
stdio only unless user needs sse document threat model for remote.
Auth: read API_KEY from env in server bootstrap never from mcp client config args list.
Logging: stderr only; never log secrets or full responses with pii.
Errors: mcp spec structured error messages user-facing safe.
Version: semver server package; pin in client mcp.json command npx package@version.
Testing: mcp-inspector or claude desktop config local before hermes publish.
Rate limit: exponential backoff on upstream http 429 in tool impl.
Timeouts: axios fetch 30s default document override.
Write tools: suffix _write require confirmation string param user_ack boolean default false.
README: install run env vars table no real keys.
Publish: optional npm; internal git url for enterprise.
Compliance: grok wiki rule no credentials in command argv for custom mcps cite in readme.
Handoff security review before prod connector deploy.
```

## Arbeitsablauf

1. Datenquelle und read/write-Klassen listen.
2. Tools als JSON-Schema skizzieren.
3. SDK-Skeleton (TS/Python) anlegen.
4. Erste read-only Tools implementieren.
5. Lokaler Test mit Inspector/Client-Config.
6. Write-Tools mit user_ack absichern.
7. README und env-Var-Doku ohne Secrets.

## Qualitätskriterien / Definition of Done

- [ ] stdio server startet in Client
- [ ] Keine Secrets in argv
- [ ] Tool-Schemas validieren
- [ ] Inspector-/Smoke-Test protokolliert

## Sicherheit & Freigaben

- Prod-Connector erst nach Security-Review.
- OAuth nur über unterstützten Flow.

## Fallstricke

- Riesige Tool-Descriptions → Token-Overhead.
- Generisches `execute` Tool → Prompt-Injection.
- Stderr voller PII.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Tickets read-only
- **Input:** REST /tickets
- **Prompt:**

```text
MCP tools list_tickets get_ticket env TICKET_API_KEY.
```

- **Erwartetes Ergebnis:**

```text
server starts | two tools | mcp.json snippet
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Passwort in config
- **Input:** args -p secret123
- **Prompt:**

```text
Quick mcp.json command line password.
```

- **Erwartetes Ergebnis:**

```text
reject argv secret | use env var pattern
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** mcp-builder skill
- **Input:** awesome-claude-skills
- **Prompt:**

```text
Follow community skill checklist for new server.
```

- **Erwartetes Ergebnis:** README checklist themes: schemas, auth, testing; Quelle awesome-claude-skills.