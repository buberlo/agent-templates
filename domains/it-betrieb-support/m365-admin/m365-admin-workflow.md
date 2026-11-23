---
id: m365-admin-workflow
title: "Microsoft 365 Admin"
domain: it-betrieb-support
category: m365-admin
tags:
  - m365
  - it-betrieb-support
  - skillcli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
  - name: Grok Bot / Connectoren wo Microsoft 365 angeboten wird
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Produktdoku."
inputs:
  - "Kontext/Briefing für Microsoft 365 Admin"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Tenants, Lizenzen, Exchange/SharePoint-Administration über Graph oder Admin-Center-Automatisierung.

## Wann nutzen

- Anfragen passen zur Kategorie **Microsoft 365 Admin**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill microsoft-office | Skill + CLI | Aus Recherche 2026-11-23 |
| Grok Bot / Connectoren wo Microsoft 365  | Plugin | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Microsoft 365 Admin (it-betrieb-support/m365-admin).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Lesen und Reporten zuerst; Lizenz- oder User-Aenderungen nie still.
```

## Arbeitsablauf

- Lesen und Reporten zuerst; Lizenz- oder User-Aenderungen nie still.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Microsoft 365 Admin-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `m365-admin` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Microsoft 365 Admin. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Microsoft 365 Admin
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
