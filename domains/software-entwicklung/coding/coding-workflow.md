---
id: coding-workflow
title: "Coding"
domain: software-entwicklung
category: coding
tags:
  - coding
  - software-entwicklung
  - mcpplattform
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Context7
    install: "https://github.com/upstash/context7"
    version_notes: "65314 GitHub Stars"
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "34686 GitHub Stars"
  - name: Hermes-Skill github / ClawHub Github
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23"
  - name: Hermes-Skills claude-code und codex
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Kontext/Briefing für Coding"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Features implementieren, Bugs fixen, Code in Repositories ändern.

## Wann nutzen

- Anfragen passen zur Kategorie **Coding**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Context7 | MCP / Plattform | Aus Recherche 2026-11-23 |
| GitHub Official MCP | MCP | Aus Recherche 2026-11-23 |
| Hermes-Skill github / ClawHub Github | Skill + CLI | Aus Recherche 2026-11-23 |
| Hermes-Skills claude-code und codex | Skill (Delegation) | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Coding (software-entwicklung/coding).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Community-Default-Stack in Posts: Context7, GitHub MCP, Playwright MCP, Chrome DevTools MCP, oft plus Sentry.
```

## Arbeitsablauf

- Community-Default-Stack in Posts: Context7, GitHub MCP, Playwright MCP, Chrome DevTools MCP, oft plus Sentry.
- Feature, Akzeptanzkriterien, Testdatei zuerst (Hermes TDD-Skill).

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Veraltete APIs ohne Context7/Docs-MCP.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen eine

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Coding-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `coding` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Coding. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Coding
- **Input:** Unvollständige oder ungültige Eingabe
- **Prompt:**
```text
Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.
```
- **Erwartetes Ergebnis:**
| Feld | Status |
|------|--------|
| input | fehlt |
| Aktion | keine Ausführung |
