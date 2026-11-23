---
id: claude-code-workflow
title: "Claude Code"
domain: agent-platforms
category: claude-code
tags:
  - claude
  - agent-platforms
  - cliagent
target_agents:
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Claude Code
    install: "https://github.com/anthropics/claude-code"
    version_notes: "156765 GitHub Stars"
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "34686 GitHub Stars"
  - name: Context7
    install: "https://github.com/upstash/context7"
    version_notes: "65314 GitHub Stars"
inputs:
  - "Kontext/Briefing für Claude Code"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Skills, MCP, Slash-Commands, Delegation und offizielle Anthropic-Dokument-Skills.

## Wann nutzen

- Anfragen passen zur Kategorie **Claude Code**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Claude Code | CLI-Agent | Aus Recherche 2026-11-23 |
| Anthropic document skills (docx, pptx, x | Skill | Aus Recherche 2026-11-23 |
| GitHub Official MCP | MCP | Aus Recherche 2026-11-23 |
| Context7 | MCP / Plattform | Aus Recherche 2026-11-23 |
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Claude Code (agent-platforms/claude-code).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Skill liegt in ~/.claude/skills oder Projekt-.claude/skills bzw. Plugin-Marketplace.
```

## Arbeitsablauf

- Skill liegt in ~/.claude/skills oder Projekt-.claude/skills bzw. Plugin-Marketplace.
- MCP nur wenn sonst Daten aus anderen Tools kopiert wuerden (offizielle Empfehlungslogik).

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- MCP-Server mit externem Content: Prompt-Injection-Risiko (Claude-Code-Docs-Warnung).
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Claude Code-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `claude-code` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Claude Code. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Claude Code
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

- **Aufgabe:** Mit Claude Code und der offiziellen Anthropic-docx-Skill ein Briefing-Dokument erzeugen und validieren.
- **Input:** Inhaltliches Briefing (Titel, zwei H1, Listen, Preistabelle) im Tutorial des Autors.
- **Prompt:**
```text
Claude Code Plugin document-skills@anthropic-agent-skills, npm-Paket docx 9.15.3, skills/docx/scripts/office/validate.py, LibreOffice-Wrapper soffice.py, pdftoppm.
```
- **Erwartetes Ergebnis:**
  Ausgabe briefing.docx mit 10.354 Bytes. Validator: 25 Absätze, All validations PASSED. Beim ersten PDF-Render lief die Tabelle über den rechten Rand (Spaltenbreiten summierten auf 11.520 DXA); nach Korrektur auf 9.360 DXA Gesamtbreite war die Context-Spalte sichtbar.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
