---
id: code-review-mcp-focus
title: "Code-Review: MCP/Skill-Fokus"
domain: software-entwicklung
category: code-review
tags:
  - code
  - software-entwicklung
  - mcp
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "34686 GitHub Stars"
  - name: Hermes-Skill github / ClawHub Github
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23"
inputs:
  - "Kontext/Briefing für Code-Review"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

PRs und Diffs prüfen, Sicherheits- und Qualitätsgates anwenden.

## Wann nutzen

- Anfragen passen zur Kategorie **Code-Review**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub Official MCP | MCP | Aus Recherche 2026-11-23 |
| Hermes-Skill github / ClawHub Github | Skill + CLI | Aus Recherche 2026-11-23 |
| semgrep MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| Hermes-Skill requesting-code-review | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Code-Review (software-entwicklung/code-review).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Claude-Code-Docs enthalten den illustrativen Prompt Review PR #456 and suggest improvements (kein gemessenes Praxiserg
```

## Arbeitsablauf

- Claude-Code-Docs enthalten den illustrativen Prompt Review PR #456 and suggest improvements (kein gemessenes Praxisergebnis).

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Code-Review-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `code-review` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Code-Review. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Code-Review
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
