---
id: context-token-management-workflow
title: "Context- und Token-Management"
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
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "40040 GitHub Stars"
  - name: Context7
    install: "https://github.com/upstash/context7"
    version_notes: "65314 GitHub Stars"
  - name: Hermes tools.include / exclude und MCP-Filter
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "Produktdoku."
inputs:
  - "Kontext/Briefing für Context- und Token-Management"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Tool-Schema-Overhead, Lazy Loading, CLI statt fetter MCPs, Prompt-Budgets.

## Wann nutzen

- Anfragen passen zur Kategorie **Context- und Token-Management**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |
| Context7 | MCP / Plattform | Aus Recherche 2026-11-23 |
| Hermes tools.include / exclude und MCP-F | Config | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Context- und Token-Management (ki-ops/context-token-management).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Baseline-Tokenverbrauch ohne Frage messen, dann Server abschalten bis der Stack tragbar ist.
```

## Arbeitsablauf

- Baseline-Tokenverbrauch ohne Frage messen, dann Server abschalten bis der Stack tragbar ist.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Context- und Token-Management-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `context-token-management` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Context- und Token-Management. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Context- und Token-Management
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

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Messen, wie viele Tokens bereits geladene MCP-Server verbrauchen, bevor eine Frage gestellt wird.
- **Input:** Der bestehende MCP-Stack des Autors in Claude. Die genaue Serverliste im First Post konnte in dieser Recherche nicht vollstaendig geladen werden (Reddit-Seite weitgehend ohne Beitragstext).
- **Prompt:**
```text
Mehrere gleichzeitig aktivierte MCP-Server in einem Claude-Setup.
```
- **Erwartetes Ergebnis:**
  Threadtitel und Suche geben die Messung mit 67.000 Tokens Overhead an, bevor die erste Frage eingegeben wurde.
- **Quelle:** https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
