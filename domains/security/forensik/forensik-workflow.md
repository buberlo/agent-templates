---
id: forensik-workflow
title: "Forensik (nur autorisiert)"
domain: security
category: forensik
tags:
  - forensik
  - security
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: terminal
    install: "Shell des Agenten"
    version_notes: "Domain-Default laut Recherche"
inputs:
  - "Kontext/Briefing für Forensik (nur autorisiert)"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Hohe Flughöhe zu forensischen Werkzeugkategorien; keine Anleitungen zur Umgehung oder Ausbeutung.

> Keine Methodik, keine Umgehungsanleitungen.

## Wann nutzen

- Anfragen passen zur Kategorie **Forensik (nur autorisiert)**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: medium`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Terminal/CLI | Ausführung | Domain-Default |

## System-Prompt / Instruktionen

```text
You are a specialist for Forensik (nur autorisiert) (security/forensik).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Nur in autorisierten Verfahren durch zustaendige Stellen; hier keine Methodik.
```

## Arbeitsablauf

- Nur in autorisierten Verfahren durch zustaendige Stellen; hier keine Methodik.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Keine forensischen Angriffs- oder Umgehungsverfahren in dieser Datei.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Forensik (nur autorisiert)-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `forensik` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Forensik (nur autorisiert). Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Forensik (nur autorisiert)
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
