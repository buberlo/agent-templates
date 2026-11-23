---
id: compliance-nis2-dsgvo-mcp-focus
title: "Compliance, NIS2 und DSGVO: MCP/Skill-Fokus"
domain: security
category: compliance-nis2-dsgvo
tags:
  - compliance
  - security
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Kontext/Briefing für Compliance, NIS2 und DSGVO"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Anforderungen, TOMs, AVVs und Nachweise strukturieren (keine Rechtsberatung).

## Wann nutzen

- Anfragen passen zur Kategorie **Compliance, NIS2 und DSGVO**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: medium`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, x | Skill | Aus Recherche 2026-11-23 |
| Hermes-Skill microsoft-office | Skill + CLI | Aus Recherche 2026-11-23 |
| Notion MCP (hosted) | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Compliance, NIS2 und DSGVO (security/compliance-nis2-dsgvo).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Ist-Zustand dokumentieren, Luecken als Fragen an Fachleute, Nachweise versionieren.
```

## Arbeitsablauf

- Ist-Zustand dokumentieren, Luecken als Fragen an Fachleute, Nachweise versionieren.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Ein Agent ist kein Datenschutzbeauftragter und keine Kanzlei.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Compliance, NIS2 und DSGVO-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `compliance-nis2-dsgvo` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Compliance, NIS2 und DSGVO. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Compliance, NIS2 und DSGVO
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
