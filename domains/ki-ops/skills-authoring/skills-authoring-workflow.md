---
id: skills-authoring-workflow
title: "Skills authoring"
domain: ki-ops
category: skills-authoring
tags:
  - skills
  - ki-ops
  - standardbeispiele
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Agent Skills Standard / Anthropic skills repo
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: OpenClaw Skill Workshop
    install: "https://docs.openclaw.ai/skills/"
    version_notes: "395081 GitHub Stars"
inputs:
  - "Kontext/Briefing für Skills authoring"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

SKILL.md nach Agent-Skills-Standard schreiben, testen und veröffentlichen.

## Wann nutzen

- Anfragen passen zur Kategorie **Skills authoring**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Agent Skills Standard / Anthropic skills | Standard + Beispiele | Aus Recherche 2026-11-23 |
| OpenClaw Skill Workshop | Plattform-Feature | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Skills authoring (ki-ops/skills-authoring).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Kurze description (OpenClaw rechnet ca. 24 Tokens plus Felder je Skill). Body erst laden wenn noetig.
```

## Arbeitsablauf

- Kurze description (OpenClaw rechnet ca. 24 Tokens plus Felder je Skill). Body erst laden wenn noetig.
- Workshop: create → evaluate → apply, nie still auf SKILL.md schreiben lassen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- Zu lange Descriptions sprengen das Skills-Prompt-Budget.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in a

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Skills authoring-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `skills-authoring` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Skills authoring. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Skills authoring
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
