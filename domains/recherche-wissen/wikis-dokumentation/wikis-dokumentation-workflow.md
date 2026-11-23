---
id: wikis-dokumentation-workflow
title: "Wikis und Dokumentation"
domain: recherche-wissen
category: wikis-dokumentation
tags:
  - wikis
  - recherche-wissen
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: deepwiki MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Notion MCP (hosted)
    install: "https://mcp.notion.com/mcp"
    version_notes: "Im offiziellen Hermes-MCP-Katalog (optional-mcps/notion)."
  - name: Obsidian-Skills (Hermes bundled, ClawHub steipete)
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "381 GitHub Stars"
inputs:
  - "Kontext/Briefing für Wikis und Dokumentation"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Interne Wikis, DeepWiki, Docs-Sites und Wissensräume pflegen und abfragen.

## Wann nutzen

- Anfragen passen zur Kategorie **Wikis und Dokumentation**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| deepwiki MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| Notion MCP (hosted) | MCP | Aus Recherche 2026-11-23 |
| Obsidian-Skills (Hermes bundled, ClawHub | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Wikis und Dokumentation (recherche-wissen/wikis-dokumentation).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Repo-Fragen ueber DeepWiki, interne Docs ueber Vault/Notion.
```

## Arbeitsablauf

- Repo-Fragen ueber DeepWiki, interne Docs ueber Vault/Notion.

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

- **Aufgabe:** Standard-Wikis und Dokumentation-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `wikis-dokumentation` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Wikis und Dokumentation. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Wikis und Dokumentation
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
