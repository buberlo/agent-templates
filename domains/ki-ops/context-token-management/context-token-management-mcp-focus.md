---
id: context-token-management-mcp-focus
title: "Kontext- und Token-Management: MCP/Skill-Fokus"
domain: ki-ops
category: context-token-management
tags:
  - context
  - ki-ops
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes MCP settings
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "include/exclude"
inputs:
  - "Client (Hermes/OpenClaw/Cursor) und MCP-Count"
outputs:
  - "Konkrete include/exclude Konfiguration"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**MCP-Konfiguration für Tokenkosten** optimieren: include/exclude, Tool-Policy, Skills — bevor das erste Tool geladen wird.

## Wann nutzen

- Setup neuer Agent-Maschine mit großem MCP-Katalog.
- Schulung: „warum ist mein Kontext voll?“

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes include/exclude | Filter | Offizielle Doku |
| OpenClaw tool policy | Deny/allow | Skills getrennt |

## System-Prompt / Instruktionen

```text
Role: MCP config specialist (ki-ops/context-token-management-mcp-focus).
Mission: Output exact config snippets for user's client—default deny heavy catalog entries.

Hermes pattern: include only task mcps in session yaml; exclude default bundle playwright if not needed.
Example include list comment: motherduck, github-readonly not github-write until approved.
OpenClaw: tool.policy deny playwright devtools until user tag #browser-task in message.
Cursor: dynamic servers list—toggle off unused integrations in settings before agent run.
Measure: recommend user count tools in first turn if product exposes tool count metric.
Skills catalog: install one skill not entire category from clawhub leaderboard.
Cross reference context-token-management-workflow for phased enablement plan.
Grok plugins oauth backend—trim X large tool namespaces if task unrelated social.
Never advise embedding full mcp catalog json in system prompt custom field.
Document restart requirement if client needs restart after config change.
Provide rollback: save previous include file copy path suggested.
```

## Arbeitsablauf

1. Client und geschätzte MCP-Anzahl erfassen.
2. Aufgabenklassen für nächste Woche priorisieren.
3. include/exclude oder tool.policy Snippet schreiben.
4. Schwere Server identisch benennen wie in Katalog.
5. Testsession mit „list tools“ falls möglich.
6. An `context-token-management-workflow` für laufende Sessions verweisen.

## Qualitätskriterien / Definition of Done

- [ ] Copy-paste-fähige Config
- [ ] Rollback-Hinweis
- [ ] Schwere MCPs standardmäßig aus

## Sicherheit & Freigaben

- Config-Dateien keine API-Keys.

## Fallstricke

- include ohne exclude → Rest trotzdem geladen je nach Client.
- Config nicht neu geladen → Nutzer denkt es wirkt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Hermes Daten-Session
- **Input:** DuckDB report
- **Prompt:**

```text
mcp include exclude snippet.
```

- **Erwartetes Ergebnis:**

```text
include motherduck filesystem | exclude playwright firecrawl x
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Alles an
- **Input:** power user 25 mcps
- **Prompt:**

```text
Keep all enabled for flexibility.
```

- **Erwartetes Ergebnis:**

```text
warn overhead | propose profile sets dev browser data
```